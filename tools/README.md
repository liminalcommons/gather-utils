# BDD Tools for Gather.town Portal Explorer

This directory contains tools for working with the BDD tests for the Gather.town Portal Explorer.

## Available Tools

### BDD Test Runner

`run_bdd_tests.py` - Runs the BDD tests and generates a coverage report.

Usage:
```bash
python tools/run_bdd_tests.py [--tags TAG]
```

Options:
- `--tags TAG`: Run only scenarios with the given tag (e.g., `--tags=REQ-1.1`)

### BDD Coverage Report Generator

`bdd_coverage_report.py` - Generates a report showing which requirements from the project plan are covered by BDD scenarios.

Usage:
```bash
python tools/bdd_coverage_report.py
```

Output:
- A markdown report showing test coverage (`reports/bdd_coverage_report.md`)
- A JSON file with detailed coverage data (`reports/bdd_coverage_data.json`)

### BDD Scenario Generator

`bdd_scenario_generator.py` - Generates skeleton BDD scenarios for requirements that don't have corresponding scenarios yet.

Usage:
```bash
python tools/bdd_scenario_generator.py [--milestone MILESTONE]
```

Options:
- `--milestone MILESTONE`: Generate scenarios only for the specified milestone

Output:
- Feature files in `features/generated/`
- Step definition files in `features/steps/`

## Integration with CI

These tools are integrated with the CI pipeline using GitHub Actions. The workflow is defined in `.github/workflows/bdd-tests.yml`.

## Best Practices

- Run the BDD tests before committing changes
- Generate a coverage report to ensure all requirements are covered
- Use the scenario generator to create skeleton scenarios for new requirements
- Keep the BDD tests up-to-date with the project plan 