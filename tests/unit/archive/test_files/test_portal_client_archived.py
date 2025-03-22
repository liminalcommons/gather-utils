"""Tests for portal client functionality.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Archived
- Owner: Development Team
- Purpose: Validate portal client functionality for interacting with portal API
- Lifecycle:
  - Created: To ensure portal client works correctly
  - Active: Used to validate portal client behavior
  - Obsolescence Conditions:
    1. When the portal client is significantly redesigned
    2. When the API changes significantly
  - Archived Reason: Replaced by tests/unit/api/test_portal_client.py with improved structure
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
                "targetY": 5,
            },
            {"id": "obj1", "type": "image", "x": 15, "y": 25},
            {
                "id": "portal2",
                "type": "portal",
                "x": 30,
                "y": 40,
                "targetMap": "map3",
                "targetX": 1,
                "targetY": 1,
                "normal": "left",
                "orientation": "horizontal",
            },
        ],
    }


class TestPortalClient:
    """Tests for portal-related functionality in the GatherClient."""

    @responses.activate
    def test_get_portals(self, client, sample_map_data):
        """Test getting portals from a map."""
        # Mock API response
        responses.add(
            responses.GET,
            "https://api.gather.town/api/v2/spaces/test-space/maps/test-map",
            json=sample_map_data,
            status=200,
        )

        portals = client.get_portals("test-space", "test-map")

        assert len(portals) == 2
        assert portals[0].id == "portal1"
        assert portals[0].type == "portal"
        assert portals[0].targetMap == "map2"
        assert portals[1].id == "portal2"
        assert portals[1].normal == "left"

    @responses.activate
    def test_get_portal_objects(self, client, sample_map_data):
        """Test getting portal objects as Portal instances."""
        # Mock API response
        responses.add(
            responses.GET,
            "https://api.gather.town/api/v2/spaces/test-space/maps/test-map",
            json=sample_map_data,
            status=200,
        )

        portals = client.get_portal_objects("test-space", "test-map")

        assert len(portals) == 2
        assert isinstance(portals[0], Portal)
        assert portals[0].id == "portal1"
        assert portals[0].type == "portal"
        assert portals[0].targetMap == "map2"
        assert isinstance(portals[1], Portal)
        assert portals[1].id == "portal2"
        assert portals[1].normal == "left"

    @responses.activate
    def test_get_portals_empty(self, client):
        """Test getting portals from a map with no portals."""
        # Mock API response with no portals
        responses.add(
            responses.GET,
            "https://api.gather.town/api/v2/spaces/test-space/maps/empty-map",
            json={
                "id": "empty-map",
                "name": "Empty Map",
                "objects": [{"id": "obj1", "type": "image", "x": 15, "y": 25}],
            },
            status=200,
        )

        portals = client.get_portals("test-space", "empty-map")

        assert len(portals) == 0

    @responses.activate
    def test_get_portals_real_data(self, client):
        """Test getting portals using real map data from a file."""
        # This test assumes you have a sample map file in tests/data
        # If you don't have this file, the test will be skipped
        map_file = Path(__file__).parent.parent / "data" / "sample_map.json"
        if not map_file.exists():
            pytest.skip("Sample map file not found")

        with open(map_file, "r") as f:
            map_data = json.load(f)

        # Mock API response with real data
        responses.add(
            responses.GET,
            "https://api.gather.town/api/v2/spaces/test-space/maps/real-map",
            json=map_data,
            status=200,
        )

        portals = client.get_portals("test-space", "real-map")

        # Just check that we got some results without asserting specific values
        # since the real data might change
        assert isinstance(portals, list)
