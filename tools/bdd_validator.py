"""
Tool: Bdd Validator
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Validate BDD feature files for compliance with standards
Dependencies: None
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
BDD Validator Tool

This tool validates BDD implementation against our best practices.
It integrates with repo_health_check.py and can be run independently.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class BDDValidator:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.validation_rules_path = (
            workspace_root / "docs/project/bdd/validation/bdd_rules.json"
        )
        self.feature_dir = workspace_root / "tests/bdd/features"
        self.steps_dir = workspace_root / "tests/bdd/steps"
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def load_validation_rules(self) -> Dict:
        """Load validation rules from JSON file."""
        try:
            with open(self.validation_rules_path) as f:
                return json.load(f)
        except FileNotFoundError:
            self.errors.append(
                f"Validation rules file not found: {self.validation_rules_path}"
            )
            return {}

    def validate_feature_structure(self, feature_file: Path) -> None:
        """Validate a feature file's structure."""
        with open(feature_file) as f:
            content = f.read()

        # Check for required sections
        required_patterns = {
            "Feature tag": r"@[A-Z]+-[A-Z]+-\d+",
            "Feature name": r"Feature:",
            "As a": r"As a .+",
            "I want": r"I want .+",
            "So that": r"So that .+",
        }

        for name, pattern in required_patterns.items():
            if not re.search(pattern, content):
                self.errors.append(f"{feature_file}: Missing {name}")

        # Check scenario structure
        scenarios = re.finditer(
            r"Scenario:.*?(?=Scenario:|$)", content, re.DOTALL
        )
        for scenario in scenarios:
            scenario_text = scenario.group()
            if not re.search(r"Given .+", scenario_text):
                self.errors.append(
                    f"{feature_file}: Scenario missing Given step"
                )
            if not re.search(r"When .+", scenario_text):
                self.errors.append(
                    f"{feature_file}: Scenario missing When step"
                )
            if not re.search(r"Then .+", scenario_text):
                self.errors.append(
                    f"{feature_file}: Scenario missing Then step"
                )

    def validate_step_definitions(self, step_file: Path) -> None:
        """Validate step definition file structure and naming."""
        with open(step_file) as f:
            content = f.read()

        # Check for docstring
        if not re.search(r'""".*?"""', content, re.DOTALL):
            self.errors.append(f"{step_file}: Missing module docstring")

        # Check step function naming
        step_funcs = re.finditer(
            r"@(?:given|when|then)\('.*?'\)\s*def\s+(\w+)", content
        )
        for match in step_funcs:
            func_name = match.group(1)
            if not re.match(r"step_(?:given|when|then)_\w+", func_name):
                self.errors.append(
                    f"{step_file}: Invalid step function name: {func_name}"
                )

    def validate_directory_structure(self) -> None:
        """Validate BDD directory structure."""
        required_dirs = [
            self.feature_dir,
            self.steps_dir,
            self.workspace_root / "docs/project/bdd",
            self.workspace_root / "docs/project/bdd/templates",
            self.workspace_root / "docs/project/bdd/validation",
        ]

        for directory in required_dirs:
            if not directory.exists():
                self.errors.append(f"Required directory missing: {directory}")

    def validate_all(self) -> Tuple[List[str], List[str]]:
        """Run all validations."""
        self.validate_directory_structure()

        # Validate feature files
        if self.feature_dir.exists():
            for feature_file in self.feature_dir.rglob("*.feature"):
                self.validate_feature_structure(feature_file)

        # Validate step definitions
        if self.steps_dir.exists():
            for step_file in self.steps_dir.rglob("*_steps.py"):
                self.validate_step_definitions(step_file)

        return self.errors, self.warnings


def main():
    """Main entry point for the validator."""
    workspace_root = Path(__file__).parent.parent
    validator = BDDValidator(workspace_root)
    errors, warnings = validator.validate_all()

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"⚠️  {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"❌ {error}")
        exit(1)

    print("✅ BDD validation passed!")
    exit(0)


if __name__ == "__main__":
    main()
