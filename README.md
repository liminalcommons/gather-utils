# Portal Explorer for Gather.town

A tool for exploring and analyzing Gather.town spaces, with a focus on understanding portal structures and connections between maps.

For development-focused documentation, see [DEVELOPER_README.md](DEVELOPER_README.md).

## Features

- List all maps in a Gather.town space
- Analyze portal objects across maps
- Extract detailed portal properties and connections
- Generate connection graphs between maps
- Export data in various formats (JSON, CSV, tables)

## Repository Structure

- `src/` - Source code
  - `gather_manager/` - Main package
    - `api/` - API client
    - `cli/` - Command-line interface
    - `models/` - Data models
    - `services/` - Business logic
    - `utils/` - Utility functions
- `tests/` - Tests
  - `unit/` - Unit tests (TDD)
  - `integration/` - Integration tests
  - `bdd/` - BDD tests
- `docs/` - Documentation
  - `project/` - Project documentation
  - `api/` - API documentation
  - `user_guide/` - User guide
  - `archive/` - Archived documentation
- `tools/` - Utility scripts and tools
  - `metadata_update/` - Tools for managing metadata compliance
- `examples/` - Example code and usage
- `data/` - Data files and analysis results
- `reports/` - Generated reports
  - `tool_metadata_compliance/` - Tool metadata compliance reports

## Documentation

Comprehensive documentation is available in the `docs` directory:

- [User Guide](docs/user_guide/index.md): Comprehensive guide for end users
- [API Reference](docs/api/index.md): Technical documentation for developers
- [CLI Reference](docs/cli/index.md): Detailed command-line interface documentation
- [Tutorials](docs/tutorials/getting_started.md): Step-by-step guides for common tasks
- [Maintenance Guidelines](docs/project/MAINTENANCE_GUIDELINES.md): Guidelines for maintaining the repository

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
│   ├── unit/                # Unit tests (TDD)
│   ├── integration/         # Integration tests
│   └── bdd/                 # BDD tests
│       ├── features/        # Feature files (organized by domain)
│       ├── steps/          # Step definitions
│       └── environment.py   # BDD test environment
├── docs/                    # Documentation
│   ├── project/            # Project documentation
│   ├── api/                # API reference
│   ├── cli/                # CLI reference
│   ├── tutorials/          # Tutorials
│   └── bdd/               # BDD documentation
├── examples/               # Example scripts
├── tools/                 # Development tools
│   ├── bdd/              # BDD-specific tools
│   ├── style/            # Style enforcement tools
│   └── docs/             # Documentation tools
└── pyproject.toml        # Project dependencies and metadata
```

For more information about:
- Development tools, see [tools/README.md](tools/README.md)
- BDD testing, see [docs/bdd/README.md](docs/bdd/README.md)
- TDD practices, see [docs/project/tdd/README.md](docs/project/tdd/README.md)
- Project system, see [docs/project/README.md](docs/project/README.md)

## Testing

### Unit Tests (TDD)

Run the unit tests with pytest:
```bash
pytest
```

For more information about TDD practices and lifecycle management, see the [TDD documentation](docs/project/tdd/README.md) and [Unit Testing Guide](tests/unit/README.md).

### BDD Tests

BDD tests are organized in the `tests/bdd` directory:

- `tests/bdd/features/`: Contains all feature files (organized by domain)
- `tests/bdd/steps/`: Contains all step definitions
- `tests/bdd/environment.py`: Environment setup for BDD tests

Run the BDD tests using pytest:
```bash
pytest tests/bdd
```

Or using behave:
```bash
behave tests/bdd/features
```

For more information on running and writing BDD tests, see:
- [BDD Testing Guide](docs/project/bdd/README.md)
- [BDD Tools Guide](docs/project/bdd/tools_guide.md)
- [BDD Conventions](docs/project/bdd/conventions.md)

## Development

### Code Style

This project follows PEP 8 style guidelines and uses pre-commit hooks to enforce them. To set up the pre-commit hooks:

1. Install the required tools:
   ```bash
   python tools/setup_style_tools.py
   ```

2. Fix existing style issues:
   ```bash
   python tools/fix_style_issues.py
   ```

3. The pre-commit hooks will automatically check your code before each commit. If there are style issues, the commit will be rejected and the issues will be fixed automatically. You can then stage the changes and commit again.

For more information about the code style guidelines, see the [Maintenance Guidelines](docs/project/MAINTENANCE_GUIDELINES.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

# Gather-Utils Project

Gather-Utils is a collection of utilities for managing and interacting with Gather.town spaces.

## Current Projects

### Tool Metadata Compliance Project

We're currently updating all tools in the repository to comply with standardized metadata requirements. See `tools/metadata_update/README.md` for details on this initiative.

Current status:
- Progress: 8/38 tools updated (21.1%)
- Next steps: Continue batch processing remaining tools

Tools for this project:
- `tools/metadata_update/metadata_injector.py` - Inject standardized metadata into tool files
- `tools/metadata_update/update_tracker.py` - Track and report on the progress of the project
- `tools/metadata_update/batch_processor.py` - Process multiple tools at once

Check the latest status report in `reports/tool_metadata_compliance/` for more details.
