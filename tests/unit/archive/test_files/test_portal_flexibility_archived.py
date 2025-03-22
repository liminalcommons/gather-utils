"""Tests for the flexible Portal model."""

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
            type=5, x=10, y=20, targetMap="destination-map"  # Integer type
        )

        assert portal.type == 5
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 0  # Should default to 0
        assert portal.targetY == 0  # Should default to 0

    def test_portal_validation_requires_targetmap(self):
        """Test that portal validation requires targetMap."""
        # Should raise validation error when missing targetMap
        with pytest.raises(ValidationError):
            Portal(
                type="portal",
                x=10,
                y=20,
                # Missing targetMap
            )

    def test_portal_from_object_with_targetmap_only(self):
        """Test converting an Object with only targetMap to a Portal."""
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
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 0  # Should default to 0
        assert portal.targetY == 0  # Should default to 0

    def test_portal_from_object_with_integer_type(self):
        """Test converting an Object with integer type to a Portal."""
        obj = Object(
            id="test-portal",
            type=5,  # Integer type
            x=10,
            y=20,
            targetMap="destination-map",
        )

        portal = Portal.from_object(obj)

        assert portal.id == "test-portal"
        assert portal.type == 5
        assert portal.targetMap == "destination-map"
        assert portal.targetX == 0  # Should default to 0
        assert portal.targetY == 0  # Should default to 0

    def test_portal_from_object_requires_targetmap(self):
        """Test that converting an Object to a Portal requires targetMap."""
        obj = Object(
            id="test-object",
            type="portal",
            x=10,
            y=20,
            # No targetMap
        )

        # Should raise ValueError when missing targetMap
        with pytest.raises(ValueError, match="missing targetMap"):
            Portal.from_object(obj)

    def test_portal_with_partial_target_coordinates(self):
        """Test creating a portal with only one target coordinate."""
        # With targetX but no targetY
        portal1 = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            targetX=5,
            # No targetY
        )

        assert portal1.targetX == 5
        assert portal1.targetY == 0  # Should default to 0

        # With targetY but no targetX
        portal2 = Portal(
            type="portal",
            x=10,
            y=20,
            targetMap="destination-map",
            targetY=15,
            # No targetX
        )

        assert portal2.targetX == 0  # Should default to 0
        assert portal2.targetY == 15
