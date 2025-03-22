#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 2: Feature File Consolidation

This script implements Phase 2 of the BDD Test Structure Consolidation project:
1. Compare feature files across different directories
2. Migrate unique feature files to the consolidated structure
3. Clean up obsolete feature files

Usage:
    python feature_file_consolidation.py
    python feature_file_consolidation.py --cleanup  # To remove obsolete files
"""

import os
import shutil
import logging
import filecmp
import difflib
from pathlib import Path
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("feature_file_consolidation.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define feature file directories
FEATURE_DIRECTORIES = [
    PROJECT_ROOT / "features" / "generated",
    PROJECT_ROOT / "tests" / "features",
    PROJECT_ROOT / "tests" / "bdd" / "features"
]

# Target directory for consolidated feature files
TARGET_DIRECTORY = PROJECT_ROOT / "tests" / "bdd" / "features"

class FeatureFile:
    """Class to represent a feature file with its metadata"""
    def __init__(self, path):
        self.path = path
        self.name = path.name
        self.content = self._read_content()
        self.stem = path.stem
        self.relative_path = path.relative_to(path.parent.parent.parent)
    
    def _read_content(self):
        """Read the content of the feature file"""
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading {self.path}: {e}")
            return ""
    
    def __eq__(self, other):
        """Check if two feature files are identical based on content"""
        return self.content == other.content
    
    def similarity(self, other):
        """Calculate similarity between two feature files"""
        if not self.content or not other.content:
            return 0
        
        s = difflib.SequenceMatcher(None, self.content, other.content)
        return s.ratio()

def collect_feature_files():
    """Collect all feature files from different directories"""
    feature_files = []
    
    for directory in FEATURE_DIRECTORIES:
        if not directory.exists():
            logger.warning(f"Directory not found: {directory}")
            continue
        
        logger.info(f"Collecting feature files from: {directory}")
        for file_path in directory.glob("**/*.feature"):
            feature_files.append(FeatureFile(file_path))
            logger.info(f"Found feature file: {file_path}")
    
    logger.info(f"Collected {len(feature_files)} feature files in total")
    return feature_files

def group_similar_features(feature_files):
    """Group similar feature files together"""
    groups = defaultdict(list)
    
    # First group by name
    for feature in feature_files:
        groups[feature.stem].append(feature)
    
    # Then check for similar content within groups
    final_groups = []
    for name, files in groups.items():
        if len(files) == 1:
            final_groups.append(files)
            continue
        
        # Group files with similar content
        content_groups = []
        for file in files:
            found_group = False
            for group in content_groups:
                if file.similarity(group[0]) > 0.8:  # 80% similarity threshold
                    group.append(file)
                    found_group = True
                    break
            
            if not found_group:
                content_groups.append([file])
        
        final_groups.extend(content_groups)
    
    return final_groups

def select_best_feature(feature_group):
    """Select the best feature file from a group of similar files"""
    # Prefer files from tests/bdd/features
    for feature in feature_group:
        if "tests/bdd/features" in str(feature.path):
            return feature
    
    # Next, prefer files from tests/features
    for feature in feature_group:
        if "tests/features" in str(feature.path):
            return feature
    
    # Default to the first file
    return feature_group[0]

def migrate_feature_files(feature_groups):
    """Migrate selected feature files to the target directory"""
    # Create target directory if it doesn't exist
    TARGET_DIRECTORY.mkdir(parents=True, exist_ok=True)
    
    migrated_files = []
    
    for group in feature_groups:
        # Select the best feature file from the group
        selected_feature = select_best_feature(group)
        
        # Define target path
        target_path = TARGET_DIRECTORY / selected_feature.name
        
        # Skip if the file is already in the target directory
        if "tests/bdd/features" in str(selected_feature.path):
            logger.info(f"File already in target directory: {selected_feature.path}")
            migrated_files.append(selected_feature)
            continue
        
        # Copy the file to the target directory
        try:
            shutil.copy2(selected_feature.path, target_path)
            logger.info(f"Migrated feature file: {selected_feature.path} -> {target_path}")
            
            # Update the path of the migrated feature
            selected_feature.path = target_path
            migrated_files.append(selected_feature)
        except Exception as e:
            logger.error(f"Error migrating feature file {selected_feature.path}: {e}")
    
    logger.info(f"Migrated {len(migrated_files)} feature files to {TARGET_DIRECTORY}")
    return migrated_files

def clean_up_obsolete_files(migrated_files, perform_cleanup=False):
    """Clean up obsolete feature files"""
    # First, identify all feature files
    all_feature_paths = []
    for directory in FEATURE_DIRECTORIES:
        if not directory.exists():
            continue
        for file_path in directory.glob("**/*.feature"):
            all_feature_paths.append(file_path)
    
    # Identify files to keep (those in the target directory)
    files_to_keep = [f.path for f in migrated_files]
    
    # Identify files to remove (those not in the target directory)
    files_to_remove = [
        path for path in all_feature_paths 
        if path not in files_to_keep and "tests/bdd/features" not in str(path)
    ]
    
    if not files_to_remove:
        logger.info("No obsolete feature files found")
        print("\nNo obsolete feature files found")
        return
    
    logger.info(f"Found {len(files_to_remove)} obsolete feature files")
    
    if perform_cleanup:
        # Actually remove the files
        removed_count = 0
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                logger.info(f"Removed obsolete feature file: {file_path}")
                removed_count += 1
            except Exception as e:
                logger.error(f"Error removing file {file_path}: {e}")
        
        logger.info(f"Removed {removed_count} obsolete feature files")
        print(f"\nRemoved {removed_count} obsolete feature files")
        
        # Check if any directories are now empty and can be removed
        check_empty_directories()
    else:
        # Just report the files to be removed
        print("\nThe following feature files are now obsolete and can be removed:")
        for file_path in files_to_remove:
            print(f"  - {file_path}")
        
        print("\nTo complete cleanup, run this script with the --cleanup flag")

def check_empty_directories():
    """Check for empty directories that can be removed"""
    empty_dirs = []
    
    # Check if the source directories are now empty
    for directory in [
        PROJECT_ROOT / "features" / "generated",
        PROJECT_ROOT / "tests" / "features"
    ]:
        if not directory.exists():
            continue
            
        # Check if the directory has any feature files
        has_features = False
        for _ in directory.glob("**/*.feature"):
            has_features = True
            break
            
        if not has_features:
            empty_dirs.append(directory)
    
    if empty_dirs:
        print("\nThe following directories no longer contain feature files and can be removed:")
        for directory in empty_dirs:
            print(f"  - {directory}")

def report_migration_results(feature_groups, migrated_files):
    """Report the results of the migration"""
    print("\n=== Feature File Consolidation Summary ===")
    print(f"Total feature files found: {sum(len(group) for group in feature_groups)}")
    print(f"Feature file groups: {len(feature_groups)}")
    print(f"Feature files migrated to {TARGET_DIRECTORY}: {len(migrated_files)}")
    
    # Print details of each group
    print("\nFeature File Groups:")
    for i, group in enumerate(feature_groups, 1):
        print(f"\nGroup {i}:")
        
        # Identify which file was selected
        selected = [f for f in migrated_files if f.stem == group[0].stem]
        selected_path = selected[0].path if selected else None
        
        for feature in group:
            status = "SELECTED" if feature.path == selected_path else ""
            print(f"  - {feature.path} {status}")

def main(perform_cleanup=False):
    """Main function to execute the feature file consolidation process"""
    logger.info(f"Starting Phase 2: Feature File Consolidation (cleanup={perform_cleanup})")
    
    # Step 1: Collect all feature files
    feature_files = collect_feature_files()
    
    # Step 2: Group similar feature files
    feature_groups = group_similar_features(feature_files)
    logger.info(f"Grouped feature files into {len(feature_groups)} groups")
    
    # Step 3: Migrate selected feature files to the target directory
    migrated_files = migrate_feature_files(feature_groups)
    
    # Step 4: Clean up obsolete feature files
    clean_up_obsolete_files(migrated_files, perform_cleanup)
    
    # Step 5: Report the results
    report_migration_results(feature_groups, migrated_files)
    
    logger.info("Phase 2: Feature File Consolidation completed")
    print("\nPhase 2: Feature File Consolidation completed")
    print("\nNext steps:")
    if not perform_cleanup:
        print("1. Review the consolidated feature files in tests/bdd/features")
        print("2. Run this script with the --cleanup flag to remove obsolete files")
    print(f"{'3' if not perform_cleanup else '1'}. Proceed to Phase 3: Step Definition Consolidation")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="BDD Feature File Consolidation")
    parser.add_argument("--cleanup", action="store_true", help="Clean up obsolete feature files")
    args = parser.parse_args()
    
    main(perform_cleanup=args.cleanup) 