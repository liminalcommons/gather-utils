"""
Tool: Bdd Traceability Matrix
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Supports BDD testing and development workflows
Dependencies: glob, logging, dataclasses
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
BDD Traceability Matrix Generator

This script scans BDD feature files to extract requirement information and generates
a traceability matrix in markdown format. The matrix shows the relationship between
requirements, features, scenarios, and their implementation status.
"""

import argparse
import glob
import logging
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("bdd_traceability_matrix")


@dataclass
class Scenario:
    """Represents a BDD scenario with its metadata."""

    name: str
    feature_file: str
    tags: List[str]
    status: str = "Unknown"  # Pass, Fail, Pending, etc.


@dataclass
class Requirement:
    """Represents a requirement with its associated scenarios."""

    req_id: str
    description: str = ""
    scenarios: List[Scenario] = None
    coverage: str = "None"  # Full, Partial, None

    def __post_init__(self):
        if self.scenarios is None:
            self.scenarios = []

    def calculate_status(self) -> str:
        """Calculate the overall test status based on scenario statuses."""
        if not self.scenarios:
            return "Missing"

        statuses = [s.status for s in self.scenarios]
        if all(status == "Pass" for status in statuses):
            return "Pass"
        elif all(status == "Fail" for status in statuses):
            return "Fail"
        elif any(status == "Pending" for status in statuses):
            return "Pending"
        else:
            return "Partial"

    def calculate_coverage(self) -> str:
        """Calculate the coverage level based on scenario statuses."""
        if not self.scenarios:
            return "None"

        status = self.calculate_status()
        if status == "Pass":
            return "Full"
        elif status == "Fail":
            return "None"
        else:
            return "Partial"


class TraceabilityMatrixGenerator:
    """Generates a traceability matrix from BDD feature files."""

    def __init__(self, features_dir: str, steps_dir: str, output_file: str):
        self.features_dir = features_dir
        self.steps_dir = steps_dir
        self.output_file = output_file
        self.requirements: Dict[str, Requirement] = {}
        self.req_pattern = re.compile(r"@REQ-([A-Za-z]+-\d+)")

    def scan_feature_files(self):
        """Scan feature files to extract requirements and scenarios."""
        logger.info(f"Scanning feature files in {self.features_dir}")

        feature_files = glob.glob(
            os.path.join(self.features_dir, "**", "*.feature"), recursive=True
        )
        logger.info(f"Found {len(feature_files)} feature files")

        for feature_file in feature_files:
            self._process_feature_file(feature_file)

    def _process_feature_file(self, file_path: str):
        """Process a single feature file to extract scenarios and requirements."""
        logger.info(f"Processing feature file: {file_path}")

        relative_path = os.path.relpath(
            file_path, os.path.dirname(self.features_dir)
        )
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract feature-level tags
        feature_tags = self._extract_feature_tags(content)

        # Extract scenarios
        scenarios = self._extract_scenarios(
            content, relative_path, feature_tags
        )

        # Associate scenarios with requirements
        self._associate_scenarios_with_requirements(scenarios)

    def _extract_feature_tags(self, content: str) -> List[str]:
        """Extract tags from the feature."""
        feature_match = re.search(r"(?:@[^\n]+\n)+Feature:", content)
        if feature_match:
            tags_section = feature_match.group(0).replace("Feature:", "")
            return re.findall(r"@\S+", tags_section)
        return []

    def _extract_scenarios(
        self, content: str, file_path: str, feature_tags: List[str]
    ) -> List[Scenario]:
        """Extract scenarios from a feature file."""
        scenarios = []

        # Find all scenario blocks including tags
        scenario_blocks = re.finditer(
            r"(?:(?:^|\n)(?:@[^\n]+\n)+)?(?:^|\n)\s*(?:Scenario|Scenario Outline):\s*([^\n]+)",
            content,
        )

        for scenario_match in scenario_blocks:
            # Get the scenario name
            scenario_name = scenario_match.group(1).strip()

            # Get scenario-specific tags
            scenario_start = scenario_match.start()
            tags_section = content[
                max(0, content.rfind("\n", 0, scenario_start)) : scenario_start
            ]
            scenario_tags = re.findall(r"@\S+", tags_section)

            # Combine with feature tags
            all_tags = feature_tags + scenario_tags

            # Create scenario object
            scenario = Scenario(
                name=scenario_name,
                feature_file=file_path,
                tags=all_tags,
                status=self._determine_scenario_status(
                    scenario_name, file_path
                ),
            )

            scenarios.append(scenario)

        logger.info(f"Found {len(scenarios)} scenarios in {file_path}")
        return scenarios

    def _determine_scenario_status(
        self, scenario_name: str, feature_file: str
    ) -> str:
        """
        Determine the execution status of a scenario.

        In a real implementation, this would query test results.
        Here we're using a simple heuristic for demonstration.
        """
        # This is a placeholder. In a real implementation, you would:
        # 1. Parse test result files (e.g., cucumber.json)
        # 2. Look up the status based on feature file and scenario name

        # For now, we'll just assign random statuses for demonstration
        import random

        statuses = ["Pass", "Fail", "Pending"]
        weights = [0.7, 0.2, 0.1]  # 70% passing, 20% failing, 10% pending
        return random.choices(statuses, weights=weights, k=1)[0]

    def _associate_scenarios_with_requirements(
        self, scenarios: List[Scenario]
    ):
        """Associate scenarios with their requirements based on tags."""
        for scenario in scenarios:
            req_ids = set()

            # Extract requirement IDs from tags
            for tag in scenario.tags:
                match = self.req_pattern.match(tag)
                if match:
                    req_id = match.group(1)
                    req_ids.add(req_id)

            # If no requirement tag, use a default "Untraced" requirement
            if not req_ids:
                req_id = "UNTRACED"
                req_ids.add(req_id)

            # Associate scenario with each requirement
            for req_id in req_ids:
                if req_id not in self.requirements:
                    self.requirements[req_id] = Requirement(req_id=req_id)

                self.requirements[req_id].scenarios.append(scenario)

    def _find_step_definition_files(
        self, feature_file: str, scenario_name: str
    ) -> List[str]:
        """
        Find step definition files that implement a scenario.

        In a real implementation, this would analyze step definition files
        to determine which ones implement steps from this scenario.
        """
        # This is a placeholder. In a real implementation, you would:
        # 1. Parse step definition files
        # 2. Match step definitions to steps in the scenario
        # 3. Return matching step definition files

        # For now, we'll return a placeholder based on the feature file name
        base_name = os.path.splitext(os.path.basename(feature_file))[0]
        return [f"{base_name}_steps.py"]

    def calculate_matrix_data(self):
        """Calculate traceability matrix data based on collected information."""
        logger.info("Calculating matrix data")

        for req_id, requirement in self.requirements.items():
            # Update requirement status and coverage based on scenarios
            requirement.coverage = requirement.calculate_coverage()

    def generate_matrix(self):
        """Generate the traceability matrix in markdown format."""
        logger.info(f"Generating matrix to {self.output_file}")

        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("# Requirements Traceability Matrix\n\n")

            f.write("## Matrix\n\n")
            f.write(
                "| Requirement ID | Requirement Description | Feature File | Scenario(s) | Step Definition File(s) | Test Status | Coverage |\n"
            )
            f.write(
                "|----------------|-------------------------|--------------|-------------|-------------------------|------------|----------|\n"
            )

            # Sort requirements by ID
            sorted_reqs = sorted(
                self.requirements.values(), key=lambda r: r.req_id
            )

            for req in sorted_reqs:
                # Skip requirements with no scenarios unless explicitly requested
                if not req.scenarios:
                    continue

                status = req.calculate_status()

                # Format scenario list
                scenarios_formatted = ""
                step_files_set = set()

                for i, scenario in enumerate(req.scenarios):
                    if i > 0:
                        scenarios_formatted += "<br>"
                    scenarios_formatted += f"{i+1}. {scenario.name}"

                    # Collect step definition files
                    step_files = self._find_step_definition_files(
                        scenario.feature_file, scenario.name
                    )
                    step_files_set.update(step_files)

                # Format feature files (unique)
                feature_files = sorted(
                    set(s.feature_file for s in req.scenarios)
                )
                feature_files_formatted = "<br>".join(feature_files)

                # Format step definition files
                step_files_formatted = "<br>".join(sorted(step_files_set))

                # Write the row
                f.write(
                    f"| REQ-{req.req_id} | {req.description} | {feature_files_formatted} | {scenarios_formatted} | {step_files_formatted} | {status} | {req.coverage} |\n"
                )

            # Add statistics
            f.write("\n## Statistics\n\n")
            f.write(f"- Total Requirements: {len(self.requirements)}\n")

            # Count by status
            status_counts = defaultdict(int)
            for req in self.requirements.values():
                status = req.calculate_status()
                status_counts[status] += 1

            f.write("- Test Status Distribution:\n")
            for status, count in status_counts.items():
                percentage = (count / len(self.requirements)) * 100
                f.write(f"  - {status}: {count} ({percentage:.1f}%)\n")

            # Count by coverage
            coverage_counts = defaultdict(int)
            for req in self.requirements.values():
                coverage_counts[req.coverage] += 1

            f.write("- Coverage Distribution:\n")
            for coverage, count in coverage_counts.items():
                percentage = (count / len(self.requirements)) * 100
                f.write(f"  - {coverage}: {count} ({percentage:.1f}%)\n")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate a BDD traceability matrix"
    )
    parser.add_argument(
        "--features-dir",
        required=True,
        help="Directory containing BDD feature files",
    )
    parser.add_argument(
        "--steps-dir", help="Directory containing step definition files"
    )
    parser.add_argument("--output", required=True, help="Output markdown file")

    args = parser.parse_args()

    generator = TraceabilityMatrixGenerator(
        features_dir=args.features_dir,
        steps_dir=args.steps_dir
        or args.features_dir.replace("features", "steps"),
        output_file=args.output,
    )

    generator.scan_feature_files()
    generator.calculate_matrix_data()
    generator.generate_matrix()

    logger.info("Traceability matrix generation complete")


if __name__ == "__main__":
    main()
