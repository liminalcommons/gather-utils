#!/usr/bin/env python3
"""
BDD Test Runner

This script runs BDD tests using behave and generates a coverage report.

Usage:
    python tools/run_bdd_tests.py [--tags TAG]

Options:
    --tags TAG    Run only scenarios with the given tag (e.g., --tags=REQ-1.1)
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_behave(tags=None):
    """Run behave tests with optional tags filter."""
    # Use the behave.ini configuration file (Behave automatically looks for this file)
    cmd = ['behave']
    
    if tags:
        cmd.extend(['--tags', tags])
    
    # Run the tests
    print(f"Running BDD tests: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}", file=sys.stderr)
    
    return result.returncode == 0


def generate_coverage_report():
    """Generate the BDD coverage report."""
    cmd = ['python', 'tools/bdd_coverage_report.py']
    
    print(f"Generating BDD coverage report: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Print the output
    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}", file=sys.stderr)
    
    return result.returncode == 0


def main():
    """Main function to run BDD tests and generate the coverage report."""
    parser = argparse.ArgumentParser(description='Run BDD tests and generate coverage report')
    parser.add_argument('--tags', help='Run only scenarios with the given tag (e.g., --tags=REQ-1.1)')
    args = parser.parse_args()
    
    # Create reports directory
    os.makedirs('reports', exist_ok=True)
    os.makedirs('reports/junit', exist_ok=True)
    
    # Run the tests
    tests_passed = run_behave(args.tags)
    
    # Generate the coverage report
    report_generated = generate_coverage_report()
    
    # Print summary
    print("\nSummary:")
    print(f"BDD Tests: {'PASSED' if tests_passed else 'FAILED'}")
    print(f"Coverage Report: {'GENERATED' if report_generated else 'FAILED'}")
    
    # Return appropriate exit code
    return 0 if tests_passed and report_generated else 1


if __name__ == '__main__':
    sys.exit(main()) 