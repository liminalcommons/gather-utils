# BDD Testing Framework for Gather.town Portal Explorer

This directory contains the Behavior-Driven Development (BDD) tests for the Gather.town Portal Explorer. The tests are written using the [Behave](https://behave.readthedocs.io/) framework and follow the Gherkin syntax.

## Directory Structure

- `features/`: Contains all feature files and step definitions
  - `*.feature`: Feature files describing the behavior of the system
  - `steps/`: Step definitions implementing the behavior
  - `environment.py`: Setup and teardown hooks for the BDD tests
  - `generated/`: Auto-generated feature files for missing requirements

## Feature Files

Each feature file corresponds to a milestone in the project plan:

- `milestone1_portal_functionality.feature`: Tests for the Portal Functionality milestone
- `milestone2_portal_explorer_service.feature`: Tests for the Portal Explorer Service milestone
- `milestone3_command_line_interface.feature`: Tests for the Command Line Interface milestone
- `milestone4_testing_quality_assurance.feature`: Tests for the Testing & Quality Assurance milestone
- `milestone5_documentation_examples.feature`: Tests for the Documentation & Examples milestone
- `bdd_integration.feature`: Tests for the BDD Integration itself

## Running the Tests

To run all BDD tests:

```bash
python tools/run_bdd_tests.py
```

To run tests for a specific feature:

```bash
behave features/milestone1_portal_functionality.feature
```

To run tests with a specific tag:

```bash
python tools/run_bdd_tests.py --tags=REQ-1.1
```

## Test Coverage

The BDD tests are mapped to requirements in the project plan using tags. Each scenario is tagged with the corresponding requirement ID (e.g., `@REQ-1.1`).

To generate a test coverage report:

```bash
python tools/bdd_coverage_report.py
```

The report will be saved to `reports/bdd_coverage_report.md`.

## Generating BDD Scenarios

To generate BDD scenarios for requirements that don't have corresponding scenarios yet:

```bash
python tools/bdd_scenario_generator.py
```

To generate scenarios for a specific milestone:

```bash
python tools/bdd_scenario_generator.py --milestone="Portal Functionality"
```

## CI Integration

The BDD tests are integrated with the CI pipeline using GitHub Actions. The workflow is defined in `.github/workflows/bdd-tests.yml`.

## Writing New Tests

To add a new test:

1. Create a new scenario in the appropriate feature file or create a new feature file
2. Tag the scenario with the corresponding requirement ID (e.g., `@REQ-1.1`)
3. Implement the step definitions in the `steps/` directory
4. Run the tests to verify that they pass

## Best Practices

- Use the Given-When-Then format for scenarios
- Keep scenarios focused on a single behavior
- Use descriptive scenario names
- Reuse step definitions where possible
- Tag scenarios with the corresponding requirement ID
- Keep step definitions simple and focused
- Use background steps for common setup 