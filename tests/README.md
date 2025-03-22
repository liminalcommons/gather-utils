# Gather Manager Test Directory

This directory contains tests for the Gather Manager project. The tests are organized based on their type and purpose.

## Test Directory Structure

```
tests/
├── bdd/              # Behavior Driven Development tests
│   ├── features/     # BDD feature files
│   └── steps/        # BDD step definitions
├── data/             # Test data files
├── integration/      # Integration tests
├── unit/             # Unit tests organized by component
│   ├── api/          # Tests for API components
│   ├── cli/          # Tests for CLI components
│   ├── models/       # Tests for data models
│   ├── services/     # Tests for service components
│   ├── utils/        # Tests for utility functions
│   └── archive/      # Archived test files
└── conftest.py       # Global test configuration
```

## Test Methodology

The project uses a hybrid approach combining:

1. **Test-Driven Development (TDD)** for unit tests with proper metadata for lifecycle management
2. **Behavior-Driven Development (BDD)** for feature and acceptance testing

## Running Tests

### Unit Tests

Run the unit tests with pytest:

```bash
# Run all unit tests
pytest tests/unit

# Run tests for a specific component
pytest tests/unit/models
```

### BDD Tests

Run the BDD tests with behave:

```bash
behave tests/bdd/features
```

## Test Lifecycle Management

All test files follow standardized lifecycle management with proper metadata:

- **Creation date** - When the test was first written
- **Last updated** - When the test was most recently modified
- **Status** - Current status (Active, Deprecated, Archived)
- **Owner** - Person or team responsible for the test
- **Purpose** - What the test is verifying
- **Lifecycle stages** - Creation reason, current usage, and obsolescence conditions
- **Last validated** - When the test was last verified to be working correctly

This metadata helps maintain test quality and prevents test debt by ensuring tests can be properly evaluated for relevance and completeness.

## Legacy Test Directories

Legacy test directories have been migrated into the new structure:

- `tests/test_api` → `tests/unit/api`
- `tests/test_models` → `tests/unit/models`

The legacy tests have been archived to `tests/unit/archive/test_files` and replaced with properly structured tests that include required metadata.

## Test Metadata

All test files include metadata documenting their purpose, ownership, and lifecycle status. See the [TDD Lifecycle Management](../docs/project/tdd/lifecycle_management.md) document for details on metadata requirements.
