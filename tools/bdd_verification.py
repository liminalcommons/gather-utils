"""
Tool: Bdd Verification
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Supports BDD testing and development workflows
Dependencies: logging, subprocess
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
BDD Test Structure Consolidation - Phase 5: Verification

This script implements Phase 5 of the BDD Test Structure Consolidation project:
1. Run the BDD tests to verify that the consolidation has not broken anything
2. Report the test results

Usage:
    python bdd_verification.py
"""

import logging
import os
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bdd_verification.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()


def run_pytest_bdd_tests():
    """Run BDD tests using pytest."""
    try:
        logger.info("Running BDD tests using pytest...")
        print("\n=== Running BDD tests using pytest ===")

        command = [sys.executable, "-m", "pytest", "tests/bdd", "-v"]
        result = subprocess.run(
            command,
            check=False,  # Don't raise exception on test failures
            capture_output=True,
            text=True,
        )

        print("\nPytest BDD Test Results:")
        print("------------------------")
        print(result.stdout)

        if result.stderr:
            logger.warning(f"Pytest stderr: {result.stderr}")
            if (
                len(result.stderr) < 1000
            ):  # Only print if it's reasonably short
                print("\nWarnings/Errors:")
                print(result.stderr)

        success = result.returncode == 0
        logger.info(
            f"Pytest BDD tests {'passed' if success else 'failed'} with return code {result.returncode}"
        )

        return success
    except Exception as e:
        logger.error(f"Error running pytest BDD tests: {e}")
        print(f"\nError running pytest BDD tests: {e}")
        return False


def run_behave_tests():
    """Run BDD tests using behave."""
    try:
        logger.info("Running BDD tests using behave...")
        print("\n=== Running BDD tests using behave ===")

        # Create reports directory if it doesn't exist
        reports_dir = PROJECT_ROOT / "reports" / "junit"
        reports_dir.mkdir(parents=True, exist_ok=True)

        command = ["behave", "tests/bdd/features", "-v"]
        result = subprocess.run(
            command,
            check=False,  # Don't raise exception on test failures
            capture_output=True,
            text=True,
        )

        print("\nBehave Test Results:")
        print("-------------------")
        print(result.stdout)

        if result.stderr:
            logger.warning(f"Behave stderr: {result.stderr}")
            if (
                len(result.stderr) < 1000
            ):  # Only print if it's reasonably short
                print("\nWarnings/Errors:")
                print(result.stderr)

        success = result.returncode == 0
        logger.info(
            f"Behave tests {'passed' if success else 'failed'} with return code {result.returncode}"
        )

        return success
    except Exception as e:
        logger.error(f"Error running behave tests: {e}")
        print(f"\nError running behave tests: {e}")
        return False


def main():
    """Main function to execute the verification process"""
    logger.info("Starting Phase 5: Verification")

    # Track overall success
    overall_success = True

    # Run BDD tests using pytest
    pytest_success = run_pytest_bdd_tests()
    overall_success = overall_success and pytest_success

    # Run BDD tests using behave
    behave_success = run_behave_tests()
    overall_success = overall_success and behave_success

    # Report overall status
    if overall_success:
        logger.info(
            "Phase 5: Verification completed successfully - all tests passed"
        )
        print(
            "\n✅ Phase 5: Verification completed successfully - all tests passed"
        )
    else:
        logger.warning("Phase 5: Verification completed with test failures")
        print("\n⚠️ Phase 5: Verification completed with test failures")
        print(
            "\nSome tests failed. You may need to fix these issues before proceeding."
        )

    print("\nNext steps:")
    if not overall_success:
        print("1. Fix any issues that arose during testing")
    print(
        f"{'2' if not overall_success else '1'}. Proceed to Phase 6: Final Cleanup"
    )

    return 0 if overall_success else 1


if __name__ == "__main__":
    sys.exit(main())
