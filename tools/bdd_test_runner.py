#!/usr/bin/env python3
"""
Tool: BDD Test Runner
Created: March 2024
Author: Development Team
Status: Active
Purpose: Primary test runner for BDD tests with parallel execution, performance metrics, and detailed reporting
Dependencies: behave, pytest
Lifecycle:
    - Created: Enhanced test runner to replace basic run_bdd_tests.py
    - Active: Currently used in CI/CD pipeline and local development
    - Obsolescence Conditions:
        1. If replaced by a more comprehensive test runner
        2. If BDD testing approach is fundamentally changed
        3. If project moves away from BDD methodology
Last Validated: 2024-03-21

Enhanced test runner for BDD features supporting:
- Parallel execution
- Performance metrics
- Detailed reporting
- Test result aggregation
"""

import argparse
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml
from jinja2 import Environment, FileSystemLoader


@dataclass
class TestResult:
    """Test execution result."""

    feature: str
    scenario: str
    status: str  # passed, failed, skipped, error
    duration: float
    error_message: Optional[str] = None
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    step_results: List[Dict[str, str]] = None


@dataclass
class PerformanceMetrics:
    """Performance metrics for a test run."""

    total_duration: float
    avg_scenario_duration: float
    slowest_scenarios: List[Tuple[str, float]]
    fastest_scenarios: List[Tuple[str, float]]
    step_timing: Dict[str, float]
    resource_usage: Dict[str, float]


class BDDTestRunner:
    """Enhanced BDD test runner."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.features_dir = base_dir / "tests/bdd/features"
        self.results_dir = base_dir / "test_results/bdd"
        self.template_dir = base_dir / "tools/templates"

        # Initialize Jinja2 for report generation
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Ensure directories exist
        self.results_dir.mkdir(parents=True, exist_ok=True)

        # Test results
        self.results: List[TestResult] = []
        self.performance: Optional[PerformanceMetrics] = None

        # Run configuration
        self.parallel = True
        self.max_workers = None  # None = CPU count
        self.tags: List[str] = []
        self.exclude_tags: List[str] = []
        self.fail_fast = False
        self.rerun_failed = True
        self.capture_stdout = True

    def discover_features(self) -> List[Path]:
        """Discover feature files to test."""
        features = list(self.features_dir.rglob("*.feature"))
        if not features:
            raise ValueError(f"No feature files found in {self.features_dir}")
        return features

    def filter_features(self, features: List[Path]) -> List[Path]:
        """Filter features based on tags."""
        if not (self.tags or self.exclude_tags):
            return features

        filtered = []
        for feature in features:
            content = feature.read_text()
            feature_tags = set()
            for line in content.split("\n"):
                if line.strip().startswith("@"):
                    feature_tags.update(
                        tag.strip() for tag in line.strip().split("@")[1:]
                    )

            # Check if feature should be included
            if self.tags and not any(tag in feature_tags for tag in self.tags):
                continue
            if self.exclude_tags and any(
                tag in feature_tags for tag in self.exclude_tags
            ):
                continue
            filtered.append(feature)

        return filtered

    def run_feature(self, feature: Path) -> List[TestResult]:
        """Run a single feature file."""
        start_time = time.time()
        results = []

        try:
            # Run behave for the feature
            cmd = ["behave", str(feature)]
            if self.tags:
                cmd.extend(["--tags", ",".join(self.tags)])
            if self.exclude_tags:
                cmd.extend(["--tags-not", ",".join(self.exclude_tags)])

            # Add format for JSON output
            json_output = self.results_dir / f"{feature.stem}_results.json"
            cmd.extend(["--format", "json", "--outfile", str(json_output)])

            # Run the test
            process = subprocess.run(
                cmd,
                capture_output=self.capture_stdout,
                text=True,
                cwd=self.base_dir,
            )

            # Parse results
            if json_output.exists():
                with open(json_output) as f:
                    feature_results = json.load(f)

                for scenario in feature_results.get("elements", []):
                    if scenario["type"] != "scenario":
                        continue

                    # Calculate duration
                    duration = sum(
                        float(step.get("result", {}).get("duration", 0))
                        for step in scenario.get("steps", [])
                    )

                    # Get step results
                    step_results = []
                    for step in scenario.get("steps", []):
                        result = step.get("result", {})
                        step_results.append(
                            {
                                "step": step["name"],
                                "status": result.get("status", "unknown"),
                                "duration": result.get("duration", 0),
                                "error_message": result.get("error_message"),
                            }
                        )

                    # Create test result
                    results.append(
                        TestResult(
                            feature=feature.stem,
                            scenario=scenario["name"],
                            status=scenario.get("status", "unknown"),
                            duration=duration,
                            error_message=None,
                            stdout=(
                                process.stdout if self.capture_stdout else None
                            ),
                            stderr=(
                                process.stderr if self.capture_stdout else None
                            ),
                            step_results=step_results,
                        )
                    )

        except Exception as e:
            # Handle execution errors
            results.append(
                TestResult(
                    feature=feature.stem,
                    scenario="<execution error>",
                    status="error",
                    duration=time.time() - start_time,
                    error_message=str(e),
                )
            )

        return results

    def run_tests(self) -> None:
        """Run all tests with configured options."""
        start_time = time.time()

        # Discover and filter features
        features = self.discover_features()
        features = self.filter_features(features)

        if not features:
            print("No features to test after filtering")
            return

        # Run features
        if self.parallel:
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_feature = {
                    executor.submit(self.run_feature, feature): feature
                    for feature in features
                }

                for future in as_completed(future_to_feature):
                    feature = future_to_feature[future]
                    try:
                        results = future.result()
                        self.results.extend(results)

                        # Check for fail fast
                        if self.fail_fast and any(
                            r.status == "failed" for r in results
                        ):
                            executor.shutdown(wait=False)
                            break
                    except Exception as e:
                        print(f"Error running {feature}: {e}")
        else:
            for feature in features:
                results = self.run_feature(feature)
                self.results.extend(results)

                # Check for fail fast
                if self.fail_fast and any(
                    r.status == "failed" for r in results
                ):
                    break

        # Calculate performance metrics
        self.calculate_performance_metrics(time.time() - start_time)

        # Generate reports
        self.generate_reports()

        # Rerun failed tests if configured
        if self.rerun_failed and any(
            r.status == "failed" for r in self.results
        ):
            self.rerun_failed_tests()

    def calculate_performance_metrics(self, total_duration: float) -> None:
        """Calculate performance metrics for the test run."""
        if not self.results:
            return

        # Calculate scenario durations
        scenario_durations = [
            (r.feature + ":" + r.scenario, r.duration) for r in self.results
        ]
        avg_duration = sum(d for _, d in scenario_durations) / len(
            scenario_durations
        )

        # Sort by duration
        scenario_durations.sort(key=lambda x: x[1], reverse=True)

        # Calculate step timing
        step_timing = {}
        for result in self.results:
            if result.step_results:
                for step in result.step_results:
                    step_name = step["step"]
                    if step_name not in step_timing:
                        step_timing[step_name] = []
                    step_timing[step_name].append(float(step["duration"]))

        # Average step timing
        step_timing = {
            step: sum(durations) / len(durations)
            for step, durations in step_timing.items()
        }

        # Resource usage (placeholder - extend with actual metrics)
        resource_usage = {
            "cpu_percent": 0.0,
            "memory_mb": 0.0,
            "io_read_mb": 0.0,
            "io_write_mb": 0.0,
        }

        self.performance = PerformanceMetrics(
            total_duration=total_duration,
            avg_scenario_duration=avg_duration,
            slowest_scenarios=scenario_durations[:5],
            fastest_scenarios=scenario_durations[-5:],
            step_timing=step_timing,
            resource_usage=resource_usage,
        )

    def generate_reports(self) -> None:
        """Generate test reports."""
        # Generate JSON report
        report_data = {
            "summary": {
                "total": len(self.results),
                "passed": sum(1 for r in self.results if r.status == "passed"),
                "failed": sum(1 for r in self.results if r.status == "failed"),
                "error": sum(1 for r in self.results if r.status == "error"),
                "skipped": sum(
                    1 for r in self.results if r.status == "skipped"
                ),
            },
            "results": [asdict(r) for r in self.results],
            "performance": (
                asdict(self.performance) if self.performance else None
            ),
            "timestamp": datetime.now().isoformat(),
        }

        # Save JSON report
        json_report = self.results_dir / "test_report.json"
        with open(json_report, "w") as f:
            json.dump(report_data, f, indent=2)

        # Generate HTML report
        template = self.env.get_template("test_report.html.j2")
        html_report = self.results_dir / "test_report.html"
        html_report.write_text(template.render(**report_data))

        # Generate summary
        self._print_summary(report_data["summary"])

    def _print_summary(self, summary: Dict) -> None:
        """Print test summary to console."""
        print("\nTest Summary:")
        print(f"Total: {summary['total']}")
        print(f"Passed: {summary['passed']}")
        print(f"Failed: {summary['failed']}")
        print(f"Error: {summary['error']}")
        print(f"Skipped: {summary['skipped']}")

        if self.performance:
            print(f"\nPerformance:")
            print(f"Total Duration: {self.performance.total_duration:.2f}s")
            print(
                f"Average Scenario Duration: {self.performance.avg_scenario_duration:.2f}s"
            )
            print("\nSlowest Scenarios:")
            for scenario, duration in self.performance.slowest_scenarios:
                print(f"  {scenario}: {duration:.2f}s")

    def rerun_failed_tests(self) -> None:
        """Rerun failed tests."""
        failed_features = {
            Path(self.features_dir / f"{r.feature}.feature")
            for r in self.results
            if r.status in ("failed", "error")
        }

        if failed_features:
            print("\nRerunning failed tests...")
            original_results = self.results
            self.results = []

            # Run failed features sequentially
            original_parallel = self.parallel
            self.parallel = False

            for feature in failed_features:
                self.results.extend(self.run_feature(feature))

            # Restore parallel setting
            self.parallel = original_parallel

            # Update results
            passed_reruns = {
                (r.feature, r.scenario)
                for r in self.results
                if r.status == "passed"
            }

            # Keep original results for scenarios that didn't pass on rerun
            self.results.extend(
                [
                    r
                    for r in original_results
                    if (r.feature, r.scenario) not in passed_reruns
                ]
            )

            # Recalculate metrics and regenerate reports
            self.calculate_performance_metrics(self.performance.total_duration)
            self.generate_reports()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Enhanced BDD test runner")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path.cwd(),
        help="Base directory containing the project",
    )
    parser.add_argument(
        "--no-parallel", action="store_true", help="Disable parallel execution"
    )
    parser.add_argument(
        "--max-workers", type=int, help="Maximum number of parallel workers"
    )
    parser.add_argument(
        "--tags", type=str, nargs="*", help="Only run features with these tags"
    )
    parser.add_argument(
        "--exclude-tags",
        type=str,
        nargs="*",
        help="Exclude features with these tags",
    )
    parser.add_argument(
        "--fail-fast", action="store_true", help="Stop on first failure"
    )
    parser.add_argument(
        "--no-rerun-failed",
        action="store_true",
        help="Disable rerunning failed tests",
    )
    parser.add_argument(
        "--no-capture", action="store_true", help="Don't capture stdout/stderr"
    )

    args = parser.parse_args()

    runner = BDDTestRunner(args.base_dir)
    runner.parallel = not args.no_parallel
    runner.max_workers = args.max_workers
    runner.tags = args.tags or []
    runner.exclude_tags = args.exclude_tags or []
    runner.fail_fast = args.fail_fast
    runner.rerun_failed = not args.no_rerun_failed
    runner.capture_stdout = not args.no_capture

    try:
        runner.run_tests()
    except KeyboardInterrupt:
        print("\nTest run interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError running tests: {e}")
        sys.exit(2)

    # Exit with status
    if any(r.status in ("failed", "error") for r in runner.results):
        sys.exit(1)


if __name__ == "__main__":
    main()
