"""
Tool: Tdd Validator
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Tool for tdd validator
Dependencies: glob
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
TDD Validator for test files.

This tool validates that test files have proper TDD metadata and follow
the established lifecycle management conventions. It checks for required fields
in the metadata section and ensures they follow the expected format.

Usage:
    python tools/tdd_validator.py --validate-metadata
    python tools/tdd_validator.py --list-tests-missing-metadata
    python tools/tdd_validator.py --fix-missing-metadata
"""

import argparse
import datetime
import glob
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Required metadata fields that must be present in every test file
REQUIRED_METADATA_FIELDS = [
    "Created:",
    "Last Updated:",
    "Status:",
    "Owner:",
    "Purpose:",
    "Lifecycle:",
    "Last Validated:",
]

# Valid status values
VALID_STATUS_VALUES = ["Active", "Draft", "Deprecated", "Archived"]

# Regular expressions to extract metadata
METADATA_SECTION_RE = r'"""(?:[^"]*?Test Metadata[^"]*?)"""'
CREATED_DATE_RE = r"Created:\s*([\d-]+)"
UPDATED_DATE_RE = r"Last Updated:\s*([\d-]+)"
STATUS_RE = r"Status:\s*(\w+)"
OWNER_RE = r"Owner:\s*(.+?)(?:\n|$)"
PURPOSE_RE = r"Purpose:\s*(.+?)(?:\n|$)"
LIFECYCLE_RE = r"Lifecycle:\s*(.+?)(?:\n\s*-|$)"
CREATED_REASON_RE = r"Created:\s*(.+?)(?:\n|$)"
ACTIVE_STATUS_RE = r"Active:\s*(.+?)(?:\n|$)"
OBSOLESCENCE_RE = r"Obsolescence Conditions:"
LAST_VALIDATED_RE = r"Last Validated:\s*([\d-]+)"

# ANSI color codes for terminal output
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def find_test_files(directory: str = "tests") -> List[str]:
    """
    Find all Python test files in the specified directory.

    Args:
        directory: The directory to search for test files

    Returns:
        A list of paths to Python test files
    """
    test_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                test_files.append(os.path.join(root, file))
    return test_files


def extract_metadata(file_path: str) -> Optional[Dict[str, str]]:
    """
    Extract metadata section from a test file.

    Args:
        file_path: Path to the test file

    Returns:
        A dictionary of metadata fields and values, or None if no metadata found
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Try to find the metadata section
    section_match = re.search(METADATA_SECTION_RE, content, re.DOTALL)
    if not section_match:
        return None

    metadata_section = section_match.group(0)

    # Extract individual fields
    metadata = {}
    metadata["created_date"] = extract_field(metadata_section, CREATED_DATE_RE)
    metadata["updated_date"] = extract_field(metadata_section, UPDATED_DATE_RE)
    metadata["status"] = extract_field(metadata_section, STATUS_RE)
    metadata["owner"] = extract_field(metadata_section, OWNER_RE)
    metadata["purpose"] = extract_field(metadata_section, PURPOSE_RE)
    metadata["lifecycle"] = (
        "present" if "Lifecycle:" in metadata_section else None
    )
    metadata["created_reason"] = extract_field(
        metadata_section, CREATED_REASON_RE
    )
    metadata["active_status"] = extract_field(
        metadata_section, ACTIVE_STATUS_RE
    )
    metadata["obsolescence"] = (
        "present" if re.search(OBSOLESCENCE_RE, metadata_section) else None
    )
    metadata["last_validated"] = extract_field(
        metadata_section, LAST_VALIDATED_RE
    )

    return metadata


def extract_field(text: str, pattern: str) -> Optional[str]:
    """
    Extract a field value using a regex pattern.

    Args:
        text: The text to search
        pattern: Regex pattern with a capture group

    Returns:
        The captured value or None if not found
    """
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return None


def validate_metadata(
    metadata: Optional[Dict[str, str]], file_path: str
) -> Tuple[bool, List[str]]:
    """
    Validate the extracted metadata against requirements.

    Args:
        metadata: Dictionary of metadata fields and values
        file_path: Path to the test file for reporting

    Returns:
        A tuple containing a boolean (valid or not) and a list of error messages
    """
    errors = []

    if metadata is None:
        return False, [f"No metadata section found in {file_path}"]

    # Check required fields
    if metadata["created_date"] is None:
        errors.append(f"Missing Created date in {file_path}")
    if metadata["updated_date"] is None:
        errors.append(f"Missing Last Updated date in {file_path}")
    if metadata["status"] is None:
        errors.append(f"Missing Status in {file_path}")
    elif metadata["status"] not in VALID_STATUS_VALUES:
        errors.append(
            f"Invalid Status value '{metadata['status']}' in {file_path}"
        )
    if metadata["owner"] is None:
        errors.append(f"Missing Owner in {file_path}")
    if metadata["purpose"] is None:
        errors.append(f"Missing Purpose in {file_path}")
    if metadata["lifecycle"] is None:
        errors.append(f"Missing Lifecycle section in {file_path}")
    if metadata["created_reason"] is None:
        errors.append(
            f"Missing Created reason in Lifecycle section in {file_path}"
        )
    if metadata["active_status"] is None:
        errors.append(
            f"Missing Active status in Lifecycle section in {file_path}"
        )
    if metadata["obsolescence"] is None:
        errors.append(
            f"Missing Obsolescence Conditions in Lifecycle section in {file_path}"
        )
    if metadata["last_validated"] is None:
        errors.append(f"Missing Last Validated date in {file_path}")

    # Validate date formats if present
    for date_field, date_value in [
        ("Created", metadata["created_date"]),
        ("Last Updated", metadata["updated_date"]),
        ("Last Validated", metadata["last_validated"]),
    ]:
        if date_value and not re.match(r"^\d{4}-\d{2}-\d{2}$", date_value):
            errors.append(
                f"Invalid {date_field} date format '{date_value}' in {file_path}"
            )

    return len(errors) == 0, errors


def generate_metadata_template() -> str:
    """
    Generate a template for the TDD metadata section.

    Returns:
        A string containing a properly formatted metadata template
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    return f'''"""
Unit tests for [component].

Test Metadata:
- Created: {today}
- Last Updated: {today}
- Status: Active
- Owner: Development Team
- Purpose: [Describe what these tests validate]
- Lifecycle:
  - Created: [Reason for creating these tests]
  - Active: [Current usage description]
  - Obsolescence Conditions:
    1. [When these tests would be considered obsolete]
    2. [Another condition if applicable]
- Last Validated: {today}
"""'''


def fix_missing_metadata(file_path: str) -> bool:
    """
    Add metadata to a test file that doesn't have it.

    Args:
        file_path: Path to the test file

    Returns:
        True if metadata was added, False otherwise
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if metadata already exists
    if re.search(METADATA_SECTION_RE, content, re.DOTALL):
        return False

    # Generate metadata
    metadata = generate_metadata_template()

    # Add metadata after any module-level docstring or at the top of the file
    module_docstring_match = re.match(r'""".*?"""', content, re.DOTALL)
    if module_docstring_match:
        updated_content = (
            content[: module_docstring_match.end()]
            + "\n\n"
            + metadata
            + content[module_docstring_match.end() :]
        )
    else:
        # Add after any shebang or coding line
        first_import = re.search(r"^import|^from", content, re.MULTILINE)
        if first_import:
            updated_content = (
                content[: first_import.start()]
                + metadata
                + "\n\n"
                + content[first_import.start() :]
            )
        else:
            updated_content = metadata + "\n\n" + content

    # Write updated content
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    return True


def main():
    """Main entry point for the TDD validator."""
    parser = argparse.ArgumentParser(
        description="Validate TDD metadata in test files"
    )
    parser.add_argument(
        "--validate-metadata",
        action="store_true",
        help="Validate metadata in all test files",
    )
    parser.add_argument(
        "--list-tests-missing-metadata",
        action="store_true",
        help="List test files missing metadata",
    )
    parser.add_argument(
        "--fix-missing-metadata",
        action="store_true",
        help="Add metadata to test files missing it",
    )
    parser.add_argument(
        "--directory",
        type=str,
        default="tests",
        help="Directory to search for test files",
    )
    args = parser.parse_args()

    # Find all test files
    test_files = find_test_files(args.directory)
    print(f"Found {len(test_files)} test files")

    if args.validate_metadata:
        all_valid = True
        error_count = 0
        files_with_metadata = 0
        files_without_metadata = 0

        for file_path in test_files:
            metadata = extract_metadata(file_path)
            if metadata:
                files_with_metadata += 1
                valid, errors = validate_metadata(metadata, file_path)
                if not valid:
                    all_valid = False
                    error_count += len(errors)
                    print(f"\nErrors in {file_path}:")
                    for error in errors:
                        print(f"  - {error}")
            else:
                files_without_metadata += 1
                all_valid = False
                print(f"\nNo metadata found in {file_path}")

        print(f"\nSummary:")
        print(f"- Files with metadata: {files_with_metadata}")
        print(f"- Files without metadata: {files_without_metadata}")
        print(f"- Total errors: {error_count}")

        if all_valid:
            print("\nAll test files have valid metadata!")
            sys.exit(0)
        else:
            print("\nSome test files have missing or invalid metadata.")
            sys.exit(1)

    elif args.list_tests_missing_metadata:
        missing_metadata = []
        for file_path in test_files:
            metadata = extract_metadata(file_path)
            if not metadata:
                missing_metadata.append(file_path)

        if missing_metadata:
            print("Test files missing metadata:")
            for file_path in missing_metadata:
                print(f"  - {file_path}")
            print(f"\nTotal: {len(missing_metadata)} files missing metadata")
            sys.exit(1)
        else:
            print("All test files have metadata!")
            sys.exit(0)

    elif args.fix_missing_metadata:
        fixed_count = 0
        for file_path in test_files:
            metadata = extract_metadata(file_path)
            if not metadata:
                if fix_missing_metadata(file_path):
                    fixed_count += 1
                    print(f"Added metadata to {file_path}")

        print(f"\nAdded metadata to {fixed_count} test files")
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
