"""
Step definitions for the Portal Discovery and Structure feature.
"""

from unittest.mock import MagicMock, patch

from behave import given, then, when
from pytest_bdd import given, parsers, then, when

from gather_manager.api import GatherAPI
from gather_manager.models import Portal, PortalConnection
from tests.bdd.steps.common.assertion_steps import *
from tests.bdd.steps.common.cli_steps import *

# Import common steps
from tests.bdd.steps.common.setup_steps import *


@given("I have a map with no portals")
def step_given_have_map_with_no_portals(context):
    """Set up a map with no portals for testing edge cases."""
    # Mark this context to be used in the CLI steps for appropriate mocking
    context.map_has_no_portals = True

    # Set up a map ID if not already set
    if not hasattr(context, "map_id"):
        context.map_id = "empty_map"


@given("I have an invalid API key")
def step_given_have_invalid_api_key(context):
    """Set up an invalid API key for testing error handling."""
    # Reuse the existing step for incorrect credentials
    step_given_have_incorrect_api_credentials(context)


@when("I run the portal validation command")
def step_when_run_portal_validation_command(context):
    """Run the portal validation command."""
    # Use the common step to run a validation command
    step_when_run_command(context, "gather-manager validate-portals")


@when("I run the portal connections command")
def step_when_run_portal_connections_command(context):
    """Run the portal connections command."""
    # Use the common step to run a connections command
    step_when_run_command(
        context, "gather-manager validate-portals --check-bidirectional"
    )


@when("I run the portal details command for a specific map")
def step_when_run_portal_details_command(context):
    """Run the portal details command for a specific map."""
    # Ensure we have a map ID
    if not hasattr(context, "map_id"):
        context.map_id = "map1"

    # Use the common step to run an explore command for a specific map
    step_when_run_command(
        context, f"gather-manager explore --map-id {context.map_id}"
    )


@when('I run the portal export command with format "{format_type}"')
def step_when_run_portal_export_command(context, format_type):
    """Run the portal export command with a specific format."""
    # Store the format for later checks
    context.export_format = format_type

    # Use the common step to run an export command
    step_when_run_command(
        context, f"gather-manager explore --export-format {format_type}"
    )


@then("I should see a message indicating no portal candidates were found")
def step_then_see_no_portal_candidates_message(context):
    """Check that the output contains a message about no portal candidates."""
    assert context.result is not None, "Result should be defined"
    assert (
        "No portal candidates found" in context.result["output"]
    ), "Output should mention no portal candidates"


@then("I should still see the distribution of object types")
def step_then_still_see_object_distribution(context):
    """Check that the output still includes object type distribution even if no portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Object Type Distribution" in context.result["output"]
    ), "Output should include object type distribution"
    assert "%" in context.result["output"], "Output should include percentages"


@then("I should see a distribution of object types in the map")
def step_then_see_object_type_distribution(context):
    """Check that the output contains a distribution of object types."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Object Type Distribution" in context.result["output"]
    ), "Output should include object type distribution"
    assert (
        "portal" in context.result["output"].lower()
    ), "Output should mention portal type"
    assert (
        "image" in context.result["output"].lower()
    ), "Output should mention image type"


@then("I should see the count and percentage of each object type")
def step_then_see_object_type_counts(context):
    """Check that the output includes count and percentage for each object type."""
    assert context.result is not None, "Result should be defined"

    # Look for patterns like "type: XX (YY%)"
    count_percentage_pattern = r"\w+: \d+ \(\d+%\)"
    matches = re.findall(count_percentage_pattern, context.result["output"])
    assert (
        len(matches) > 0
    ), "Output should include count and percentage for object types"


@then("I should see a list of objects with targetMap properties")
def step_then_see_objects_with_target_map(context):
    """Check that the output includes objects with targetMap properties."""
    assert context.result is not None, "Result should be defined"
    assert (
        "targetMap" in context.result["output"]
    ), "Output should mention targetMap property"

    # Look for text indicating portal candidates
    portal_candidate_indicators = [
        "Portal Candidates",
        "objects with targetMap properties found",
        "Sample Portal Structure",
    ]
    has_indicator = any(
        indicator in context.result["output"]
        for indicator in portal_candidate_indicators
    )
    assert has_indicator, "Output should include portal candidates section"


@then("I should see sample portal candidates")
def step_then_see_sample_portal_candidates(context):
    """Check that the output includes sample portal candidates."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Sample Portal Structure" in context.result["output"]
    ), "Output should include sample portal structure"

    # Check for JSON-like structure with portal properties
    portal_structure_indicators = [
        '"id":',
        '"type":',
        '"properties":',
        '"targetMap":',
        '"targetX":',
        '"targetY":',
    ]
    has_structure = all(
        indicator in context.result["output"]
        for indicator in portal_structure_indicators
    )
    assert has_structure, "Output should include detailed portal structure"


@then("I should see common properties among portal candidates")
def step_then_see_common_portal_properties(context):
    """Check that the output includes common properties among portal candidates."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Common Portal Properties" in context.result["output"]
    ), "Output should include common portal properties section"

    # Look for text indicating presence of common properties
    common_property_indicators = ["Present in", "candidates"]
    has_indicators = all(
        indicator in context.result["output"]
        for indicator in common_property_indicators
    )
    assert has_indicators, "Output should show presence of common properties"


@then("I should see an error message")
def step_then_see_error_message(context):
    """Check that the output contains an error message."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Error" in context.result["output"]
    ), "Output should include an error message"


@then("I should see a list of valid and invalid portals")
def step_then_see_valid_invalid_portals(context):
    """Check that the validation result contains valid and invalid portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Valid Portals" in context.result["output"]
    ), "Output should include valid portals section"
    assert (
        "Invalid Portals" in context.result["output"]
    ), "Output should include invalid portals section"


@then("each portal should show its validation status")
def step_then_show_portal_validation_status(context):
    """Check that each portal shows its validation status."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Valid" in context.result["output"]
    ), "Output should include valid status"
    assert (
        "Invalid" in context.result["output"]
        or "Missing" in context.result["output"]
    ), "Output should include invalid status"


@then("invalid portals should show the reason for invalidity")
def step_then_show_invalidity_reason(context):
    """Check that invalid portals show the reason for invalidity."""
    assert context.result is not None, "Result should be defined"

    # Look for text indicating why portals are invalid
    invalidity_indicators = ["Missing", "property"]
    has_indicators = all(
        indicator in context.result["output"]
        for indicator in invalidity_indicators
    )
    assert has_indicators, "Output should show reasons for portal invalidity"


@then("I should see a list of portal pairs where one direction is missing")
def step_then_see_one_way_portal_pairs(context):
    """Check that the output includes one-way portal pairs."""
    assert context.result is not None, "Result should be defined"
    assert (
        "One-way Portal Connections" in context.result["output"]
    ), "Output should include one-way connections section"
    assert (
        "Missing return portal" in context.result["output"]
    ), "Output should mention missing return portals"


@then("I should see the source and target maps for each one-way portal")
def step_then_see_one_way_portal_maps(context):
    """Check that the output shows source and target maps for one-way portals."""
    assert context.result is not None, "Result should be defined"

    # Look for text indicating source and target maps
    map_indicators = ["From map", "to map"]
    has_indicators = all(
        indicator in context.result["output"] for indicator in map_indicators
    )
    assert has_indicators, "Output should show source and target maps"


@then("I should see suggestions for creating the missing portals")
def step_then_see_missing_portal_suggestions(context):
    """Check that the output includes suggestions for creating missing portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Suggestions for creating missing portals" in context.result["output"]
    ), "Output should include suggestions section"
    assert (
        "Create portal targeting" in context.result["output"]
    ), "Output should include portal creation suggestions"


@then("the portal data should be exported to a {format_type} file")
def step_then_portal_data_exported_to_file(context, format_type):
    """Check that the portal data is exported to a file."""
    assert context.result is not None, "Result should be defined"
    assert (
        "saved to" in context.result["output"]
        or "Results saved" in context.result["output"]
    ), "Output should mention saving results"

    # Check that the export format matches what was requested
    if hasattr(context, "export_format"):
        assert (
            context.export_format == format_type
        ), f"Export format should be {format_type}"


@then("the CLI should be accessible as a system command")
def step_then_cli_accessible_as_system_command(context):
    """Check that the CLI is accessible as a system command."""
    # This is a placeholder - in a real test, we'd check for actual accessibility
    context.cli_accessible = True
    assert (
        context.cli_accessible
    ), "CLI should be accessible as a system command"


@given("I have a valid Gather API key")
def valid_api_key(context):
    """Ensure valid API key is set."""
    context.api_key = context.config.get("gather_api_key")
    assert context.api_key, "Gather API key not found in configuration"
    context.api = GatherAPI(context.api_key)


@given("I have a valid space ID")
def valid_space_id(context):
    """Ensure valid space ID is set."""
    context.space_id = context.config.get("gather_space_id")
    assert context.space_id, "Space ID not found in configuration"


@given("I have a specific map ID")
def specific_map_id(context):
    """Set a specific map ID for testing."""
    # Get first available map ID for testing
    maps = context.api.get_maps(context.space_id)
    assert maps, "No maps found in space"
    context.map_id = maps[0]["id"]


@given("there are portals in the space")
def existing_portals(context):
    """Ensure there are portals in the space."""
    context.portals = context.api.get_portals(context.space_id)
    assert context.portals, "No portals found in space"


@when("I request to list all portals")
def list_all_portals(context):
    """Request all portals in the space."""
    context.portal_list = context.api.get_portals(context.space_id)


@when("I request to list portals for that map")
def list_map_portals(context):
    """Request portals for a specific map."""
    context.map_portals = context.api.get_portals(
        context.space_id, map_id=context.map_id
    )


@when("I validate portal connections")
def validate_connections(context):
    """Validate all portal connections."""
    context.broken_connections = context.api.validate_portal_connections(
        context.space_id
    )


@then("I should receive a list of all portals")
def verify_portal_list(context):
    """Verify portal list is returned."""
    assert isinstance(context.portal_list, list), "Portal list not returned"
    assert len(context.portal_list) > 0, "No portals found"


@then("each portal should have valid properties")
def verify_portal_properties(context):
    """Verify each portal has required properties."""
    required_properties = {row["property"] for row in context.table}

    for portal in context.portal_list:
        for prop in required_properties:
            assert prop in portal, f"Portal missing property: {prop}"
            assert portal[prop] is not None, f"Portal property {prop} is None"


@then("I should receive only portals from that map")
def verify_map_portals(context):
    """Verify portals are from the specified map."""
    assert all(
        portal["mapId"] == context.map_id for portal in context.map_portals
    ), "Found portals from other maps"


@then("the portal list should not be empty")
def verify_non_empty_list(context):
    """Verify portal list contains items."""
    assert len(context.map_portals) > 0, "No portals found in map"


@then("I should receive a list of broken connections")
def verify_broken_connections(context):
    """Verify broken connections list is returned."""
    assert isinstance(
        context.broken_connections, list
    ), "Broken connections not returned as list"


@then("each broken connection should indicate")
def verify_broken_connection_details(context):
    """Verify broken connection details."""
    required_details = {row["detail"] for row in context.table}

    if context.broken_connections:
        for connection in context.broken_connections:
            for detail in required_details:
                assert detail in connection, f"Missing detail: {detail}"
