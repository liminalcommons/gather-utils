"""Test configuration for the gather-manager package."""

import pytest
import os
import json
from pathlib import Path
from typing import Dict, Any
from unittest.mock import MagicMock, patch

# Test data directory
TEST_DATA_DIR = Path(__file__).parent / "data"
os.makedirs(TEST_DATA_DIR, exist_ok=True)

# Add fixtures that will be available to all tests

@pytest.fixture
def mock_env_vars():
    """Fixture to mock environment variables for testing."""
    with patch.dict(os.environ, {
        "GATHER_API_KEY": "test_api_key",
        "GATHER_SPACE_ID": "test_space_id"
    }):
        yield

@pytest.fixture
def mock_api_client():
    """Fixture to provide a mock API client."""
    mock_client = MagicMock()
    mock_client.get_maps.return_value = [
        {"id": "map1", "name": "Test Map 1"},
        {"id": "map2", "name": "Test Map 2"}
    ]
    mock_client.get_map_objects.return_value = {
        "objects": [
            {
                "id": "portal1",
                "type": 4,  # Portal type
                "properties": {
                    "targetMap": "map2",
                    "targetX": 10,
                    "targetY": 20
                }
            }
        ]
    }
    return mock_client

@pytest.fixture
def sample_portal_data():
    """Fixture to provide sample portal data for testing."""
    return {
        "id": "portal1",
        "type": 4,  # Portal type
        "x": 5,
        "y": 5,
        "properties": {
            "targetMap": "map2",
            "targetX": 10,
            "targetY": 20,
            "normal": True
        }
    }

@pytest.fixture
def sample_map_data():
    """Fixture to provide sample map data for testing."""
    return {
        "id": "map1",
        "name": "Test Map",
        "dimensions": [50, 50],
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
                    "normal": True
                }
            }
        ]
    }

@pytest.fixture
def mock_api_key():
    """Fixture to provide a mock API key."""
    return "test_api_key_12345"
