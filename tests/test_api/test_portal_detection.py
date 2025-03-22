"""Tests for the enhanced portal detection logic in GatherClient."""

import pytest
import responses
import json
from pathlib import Path

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
                "targetY": 5
            },
            # Case 2: Integer type with targetMap (should be detected as portal)
            {
                "id": "portal2",
                "type": 5,
                "x": 15,
                "y": 25,
                "targetMap": "map3",
                "targetX": 10,
                "targetY": 10
            },
            # Case 3: Object with portal-related properties
            {
                "id": "portal3",
                "type": "custom",
                "x": 30,
                "y": 40,
                "properties": {
                    "isPortal": True,
                    "target": "map4"
                }
            },
            # Case 4: Integer type that matches potential portal types
            {
                "id": "portal4",
                "type": 6,
                "x": 50,
                "y": 60
            },
            # Regular object (not a portal)
            {
                "id": "obj1",
                "type": "image",
                "x": 70,
                "y": 80
            }
        ]
    }


class TestPortalDetection:
    """Tests for the enhanced portal detection logic."""
    
    @responses.activate
    def test_detect_string_portal_type(self, client, complex_map_data):
        """Test detection of portals with string 'portal' type."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify portal with string "portal" type is detected
        portal1 = next((p for p in portals if p.id == "portal1"), None)
        assert portal1 is not None, "Portal with string 'portal' type should be detected"
        assert portal1.type == "portal"
        assert portal1.targetMap == "map2"
    
    @responses.activate
    def test_detect_integer_type_with_targetmap(self, client, complex_map_data):
        """Test detection of portals with integer type and targetMap property."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify portal with integer type and targetMap is detected
        portal2 = next((p for p in portals if p.id == "portal2"), None)
        assert portal2 is not None, "Portal with integer type and targetMap should be detected"
        assert portal2.type == 5
        assert portal2.targetMap == "map3"
    
    @responses.activate
    def test_detect_portal_properties(self, client, complex_map_data):
        """Test detection of portals based on portal-related properties."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify portal with portal-related properties is detected
        portal3 = next((p for p in portals if p.id == "portal3"), None)
        assert portal3 is not None, "Portal with portal-related properties should be detected"
        assert portal3.type == "custom"
        assert portal3.properties.get("isPortal") is True
    
    @responses.activate
    def test_detect_specific_integer_types(self, client, complex_map_data):
        """Test detection of portals with specific integer types."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify portal with specific integer type is detected
        portal4 = next((p for p in portals if p.id == "portal4"), None)
        assert portal4 is not None, "Portal with specific integer type should be detected"
        assert portal4.type == 6
    
    @responses.activate
    def test_non_portals_not_detected(self, client, complex_map_data):
        """Test that non-portal objects are not detected as portals."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify regular object is not detected as portal
        obj1 = next((p for p in portals if p.id == "obj1"), None)
        assert obj1 is None, "Regular object should not be detected as portal"
    
    @responses.activate
    def test_all_portals_detected(self, client, complex_map_data):
        """Test that all portal types are detected."""
        # Setup mock response
        space_id = "test-space"
        map_id = "test-map"
        formatted_space_id = client._format_space_id(space_id)
        
        responses.add(
            responses.GET,
            f"{client.base_url}/api/v2/spaces/{formatted_space_id}/maps/{map_id}",
            json=complex_map_data,
            status=200
        )
        
        # Get portals
        portals = client.get_portals(space_id, map_id)
        
        # Verify all portals are detected
        portal_ids = [p.id for p in portals]
        assert "portal1" in portal_ids, "Portal1 should be detected"
        assert "portal2" in portal_ids, "Portal2 should be detected"
        assert "portal3" in portal_ids, "Portal3 should be detected"
        assert "portal4" in portal_ids, "Portal4 should be detected"
        assert "obj1" not in portal_ids, "Obj1 should not be detected"
        assert len(portals) == 4, "Should detect exactly 4 portals" 