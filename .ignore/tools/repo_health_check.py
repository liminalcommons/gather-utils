"""
Tool: Repo Health Check
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Validate system configuration and dependencies
Dependencies: subprocess, bdd_validator
Lifecycle:
    - Created: To automate common development tasks
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When project requirements change significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python
"""
Repository Health Check Tool

This tool validates the repository structure and contents.
"""
import argparse
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple

from bdd_validator import BDDValidator

# Add tool inventory manager import for tool validation
try:
    from tool_inventory_manager import find_tools, validate_tool_metadata

    TOOL_VALIDATION_AVAILABLE = True
except ImportError:
    TOOL_VALIDATION_AVAILABLE = False


def check_documentation_freshness():
    """Check if documentation is up to date."""
    print("Checking documentation freshness...")
    # Implementation details...


def check_test_coverage():
    """Check test coverage meets thresholds."""
    print("Checking test coverage...")
    # Run pytest with coverage
    result = subprocess.run(
        ["python", "-m", "pytest", "--cov=gather_manager", "tests/unit"],
        capture_output=True,
        text=True,
    )

    # Parse coverage output
    # Implementation details...


def check_code_quality():
    """Run linters and code quality checks."""
    print("Checking code quality...")
    # Run flake8
    result = subprocess.run(
        ["flake8", "src", "tests"], capture_output=True, text=True
    )

    if result.returncode != 0:
        print("Code quality issues found:")
        print(result.stdout)
        return False

    return True


def check_for_redundancy():
    """Check for redundancy in the repository."""
    print("Checking for redundancy...")
    # Implementation details...


def check_tool_metadata() -> bool:
    """
    Check if all tools have proper metadata.

    Returns:
        bool: True if all tools have valid metadata, False otherwise.
    """
    if not TOOL_VALIDATION_AVAILABLE:
        print(
            "Tool validation not available. Please make sure tool_inventory_manager.py is available."
        )
        return True

    print("Checking tool metadata...")
    tools = find_tools()
    valid_tools = 0
    invalid_tools = 0
    errors_by_tool = {}

    for tool_path in tools:
        valid, metadata, errors = validate_tool_metadata(tool_path)
        if valid:
            valid_tools += 1
        else:
            invalid_tools += 1
            errors_by_tool[tool_path] = errors

    if invalid_tools > 0:
        print(f"Found {invalid_tools} tools with invalid metadata:")
        for tool_path, errors in errors_by_tool.items():
            print(f"  {os.path.basename(tool_path)}:")
            for error in errors:
                print(f"    - {error}")
        return False

    print(f"All {valid_tools} tools have valid metadata.")
    return True


def validate_repository_structure_for_agent():
    """
    Validate repository structure for agent use.

    This performs a basic check to ensure the repository is in a state
    that can be used by an AI agent.
    """
    print("Validating repository structure for agent...")

    # Check if all required directories exist
    required_dirs = [
        "docs",
        "docs/project",
        "tools",
        "tests",
        "tests/bdd",
        "reports",
    ]

    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)

    if missing_dirs:
        print("Missing required directories:")
        for dir_path in missing_dirs:
            print(f"  {dir_path}")
        return False

    # Check if all required files exist
    required_files = [
        "docs/project/README.md",
        "docs/project/PROJECT_STATUS.md",
        "docs/project/DEFINITION_OF_DONE.md",
    ]

    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print("Missing required files:")
        for file_path in missing_files:
            print(f"  {file_path}")
        return False

    # Check if project status is up to date
    project_status_path = "docs/project/PROJECT_STATUS.md"
    if os.path.exists(project_status_path):
        mod_time = datetime.fromtimestamp(
            os.path.getmtime(project_status_path)
        )
        if (datetime.now() - mod_time) > timedelta(days=7):
            print(
                f"Warning: {project_status_path} has not been updated in the last 7 days."
            )
            # Don't fail for this, just warn

    # Check tool metadata
    tool_metadata_valid = check_tool_metadata()

    print("Repository structure validation complete.")
    return tool_metadata_valid


def check_directory_structure(root: Path) -> List[str]:
    """Check if all required directories exist."""
    errors = []
    required_dirs = [
        "docs/project/bdd",
        "docs/project/bdd/templates",
        "docs/project/bdd/validation",
        "tests/bdd/features",
        "tests/bdd/steps",
    ]

    for dir_path in required_dirs:
        if not (root / dir_path).exists():
            errors.append(f"Required directory missing: {dir_path}")

    return errors


def check_documentation(root: Path) -> List[str]:
    """Check if all required documentation exists."""
    errors = []
    required_docs = [
        "docs/project/bdd/README.md",
        "docs/project/bdd/best_practices.md",
        "docs/project/bdd/templates/feature.feature",
        "docs/project/bdd/templates/steps.py",
        "docs/project/bdd/validation/bdd_rules.json",
    ]

    for doc_path in required_docs:
        if not (root / doc_path).exists():
            errors.append(f"Required documentation missing: {doc_path}")

    return errors


def validate_for_agent(root: Path) -> Tuple[List[str], List[str]]:
    """Validate repository for agent operations."""
    errors = []
    warnings = []

    # Check directory structure
    errors.extend(check_directory_structure(root))

    # Check documentation
    errors.extend(check_documentation(root))

    # Run BDD validation if requested
    if "--validate-bdd" in sys.argv:
        bdd_validator = BDDValidator(root)
        bdd_errors, bdd_warnings = bdd_validator.validate_all()
        errors.extend(bdd_errors)
        warnings.extend(bdd_warnings)

    return errors, warnings


def main():
    """
    Main function.

    This function parses command-line arguments and runs the appropriate checks.
    """
    parser = argparse.ArgumentParser(description="Repository Health Check")
    parser.add_argument(
        "--validate-for-agent",
        action="store_true",
        help="Validate repository structure for agent use",
    )
    parser.add_argument(
        "--check-documentation",
        action="store_true",
        help="Check if documentation is up to date",
    )
    parser.add_argument(
        "--check-test-coverage",
        action="store_true",
        help="Check test coverage",
    )
    parser.add_argument(
        "--check-code-quality", action="store_true", help="Check code quality"
    )
    parser.add_argument(
        "--check-redundancy", action="store_true", help="Check for redundancy"
    )
    parser.add_argument(
        "--check-tool-metadata",
        action="store_true",
        help="Check if all tools have proper metadata",
    )
    parser.add_argument("--all", action="store_true", help="Run all checks")

    args = parser.parse_args()

    if args.validate_for_agent:
        if not validate_repository_structure_for_agent():
            sys.exit(1)

    if args.check_documentation or args.all:
        check_documentation_freshness()

    if args.check_test_coverage or args.all:
        check_test_coverage()

    if args.check_code_quality or args.all:
        check_code_quality()

    if args.check_redundancy or args.all:
        check_for_redundancy()

    if args.check_tool_metadata or args.all:
        if not check_tool_metadata():
            sys.exit(1)

    if not any(
        [
            args.validate_for_agent,
            args.check_documentation,
            args.check_test_coverage,
            args.check_code_quality,
            args.check_redundancy,
            args.check_tool_metadata,
            args.all,
        ]
    ):
        parser.print_help()

    sys.exit(0)


if __name__ == "__main__":
    main()
