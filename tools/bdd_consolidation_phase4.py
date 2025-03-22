#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 4

This script orchestrates Phase 4 of the BDD Test Structure Consolidation project:
1. Clean up duplicate entries in pytest.ini
2. Ensure behave.ini is correctly configured
3. Update environment setup in tests/bdd/environment.py

Usage:
    python bdd_consolidation_phase4.py
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
        logging.FileHandler("bdd_consolidation_phase4.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

def run_config_cleanup():
    """Run the configuration cleanup script."""
    script_path = TOOLS_DIR / "config_cleanup.py"
    
    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False
    
    try:
        command = [sys.executable, str(script_path)]
            
        logger.info(f"Running script: {' '.join(command)}")
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            logger.warning(f"Script stderr: {result.stderr}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Script failed with exit code {e.returncode}: {e.stderr}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main function to execute Phase 4 of the BDD consolidation project."""
    logger.info("Starting Phase 4 of BDD Test Structure Consolidation")
    
    print("\n=== Phase 4: Configuration Cleanup ===")
    if not run_config_cleanup():
        logger.error("Configuration cleanup failed. Aborting Phase 4.")
        print("\nConfiguration cleanup failed. Please check the logs.")
        return 1
    
    logger.info("Phase 4 of BDD Test Structure Consolidation completed successfully")
    
    print("\nPhase 4 completed successfully.")
    print("Next steps:")
    print("1. Proceed to Phase 5: Verification")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 