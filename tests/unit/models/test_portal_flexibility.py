"""
Unit tests for the flexible Portal model.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate the Portal model's flexibility with different input formats
- Lifecycle:
  - Created: To ensure Portal model handles various input scenarios correctly
  - Active: Currently used to validate Portal model's flexibility
  - Obsolescence Conditions:
    1. When the Portal model is significantly redesigned
    2. When the portal system is removed or replaced
- Last Validated: 2024-03-21
"""

import pytest
from pydantic import ValidationError

from gather_manager.models.space import Object, Portal


class TestFlexiblePortalModel:
    """Tests for the flexible Portal model."""

    def test_portal_with_targetmap_only(self):
        """Test creating a portal with only targetMap (targetX and targetY should default to 0)."""
        portal = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            # No targetX or targetY
        )

        assert portal.type == "portal"
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 0  # Should default to 0
        assert portal.targetY == 0  # Should default to 0

    def test_portal_with_integer_type(self):
        """Test creating a portal with integer type."""
        portal = Portal(
            type=4,  # Integer type instead of string
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            targetY=15,
        )

        assert portal.type == 4
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 5
        assert portal.targetY == 15

    def test_portal_validation_requires_targetmap(self):
        """Test that portal validation requires targetMap."""
        # Should raise validation error when missing targetMap
        with pytest.raises(ValidationError):
            Portal(
                type="portal",
                x=10,
                y=20,
                # Missing targetMap, but has targetX and targetY
                targetX=5,
                targetY=15,
            )

    def test_portal_from_object_with_targetmap_only(self):
        """Test converting a generic Object to a Portal with only targetMap."""
        obj = Object(
            id="test-portal",
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            # No targetX or targetY
        )

        portal = Portal.from_object(obj)

        assert portal.id == "test-portal"
        assert portal.type == "portal"
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 0  # Should default to 0
        assert portal.targetY == 0  # Should default to 0

    def test_portal_from_object_with_integer_type(self):
        """Test converting a generic Object to a Portal with integer type."""
        obj = Object(
            id="test-portal",
            type=4,  # Integer type instead of string
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            targetY=15,
        )

        portal = Portal.from_object(obj)

        assert portal.id == "test-portal"
        assert portal.type == 4
        assert portal.x == 10
        assert portal.y == 20
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 5
        assert portal.targetY == 15

    def test_portal_from_object_requires_targetmap(self):
        """Test that portal from_object requires targetMap."""
        # Create an object without targetMap
        obj = Object(
            id="test-portal",
            type="portal",
            x=10,
            y=20,
            # Missing targetMap
            targetX=5,
            targetY=15,
        )

        # Should raise ValueError when converting to Portal
        with pytest.raises(ValueError):
            Portal.from_object(obj)

    def test_portal_with_partial_target_coordinates(self):
        """Test creating a portal with partial target coordinates."""
        # Portal with targetMap and targetX but no targetY
        portal1 = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            # No targetY
        )

        assert portal1.targetMap == "destination-map"
        assert portal1.targetX == 5
        assert portal1.targetY == 0  # Should default to 0

        # Portal with targetMap and targetY but no targetX
        portal2 = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            # No targetX
            targetY=15,
        )

        assert portal2.targetMap == "destination-map"
        assert portal2.targetX == 0  # Should default to 0
        assert portal2.targetY == 15
