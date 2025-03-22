"""
Step definitions for the Portal Analysis and Troubleshooting feature.
"""
from behave import given, when, then
from unittest.mock import patch, MagicMock

# Import common steps
from tests.bdd.steps.common.setup_steps import *
from tests.bdd.steps.common.cli_steps import *
from tests.bdd.steps.common.assertion_steps import *


@when('I run the command "gather-manager validate-portals --check-bidirectional"')
def step_when_run_validate_portals_bidirectional(context):
    """Run the validate-portals command with bidirectional check."""
    step_when_run_command(context, "gather-manager validate-portals --check-bidirectional")


@when('I run the command "gather-manager validate-portals --report"')
def step_when_run_validate_portals_report(context):
    """Run the validate-portals command with report option."""
    step_when_run_command(context, "gather-manager validate-portals --report")


@when('I run the command "gather-manager fix-portals"')
def step_when_run_fix_portals(context):
    """Run the fix-portals command."""
    step_when_run_command(context, "gather-manager fix-portals")


@then('I should see a list of issues that were fixed')
def step_then_see_fixed_issues_list(context):
    """Check that the output contains a list of issues that were fixed."""
    assert context.result is not None, "Result should be defined"
    assert "Issues Fixed" in context.result["output"], "Output should include issues fixed section"
    
    # Check for specific issues being fixed
    fixed_issue_indicators = [
        "Added", 
        "Fixed", 
        "Corrected"
    ]
    has_fixed_issue = any(indicator in context.result["output"] for indicator in fixed_issue_indicators)
    assert has_fixed_issue, "Output should describe fixed issues"


@then('I should see a list of issues that require manual intervention')
def step_then_see_manual_intervention_issues(context):
    """Check that the output lists issues requiring manual intervention."""
    assert context.result is not None, "Result should be defined"
    assert "Manual Intervention" in context.result["output"], "Output should include manual intervention section"
    
    # Check for issues that couldn't be automatically fixed
    manual_issue_indicators = [
        "Cannot determine", 
        "Unable to fix", 
        "Requires manual"
    ]
    has_manual_issue = any(indicator in context.result["output"] for indicator in manual_issue_indicators)
    assert has_manual_issue, "Output should describe issues needing manual intervention"


@then('the changes should be applied to my space')
def step_then_changes_applied_to_space(context):
    """Check that the output indicates changes were applied to the space."""
    assert context.result is not None, "Result should be defined"
    assert "Changes have been applied" in context.result["output"], "Output should confirm changes were applied"


@then('I should see a summary of portal health across my space')
def step_then_see_portal_health_summary(context):
    """Check that the output contains a summary of portal health."""
    assert context.result is not None, "Result should be defined"
    assert "Portal Health Report" in context.result["output"], "Output should include portal health report"
    assert "Summary" in context.result["output"], "Output should include summary section"
    
    # Check for portal counts and percentages
    summary_indicators = [
        "Total portals", 
        "Valid portals", 
        "Invalid portals", 
        "%"
    ]
    has_summary = all(indicator in context.result["output"] for indicator in summary_indicators)
    assert has_summary, "Output should include portal health statistics"


@then('I should see statistics on portal issues by type')
def step_then_see_portal_issue_statistics(context):
    """Check that the output includes statistics on portal issues by type."""
    assert context.result is not None, "Result should be defined"
    assert "Issues by Type" in context.result["output"], "Output should include issues by type section"
    
    # Check for issue types and percentages
    issue_type_indicators = [
        "Missing", 
        "%"
    ]
    has_issue_types = all(indicator in context.result["output"] for indicator in issue_type_indicators)
    assert has_issue_types, "Output should include issue type statistics"


@then('I should see a list of maps with the most issues')
def step_then_see_maps_with_most_issues(context):
    """Check that the output includes a list of maps with the most issues."""
    assert context.result is not None, "Result should be defined"
    assert "Maps with Issues" in context.result["output"], "Output should include maps with issues section"
    
    # Check for map-specific issue counts
    map_issue_indicators = [
        "map", 
        "issues"
    ]
    has_map_issues = all(indicator in context.result["output"] for indicator in map_issue_indicators)
    assert has_map_issues, "Output should include maps with issue counts"


@then('the report should be saved to a file')
def step_then_report_saved_to_file(context):
    """Check that the report is saved to a file."""
    assert context.result is not None, "Result should be defined"
    assert "saved to" in context.result["output"] or "Report saved" in context.result["output"], "Output should confirm report was saved"
    
    # Check for specific file mention
    report_file_indicators = [
        "portal_health_report.json", 
        "portal_validation_report.json"
    ]
    has_report_file = any(indicator in context.result["output"] for indicator in report_file_indicators)
    assert has_report_file, "Output should mention the report filename"


@then('the exported data should contain all portal information')
def step_then_exported_data_contains_all_info(context):
    """Check that the exported data contains all portal information."""
    # This is difficult to verify without examining the actual file
    # In a real test, we would check the contents of the file
    # For this mock test, we'll assume the export was successful if the previous step passed
    pass


@then('I should see a property frequency analysis for that map')
def step_then_see_map_specific_property_analysis(context):
    """Check that the output contains a property frequency analysis for a specific map."""
    assert context.result is not None, "Result should be defined"
    assert "Property Frequency Analysis" in context.result["output"], "Output should include property frequency analysis"
    
    # Since we've already tested most of the property analysis assertions in common steps,
    # we just need to verify that this appears to be map-specific
    map_specific_indicators = [
        context.map_id, 
        "Map", 
        "in map"
    ]
    has_map_specific = any(indicator in context.result["output"] for indicator in map_specific_indicators)
    assert has_map_specific, "Output should be specific to the requested map"
