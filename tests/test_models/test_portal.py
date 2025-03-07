"""Tests for portal models and functionality."""

import pytest
from pydantic import ValidationError

from gather_manager.models.space import Object, Portal


class TestPortalModel:
    """Tests for the Portal model."""
    
    def test_portal_creation(self):
        """Test creating a portal with required fields."""
        portal = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            targetY=15
        )
        
        assert portal.type == "portal"
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 5
        assert portal.targetY == 15
        assert portal.width == 1  # Default value
        assert portal.height == 1  # Default value
    
    def test_portal_validation(self):
        """Test that portal validation requires target information."""
        # Should raise validation error when missing required target fields
        with pytest.raises(ValidationError):
            Portal(
                type="portal",
                x=10,
                y=20,
                # Missing targetMap, targetX, targetY
            )
    
    def test_portal_from_object(self):
        """Test converting a generic Object to a Portal."""
        obj = Object(
            id="test-portal",
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            targetY=15
        )
        
        portal = Portal.from_object(obj)
        
        assert portal.id == "test-portal"
        assert portal.type == "portal"
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 5
        assert portal.targetY == 15
    
    def test_portal_with_optional_fields(self):
        """Test creating a portal with optional fields."""
        portal = Portal(
            id="test-portal",
            type="portal",
            x=10,
            y=20,
            width=2,
            height=3,
            targetMap="destination-map",
            targetX=5,
            targetY=15,
            normal="left",
            orientation="horizontal",
            properties={"custom": "value"}
        )
        
        assert portal.id == "test-portal"
        assert portal.width == 2
        assert portal.height == 3
        assert portal.normal == "left"
        assert portal.orientation == "horizontal"
        assert portal.properties == {"custom": "value"} 