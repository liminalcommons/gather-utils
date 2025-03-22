# Portal Explorer CLI Reference

This document provides detailed information about the Portal Explorer command-line interface.

## Global Options

These options apply to all Portal Explorer commands.

| Option | Description |
|--------|-------------|
| `--help` | Show help message and exit |
| `--version` | Show version and exit |
| `--api-key TEXT` | Gather.town API key (overrides config) |
| `--space-id TEXT` | Gather.town space ID (overrides config) |
| `--verbose` | Enable verbose output |

## Commands

### list-maps

List all maps in a Gather.town space.

```bash
gather-explorer list-maps [OPTIONS]
```

#### Options

| Option | Description |
|--------|-------------|
| `--format [table\|json\|csv]` | Output format (default: table) |
| `--output TEXT` | Output file path (default: stdout) |
| `--help` | Show help message and exit |

#### Examples

```bash
# List maps in table format
gather-explorer list-maps

# List maps in JSON format
gather-explorer list-maps --format json

# Save map list to a CSV file
gather-explorer list-maps --format csv --output maps.csv
```

### explore

Explore portals in a map or across all maps.

```bash
gather-explorer explore [OPTIONS]
```

#### Options

| Option | Description |
|--------|-------------|
| `--map-id TEXT` | ID of the map to explore |
| `--all-maps` | Explore all maps |
| `--filter-target TEXT` | Filter portals by target map |
| `--format [table\|json\|csv]` | Output format (default: table) |
| `--output TEXT` | Output file path (default: stdout) |
| `--help` | Show help message and exit |

#### Examples

```bash
# Explore portals in a specific map
gather-explorer explore --map-id main

# Explore portals across all maps
gather-explorer explore --all-maps

# Filter portals by target map
gather-explorer explore --map-id main --filter-target cafeteria

# Save exploration results to a JSON file
gather-explorer explore --all-maps --format json --output portals.json
```

### connections

Analyze connections between maps.

```bash
gather-explorer connections [OPTIONS]
```

#### Options

| Option | Description |
|--------|-------------|
| `--format [table\|json\|csv\|graph]` | Output format (default: table) |
| `--output TEXT` | Output file path (default: stdout) |
| `--help` | Show help message and exit |

#### Examples

```bash
# Show connections in table format
gather-explorer connections

# Show connections in graph format
gather-explorer connections --format graph

# Save connections to a JSON file
gather-explorer connections --format json --output connections.json
```

## Environment Variables

Portal Explorer recognizes the following environment variables:

| Variable | Description |
|----------|-------------|
| `GATHER_API_KEY` | Your Gather.town API key |
| `GATHER_SPACE_ID` | Your Gather.town space ID |
| `GATHER_API_URL` | (Optional) The base URL for the Gather.town API |

## Configuration File

Portal Explorer can be configured using a configuration file at `~/.portal-explorer/config.ini`:

```ini
[gather]
api_key = your_api_key
space_id = your_space_id
api_url = https://gather.town/api
```

## Exit Codes

| Code | Description |
|------|-------------|
| 0 | Success |
| 1 | General error |
| 2 | Configuration error |
| 3 | API error |
| 4 | Input error |

---

This CLI reference was generated for Portal Explorer version 1.0.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils).
