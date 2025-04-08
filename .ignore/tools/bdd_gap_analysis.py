"""
Tool: Bdd Gap Analysis
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Supports BDD testing and development workflows
Dependencies: csv, logging, dataclasses
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
BDD Gap Analysis Tool

This script analyzes BDD feature files and requirements to generate a gap analysis report.
It identifies areas where requirements lack adequate BDD coverage and provides
prioritized recommendations for improving test coverage.
"""

import argparse
import csv
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
logger = logging.getLogger("bdd_gap_analysis")


@dataclass
class RequirementArea:
    """Represents a grouping of related requirements."""

    name: str
    description: str
    requirements: List[str] = field(default_factory=list)
    priority: str = "Medium"  # High, Medium, Low
    total_reqs: int = 0
    covered_reqs: int = 0

    @property
    def coverage_percentage(self) -> float:
        """Calculate the percentage of coverage."""
        if self.total_reqs == 0:
            return 0.0
        return (self.covered_reqs / self.total_reqs) * 100

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
class RequirementDetail:
    """Detailed information about a requirement."""

    id: str
    description: str
    area: str
    priority: str = "Medium"
    scenarios_count: int = 0
    status: str = (
        "Not Covered"  # Fully Covered, Partially Covered, Not Covered
    )
    tags: List[str] = field(default_factory=list)


@dataclass
class GapRecommendation:
    """Recommendation for addressing a coverage gap."""

    area: str
    priority: str  # High, Medium, Low
    risk_level: str  # High, Medium, Low
    description: str
    affected_requirements: List[str] = field(default_factory=list)
    effort_estimate: str = "Medium"  # Low, Medium, High


class BDDGapAnalyzer:
    """Analyzes BDD feature files and requirements to identify coverage gaps."""

    def __init__(
        self,
        coverage_data_file: str,
        requirements_file: str,
        areas_file: str = None,
    ):
        self.coverage_data_file = coverage_data_file
        self.requirements_file = requirements_file
        self.areas_file = areas_file
        self.requirement_areas: Dict[str, RequirementArea] = {}
        self.requirements: Dict[str, RequirementDetail] = {}
        self.recommendations: List[GapRecommendation] = []

    def load_data(self):
        """Load data from input files."""
        self._load_requirements()

        if self.areas_file:
            self._load_requirement_areas()
        else:
            self._infer_requirement_areas()

        self._load_coverage_data()

        logger.info(
            f"Loaded {len(self.requirements)} requirements in {len(self.requirement_areas)} areas"
        )

    def _load_requirements(self):
        """Load requirements from a file."""
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

                self.requirements[req_id] = RequirementDetail(
                    id=req_id,
                    description=row.get("Description", ""),
                    area=row.get("Area", "Uncategorized"),
                    priority=row.get("Priority", "Medium"),
                    tags=tags,
                )

    def _load_requirements_from_json(self):
        """Load requirements from a JSON file."""
        with open(self.requirements_file, "r", encoding="utf-8") as f:
            requirements_data = json.load(f)

            for req_data in requirements_data:
                req_id = req_data.get("id", "")
                if not req_id:
                    continue

                self.requirements[req_id] = RequirementDetail(
                    id=req_id,
                    description=req_data.get("description", ""),
                    area=req_data.get("area", "Uncategorized"),
                    priority=req_data.get("priority", "Medium"),
                    tags=req_data.get("tags", []),
                )

    def _load_requirement_areas(self):
        """Load requirement areas from a file."""
        logger.info(f"Loading requirement areas from {self.areas_file}")

        file_ext = os.path.splitext(self.areas_file)[1].lower()

        if file_ext == ".csv":
            self._load_areas_from_csv()
        elif file_ext == ".json":
            self._load_areas_from_json()
        else:
            logger.error(f"Unsupported areas file format: {file_ext}")
            raise ValueError(f"Unsupported areas file format: {file_ext}")

    def _load_areas_from_csv(self):
        """Load requirement areas from a CSV file."""
        with open(self.areas_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                area_name = row.get("Name", "")
                if not area_name:
                    continue

                self.requirement_areas[area_name] = RequirementArea(
                    name=area_name,
                    description=row.get("Description", ""),
                    priority=row.get("Priority", "Medium"),
                )

    def _load_areas_from_json(self):
        """Load requirement areas from a JSON file."""
        with open(self.areas_file, "r", encoding="utf-8") as f:
            areas_data = json.load(f)

            for area_data in areas_data:
                area_name = area_data.get("name", "")
                if not area_name:
                    continue

                self.requirement_areas[area_name] = RequirementArea(
                    name=area_name,
                    description=area_data.get("description", ""),
                    priority=area_data.get("priority", "Medium"),
                )

    def _infer_requirement_areas(self):
        """Infer requirement areas from requirement data."""
        logger.info("Inferring requirement areas from requirements")

        # Extract areas from requirements
        for req in self.requirements.values():
            area_name = req.area
            if area_name and area_name not in self.requirement_areas:
                self.requirement_areas[area_name] = RequirementArea(
                    name=area_name,
                    description=f"Requirements related to {area_name}",
                    priority="Medium",  # Default priority
                )

        # If no areas found, create a default one
        if not self.requirement_areas:
            self.requirement_areas["General"] = RequirementArea(
                name="General",
                description="General requirements",
                priority="Medium",
            )

    def _load_coverage_data(self):
        """Load coverage data from the coverage report."""
        logger.info(f"Loading coverage data from {self.coverage_data_file}")

        with open(self.coverage_data_file, "r", encoding="utf-8") as f:
            coverage_data = json.load(f)

            # Process requirements coverage
            if "requirements" in coverage_data:
                for req_data in coverage_data["requirements"]:
                    req_id = req_data.get("id", "")
                    if not req_id or req_id not in self.requirements:
                        continue

                    req = self.requirements[req_id]
                    req.scenarios_count = req_data.get("scenarios_count", 0)

                    # Determine status based on coverage
                    if req.scenarios_count == 0:
                        req.status = "Not Covered"
                    elif req_data.get("coverage_percentage", 0) == 100:
                        req.status = "Fully Covered"
                    else:
                        req.status = "Partially Covered"

            # If no requirements found in coverage data, try to use scenarios
            elif "scenarios" in coverage_data:
                req_scenario_count = defaultdict(int)

                for scenario in coverage_data["scenarios"]:
                    for req_id in scenario.get("requirement_ids", []):
                        if req_id in self.requirements:
                            req_scenario_count[req_id] += 1

                for req_id, count in req_scenario_count.items():
                    self.requirements[req_id].scenarios_count = count
                    self.requirements[req_id].status = (
                        "Fully Covered" if count > 0 else "Not Covered"
                    )

        # Update requirement areas with coverage data
        for req in self.requirements.values():
            area_name = req.area
            if area_name in self.requirement_areas:
                area = self.requirement_areas[area_name]
                area.requirements.append(req.id)
                area.total_reqs += 1
                if req.status in ["Fully Covered", "Partially Covered"]:
                    area.covered_reqs += 1

    def analyze_gaps(self):
        """Analyze coverage gaps and generate recommendations."""
        logger.info("Analyzing coverage gaps")

        # Analyze gaps by area
        self._analyze_area_gaps()

        # Analyze requirement clusters
        self._analyze_requirement_clusters()

        # Analyze by priority
        self._analyze_priority_gaps()

        # Sort recommendations by risk level and priority
        self.recommendations.sort(
            key=lambda rec: (
                (
                    0
                    if rec.risk_level == "High"
                    else (1 if rec.risk_level == "Medium" else 2)
                ),
                (
                    0
                    if rec.priority == "High"
                    else (1 if rec.priority == "Medium" else 2)
                ),
            )
        )

        logger.info(f"Generated {len(self.recommendations)} recommendations")

    def _analyze_area_gaps(self):
        """Analyze gaps by requirement area."""
        for area_name, area in self.requirement_areas.items():
            # Skip areas with no requirements
            if area.total_reqs == 0:
                continue

            # Analyze coverage percentage
            if area.coverage_percentage < 50:
                # Create recommendation for low coverage areas
                uncovered_reqs = [
                    req_id
                    for req_id in area.requirements
                    if self.requirements[req_id].status == "Not Covered"
                ]

                self.recommendations.append(
                    GapRecommendation(
                        area=area_name,
                        priority=area.priority,
                        risk_level=area.risk_level,
                        description=f"Improve coverage for the {area_name} area (currently at {area.coverage_percentage:.1f}%)",
                        affected_requirements=uncovered_reqs,
                        effort_estimate=(
                            "High" if len(uncovered_reqs) > 5 else "Medium"
                        ),
                    )
                )

    def _analyze_requirement_clusters(self):
        """Analyze clusters of related requirements with coverage gaps."""
        # Group requirements by tags for analysis
        tag_groups = defaultdict(list)

        for req_id, req in self.requirements.items():
            for tag in req.tags:
                tag_groups[tag].append(req_id)

        # Analyze each tag group
        for tag, req_ids in tag_groups.items():
            if (
                len(req_ids) < 3
            ):  # Only consider groups with at least 3 requirements
                continue

            # Count uncovered requirements in this group
            uncovered_reqs = [
                req_id
                for req_id in req_ids
                if self.requirements[req_id].status == "Not Covered"
            ]

            # If more than 50% of requirements in the group are uncovered
            if len(uncovered_reqs) / len(req_ids) > 0.5:
                # Get the priority from the highest priority requirement
                priority = max(
                    self.requirements[req_id].priority for req_id in req_ids
                )

                # Determine risk level
                risk_level = "High" if priority == "High" else "Medium"

                self.recommendations.append(
                    GapRecommendation(
                        area="Cross-cutting",
                        priority=priority,
                        risk_level=risk_level,
                        description=f"Create scenarios for requirements with tag '{tag}' ({len(uncovered_reqs)} uncovered out of {len(req_ids)} total)",
                        affected_requirements=uncovered_reqs,
                        effort_estimate=(
                            "High" if len(uncovered_reqs) > 5 else "Medium"
                        ),
                    )
                )

    def _analyze_priority_gaps(self):
        """Analyze gaps by requirement priority."""
        priority_reqs = defaultdict(list)

        for req_id, req in self.requirements.items():
            priority_reqs[req.priority].append(req_id)

        # Check high priority requirements first
        if "High" in priority_reqs:
            high_priority_uncovered = [
                req_id
                for req_id in priority_reqs["High"]
                if self.requirements[req_id].status == "Not Covered"
            ]

            if high_priority_uncovered:
                self.recommendations.append(
                    GapRecommendation(
                        area="High Priority",
                        priority="High",
                        risk_level="High",
                        description=f"Create scenarios for {len(high_priority_uncovered)} uncovered high-priority requirements",
                        affected_requirements=high_priority_uncovered,
                        effort_estimate=(
                            "High"
                            if len(high_priority_uncovered) > 3
                            else "Medium"
                        ),
                    )
                )

        # Then check medium priority
        if "Medium" in priority_reqs:
            medium_priority_uncovered = [
                req_id
                for req_id in priority_reqs["Medium"]
                if self.requirements[req_id].status == "Not Covered"
            ]

            if (
                len(medium_priority_uncovered) > 5
            ):  # Only consider if there are many gaps
                self.recommendations.append(
                    GapRecommendation(
                        area="Medium Priority",
                        priority="Medium",
                        risk_level="Medium",
                        description=f"Create scenarios for {len(medium_priority_uncovered)} uncovered medium-priority requirements",
                        affected_requirements=medium_priority_uncovered[
                            :10
                        ],  # Limit to top 10
                        effort_estimate="High",
                    )
                )

    def generate_reports(self, output_dir: str):
        """Generate gap analysis reports."""
        logger.info(f"Generating reports in {output_dir}")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Generate main gap analysis report
        self._generate_gap_report(os.path.join(output_dir, "gap_analysis.md"))

        # Generate JSON data for further processing
        self._generate_json_data(
            os.path.join(output_dir, "gap_analysis_data.json")
        )

        # Generate action plan
        self._generate_action_plan(
            os.path.join(output_dir, "gap_action_plan.md")
        )

    def _generate_gap_report(self, output_file: str):
        """Generate the main gap analysis report in markdown."""
        logger.info(f"Generating gap report: {output_file}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# BDD Coverage Gap Analysis\n\n")

            # Executive summary
            f.write("## Executive Summary\n\n")

            total_reqs = len(self.requirements)
            covered_reqs = sum(
                1
                for req in self.requirements.values()
                if req.status in ["Fully Covered", "Partially Covered"]
            )
            coverage_pct = (
                (covered_reqs / total_reqs * 100) if total_reqs > 0 else 0
            )

            f.write(
                f"This report analyzes the BDD coverage gaps across {total_reqs} requirements "
            )
            f.write(f"in {len(self.requirement_areas)} functional areas. ")
            f.write(
                f"Overall coverage is at **{coverage_pct:.1f}%** with {covered_reqs} requirements "
            )
            f.write(f"having some level of BDD test coverage.\n\n")

            # Count high risk gaps
            high_risk_count = sum(
                1 for rec in self.recommendations if rec.risk_level == "High"
            )
            if high_risk_count > 0:
                f.write(
                    f"**{high_risk_count} high-risk coverage gaps** have been identified that require "
                )
                f.write(
                    "immediate attention to ensure proper test coverage of critical functionality.\n\n"
                )

            # Top recommendations overview
            f.write("### Top Recommendations\n\n")
            for i, rec in enumerate(self.recommendations[:3], 1):
                f.write(
                    f"{i}. **{rec.description}** (Risk: {rec.risk_level}, Priority: {rec.priority})\n"
                )
            f.write("\n")

            # Coverage by area
            f.write("## Coverage by Functional Area\n\n")
            f.write(
                "| Functional Area | Requirements | Covered | Coverage % | Risk Level |\n"
            )
            f.write(
                "|----------------|--------------|---------|------------|------------|\n"
            )

            sorted_areas = sorted(
                [
                    area
                    for area in self.requirement_areas.values()
                    if area.total_reqs > 0
                ],
                key=lambda a: a.coverage_percentage,
            )

            for area in sorted_areas:
                f.write(
                    f"| {area.name} | {area.total_reqs} | {area.covered_reqs} | "
                )
                f.write(
                    f"{area.coverage_percentage:.1f}% | {area.risk_level} |\n"
                )

            # Gap analysis by priority
            f.write("\n## Coverage Gaps by Priority\n\n")

            priority_stats = defaultdict(
                lambda: {"total": 0, "covered": 0, "uncovered": 0}
            )

            for req in self.requirements.values():
                priority_stats[req.priority]["total"] += 1
                if req.status in ["Fully Covered", "Partially Covered"]:
                    priority_stats[req.priority]["covered"] += 1
                else:
                    priority_stats[req.priority]["uncovered"] += 1

            f.write(
                "| Priority | Total Requirements | Covered | Uncovered | Coverage % |\n"
            )
            f.write(
                "|----------|---------------------|---------|-----------|------------|\n"
            )

            for priority in ["High", "Medium", "Low"]:
                if priority not in priority_stats:
                    continue

                stats = priority_stats[priority]
                coverage_pct = (
                    (stats["covered"] / stats["total"] * 100)
                    if stats["total"] > 0
                    else 0
                )

                f.write(
                    f"| {priority} | {stats['total']} | {stats['covered']} | "
                )
                f.write(f"{stats['uncovered']} | {coverage_pct:.1f}% |\n")

            # Detailed recommendations
            f.write("\n## Detailed Recommendations\n\n")

            if not self.recommendations:
                f.write(
                    "No recommendations generated. Coverage appears to be adequate across all areas.\n"
                )
            else:
                # Group recommendations by risk level
                for risk_level in ["High", "Medium", "Low"]:
                    risk_recs = [
                        rec
                        for rec in self.recommendations
                        if rec.risk_level == risk_level
                    ]
                    if not risk_recs:
                        continue

                    f.write(f"### {risk_level} Risk Recommendations\n\n")

                    for i, rec in enumerate(risk_recs, 1):
                        f.write(f"**{i}. {rec.description}**\n\n")
                        f.write(f"- **Area:** {rec.area}\n")
                        f.write(f"- **Priority:** {rec.priority}\n")
                        f.write(
                            f"- **Effort Estimate:** {rec.effort_estimate}\n"
                        )

                        if rec.affected_requirements:
                            f.write("- **Affected Requirements:**\n")
                            for req_id in rec.affected_requirements[
                                :5
                            ]:  # Show only first 5
                                req = self.requirements.get(req_id)
                                if req:
                                    f.write(
                                        f"  - REQ-{req_id}: {req.description}\n"
                                    )

                            if len(rec.affected_requirements) > 5:
                                f.write(
                                    f"  - Plus {len(rec.affected_requirements) - 5} more requirements\n"
                                )

                        f.write("\n")

            # Methodology
            f.write("## Methodology\n\n")
            f.write(
                "This gap analysis was performed by analyzing requirement coverage data against "
            )
            f.write(
                "defined functional areas. Requirements were considered covered if they had "
            )
            f.write(
                "at least one associated BDD scenario. The analysis focused on identifying "
            )
            f.write(
                "areas with low coverage, particularly those with high business priority.\n\n"
            )

            f.write(
                "Recommendations were generated based on the following criteria:\n\n"
            )
            f.write("1. Functional areas with less than 50% coverage\n")
            f.write(
                "2. Clusters of related requirements with common tags having low coverage\n"
            )
            f.write("3. High priority requirements with no BDD coverage\n")

    def _generate_json_data(self, output_file: str):
        """Generate JSON data for further processing."""
        logger.info(f"Generating JSON data: {output_file}")

        data = {
            "areas": [
                asdict(area) for area in self.requirement_areas.values()
            ],
            "requirements": [
                asdict(req) for req in self.requirements.values()
            ],
            "recommendations": [asdict(rec) for rec in self.recommendations],
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _generate_action_plan(self, output_file: str):
        """Generate an action plan for addressing the gaps."""
        logger.info(f"Generating action plan: {output_file}")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# BDD Coverage Gap Action Plan\n\n")

            if not self.recommendations:
                f.write("No coverage gaps requiring action were identified.\n")
                return

            # Write introduction
            f.write(
                "This action plan outlines the steps needed to address the coverage gaps "
            )
            f.write(
                "identified in the BDD Gap Analysis. The actions are prioritized by risk "
            )
            f.write("level and effort estimate.\n\n")

            # Sprint planning section
            f.write("## Implementation Plan\n\n")

            # Categorize by effort and risk
            immediate_actions = [
                rec
                for rec in self.recommendations
                if rec.risk_level == "High" and rec.effort_estimate != "High"
            ]

            short_term_actions = [
                rec
                for rec in self.recommendations
                if (rec.risk_level == "High" and rec.effort_estimate == "High")
                or (
                    rec.risk_level == "Medium"
                    and rec.effort_estimate != "High"
                )
            ]

            long_term_actions = [
                rec
                for rec in self.recommendations
                if rec.risk_level == "Low"
                or (
                    rec.risk_level == "Medium"
                    and rec.effort_estimate == "High"
                )
            ]

            # Immediate actions (Sprint 1)
            f.write("### Sprint 1: Immediate Actions\n\n")

            if immediate_actions:
                for i, action in enumerate(immediate_actions, 1):
                    f.write(f"**{i}. {action.description}**\n\n")
                    f.write(f"- **Area:** {action.area}\n")
                    f.write(f"- **Priority:** {action.priority}\n")
                    f.write(f"- **Effort:** {action.effort_estimate}\n")
                    f.write(
                        f"- **Requirements to Cover:** {len(action.affected_requirements)}\n\n"
                    )

                    if action.affected_requirements:
                        f.write("**Tasks:**\n\n")
                        for j, req_id in enumerate(
                            action.affected_requirements, 1
                        ):
                            req = self.requirements.get(req_id)
                            if req:
                                f.write(
                                    f"{i}.{j}. Create BDD scenarios for REQ-{req_id}: {req.description}\n"
                                )
                        f.write("\n")
            else:
                f.write("No immediate actions required.\n\n")

            # Short-term actions (Sprint 2)
            f.write("### Sprint 2: Short-term Actions\n\n")

            if short_term_actions:
                for i, action in enumerate(
                    short_term_actions[:5], 1
                ):  # Limit to 5 actions per sprint
                    f.write(f"**{i}. {action.description}**\n\n")
                    f.write(f"- **Area:** {action.area}\n")
                    f.write(f"- **Priority:** {action.priority}\n")
                    f.write(f"- **Effort:** {action.effort_estimate}\n")
                    f.write(
                        f"- **Requirements to Cover:** {len(action.affected_requirements)}\n\n"
                    )

                if len(short_term_actions) > 5:
                    f.write(
                        f"Plus {len(short_term_actions) - 5} more actions to be scheduled.\n\n"
                    )
            else:
                f.write("No short-term actions required.\n\n")

            # Long-term actions
            f.write("### Future Sprints: Long-term Actions\n\n")

            if long_term_actions:
                f.write(
                    f"There are {len(long_term_actions)} long-term actions identified. "
                )
                f.write(
                    "These should be scheduled in future sprints based on capacity and priority.\n\n"
                )

                # Group by area
                area_actions = defaultdict(list)
                for action in long_term_actions:
                    area_actions[action.area].append(action)

                for area, actions in area_actions.items():
                    f.write(f"**{area}:** {len(actions)} actions\n")
            else:
                f.write("No long-term actions required.\n\n")

            # Success criteria
            f.write("\n## Success Criteria\n\n")
            f.write(
                "The implementation of this action plan will be considered successful when:\n\n"
            )
            f.write("1. All high-risk coverage gaps have been addressed\n")
            f.write("2. Overall BDD coverage exceeds 75% of requirements\n")
            f.write("3. Each functional area has at least 50% coverage\n")
            f.write("4. All high-priority requirements have BDD coverage\n")
            f.write(
                "5. Documentation has been updated to reflect the new scenarios\n"
            )

            # Monitoring and reporting
            f.write("\n## Monitoring and Reporting\n\n")
            f.write(
                "Progress on addressing coverage gaps should be monitored through:\n\n"
            )
            f.write("1. Weekly BDD coverage reports\n")
            f.write("2. Sprint review demonstrations of new scenarios\n")
            f.write("3. Updates to the traceability matrix\n")
            f.write(
                "4. Regular gap analysis to identify new areas for improvement\n"
            )


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate a BDD gap analysis report"
    )
    parser.add_argument(
        "--coverage-data",
        required=True,
        help="JSON file containing coverage data",
    )
    parser.add_argument(
        "--requirements-file",
        required=True,
        help="File containing requirements data (CSV or JSON)",
    )
    parser.add_argument(
        "--areas-file",
        help="File containing requirement areas data (CSV or JSON)",
    )
    parser.add_argument(
        "--output-dir", required=True, help="Directory for output reports"
    )

    args = parser.parse_args()

    analyzer = BDDGapAnalyzer(
        coverage_data_file=args.coverage_data,
        requirements_file=args.requirements_file,
        areas_file=args.areas_file,
    )

    analyzer.load_data()
    analyzer.analyze_gaps()
    analyzer.generate_reports(args.output_dir)

    logger.info("BDD gap analysis complete")


if __name__ == "__main__":
    main()
