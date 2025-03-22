# Getting Started with Gather Manager

This tutorial will guide you through the process of setting up and using Gather Manager to analyze portals in your Gather.town space.

## Prerequisites

Before you begin, make sure you have:

- Python 3.9 or higher installed
- A Gather.town API key
- A Gather.town space ID

## Installation

1. Install Gather Manager using pip:

```bash
pip install gather-manager
```

2. Verify the installation:

```bash
gather-manager --version
```

You should see the version number of Gather Manager displayed.

## Configuration

There are three ways to configure Gather Manager:

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

### Option 2: .env File

Create a `.env` file in your current working directory or in `~/.gather-manager/.env`:

```
GATHER_API_KEY=your_api_key
GATHER_SPACE_ID=your_space_id
```

Gather Manager will automatically load these environment variables when it starts.

### Option 3: Configuration File

Create a configuration file at `~/.gather-manager/config.ini` (Linux/macOS) or `%USERPROFILE%\.gather-manager\config.ini` (Windows):

```ini
[gather]
api_key = your_api_key
space_id = your_space_id
```

> **Note:** If you specify the same configuration in multiple places, the following order of precedence applies:
> 1. Command line arguments (e.g., `--space-id`)
> 2. Environment variables (including those from `.env` files)
> 3. Configuration file

### Testing Your Configuration

To verify that your API key and space ID are working correctly, you can run the included test script:

```bash
python test_api_connection.py
```

This script will:
1. Check if your API key and space ID are properly set
2. Connect to the Gather.town API
3. List the maps in your space
4. Test retrieving objects from a map

If everything is working correctly, you should see a success message and a list of maps in your space.

## Tutorial: Exploring Portals in Your Space

### Step 1: List All Maps

First, let's list all the maps in your Gather.town space:

```bash
gather-manager list-maps
```

You can also specify the space ID directly as a parameter:

```bash
gather-manager list-maps --space-id your_space_id
```

You should see a table listing all the maps in your space, including their IDs and names.

Example output:

```
Maps in space your_space_id
┏━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Map ID               ┃ Name          ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ main                 │ Main Office   │
│ 2 │ cafeteria            │ Cafeteria     │
│ 3 │ conference_room      │ Conference Room│
└───┴──────────────────────┴───────────────┘
```

Take note of the map IDs, as you'll need them for the next steps.

### Step 2: Explore Portals in a Specific Map

Now, let's explore the portals in a specific map. Replace `<map_id>` with one of the map IDs from the previous step:

```bash
gather-manager explore --map-id <map_id>
```

You can also specify the space ID directly as a parameter:

```bash
gather-manager explore --space-id your_space_id --map-id <map_id>
```

Example:

```bash
gather-manager explore --map-id main
```

This will display information about the portals in the specified map, including a sample portal structure.

Example output:

```
Analyzing portals in map: main
Found 5 portals

Sample portal structure:
  id: portal1
  x: 10
  y: 15
  targetMap: cafeteria
  targetX: 5
  targetY: 5
  ...

Results saved to: data/session_20240315_123456/
```

### Step 3: Explore Portals Across All Maps

To analyze portals in all maps in your space, simply run the explore command without specifying a map ID:

```bash
gather-manager explore
```

You can also specify the space ID directly as a parameter:

```bash
gather-manager explore --space-id your_space_id
```

This will analyze portals in all maps and provide a summary of the findings.

Example output:

```
Analyzing all maps in space: your_space_id
Analyzed 3 maps, found 12 portals total

Results saved to: data/session_20240315_123456/
```

### Step 4: Perform Detailed Portal Property Analysis

For a more detailed analysis of portal properties, use the `--analyze-properties` (or `-p`) flag:

```bash
gather-manager explore --analyze-properties
```

You can also specify the space ID directly as a parameter:

```bash
gather-manager explore --space-id your_space_id --analyze-properties
```

This will perform additional analysis on portal properties, showing frequency and directional analysis.

Example output:

```
Analyzing all maps in space: your_space_id
Analyzed 3 maps, found 12 portals total

Performing detailed portal property analysis...
┏━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━┓
┃ Property       ┃ Count ┃ Percentage ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━┩
│ targetMap      │ 12    │ 100%       │
│ targetX        │ 12    │ 100%       │
│ targetY        │ 12    │ 100%       │
│ locked         │ 5     │ 41.7%      │
│ hidden         │ 2     │ 16.7%      │
└────────────────┴───────┴────────────┘

Directional Properties Analysis:
  locked appears directional: No
    Values: [true, false]
  hidden appears directional: Yes
    Values: [true]

Results saved to: data/session_20240315_123456/
```

### Step 5: Save Results for Further Analysis

All results from your exploration are automatically saved to the output directory (default: `data/`). Each session creates a timestamped directory containing the analysis results.

You can specify a custom output directory using the `--output-dir` option:

```bash
gather-manager explore --output-dir my_analysis
```

You can also combine this with other parameters:

```bash
gather-manager explore --space-id your_space_id --output-dir my_analysis
```

## Next Steps

Now that you've learned the basics of Gather Manager, you can:

- Explore more advanced features in the [User Guide](../user_guide/index.md)
- Learn about the API for programmatic use in the [API Reference](../api/index.md)
- Check out the [CLI Reference](../cli/index.md) for detailed information about all available commands and options

## Troubleshooting

If you encounter any issues:

### API Key and Space ID Issues

1. Verify that your API key and space ID are correct
2. Run the test script to check your connection: `python test_api_connection.py`
3. Make sure you have internet connectivity
4. Check that you're using the latest version of Gather Manager

### Portal Detection Issues

If you're not seeing portals that you know exist in your map, you can use the debug script to analyze the map objects:

```bash
python debug_map_objects.py <map_id>
```

This script will:
1. Analyze all objects in the specified map
2. Show the distribution of object types
3. Identify potential portal candidates
4. Save the analysis to a JSON file for further investigation

The analysis can help identify what object types correspond to portals in your specific Gather.town space.

### Validation Errors

If you see errors like:
```ValidationError: ... validation errors for MapData
objects.0.type
  Input should be a valid string
```

This usually indicates that the Gather.town API has returned data in a format that doesn't match our expectations. The latest version of Gather Manager should handle these cases automatically, but if you're using an older version, please update to the latest version:

```bash
pip install --upgrade gather-manager
```

### Other Issues

If you're still experiencing problems:

1. Check that you have Python 3.9 or higher installed
2. Make sure all dependencies are correctly installed
3. Try running with verbose logging: `LOG_LEVEL=DEBUG gather-manager ...`
4. Check the [project repository](https://github.com/liminalcommons/gather-utils) for known issues

---

This tutorial was created for Gather Manager version 0.1.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils). 