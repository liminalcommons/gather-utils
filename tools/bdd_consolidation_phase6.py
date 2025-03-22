#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 6

This script orchestrates Phase 6 of the BDD Test Structure Consolidation project:
1. Remove obsolete directories
2. Update any remaining documentation

Usage:
    python bdd_consolidation_phase6.py
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
        logging.FileHandler("bdd_consolidation_phase6.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

def run_final_cleanup():
    """Run the final cleanup script."""
    script_path = TOOLS_DIR / "final_cleanup.py"
    
    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False
    
    try:
        command = [sys.executable, str(script_path)]
            
        logger.info(f"Running script: {' '.join(command)}")
        result = subprocess.run(
            command,
            check=True,
            capture_output=False,  # Direct user interaction is needed
            text=True
        )
        
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        logger.error(f"Script failed with exit code {e.returncode}")
        return False
    except Exception as e:
        logger.error(f"Script failed with exception: {e}")
        return False

def main():
    """Main function to execute Phase 6 of the BDD consolidation project."""
    logger.info("Starting Phase 6 of BDD Test Structure Consolidation")
    
    print("\n=== Phase 6: Final Cleanup ===")
    if run_final_cleanup():
        logger.info("Phase 6 of BDD Test Structure Consolidation completed successfully")
        print("\nBDD Test Structure Consolidation project is now complete!")
        return 0
    else:
        logger.error("Phase 6 of BDD Test Structure Consolidation failed")
        print("\nPhase 6 failed. Please check the logs and try again.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 