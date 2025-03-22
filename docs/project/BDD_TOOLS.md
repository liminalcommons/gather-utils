# BDD Testing Tools

## Overview

This document provides information about the tools developed for BDD test structure consolidation and management.

## Consolidation Tools

### Main Orchestration

- **bdd_consolidation.py**: The main orchestration script that runs all phases of the BDD consolidation process.
  - Usage: `python tools/bdd_consolidation.py [--start-phase PHASE] [--end-phase PHASE]`

### Phase-Specific Scripts

1. **bdd_consolidation_phase1.py**: Preparation phase (backup and documentation)
2. **bdd_consolidation_phase2.py**: Feature File Consolidation
3. **bdd_consolidation_phase3.py**: Step Definition Consolidation
4. **bdd_consolidation_phase4.py**: Configuration Cleanup
5. **bdd_consolidation_phase5.py**: Verification
6. **bdd_consolidation_phase6.py**: Final Cleanup

### Utility Scripts

- **feature_file_consolidation.py**: Consolidates feature files from different locations
- **step_definition_consolidation.py**: Consolidates step definition files
- **config_cleanup.py**: Cleans up configuration files like pytest.ini and behave.ini
- **bdd_verification.py**: Verifies that BDD tests run correctly after consolidation
- **final_cleanup.py**: Performs final cleanup tasks

## Verification and Migration Tools

### Step Verification

The `step_verification.py` tool verifies that all steps from legacy step definition files have been properly migrated to the consolidated step repository.

Usage:
```bash
python tools/step_verification.py [legacy_step_file] [consolidated_steps_dir]
```

This tool:
1. Extracts step patterns from a legacy step definition file
2. Extracts step patterns from all step definition files in the consolidated repository
3. Compares the steps to identify any missing steps
4. Reports the missing steps and where existing steps are implemented

### Step Migration

The `migrate_missing_steps.py` tool migrates missing steps from legacy step definition files to the consolidated step repository.

Usage:
```bash
python tools/migrate_missing_steps.py
```

This tool:
1. Identifies steps missing from the consolidated repository
2. Extracts the implementations of these steps from the legacy file
3. Migrates the step implementations to the appropriate file in the consolidated repository
4. Creates a migration report

## Running BDD Tests

BDD tests can be run using either pytest or behave:

### Using pytest

```bash
pytest tests/bdd
```

### Using behave

```bash
behave tests/bdd/features
```

## BDD Structure

All BDD tests are now located in the `tests/bdd` directory with the following structure:

```
tests/bdd/
├── features/     # Contains all feature files
├── steps/        # Contains all step definitions
└── environment.py # Environment setup for BDD tests
```

## Configuration

BDD testing is configured through:

- `pytest.ini`: Contains pytest configuration for BDD tests
- `behave.ini`: Contains behave-specific configuration 