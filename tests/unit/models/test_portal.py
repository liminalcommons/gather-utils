"""
Unit tests for the Portal model.
"""
import pytest
from pydantic import ValidationError

# Import the model we want to test
from gather_manager.models.portal import Portal


class TestPortalModel:
    """Test suite for the Portal model."""

    def test_portal_creation(self, sample_portal_data):
        """Test that a Portal can be created from valid data."""
        # Create a Portal from the sample data
        portal = Portal.model_validate(sample_portal_data)
        
        # Verify the Portal has the expected attributes
        assert portal.id == "portal1"
        assert portal.type == 4
        assert portal.x == 5
        assert portal.y == 5
        assert portal.properties.target_map == "map2"
        assert portal.properties.target_x == 10
        assert portal.properties.target_y == 20
        assert portal.properties.normal is True

    def test_portal_validation_error(self):
        """Test that validation errors are raised for invalid data."""
        # Missing required fields
        invalid_data = {
            "id": "portal1",
            "type": 4,
            # Missing x and y coordinates
            "properties": {
                "targetMap": "map2",
                "targetX": 10,
                "targetY": 20
            }
        }
        
        # Verify that a validation error is raised
        with pytest.raises(ValidationError):
            Portal.model_validate(invalid_data)

    def test_portal_is_valid(self, sample_portal_data):
        """Test the is_valid method of the Portal model."""
        portal = Portal.model_validate(sample_portal_data)
        
        # A portal with all required properties should be valid
        assert portal.is_valid() is True
        
        # Modify the portal to make it invalid
        portal.properties.target_map = None
        assert portal.is_valid() is False

    def test_portal_get_destination(self, sample_portal_data):
        """Test the get_destination method of the Portal model."""
        portal = Portal.model_validate(sample_portal_data)
        
        # Get the destination of the portal
        destination = portal.get_destination()
        
        # Verify the destination has the expected values
        assert destination["map_id"] == "map2"
        assert destination["x"] == 10
        assert destination["y"] == 20

    def test_portal_to_dict(self, sample_portal_data):
        """Test the to_dict method of the Portal model."""
        portal = Portal.model_validate(sample_portal_data)
        
        # Convert the portal to a dictionary
        portal_dict = portal.to_dict()
        
        # Verify the dictionary has the expected keys and values
        assert portal_dict["id"] == "portal1"
        assert portal_dict["type"] == 4
        assert portal_dict["x"] == 5
        assert portal_dict["y"] == 5
        assert portal_dict["target_map"] == "map2"
        assert portal_dict["target_x"] == 10
        assert portal_dict["target_y"] == 20
        assert portal_dict["is_valid"] is True 