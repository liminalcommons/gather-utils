"""
Tool: Update Bdd Docs
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Generate documentation from BDD feature files
Dependencies: logging, pytest_bdd
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
BDD Documentation Update Script

This script updates the BDD testing documentation to reflect the new consolidated structure
as part of the BDD Test Structure Consolidation project (Phase 1).
"""

import datetime
import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bdd_docs_update.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define the new BDD structure documentation
NEW_BDD_STRUCTURE_DOC = """# BDD Testing Structure

This document outlines the consolidated BDD testing structure for the project.

## Directory Structure

All BDD tests are now organized under the `tests/bdd` directory:

```
tests/bdd/
├── features/     # Contains all feature files
├── steps/        # Contains all step definitions
└── environment.py # Environment setup for BDD tests
```

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

## Configuration

BDD testing is configured through the following files:

- `pytest.ini`: Contains pytest configuration for BDD tests
- `behave.ini`: Contains behave-specific configuration

## Writing BDD Tests

### Feature Files

Feature files should be placed in the `tests/bdd/features` directory and follow this format:

```gherkin
Feature: Feature name
  As a [role]
  I want [feature]
  So that [benefit]

  Scenario: Scenario name
    Given [precondition]
    When [action]
    Then [expected result]
```

### Step Definitions

Step definitions should be placed in the `tests/bdd/steps` directory and follow this format:

```python
from pytest_bdd import given, when, then

@given("precondition")
def step_impl(context):
    # Implementation
    pass

@when("action")
def step_impl(context):
    # Implementation
    pass

@then("expected result")
def step_impl(context):
    # Implementation
    pass
```

## Best Practices

1. Keep feature files focused on business requirements
2. Write step definitions that are reusable
3. Use tags to categorize and filter tests
4. Maintain a consistent naming convention

Last updated: {date}
"""


def update_readme():
    """Update the BDD README file with the new structure."""
    bdd_readme_path = PROJECT_ROOT / "tests" / "bdd" / "README.md"

    # Create the directory if it doesn't exist
    bdd_readme_path.parent.mkdir(parents=True, exist_ok=True)

    # Format the documentation with the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    doc_content = NEW_BDD_STRUCTURE_DOC.format(date=current_date)

    # Write the documentation to the README file
    try:
        with open(bdd_readme_path, "w") as f:
            f.write(doc_content)
        logger.info(f"Updated BDD README at: {bdd_readme_path}")
    except Exception as e:
        logger.error(f"Failed to update BDD README: {e}")


def update_main_readme():
    """Update the main README.md file with information about the new BDD structure."""
    main_readme_path = PROJECT_ROOT / "README.md"

    if not main_readme_path.exists():
        logger.warning(f"Main README not found at: {main_readme_path}")
        return

    try:
        with open(main_readme_path, "r") as f:
            content = f.read()

        # Check if there's a BDD testing section to update
        bdd_section_start = content.find("## BDD Testing")

        if bdd_section_start == -1:
            # If no BDD section exists, append it to the end
            bdd_section = """
## BDD Testing

BDD tests are located in the `tests/bdd` directory. For more information on running and writing BDD tests,
see the [BDD Testing documentation](tests/bdd/README.md).
"""
            content += bdd_section
        else:
            # Find the end of the BDD section (next ## heading)
            next_section = content.find("##", bdd_section_start + 1)
            if next_section == -1:
                next_section = len(content)

            # Replace the BDD section
            bdd_section = """
## BDD Testing

BDD tests are located in the `tests/bdd` directory. For more information on running and writing BDD tests,
see the [BDD Testing documentation](tests/bdd/README.md).
"""
            content = (
                content[:bdd_section_start]
                + bdd_section
                + content[next_section:]
            )

        # Write the updated content back to the README
        with open(main_readme_path, "w") as f:
            f.write(content)

        logger.info(f"Updated main README with BDD testing information")
    except Exception as e:
        logger.error(f"Failed to update main README: {e}")


def main():
    """Main function to execute the documentation update process."""
    logger.info("Starting BDD documentation update process")

    try:
        # Update the BDD README
        update_readme()

        # Update the main README
        update_main_readme()

        logger.info("Documentation update completed successfully")
        print("\nDocumentation update completed successfully!")

    except Exception as e:
        logger.error(f"Documentation update process failed: {e}")
        print(f"Documentation update process failed. See log for details.")


if __name__ == "__main__":
    main()
