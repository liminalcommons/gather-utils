# Getting Started with Portal Explorer

This tutorial will guide you through the process of setting up and using Portal Explorer to analyze portals in your Gather.town space.

## Prerequisites

Before you begin, make sure you have:

- Python 3.8 or higher installed
- A Gather.town API key
- A Gather.town space ID

## Installation

1. Install Portal Explorer using pip:

```bash
pip install portal-explorer
```

2. Verify the installation:

```bash
gather-explorer --version
```

You should see the version number of Portal Explorer displayed.

## Configuration

There are two ways to configure Portal Explorer:

### Option 1: Environment Variables

Set the following environment variables:

```bash
# On Linux/macOS
export GATHER_API_KEY=your_api_key
export GATHER_SPACE_ID=your_space_id

# On Windows (Command Prompt)
set GATHER_API_KEY=your_api_key
set GATHER_SPACE_ID=your_space_id

# On Windows (PowerShell)
$env:GATHER_API_KEY = "your_api_key"
$env:GATHER_SPACE_ID = "your_space_id"
```

### Option 2: Configuration File

Create a configuration file at `~/.portal-explorer/config.ini` (Linux/macOS) or `%USERPROFILE%\.portal-explorer\config.ini` (Windows):

```ini
[gather]
api_key = your_api_key
space_id = your_space_id
```

## Tutorial: Exploring Portals in Your Space

### Step 1: List All Maps

First, let's list all the maps in your Gather.town space:

```bash
gather-explorer list-maps
```

You should see a table listing all the maps in your space, including their IDs and names.

Example output:

```
ID                      Name
----------------------  ----------------
main                    Main Office
cafeteria               Cafeteria
conference_room         Conference Room
```

Take note of the map IDs, as you'll need them for the next steps.

### Step 2: Explore Portals in a Specific Map

Now, let's explore the portals in a specific map. Replace `<map_id>` with one of the map IDs from the previous step:

```bash
gather-explorer explore --map-id <map_id>
```

Example:

```bash
gather-explorer explore --map-id main
```

This will display a table of all portals in the specified map, including their IDs, positions, target maps, and target positions.

Example output:

```
Map: Main Office (main)

Portals:
ID                      Position    Target Map       Target Position
----------------------  ----------  --------------   ---------------
portal1                 (10, 15)    cafeteria        (5, 5)
portal2                 (20, 25)    conference_room  (10, 10)
```

### Step 3: Explore Portals Across All Maps

To get a comprehensive view of all portals in your space, run:

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

### Step 4: Save Results to a File

You can save the results of your exploration to a file in various formats:

```bash
gather-explorer explore --all-maps --format json --output portals.json
```

This will save the portal information to a JSON file named `portals.json`.

You can also use other formats like CSV:

```bash
gather-explorer explore --all-maps --format csv --output portals.csv
```

### Step 5: Analyze Connections Between Maps

To focus specifically on the connections between maps:

```bash
gather-explorer connections
```

Example output:

```
Connections:
Source Map             Target Map             Bidirectional
---------------------- ---------------------- -------------
main                   cafeteria              Yes
main                   conference_room        Yes
```

## Next Steps

Now that you've learned the basics of Portal Explorer, you can:

- Explore more advanced features in the [User Guide](../user_guide/index.md)
- Learn about the API for programmatic use in the [API Reference](../api/index.md)
- Check out the [CLI Reference](../cli/index.md) for detailed information about all available commands and options

## Troubleshooting

If you encounter any issues:

1. Verify that your API key and space ID are correct
2. Check that you have internet connectivity
3. Make sure you're using the latest version of Portal Explorer
4. Consult the [Troubleshooting](../user_guide/index.md#troubleshooting) section in the User Guide

---

This tutorial was created for Portal Explorer version 1.0.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils). 