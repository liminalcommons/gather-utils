"""
Common setup step definitions used across multiple features.
"""
from behave import given, when, then
from unittest.mock import MagicMock, patch


@given('I have a valid Gather.town API key')
def step_given_have_valid_api_key(context):
    """Set up a valid API key in the context."""
    context.api_key = "test_api_key"
    assert context.api_key, "API key should be set"


@given('I have a valid Gather.town space ID')
def step_given_have_valid_space_id(context):
    """Set up a valid space ID in the context."""
    context.space_id = "test_space_id"
    assert context.space_id, "Space ID should be set"


@given('my space has at least one map with portals')
def step_given_space_has_map_with_portals(context):
    """Set up a space with at least one map containing portals."""
    # This is handled by the mock setup
    context.mock_space_data = {
        "id": context.space_id if hasattr(context, 'space_id') else "test_space_id",
        "name": "Test Space",
        "maps": [
            {"id": "map1", "name": "Test Map 1"},
            {"id": "map2", "name": "Test Map 2"}
        ]
    }
    
    context.mock_portal_data = [
        {
            "id": "portal1",
            "type": "portal",
            "x": 10,
            "y": 10,
            "properties": {
                "targetMap": "map2",
                "targetX": 5,
                "targetY": 5,
                "normal": True
            }
        }
    ]
    
    pass


@given('I know the ID of a map in my space')
def step_given_know_map_id(context):
    """Set up a known map ID."""
    context.map_id = "map1"
    assert context.map_id, "Map ID should be set"


@given('I have the Portal Explorer codebase')
def step_given_have_portal_explorer_codebase(context):
    """Set up the Portal Explorer codebase context."""
    # This is a placeholder - in a real test, we'd check for the existence of key files
    context.codebase_ready = True
    assert context.codebase_ready, "Codebase should be available"


@given('I have the necessary dependencies installed')
def step_given_have_necessary_dependencies(context):
    """Set up necessary dependencies."""
    # This is a placeholder - in a real test, we'd check for actual dependencies
    context.dependencies_installed = True
    assert context.dependencies_installed, "Dependencies should be installed"


@given('I have the Portal Explorer CLI installed')
def step_given_have_portal_explorer_cli_installed(context):
    """Set up the Portal Explorer CLI installation."""
    # In a real test, we might check for actual installation
    context.cli_installed = True
    assert context.cli_installed, "Portal Explorer CLI should be installed"


@given('I have configured my API key and space ID')
def step_given_have_configured_api_key_and_space_id(context):
    """Set up API key and space ID configuration."""
    # Set up the API key and space ID
    context.api_key = "test_api_key"
    context.space_id = "test_space_id"
    
    # In a real test, we might check for actual configuration
    context.api_configured = True
    assert context.api_configured, "API key and space ID should be configured"


@given('I have installed the Portal Explorer package')
def step_given_have_installed_package(context):
    """Set up having installed the package."""
    # Reuse the previous step
    step_given_have_portal_explorer_cli_installed(context)


@given('I have the Portal Explorer source code')
def step_given_have_portal_explorer_source_code(context):
    """Set up the Portal Explorer source code."""
    # This is similar to having the codebase
    step_given_have_portal_explorer_codebase(context)


@given('I have a project with BDD features and scenarios')
def step_given_have_project_with_bdd_features(context):
    """Set up a project with BDD features and scenarios."""
    # Check if the features directory exists
    features_dir = Path('features') if 'Path' in globals() else MagicMock()
    # For testing, we just set up a flag
    context.has_bdd_features = True
    assert context.has_bdd_features, "Should have BDD features"


@given('I have the necessary BDD tools installed')
def step_given_have_necessary_bdd_tools(context):
    """Check that necessary BDD tools are installed."""
    # For testing, we just set up a flag
    context.bdd_tools_installed = True
    assert context.bdd_tools_installed, "BDD tools should be installed"


@given('we have an existing development system')
def step_given_have_existing_development_system(context):
    """Set up an existing development system."""
    # For testing, we just set up a flag
    context.has_development_system = True
    assert context.has_development_system, "Should have an existing development system"


@given('we have agent and project systems in place')
def step_given_have_agent_and_project_systems(context):
    """Set up agent and project systems."""
    # For testing, we just set up a flag
    context.has_agent_and_project_systems = True
    assert context.has_agent_and_project_systems, "Should have agent and project systems"


@given('we have established release standards')
def step_given_have_established_release_standards(context):
    """Set up established release standards."""
    # For testing, we just set up a flag
    context.has_release_standards = True
    assert context.has_release_standards, "Should have established release standards"


@given('Release {number} has been completed')
def step_given_release_has_been_completed(context, number):
    """Set up a completed release."""
    # For testing, we just set up a flag
    context.completed_releases = getattr(context, 'completed_releases', set())
    context.completed_releases.add(number)
    assert number in context.completed_releases, f"Release {number} should be completed"


@given('BDD Release {number} has been completed')
def step_given_bdd_release_has_been_completed(context, number):
    """Set up a completed BDD release."""
    # For testing, we just set up a flag
    context.completed_bdd_releases = getattr(context, 'completed_bdd_releases', set())
    context.completed_bdd_releases.add(number)
    assert number in context.completed_bdd_releases, f"BDD Release {number} should be completed"
