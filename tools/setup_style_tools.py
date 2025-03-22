#!/usr/bin/env python
"""
Setup script for style checking tools.

This script installs all the required tools for style checking:
1. pre-commit
2. black
3. flake8
4. isort
"""
import subprocess
import sys

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

def install_tools():
    """Install all required tools."""
    print_header("Installing Style Checking Tools")
    
    tools = [
        "pre-commit",
        "black",
        "flake8",
        "flake8-docstrings",
        "isort",
    ]
    
    for tool in tools:
        run_command(
            ["pip", "install", tool],
            f"Installing {tool}"
        )

def setup_pre_commit():
    """Set up pre-commit hooks."""
    print_header("Setting Up Pre-commit Hooks")
    
    run_command(
        ["pre-commit", "install"],
        "Installing pre-commit hooks"
    )
    
    run_command(
        ["pre-commit", "install", "--hook-type", "pre-push"],
        "Installing pre-push hooks"
    )

def main():
    """Run the setup script."""
    print_header("Starting Style Tools Setup")
    
    install_tools()
    setup_pre_commit()
    
    print_header("Style Tools Setup Complete")
    print("\nNext steps:")
    print("1. Run the style fixer script to fix existing issues:")
    print("   python tools/fix_style_issues.py")
    print("2. Commit the changes")
    print("3. Future commits will automatically be checked for style issues")

if __name__ == "__main__":
    main() 