# Portal Explorer API Reference

This document provides detailed information about the Portal Explorer API for developers who want to use the tool programmatically.

## Table of Contents

1. [Client API](#client-api)
2. [Service API](#service-api)
3. [Models](#models)
4. [Utilities](#utilities)

## Client API

The `GatherClient` class provides methods for interacting with the Gather.town API.

### GatherClient

```python
from portal_explorer.client import GatherClient

client = GatherClient(api_key="YOUR_API_KEY", space_id="YOUR_SPACE_ID")
```

#### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| api_key | str | Your Gather.town API key |
| space_id | str | The ID of the Gather.town space |
| base_url | str | (Optional) The base URL for the Gather.town API |

#### Methods

##### get_space()

Retrieves information about the configured space.

```python
space_data = client.get_space()
```

**Returns**: A dictionary containing space information.

##### get_maps()

Retrieves all maps in the configured space.

```python
maps = client.get_maps()
```

**Returns**: A list of map objects.

##### get_map(map_id)

Retrieves a specific map by ID.

```python
map_data = client.get_map("main")
```

**Parameters**:
- `map_id` (str): The ID of the map to retrieve.

**Returns**: A map object.

##### get_portals(map_id)

Retrieves all portals in a specific map.

```python
portals = client.get_portals("main")
```

**Parameters**:
- `map_id` (str): The ID of the map to retrieve portals from.

**Returns**: A list of portal objects.

## Service API

The `PortalExplorer` class provides high-level methods for analyzing portals.

### PortalExplorer

```python
from portal_explorer.client import GatherClient
from portal_explorer.service import PortalExplorer

client = GatherClient(api_key="YOUR_API_KEY", space_id="YOUR_SPACE_ID")
explorer = PortalExplorer(client)
```

#### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| client | GatherClient | An instance of the GatherClient class |

#### Methods

##### analyze_map_portals(map_id)

Analyzes portals in a specific map.

```python
portals = explorer.analyze_map_portals("main")
```

**Parameters**:
- `map_id` (str): The ID of the map to analyze.

**Returns**: A list of Portal objects.

##### analyze_all_maps()

Analyzes portals across all maps in the space.

```python
all_portals = explorer.analyze_all_maps()
```

**Returns**: A dictionary mapping map IDs to lists of Portal objects.

##### analyze_connections()

Analyzes connections between maps.

```python
connections = explorer.analyze_connections()
```

**Returns**: A list of PortalConnection objects.

##### save_results(data, output_file, format="json")

Saves analysis results to a file.

```python
explorer.save_results(portals, "portals.json", format="json")
```

**Parameters**:
- `data`: The data to save.
- `output_file` (str): The path to the output file.
- `format` (str): The output format (json, csv, or table).

## Models

### Portal

The `Portal` class represents a portal in a Gather.town map.

```python
from portal_explorer.models import Portal

portal = Portal(
    id="portal1",
    position=(10, 15),
    target_map="cafeteria",
    target_position=(5, 5)
)
```

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| id | str | The unique identifier of the portal |
| position | Tuple[int, int] | The (x, y) position of the portal in the map |
| target_map | str | The ID of the map this portal leads to |
| target_position | Tuple[int, int] | The position in the target map where this portal leads to |

### MapData

The `MapData` class represents a map in a Gather.town space.

```python
from portal_explorer.models import MapData

map_data = MapData(
    id="main",
    name="Main Office",
    portals=[]
)
```

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| id | str | The unique identifier of the map |
| name | str | The name of the map |
| portals | List[Portal] | The portals in the map |

### PortalConnection

The `PortalConnection` class represents a connection between two maps.

```python
from portal_explorer.models import PortalConnection

connection = PortalConnection(
    source_map="main",
    target_map="cafeteria",
    bidirectional=True
)
```

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| source_map | str | The ID of the source map |
| target_map | str | The ID of the target map |
| bidirectional | bool | Whether the connection is bidirectional |

## Utilities

### Formatting

The `portal_explorer.cli` module provides utilities for formatting output.

```python
from portal_explorer.cli import format_maps_table, format_portals_table

# Format maps as a table
maps_table = format_maps_table(maps)

# Format portals as a table
portals_table = format_portals_table(portals)
```

### Configuration

The `portal_explorer.config` module provides utilities for loading configuration.

```python
from portal_explorer.config import load_config

# Load configuration from environment variables or config file
config = load_config()
```

---

This API reference was generated for Portal Explorer version 1.0.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils). 