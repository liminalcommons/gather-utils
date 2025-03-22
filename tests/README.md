# Gather Manager Test Directory

This directory contains tests for the Gather Manager project. The tests are organized based on their type and purpose:

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

## Test Types

- **Unit Tests**: Tests for individual components and functions
- **Integration Tests**: Tests that verify interactions between components
- **BDD Tests**: Tests that validate behavior against business requirements

## Running Tests

To run all tests:

```bash
pytest
```

To run specific test types:

```bash
# Unit tests
pytest tests/unit

# BDD tests
pytest tests/bdd

# Integration tests
pytest tests/integration
```

## Test Lifecycle Management

All tests follow the TDD lifecycle management approach. See [TDD Lifecycle Management](../docs/project/tdd/lifecycle_management.md) for details.

## Legacy Test Directories

Legacy test directories have been migrated into the new structure:

- `tests/test_api` → `tests/unit/api`
- `tests/test_models` → `tests/unit/models`

The legacy tests have been archived to `tests/unit/archive/test_files` and replaced with properly structured tests that include required metadata.

## Test Metadata

All test files include metadata documenting their purpose, ownership, and lifecycle status. See the [TDD Lifecycle Management](../docs/project/tdd/lifecycle_management.md) document for details on metadata requirements. 