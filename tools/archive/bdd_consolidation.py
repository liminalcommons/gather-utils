"""
Tool: Bdd Consolidation
Created: 2025-03-21
Author: Development Team
Status: Archived
Purpose: Supports BDD testing and development workflows
Dependencies: logging, subprocess
Lifecycle:
    - Created: To support BDD testing and development workflows
    - Active: Archived for reference but no longer actively used
    - Obsolescence Conditions:
        1. When BDD testing approach changes significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""
#!/usr/bin/env python3
"""
BDD Test Structure Consolidation

This script orchestrates the entire BDD Test Structure Consolidation project:
1. Phase 1: Preparation (backup and documentation)
2. Phase 2: Feature File Consolidation
3. Phase 3: Step Definition Consolidation
4. Phase 4: Configuration Cleanup
5. Phase 5: Verification
6. Phase 6: Final Cleanup

Usage:
    python bdd_consolidation.py [--start-phase PHASE] [--end-phase PHASE]

Options:
    --start-phase PHASE  Start execution from this phase (1-6, default: 1)
    --end-phase PHASE    End execution at this phase (1-6, default: 6)
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bdd_consolidation.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

# Define the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
TOOLS_DIR = PROJECT_ROOT / "tools"

# Define phase scripts
PHASE_SCRIPTS = {
    1: "bdd_consolidation_phase1.py",
    2: "bdd_consolidation_phase2.py",
    3: "bdd_consolidation_phase3.py",
    4: "bdd_consolidation_phase4.py",
    5: "bdd_consolidation_phase5.py",
    6: "bdd_consolidation_phase6.py",
}

# Define phase descriptions
PHASE_DESCRIPTIONS = {
    1: "Preparation (backup and documentation)",
    2: "Feature File Consolidation",
    3: "Step Definition Consolidation",
    4: "Configuration Cleanup",
    5: "Verification",
    6: "Final Cleanup",
}


def run_phase(phase, args=None):
    """Run a specific phase of the consolidation process."""
    if phase not in PHASE_SCRIPTS:
        logger.error(f"Invalid phase: {phase}")
        return False

    script_path = TOOLS_DIR / PHASE_SCRIPTS[phase]

    if not script_path.exists():
        logger.error(f"Script not found: {script_path}")
        return False

    try:
        command = [sys.executable, str(script_path)]
        if args:
            command.extend(args)

        logger.info(f"Running phase {phase}: {PHASE_DESCRIPTIONS[phase]}")
        print(f"\n=== Running Phase {phase}: {PHASE_DESCRIPTIONS[phase]} ===")

        result = subprocess.run(command, check=False, capture_output=False)

        success = result.returncode == 0
        if success:
            logger.info(f"Phase {phase} completed successfully")
        else:
            logger.error(
                f"Phase {phase} failed with exit code {result.returncode}"
            )

        return success
    except Exception as e:
        logger.error(f"Error running phase {phase}: {e}")
        return False


def main():
    """Main function to execute the BDD consolidation project."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="BDD Test Structure Consolidation"
    )
    parser.add_argument(
        "--start-phase",
        type=int,
        choices=range(1, 7),
        default=1,
        help="Start execution from this phase (1-6, default: 1)",
    )
    parser.add_argument(
        "--end-phase",
        type=int,
        choices=range(1, 7),
        default=6,
        help="End execution at this phase (1-6, default: 6)",
    )

    args = parser.parse_args()

    start_phase = args.start_phase
    end_phase = args.end_phase

    if start_phase > end_phase:
        logger.error(
            f"Start phase ({start_phase}) cannot be greater than end phase ({end_phase})"
        )
        print(
            f"Error: Start phase ({start_phase}) cannot be greater than end phase ({end_phase})"
        )
        return 1

    logger.info(
        f"Starting BDD Test Structure Consolidation (phases {start_phase}-{end_phase})"
    )
    print(
        f"Starting BDD Test Structure Consolidation (phases {start_phase}-{end_phase})"
    )

    # Run each phase in sequence
    for phase in range(start_phase, end_phase + 1):
        # Add specific arguments for certain phases
        phase_args = None
        if phase == 2 and start_phase == phase:  # First run of Phase 2
            phase_args = []  # No arguments for first run
        elif (
            phase == 2 and start_phase != phase
        ):  # Phase 2 called from full sequence
            phase_args = ["--cleanup"]  # Clean up in full sequence

        if phase == 3 and start_phase == phase:  # First run of Phase 3
            phase_args = []  # No arguments for first run
        elif (
            phase == 3 and start_phase != phase
        ):  # Phase 3 called from full sequence
            phase_args = ["--cleanup"]  # Clean up in full sequence

        # Execute the phase
        if not run_phase(phase, phase_args):
            logger.error(
                f"Stopping consolidation process due to failure in phase {phase}"
            )
            print(
                f"\nStopping consolidation process due to failure in phase {phase}"
            )
            return 1

    logger.info("BDD Test Structure Consolidation completed successfully")
    print("\nBDD Test Structure Consolidation completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
