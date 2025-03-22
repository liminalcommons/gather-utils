#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 5

This script orchestrates Phase 5 of the BDD Test Structure Consolidation project:
1. Run the BDD tests to verify that the consolidation has not broken anything

Usage:
    python bdd_consolidation_phase5.py
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
        logging.FileHandler("bdd_consolidation_phase5.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

def run_bdd_verification():
    """Run the BDD verification script."""
    script_path = TOOLS_DIR / "bdd_verification.py"
    
    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False
    
    try:
        command = [sys.executable, str(script_path)]
            
        logger.info(f"Running script: {' '.join(command)}")
        result = subprocess.run(
            command,
            check=False,  # Don't raise exception on test failures
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            logger.warning(f"Script stderr: {result.stderr}")
        
        # Return success status based on verification script return code
        return result.returncode == 0
    except Exception as e:
        logger.error(f"Script failed with exception: {e}")
        print(f"Error: {e}")
        return False

def main():
    """Main function to execute Phase 5 of the BDD consolidation project."""
    logger.info("Starting Phase 5 of BDD Test Structure Consolidation")
    
    print("\n=== Phase 5: Verification ===")
    success = run_bdd_verification()
    
    if success:
        logger.info("Phase 5 of BDD Test Structure Consolidation completed successfully")
        print("\nPhase 5 completed successfully.")
        print("Next steps:")
        print("1. Proceed to Phase 6: Final Cleanup")
        return 0
    else:
        logger.warning("Phase 5 of BDD Test Structure Consolidation completed with test failures")
        print("\nPhase 5 completed with test failures.")
        print("Next steps:")
        print("1. Fix any issues that arose during testing")
        print("2. Re-run Phase 5 to verify the fixes")
        print("3. Proceed to Phase 6: Final Cleanup")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 