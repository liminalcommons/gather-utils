#!/usr/bin/env python3
"""
BDD Step Verification Tool

This script verifies that all steps from legacy step definition files
have been properly migrated to the consolidated step repository.

Usage:
    python step_verification.py [legacy_step_file] [consolidated_steps_dir]
"""

import os
import sys
import re
import glob
from pathlib import Path

def extract_steps_from_file(file_path):
    """Extract step patterns from a step definition file."""
    steps = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all step decorators (given, when, then)
        step_pattern = re.compile(r'@(given|when|then)\s*\(\s*[\'"](.+?)[\'"]\s*\)')
        matches = step_pattern.finditer(content)
        
        for match in matches:
            step_type = match.group(1)  # given, when, or then
            step_pattern = match.group(2)  # The actual pattern
            steps.append((step_type, step_pattern))
    
    except Exception as e:
        print(f"Error extracting steps from {file_path}: {e}")
    
    return steps

def find_all_step_files(directory):
    """Find all step definition files in a directory."""
    return glob.glob(os.path.join(directory, "**/*.py"), recursive=True)

def compare_steps(legacy_steps, consolidated_dirs):
    """Compare steps from legacy file with consolidated step files."""
    # Extract all steps from consolidated files
    consolidated_steps = []
    for directory in consolidated_dirs:
        step_files = find_all_step_files(directory)
        for file_path in step_files:
            file_steps = extract_steps_from_file(file_path)
            for step in file_steps:
                consolidated_steps.append((step[0], step[1], os.path.basename(file_path)))
    
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
    
    # Find where each legacy step is implemented
    step_locations = {}
    for legacy_step in legacy_steps:
        step_type, step_pattern = legacy_step
        locations = []
        
        for cons_step in consolidated_steps:
            cons_type, cons_pattern, cons_file = cons_step
            if step_type == cons_type and step_pattern == cons_pattern:
                locations.append(cons_file)
        
        step_locations[(step_type, step_pattern)] = locations
    
    return missing_steps, step_locations

def main():
    """Main function to run the verification."""
    # Define default paths
    project_root = Path(__file__).parent.parent.absolute()
    default_legacy_file = project_root / "features" / "steps" / "command_line_interface_steps.py.bak"
    default_consolidated_dir = project_root / "tests" / "bdd" / "steps"
    
    # Parse command line arguments
    legacy_file = default_legacy_file
    consolidated_dirs = [default_consolidated_dir]
    
    if len(sys.argv) > 1:
        legacy_file = Path(sys.argv[1])
    
    if len(sys.argv) > 2:
        consolidated_dirs = [Path(sys.argv[2])]
    
    # Extract steps
    print(f"Analyzing legacy step file: {legacy_file}")
    legacy_steps = extract_steps_from_file(legacy_file)
    print(f"Found {len(legacy_steps)} steps in legacy file")
    
    # Compare steps
    print(f"Comparing with consolidated steps in: {consolidated_dirs}")
    missing_steps, step_locations = compare_steps(legacy_steps, consolidated_dirs)
    
    # Report results
    print("\n=== Step Verification Results ===")
    print(f"Total steps in legacy file: {len(legacy_steps)}")
    print(f"Steps missing from consolidated repository: {len(missing_steps)}")
    
    if missing_steps:
        print("\n=== Missing Steps ===")
        for step_type, step_pattern in missing_steps:
            print(f"@{step_type}('{step_pattern}')")
    
    print("\n=== Step Implementation Locations ===")
    for (step_type, step_pattern), locations in step_locations.items():
        if locations:
            print(f"@{step_type}('{step_pattern}'): {', '.join(locations)}")
        else:
            print(f"@{step_type}('{step_pattern}'): NOT FOUND")
    
    # Summary
    if missing_steps:
        print("\n⚠️ Some steps are missing from the consolidated repository.")
        print("Consider migrating these steps to maintain full test coverage.")
    else:
        print("\n✅ All steps have been successfully migrated to the consolidated repository.")

if __name__ == "__main__":
    main() 