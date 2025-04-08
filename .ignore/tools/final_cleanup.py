"""
Tool: Final Cleanup
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Fix issues or clean up in the codebase
Dependencies: logging, shutil, subprocess
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
BDD Test Structure Consolidation - Phase 6: Final Cleanup

This script implements Phase 6 of the BDD Test Structure Consolidation project:
1. Verify all step definitions have been migrated
2. Remove obsolete directories
3. Update any remaining documentation

Usage:
    python final_cleanup.py
"""

import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("final_cleanup.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

# Define obsolete directories to clean up
OBSOLETE_DIRECTORIES = [
    PROJECT_ROOT / "features",
    PROJECT_ROOT / "tests" / "features",
    PROJECT_ROOT / "tests" / "step_defs",
]


def verify_step_definitions():
    """Verify all step definitions have been migrated."""
    print("\n=== Verifying Step Definitions ===")
    step_verification_script = TOOLS_DIR / "step_verification.py"

    if not step_verification_script.exists():
        logger.warning(
            f"Step verification script not found: {step_verification_script}"
        )
        print(
            f"Step verification script not found: {step_verification_script}"
        )
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(step_verification_script)],
            check=False,
            capture_output=True,
            text=True,
        )

        print(result.stdout)

        # Check if any steps are missing
        if "Some steps are missing" in result.stdout:
            choice = input(
                "\nMissing steps were found. Do you want to migrate them? (y/n): "
            )
            if choice.lower() == "y":
                migrate_missing_steps()
            else:
                print("Skipping step migration.")
                logger.info("User chose to skip step migration")

        return True
    except Exception as e:
        logger.error(f"Error running step verification: {e}")
        print(f"Error running step verification: {e}")
        return False


def migrate_missing_steps():
    """Migrate missing step definitions."""
    migration_script = TOOLS_DIR / "migrate_missing_steps.py"

    if not migration_script.exists():
        logger.warning(f"Step migration script not found: {migration_script}")
        print(f"Step migration script not found: {migration_script}")
        return False

    try:
        # Run migration script
        result = subprocess.run(
            [sys.executable, str(migration_script)],
            check=False,
            capture_output=False,  # Direct user interaction is needed
            text=True,
        )

        return result.returncode == 0
    except Exception as e:
        logger.error(f"Error running step migration: {e}")
        print(f"Error running step migration: {e}")
        return False


def remove_obsolete_directories():
    """Remove obsolete directories."""
    removed_count = 0

    for directory in OBSOLETE_DIRECTORIES:
        if not directory.exists():
            logger.info(f"Directory already removed: {directory}")
            continue

        try:
            # Check if directory is empty
            is_empty = True
            for _ in directory.glob("**/*"):
                is_empty = False
                break

            if is_empty:
                # If directory is empty, just remove it
                directory.rmdir()
                logger.info(f"Removed empty directory: {directory}")
                removed_count += 1
            else:
                # If directory is not empty, confirm with user before removing
                print(f"\nDirectory not empty: {directory}")
                print("Contents:")
                for item in directory.glob("**/*"):
                    if item.is_file():
                        print(f"  - {item.relative_to(PROJECT_ROOT)}")

                choice = input(
                    f"\nDo you want to remove this directory and all its contents? (y/n): "
                )
                if choice.lower() == "y":
                    shutil.rmtree(directory)
                    logger.info(
                        f"Removed directory with contents: {directory}"
                    )
                    removed_count += 1
                else:
                    logger.info(f"Skipped removal of directory: {directory}")
                    print(f"Skipped removal of: {directory}")
        except Exception as e:
            logger.error(f"Error removing directory {directory}: {e}")
            print(f"Error removing directory {directory}: {e}")

    return removed_count


def update_readme():
    """Update the main README.md with final BDD structure information."""
    readme_path = PROJECT_ROOT / "README.md"

    if not readme_path.exists():
        logger.warning(f"README.md not found at {readme_path}")
        return False

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update BDD section or add if it doesn't exist
        bdd_section = """
## BDD Testing

BDD tests are now consolidated in the `tests/bdd` directory:

- `tests/bdd/features/`: Contains all feature files
- `tests/bdd/steps/`: Contains all step definitions
- `tests/bdd/environment.py`: Environment setup for BDD tests

For more information on running and writing BDD tests, see the [BDD Testing documentation](tests/bdd/README.md).
"""

        # Check if there's an existing BDD testing section
        bdd_section_match = re.search(
            r"## BDD Testing\s.*?(?=\n##|\Z)", content, re.DOTALL
        )

        if bdd_section_match:
            # Replace existing section
            content = (
                content[: bdd_section_match.start()]
                + bdd_section
                + content[bdd_section_match.end() :]
            )
        else:
            # Add new section at the end
            content += bdd_section

        # Write updated content
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info(f"Updated README.md with final BDD structure information")
        return True
    except Exception as e:
        logger.error(f"Error updating README.md: {e}")
        return False


def create_summary_file():
    """Create a summary file describing the consolidation process."""
    summary_path = (
        PROJECT_ROOT / "docs" / "project" / "BDD_CONSOLIDATION_SUMMARY.md"
    )

    # Create directory if it doesn't exist
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(
                """# BDD Test Structure Consolidation Summary

## Overview

The BDD test structure consolidation project has been completed. This project involved consolidating
all BDD-related files into a single, standardized structure to improve maintainability and organization.

## Consolidated Structure

All BDD tests are now located in the `tests/bdd` directory with the following structure:

```
tests/bdd/
├── features/     # Contains all feature files
├── steps/        # Contains all step definitions
└── environment.py # Environment setup for BDD tests
```

## Configuration

BDD testing is configured through:

- `pytest.ini`: Contains pytest configuration for BDD tests
- `behave.ini`: Contains behave-specific configuration

## Running BDD Tests

BDD tests can be run using either pytest or behave:

### Using pytest

```bash
pytest tests/bdd
```

### Using behave

```bash
behave tests/bdd/features
```

## Consolidation Process

The consolidation was completed in six phases:

1. **Preparation**: Created backups and updated documentation
2. **Feature File Consolidation**: Migrated and merged feature files
3. **Step Definition Consolidation**: Migrated and merged step definitions
4. **Configuration Cleanup**: Updated configuration files
5. **Verification**: Ran BDD tests to verify the consolidation
6. **Final Cleanup**: Removed obsolete directories and updated documentation

## Completion Date

This consolidation project was completed on {datetime.datetime.now().strftime('%Y-%m-%d')}.
"""
            )

        logger.info(f"Created consolidation summary file at {summary_path}")
        return True
    except Exception as e:
        logger.error(f"Error creating consolidation summary file: {e}")
        return False


def main():
    """Main function to execute the final cleanup process"""
    logger.info("Starting Phase 6: Final Cleanup")

    # Step 0: Verify step definitions
    verify_step_definitions()

    # Step 1: Remove obsolete directories
    print("\n=== Removing obsolete directories ===")
    removed_count = remove_obsolete_directories()
    print(f"Removed {removed_count} obsolete directories")

    # Step 2: Update README.md
    print("\n=== Updating documentation ===")
    if update_readme():
        print("Updated README.md with final BDD structure information")
    else:
        print("Failed to update README.md")

    # Step 3: Create consolidation summary file
    if create_summary_file():
        print(
            "Created consolidation summary file at docs/project/BDD_CONSOLIDATION_SUMMARY.md"
        )
    else:
        print("Failed to create consolidation summary file")

    logger.info("Phase 6: Final Cleanup completed")
    print("\nPhase 6: Final Cleanup completed")
    print("\nBDD Test Structure Consolidation project is now complete!")
    print(
        "\nThe consolidated BDD test structure is now available at tests/bdd."
    )
    print(
        "For more information, see the documentation at tests/bdd/README.md and"
    )
    print(
        "the consolidation summary at docs/project/BDD_CONSOLIDATION_SUMMARY.md."
    )


if __name__ == "__main__":
    import datetime

    main()
