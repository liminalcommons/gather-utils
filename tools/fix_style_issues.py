#!/usr/bin/env python
"""
Style issues fixer script.

This script automatically fixes common style issues across the codebase:
1. Removes trailing whitespace
2. Ensures files end with a newline
3. Sorts imports using isort
4. Formats code using black
"""
import os
import subprocess
import sys
from pathlib import Path

# Directories to process
DIRECTORIES = [
    "src",
    "tests",
    "tools",
]

# File extensions to process
EXTENSIONS = [".py"]

def print_header(title):
    """Print a section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}")

def run_command(command, description):
    """Run a command and print its output."""
    print(f"\n> {description}...")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"Command: {' '.join(command)}")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def fix_trailing_whitespace_and_newlines():
    """Fix trailing whitespace and ensure files end with a newline."""
    print_header("Fixing Trailing Whitespace and Newlines")
    
    for directory in DIRECTORIES:
        for ext in EXTENSIONS:
            run_command(
                ["find", directory, "-name", f"*{ext}", "-exec", "sed", "-i", "", "-e", "s/[[:space:]]*$//", "{}", ";"],
                f"Removing trailing whitespace in {directory}/*{ext}"
            )
            run_command(
                ["find", directory, "-name", f"*{ext}", "-exec", "sed", "-i", "", "-e", "$a\\", "{}", ";"],
                f"Ensuring files end with newline in {directory}/*{ext}"
            )

def run_isort():
    """Sort imports using isort."""
    print_header("Sorting Imports with isort")
    
    for directory in DIRECTORIES:
        run_command(
            ["isort", "--profile", "black", "--line-length", "79", directory],
            f"Sorting imports in {directory}"
        )

def run_black():
    """Format code using black."""
    print_header("Formatting Code with Black")
    
    for directory in DIRECTORIES:
        run_command(
            ["black", "--line-length", "79", directory],
            f"Formatting code in {directory}"
        )

def run_flake8():
    """Run flake8 to check for remaining issues."""
    print_header("Checking for Remaining Issues with Flake8")
    
    for directory in DIRECTORIES:
        run_command(
            ["flake8", "--max-line-length=79", "--extend-ignore=E203", directory],
            f"Checking for issues in {directory}"
        )

def main():
    """Run all style fixers."""
    print_header("Starting Style Issues Fixer")
    
    # Check if required tools are installed
    for tool in ["isort", "black", "flake8"]:
        try:
            subprocess.run(["which", tool], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print(f"Error: {tool} is not installed. Please install it with 'pip install {tool}'.")
            sys.exit(1)
    
    # Fix style issues
    fix_trailing_whitespace_and_newlines()
    run_isort()
    run_black()
    run_flake8()
    
    print_header("Style Issues Fixer Complete")
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Run tests to ensure everything still works")
    print("3. Commit the changes")

if __name__ == "__main__":
    main() 