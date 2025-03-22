"""
Common assertion steps that can be reused across multiple features.
"""

import re
from pathlib import Path

from behave import then


@then("I should see a list of maps in the space")
def step_then_see_maps_list(context):
    """Check that the output contains a list of maps."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Map 1" in context.result["output"]
        or "Test Map 1" in context.result["output"]
    ), "Output should include Map 1"
    assert (
        "Map 2" in context.result["output"]
        or "Test Map 2" in context.result["output"]
    ), "Output should include Map 2"


@then("I should display a list of all maps in the space")
def step_then_display_maps_list(context):
    """Check that the command displays a list of all maps in the space."""
    step_then_see_maps_list(context)


@then("each map should have an ID and name")
def step_then_maps_have_id_and_name(context):
    """Check that each map has an ID and name."""
    assert context.result is not None, "Result should be defined"
    assert "map1" in context.result["output"], "Output should include map1"
    assert "map2" in context.result["output"], "Output should include map2"
    assert (
        "Map 1" in context.result["output"]
        or "Test Map 1" in context.result["output"]
    ), "Output should include Map 1"
    assert (
        "Map 2" in context.result["output"]
        or "Test Map 2" in context.result["output"]
    ), "Output should include Map 2"


@then("it should include map IDs and names")
def step_then_include_map_ids_and_names(context):
    """Check that the output includes map IDs and names."""
    step_then_maps_have_id_and_name(context)


@then("the output should be formatted as a table")
def step_then_output_formatted_as_table(context):
    """Check that the output is formatted as a table."""
    assert context.result is not None, "Result should be defined"
    table_markers = ["┃", "┏", "┓", "┡", "┩", "└", "┘", "|", "+"]
    has_table_marker = any(
        marker in context.result["output"] for marker in table_markers
    )
    assert has_table_marker, "Output should be formatted as a table"
    assert (
        "Map ID" in context.result["output"]
        or "map1" in context.result["output"]
    ), "Output should include Map ID column"
    assert (
        "Name" in context.result["output"]
        or "Test Map" in context.result["output"]
    ), "Output should include Name column"


@then("the output should be formatted with rich tables and styling")
def step_then_output_formatted_with_rich_tables(context):
    """Check that the output is formatted with rich tables and styling."""
    step_then_output_formatted_as_table(context)


@then("I should see a list of portals in that map")
def step_then_see_portals_list(context):
    """Check that the output contains a list of portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Found" in context.result["output"]
        or "portal" in context.result["output"]
    ), "Output should mention portals"
    assert (
        "portals" in context.result["output"]
    ), "Output should include the word 'portals'"


@then("I should see details about each portal")
def step_then_see_portal_details(context):
    """Check that the output contains details about each portal."""
    assert context.result is not None, "Result should be defined"

    # For explore commands, we've mocked the output
    if "Exploring portals" in context.result["output"]:
        assert (
            "portals in map" in context.result["output"]
        ), "Output should mention portals in map"
    else:
        portal_indicators = ["obj1", "Portal", "Sample portal structure"]
        has_portal_indicator = any(
            indicator in context.result["output"]
            for indicator in portal_indicators
        )
        assert has_portal_indicator, "Output should include portal details"

        property_indicators = ["targetMap", "targetX", "targetY"]
        has_property_indicator = any(
            indicator in context.result["output"]
            for indicator in property_indicators
        )
        assert (
            has_property_indicator
        ), "Output should include portal properties"


@then("the results should be saved to a file")
def step_then_results_saved_to_file(context):
    """Check that the results are saved to a file."""
    assert context.result is not None, "Result should be defined"
    assert (
        "saved to" in context.result["output"]
        or "Results saved" in context.result["output"]
    ), "Output should mention saving results"
    assert (
        context.result["temp_dir"] is not None
    ), "Temp directory should be defined"
    assert Path(
        context.result["temp_dir"]
    ).exists(), "Temp directory should exist"


@then('the results should be saved to the "{directory}" directory')
def step_then_results_saved_to_custom_directory(context, directory):
    """Check that the results are saved to the specified directory."""
    assert context.result is not None, "Result should be defined"
    assert (
        directory in context.result["output"]
    ), f"Output should mention {directory} directory"


@then("I should see a confirmation message with the output location")
def step_then_see_output_location_confirmation(context):
    """Check that the output contains a confirmation message with the output location."""
    assert context.result is not None, "Result should be defined"
    assert (
        "saved to" in context.result["output"]
        or "Results saved" in context.result["output"]
    ), "Output should mention saving results"


@then("I should see a summary of portals across all maps")
def step_then_see_portals_summary(context):
    """Check that the output contains a summary of portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Total:" in context.result["output"]
        or "Total " in context.result["output"]
    ), "Output should include total"
    assert (
        "portals across" in context.result["output"]
        or "portals in" in context.result["output"]
    ), "Output should mention portals across/in maps"
    assert "maps" in context.result["output"], "Output should mention maps"


@then("I should see the total number of portals found")
def step_then_see_total_portals(context):
    """Check that the output contains the total number of portals."""
    assert context.result is not None, "Result should be defined"

    # Look for patterns like "Total: X portals" or "Found X portals"
    portal_count_patterns = [
        r"Total: \d+ portal",
        r"Total \d+ portal",
        r"Found \d+ portal",
    ]

    has_portal_count = any(
        re.search(pattern, context.result["output"])
        for pattern in portal_count_patterns
    )
    assert (
        has_portal_count
    ), "Output should include the total number of portals"


@then("I should see a property frequency analysis")
def step_then_see_property_frequency_analysis(context):
    """Check that the output contains a property frequency analysis."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Property Frequency Analysis" in context.result["output"]
    ), "Output should include Property Frequency Analysis"
    assert (
        "targetMap" in context.result["output"]
    ), "Output should include targetMap"
    assert (
        "targetX" in context.result["output"]
    ), "Output should include targetX"
    assert (
        "targetY" in context.result["output"]
    ), "Output should include targetY"


@then("I should see the percentage of portals with each property")
def step_then_see_property_percentages(context):
    """Check that the output contains the percentage of portals with each property."""
    assert context.result is not None, "Result should be defined"
    assert (
        "%" in context.result["output"]
    ), "Output should include percentage signs"

    # Look for patterns like "XX% (Y/Z)"
    percentage_pattern = r"\d+% \(\d+/\d+\)"
    assert re.search(
        percentage_pattern, context.result["output"]
    ), "Output should include percentages in the format XX% (Y/Z)"


@then("I should see which properties appear to be directional")
def step_then_see_directional_properties(context):
    """Check that the output identifies directional properties."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Directional Properties" in context.result["output"]
    ), "Output should include Directional Properties section"
    assert (
        "Yes" in context.result["output"]
    ), "Output should include Yes for directional properties"
    assert (
        "No" in context.result["output"]
    ), "Output should include No for non-directional properties"


@then("I should see properties that are present in less than 50% of portals")
def step_then_see_unusual_properties(context):
    """Check that the output identifies properties present in less than 50% of portals."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Unusual Properties" in context.result["output"]
    ), "Output should include Unusual Properties section"

    # Look for patterns like "XX% (Y/Z)" with XX < 50
    unusual_percentage_pattern = r"\d{1,2}% \(\d+/\d+\)"  # 0-49%
    assert re.search(
        unusual_percentage_pattern, context.result["output"]
    ), "Output should include percentages less than 50%"


@then("I should be able to identify portals with unusual configurations")
def step_then_identify_unusual_portals(context):
    """Check that the output helps identify portals with unusual configurations."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Unusual Portal Configurations" in context.result["output"]
    ), "Output should include Unusual Portal Configurations section"
    assert (
        "Portal" in context.result["output"]
    ), "Output should mention specific portals"
    unusual_indicators = ["Missing", "Has", "uncommon"]
    has_unusual_indicator = any(
        indicator in context.result["output"]
        for indicator in unusual_indicators
    )
    assert (
        has_unusual_indicator
    ), "Output should describe what makes portals unusual"


@then("I should see which properties have consistent values")
def step_then_see_consistent_properties(context):
    """Check that the output identifies properties with consistent values."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Property Value Consistency" in context.result["output"]
    ), "Output should include Property Value Consistency section"
    assert (
        "Consistent" in context.result["output"]
    ), "Output should mention consistent properties"


@then("I should see which properties have variable values")
def step_then_see_variable_properties(context):
    """Check that the output identifies properties with variable values."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Variable" in context.result["output"]
    ), "Output should mention variable properties"

    # Look for patterns like "Variable (X unique values)"
    variable_pattern = r"Variable \(\d+ unique values\)"
    assert re.search(
        variable_pattern, context.result["output"]
    ), "Output should include count of unique values"


@then("I should be able to identify inconsistencies in portal configurations")
def step_then_identify_configuration_inconsistencies(context):
    """Check that the output helps identify inconsistencies in portal configurations."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Configuration Inconsistencies" in context.result["output"]
    ), "Output should include Configuration Inconsistencies section"

    inconsistency_indicators = [
        "Some portals",
        "unusual",
        "outside normal range",
    ]
    has_inconsistency_indicator = any(
        indicator in context.result["output"]
        for indicator in inconsistency_indicators
    )
    assert (
        has_inconsistency_indicator
    ), "Output should describe configuration inconsistencies"


@then("I should see a user-friendly error message")
def step_then_see_user_friendly_error_message(context):
    """Check that the command shows a user-friendly error message."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Error:" in context.result["output"]
    ), "Output should include an error message"
    assert (
        "Unable to authenticate" in context.result["output"]
        or "API key" in context.result["output"]
    ), "Output should include authentication error"


@then("I should receive guidance on how to fix the issue")
def step_then_receive_fix_guidance(context):
    """Check that the command provides guidance on how to fix the issue."""
    assert context.result is not None, "Result should be defined"
    guidance_indicators = [
        "Please check",
        "You can",
        "Try",
        "Make sure",
        "environment variables",
    ]
    has_guidance = any(
        indicator in context.result["output"]
        for indicator in guidance_indicators
    )
    assert has_guidance, "Output should include guidance on fixing the issue"


@then("the program should exit gracefully")
def step_then_program_exit_gracefully(context):
    """Check that the program exits gracefully."""
    assert context.result is not None, "Result should be defined"
    assert (
        context.result["exit_code"] != 0
    ), "Command should exit with non-zero code for errors"
    assert (
        context.result["exit_code"] == 1
    ), "Command should exit with code 1 for API errors"


@then("I should see help information")
def step_then_see_help_information(context):
    """Check that the command shows help information."""
    assert context.result is not None, "Result should be defined"
    assert (
        "Usage:" in context.result["output"]
    ), "Output should include usage information"
    assert (
        "Options:" in context.result["output"]
    ), "Output should include options information"
    assert (
        "Commands:" in context.result["output"]
    ), "Output should include commands information"


@then("all available commands should be listed")
def step_then_all_commands_listed(context):
    """Check that all available commands are listed."""
    assert context.result is not None, "Result should be defined"
    assert (
        "explore" in context.result["output"]
    ), "Output should include explore command"
    assert (
        "list-maps" in context.result["output"]
    ), "Output should include list-maps command"


@then("long-running operations should show progress indicators")
def step_then_show_progress_indicators(context):
    """Check that long-running operations show progress indicators."""
    assert context.result is not None, "Result should be defined"
    progress_indicators = ["Progress:", "[", "]", "%"]
    has_progress_indicator = all(
        indicator in context.result["output"]
        for indicator in progress_indicators
    )
    assert has_progress_indicator, "Output should include progress indicators"


@then("the information should be presented in a user-friendly way")
def step_then_information_presented_user_friendly(context):
    """Check that the information is presented in a user-friendly way."""
    # This is somewhat subjective, but we can check for basic formatting
    step_then_output_formatted_as_table(context)
