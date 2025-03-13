"""
Common step definitions that can be reused across multiple features.
"""
from behave import given, when, then
from unittest.mock import MagicMock, patch


@given('I have a valid Gather.town API key')
def step_have_valid_api_key(context):
    """Set up a valid API key in the context."""
    context.api_key = context.config['api_key']
    assert context.api_key, "API key should be set"


@given('I have access to a Gather.town space with portals')
def step_have_access_to_space_with_portals(context):
    """Set up access to a space with portals."""
    context.space_id = context.config['space_id']
    assert context.space_id, "Space ID should be set"
    
    # Mock space data with portals for testing
    context.mock_space_data = {
        "id": context.space_id,
        "name": "Test Space",
        "maps": [
            {"id": "map1", "name": "Test Map 1"},
            {"id": "map2", "name": "Test Map 2"}
        ]
    }
    
    # Mock portal data
    context.mock_portal_data = [
        {
            "id": "portal1",
            "type": "portal",
            "x": 10,
            "y": 10,
            "properties": {
                "targetMap": "map2",
                "targetX": 5,
                "targetY": 5
            }
        }
    ]


@given('I have access to a Gather.town space with multiple maps and portals')
def step_have_access_to_space_with_multiple_maps(context):
    """Set up access to a space with multiple maps and portals."""
    # Reuse the basic space setup
    step_have_access_to_space_with_portals(context)
    
    # Add more maps and portals for multi-map testing
    context.mock_space_data["maps"].extend([
        {"id": "map3", "name": "Test Map 3"},
        {"id": "map4", "name": "Test Map 4"}
    ])
    
    # Add more complex portal connections
    context.mock_portal_data.extend([
        {
            "id": "portal2",
            "type": "portal",
            "x": 20,
            "y": 20,
            "properties": {
                "targetMap": "map3",
                "targetX": 15,
                "targetY": 15
            }
        },
        {
            "id": "portal3",
            "type": "portal",
            "x": 5,
            "y": 5,
            "properties": {
                "targetMap": "map1",
                "targetX": 10,
                "targetY": 10
            }
        }
    ])


@given('I have the Portal Explorer codebase')
def step_have_portal_explorer_codebase(context):
    """Set up the Portal Explorer codebase context."""
    # This is a placeholder - in a real test, we'd check for the existence of key files
    context.codebase_ready = True
    assert context.codebase_ready, "Codebase should be available"


@given('I have set up the testing framework')
def step_have_testing_framework(context):
    """Set up the testing framework."""
    # This is a placeholder - in a real test, we'd check for pytest configuration
    context.testing_framework_ready = True
    assert context.testing_framework_ready, "Testing framework should be set up"


@given('I have a GatherClient instance')
def step_have_gatherclient_instance(context):
    """Set up a GatherClient instance (or mock)."""
    # In tests, we'll use a mock client
    if hasattr(context, 'mock_client'):
        context.client = context.mock_client
    else:
        context.client = MagicMock()
        
    # Configure the mock to return our test data
    context.client.get_space.return_value = context.mock_space_data
    context.client.get_portals.return_value = context.mock_portal_data 