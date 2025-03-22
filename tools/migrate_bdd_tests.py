#!/usr/bin/env python3
"""
BDD Test Migration Script

This script migrates BDD tests from the old structure to the new consolidated structure.
It copies feature files from features/generated to tests/bdd/features/generated,
ensuring no duplicates are created.

Usage:
    python tools/migrate_bdd_tests.py
"""
import os
import shutil
import sys
from pathlib import Path


def migrate_feature_files():
    """Migrate feature files from features/generated to tests/bdd/features/generated."""
    project_root = Path(__file__).parent.parent
    source_dir = project_root / 'features' / 'generated'
    target_dir = project_root / 'tests' / 'bdd' / 'features' / 'generated'
    
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Get a list of all feature files in the source directory
    feature_files = list(source_dir.glob('*.feature'))
    
    if not feature_files:
        print("No feature files found in features/generated")
        return False
    
    print(f"Found {len(feature_files)} feature files to migrate")
    
    # Copy each feature file to the target directory
    for feature_file in feature_files:
        target_file = target_dir / feature_file.name
        
        # Check if the file already exists in the target directory
        if target_file.exists():
            print(f"Skipping {feature_file.name} - already exists in target directory")
            continue
        
        # Copy the file
        shutil.copy2(feature_file, target_file)
        print(f"Migrated {feature_file.name} to {target_file}")
    
    return True


def migrate_environment_files():
    """Migrate environment files from features/environment to tests/bdd."""
    project_root = Path(__file__).parent.parent
    source_dir = project_root / 'features' / 'environment'
    target_file = project_root / 'tests' / 'bdd' / 'environment.py'
    
    # Check if the source directory exists
    if not source_dir.exists() or not any(source_dir.iterdir()):
        print("No environment files found in features/environment")
        return False
    
    # If there's an environment.py file in the source directory, copy it
    source_file = source_dir / 'environment.py'
    if source_file.exists():
        # Check if the target file already exists
        if target_file.exists():
            print(f"Skipping environment.py - already exists in target directory")
            return False
        
        # Copy the file
        shutil.copy2(source_file, target_file)
        print(f"Migrated environment.py to {target_file}")
        return True
    
    return False


def migrate_step_definitions():
    """Migrate step definitions from features/steps to tests/bdd/steps."""
    project_root = Path(__file__).parent.parent
    source_dir = project_root / 'features' / 'steps'
    target_dir = project_root / 'tests' / 'bdd' / 'steps'
    
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Get a list of all step definition files in the source directory
    step_files = list(source_dir.glob('*.py'))
    
    if not step_files:
        print("No step definition files found in features/steps")
        return False
    
    print(f"Found {len(step_files)} step definition files to migrate")
    
    # Copy each step definition file to the target directory
    for step_file in step_files:
        # Skip backup files
        if step_file.name.endswith('.bak'):
            continue
            
        target_file = target_dir / step_file.name
        
        # Check if the file already exists in the target directory
        if target_file.exists():
            print(f"Skipping {step_file.name} - already exists in target directory")
            continue
        
        # Copy the file
        shutil.copy2(step_file, target_file)
        print(f"Migrated {step_file.name} to {target_file}")
    
    return True


def main():
    """Main function to migrate BDD tests."""
    print("Starting BDD test migration...")
    
    # Migrate feature files
    feature_migrated = migrate_feature_files()
    
    # Migrate environment files
    environment_migrated = migrate_environment_files()
    
    # Migrate step definitions
    steps_migrated = migrate_step_definitions()
    
    # Print summary
    print("\nMigration Summary:")
    print(f"Feature Files: {'MIGRATED' if feature_migrated else 'NO CHANGES'}")
    print(f"Environment Files: {'MIGRATED' if environment_migrated else 'NO CHANGES'}")
    print(f"Step Definitions: {'MIGRATED' if steps_migrated else 'NO CHANGES'}")
    
    print("\nMigration complete. Please review the migrated files and update your tests as needed.")
    print("You can now run your BDD tests using: python tools/run_bdd_tests.py")
    
    return 0


if __name__ == '__main__':
    sys.exit(main()) 