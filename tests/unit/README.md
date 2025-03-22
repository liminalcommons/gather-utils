# Unit Tests Directory

This directory contains test files organized in a TDD (Test-Driven Development) fashion. Tests are structured by component type.

## Directory Structure

```
unit/
├── api/          # Tests for API components
├── cli/          # Tests for CLI components
├── models/       # Tests for data models
├── services/     # Tests for service components
├── utils/        # Tests for utility components
└── archive/      # Archived test files
    └── test_files/ # Legacy test files preserved for reference
```

## Test Organization

Tests are organized by component type:

- `api/`: Tests for API-related functionality including client interactions with the Gather API
- `cli/`: Tests for command-line interface functionality
- `models/`: Tests for data models and domain entities
- `services/`: Tests for service layer business logic
- `utils/`: Tests for utility functions and helpers

## Naming Conventions

- Test files follow the pattern: `test_<module_name>.py`
- Test classes follow the pattern: `Test<ClassName>`
- Test methods follow the pattern: `test_<functionality_being_tested>`

## TDD Metadata

All test files include standardized metadata for lifecycle management:

```python
"""
Unit tests for [component].

Test Metadata:
- Created: [Date]
- Last Updated: [Date]
- Status: [Active/Deprecated/Archived]
- Owner: [Owner]
- Purpose: [Purpose]
- Lifecycle:
  - Created: [Creation reason]
  - Active: [Current usage]
  - Obsolescence Conditions: [When the test will become obsolete]
- Last Validated: [Date]
"""
```

## Running Tests

Tests can be run using pytest:

```bash
pytest tests/unit
```

Or for a specific component:

```bash
pytest tests/unit/models
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
