# Portal Explorer User Guide

## Introduction

Portal Explorer is a tool for exploring and analyzing portals in Gather.town spaces. It allows you to:

- List all maps in a Gather.town space
- Analyze portals in specific maps
- Analyze portals across all maps
- Visualize connections between maps
- Export portal information in various formats

This guide will help you get started with Portal Explorer and make the most of its features.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)
7. [API Reference](#api-reference)

## Installation

### Prerequisites

Before installing Portal Explorer, ensure you have:

- Python 3.8 or higher
- A Gather.town API key
- A Gather.town space ID

### Installing Portal Explorer

You can install Portal Explorer using pip:

```bash
pip install portal-explorer
```

To verify the installation, run:

```bash
gather-explorer --version
```

This should display the version number of the installed Portal Explorer.

## Configuration

Before using Portal Explorer, you need to configure your API key and space ID. You can do this in two ways:

### Environment Variables

Set the following environment variables:

```bash
export GATHER_API_KEY=your_api_key
export GATHER_SPACE_ID=your_space_id
```

### Configuration File

Create a file at `~/.portal-explorer/config.ini` with the following content:

```ini
[gather]
api_key = your_api_key
space_id = your_space_id
```

## Basic Usage

### Listing Maps

To list all maps in your Gather.town space:

```bash
gather-explorer list-maps
```

This will display a table of all maps in your space, including their IDs and names.

Example output:

```
ID                      Name
----------------------  ----------------
main                    Main Office
cafeteria               Cafeteria
conference_room         Conference Room
```

### Exploring Portals in a Specific Map

To explore portals in a specific map:

```bash
gather-explorer explore --map-id <map_id>
```

Replace `<map_id>` with the ID of the map you want to explore.

Example output:

```
Map: Main Office (main)

Portals:
ID                      Position    Target Map       Target Position
----------------------  ----------  --------------   ---------------
portal1                 (10, 15)    cafeteria        (5, 5)
portal2                 (20, 25)    conference_room  (10, 10)
```

### Exploring Portals Across All Maps

To explore portals across all maps:

```bash
gather-explorer explore --all-maps
```

This will analyze portals in all maps and show connections between them.

Example output:

```
Map: Main Office (main)

Portals:
ID                      Position    Target Map       Target Position
----------------------  ----------  --------------   ---------------
portal1                 (10, 15)    cafeteria        (5, 5)
portal2                 (20, 25)    conference_room  (10, 10)

Map: Cafeteria (cafeteria)

Portals:
ID                      Position    Target Map       Target Position
----------------------  ----------  --------------   ---------------
portal3                 (5, 5)      main             (10, 15)

Map: Conference Room (conference_room)

Portals:
ID                      Position    Target Map       Target Position
----------------------  ----------  --------------   ---------------
portal4                 (10, 10)    main             (20, 25)

Connection Graph:
main <--> cafeteria (bidirectional)
main <--> conference_room (bidirectional)
```

## Advanced Usage

### Output Formats

Portal Explorer supports multiple output formats:

```bash
gather-explorer list-maps --format json
gather-explorer explore --all-maps --format csv --output portals.csv
```

Supported formats:
- `table` (default): Displays data in a formatted table
- `json`: Outputs data in JSON format
- `csv`: Outputs data in CSV format

### Saving Output to a File

To save the output to a file:

```bash
gather-explorer explore --all-maps --output analysis.json --format json
```

### Filtering Portals

You can filter portals by various criteria:

```bash
gather-explorer explore --map-id main --filter-target cafeteria
```

This will show only portals that lead to the "cafeteria" map.

### Analyzing Portal Connections

To focus on the connections between maps:

```bash
gather-explorer connections
```

This will display a graph of connections between maps without detailed portal information.

## Troubleshooting

### API Connection Issues

If you encounter API connection issues:

1. Check that your API key and space ID are correct
2. Ensure you have internet connectivity
3. Verify that the Gather.town API is operational
4. Check for any rate limiting or API usage restrictions

### Command Not Found

If you get a "command not found" error:

1. Ensure that Portal Explorer is installed
2. Check that your PATH includes the Python scripts directory
3. Try reinstalling the package: `pip install --force-reinstall portal-explorer`

### Permission Denied

If you get a "permission denied" error when running the command:

1. Check that the script has execute permissions
2. Try running with elevated privileges (if appropriate)
3. Verify that you have the necessary permissions to access the configuration files

## FAQ

### How do I get a Gather.town API key?

You can obtain an API key from the Gather.town developer portal at https://gather.town/developers.

### Can I analyze multiple spaces at once?

Currently, Portal Explorer can only analyze one space at a time. You need to change your configuration to switch between spaces.

### Is there a limit to how many maps I can analyze?

There is no limit imposed by Portal Explorer, but the Gather.town API may have rate limits or restrictions on the number of requests.

### Can I use Portal Explorer programmatically?

Yes, you can import the Portal Explorer modules in your Python code:

```python
from portal_explorer.client import GatherClient
from portal_explorer.service import PortalExplorer

client = GatherClient(api_key="YOUR_API_KEY", space_id="YOUR_SPACE_ID")
explorer = PortalExplorer(client)
portals = explorer.analyze_map_portals("main")
```

## API Reference

For detailed API documentation, please refer to the [API Reference](../api/index.md) section.

---

This user guide was generated for Portal Explorer version 1.0.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils).
