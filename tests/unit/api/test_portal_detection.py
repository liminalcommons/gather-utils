"""
Unit tests for the enhanced portal detection logic in GatherClient.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate the enhanced portal detection logic in the GatherClient
- Lifecycle:
  - Created: To ensure the GatherClient correctly detects various portal formats
  - Active: Currently used to validate portal detection in different scenarios
  - Obsolescence Conditions:
    1. When the portal detection logic is significantly redesigned
    2. When the Gather API changes its portal representation format
- Last Validated: 2024-03-21
"""

import json
from pathlib import Path

import pytest
import responses

from gather_manager.api.client import GatherClient
from gather_manager.models.space import Object, Portal


@pytest.fixture
def client():
    """Fixture to provide a GatherClient instance."""
    return GatherClient(api_key="test_api_key")


@pytest.fixture
def complex_map_data():
    """Fixture to provide complex map data with various portal types."""
    return {
        "id": "test-map",
        "name": "Test Map",
        "objects": [
            # Case 1: Standard string "portal" type
            {
                "id": "portal1",
                "type": "portal",
                "x": 10,
                "y": 20,
                "targetMap": "map2",
                "targetX": 5,
                "targetY": 15,
            },
            # Case 2: Integer portal type (4)
            {
                "id": "portal2",
                "type": 4,
                "x": 30,
                "y": 40,
                "targetMap": "map3",
                "targetX": 25,
                "targetY": 35,
            },
            # Case 3: Portal with properties object
            {
                "id": "portal3",
                "type": "portal",
                "x": 50,
                "y": 60,
                "properties": {
                    "targetMap": "map4",
                    "targetX": 45,
                    "targetY": 55,
                },
            },
            # Case 4: Non-portal object
            {"id": "not-a-portal", "type": "other", "x": 70, "y": 80},
        ],
    }


class TestPortalDetection:
    """Tests for the enhanced portal detection logic in GatherClient."""

    @responses.activate
    def test_detect_string_portal_type(self, client, complex_map_data):
        """Test detecting portals with string 'portal' type."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Find the portal with string 'portal' type
        string_portal = next((p for p in portals if p.id == "portal1"), None)

        # Verify it was detected and has the correct attributes
        assert string_portal is not None
        assert string_portal.type == "portal"
        assert string_portal.targetMap == "map2"
        assert string_portal.targetX == 5
        assert string_portal.targetY == 15

    @responses.activate
    def test_detect_integer_type_with_targetmap(
        self, client, complex_map_data
    ):
        """Test detecting portals with integer type and targetMap attributes."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Find the portal with integer type
        integer_portal = next((p for p in portals if p.id == "portal2"), None)

        # Verify it was detected and has the correct attributes
        assert integer_portal is not None
        assert integer_portal.type == 4
        assert integer_portal.targetMap == "map3"
        assert integer_portal.targetX == 25
        assert integer_portal.targetY == 35

    @responses.activate
    def test_detect_portal_properties(self, client, complex_map_data):
        """Test detecting portals with properties object."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Find the portal with properties object
        properties_portal = next(
            (p for p in portals if p.id == "portal3"), None
        )

        # Verify it was detected and has the correct attributes
        assert properties_portal is not None
        assert properties_portal.type == "portal"
        assert properties_portal.properties.target_map == "map4"
        assert properties_portal.properties.target_x == 45
        assert properties_portal.properties.target_y == 55

    @responses.activate
    def test_detect_specific_integer_types(self, client, complex_map_data):
        """Test detecting portals with specific integer types."""
        # Add an additional portal with a different integer type
        complex_map_data["objects"].append(
            {
                "id": "portal4",
                "type": 5,  # Another integer type that might be a portal
                "x": 90,
                "y": 100,
                "targetMap": "map5",
                "targetX": 85,
                "targetY": 95,
            }
        )

        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Find the new portal with integer type 5
        integer_portal = next((p for p in portals if p.id == "portal4"), None)

        # Verify it was detected and has the correct attributes
        assert integer_portal is not None
        assert integer_portal.type == 5
        assert integer_portal.targetMap == "map5"

    @responses.activate
    def test_non_portals_not_detected(self, client, complex_map_data):
        """Test that non-portal objects are not detected as portals."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Check that the non-portal object was not included
        non_portal_ids = [p.id for p in portals]
        assert "not-a-portal" not in non_portal_ids

        # Also check the total count of portals
        assert len(portals) == 3  # Should only detect the 3 portals

    @responses.activate
    def test_all_portals_detected(self, client, complex_map_data):
        """Test that all portal types are correctly detected."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=complex_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Check that all expected portals are included
        portal_ids = [p.id for p in portals]
        expected_ids = ["portal1", "portal2", "portal3"]

        for expected_id in expected_ids:
            assert expected_id in portal_ids

        # Also check the total count
        assert len(portals) == len(expected_ids)
