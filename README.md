# Gather.town API Explorer

A tool for exploring and analyzing Gather.town spaces, with a focus on understanding portal structures and connections between maps.

## Features

- List all maps in a Gather.town space
- Analyze portal objects across maps
- Extract detailed portal properties and connections
- Generate JSON reports for further analysis

## Installation

### Prerequisites

- Python 3.9+
- Poetry (for dependency management)

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd gather-manager
   ```

2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file with your Gather.town API credentials:
   ```
   GATHER_API_KEY=your_api_key_here
   GATHER_SPACE_ID=your_space_id_here
   ```

## Usage

### Command Line Interface

List all maps in a space:
```bash
poetry run gather-manager list-maps
```

Explore portals in all maps:
```bash
poetry run gather-manager explore
```

Explore portals in a specific map:
```bash
poetry run gather-manager explore --map-id=your_map_id
```

### Python API

```python
from gather_manager.api.client import GatherClient
from gather_manager.services.explorer import PortalExplorer

# Initialize client
client = GatherClient(api_key="your_api_key")

# List maps
maps = client.get_maps("your_space_id")

# Analyze portals
explorer = PortalExplorer(client=client)
portals = explorer.analyze_map_portals("your_space_id", "your_map_id")
```

## Project Structure

```
gather-manager/
├── src/
│   └── gather_manager/       # Main package
│       ├── api/              # API interaction layer
│       ├── models/           # Data models/schemas
│       ├── services/         # Business logic
│       ├── cli/              # Command-line interface
│       └── utils/            # Utility functions
├── tests/                    # Test suite
├── docs/                     # Documentation
├── examples/                 # Example usage
├── features/                 # BDD tests
│   ├── steps/                # Step definitions
│   ├── generated/            # Generated scenarios
│   └── README.md             # BDD documentation
├── tools/                    # Development tools
│   ├── bdd_coverage_report.py  # Generate BDD coverage reports
│   ├── run_bdd_tests.py        # Run BDD tests
│   └── bdd_scenario_generator.py  # Generate BDD scenarios
└── pyproject.toml           # Project dependencies and metadata
```

## Testing

### Unit Tests

Run the unit tests with pytest:
```bash
poetry run pytest
```

### BDD Tests

This project uses Behavior-Driven Development (BDD) for testing. The BDD tests are written using the [Behave](https://behave.readthedocs.io/) framework and follow the Gherkin syntax.

Run the BDD tests:
```bash
python tools/run_bdd_tests.py
```

Generate a BDD coverage report:
```bash
python tools/bdd_coverage_report.py
```

For more information about the BDD framework, see the [BDD README](features/README.md).

## License

[MIT License](LICENSE) 