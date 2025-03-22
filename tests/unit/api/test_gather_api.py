"""
Unit tests for the GatherClient API.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate core GatherClient API functionality
- Lifecycle:
  - Created: To ensure GatherClient API operations work correctly
  - Active: Currently used to validate core API functionality
  - Obsolescence Conditions:
    1. When the GatherClient API is significantly redesigned
    2. When the Gather API endpoints are changed
- Last Validated: 2024-03-21
"""

import json
import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

# Add the project root to PYTHONPATH so that the 'gather_manager' package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src')))
load_dotenv()

from gather_manager.api.client import GatherClient

# Use fake API credentials for unit tests
API_KEY = "test_api_key"
SPACE_ID = "test_space_id"
SPACE_NAME = "Test Space"
code_space_id = f"{SPACE_ID}\\{SPACE_NAME}"


def summarize_data(data, max_depth=2, current_depth=0):
    """Recursively summarize data by limiting the depth of nested structures."""
    if current_depth >= max_depth:
        if isinstance(data, (dict, list)):
            return "..."
        return data
    if hasattr(data, '__dict__'):
        data = data.__dict__
    if isinstance(data, dict):
        summary = {}
        for key, value in data.items():
            summary[key] = summarize_data(value, max_depth, current_depth + 1)
        return summary
    elif isinstance(data, list):
        if len(data) > 3:
            return [
                summarize_data(data[0], max_depth, current_depth + 1),
                "...",
                summarize_data(data[-1], max_depth, current_depth + 1),
            ]
        return [summarize_data(item, max_depth, current_depth + 1) for item in data]
    return data


@pytest.mark.skip(reason="Uses real API credentials, only for manual testing")
def test_fetch_space_info():
    """Test fetching space information."""
    client = GatherClient(api_key=API_KEY)
    space_info = client.get_space(SPACE_ID)
    print(f"Space Info: {summarize_data(space_info)}")
    assert space_info is not None
    assert "id" in space_info


@pytest.mark.skip(reason="Uses real API credentials, only for manual testing")
def test_fetch_maps():
    """Test fetching map information."""
    client = GatherClient(api_key=API_KEY)
    maps = client.get_maps(SPACE_ID)
    print(f"Maps: {summarize_data(maps)}")
    assert maps is not None
    assert isinstance(maps, list)
    if maps:
        assert "id" in maps[0]


@pytest.mark.skip(reason="Uses real API credentials, only for manual testing")
def test_download_maps(tmp_path, monkeypatch):
    """Test downloading map data."""
    # Temporarily change to the test directory
    monkeypatch.chdir(tmp_path)
    
    client = GatherClient(api_key=API_KEY)
    space_id = SPACE_ID
    map_ids = [map_data["id"] for map_data in client.get_maps(space_id)][:2]  # Just get first 2 maps
    
    # Download maps
    for map_id in map_ids:
        map_data = client.get_map(space_id, map_id)
        assert map_data is not None
        
        # Save to file
        output_file = f"{map_id}.json"
        with open(output_file, "w") as f:
            json.dump(map_data, f, indent=2)
        
        # Verify file exists
        assert os.path.exists(output_file)
        
        # Load and verify content
        with open(output_file, "r") as f:
            loaded_data = json.load(f)
        
        assert loaded_data["id"] == map_id
        assert "objects" in loaded_data 