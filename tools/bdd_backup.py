#!/usr/bin/env python3
"""
BDD Test Backup Script

This script creates a backup of all BDD-related files before making any changes
as part of the BDD Test Structure Consolidation project (Phase 1).
"""

import os
import shutil
import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bdd_backup.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Define directories to backup
BDD_DIRECTORIES = [
    "features",
    "features/steps",
    "features/generated",
    "tests/features",
    "tests/step_defs",
    "tests/bdd",
    "tests/bdd/features",
    "tests/bdd/steps",
]

# Define configuration files to backup
CONFIG_FILES = [
    "pytest.ini",
    "behave.ini",
]

def create_backup_directory():
    """Create a timestamped backup directory."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = PROJECT_ROOT / f"backup_bdd_{timestamp}"
    backup_dir.mkdir(exist_ok=True)
    logger.info(f"Created backup directory: {backup_dir}")
    return backup_dir

def backup_directories(backup_dir):
    """Backup all BDD-related directories."""
    for dir_path in BDD_DIRECTORIES:
        source_path = PROJECT_ROOT / dir_path
        if not source_path.exists():
            logger.warning(f"Directory not found, skipping: {source_path}")
            continue
            
        # Create the destination directory structure
        dest_path = backup_dir / dir_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy the directory
        try:
            shutil.copytree(source_path, dest_path)
            logger.info(f"Backed up directory: {source_path} -> {dest_path}")
        except Exception as e:
            logger.error(f"Failed to backup directory {source_path}: {e}")

def backup_config_files(backup_dir):
    """Backup configuration files related to BDD testing."""
    config_backup_dir = backup_dir / "config"
    config_backup_dir.mkdir(exist_ok=True)
    
    for file_name in CONFIG_FILES:
        source_path = PROJECT_ROOT / file_name
        if not source_path.exists():
            logger.warning(f"Config file not found, skipping: {source_path}")
            continue
            
        # Copy the file
        try:
            shutil.copy2(source_path, config_backup_dir / file_name)
            logger.info(f"Backed up config file: {source_path} -> {config_backup_dir / file_name}")
        except Exception as e:
            logger.error(f"Failed to backup config file {source_path}: {e}")

def main():
    """Main function to execute the backup process."""
    logger.info("Starting BDD test files backup process")
    
    try:
        # Create backup directory
        backup_dir = create_backup_directory()
        
        # Backup directories
        backup_directories(backup_dir)
        
        # Backup configuration files
        backup_config_files(backup_dir)
        
        logger.info(f"Backup completed successfully. Files stored in: {backup_dir}")
        print(f"\nBackup completed successfully!\nFiles stored in: {backup_dir}")
        
    except Exception as e:
        logger.error(f"Backup process failed: {e}")
        print(f"Backup process failed. See log for details.")

if __name__ == "__main__":
    main() 