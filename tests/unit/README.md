# Unit Testing Guide

This directory contains unit tests for the project, following the Test-Driven Development (TDD) approach.

## Overview

Our unit tests are written using pytest and follow the TDD lifecycle management standards. All tests must include proper metadata to track their lifecycle status.

## Directory Structure

```
tests/unit/
├── api/            # Tests for API components
├── cli/            # Tests for CLI components
├── models/         # Tests for data models
├── services/       # Tests for service components
├── utils/          # Tests for utility functions
└── archive/        # Archived tests
    ├── test_files/ # Archived test files
    └── fixtures/   # Archived fixtures
```

## TDD Workflow

We follow the Red-Green-Refactor cycle:

1. **Red**: Write a failing test that defines the expected behavior
2. **Green**: Implement the minimum code to make the test pass
3. **Refactor**: Clean up the code while keeping tests passing

## Metadata Requirements

All test files must include metadata in the following format:

```python
"""
Tests for the module_name module.

Test Metadata:
- Created: YYYY-MM-DD
- Last Updated: YYYY-MM-DD
- Status: Draft|Active|Deprecated|Archived
- Owner: Team/Individual
- Purpose: Brief description of what this test is validating
- Lifecycle:
  - Created: Why this test was created
  - Active: Current usage status
  - Obsolescence Conditions:
    1. When this test would be considered obsolete
    2. Additional condition if applicable
- Last Validated: YYYY-MM-DD
"""
```

## Running Tests

To run all unit tests:

```bash
pytest tests/unit
```

To run a specific test file:

```bash
pytest tests/unit/test_file.py
```

To run with coverage:

```bash
pytest tests/unit --cov=src --cov-report=term --cov-report=html
```

## Test Validation

Tests are validated using the TDD validator tool:

```bash
python tools/tdd_validator.py --validate-metadata
python tools/tdd_validator.py --validate-status
python tools/tdd_validator.py --generate-lifecycle-report
```

## Documentation

For more detailed information, see:

- [TDD Lifecycle Management](../../docs/project/tdd/lifecycle_management.md)
- [TDD Best Practices](../../docs/project/tdd/best_practices.md)
- [Test Templates](../../docs/project/tdd/templates/)
- [TDD-BDD Integration](../../docs/project/tdd-bdd-integration.md)

## Continuous Integration

All unit tests are run as part of the CI pipeline. Tests must pass before code can be merged.

## Adding New Tests

When adding new tests:

1. Use the test templates in `docs/project/tdd/templates/`
2. Follow the naming convention: `test_<module_name>.py`
3. Include all required metadata
4. Follow the best practices in the TDD documentation
5. Ensure tests are isolated and don't depend on external state 