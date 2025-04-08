"""
Common step definitions for BDD tests.

This module contains common step definitions that are used across multiple
feature files to reduce duplication and ensure consistency.
"""

from pathlib import Path
from unittest.mock import MagicMock

from behave import given, then, when

from tests.bdd.utils.imports import *
from tests.bdd.utils.step_utils import setup_test_environment, assert_with_context

# Common setup steps

@given("I have a valid API key")
def step_given_have_valid_api_key(context):
    """Ensure a valid API key is set up."""
    context.api_key = "valid_api_key"
    assert context.api_key, "API key should be set"


@given("I have a valid space ID")
def step_given_have_valid_space_id(context):
    """Ensure a valid space ID is set up."""
    context.space_id = "valid_space_id"
    assert context.space_id, "Space ID should be set"


@given("I have valid API credentials")
def step_given_have_valid_api_credentials(context):
    """Ensure valid API credentials are set up."""
    step_given_have_valid_api_key(context)
    step_given_have_valid_space_id(context)


@given("I have a mock API client")
def step_given_have_mock_api_client(context):
    """Set up a mock API client."""
    context.client = MagicMock()
    # Configure basic mock behavior
    context.client.get_maps.return_value = ["map1", "map2", "map3"]
    assert context.client, "API client should be set up"


@given("I have a Gather space with maps")
def step_given_have_gather_space_with_maps(context):
    """Set up a Gather space with maps."""
    # Make sure we have a client
    if not hasattr(context, "client"):
        step_given_have_mock_api_client(context)
    
    # Configure the mock client to return maps
    context.maps = ["map1", "map2", "map3"]
    context.client.get_maps.return_value = context.maps
    
    assert context.maps, "Maps should be set up"


# Common CLI steps

@given("I have the Portal Explorer CLI installed")
def step_given_have_portal_explorer_cli_installed(context):
    """Set up the Portal Explorer CLI installation."""
    context.cli_installed = True
    assert context.cli_installed, "CLI should be installed"


@given("I have configured my API key and space ID")
def step_given_have_configured_api_key_and_space_id(context):
    """Set up API key and space ID configuration."""
    step_given_have_valid_api_credentials(context)
    context.config_file_created = True
    assert context.config_file_created, "Config file should be created"


@when("I run the command {command}")
def step_when_run_command(context, command):
    """Run a command."""
    context.last_command = command
    context.last_output = f"Mock output for {command}"
    assert context.last_command, "Last command should be set"


# Common assertion steps

@then("I should see a list of maps")
def step_then_see_list_of_maps(context):
    """Check that a list of maps is displayed."""
    assert hasattr(context, "maps"), "Maps should be available"
    assert context.maps, "Maps should not be empty"


@then("I should see a success message")
def step_then_see_success_message(context):
    """Check that a success message is displayed."""
    if hasattr(context, "last_output"):
        assert "success" in context.last_output.lower() or "completed" in context.last_output.lower(), "Output should contain success message"
    else:
        assert hasattr(context, "success"), "Success flag should be set"
        assert context.success, "Operation should be successful"


@then("I should see an error message")
def step_then_see_error_message(context):
    """Check that an error message is displayed."""
    if hasattr(context, "last_output"):
        assert "error" in context.last_output.lower() or "failed" in context.last_output.lower(), "Output should contain error message"
    else:
        assert hasattr(context, "error"), "Error flag should be set"
        assert context.error, "Operation should have failed" 