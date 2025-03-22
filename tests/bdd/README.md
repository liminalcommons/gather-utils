# BDD Testing Structure

This document outlines the consolidated BDD testing structure for the project.

## Directory Structure

All BDD tests are now organized under the `tests/bdd` directory:

```
tests/bdd/
├── features/     # Contains all feature files
├── steps/        # Contains all step definitions
└── environment.py # Environment setup for BDD tests
```

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

## Configuration

BDD testing is configured through the following files:

- `pytest.ini`: Contains pytest configuration for BDD tests
- `behave.ini`: Contains behave-specific configuration

## Writing BDD Tests

### Feature Files

Feature files should be placed in the `tests/bdd/features` directory and follow this format:

```gherkin
Feature: Feature name
  As a [role]
  I want [feature]
  So that [benefit]

  Scenario: Scenario name
    Given [precondition]
    When [action]
    Then [expected result]
```

### Step Definitions

Step definitions should be placed in the `tests/bdd/steps` directory and follow this format:

```python
from pytest_bdd import given, when, then

@given("precondition")
def step_impl(context):
    # Implementation
    pass

@when("action")
def step_impl(context):
    # Implementation
    pass

@then("expected result")
def step_impl(context):
    # Implementation
    pass
```

## Best Practices

1. Keep feature files focused on business requirements
2. Write step definitions that are reusable
3. Use tags to categorize and filter tests
4. Maintain a consistent naming convention

Last updated: 2025-03-17
