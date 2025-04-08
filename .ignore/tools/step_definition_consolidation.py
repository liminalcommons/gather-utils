"""
Tool: Step Definition Consolidation
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Tool for step definition consolidation
Dependencies: ast, difflib, logging, shutil
Lifecycle:
    - Created: To automate common development tasks
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When project requirements change significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 3: Step Definition Consolidation

This script implements Phase 3 of the BDD Test Structure Consolidation project:
1. Compare step definitions across different directories
2. Migrate unique step definitions to the consolidated structure
3. Clean up obsolete step definition files

Usage:
    python step_definition_consolidation.py
    python step_definition_consolidation.py --cleanup  # To remove obsolete files
"""

import ast
import difflib
import logging
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("step_definition_consolidation.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define step definition directories
STEP_DIRECTORIES = [
    PROJECT_ROOT / "features" / "steps",
    PROJECT_ROOT / "tests" / "step_defs",
    PROJECT_ROOT / "tests" / "bdd" / "steps",
]

# Target directory for consolidated step definitions
TARGET_DIRECTORY = PROJECT_ROOT / "tests" / "bdd" / "steps"


class StepDefinition:
    """Class to represent a step definition file with its metadata and step functions"""

    def __init__(self, path):
        self.path = path
        self.name = path.name
        self.content = self._read_content()
        self.stem = path.stem
        self.relative_path = path.relative_to(path.parent.parent.parent)
        self.step_functions = self._extract_step_functions()

    def _read_content(self):
        """Read the content of the step definition file"""
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading {self.path}: {e}")
            return ""

    def _extract_step_functions(self):
        """Extract step functions from the file"""
        step_functions = []
        if not self.content:
            return step_functions

        try:
            # Parse the Python file
            tree = ast.parse(self.content)

            # Find step function decorators (given, when, then)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Call) and hasattr(
                            decorator.func, "id"
                        ):
                            if decorator.func.id in ["given", "when", "then"]:
                                # Extract step pattern from the decorator arguments
                                if decorator.args:
                                    step_pattern = (
                                        decorator.args[0].s
                                        if hasattr(decorator.args[0], "s")
                                        else str(decorator.args[0])
                                    )
                                    step_functions.append(
                                        {
                                            "type": decorator.func.id,
                                            "pattern": step_pattern,
                                            "function_name": node.name,
                                            "node": node,
                                        }
                                    )
        except SyntaxError as e:
            logger.error(f"Syntax error in {self.path}: {e}")
        except Exception as e:
            logger.error(
                f"Error extracting step functions from {self.path}: {e}"
            )

        return step_functions

    def __eq__(self, other):
        """Check if two step definition files are identical based on content"""
        return self.content == other.content

    def similarity(self, other):
        """Calculate similarity between two step definition files"""
        if not self.content or not other.content:
            return 0

        s = difflib.SequenceMatcher(None, self.content, other.content)
        return s.ratio()

    def has_overlapping_steps(self, other):
        """Check if two step definition files have overlapping step patterns"""
        my_patterns = {step["pattern"] for step in self.step_functions}
        other_patterns = {step["pattern"] for step in other.step_functions}
        return bool(my_patterns.intersection(other_patterns))


def collect_step_definition_files():
    """Collect all step definition files from different directories"""
    step_files = []

    for directory in STEP_DIRECTORIES:
        if not directory.exists():
            logger.warning(f"Directory not found: {directory}")
            continue

        logger.info(f"Collecting step definition files from: {directory}")
        for file_path in directory.glob("**/*.py"):
            if file_path.name == "__init__.py" or file_path.name.startswith(
                "_"
            ):
                continue  # Skip __init__.py and other special files

            step_file = StepDefinition(file_path)
            if (
                step_file.step_functions
            ):  # Only include files with step functions
                step_files.append(step_file)
                logger.info(
                    f"Found step definition file: {file_path} with {len(step_file.step_functions)} step functions"
                )

    logger.info(f"Collected {len(step_files)} step definition files in total")
    return step_files


def group_similar_step_files(step_files):
    """Group similar step definition files together"""
    groups = defaultdict(list)

    # First group by name
    for step_file in step_files:
        groups[step_file.stem].append(step_file)

    # Then check for similar content within groups
    final_groups = []
    for name, files in groups.items():
        if len(files) == 1:
            final_groups.append(files)
            continue

        # Group files with similar content
        content_groups = []
        for file in files:
            found_group = False
            for group in content_groups:
                if file.similarity(
                    group[0]
                ) > 0.7 or file.has_overlapping_steps(
                    group[0]
                ):  # 70% similarity threshold or overlapping steps
                    group.append(file)
                    found_group = True
                    break

            if not found_group:
                content_groups.append([file])

        final_groups.extend(content_groups)

    # Also group files with overlapping step definitions across different names
    # This is a more complex problem requiring a second pass
    i = 0
    while i < len(final_groups):
        merged = False
        j = i + 1
        while j < len(final_groups):
            if any(
                file1.has_overlapping_steps(file2)
                for file1 in final_groups[i]
                for file2 in final_groups[j]
            ):
                # Merge groups if they have overlapping step patterns
                final_groups[i].extend(final_groups[j])
                final_groups.pop(j)
                merged = True
            else:
                j += 1

        if not merged:
            i += 1

    return final_groups


def select_best_step_file(step_group):
    """Select the best step definition file from a group"""
    # Prefer files from tests/bdd/steps
    for step_file in step_group:
        if "tests/bdd/steps" in str(step_file.path):
            return step_file

    # Next, prefer files from tests/step_defs
    for step_file in step_group:
        if "tests/step_defs" in str(step_file.path):
            return step_file

    # Default to the file with the most step functions
    return max(step_group, key=lambda x: len(x.step_functions))


def merge_step_functions(step_group):
    """Merge step functions from multiple files into one file"""
    base_file = select_best_step_file(step_group)

    # If there's only one file in the group, just return it
    if len(step_group) == 1:
        return base_file

    # Create a new file combining step functions from all files
    merged_content = f"""# Merged step definitions from multiple files
# Original files:
{chr(10).join(f'# - {step_file.path}' for step_file in step_group)}

{base_file.content}

# --- Merged step functions from other files ---

"""

    # Track patterns that have already been included
    existing_patterns = {step["pattern"] for step in base_file.step_functions}

    # Add unique step functions from other files
    for step_file in step_group:
        if step_file == base_file:
            continue

        for step in step_file.step_functions:
            if step["pattern"] not in existing_patterns:
                # Extract the function definition
                try:
                    source_lines = step_file.content.splitlines()
                    func_lines = ast.unparse(step["node"]).splitlines()

                    # Add a comment indicating the source
                    merged_content += f"\n# From {step_file.path}\n"

                    # Add the function with its decorator
                    merged_content += "\n".join(func_lines) + "\n\n"

                    existing_patterns.add(step["pattern"])
                except Exception as e:
                    logger.error(f"Error extracting function: {e}")

    # Create a new StepDefinition object with the merged content
    merged_file = StepDefinition(base_file.path)
    merged_file.content = merged_content

    return merged_file


def migrate_step_definition_files(step_groups):
    """Migrate and merge step definition files to the target directory"""
    # Create target directory if it doesn't exist
    TARGET_DIRECTORY.mkdir(parents=True, exist_ok=True)

    migrated_files = []

    for group in step_groups:
        # Merge step functions from the group
        merged_file = merge_step_functions(group)

        # Define target path
        target_path = TARGET_DIRECTORY / merged_file.name

        # Skip if the file is already in the target directory and no merging was needed
        if "tests/bdd/steps" in str(merged_file.path) and len(group) == 1:
            logger.info(
                f"File already in target directory: {merged_file.path}"
            )
            migrated_files.append(merged_file)
            continue

        # Write the merged file to the target directory
        try:
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(merged_file.content)

            logger.info(
                f"{'Merged' if len(group) > 1 else 'Migrated'} step definition file: {merged_file.path} -> {target_path}"
            )

            # Update the path of the migrated file
            merged_file.path = target_path
            migrated_files.append(merged_file)
        except Exception as e:
            logger.error(
                f"Error writing step definition file {target_path}: {e}"
            )

    logger.info(
        f"Migrated {len(migrated_files)} step definition files to {TARGET_DIRECTORY}"
    )
    return migrated_files


def ensure_init_file():
    """Ensure __init__.py exists in the target directory"""
    init_file = TARGET_DIRECTORY / "__init__.py"
    if not init_file.exists():
        try:
            with open(init_file, "w", encoding="utf-8") as f:
                f.write("# Step definitions package\n")
            logger.info(f"Created __init__.py in {TARGET_DIRECTORY}")
        except Exception as e:
            logger.error(f"Error creating __init__.py: {e}")


def clean_up_obsolete_files(migrated_files, perform_cleanup=False):
    """Clean up obsolete step definition files"""
    # First, identify all step definition files
    all_step_paths = []
    for directory in STEP_DIRECTORIES:
        if not directory.exists():
            continue
        for file_path in directory.glob("**/*.py"):
            if (
                file_path.name != "__init__.py"
                and not file_path.name.startswith("_")
            ):
                all_step_paths.append(file_path)

    # Identify files to keep (those in the target directory)
    files_to_keep = [f.path for f in migrated_files]

    # Identify files to remove (those not in the target directory)
    files_to_remove = [
        path
        for path in all_step_paths
        if path not in files_to_keep and "tests/bdd/steps" not in str(path)
    ]

    if not files_to_remove:
        logger.info("No obsolete step definition files found")
        print("\nNo obsolete step definition files found")
        return

    logger.info(f"Found {len(files_to_remove)} obsolete step definition files")

    if perform_cleanup:
        # Actually remove the files
        removed_count = 0
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                logger.info(
                    f"Removed obsolete step definition file: {file_path}"
                )
                removed_count += 1
            except Exception as e:
                logger.error(f"Error removing file {file_path}: {e}")

        logger.info(f"Removed {removed_count} obsolete step definition files")
        print(f"\nRemoved {removed_count} obsolete step definition files")

        # Check if any directories are now empty and can be removed
        check_empty_directories()
    else:
        # Just report the files to be removed
        print(
            "\nThe following step definition files are now obsolete and can be removed:"
        )
        for file_path in files_to_remove:
            print(f"  - {file_path}")

        print("\nTo complete cleanup, run this script with the --cleanup flag")


def check_empty_directories():
    """Check for empty directories that can be removed"""
    empty_dirs = []

    # Check if the source directories are now empty
    for directory in [
        PROJECT_ROOT / "features" / "steps",
        PROJECT_ROOT / "tests" / "step_defs",
    ]:
        if not directory.exists():
            continue

        # Check if the directory has any Python files (excluding __init__.py)
        has_py_files = False
        for path in directory.glob("**/*.py"):
            if path.name != "__init__.py" and not path.name.startswith("_"):
                has_py_files = True
                break

        if not has_py_files:
            empty_dirs.append(directory)

    if empty_dirs:
        print(
            "\nThe following directories no longer contain step definition files and can be removed:"
        )
        for directory in empty_dirs:
            print(f"  - {directory}")


def report_migration_results(step_groups, migrated_files):
    """Report the results of the migration"""
    print("\n=== Step Definition Consolidation Summary ===")
    print(
        f"Total step definition files found: {sum(len(group) for group in step_groups)}"
    )
    print(f"Step definition file groups: {len(step_groups)}")
    print(
        f"Step definition files migrated to {TARGET_DIRECTORY}: {len(migrated_files)}"
    )

    # Print details of each group
    print("\nStep Definition File Groups:")
    for i, group in enumerate(step_groups, 1):
        print(f"\nGroup {i}:")

        # Identify which file was migrated
        migrated_stems = [f.stem for f in migrated_files]

        for step_file in group:
            status = "MIGRATED" if step_file.stem in migrated_stems else ""
            step_count = len(step_file.step_functions)
            print(f"  - {step_file.path} ({step_count} steps) {status}")


def main(perform_cleanup=False):
    """Main function to execute the step definition consolidation process"""
    logger.info(
        f"Starting Phase 3: Step Definition Consolidation (cleanup={perform_cleanup})"
    )

    # Step 1: Collect all step definition files
    step_files = collect_step_definition_files()

    # Step 2: Group similar step definition files
    step_groups = group_similar_step_files(step_files)
    logger.info(
        f"Grouped step definition files into {len(step_groups)} groups"
    )

    # Step 3: Ensure __init__.py exists in the target directory
    ensure_init_file()

    # Step 4: Migrate and merge step definition files to the target directory
    migrated_files = migrate_step_definition_files(step_groups)

    # Step 5: Clean up obsolete step definition files
    clean_up_obsolete_files(migrated_files, perform_cleanup)

    # Step 6: Report the results
    report_migration_results(step_groups, migrated_files)

    logger.info("Phase 3: Step Definition Consolidation completed")
    print("\nPhase 3: Step Definition Consolidation completed")
    print("\nNext steps:")
    if not perform_cleanup:
        print(
            "1. Review the consolidated step definition files in tests/bdd/steps"
        )
        print(
            "2. Run this script with the --cleanup flag to remove obsolete files"
        )
    print(
        f"{'3' if not perform_cleanup else '1'}. Proceed to Phase 4: Configuration Cleanup"
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="BDD Step Definition Consolidation"
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Clean up obsolete step definition files",
    )
    args = parser.parse_args()

    main(perform_cleanup=args.cleanup)
