"""
Utility functions for BDD step definitions.

This module provides common utility functions used across step definitions
to ensure consistent behavior and reduce duplication.
"""

from pathlib import Path
from unittest.mock import MagicMock

def create_mock_client():
    """Create a mock API client for testing."""
    mock_client = MagicMock()
    # Configure basic mock behavior
    mock_client.get_maps.return_value = ["map1", "map2", "map3"]
    return mock_client

def setup_test_environment(context):
    """Set up the test environment with common configuration."""
    # Create a mock client if not already present
    if not hasattr(context, "mock_client"):
        context.mock_client = create_mock_client()
    
    # Set up common configuration
    if not hasattr(context, "config"):
        context.config = {"api_key": "test_api_key", "space_id": "test_space_id"}

def find_file_in_project(filename, start_dir="."):
    """Find a file in the project directory."""
    start_path = Path(start_dir)
    for path in start_path.rglob(filename):
        return path
    return None

def assert_with_context(condition, message, context):
    """Assert with additional context information."""
    if not condition:
        # Add any available context information to the message
        if hasattr(context, "last_command"):
            message += f"\nLast command: {context.last_command}"
        if hasattr(context, "last_output"):
            message += f"\nLast output: {context.last_output}"
    
    assert condition, message 