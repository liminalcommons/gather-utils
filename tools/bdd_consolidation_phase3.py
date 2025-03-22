#!/usr/bin/env python3
"""
BDD Test Structure Consolidation - Phase 3

This script orchestrates Phase 3 of the BDD Test Structure Consolidation project:
1. Compare step definitions in different directories
2. Migrate and merge step definitions to the consolidated structure
3. Clean up obsolete step definition files

Usage:
    python bdd_consolidation_phase3.py
    python bdd_consolidation_phase3.py --cleanup  # To remove obsolete files
"""

import os
import sys
import logging
import subprocess
import argparse
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bdd_consolidation_phase3.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

def run_step_definition_consolidation(cleanup=False):
    """Run the step definition consolidation script."""
    script_path = TOOLS_DIR / "step_definition_consolidation.py"
    
    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False
    
    try:
        command = [sys.executable, str(script_path)]
        if cleanup:
            command.append("--cleanup")
            
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
    """Main function to execute Phase 3 of the BDD consolidation project."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="BDD Test Structure Consolidation - Phase 3")
    parser.add_argument("--cleanup", action="store_true", help="Clean up obsolete step definition files")
    args = parser.parse_args()
    
    logger.info(f"Starting Phase 3 of BDD Test Structure Consolidation (cleanup={args.cleanup})")
    
    print("\n=== Phase 3: Step Definition Consolidation ===")
    if not run_step_definition_consolidation(cleanup=args.cleanup):
        logger.error("Step definition consolidation failed. Aborting Phase 3.")
        print("\nStep definition consolidation failed. Please check the logs.")
        return 1
    
    logger.info("Phase 3 of BDD Test Structure Consolidation completed successfully")
    
    if not args.cleanup:
        print("\nPhase 3 initial run completed successfully.")
        print("Next steps:")
        print("1. Review the consolidated step definition files in tests/bdd/steps")
        print("2. Run this script with the --cleanup flag to remove obsolete files")
        print("3. Proceed to Phase 4: Configuration Cleanup")
    else:
        print("\nPhase 3 cleanup completed successfully.")
        print("Next steps:")
        print("1. Proceed to Phase 4: Configuration Cleanup")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 