# Portal Explorer for Gather.town

A tool for exploring and analyzing Gather.town spaces, with a focus on understanding portal structures and connections between maps.

## Features

- List all maps in a Gather.town space
- Analyze portal objects across maps
- Extract detailed portal properties and connections
- Generate connection graphs between maps
- Export data in various formats (JSON, CSV, tables)

## Project Structure

```
portal-explorer/
├── src/                    # Source code
│   └── portal_explorer/    # Main package
├── tests/                  # Test suite
│   ├── unit/              # Unit tests
│   └── bdd/               # BDD tests
├── docs/                   # Documentation
└── examples/              # Example scripts
```

## Development Setup

### Prerequisites

- Python 3.9+
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portal-explorer.git
   cd portal-explorer
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Configure your Gather.town API credentials:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

## Testing

### Unit Tests

Run unit tests with pytest:
```bash
poetry run pytest tests/unit
```

### BDD Tests

Run BDD tests with behave:
```bash
poetry run behave tests/bdd/features
```

## Development Practices

### Code Style

This project follows standard Python practices:

- [PEP 8](https://peps.python.org/pep-0008/) for code style
- [Black](https://black.readthedocs.io/) for code formatting
- [isort](https://pycqa.github.io/isort/) for import sorting
- [mypy](https://mypy.readthedocs.io/) for type checking
- [flake8](https://flake8.pycqa.org/) for linting

Pre-commit hooks are configured to ensure code quality:

```bash
poetry run pre-commit install
```

### Test-Driven Development (TDD)

We follow standard TDD practices:
1. Write a failing test
2. Write the minimum code to make it pass
3. Refactor while keeping tests green

### Behavior-Driven Development (BDD)

BDD tests are written in Gherkin syntax using behave:

```gherkin
# tests/bdd/features/map_listing.feature
Feature: List Maps
  Scenario: List all maps in a space
    Given I have valid API credentials
    When I request all maps
    Then I should receive a list of maps
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests first (TDD/BDD)
4. Implement your changes
5. Submit a pull request

## License

[MIT License](LICENSE)

# Gather-Utils Project

Gather-Utils is a collection of utilities for managing and interacting with Gather.town spaces.

## Current Projects

###TBD
