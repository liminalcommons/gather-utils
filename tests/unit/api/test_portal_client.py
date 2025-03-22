"""
Unit tests for portal-related functionality in the GatherClient.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate the GatherClient's portal-related API functionality
- Lifecycle:
  - Created: To ensure the GatherClient correctly handles portal data
  - Active: Currently used to validate GatherClient interactions with portals
  - Obsolescence Conditions:
    1. When the GatherClient API is significantly redesigned
    2. When the portal API endpoints are changed or removed
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
def sample_map_data():
    """Fixture to provide sample map data with portals."""
    return {
        "id": "test-map",
        "name": "Test Map",
        "objects": [
            {
                "id": "portal1",
                "type": "portal",
                "x": 10,
                "y": 20,
                "targetMap": "map2",
                "targetX": 5,
                "targetY": 15,
            },
            {
                "id": "portal2",
                "type": "portal",
                "x": 30,
                "y": 40,
                "targetMap": "map3",
                "targetX": 25,
                "targetY": 35,
            },
            {"id": "not-a-portal", "type": "other", "x": 50, "y": 60},
        ],
    }


class TestPortalClient:
    """Tests for portal-related functionality in the GatherClient."""

    @responses.activate
    def test_get_portals(self, client, sample_map_data):
        """Test retrieving portal objects from a map."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=sample_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "test-map")

        # Verify the results
        assert len(portals) == 2
        assert all(isinstance(portal, Portal) for portal in portals)
        assert portals[0].id == "portal1"
        assert portals[1].id == "portal2"

    @responses.activate
    def test_get_portal_objects(self, client, sample_map_data):
        """Test retrieving raw portal objects from a map."""
        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/test-map",
            json=sample_map_data,
            status=200,
        )

        # Call the method to test
        portal_objects = client.get_portal_objects("test-space", "test-map")

        # Verify the results
        assert len(portal_objects) == 2
        assert all(isinstance(obj, dict) for obj in portal_objects)
        assert portal_objects[0]["id"] == "portal1"
        assert portal_objects[1]["id"] == "portal2"

    @responses.activate
    def test_get_portals_empty(self, client):
        """Test retrieving portal objects from a map with no portals."""
        # Create a sample map with no portals
        empty_map_data = {
            "id": "empty-map",
            "name": "Empty Map",
            "objects": [{"id": "not-a-portal", "type": "other", "x": 50, "y": 60}],
        }

        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/empty-map",
            json=empty_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "empty-map")

        # Verify the results
        assert len(portals) == 0

    @responses.activate
    def test_get_portals_real_data(self, client):
        """Test retrieving portal objects from a realistic map data structure."""
        # Load a sample of real map data from a file if available,
        # or create a more complex sample
        real_map_data = {
            "id": "real-map",
            "name": "Real Map",
            "objects": [
                {
                    "id": "portal1",
                    "type": "portal",
                    "x": 10,
                    "y": 20,
                    "width": 1,
                    "height": 1,
                    "properties": {
                        "targetMap": "destination-map",
                        "targetX": 5,
                        "targetY": 15,
                        "normal": "right",
                    },
                },
                {
                    "id": "portal2",
                    "type": 4,  # Portal type represented as integer
                    "x": 30,
                    "y": 40,
                    "width": 2,
                    "height": 1,
                    "properties": {
                        "targetMap": "other-map",
                        "targetX": 25,
                        "targetY": 35,
                    },
                },
            ],
        }

        # Mock the API response
        responses.add(
            responses.GET,
            f"https://api.gather.town/api/v2/spaces/test-space/real-map",
            json=real_map_data,
            status=200,
        )

        # Call the method to test
        portals = client.get_portals("test-space", "real-map")

        # Verify the results
        assert len(portals) == 2

        # Check first portal with string type and normal property
        assert portals[0].id == "portal1"
        assert portals[0].type == "portal"
        assert hasattr(portals[0], "normal")
        assert portals[0].normal == "right"

        # Check second portal with integer type
        assert portals[1].id == "portal2"
        assert portals[1].type == 4
