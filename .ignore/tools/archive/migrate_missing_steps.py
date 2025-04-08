"""
Tool: Migrate Missing Steps
Created: 2025-03-21
Author: Development Team
Status: Archived
Purpose: Tool for migrate missing steps
Dependencies: ast, glob, logging, behave
Lifecycle:
    - Created: To automate common development tasks
    - Active: Archived for reference but no longer actively used
    - Obsolescence Conditions:
        1. When project requirements change significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
BDD Missing Steps Migration Tool

This script identifies missing steps in the consolidated step repository
and migrates them from legacy step definition files.

Usage:
    python migrate_missing_steps.py
"""

import ast
import glob
import logging
import os
import re
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("migrate_missing_steps.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def extract_steps_from_file(file_path):
    """Extract step patterns from a step definition file."""
    steps = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all step decorators (given, when, then)
        step_pattern = re.compile(
            r'@(given|when|then)\s*\(\s*[\'"](.+?)[\'"]\s*\)'
        )
        matches = step_pattern.finditer(content)

        for match in matches:
            step_type = match.group(1)  # given, when, or then
            step_pattern = match.group(2)  # The actual pattern
            steps.append((step_type, step_pattern))

    except Exception as e:
        logger.error(f"Error extracting steps from {file_path}: {e}")

    return steps


def find_all_step_files(directory):
    """Find all step definition files in a directory."""
    return glob.glob(os.path.join(directory, "**/*.py"), recursive=True)


def find_missing_steps(legacy_file, consolidated_dirs):
    """Find steps missing from consolidated files."""
    # Extract steps from legacy file
    legacy_steps = extract_steps_from_file(legacy_file)
    logger.info(
        f"Found {len(legacy_steps)} steps in legacy file {legacy_file}"
    )

    # Extract all steps from consolidated files
    consolidated_steps = []
    for directory in consolidated_dirs:
        step_files = find_all_step_files(directory)
        for file_path in step_files:
            file_steps = extract_steps_from_file(file_path)
            for step in file_steps:
                consolidated_steps.append(
                    (step[0], step[1], os.path.basename(file_path))
                )

    # Find missing steps
    missing_steps = []
    for legacy_step in legacy_steps:
        step_type, step_pattern = legacy_step

        # Check if this step exists in consolidated steps
        found = False
        for cons_step in consolidated_steps:
            cons_type, cons_pattern, cons_file = cons_step
            if step_type == cons_type and step_pattern == cons_pattern:
                found = True
                break

        if not found:
            missing_steps.append(legacy_step)

    logger.info(f"Found {len(missing_steps)} missing steps")
    return missing_steps, legacy_steps


def extract_step_implementation(file_path, step_type, step_pattern):
    """Extract the implementation of a step from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse the Python code
        tree = ast.parse(content)

        # Find the step function
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check if this function has the step decorator
                for decorator in node.decorator_list:
                    if (
                        isinstance(decorator, ast.Call)
                        and isinstance(decorator.func, ast.Name)
                        and decorator.func.id == step_type
                        and len(decorator.args) > 0
                        and isinstance(decorator.args[0], ast.Constant)
                        and decorator.args[0].value == step_pattern
                    ):

                        # Extract the function code
                        function_lines = content.splitlines()[
                            node.lineno - 1 : node.end_lineno
                        ]
                        return "\n".join(function_lines)

        logger.warning(
            f"Could not find implementation for @{step_type}('{step_pattern}') in {file_path}"
        )
        return None

    except Exception as e:
        logger.error(f"Error extracting implementation from {file_path}: {e}")
        return None


def migrate_steps(legacy_file, target_file, missing_steps):
    """Migrate missing steps from legacy file to target file."""
    # Get implementations of missing steps
    implementations = []
    for step_type, step_pattern in missing_steps:
        implementation = extract_step_implementation(
            legacy_file, step_type, step_pattern
        )
        if implementation:
            implementations.append(implementation)

    # Ensure target file exists
    if not os.path.exists(target_file):
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(
                """\"\"\"
Command Line Interface step definitions for BDD tests.
\"\"\"
from behave import given, when, then

"""
            )

    # Append implementations to target file
    with open(target_file, "a", encoding="utf-8") as f:
        for implementation in implementations:
            f.write("\n\n" + implementation)

    logger.info(
        f"Migrated {len(implementations)} step implementations to {target_file}"
    )
    return len(implementations)


def main():
    """Main function to run the migration."""
    # Define paths
    project_root = Path(__file__).parent.parent.absolute()
    legacy_file = (
        project_root
        / "features"
        / "steps"
        / "command_line_interface_steps.py.bak"
    )
    consolidated_dir = project_root / "tests" / "bdd" / "steps"
    target_file = consolidated_dir / "command_line_interface_steps.py"

    logger.info("Starting BDD Missing Steps Migration")
    print(f"Legacy file: {legacy_file}")
    print(f"Consolidated directory: {consolidated_dir}")
    print(f"Target file: {target_file}")

    # Find missing steps
    missing_steps, all_steps = find_missing_steps(
        legacy_file, [consolidated_dir]
    )

    # Report missing steps
    if missing_steps:
        print("\n=== Missing Steps ===")
        for step_type, step_pattern in missing_steps:
            print(f"@{step_type}('{step_pattern}')")

        # Migrate steps
        choice = input(
            f"\nDo you want to migrate these {len(missing_steps)} steps to {target_file}? (y/n): "
        )
        if choice.lower() == "y":
            count = migrate_steps(legacy_file, target_file, missing_steps)
            print(f"\nMigrated {count} step implementations to {target_file}")
            print(
                f"Please review the migrated steps and make any necessary modifications."
            )
        else:
            print("\nSkipped migration of missing steps.")
    else:
        print(
            "\n✅ All steps have already been migrated to the consolidated repository."
        )

    # Create a migration report
    report_path = project_root / "reports" / "step_migration_report.md"
    os.makedirs(report_path.parent, exist_ok=True)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# BDD Step Migration Report\n\n")
        f.write(f"Legacy file: `{legacy_file}`\n\n")
        f.write(f"## Total Steps: {len(all_steps)}\n\n")
        f.write(f"## Missing Steps: {len(missing_steps)}\n\n")

        if missing_steps:
            f.write("### List of Missing Steps\n\n")
            for step_type, step_pattern in missing_steps:
                f.write(f"- `@{step_type}('{step_pattern}')`\n")

        f.write("\n## Migration Status\n\n")

        if missing_steps:
            if choice.lower() == "y":
                f.write(
                    f"✅ {count} steps have been migrated to `{target_file}`\n"
                )
                if count < len(missing_steps):
                    f.write(
                        f"⚠️ {len(missing_steps) - count} steps could not be migrated automatically\n"
                    )
            else:
                f.write("❌ Migration was skipped by user\n")
        else:
            f.write("✅ All steps have already been migrated\n")

    print(f"\nMigration report created at {report_path}")


if __name__ == "__main__":
    main()
