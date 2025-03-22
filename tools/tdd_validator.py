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
TDD Validator Tool.

This tool validates TDD test files for proper metadata and generates reports
on test status and lifecycle.

Usage:
    python tools/tdd_validator.py --validate-metadata
    python tools/tdd_validator.py --validate-status
    python tools/tdd_validator.py --generate-lifecycle-report
"""

import argparse
import glob
import os
import re
import sys
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Constants
TEST_DIRS = ["tests/unit", "tests/integration"]
REQUIRED_METADATA_FIELDS = [
    "Created",
    "Last Updated",
    "Status",
    "Owner",
    "Purpose",
    "Lifecycle",
    "Last Validated"
]
VALID_STATUS_VALUES = ["Draft", "Active", "Deprecated", "Archived"]
METADATA_PATTERN = r'"""[\s\S]*?Test Metadata:[\s\S]*?(?:"""|\n\n)'

# ANSI color codes for terminal output
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def find_test_files() -> List[str]:
    """
    Find all test files in the project.
    
    Returns:
        List[str]: A list of paths to test files.
    """
    test_files = []
    for test_dir in TEST_DIRS:
        if os.path.exists(test_dir):
            for root, _, files in os.walk(test_dir):
                for file in files:
                    if file.startswith("test_") and file.endswith(".py"):
                        test_files.append(os.path.join(root, file))
    return test_files


def extract_metadata(file_path: str) -> Optional[str]:
    """
    Extract metadata block from a test file.
    
    Args:
        file_path (str): Path to the test file.
        
    Returns:
        Optional[str]: The metadata block if found, None otherwise.
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()
            
        # Look for metadata in docstring
        match = re.search(METADATA_PATTERN, content)
        if match:
            return match.group(0)
        return None
    except Exception as e:
        print(f"{COLOR_RED}Error reading {file_path}: {e}{COLOR_RESET}")
        return None


def parse_metadata(metadata_str: str) -> Dict[str, str]:
    """
    Parse metadata string into a dictionary.
    
    Args:
        metadata_str (str): The metadata string to parse.
        
    Returns:
        Dict[str, str]: Dictionary of metadata fields.
    """
    metadata = {}
    if not metadata_str:
        return metadata
        
    # Extract lines that look like metadata (- Key: Value)
    lines = metadata_str.split("\n")
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("- ") and ":" in line:
            parts = line[2:].split(":", 1)
            if len(parts) == 2:
                key, value = parts
                key = key.strip()
                value = value.strip()
                
                # Handle multi-line values for Lifecycle
                if key == "Lifecycle":
                    # Since Lifecycle is a nested structure, just store a placeholder
                    metadata[key] = "Present"
                elif key in ["Created", "Last Updated", "Last Validated"]:
                    # For date fields, try to find the actual date value
                    value_parts = value.split()
                    if value_parts and len(value_parts[0]) == 10 and value_parts[0].count("-") == 2:
                        # This looks like a date in YYYY-MM-DD format
                        metadata[key] = value_parts[0]
                    else:
                        metadata[key] = value
                else:
                    metadata[key] = value
                
    return metadata


def validate_metadata(file_path: str, metadata: Dict[str, str]) -> List[str]:
    """
    Validate metadata for required fields and values.
    
    Args:
        file_path (str): Path to the test file.
        metadata (Dict[str, str]): Parsed metadata.
        
    Returns:
        List[str]: List of validation errors.
    """
    errors = []
    
    # Check for required fields
    for field in REQUIRED_METADATA_FIELDS:
        if field not in metadata:
            errors.append(f"Missing required field: {field}")
    
    # Validate Status field
    if "Status" in metadata and metadata["Status"] not in VALID_STATUS_VALUES:
        errors.append(f"Invalid Status value: {metadata['Status']}. " 
                     f"Must be one of {VALID_STATUS_VALUES}")
    
    # Validate dates - only check format if field exists and is not the special Lifecycle placeholder
    for date_field in ["Created", "Last Updated", "Last Validated"]:
        if date_field in metadata and metadata[date_field] != "Present":
            try:
                # Only try to parse if it looks like a date
                if len(metadata[date_field]) >= 10 and metadata[date_field].count("-") == 2:
                    datetime.strptime(metadata[date_field][:10], "%Y-%m-%d")
            except ValueError:
                errors.append(f"Invalid date format for {date_field}: {metadata[date_field]}. "
                             "Use YYYY-MM-DD")
    
    return errors


def validate_test_file_metadata(file_path: str) -> Tuple[bool, List[str]]:
    """
    Validate metadata for a test file.
    
    Args:
        file_path (str): Path to the test file.
        
    Returns:
        Tuple[bool, List[str]]: Success status and list of errors.
    """
    metadata_str = extract_metadata(file_path)
    if not metadata_str:
        return False, ["No metadata found in test file"]
        
    metadata = parse_metadata(metadata_str)
    errors = validate_metadata(file_path, metadata)
    
    return len(errors) == 0, errors


def validate_all_metadata() -> bool:
    """
    Validate metadata for all test files.
    
    Returns:
        bool: True if all tests have valid metadata, False otherwise.
    """
    test_files = find_test_files()
    all_valid = True
    valid_count = 0
    invalid_count = 0
    
    print(f"{COLOR_BLUE}Validating metadata for {len(test_files)} test files...{COLOR_RESET}")
    
    for file_path in test_files:
        valid, errors = validate_test_file_metadata(file_path)
        if valid:
            print(f"{COLOR_GREEN}✓ {file_path}{COLOR_RESET}")
            valid_count += 1
        else:
            print(f"{COLOR_RED}✗ {file_path}{COLOR_RESET}")
            for error in errors:
                print(f"  {COLOR_RED}- {error}{COLOR_RESET}")
            invalid_count += 1
            all_valid = False
    
    print(f"\n{COLOR_BLUE}Summary:{COLOR_RESET}")
    print(f"{COLOR_GREEN}Valid: {valid_count}{COLOR_RESET}")
    print(f"{COLOR_RED}Invalid: {invalid_count}{COLOR_RESET}")
    
    return all_valid


def validate_test_status() -> bool:
    """
    Run tests and validate their passing status.
    
    Returns:
        bool: True if all tests pass, False otherwise.
    """
    print(f"{COLOR_BLUE}Validating test status...{COLOR_RESET}")
    print(f"{COLOR_YELLOW}Running pytest to check test status{COLOR_RESET}")
    
    # Run pytest with verbose output
    import subprocess
    result = subprocess.run(["pytest", "-v"], capture_output=True, text=True)
    
    # Print output
    print(result.stdout)
    
    return result.returncode == 0


def generate_lifecycle_report() -> None:
    """Generate a report on the lifecycle status of all tests."""
    test_files = find_test_files()
    status_counts = {"Draft": 0, "Active": 0, "Deprecated": 0, "Archived": 0, "Missing": 0}
    tests_by_status = {"Draft": [], "Active": [], "Deprecated": [], "Archived": [], "Missing": []}
    
    print(f"{COLOR_BLUE}Generating lifecycle report for {len(test_files)} test files...{COLOR_RESET}")
    
    for file_path in test_files:
        metadata_str = extract_metadata(file_path)
        if not metadata_str:
            status_counts["Missing"] += 1
            tests_by_status["Missing"].append(file_path)
            continue
            
        metadata = parse_metadata(metadata_str)
        if "Status" in metadata and metadata["Status"] in VALID_STATUS_VALUES:
            status = metadata["Status"]
            status_counts[status] += 1
            tests_by_status[status].append(file_path)
        else:
            status_counts["Missing"] += 1
            tests_by_status["Missing"].append(file_path)
    
    # Generate report
    report_path = "docs/project/tdd/validation/lifecycle_report.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, "w") as f:
        f.write("---\n")
        f.write("Title: TDD Lifecycle Status Report\n")
        f.write(f"Created: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("Status: Active\n")
        f.write("Owner: Development Team\n")
        f.write("Purpose: Report on the lifecycle status of TDD tests\n")
        f.write("---\n\n")
        
        f.write("# TDD Lifecycle Status Report\n\n")
        f.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Summary\n\n")
        f.write("| Status | Count | Percentage |\n")
        f.write("|--------|-------|------------|\n")
        
        total = len(test_files)
        for status in ["Draft", "Active", "Deprecated", "Archived", "Missing"]:
            count = status_counts[status]
            percentage = (count / total) * 100 if total > 0 else 0
            f.write(f"| {status} | {count} | {percentage:.1f}% |\n")
            
        f.write("\n## Test Files by Status\n\n")
        
        for status in ["Draft", "Active", "Deprecated", "Archived", "Missing"]:
            f.write(f"### {status} Tests ({status_counts[status]})\n\n")
            if tests_by_status[status]:
                for file_path in tests_by_status[status]:
                    f.write(f"- `{file_path}`\n")
            else:
                f.write("*No tests in this category*\n")
            f.write("\n")
    
    print(f"{COLOR_GREEN}Report generated: {report_path}{COLOR_RESET}")


def main() -> int:
    """
    Main function for the TDD validator tool.
    
    Returns:
        int: Exit code (0 for success, non-zero for failure).
    """
    parser = argparse.ArgumentParser(description="TDD Validator Tool")
    parser.add_argument("--validate-metadata", action="store_true", 
                        help="Validate metadata in test files")
    parser.add_argument("--validate-status", action="store_true",
                        help="Validate test status (passing/failing)")
    parser.add_argument("--generate-lifecycle-report", action="store_true",
                        help="Generate lifecycle status report")
    
    args = parser.parse_args()
    
    if args.validate_metadata:
        if not validate_all_metadata():
            return 1
            
    if args.validate_status:
        if not validate_test_status():
            return 1
            
    if args.generate_lifecycle_report:
        generate_lifecycle_report()
        
    if not any([args.validate_metadata, args.validate_status, args.generate_lifecycle_report]):
        parser.print_help()
        return 1
        
    return 0


if __name__ == "__main__":
    sys.exit(main()) 