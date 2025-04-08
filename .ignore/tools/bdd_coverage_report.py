"""
Tool: BDD Coverage Report Generator
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Generates coverage reports for BDD features and scenarios
Dependencies: pandas, matplotlib, logging
Lifecycle:
    - Created: To visualize BDD test coverage
    - Active: Used for regular coverage reporting
    - Obsolescence Conditions:
        1. When replaced by integrated coverage solution
        2. When BDD testing approach changes
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
BDD Coverage Report Generator

This script analyzes BDD feature files and requirements to generate a coverage report.
It identifies gaps in BDD coverage and provides recommendations for improving test coverage.
"""

import argparse
import csv
import glob
import json
import logging
import os
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("bdd_coverage_report")


@dataclass
class Requirement:
    """Represents a requirement with its metadata."""

    id: str
    description: str
    priority: str = "Medium"  # High, Medium, Low
    tags: List[str] = field(default_factory=list)
    source: str = ""  # Source document or system

    # Coverage metrics
    scenarios_count: int = 0
    passed_scenarios: int = 0
    failed_scenarios: int = 0
    pending_scenarios: int = 0

    @property
    def coverage_percentage(self) -> float:
        """Calculate the percentage of coverage."""
        if self.scenarios_count == 0:
            return 0.0
        return (self.passed_scenarios / self.scenarios_count) * 100

    @property
    def coverage_status(self) -> str:
        """Determine the coverage status."""
        if self.scenarios_count == 0:
            return "Not Covered"
        elif self.coverage_percentage == 100:
            return "Fully Covered"
        elif self.coverage_percentage >= 50:
            return "Partially Covered"
        else:
            return "Poorly Covered"

    @property
    def risk_level(self) -> str:
        """Determine the risk level based on priority and coverage."""
        if self.priority == "High" and self.coverage_percentage < 75:
            return "High"
        elif self.priority == "High" and self.coverage_percentage < 100:
            return "Medium"
        elif self.priority == "Medium" and self.coverage_percentage < 50:
            return "Medium"
        elif self.coverage_percentage < 25:
            return "Medium"
        else:
            return "Low"


@dataclass
class BDDScenario:
    """Represents a BDD scenario with its metadata."""

    name: str
    feature_file: str
    feature_name: str
    tags: List[str] = field(default_factory=list)
    steps_count: int = 0
    status: str = "Unknown"  # Pass, Fail, Pending
    requirement_ids: List[str] = field(default_factory=list)


@dataclass
class CoverageGap:
    """Represents a gap in BDD coverage."""

    requirement_id: str
    requirement_description: str
    gap_type: str  # "No Coverage", "Partial Coverage", "Failed Tests"
    priority: str  # High, Medium, Low
    recommendation: str
    risk_level: str  # High, Medium, Low


class BDDCoverageAnalyzer:
    """Analyzes BDD feature files and requirements for coverage reporting."""

    def __init__(self, features_dir: str, requirements_file: str = None):
        self.features_dir = features_dir
        self.requirements_file = requirements_file
        self.requirements: Dict[str, Requirement] = {}
        self.scenarios: List[BDDScenario] = []
        self.coverage_gaps: List[CoverageGap] = []
        self.req_pattern = re.compile(r"@REQ-([A-Za-z]+-\d+)")

    def load_requirements(self):
        """Load requirements from a file or discover them from BDD tags."""
        if self.requirements_file and os.path.exists(self.requirements_file):
            self._load_requirements_from_file()
        else:
            logger.warning(
                "No requirements file provided or file not found. "
                "Requirements will be discovered from BDD tags only."
            )

    def _load_requirements_from_file(self):
        """Load requirements from a file (CSV, JSON, etc.)."""
        logger.info(f"Loading requirements from {self.requirements_file}")

        file_ext = os.path.splitext(self.requirements_file)[1].lower()

        if file_ext == ".csv":
            self._load_requirements_from_csv()
        elif file_ext == ".json":
            self._load_requirements_from_json()
        else:
            logger.error(f"Unsupported requirements file format: {file_ext}")
            raise ValueError(
                f"Unsupported requirements file format: {file_ext}"
            )

    def _load_requirements_from_csv(self):
        """Load requirements from a CSV file."""
        with open(self.requirements_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                req_id = row.get("ID", "")
                if not req_id:
                    continue

                # Extract tags if they exist
                tags = []
                if "Tags" in row and row["Tags"]:
                    tags = [tag.strip() for tag in row["Tags"].split(",")]

                self.requirements[req_id] = Requirement(
                    id=req_id,
                    description=row.get("Description", ""),
                    priority=row.get("Priority", "Medium"),
                    tags=tags,
                    source=row.get("Source", ""),
                )

        logger.info(f"Loaded {len(self.requirements)} requirements from CSV")

    def _load_requirements_from_json(self):
        """Load requirements from a JSON file."""
        with open(self.requirements_file, "r", encoding="utf-8") as f:
            requirements_data = json.load(f)

            for req_data in requirements_data:
                req_id = req_data.get("id", "")
                if not req_id:
                    continue

                self.requirements[req_id] = Requirement(
                    id=req_id,
                    description=req_data.get("description", ""),
                    priority=req_data.get("priority", "Medium"),
                    tags=req_data.get("tags", []),
                    source=req_data.get("source", ""),
                )

        logger.info(f"Loaded {len(self.requirements)} requirements from JSON")

    def scan_feature_files(self):
        """Scan feature files to extract scenarios and requirements."""
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

        # Extract feature name
        feature_match = re.search(r"Feature:\s*([^\n]+)", content)
        feature_name = (
            feature_match.group(1).strip()
            if feature_match
            else "Unknown Feature"
        )

        # Extract feature-level tags
        feature_tags = self._extract_feature_tags(content)

        # Extract scenarios
        scenarios = self._extract_scenarios(
            content, relative_path, feature_name, feature_tags
        )

        # Add to our list of scenarios
        self.scenarios.extend(scenarios)

        # Extract requirements from tags and update requirements list
        self._extract_requirements_from_tags(scenarios)

    def _extract_feature_tags(self, content: str) -> List[str]:
        """Extract tags from the feature."""
        feature_match = re.search(r"(?:@[^\n]+\n)+Feature:", content)
        if feature_match:
            tags_section = feature_match.group(0).replace("Feature:", "")
            return re.findall(r"@\S+", tags_section)
        return []

    def _extract_scenarios(
        self,
        content: str,
        file_path: str,
        feature_name: str,
        feature_tags: List[str],
    ) -> List[BDDScenario]:
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

            # Count steps in scenario
            scenario_end = content.find("\n\n", scenario_match.end())
            if scenario_end == -1:
                scenario_end = len(content)
            scenario_content = content[scenario_match.end() : scenario_end]
            steps_count = len(
                re.findall(
                    r"^\s*(Given|When|Then|And|But)\s+",
                    scenario_content,
                    re.MULTILINE,
                )
            )

            # Extract requirement IDs from tags
            requirement_ids = []
            for tag in all_tags:
                match = self.req_pattern.match(tag)
                if match:
                    requirement_ids.append(match.group(1))

            # Create scenario object
            scenario = BDDScenario(
                name=scenario_name,
                feature_file=file_path,
                feature_name=feature_name,
                tags=all_tags,
                steps_count=steps_count,
                status=self._determine_scenario_status(
                    scenario_name, file_path
                ),
                requirement_ids=requirement_ids,
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

    def _extract_requirements_from_tags(self, scenarios: List[BDDScenario]):
        """Extract requirements from scenario tags and update requirements list."""
        # Create a set of all requirement IDs found in tags
        for scenario in scenarios:
            for req_id in scenario.requirement_ids:
                # If the requirement doesn't exist yet, create it
                if req_id not in self.requirements:
                    self.requirements[req_id] = Requirement(
                        id=req_id,
                        description=f"Requirement discovered from tag @REQ-{req_id}",
                    )

                # Update requirement metrics based on this scenario
                req = self.requirements[req_id]
                req.scenarios_count += 1

                if scenario.status == "Pass":
                    req.passed_scenarios += 1
                elif scenario.status == "Fail":
                    req.failed_scenarios += 1
                elif scenario.status == "Pending":
                    req.pending_scenarios += 1

    def find_coverage_gaps(self):
        """Identify gaps in BDD coverage."""
        logger.info("Analyzing coverage gaps")

        for req_id, req in self.requirements.items():
            if req.scenarios_count == 0:
                # No coverage at all
                self.coverage_gaps.append(
                    CoverageGap(
                        requirement_id=req_id,
                        requirement_description=req.description,
                        gap_type="No Coverage",
                        priority=req.priority,
                        recommendation=f"Create BDD scenarios to cover requirement REQ-{req_id}",
                        risk_level=(
                            "High" if req.priority == "High" else "Medium"
                        ),
                    )
                )
            elif req.coverage_percentage < 50:
                # Partial coverage
                self.coverage_gaps.append(
                    CoverageGap(
                        requirement_id=req_id,
                        requirement_description=req.description,
                        gap_type="Partial Coverage",
                        priority=req.priority,
                        recommendation=f"Increase BDD scenario coverage for requirement REQ-{req_id}",
                        risk_level=req.risk_level,
                    )
                )
            elif req.failed_scenarios > 0:
                # Failed tests
                self.coverage_gaps.append(
                    CoverageGap(
                        requirement_id=req_id,
                        requirement_description=req.description,
                        gap_type="Failed Tests",
                        priority=req.priority,
                        recommendation=f"Fix failing BDD scenarios for requirement REQ-{req_id}",
                        risk_level=req.risk_level,
                    )
                )

        # Sort gaps by risk level (High to Low) and then by priority
        self.coverage_gaps.sort(
            key=lambda gap: (
                (
                    0
                    if gap.risk_level == "High"
                    else (1 if gap.risk_level == "Medium" else 2)
                ),
                (
                    0
                    if gap.priority == "High"
                    else (1 if gap.priority == "Medium" else 2)
                ),
            )
        )

        logger.info(f"Found {len(self.coverage_gaps)} coverage gaps")

    def generate_reports(self, output_dir: str):
        """Generate coverage reports in various formats."""
        logger.info(f"Generating reports in {output_dir}")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Generate summary report (markdown)
        self._generate_summary_report(
            os.path.join(output_dir, "coverage_summary.md")
        )

        # Generate detailed report (JSON)
        self._generate_detailed_report(
            os.path.join(output_dir, "coverage_detailed.json")
        )

        # Generate gap analysis report (markdown)
        self._generate_gap_report(os.path.join(output_dir, "coverage_gaps.md"))

    def _generate_summary_report(self, output_file: str):
        """Generate a summary report in markdown format."""
        logger.info(f"Generating summary report: {output_file}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# BDD Coverage Summary Report\n\n")

            # Overall statistics
            f.write("## Overall Statistics\n\n")
            total_reqs = len(self.requirements)
            covered_reqs = sum(
                1
                for req in self.requirements.values()
                if req.scenarios_count > 0
            )
            fully_covered_reqs = sum(
                1
                for req in self.requirements.values()
                if req.coverage_percentage == 100
            )

            f.write(f"- Total Requirements: {total_reqs}\n")
            f.write(
                f"- Requirements with BDD Coverage: {covered_reqs} ({covered_reqs/total_reqs*100:.1f}%)\n"
            )
            f.write(
                f"- Fully Covered Requirements: {fully_covered_reqs} ({fully_covered_reqs/total_reqs*100:.1f}%)\n"
            )
            f.write(f"- Total BDD Scenarios: {len(self.scenarios)}\n")
            f.write(
                f"- Coverage Gaps Identified: {len(self.coverage_gaps)}\n\n"
            )

            # Coverage by priority
            f.write("## Coverage by Priority\n\n")
            f.write(
                "| Priority | Total | Covered | Fully Covered | Coverage % |\n"
            )
            f.write(
                "|----------|-------|---------|---------------|------------|\n"
            )

            for priority in ["High", "Medium", "Low"]:
                priority_reqs = [
                    req
                    for req in self.requirements.values()
                    if req.priority == priority
                ]
                total = len(priority_reqs)
                if total == 0:
                    continue

                covered = sum(
                    1 for req in priority_reqs if req.scenarios_count > 0
                )
                fully_covered = sum(
                    1
                    for req in priority_reqs
                    if req.coverage_percentage == 100
                )
                coverage_pct = (
                    (fully_covered / total * 100) if total > 0 else 0
                )

                f.write(
                    f"| {priority} | {total} | {covered} | {fully_covered} | {coverage_pct:.1f}% |\n"
                )

            # Risk assessment
            f.write("\n## Risk Assessment\n\n")
            f.write("| Risk Level | Count | Description |\n")
            f.write("|------------|-------|-------------|\n")

            risk_levels = {"High": 0, "Medium": 0, "Low": 0}
            for req in self.requirements.values():
                risk_levels[req.risk_level] += 1

            f.write(
                f"| High | {risk_levels['High']} | High priority requirements with insufficient coverage |\n"
            )
            f.write(
                f"| Medium | {risk_levels['Medium']} | Medium priority requirements with poor coverage or high priority with partial coverage |\n"
            )
            f.write(
                f"| Low | {risk_levels['Low']} | Well-covered requirements |\n"
            )

            # Top gaps
            if self.coverage_gaps:
                f.write("\n## Top Coverage Gaps\n\n")
                f.write(
                    "| Requirement | Priority | Gap Type | Risk Level | Recommendation |\n"
                )
                f.write(
                    "|-------------|----------|----------|------------|----------------|\n"
                )

                # Show top 10 gaps
                for gap in self.coverage_gaps[:10]:
                    f.write(
                        f"| REQ-{gap.requirement_id} | {gap.priority} | {gap.gap_type} | {gap.risk_level} | {gap.recommendation} |\n"
                    )

                if len(self.coverage_gaps) > 10:
                    f.write(
                        f"\n*Plus {len(self.coverage_gaps) - 10} more gaps. See the gap analysis report for details.*\n"
                    )

            # Recommendations
            f.write("\n## Recommendations\n\n")

            high_risk_gaps = [
                gap for gap in self.coverage_gaps if gap.risk_level == "High"
            ]
            if high_risk_gaps:
                f.write("### High Priority Actions\n\n")
                for i, gap in enumerate(high_risk_gaps[:5], 1):
                    f.write(f"{i}. {gap.recommendation}\n")

            # General recommendations
            f.write("\n### General Recommendations\n\n")
            no_coverage = sum(
                1
                for gap in self.coverage_gaps
                if gap.gap_type == "No Coverage"
            )
            partial_coverage = sum(
                1
                for gap in self.coverage_gaps
                if gap.gap_type == "Partial Coverage"
            )
            failed_tests = sum(
                1
                for gap in self.coverage_gaps
                if gap.gap_type == "Failed Tests"
            )

            if no_coverage > 0:
                f.write(
                    f"1. Create BDD scenarios for {no_coverage} requirements with no coverage\n"
                )
            if partial_coverage > 0:
                f.write(
                    f"2. Improve scenario coverage for {partial_coverage} partially covered requirements\n"
                )
            if failed_tests > 0:
                f.write(f"3. Fix {failed_tests} failing BDD scenarios\n")
            f.write(
                "4. Regularly review and update the BDD coverage analysis\n"
            )
            f.write(
                "5. Consider automating the coverage reporting in the CI/CD pipeline\n"
            )

    def _generate_detailed_report(self, output_file: str):
        """Generate a detailed report in JSON format."""
        logger.info(f"Generating detailed report: {output_file}")

        # Prepare data structure for JSON
        report_data = {
            "summary": {
                "total_requirements": len(self.requirements),
                "total_scenarios": len(self.scenarios),
                "total_gaps": len(self.coverage_gaps),
            },
            "requirements": [
                asdict(req) for req in self.requirements.values()
            ],
            "scenarios": [asdict(scenario) for scenario in self.scenarios],
            "coverage_gaps": [asdict(gap) for gap in self.coverage_gaps],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)

    def _generate_gap_report(self, output_file: str):
        """Generate a gap analysis report in markdown format."""
        logger.info(f"Generating gap report: {output_file}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# BDD Coverage Gap Analysis\n\n")

            if not self.coverage_gaps:
                f.write("No coverage gaps identified.\n")
                return

            # Group gaps by type
            gaps_by_type = defaultdict(list)
            for gap in self.coverage_gaps:
                gaps_by_type[gap.gap_type].append(gap)

            # No Coverage section
            if "No Coverage" in gaps_by_type:
                f.write("## Requirements Without BDD Coverage\n\n")
                f.write(
                    "| Requirement | Description | Priority | Risk Level |\n"
                )
                f.write(
                    "|-------------|-------------|----------|------------|\n"
                )

                for gap in gaps_by_type["No Coverage"]:
                    f.write(
                        f"| REQ-{gap.requirement_id} | {gap.requirement_description} | {gap.priority} | {gap.risk_level} |\n"
                    )

                f.write("\n### Recommendations\n\n")
                f.write(
                    "1. Prioritize creating BDD scenarios for high priority requirements\n"
                )
                f.write(
                    "2. Create at least one scenario for each requirement to establish basic coverage\n"
                )
                f.write(
                    "3. Focus on defining clear acceptance criteria in each scenario\n\n"
                )

            # Partial Coverage section
            if "Partial Coverage" in gaps_by_type:
                f.write("## Requirements With Partial Coverage\n\n")
                f.write(
                    "| Requirement | Description | Priority | Current Coverage | Risk Level |\n"
                )
                f.write(
                    "|-------------|-------------|----------|-----------------|--------------|\n"
                )

                for gap in gaps_by_type["Partial Coverage"]:
                    req = self.requirements.get(gap.requirement_id)
                    coverage = (
                        f"{req.coverage_percentage:.1f}%" if req else "Unknown"
                    )
                    f.write(
                        f"| REQ-{gap.requirement_id} | {gap.requirement_description} | {gap.priority} | {coverage} | {gap.risk_level} |\n"
                    )

                f.write("\n### Recommendations\n\n")
                f.write("1. Review existing scenarios for completeness\n")
                f.write(
                    "2. Add scenarios to cover additional aspects of these requirements\n"
                )
                f.write(
                    "3. Focus on edge cases and negative testing scenarios\n\n"
                )

            # Failed Tests section
            if "Failed Tests" in gaps_by_type:
                f.write("## Requirements With Failing Tests\n\n")
                f.write(
                    "| Requirement | Description | Priority | Failed / Total Scenarios | Risk Level |\n"
                )
                f.write(
                    "|-------------|-------------|----------|--------------------------|------------|\n"
                )

                for gap in gaps_by_type["Failed Tests"]:
                    req = self.requirements.get(gap.requirement_id)
                    ratio = (
                        f"{req.failed_scenarios}/{req.scenarios_count}"
                        if req
                        else "Unknown"
                    )
                    f.write(
                        f"| REQ-{gap.requirement_id} | {gap.requirement_description} | {gap.priority} | {ratio} | {gap.risk_level} |\n"
                    )

                f.write("\n### Recommendations\n\n")
                f.write("1. Investigate and fix failing scenarios\n")
                f.write(
                    "2. Consider if failures indicate issues with the requirements\n"
                )
                f.write(
                    "3. Ensure test environment is properly configured\n\n"
                )

            # Action plan
            f.write("## Suggested Action Plan\n\n")

            # High priority actions
            high_risk_gaps = [
                gap for gap in self.coverage_gaps if gap.risk_level == "High"
            ]
            if high_risk_gaps:
                f.write("### Immediate Actions (High Risk)\n\n")
                for i, gap in enumerate(high_risk_gaps, 1):
                    f.write(f"{i}. {gap.recommendation}\n")
                f.write("\n")

            # Medium priority actions
            medium_risk_gaps = [
                gap for gap in self.coverage_gaps if gap.risk_level == "Medium"
            ]
            if medium_risk_gaps:
                f.write("### Short-term Actions (Medium Risk)\n\n")
                for i, gap in enumerate(medium_risk_gaps[:10], 1):
                    f.write(f"{i}. {gap.recommendation}\n")

                if len(medium_risk_gaps) > 10:
                    f.write(
                        f"...plus {len(medium_risk_gaps) - 10} more medium risk items\n"
                    )
                f.write("\n")

            # Low priority actions
            low_risk_gaps = [
                gap for gap in self.coverage_gaps if gap.risk_level == "Low"
            ]
            if low_risk_gaps:
                f.write("### Long-term Actions (Low Risk)\n\n")
                f.write(
                    f"There are {len(low_risk_gaps)} low risk coverage items that can be addressed as part of regular maintenance.\n"
                )


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate a BDD coverage report"
    )
    parser.add_argument(
        "--features-dir",
        required=True,
        help="Directory containing BDD feature files",
    )
    parser.add_argument(
        "--requirements-file",
        help="File containing requirements data (CSV or JSON)",
    )
    parser.add_argument(
        "--output-dir", required=True, help="Directory for output reports"
    )

    args = parser.parse_args()

    analyzer = BDDCoverageAnalyzer(
        features_dir=args.features_dir,
        requirements_file=args.requirements_file,
    )

    analyzer.load_requirements()
    analyzer.scan_feature_files()
    analyzer.find_coverage_gaps()
    analyzer.generate_reports(args.output_dir)

    logger.info("BDD coverage analysis complete")


if __name__ == "__main__":
    main()
