"""Test configuration for the gather-manager package."""

import pytest
import os
import json
from pathlib import Path
from typing import Dict, Any

# Test data directory
TEST_DATA_DIR = Path(__file__).parent / "data"
os.makedirs(TEST_DATA_DIR, exist_ok=True)


@pytest.fixture
def mock_api_key():
    """Fixture to provide a mock API key."""
    return "test_api_key_12345"
