#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 1

This script orchestrates Phase 1 of the BDD Test Structure Consolidation project:
1. Create a backup of all BDD-related files
2. Update the BDD testing documentation

Usage:
    python bdd_consolidation_phase1.py
"""

import os
import sys
import logging
import subprocess
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bdd_consolidation_phase1.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

def run_script(script_name):
    """Run a Python script and return its success status."""
    script_path = TOOLS_DIR / script_name
    
    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False
    
    try:
        logger.info(f"Running script: {script_path}")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True,
            capture_output=True,
            text=True
        )
        logger.info(f"Script output: {result.stdout}")
        if result.stderr:
            logger.warning(f"Script stderr: {result.stderr}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Script failed with exit code {e.returncode}: {e.stderr}")
        return False

def main():
    """Main function to execute Phase 1 of the BDD consolidation project."""
    logger.info("Starting Phase 1 of BDD Test Structure Consolidation")
    
    # Step 1: Create backup of all BDD-related files
    print("\n=== Step 1: Creating backup of all BDD-related files ===")
    if not run_script("bdd_backup.py"):
        logger.error("Backup creation failed. Aborting Phase 1.")
        print("\nBackup creation failed. Aborting Phase 1.")
        return
    
    # Step 2: Update documentation
    print("\n=== Step 2: Updating BDD documentation ===")
    if not run_script("update_bdd_docs.py"):
        logger.error("Documentation update failed. Phase 1 partially completed.")
        print("\nDocumentation update failed. Phase 1 partially completed.")
        return
    
    # Phase 1 completed successfully
    logger.info("Phase 1 of BDD Test Structure Consolidation completed successfully")
    print("\n=== Phase 1 of BDD Test Structure Consolidation completed successfully ===")
    print("\nNext steps:")
    print("1. Review the updated documentation in tests/bdd/README.md")
    print("2. Proceed to Phase 2: Feature File Consolidation")

if __name__ == "__main__":
    main() 