"""
Tool: Bdd Docs Generator
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Generate documentation from BDD feature files
Dependencies: ast, dataclasses, markdown, yaml, jinja2
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
BDD Documentation Generator

Generates comprehensive documentation from BDD features and step definitions including:
- Living documentation from feature files
- Searchable step catalog
- Coverage reports
- Requirement traceability
"""

import argparse
import ast
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader


@dataclass
class StepDefinition:
    """Step definition metadata."""

    step_type: str  # given, when, then
    pattern: str  # step pattern
    function: str  # function name
    docstring: str  # function docstring
    file_path: str  # source file
    line_number: int  # line number
    args: List[str]  # function arguments
    raises: List[str]  # documented exceptions


@dataclass
class Scenario:
    """Scenario metadata."""

    name: str
    tags: List[str]
    steps: List[str]
    examples: Optional[List[Dict[str, str]]] = None


@dataclass
class Feature:
    """Feature metadata."""

    path: Path
    name: str
    description: List[str]
    tags: List[str]
    background: Optional[List[str]]
    scenarios: List[Scenario]


@dataclass
class Requirement:
    """Requirement tracking."""

    req_id: str
    features: List[str]
    scenarios: List[str]
    step_coverage: List[str]


class BDDDocGenerator:
    """Main documentation generator class."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.features_dir = base_dir / "tests/bdd/features"
        self.steps_dir = base_dir / "tests/bdd/steps"
        self.docs_dir = base_dir / "docs/bdd"
        self.template_dir = base_dir / "tools/templates"

        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Data structures
        self.features: Dict[str, Feature] = {}
        self.step_defs: Dict[str, StepDefinition] = {}
        self.requirements: Dict[str, Requirement] = {}

        # Ensure output directories exist
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        (self.docs_dir / "features").mkdir(exist_ok=True)
        (self.docs_dir / "steps").mkdir(exist_ok=True)
        (self.docs_dir / "requirements").mkdir(exist_ok=True)

    def parse_features(self) -> None:
        """Parse all feature files."""
        for feature_file in self.features_dir.rglob("*.feature"):
            feature = self._parse_feature_file(feature_file)
            self.features[feature.name] = feature
            self._update_requirements(feature)

    def _parse_feature_file(self, path: Path) -> Feature:
        """Parse a single feature file."""
        content = path.read_text()
        lines = content.split("\n")

        # Extract feature metadata
        feature_match = re.search(r"Feature: (.+)$", content, re.MULTILINE)
        if not feature_match:
            raise ValueError(f"No feature found in {path}")

        name = feature_match.group(1).strip()

        # Extract tags
        tags = []
        for line in lines:
            if line.strip().startswith("@"):
                tags.extend(tag.strip() for tag in line.strip().split("@")[1:])

        # Extract description (lines between Feature and first Scenario/Background)
        description = []
        for line in lines[lines.index(f"Feature: {name}") + 1 :]:
            if line.strip().startswith(("Scenario:", "Background:", "@")):
                break
            if line.strip():
                description.append(line.strip())

        # Extract background
        background = None
        background_match = re.search(
            r"Background:(.+?)(?=Scenario:|$)", content, re.DOTALL
        )
        if background_match:
            background = [
                line.strip()
                for line in background_match.group(1).split("\n")
                if line.strip() and not line.strip().startswith("Background:")
            ]

        # Extract scenarios
        scenarios = []
        scenario_blocks = re.finditer(
            r"(?:@[^\n]+\n)?Scenario(?:\sOutline)?:(.+?)(?=(?:@|\Z|\n\s*Scenario))",
            content,
            re.DOTALL,
        )

        for block in scenario_blocks:
            scenario_text = block.group(0)
            scenario_lines = scenario_text.split("\n")

            # Get scenario tags
            scenario_tags = []
            for line in scenario_lines:
                if line.strip().startswith("@"):
                    scenario_tags.extend(
                        tag.strip() for tag in line.strip().split("@")[1:]
                    )

            # Get scenario name
            name_match = re.search(
                r"Scenario(?:\sOutline)?:\s*(.+)$", scenario_text, re.MULTILINE
            )
            if not name_match:
                continue
            scenario_name = name_match.group(1).strip()

            # Get steps
            steps = []
            for line in scenario_lines:
                step_match = re.match(
                    r"\s*(Given|When|Then|And|But)\s+(.+)$", line
                )
                if step_match:
                    steps.append(line.strip())

            # Get examples if they exist
            examples = None
            examples_match = re.search(
                r"Examples:(.+?)(?=(?:@|\Z|\n\s*Scenario))",
                scenario_text,
                re.DOTALL,
            )
            if examples_match:
                examples_text = examples_match.group(1)
                # Parse the examples table
                examples = self._parse_table(examples_text)

            scenarios.append(
                Scenario(
                    name=scenario_name,
                    tags=scenario_tags,
                    steps=steps,
                    examples=examples,
                )
            )

        return Feature(
            path=path,
            name=name,
            description=description,
            tags=tags,
            background=background,
            scenarios=scenarios,
        )

    def parse_step_definitions(self) -> None:
        """Parse all step definition files."""
        for step_file in self.steps_dir.rglob("*.py"):
            if step_file.name.startswith("__"):
                continue
            self._parse_step_file(step_file)

    def _parse_step_file(self, path: Path) -> None:
        """Parse a single step definition file."""
        try:
            with open(path) as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Look for step decorators
                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Call):
                            if isinstance(
                                decorator.func, ast.Name
                            ) and decorator.func.id in [
                                "given",
                                "when",
                                "then",
                            ]:
                                # Extract step pattern from decorator
                                pattern = ast.literal_eval(decorator.args[0])

                                # Extract docstring
                                docstring = ast.get_docstring(node) or ""

                                # Extract arguments
                                args = [
                                    arg.arg
                                    for arg in node.args.args
                                    if arg.arg != "self"
                                ]

                                # Extract raises from docstring
                                raises = []
                                for line in docstring.split("\n"):
                                    if "raises:" in line.lower():
                                        raises.append(
                                            line.split(":")[-1].strip()
                                        )

                                self.step_defs[pattern] = StepDefinition(
                                    step_type=decorator.func.id,
                                    pattern=pattern,
                                    function=node.name,
                                    docstring=docstring,
                                    file_path=str(path),
                                    line_number=node.lineno,
                                    args=args,
                                    raises=raises,
                                )
        except Exception as e:
            print(f"Error parsing {path}: {e}")

    def _update_requirements(self, feature: Feature) -> None:
        """Update requirements tracking from feature metadata."""
        # Extract requirement IDs from tags
        req_ids = [tag for tag in feature.tags if tag.startswith("REQ-")]
        for scenario in feature.scenarios:
            req_ids.extend(
                tag for tag in scenario.tags if tag.startswith("REQ-")
            )

        # Update requirements tracking
        for req_id in req_ids:
            if req_id not in self.requirements:
                self.requirements[req_id] = Requirement(
                    req_id=req_id, features=[], scenarios=[], step_coverage=[]
                )
            req = self.requirements[req_id]
            if feature.name not in req.features:
                req.features.append(feature.name)
            for scenario in feature.scenarios:
                if scenario.name not in req.scenarios:
                    req.scenarios.append(scenario.name)
                for step in scenario.steps:
                    if step not in req.step_coverage:
                        req.step_coverage.append(step)

    def _parse_table(self, table_text: str) -> List[Dict[str, str]]:
        """Parse a Gherkin table into a list of dictionaries."""
        lines = [
            line.strip() for line in table_text.split("\n") if "|" in line
        ]
        if not lines:
            return []

        # Extract headers
        headers = [
            cell.strip() for cell in lines[0].split("|") if cell.strip()
        ]

        # Parse rows
        result = []
        for line in lines[1:]:
            cells = [cell.strip() for cell in line.split("|") if cell.strip()]
            if len(cells) == len(headers):
                result.append(dict(zip(headers, cells)))

        return result

    def generate_documentation(self) -> None:
        """Generate all documentation."""
        self.parse_features()
        self.parse_step_definitions()

        # Generate feature documentation
        self._generate_feature_docs()

        # Generate step catalog
        self._generate_step_catalog()

        # Generate requirements coverage
        self._generate_requirements_docs()

        # Generate index
        self._generate_index()

    def _generate_feature_docs(self) -> None:
        """Generate documentation for each feature."""
        template = self.env.get_template("feature.md.j2")
        features_dir = self.docs_dir / "features"

        for feature in self.features.values():
            output = template.render(feature=feature)
            (
                features_dir / f"{feature.name.lower().replace(' ', '_')}.md"
            ).write_text(output)

    def _generate_step_catalog(self) -> None:
        """Generate searchable step catalog."""
        template = self.env.get_template("step_catalog.md.j2")
        output = template.render(steps=self.step_defs)
        (self.docs_dir / "steps" / "catalog.md").write_text(output)

    def _generate_requirements_docs(self) -> None:
        """Generate requirements coverage documentation."""
        template = self.env.get_template("requirements.md.j2")
        output = template.render(requirements=self.requirements)
        (self.docs_dir / "requirements" / "coverage.md").write_text(output)

    def _generate_index(self) -> None:
        """Generate documentation index."""
        template = self.env.get_template("index.md.j2")
        output = template.render(
            features=self.features,
            step_count=len(self.step_defs),
            req_count=len(self.requirements),
        )
        (self.docs_dir / "index.md").write_text(output)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate BDD documentation")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path.cwd(),
        help="Base directory containing the project",
    )
    args = parser.parse_args()

    generator = BDDDocGenerator(args.base_dir)
    generator.generate_documentation()


if __name__ == "__main__":
    main()
