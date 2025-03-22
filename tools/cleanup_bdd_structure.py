#!/usr/bin/env python3
"""
BDD Structure Cleanup Script

This script cleans up the obsolete BDD test structure after migration.
It creates backups of the old structure before removing it.

Usage:
    python tools/cleanup_bdd_structure.py [--force]

Options:
    --force    Skip confirmation and proceed with cleanup
"""
import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


def backup_directory(directory):
    """Create a backup of a directory."""
    if not directory.exists():
        return None
        
    # Create a backup directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = directory.parent / f"{directory.name}_backup_{timestamp}"
    
    # Copy the directory to the backup location
    shutil.copytree(directory, backup_dir)
    print(f"Created backup of {directory} at {backup_dir}")
    
    return backup_dir


def cleanup_features_directory():
    """Clean up the features directory."""
    project_root = Path(__file__).parent.parent
    features_dir = project_root / 'features'
    
    if not features_dir.exists():
        print("Features directory not found, nothing to clean up")
        return False
    
    # Create a backup of the features directory
    backup_dir = backup_directory(features_dir)
    if not backup_dir:
        return False
    
    # Remove the features directory
    shutil.rmtree(features_dir)
    print(f"Removed {features_dir}")
    
    return True


def cleanup_pytest_bdd_config():
    """Clean up pytest-bdd configuration from pytest.ini."""
    project_root = Path(__file__).parent.parent
    pytest_ini = project_root / 'pytest.ini'
    
    if not pytest_ini.exists():
        print("pytest.ini not found, nothing to clean up")
        return False
    
    # Create a backup of pytest.ini
    backup_file = pytest_ini.parent / f"pytest.ini.bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    shutil.copy2(pytest_ini, backup_file)
    print(f"Created backup of pytest.ini at {backup_file}")
    
    # Read the content of pytest.ini
    with open(pytest_ini, 'r') as f:
        content = f.readlines()
    
    # Filter out pytest-bdd configuration lines
    new_content = []
    for line in content:
        if not line.strip().startswith('bdd_features_dir') and not line.strip().startswith('bdd_steps_dir'):
            new_content.append(line)
    
    # Write the filtered content back to pytest.ini
    with open(pytest_ini, 'w') as f:
        f.writelines(new_content)
    
    print(f"Removed pytest-bdd configuration from {pytest_ini}")
    
    return True


def main():
    """Main function to clean up the BDD test structure."""
    parser = argparse.ArgumentParser(description='Clean up obsolete BDD test structure')
    parser.add_argument('--force', action='store_true', help='Skip confirmation and proceed with cleanup')
    args = parser.parse_args()
    
    print("This script will clean up the obsolete BDD test structure after migration.")
    print("It will create backups before removing any files.")
    
    if not args.force:
        confirmation = input("Are you sure you want to proceed? (y/n): ")
        if confirmation.lower() != 'y':
            print("Cleanup aborted")
            return 1
    
    # Clean up the features directory
    features_cleaned = cleanup_features_directory()
    
    # Clean up pytest-bdd configuration
    pytest_cleaned = cleanup_pytest_bdd_config()
    
    # Print summary
    print("\nCleanup Summary:")
    print(f"Features Directory: {'CLEANED' if features_cleaned else 'NO CHANGES'}")
    print(f"pytest-bdd Configuration: {'CLEANED' if pytest_cleaned else 'NO CHANGES'}")
    
    print("\nCleanup complete. The obsolete BDD test structure has been removed.")
    print("Backups have been created in case you need to restore anything.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main()) 