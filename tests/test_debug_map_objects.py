"""Tests for the debug_map_objects script."""

import pytest
import json
import os
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock
from collections import Counter

# Add the src directory to the path so we can import the script
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the script
import debug_map_objects
from gather_manager.api.client import GatherClient
from gather_manager.models.space import Object


@pytest.fixture
def sample_map_data():
    """Fixture to provide sample map data for testing."""
    return {
        "id": "test-map",
        "name": "Test Map",
        "objects": [
            # Portal with string type
            {
                "id": "portal1",
                "type": "portal",
                "x": 10,
                "y": 20,
                "targetMap": "map2",
                "targetX": 5,
                "targetY": 5
            },
            # Portal with integer type
            {
                "id": "portal2",
                "type": 5,
                "x": 15,
                "y": 25,
                "targetMap": "map3",
                "targetX": 10,
                "targetY": 10
            },
            # Regular object
            {
                "id": "obj1",
                "type": "image",
                "x": 70,
                "y": 80
            },
            # Another regular object
            {
                "id": "obj2",
                "type": "image",
                "x": 90,
                "y": 100
            }
        ]
    }


@pytest.fixture
def sample_objects(sample_map_data):
    """Fixture to provide sample objects for testing."""
    return [Object(**obj) for obj in sample_map_data["objects"]]


class TestDebugMapObjects:
    """Tests for the debug_map_objects script functions."""
    
    @patch("debug_map_objects.GatherClient")
    @patch("debug_map_objects.console.print")
    @patch("builtins.open", new_callable=MagicMock)
    @patch("json.dump")
    def test_analyze_map_objects(self, mock_json_dump, mock_open, mock_print, mock_client_class):
        """Test the analyze_map_objects function."""
        # Setup mock client
        mock_client = mock_client_class.return_value
        mock_client.get_map_objects.return_value = [
            Object(id="portal1", type="portal", x=10, y=20, targetMap="map2", targetX=5, targetY=5),
            Object(id="obj1", type="image", x=70, y=80)
        ]
        
        # Call the function
        result = debug_map_objects.analyze_map_objects("test-space", "test-map")
        
        # Verify the function returned True (success)
        assert result is True
        
        # Verify client was called correctly
        mock_client.get_map_objects.assert_called_once_with("test-space", "test-map")
        
        # Verify file was opened for writing
        mock_open.assert_called_once()
        mock_open.return_value.__enter__.assert_called_once()
        
        # Verify json.dump was called
        mock_json_dump.assert_called_once()
        
        # Verify the analysis data structure
        analysis_data = mock_json_dump.call_args[0][0]
        assert analysis_data["map_id"] == "test-map"
        assert analysis_data["total_objects"] == 2
        assert "type_distribution" in analysis_data
        assert "portal_candidates_count" in analysis_data
        assert "sample_portal_candidates" in analysis_data
    
    @patch("debug_map_objects.GatherClient")
    @patch("debug_map_objects.console.print")
    def test_analyze_map_objects_with_no_portals(self, mock_print, mock_client_class):
        """Test the analyze_map_objects function with no portals."""
        # Setup mock client
        mock_client = mock_client_class.return_value
        mock_client.get_map_objects.return_value = [
            Object(id="obj1", type="image", x=70, y=80),
            Object(id="obj2", type="image", x=90, y=100)
        ]
        
        # Call the function with mocked open and json.dump
        with patch("builtins.open", new_callable=MagicMock) as mock_open, \
             patch("json.dump") as mock_json_dump:
            result = debug_map_objects.analyze_map_objects("test-space", "test-map")
            
            # Verify the function returned True (success)
            assert result is True
            
            # Verify json.dump was called with correct portal_candidates_count
            analysis_data = mock_json_dump.call_args[0][0]
            assert analysis_data["portal_candidates_count"] == 0
    
    @patch("debug_map_objects.GatherClient")
    @patch("debug_map_objects.console.print")
    def test_analyze_map_objects_api_error(self, mock_print, mock_client_class):
        """Test the analyze_map_objects function with API error."""
        # Setup mock client to raise an error
        from gather_manager.utils.exceptions import GatherManagerError
        mock_client = mock_client_class.return_value
        mock_client.get_map_objects.side_effect = GatherManagerError("API Error")
        
        # Call the function
        result = debug_map_objects.analyze_map_objects("test-space", "test-map")
        
        # Verify the function returned False (failure)
        assert result is False
        
        # Verify error was printed
        mock_print.assert_any_call("[bold red]API Error:[/] API Error")
    
    @patch("debug_map_objects.GatherClient")
    @patch("debug_map_objects.console.print")
    def test_analyze_map_objects_unexpected_error(self, mock_print, mock_client_class):
        """Test the analyze_map_objects function with unexpected error."""
        # Setup mock client to raise an error
        mock_client = mock_client_class.return_value
        mock_client.get_map_objects.side_effect = Exception("Unexpected Error")
        
        # Call the function
        result = debug_map_objects.analyze_map_objects("test-space", "test-map")
        
        # Verify the function returned False (failure)
        assert result is False
        
        # Verify error was printed
        mock_print.assert_any_call("[bold red]Unexpected Error:[/] Unexpected Error") 