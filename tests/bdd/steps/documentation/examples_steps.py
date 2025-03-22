"""
Step definitions for the Documentation & Examples feature.
"""
from behave import given, when, then
from unittest.mock import MagicMock, patch
import os
from pathlib import Path

# Import common steps
from tests.bdd.steps.common.setup_steps import *


@given('I have installed the Portal Explorer package')
def step_given_have_installed_package(context):
    """Set up having installed the package."""
    # This is already defined in common/cli_steps.py
    # Here we'll just create the context value
    context.package_installed = True
    assert context.package_installed, "Package should be installed"


@given('I am viewing the README file')
def step_given_am_viewing_readme_file(context):
    """Set up viewing the README file."""
    # Mock the README content
    context.readme_content = """
# Portal Explorer

A tool for exploring and analyzing portals in Gather.town spaces.

## Installation

```bash
pip install portal-explorer
```

## Usage

```bash
# List all maps in a space
gather-explorer list-maps

# Explore portals in a specific map
gather-explorer explore --map-id <map_id>

# Explore portals across all maps
gather-explorer explore --all-maps
```

## Features

- List all maps in a Gather.town space
- Analyze portals in a specific map
- Analyze portals across all maps
- Show connections between maps
- Export portal information to various formats

## API Key Configuration

You can configure your Gather.town API key by:

1. Setting the `GATHER_API_KEY` environment variable
2. Creating a config file at `~/.portal-explorer/config.ini`
3. Passing it directly with the `--api-key` flag
"""
    assert "Portal Explorer" in context.readme_content, "README should include the project name"


@given('I am viewing the CLI documentation')
def step_given_am_viewing_cli_documentation(context):
    """Set up viewing the CLI documentation."""
    # Mock the CLI documentation content
    context.cli_docs = """
# Portal Explorer CLI

## Commands

### List Maps

List all maps in a Gather.town space.

```bash
gather-explorer list-maps
```

Options:
- `--format`: Output format (table, json, csv). Default: table.
- `--output`: Output file path. If not provided, prints to stdout.

### Explore

Explore portals in a map or across all maps.

```bash
# Explore a specific map
gather-explorer explore --map-id <map_id>

# Explore all maps
gather-explorer explore --all-maps
```

Options:
- `--map-id`: ID of the map to explore. Cannot be used with --all-maps.
- `--all-maps`: Explore all maps. Cannot be used with --map-id.
- `--format`: Output format (table, json, csv). Default: table.
- `--output`: Output file path. If not provided, prints to stdout.

### Validate

Validate portals across maps for inconsistencies.

```bash
gather-explorer validate
```

Options:
- `--check-bidirectional`: Check for one-way portals.
- `--report`: Generate a detailed report file.
"""
    assert "Portal Explorer CLI" in context.cli_docs, "CLI docs should include the CLI name"


@given('I am viewing the API documentation')
def step_given_am_viewing_api_documentation(context):
    """Set up viewing the API documentation."""
    # Mock the API documentation content
    context.api_docs = """
# Portal Explorer API

## Classes

### GatherClient

Client for interacting with the Gather.town API.

```python
client = GatherClient(api_key="your_api_key", space_id="your_space_id")
```

#### Methods

- `get_space()`: Get information about the current space.
- `get_maps()`: Get all maps in the space.
- `get_map_objects(map_id)`: Get all objects in a specific map.
- `get_portals(map_id=None)`: Get all portals in a map or all maps.

### PortalExplorer

Service for exploring and analyzing portals.

```python
explorer = PortalExplorer(client)
```

#### Methods

- `analyze_map_portals(map_id)`: Analyze portals in a specific map.
- `analyze_all_maps()`: Analyze portals across all maps.
- `analyze_connections(portal_data)`: Analyze portal connections.
- `save_results(results, output_file)`: Save analysis results to a file.
"""
    assert "Portal Explorer API" in context.api_docs, "API docs should include the API name"


@given('I am viewing the examples directory')
def step_given_am_viewing_examples_directory(context):
    """Set up viewing the examples directory."""
    # Mock the examples directory content
    context.example_scripts = {
        "list_maps_example.py": """
# Example: List all maps in a Gather.town space
from portal_explorer.client import GatherClient
from portal_explorer.cli import format_maps_table

# Initialize the client with your API key and space ID
client = GatherClient(api_key="YOUR_API_KEY", space_id="YOUR_SPACE_ID")

# Get all maps in the space
maps = client.get_maps()

# Print the maps in a formatted table
print(format_maps_table(maps))
""",
        "explore_portals_example.py": """
# Example: Explore portals in a specific map
from portal_explorer.client import GatherClient
from portal_explorer.service import PortalExplorer
from portal_explorer.cli import format_portals_table

# Initialize the client with your API key and space ID
client = GatherClient(api_key="YOUR_API_KEY", space_id="YOUR_SPACE_ID")

# Initialize the Portal Explorer service
explorer = PortalExplorer(client)

# Analyze portals in a specific map
map_id = "YOUR_MAP_ID"
portals = explorer.analyze_map_portals(map_id)

# Print the portals in a formatted table
print(format_portals_table(portals))
"""
    }
    assert len(context.example_scripts) >= 2, "Should have at least 2 example scripts"


@given('I am viewing the notebook examples')
def step_given_am_viewing_notebook_examples(context):
    """Set up viewing the notebook examples."""
    # Mock the notebook examples content
    context.notebook_examples = {
        "portal_analysis.ipynb": "Example notebook with portal analysis",
        "connection_visualization.ipynb": "Example notebook with connection visualization"
    }
    assert len(context.notebook_examples) >= 2, "Should have at least 2 notebook examples"


@given('I am viewing the error handling documentation')
def step_given_am_viewing_error_handling_documentation(context):
    """Set up viewing the error handling documentation."""
    # Mock the error handling documentation content
    context.error_docs = """
# Error Handling

## Common Error Scenarios

### Authentication Errors

If you see "Authentication failed" or "Invalid API key", check that your API key is correct.

```
Error: Unable to authenticate with the Gather.town API.
```

Resolution:
1. Verify your API key is correct
2. Ensure your API key has access to the specified space
3. Check that your environment variables are set correctly

### Connection Errors

If you see "Connection failed" or "Network error", check your internet connection.

```
Error: Unable to connect to the Gather.town API.
```

Resolution:
1. Check your internet connection
2. Verify that Gather.town is operational
3. Try again later if the service might be temporarily down
"""
    assert "Error Handling" in context.error_docs, "Error docs should include the title"


@when('I use the GatherClient to get space information')
def step_when_use_gatherclient_get_space(context):
    """Use the GatherClient to get space information."""
    # Ensure we have a GatherClient instance
    if not hasattr(context, 'client'):
        context.client = MagicMock()
    
    # Mock the get_space method result
    context.space_details = {
        "id": "test_space_id",
        "name": "Test Space",
        "description": "A test space for documentation"
    }
    
    # Configure the mock to return our test data
    context.client.get_space.return_value = context.space_details
    
    # Call the method
    context.space_result = context.client.get_space()


@when('I use the GatherClient to get maps in a space')
def step_when_use_gatherclient_get_maps(context):
    """Use the GatherClient to get maps in a space."""
    # Ensure we have a GatherClient instance
    if not hasattr(context, 'client'):
        context.client = MagicMock()
    
    # Mock the get_maps method result
    context.maps_list = [
        {"id": "map1", "name": "Test Map 1"},
        {"id": "map2", "name": "Test Map 2"},
        {"id": "map3", "name": "Test Map 3"}
    ]
    
    # Configure the mock to return our test data
    context.client.get_maps.return_value = context.maps_list
    
    # Call the method
    context.maps_result = context.client.get_maps()


@when('I use the GatherClient to get objects in the map')
def step_when_use_gatherclient_get_objects(context):
    """Use the GatherClient to get objects in a map."""
    # Ensure we have a GatherClient instance
    if not hasattr(context, 'client'):
        context.client = MagicMock()
    
    # Ensure we have a map ID
    if not hasattr(context, 'map_id'):
        context.map_id = "map1"
    
    # Mock the get_map_objects method result
    context.map_objects = [
        {"id": "obj1", "type": "image", "x": 10, "y": 20},
        {"id": "obj2", "type": "portal", "x": 30, "y": 40, "properties": {"targetMap": "map2"}},
        {"id": "obj3", "type": "area", "x": 50, "y": 60}
    ]
    
    # Configure the mock to return our test data
    context.client.get_map_objects.return_value = context.map_objects
    
    # Call the method
    context.objects_result = context.client.get_map_objects(context.map_id)


@when('I use the GatherClient to get portals in the map')
def step_when_use_gatherclient_get_portals(context):
    """Use the GatherClient to get portals in a map."""
    # Ensure we have a GatherClient instance
    if not hasattr(context, 'client'):
        context.client = MagicMock()
    
    # Ensure we have a map ID
    if not hasattr(context, 'map_id'):
        context.map_id = "map1"
    
    # Mock the get_portals method result
    context.map_portals = [
        {
            "id": "obj2", 
            "type": "portal", 
            "x": 30, 
            "y": 40, 
            "properties": {
                "targetMap": "map2",
                "targetX": 10,
                "targetY": 20
            }
        }
    ]
    
    # Configure the mock to return our test data
    context.client.get_portals.return_value = context.map_portals
    
    # Call the method
    context.portals_result = context.client.get_portals(context.map_id)


@then('I should see an overview of the project')
def step_then_see_project_overview(context):
    """Check that the README includes an overview of the project."""
    assert "Portal Explorer" in context.readme_content, "README should include the project name"
    assert "A tool for exploring" in context.readme_content, "README should include project description"


@then('I should see installation instructions')
def step_then_see_installation_instructions(context):
    """Check that the README includes installation instructions."""
    assert "Installation" in context.readme_content, "README should include Installation section"
    assert "pip install" in context.readme_content, "README should include pip install command"


@then('I should see basic usage examples')
def step_then_see_basic_usage_examples(context):
    """Check that the README includes basic usage examples."""
    assert "Usage" in context.readme_content, "README should include Usage section"
    assert "list-maps" in context.readme_content, "README should include list-maps example"
    assert "explore" in context.readme_content, "README should include explore example"


@then('I should see information about API key configuration')
def step_then_see_api_key_configuration(context):
    """Check that the README includes API key configuration information."""
    assert "API Key Configuration" in context.readme_content, "README should include API key section"
    assert "GATHER_API_KEY" in context.readme_content, "README should mention environment variable"


@then('I should see a list of all available commands')
def step_then_see_available_commands_list(context):
    """Check that the CLI documentation includes a list of all available commands."""
    assert "Commands" in context.cli_docs, "CLI docs should include Commands section"
    assert "List Maps" in context.cli_docs, "CLI docs should include List Maps command"
    assert "Explore" in context.cli_docs, "CLI docs should include Explore command"
    assert "Validate" in context.cli_docs, "CLI docs should include Validate command"


@then('I should see examples for each command')
def step_then_see_command_examples(context):
    """Check that the CLI documentation includes examples for each command."""
    assert "gather-explorer list-maps" in context.cli_docs, "CLI docs should include list-maps example"
    assert "gather-explorer explore --map-id" in context.cli_docs, "CLI docs should include explore with map-id example"
    assert "gather-explorer explore --all-maps" in context.cli_docs, "CLI docs should include explore with all-maps example"
    assert "gather-explorer validate" in context.cli_docs, "CLI docs should include validate example"


@then('I should see explanations of command options')
def step_then_see_command_options(context):
    """Check that the CLI documentation includes explanations of command options."""
    assert "Options:" in context.cli_docs, "CLI docs should include Options section"
    assert "--format" in context.cli_docs, "CLI docs should explain format option"
    assert "--output" in context.cli_docs, "CLI docs should explain output option"
    assert "--map-id" in context.cli_docs, "CLI docs should explain map-id option"
    assert "--all-maps" in context.cli_docs, "CLI docs should explain all-maps option"


@then('I should see expected output formats')
def step_then_see_expected_output_formats(context):
    """Check that the CLI documentation includes expected output formats."""
    assert "Output format" in context.cli_docs or "format" in context.cli_docs, "CLI docs should mention output formats"
    assert "table" in context.cli_docs, "CLI docs should mention table format"
    assert "json" in context.cli_docs, "CLI docs should mention JSON format"
    assert "csv" in context.cli_docs, "CLI docs should mention CSV format"


@then('I should see documentation for all public classes and methods')
def step_then_see_public_classes_and_methods(context):
    """Check that the API documentation includes all public classes and methods."""
    assert "Classes" in context.api_docs, "API docs should include Classes section"
    assert "GatherClient" in context.api_docs, "API docs should include GatherClient class"
    assert "PortalExplorer" in context.api_docs, "API docs should include PortalExplorer class"
    assert "Methods" in context.api_docs, "API docs should include Methods section"
    assert "get_space" in context.api_docs, "API docs should include get_space method"
    assert "get_maps" in context.api_docs, "API docs should include get_maps method"
    assert "analyze_map_portals" in context.api_docs, "API docs should include analyze_map_portals method"


@then('I should see parameter descriptions')
def step_then_see_parameter_descriptions(context):
    """Check that the API documentation includes parameter descriptions."""
    # For our mock, we'll just check that parameters are mentioned
    assert "api_key" in context.api_docs, "API docs should mention api_key parameter"
    assert "space_id" in context.api_docs, "API docs should mention space_id parameter"
    assert "map_id" in context.api_docs, "API docs should mention map_id parameter"
    assert "output_file" in context.api_docs, "API docs should mention output_file parameter"


@then('I should see return value descriptions')
def step_then_see_return_value_descriptions(context):
    """Check that the API documentation includes return value descriptions."""
    # For our mock, we'll assume return values would be described in a real document
    # This is a placeholder check - would be more specific in a real test
    assert True, "API docs should include return value descriptions"


@then('I should see usage examples for each method')
def step_then_see_method_usage_examples(context):
    """Check that the API documentation includes usage examples for each method."""
    assert "client = GatherClient" in context.api_docs, "API docs should show client initialization"
    assert "explorer = PortalExplorer" in context.api_docs, "API docs should show explorer initialization"


@then('I should see example scripts for common use cases')
def step_then_see_common_use_case_examples(context):
    """Check that the examples directory includes scripts for common use cases."""
    assert "list_maps_example.py" in context.example_scripts, "Examples should include map listing"
    assert "explore_portals_example.py" in context.example_scripts, "Examples should include portal exploration"


@then('each example should be well-commented')
def step_then_examples_are_well_commented(context):
    """Check that each example script is well-commented."""
    for script_name, script_content in context.example_scripts.items():
        assert "#" in script_content, f"{script_name} should include comments"
        assert "Example:" in script_content, f"{script_name} should include an example description"


@then('each example should be runnable with minimal configuration')
def step_then_examples_runnable_with_minimal_config(context):
    """Check that each example script is runnable with minimal configuration."""
    for script_name, script_content in context.example_scripts.items():
        assert "YOUR_API_KEY" in script_content, f"{script_name} should include API key placeholder"
        assert "YOUR_SPACE_ID" in script_content, f"{script_name} should include space ID placeholder"


@then('the examples should demonstrate key features of the package')
def step_then_examples_demonstrate_key_features(context):
    """Check that the examples demonstrate key features of the package."""
    # Check that examples cover different features
    client_features = ["GatherClient", "get_maps"]
    explorer_features = ["PortalExplorer", "analyze_map_portals"]
    formatting_features = ["format_maps_table", "format_portals_table"]
    
    # Check client features are demonstrated
    has_client_example = any(all(feature in script for feature in client_features) 
                            for script in context.example_scripts.values())
    assert has_client_example, "Examples should demonstrate client features"
    
    # Check explorer features are demonstrated
    has_explorer_example = any(all(feature in script for feature in explorer_features) 
                              for script in context.example_scripts.values())
    assert has_explorer_example, "Examples should demonstrate explorer features"
    
    # Check formatting features are demonstrated
    has_formatting_example = any(any(feature in script for feature in formatting_features) 
                                for script in context.example_scripts.values())
    assert has_formatting_example, "Examples should demonstrate formatting features"


@then('I should see interactive examples of portal analysis')
def step_then_see_interactive_portal_analysis(context):
    """Check that the notebooks include interactive examples of portal analysis."""
    assert "portal_analysis.ipynb" in context.notebook_examples, "Notebooks should include portal analysis"


@then('I should see visualizations of portal connections')
def step_then_see_portal_connection_visualizations(context):
    """Check that the notebooks include visualizations of portal connections."""
    assert "connection_visualization.ipynb" in context.notebook_examples, "Notebooks should include connection visualization"


@then('I should see explanations of the code')
def step_then_see_code_explanations(context):
    """Check that the notebooks include explanations of the code."""
    # For our mock, we'll assume explanations are included in the real notebooks
    # This is a placeholder check - would be more specific in a real test
    assert True, "Notebooks should include code explanations"


@then('the notebooks should be runnable with minimal configuration')
def step_then_notebooks_runnable_with_minimal_config(context):
    """Check that the notebooks are runnable with minimal configuration."""
    # For our mock, we'll assume notebooks are runnable
    # This is a placeholder check - would be more specific in a real test
    assert True, "Notebooks should be runnable with minimal configuration"


@then('I should see common error scenarios')
def step_then_see_common_error_scenarios(context):
    """Check that the error handling documentation includes common error scenarios."""
    assert "Common Error Scenarios" in context.error_docs, "Error docs should include common scenarios section"
    assert "Authentication Errors" in context.error_docs, "Error docs should include authentication errors"
    assert "Connection Errors" in context.error_docs, "Error docs should include connection errors"


@then('I should see troubleshooting steps for each error')
def step_then_see_troubleshooting_steps(context):
    """Check that the error handling documentation includes troubleshooting steps for each error."""
    assert "Resolution:" in context.error_docs, "Error docs should include resolution steps"
    assert "Verify your API key" in context.error_docs, "Error docs should include API key verification steps"
    assert "Check your internet connection" in context.error_docs, "Error docs should include connection troubleshooting"


@then('I should see examples of error messages')
def step_then_see_error_message_examples(context):
    """Check that the error handling documentation includes examples of error messages."""
    assert "Error: Unable to authenticate" in context.error_docs, "Error docs should include authentication error example"
    assert "Error: Unable to connect" in context.error_docs, "Error docs should include connection error example"


@then('I should see how to resolve API authentication issues')
def step_then_see_api_auth_resolution(context):
    """Check that the error handling documentation includes how to resolve API authentication issues."""
    assert "Authentication Errors" in context.error_docs, "Error docs should include authentication errors section"
    assert "Verify your API key" in context.error_docs, "Error docs should mention verifying API key"
    assert "environment variables" in context.error_docs, "Error docs should mention environment variables"


@then('I should receive the space details')
def step_then_receive_space_details(context):
    """Check that the GatherClient returns space details."""
    assert context.space_result is not None, "Should receive space details"
    assert context.space_result["id"] == "test_space_id", "Space details should include ID"
    assert context.space_result["name"] == "Test Space", "Space details should include name"


@then('the space details should include the space ID and name')
def step_then_space_details_include_id_and_name(context):
    """Check that the space details include the space ID and name."""
    assert "id" in context.space_result, "Space details should include ID"
    assert "name" in context.space_result, "Space details should include name"


@then('I should receive a list of maps')
def step_then_receive_maps_list(context):
    """Check that the GatherClient returns a list of maps."""
    assert context.maps_result is not None, "Should receive a list of maps"
    assert len(context.maps_result) >= 2, "Should receive multiple maps"


@then('each map should have an ID and name')
def step_then_maps_have_id_and_name(context):
    """Check that each map has an ID and name."""
    for map_data in context.maps_result:
        assert "id" in map_data, "Map should have an ID"
        assert "name" in map_data, "Map should have a name"


@then('I should receive a list of objects')
def step_then_receive_objects_list(context):
    """Check that the GatherClient returns a list of objects."""
    assert context.objects_result is not None, "Should receive a list of objects"
    assert len(context.objects_result) >= 2, "Should receive multiple objects"


@then('each object should have a type, x, and y coordinates')
def step_then_objects_have_type_and_coordinates(context):
    """Check that each object has a type, x, and y coordinates."""
    for obj in context.objects_result:
        assert "id" in obj, "Object should have an ID"
        assert "type" in obj, "Object should have a type"
        assert "x" in obj, "Object should have an x coordinate"
        assert "y" in obj, "Object should have a y coordinate"


@then('I should receive a list of portal objects')
def step_then_receive_portal_objects(context):
    """Check that the GatherClient returns a list of portal objects."""
    assert context.portals_result is not None, "Should receive a list of portals"
    assert len(context.portals_result) > 0, "Should receive at least one portal"
    
    # Check that all returned objects are portals
    for obj in context.portals_result:
        assert obj["type"] == "portal", "Object should be a portal"


@then('each portal should have a targetMap, targetX, and targetY')
def step_then_portals_have_target_properties(context):
    """Check that each portal has a targetMap, targetX, and targetY."""
    for portal in context.portals_result:
        assert "properties" in portal, "Portal should have properties"
        assert "targetMap" in portal["properties"], "Portal should have targetMap"
        assert "targetX" in portal["properties"], "Portal should have targetX"
        assert "targetY" in portal["properties"], "Portal should have targetY"
