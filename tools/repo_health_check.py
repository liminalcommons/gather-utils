#!/usr/bin/env python
"""
Repository Health Check Tool

This tool validates the repository structure and contents.
"""
import os
import sys
import subprocess
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple

from bdd_validator import BDDValidator

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
        text=True
    )
    
    # Parse coverage output
    # Implementation details...

def check_code_quality():
    """Run linters and code quality checks."""
    print("Checking code quality...")
    # Run flake8
    result = subprocess.run(
        ["flake8", "src", "tests"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("Code quality issues found:")
        print(result.stdout)
        return False
    
    return True

def check_for_redundancy():
    """Check for redundant or duplicate files."""
    print("Checking for redundancy...")
    # Implementation details...

def validate_repository_structure_for_agent():
    """
    Validate repository structure for agent compatibility.
    
    Checks:
    - Required directories exist
    - Documentation structure is correct
    - Test organization follows conventions
    - Source code structure is navigable
    """
    print("Validating repository structure for agent compatibility...")
    
    # Define required directories and files
    required_dirs = [
        "src",
        "tests",
        "docs",
        "tools",
        "reports"
    ]
    
    required_files = [
        "README.md",
        "docs/project/MAINTENANCE_GUIDELINES.md",
        "pytest.ini"
    ]
    
    # Check required directories
    missing_dirs = []
    for directory in required_dirs:
        if not os.path.isdir(directory):
            missing_dirs.append(directory)
    
    if missing_dirs:
        print(f"Missing required directories: {', '.join(missing_dirs)}")
        return False
    
    # Check required files
    missing_files = []
    for file in required_files:
        if not os.path.isfile(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"Missing required files: {', '.join(missing_files)}")
        return False
    
    # Check test organization
    if not os.path.isdir("tests/bdd") or not os.path.isdir("tests/unit"):
        print("Tests should be organized into BDD and unit test directories")
        return False
    
    # Check documentation structure
    if not os.path.isdir("docs/project") or not os.path.isdir("docs/api"):
        print("Documentation should include project and API directories")
        return False
    
    print("Repository structure is valid for agent compatibility")
    return True

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
    """Main entry point for the health check."""
    parser = argparse.ArgumentParser(description="Check repository health")
    parser.add_argument("--validate-for-agent", action="store_true",
                      help="Validate repository for agent operations")
    parser.add_argument("--validate-bdd", action="store_true",
                      help="Run BDD validation")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    errors = []
    warnings = []

    if args.validate_for_agent:
        agent_errors, agent_warnings = validate_for_agent(root)
        errors.extend(agent_errors)
        warnings.extend(agent_warnings)
    elif args.validate_bdd:
        bdd_validator = BDDValidator(root)
        bdd_errors, bdd_warnings = bdd_validator.validate_all()
        errors.extend(bdd_errors)
        warnings.extend(bdd_warnings)

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"⚠️  {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"❌ {error}")
        sys.exit(1)

    print("✅ Repository health check passed!")
    sys.exit(0)

if __name__ == "__main__":
    main()
