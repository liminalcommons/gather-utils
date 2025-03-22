"""
Step definitions for the TDD Portal Model feature.
"""
from behave import given, when, then
from gather_manager.models.portal import Portal


@given('I have a valid portal data structure')
def step_have_valid_portal_data(context):
    """Set up a valid portal data structure."""
    context.portal_data = {
        "id": "portal1",
        "type": 4,  # Portal type
        "x": 5,
        "y": 5,
        "properties": {
            "targetMap": "map2",
            "targetX": 10,
            "targetY": 20,
            "normal": True
        }
    }


@given('I have a Portal model instance')
def step_have_portal_model_instance(context):
    """Set up a Portal model instance."""
    # Reuse the step to get valid portal data
    if not hasattr(context, 'portal_data'):
        step_have_valid_portal_data(context)
    
    # Create a Portal model instance
    context.portal = Portal.model_validate(context.portal_data)


@when('I create a Portal model instance')
def step_create_portal_model_instance(context):
    """Create a Portal model instance from the portal data."""
    context.portal = Portal.model_validate(context.portal_data)


@when('I check if the Portal is valid')
def step_check_portal_validity(context):
    """Check if the Portal is valid."""
    context.valid_result = context.portal.is_valid()
    
    # Create an invalid portal for testing
    invalid_portal_data = context.portal_data.copy()
    invalid_portal_data["properties"]["targetMap"] = None
    context.invalid_portal = Portal.model_validate(invalid_portal_data)
    context.invalid_result = context.invalid_portal.is_valid()


@when('I get the destination of the Portal')
def step_get_portal_destination(context):
    """Get the destination of the Portal."""
    context.destination = context.portal.get_destination()


@when('I convert the Portal to a dictionary')
def step_convert_portal_to_dict(context):
    """Convert the Portal to a dictionary."""
    context.portal_dict = context.portal.to_dict()


@then('the Portal model should have the correct attributes')
def step_check_portal_attributes(context):
    """Check that the Portal model has the correct attributes."""
    assert context.portal.id == "portal1"
    assert context.portal.type == 4
    assert context.portal.x == 5
    assert context.portal.y == 5
    assert context.portal.properties.target_map == "map2"
    assert context.portal.properties.target_x == 10
    assert context.portal.properties.target_y == 20
    assert context.portal.properties.normal is True


@then('the Portal model should be valid')
def step_check_portal_is_valid(context):
    """Check that the Portal model is valid."""
    assert context.portal.is_valid() is True


@then('it should return True for valid portals')
def step_check_valid_portal_result(context):
    """Check that valid portals return True."""
    assert context.valid_result is True


@then('it should return False for invalid portals')
def step_check_invalid_portal_result(context):
    """Check that invalid portals return False."""
    assert context.invalid_result is False


@then('it should return the correct destination map and coordinates')
def step_check_destination(context):
    """Check that the destination has the correct map and coordinates."""
    assert context.destination["map_id"] == "map2"
    assert context.destination["x"] == 10
    assert context.destination["y"] == 20


@then('the dictionary should contain all Portal information')
def step_check_portal_dict(context):
    """Check that the dictionary contains all Portal information."""
    assert context.portal_dict["id"] == "portal1"
    assert context.portal_dict["type"] == 4
    assert context.portal_dict["x"] == 5
    assert context.portal_dict["y"] == 5
    assert context.portal_dict["target_map"] == "map2"
    assert context.portal_dict["target_x"] == 10
    assert context.portal_dict["target_y"] == 20
    assert context.portal_dict["is_valid"] is True 