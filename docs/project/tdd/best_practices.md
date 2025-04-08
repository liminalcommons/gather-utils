---
Title: TDD Best Practices
Created: 2024-03-21
Last Updated: 2024-03-21
Status: Draft
Owner: Development Team
Purpose: Define best practices for Test-Driven Development
Audience: Developers, QA Engineers
Lifecycle:
  - Created: To establish clear best practices for TDD
  - Active: Used to guide TDD development
  - Obsolescence Conditions:
    1. When TDD approach is replaced by a different testing methodology
    2. When specific practices become obsolete due to tooling changes
Last Validated: 2024-03-21
---

# TDD Best Practices

This document outlines the best practices for Test-Driven Development (TDD) in our projects.

## Table of Contents

1. [TDD Workflow](#tdd-workflow)
2. [Test Organization](#test-organization)
3. [Naming Conventions](#naming-conventions)
4. [Test Structure](#test-structure)
5. [Fixtures and Mocks](#fixtures-and-mocks)
6. [Coverage Guidelines](#coverage-guidelines)
7. [Documentation Standards](#documentation-standards)
8. [Common Patterns](#common-patterns)

## TDD Workflow

### Red-Green-Refactor Cycle

1. **Red**: Write a failing test that defines the functionality you want to implement
2. **Green**: Write the minimum amount of code to make the test pass
3. **Refactor**: Clean up the code while keeping the tests passing

### Implementation Guidelines

1. **Test First**: Always write tests before implementing functionality
2. **Small Steps**: Make incremental changes with frequent test runs
3. **One Feature at a Time**: Focus on single functionality per cycle
4. **Maintain Working Code**: Never leave the codebase in a broken state

## Test Organization

### Directory Structure

```
tests/
├── unit/                # Unit tests
│   ├── test_module_a/   # Tests for module A
│   ├── test_module_b/   # Tests for module B
│   └── fixtures/        # Shared test fixtures
├── integration/         # Integration tests
└── conftest.py          # Shared pytest configuration
```

### File Organization

1. **Mirror Source**: Test files should mirror the structure of the source code
2. **One Module, One Test File**: Each module should have a corresponding test file
3. **Group Related Tests**: Group related test cases in the same file
4. **Separate Fixtures**: Place reusable fixtures in dedicated files

## Naming Conventions

### Files

- Test files should be named `test_<module_name>.py`
- Fixture files should be named `<name>_fixtures.py`

### Test Functions

- `test_<function_name>`: Tests for specific functions
- `test_<function_name>_<scenario>`: Tests for specific scenarios
- `test_<class_name>_<method_name>`: Tests for class methods

### Test Classes

- `Test<ClassName>`: Tests for a specific class
- `Test<FeatureName>`: Tests for a specific feature

## Test Structure

### Test Components

Each test should have:

1. **Arrangement (Setup)**: Prepare the test environment
2. **Action**: Execute the code being tested
3. **Assertion**: Verify the expected outcome

Example:
```python
def test_add_numbers():
    # Arrange
    a, b = 2, 3
    expected = 5

    # Act
    result = add_numbers(a, b)

    # Assert
    assert result == expected
```

### Test Isolation

1. **Independent Tests**: Tests should not depend on each other
2. **Clean Environment**: Reset state between tests
3. **Controlled Dependencies**: Mock external dependencies

## Fixtures and Mocks

### Fixture Usage

1. **Shared Setup**: Use fixtures for shared test setup
2. **Scoped Fixtures**: Use appropriate scope (function, class, module, session)
3. **Parametrized Tests**: Use parametrize for testing multiple inputs

Example:
```python
@pytest.fixture
def sample_user():
    return User(id=1, name="Test User")

def test_user_name(sample_user):
    assert sample_user.name == "Test User"
```

### Mocking Strategies

1. **External Dependencies**: Mock API calls, database connections, etc.
2. **Side Effects**: Mock functions with side effects
3. **Minimal Mocking**: Mock only what's necessary
4. **Realistic Data**: Use realistic test data

Example:
```python
def test_get_user_data(mocker):
    # Mock the API call
    mock_response = {"id": 1, "name": "Test User"}
    mocker.patch("app.services.api.get_user", return_value=mock_response)

    # Test the function that uses the API
    result = get_user_info(1)
    assert result.name == "Test User"
```

## Coverage Guidelines

### Coverage Targets

- **Unit Tests**: Aim for 90%+ line coverage
- **Branch Coverage**: Aim for 80%+ branch coverage
- **Critical Code**: 100% coverage for critical code paths

### Measuring Coverage

```bash
# Run tests with coverage
pytest --cov=app --cov-report=term --cov-report=html

# Check coverage report
open htmlcov/index.html
```

### Coverage Gaps

1. **Identify Gaps**: Regularly review coverage reports
2. **Prioritize Gaps**: Focus on critical functionality first
3. **Document Exclusions**: Document any code explicitly excluded from coverage

## Documentation Standards

### Test Documentation

Each test module should include:

```python
"""
Tests for the module_name module.

Test Metadata:
- Created: YYYY-MM-DD
- Last Updated: YYYY-MM-DD
- Status: Draft|Active|Deprecated|Archived
- Owner: Team/Individual
- Purpose: What these tests are validating
- Lifecycle:
  - Created: Why these tests were created
  - Active: Current usage status
  - Obsolescence Conditions:
    1. When these tests would be considered obsolete
    2. Additional condition if applicable
- Last Validated: YYYY-MM-DD
"""
```

### Function Documentation

Each test function should have a docstring explaining:
- What functionality is being tested
- Any edge cases being handled
- Expected behavior

Example:
```python
def test_divide_by_zero():
    """
    Test that divide() raises a ValueError when dividing by zero.

    This test verifies the error handling behavior of the divide function
    when the divisor is zero.
    """
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)
```

## Common Patterns

### Testing Exceptions

```python
def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        process_input(-1)
    assert "Input must be positive" in str(excinfo.value)
```

### Testing Asynchronous Code

```python
@pytest.mark.asyncio
async def test_async_function():
    result = await async_operation()
    assert result == expected_value
```

### Parameterized Tests

```python
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input, expected):
    assert square(input) == expected
```

### Test Factories

```python
def create_test_user(name="Test User", role="user"):
    """Factory function to create test users with default values."""
    return User(name=name, role=role)
```

## References

- [TDD Lifecycle Management](./lifecycle_management.md)
- [pytest Documentation](https://docs.pytest.org/)
- [Factory Pattern](../patterns/factory_pattern.md)
- [Mocking Best Practices](../testing/mocking_best_practices.md)
