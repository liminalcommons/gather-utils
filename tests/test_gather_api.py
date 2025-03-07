#!/usr/bin/env python3
import sys, os
import json
import pytest

# Add the project root to PYTHONPATH so that the 'gather_manager' package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from dotenv import load_dotenv
load_dotenv()

from gather_manager.api.client import GatherClient

API_KEY = "***REMOVED***"
SPACE_ID = "***REMOVED***"
SPACE_NAME = "Liminal Commons"
# For code, use backslash between SPACE_ID and SPACE_NAME
code_space_id = f"{SPACE_ID}\\{SPACE_NAME}"

client = GatherClient(api_key=API_KEY)


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
        return [summarize_data(item, max_depth, current_depth + 1) for item in data]
    else:
        return data


def test_fetch_space_info():
    """Test that fetching space info returns expected fields."""
    space = client.get_space(code_space_id)
    summarized_space = summarize_data(space)
    assert "id" in summarized_space, "Space info should contain an 'id' field"
    assert summarized_space.get("name") == SPACE_NAME, "Space name should match"


def test_fetch_maps():
    """Test that fetching maps returns a non-empty list and each map has an 'id'."""
    maps = client.get_maps(code_space_id)
    assert isinstance(maps, list), "Maps should be returned as a list"
    assert len(maps) > 0, "There should be at least one map"
    for m in maps:
        assert hasattr(m, 'id'), "Each map should have an 'id' attribute"


def test_download_maps(tmp_path, monkeypatch):
    """Test downloading maps saves JSON files to the directory specified by OUTPUT_DIR env (overridden to tmp_path)."""
    # Override OUTPUT_DIR to use temporary directory
    monkeypatch.setenv("OUTPUT_DIR", str(tmp_path))
    maps = client.get_maps(code_space_id)
    output_dir = os.path.join(os.getenv("OUTPUT_DIR", "."), SPACE_NAME)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for m in maps:
        map_id = m.id
        formatted_space_id = client._format_space_id(code_space_id)
        # Get raw map data
        detailed_map = client._request("GET", f"api/v2/spaces/{formatted_space_id}/maps/{map_id}")
        file_name = f"map_{map_id}.json"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w") as f:
            json.dump(detailed_map, f, indent=2)
        assert os.path.exists(file_path), f"Map file {file_name} should exist"
    files = os.listdir(output_dir)
    assert len(files) == len(maps), "The number of downloaded map files should match the number of maps" 