"""
Unit tests for the PortalService class.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate the PortalService functionality
- Lifecycle:
  - Created: To ensure PortalService works correctly with portals
  - Active: Currently used to validate portal service operations
  - Obsolescence Conditions:
    1. When the PortalService is significantly redesigned
    2. When the portal system is changed or replaced
- Last Validated: 2024-03-21
"""

import csv
import json
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from gather_manager.api.client import GatherClient
from gather_manager.models.portal import Portal
from gather_manager.services.portal_service import PortalService


class TestPortalService:
    """Test suite for the PortalService class."""

    @pytest.fixture
    def mock_api_client(self):
        """Fixture to provide a mock API client."""
        mock_client = MagicMock()

        # Setup mock data for maps
        mock_client.get_maps.return_value = [
            {"id": "map1", "name": "Test Map 1"},
            {"id": "map2", "name": "Test Map 2"},
        ]

        # Setup mock data for map objects
        mock_client.get_map_objects.side_effect = lambda map_id: {
            "map1": {
                "objects": [
                    {
                        "id": "portal1",
                        "type": 4,  # Portal type
                        "x": 5,
                        "y": 5,
                        "properties": {
                            "targetMap": "map2",
                            "targetX": 10,
                            "targetY": 20,
                            "normal": True,
                        },
                    },
                    {
                        "id": "portal2",
                        "type": 4,  # Portal type
                        "x": 15,
                        "y": 15,
                        "properties": {
                            # Missing targetMap
                            "targetX": 10,
                            "targetY": 20,
                            "normal": True,
                        },
                    },
                ]
            },
            "map2": {
                "objects": [
                    {
                        "id": "portal3",
                        "type": 4,  # Portal type
                        "x": 10,
                        "y": 20,
                        "properties": {
                            "targetMap": "map1",
                            "targetX": 5,
                            "targetY": 5,
                            "normal": True,
                        },
                    }
                ]
            },
        }[map_id]

        return mock_client

    def test_validate_portals(self, mock_api_client):
        """Test the validate_portals method."""
        # Create a PortalService with the mock API client
        service = PortalService(api_client=mock_api_client)

        # Call the method
        result = service.validate_portals()

        # Verify the API client was called correctly
        mock_api_client.get_maps.assert_called_once()
        assert mock_api_client.get_map_objects.call_count == 2

        # Verify the result contains valid and invalid portals
        assert "valid_portals" in result
        assert "invalid_portals" in result

        # Verify the valid portals
        assert len(result["valid_portals"]) == 2
        assert result["valid_portals"][0]["id"] == "portal1"
        assert result["valid_portals"][1]["id"] == "portal3"

        # Verify the invalid portals
        assert len(result["invalid_portals"]) == 1
        assert result["invalid_portals"][0]["id"] == "portal2"
        assert "reason" in result["invalid_portals"][0]

    def test_analyze_connections(self, mock_api_client):
        """Test the analyze_connections method."""
        # Create a PortalService with the mock API client
        service = PortalService(api_client=mock_api_client)

        # Call the method
        result = service.analyze_connections()

        # Verify the API client was called correctly
        mock_api_client.get_maps.assert_called_once()
        assert mock_api_client.get_map_objects.call_count == 2

        # Verify the result contains the expected connections
        assert len(result) == 2

        # Verify the connection from map1 to map2
        map1_to_map2 = next(
            (
                c
                for c in result
                if c["source_map"] == "map1" and c["destination_map"] == "map2"
            ),
            None,
        )
        assert map1_to_map2 is not None
        assert map1_to_map2["portal_count"] == 1

        # Verify the connection from map2 to map1
        map2_to_map1 = next(
            (
                c
                for c in result
                if c["source_map"] == "map2" and c["destination_map"] == "map1"
            ),
            None,
        )
        assert map2_to_map1 is not None
        assert map2_to_map1["portal_count"] == 1

    def test_get_portal_details(self, mock_api_client):
        """Test the get_portal_details method."""
        # Create a PortalService with the mock API client
        service = PortalService(api_client=mock_api_client)

        # Call the method for map1
        result = service.get_portal_details(map_id="map1")

        # Verify the API client was called correctly
        mock_api_client.get_map_objects.assert_called_once_with("map1")

        # Verify the result contains the expected portal details
        assert len(result) == 2

        # Verify the details of portal1
        portal1 = next((p for p in result if p["id"] == "portal1"), None)
        assert portal1 is not None
        assert portal1["map_id"] == "map1"
        assert portal1["x"] == 5
        assert portal1["y"] == 5
        assert portal1["target_map"] == "map2"
        assert portal1["target_x"] == 10
        assert portal1["target_y"] == 20
        assert portal1["is_valid"] is True

        # Verify the details of portal2
        portal2 = next((p for p in result if p["id"] == "portal2"), None)
        assert portal2 is not None
        assert portal2["map_id"] == "map1"
        assert portal2["is_valid"] is False

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    @patch("pathlib.Path.mkdir")
    def test_export_portals_json(
        self, mock_mkdir, mock_json_dump, mock_file_open, mock_api_client
    ):
        """Test the export_portals method with JSON format."""
        # Create a PortalService with the mock API client
        service = PortalService(api_client=mock_api_client)

        # Call the method
        result = service.export_portals(format="json", output_dir="test_output")

        # Verify the API client was called correctly
        mock_api_client.get_maps.assert_called_once()
        assert mock_api_client.get_map_objects.call_count == 2

        # Verify the directory was created
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

        # Verify the file was opened for writing
        mock_file_open.assert_called_once()
        file_path = mock_file_open.call_args[0][0]
        assert str(file_path).endswith(".json")

        # Verify json.dump was called with the portal data
        mock_json_dump.assert_called_once()
        portal_data = mock_json_dump.call_args[0][0]
        assert len(portal_data) == 3

        # Verify the result is the file path
        assert result.endswith(".json")

    @patch("builtins.open", new_callable=mock_open)
    @patch("csv.writer")
    @patch("pathlib.Path.mkdir")
    def test_export_portals_csv(
        self, mock_mkdir, mock_csv_writer, mock_file_open, mock_api_client
    ):
        """Test the export_portals method with CSV format."""
        # Create a mock CSV writer
        mock_writer = MagicMock()
        mock_csv_writer.return_value = mock_writer

        # Create a PortalService with the mock API client
        service = PortalService(api_client=mock_api_client)

        # Call the method
        result = service.export_portals(format="csv", output_dir="test_output")

        # Verify the API client was called correctly
        mock_api_client.get_maps.assert_called_once()
        assert mock_api_client.get_map_objects.call_count == 2

        # Verify the directory was created
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

        # Verify the file was opened for writing
        mock_file_open.assert_called_once()
        file_path = mock_file_open.call_args[0][0]
        assert str(file_path).endswith(".csv")

        # Verify csv.writer was created
        mock_csv_writer.assert_called_once()

        # Verify the writer's writerow method was called for the header and each portal
        assert mock_writer.writerow.call_count >= 4  # Header + 3 portals

        # Verify the result is the file path
        assert result.endswith(".csv")
