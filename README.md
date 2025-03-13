# Portal Explorer for Gather.town

A tool for exploring and analyzing Gather.town spaces, with a focus on understanding portal structures and connections between maps.

## Features

- List all maps in a Gather.town space
- Analyze portal objects across maps
- Extract detailed portal properties and connections
- Generate connection graphs between maps
- Export data in various formats (JSON, CSV, tables)

## Documentation

Comprehensive documentation is available in the `docs` directory:

- [User Guide](docs/user_guide/index.md): Comprehensive guide for end users
- [API Reference](docs/api/index.md): Technical documentation for developers
- [CLI Reference](docs/cli/index.md): Detailed command-line interface documentation
- [Tutorials](docs/tutorials/getting_started.md): Step-by-step guides for common tasks

## Installation

### Prerequisites

- Python 3.8+
- pip (for package installation)

### Setup

1. Install the package using pip:
   ```bash
   pip install portal-explorer
   ```

2. Configure your Gather.town API credentials:

   **Option 1: Environment Variables**
   ```bash
   export GATHER_API_KEY=your_api_key_here
   export GATHER_SPACE_ID=your_space_id_here
   ```

   **Option 2: Configuration File**
   Create a file at `~/.portal-explorer/config.ini`:
   ```ini
   [gather]
   api_key = your_api_key
   space_id = your_space_id
   ```

## Usage

### Command Line Interface

List all maps in a space:
```bash
gather-explorer list-maps
```

Explore portals in a specific map:
```bash
gather-explorer explore --map-id <map_id>
```

Explore portals across all maps:
```bash
gather-explorer explore --all-maps
```

Analyze connections between maps:
```bash
gather-explorer connections
```

Save results to a file:
```bash
gather-explorer explore --all-maps --format json --output portals.json
```

### Python API

```python
from portal_explorer.client import GatherClient
from portal_explorer.service import PortalExplorer

# Initialize client
client = GatherClient(api_key="your_api_key", space_id="your_space_id")

# List maps
maps = client.get_maps()

# Analyze portals in a specific map
explorer = PortalExplorer(client=client)
portals = explorer.analyze_map_portals("your_map_id")

# Analyze portals across all maps
all_portals = explorer.analyze_all_maps()

# Analyze connections between maps
connections = explorer.analyze_connections()

# Save results to a file
explorer.save_results(all_portals, "portals.json", format="json")
```

## Project Structure

```
portal-explorer/
├── src/
│   └── portal_explorer/      # Main package
│       ├── client.py         # API client
│       ├── models.py         # Data models
│       ├── service.py        # Portal explorer service
│       ├── cli.py            # Command-line interface
│       └── utils.py          # Utility functions
├── tests/                    # Test suite
├── docs/                     # Documentation
│   ├── user_guide/           # User guide
│   ├── api/                  # API reference
│   ├── cli/                  # CLI reference
│   └── tutorials/            # Tutorials
├── examples/                 # Example scripts
├── features/                 # BDD tests
│   ├── steps/                # Step definitions
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
pytest
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE) 