"""
Tool: Bdd Comprehensive Analyzer
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Analyze BDD features and scenarios for patterns and issues
Dependencies: logging, subprocess
Lifecycle:
    - Created: To support BDD testing and development workflows
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When BDD testing approach changes significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
BDD Comprehensive Analyzer

This script orchestrates all BDD analysis tools to generate a comprehensive
analysis report of BDD features, which serves as a foundation for the
consolidation strategy in Release 2 of the BDD refactoring initiative.
"""

import argparse
import datetime
import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("bdd_comprehensive_analyzer")


class BDDComprehensiveAnalyzer:
    """Orchestrates all BDD analysis tools for a comprehensive analysis."""

    def __init__(
        self,
        features_dir: str,
        steps_dir: str,
        requirements_file: Optional[str],
        output_dir: str,
        similarity_threshold: float = 0.75,
        tag_threshold: float = 0.5,
    ):
        self.features_dir = Path(features_dir)
        self.steps_dir = Path(steps_dir) if steps_dir else None
        self.requirements_file = (
            Path(requirements_file) if requirements_file else None
        )
        self.output_dir = Path(output_dir)
        self.similarity_threshold = similarity_threshold
        self.tag_threshold = tag_threshold

        # Create output directories
        self.duplication_dir = self.output_dir / "duplication"
        self.traceability_dir = self.output_dir / "traceability"
        self.coverage_dir = self.output_dir / "coverage"
        self.gap_dir = self.output_dir / "gap"
        self.summary_dir = self.output_dir / "summary"

        for directory in [
            self.output_dir,
            self.duplication_dir,
            self.traceability_dir,
            self.coverage_dir,
            self.gap_dir,
            self.summary_dir,
        ]:
            directory.mkdir(exist_ok=True, parents=True)

    def run_analysis(self):
        """Run the complete analysis pipeline."""
        logger.info("Starting comprehensive BDD analysis")

        # Step 1: Run duplication analysis
        duplication_report = self._run_duplication_analysis()

        # Step 2: Generate traceability matrix
        traceability_matrix = self._generate_traceability_matrix()

        # Step 3: Analyze coverage
        coverage_report = self._analyze_coverage()

        # Step 4: Perform gap analysis
        gap_analysis = self._perform_gap_analysis()

        # Step 5: Generate comprehensive summary
        self._generate_comprehensive_summary(
            duplication_report,
            traceability_matrix,
            coverage_report,
            gap_analysis,
        )

        logger.info(
            f"Comprehensive analysis complete. Reports available in {self.output_dir}"
        )

    def _run_duplication_analysis(self) -> Path:
        """Run the BDD duplication analyzer."""
        logger.info("Running duplication analysis")

        output_file = self.duplication_dir / "duplication_report.md"

        cmd = [
            sys.executable,
            "tools/bdd_duplication_analyzer.py",
            "--feature-dir",
            str(self.features_dir),
            "--output-file",
            str(output_file),
            "--threshold",
            str(self.similarity_threshold),
            "--tag-threshold",
            str(self.tag_threshold),
        ]

        try:
            logger.info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )
            logger.info(f"Duplication analysis completed: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Duplication analysis failed: {e.stderr}")
            raise

        # Also generate the merge plan
        merge_plan_file = self.duplication_dir / "merge_plan.md"
        cmd = [
            sys.executable,
            "tools/bdd_duplication_analyzer.py",
            "--feature-dir",
            str(self.features_dir),
            "--generate-merge-plan",
            "--output-file",
            str(merge_plan_file),
        ]

        try:
            logger.info(f"Generating merge plan: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )
            logger.info(f"Merge plan generation completed: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Merge plan generation failed: {e.stderr}")
            # Continue even if merge plan fails

        # Extract duplication statistics from the report for later use
        self._extract_duplication_stats(output_file)

        return output_file

    def _extract_duplication_stats(self, report_file: Path) -> Dict[str, int]:
        """Extract duplication statistics from the report file."""
        stats = {
            "exact_duplicates": 0,
            "semantic_duplicates": 0,
            "overlapping_features": 0,
            "tag_inconsistencies": 0,
        }

        try:
            with open(report_file, "r", encoding="utf-8") as f:
                content = f.read()

                # Look for patterns like "Found 5 exact duplicates"
                import re

                exact_match = re.search(
                    r"Found (\d+) exact duplicates", content
                )
                if exact_match:
                    stats["exact_duplicates"] = int(exact_match.group(1))

                semantic_match = re.search(
                    r"Found (\d+) semantic duplicates", content
                )
                if semantic_match:
                    stats["semantic_duplicates"] = int(semantic_match.group(1))

                overlap_match = re.search(
                    r"Found (\d+) overlapping features", content
                )
                if overlap_match:
                    stats["overlapping_features"] = int(overlap_match.group(1))

                tag_match = re.search(
                    r"Found (\d+) tag inconsistencies", content
                )
                if tag_match:
                    stats["tag_inconsistencies"] = int(tag_match.group(1))
        except Exception as e:
            logger.error(f"Failed to extract duplication stats: {e}")

        # Save stats to a JSON file
        stats_file = self.duplication_dir / "duplication_stats.json"
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

        return stats

    def _generate_traceability_matrix(self) -> Path:
        """Generate the BDD traceability matrix."""
        logger.info("Generating traceability matrix")

        output_file = self.traceability_dir / "traceability_matrix.md"

        cmd = [
            sys.executable,
            "tools/bdd_traceability_matrix.py",
            "--features-dir",
            str(self.features_dir),
        ]

        if self.steps_dir:
            cmd.extend(["--steps-dir", str(self.steps_dir)])

        cmd.extend(["--output", str(output_file)])

        try:
            logger.info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )
            logger.info(
                f"Traceability matrix generation completed: {result.stdout}"
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Traceability matrix generation failed: {e.stderr}")
            raise

        return output_file

    def _analyze_coverage(self) -> Path:
        """Analyze BDD coverage."""
        logger.info("Analyzing BDD coverage")

        output_dir = self.coverage_dir

        cmd = [
            sys.executable,
            "tools/bdd_coverage_report.py",
            "--features-dir",
            str(self.features_dir),
            "--output-dir",
            str(output_dir),
        ]

        if self.requirements_file:
            cmd.extend(["--requirements-file", str(self.requirements_file)])

        try:
            logger.info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )
            logger.info(f"Coverage analysis completed: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Coverage analysis failed: {e.stderr}")
            raise

        return output_dir / "coverage_summary.md"

    def _perform_gap_analysis(self) -> Path:
        """Perform BDD gap analysis."""
        logger.info("Performing gap analysis")

        # Gap analysis requires coverage data and requirements file
        coverage_data_file = self.coverage_dir / "coverage_detailed.json"

        # Check if coverage data exists
        if not coverage_data_file.exists():
            logger.error(f"Coverage data file not found: {coverage_data_file}")
            return Path("")

        output_dir = self.gap_dir

        cmd = [
            sys.executable,
            "tools/bdd_gap_analysis.py",
            "--coverage-data",
            str(coverage_data_file),
            "--output-dir",
            str(output_dir),
        ]

        if self.requirements_file:
            cmd.extend(["--requirements-file", str(self.requirements_file)])

        try:
            logger.info(f"Executing: {' '.join(cmd)}")
            result = subprocess.run(
                cmd, check=True, capture_output=True, text=True
            )
            logger.info(f"Gap analysis completed: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Gap analysis failed: {e.stderr}")
            # Continue even if gap analysis fails

        return output_dir / "gap_analysis.md"

    def _generate_comprehensive_summary(
        self,
        duplication_report: Path,
        traceability_matrix: Path,
        coverage_report: Path,
        gap_analysis: Path,
    ) -> Path:
        """Generate a comprehensive summary report."""
        logger.info("Generating comprehensive summary")

        output_file = self.summary_dir / "comprehensive_analysis_summary.md"

        # Load statistics
        duplication_stats = {}
        duplication_stats_file = (
            self.duplication_dir / "duplication_stats.json"
        )
        if duplication_stats_file.exists():
            with open(duplication_stats_file, "r", encoding="utf-8") as f:
                duplication_stats = json.load(f)

        # Create summary report
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# BDD Comprehensive Analysis Summary\n\n")

            # Date and time
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"**Analysis Date:** {now}\n\n")

            # Input details
            f.write("## Analysis Details\n\n")
            f.write(f"- **Features Directory:** `{self.features_dir}`\n")
            if self.steps_dir:
                f.write(f"- **Steps Directory:** `{self.steps_dir}`\n")
            if self.requirements_file:
                f.write(
                    f"- **Requirements File:** `{self.requirements_file}`\n"
                )
            f.write(
                f"- **Similarity Threshold:** {self.similarity_threshold}\n"
            )
            f.write(f"- **Tag Threshold:** {self.tag_threshold}\n\n")

            # Summary of findings
            f.write("## Summary of Findings\n\n")

            # Duplication findings
            f.write("### Duplication Analysis\n\n")
            if duplication_stats:
                f.write(
                    f"- **Exact Duplicates:** {duplication_stats.get('exact_duplicates', 0)}\n"
                )
                f.write(
                    f"- **Semantic Duplicates:** {duplication_stats.get('semantic_duplicates', 0)}\n"
                )
                f.write(
                    f"- **Overlapping Features:** {duplication_stats.get('overlapping_features', 0)}\n"
                )
                f.write(
                    f"- **Tag Inconsistencies:** {duplication_stats.get('tag_inconsistencies', 0)}\n"
                )

                total_issues = sum(duplication_stats.values())
                f.write(
                    f"\nTotal issues requiring attention: **{total_issues}**\n\n"
                )

                # Priority calculation
                if total_issues > 20:
                    priority = "High"
                elif total_issues > 10:
                    priority = "Medium"
                else:
                    priority = "Low"

                f.write(f"**Consolidation Priority:** {priority}\n\n")
            else:
                f.write("No duplication statistics available.\n\n")

            # Links to detailed reports
            f.write("## Detailed Reports\n\n")
            f.write("The following detailed reports are available:\n\n")
            f.write(
                f"1. [Duplication Report]({os.path.relpath(duplication_report, self.summary_dir)})\n"
            )
            f.write(
                f"2. [Merge Plan]({os.path.relpath(self.duplication_dir / 'merge_plan.md', self.summary_dir)})\n"
            )
            f.write(
                f"3. [Traceability Matrix]({os.path.relpath(traceability_matrix, self.summary_dir)})\n"
            )
            f.write(
                f"4. [Coverage Report]({os.path.relpath(coverage_report, self.summary_dir)})\n"
            )
            f.write(
                f"5. [Gap Analysis]({os.path.relpath(gap_analysis, self.summary_dir)})\n\n"
            )

            # Next steps for consolidation
            f.write("## Recommended Consolidation Steps\n\n")
            f.write(
                "Based on the analysis, the following consolidation steps are recommended:\n\n"
            )

            # Recommendations based on duplication stats
            if duplication_stats.get("exact_duplicates", 0) > 0:
                f.write("1. **Eliminate Exact Duplicates**\n")
                f.write(
                    "   - First priority: Remove identical scenarios while preserving requirement coverage\n"
                )
                f.write("   - Estimated effort: Low\n\n")

            if duplication_stats.get("semantic_duplicates", 0) > 0:
                f.write("2. **Consolidate Similar Scenarios**\n")
                f.write(
                    "   - Review and merge semantically similar scenarios\n"
                )
                f.write(
                    "   - Choose the most comprehensive version of each scenario\n"
                )
                f.write("   - Ensure all requirements remain covered\n")
                f.write("   - Estimated effort: Medium\n\n")

            if duplication_stats.get("overlapping_features", 0) > 0:
                f.write("3. **Reorganize Overlapping Features**\n")
                f.write(
                    "   - Restructure features with overlapping concerns\n"
                )
                f.write("   - Group scenarios according to functional areas\n")
                f.write("   - Follow the directory organization conventions\n")
                f.write("   - Estimated effort: Medium\n\n")

            if duplication_stats.get("tag_inconsistencies", 0) > 0:
                f.write("4. **Standardize Tags**\n")
                f.write(
                    "   - Apply consistent tagging patterns across all features\n"
                )
                f.write(
                    "   - Ensure requirement tags follow the @REQ-[domain]-[number] format\n"
                )
                f.write("   - Standardize component and feature tags\n")
                f.write("   - Estimated effort: Low\n\n")

            f.write("5. **Implement Directory Structure**\n")
            f.write(
                "   - Organize feature files according to the defined directory structure\n"
            )
            f.write("   - Group features by domain (CLI, API, Model, etc.)\n")
            f.write("   - Ensure step definitions follow the same structure\n")
            f.write("   - Estimated effort: Medium\n\n")

            f.write("6. **Address Coverage Gaps**\n")
            f.write("   - Review the gap analysis report for coverage gaps\n")
            f.write("   - Prioritize high-risk coverage gaps\n")
            f.write(
                "   - Create new scenarios to cover missing requirements\n"
            )
            f.write("   - Estimated effort: High\n\n")

            # Implementation plan
            f.write("## Implementation Timeline\n\n")
            f.write(
                "The following implementation timeline is recommended for the consolidation phase:\n\n"
            )

            # Week by week plan
            f.write("### Week 1: Exact Duplicates\n")
            f.write(
                "- Remove exact duplicates by implementing the merge plan\n"
            )
            f.write(
                "- Validate that all tests still pass after consolidation\n\n"
            )

            f.write("### Week 2: Similar Scenarios\n")
            f.write("- Consolidate semantically similar scenarios\n")
            f.write("- Update step definitions as needed\n\n")

            f.write("### Week 3-4: Feature Reorganization\n")
            f.write("- Implement the directory structure\n")
            f.write("- Reorganize overlapping features\n")
            f.write("- Group scenarios by functional area\n\n")

            f.write("### Week 5: Tag Standardization\n")
            f.write("- Apply consistent tagging across all features\n")
            f.write("- Validate requirement traceability\n\n")

            f.write("### Week 6: Coverage Improvement\n")
            f.write("- Address high-priority coverage gaps\n")
            f.write("- Create new scenarios for uncovered requirements\n\n")

            f.write("### Week 7-8: Validation and Documentation\n")
            f.write("- Run comprehensive tests to validate consolidation\n")
            f.write("- Update documentation\n")
            f.write("- Train team on new structure and conventions\n\n")

        logger.info(f"Comprehensive summary generated: {output_file}")

        # Generate consolidated stats file for automation
        self._generate_consolidated_stats()

        return output_file

    def _generate_consolidated_stats(self):
        """Generate a consolidated statistics file for automation."""
        stats = {
            "analysis_date": datetime.datetime.now().isoformat(),
            "features_dir": str(self.features_dir),
            "duplication": {},
            "coverage": {},
            "gap": {},
        }

        # Load duplication stats
        duplication_stats_file = (
            self.duplication_dir / "duplication_stats.json"
        )
        if duplication_stats_file.exists():
            with open(duplication_stats_file, "r", encoding="utf-8") as f:
                stats["duplication"] = json.load(f)

        # Try to extract coverage stats
        coverage_file = self.coverage_dir / "coverage_detailed.json"
        if coverage_file.exists():
            try:
                with open(coverage_file, "r", encoding="utf-8") as f:
                    coverage_data = json.load(f)
                    if "summary" in coverage_data:
                        stats["coverage"] = coverage_data["summary"]
            except Exception as e:
                logger.error(f"Failed to extract coverage stats: {e}")

        # Try to extract gap stats
        gap_file = self.gap_dir / "gap_analysis_data.json"
        if gap_file.exists():
            try:
                with open(gap_file, "r", encoding="utf-8") as f:
                    gap_data = json.load(f)
                    stats["gap"] = {
                        "total_gaps": len(gap_data.get("recommendations", [])),
                        "high_risk_gaps": len(
                            [
                                r
                                for r in gap_data.get("recommendations", [])
                                if r.get("risk_level") == "High"
                            ]
                        ),
                        "medium_risk_gaps": len(
                            [
                                r
                                for r in gap_data.get("recommendations", [])
                                if r.get("risk_level") == "Medium"
                            ]
                        ),
                        "low_risk_gaps": len(
                            [
                                r
                                for r in gap_data.get("recommendations", [])
                                if r.get("risk_level") == "Low"
                            ]
                        ),
                    }
            except Exception as e:
                logger.error(f"Failed to extract gap stats: {e}")

        # Save consolidated stats
        stats_file = self.summary_dir / "consolidated_stats.json"
        with open(stats_file, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

        logger.info(f"Consolidated stats generated: {stats_file}")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Comprehensive BDD Analysis for Release 2"
    )

    parser.add_argument(
        "--features-dir",
        required=True,
        help="Directory containing BDD feature files",
    )

    parser.add_argument(
        "--steps-dir", help="Directory containing step definition files"
    )

    parser.add_argument(
        "--requirements-file",
        help="File containing requirements data (CSV or JSON)",
    )

    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for analysis reports",
    )

    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.75,
        help="Similarity threshold for semantic duplicates (default: 0.75)",
    )

    parser.add_argument(
        "--tag-threshold",
        type=float,
        default=0.5,
        help="Threshold for tag overlap detection (default: 0.5)",
    )

    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_args()

    analyzer = BDDComprehensiveAnalyzer(
        features_dir=args.features_dir,
        steps_dir=args.steps_dir,
        requirements_file=args.requirements_file,
        output_dir=args.output_dir,
        similarity_threshold=args.similarity_threshold,
        tag_threshold=args.tag_threshold,
    )

    analyzer.run_analysis()

    logger.info("Comprehensive BDD analysis complete")


if __name__ == "__main__":
    main()
