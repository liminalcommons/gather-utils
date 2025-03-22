"""
Unit tests for the portal analysis CLI commands.

Test Metadata:
- Created: 2024-03-21
- Last Updated: 2024-03-21
- Status: Active
- Owner: Development Team
- Purpose: Validate the portal CLI commands functionality
- Lifecycle:
  - Created: To ensure portal CLI commands work correctly
  - Active: Currently used to validate CLI command behavior
  - Obsolescence Conditions:
    1. When the CLI interface is significantly redesigned
    2. When the portal analysis commands are removed or replaced
- Last Validated: 2024-03-21
"""

from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

# Import the CLI app and commands we want to test
from gather_manager.cli.main import app
from gather_manager.models.portal import Portal


@pytest.fixture
def cli_runner():
    """Fixture to provide a CLI runner for testing."""
    return CliRunner()


@pytest.fixture
def mock_portal_service():
    """Fixture to provide a mock portal service."""
    mock_service = MagicMock()

    # Setup mock data for validation
    mock_service.validate_portals.return_value = {
        "valid_portals": [
            {
                "id": "portal1",
                "map_id": "map1",
                "x": 5,
                "y": 5,
                "target_map": "map2",
                "target_x": 10,
                "target_y": 20,
                "is_valid": True,
            }
        ],
        "invalid_portals": [
            {
                "id": "portal2",
                "map_id": "map1",
                "x": 15,
                "y": 15,
                "target_map": None,
                "is_valid": False,
                "reason": "Missing target map",
            }
        ],
    }

    # Setup mock data for connections
    mock_service.analyze_connections.return_value = [
        {"source_map": "map1", "destination_map": "map2", "portal_count": 2},
        {"source_map": "map2", "destination_map": "map1", "portal_count": 1},
    ]

    # Setup mock data for details
    mock_service.get_portal_details.return_value = [
        {
            "id": "portal1",
            "map_id": "map1",
            "x": 5,
            "y": 5,
            "target_map": "map2",
            "target_x": 10,
            "target_y": 20,
            "is_valid": True,
        }
    ]

    return mock_service


class TestPortalCommands:
    """Test suite for the portal analysis CLI commands."""

    @patch("gather_manager.cli.main.PortalService")
    def test_portal_validation_command(
        self, mock_portal_service_class, cli_runner, mock_portal_service
    ):
        """Test the portal validation command."""
        # Setup the mock
        mock_portal_service_class.return_value = mock_portal_service

        # Run the command
        result = cli_runner.invoke(
            app, ["portals", "validate", "--space-id", "test_space_id"]
        )

        # Print the result for debugging
        print(f"Exit code: {result.exit_code}")
        print(f"Exception: {result.exception}")
        print(f"Output: {result.stdout}")

        # Verify the command was successful
        assert result.exit_code == 0

        # Verify the service was called with the correct parameters
        mock_portal_service.validate_portals.assert_called_once()

        # Verify the output contains the expected information
        assert "Valid Portals" in result.stdout
        assert "Invalid Portals" in result.stdout
        assert "portal1" in result.stdout
        assert "portal2" in result.stdout
        assert "Missing target map" in result.stdout

    @patch("gather_manager.cli.main.PortalService")
    def test_portal_connections_command(
        self, mock_portal_service_class, cli_runner, mock_portal_service
    ):
        """Test the portal connections command."""
        # Setup the mock
        mock_portal_service_class.return_value = mock_portal_service

        # Run the command
        result = cli_runner.invoke(
            app, ["portals", "connections", "--space-id", "test_space_id"]
        )

        # Print the result for debugging
        print(f"Exit code: {result.exit_code}")
        print(f"Exception: {result.exception}")
        print(f"Output: {result.stdout}")

        # Verify the command was successful
        assert result.exit_code == 0

        # Verify the service was called with the correct parameters
        mock_portal_service.analyze_connections.assert_called_once()

        # Verify the output contains the expected information
        assert "Map Connections" in result.stdout
        assert "map1" in result.stdout
        assert "map2" in result.stdout
        assert "2 portals" in result.stdout
        assert "1 portal" in result.stdout

    @patch("gather_manager.cli.main.PortalService")
    def test_portal_details_command(
        self, mock_portal_service_class, cli_runner, mock_portal_service
    ):
        """Test the portal details command."""
        # Setup the mock
        mock_portal_service_class.return_value = mock_portal_service

        # Run the command
        result = cli_runner.invoke(
            app,
            [
                "portals",
                "details",
                "--space-id",
                "test_space_id",
                "--map-id",
                "map1",
            ],
        )

        # Verify the command was successful
        assert result.exit_code == 0

        # Verify the service was called with the correct parameters
        mock_portal_service.get_portal_details.assert_called_once_with(map_id="map1")

        # Verify the output contains the expected information
        assert "Portal Details for map1" in result.stdout
        assert "portal1" in result.stdout
        assert "Position: (5, 5)" in result.stdout
        assert "Destination: map2 (10, 20)" in result.stdout
        assert "Valid: Yes" in result.stdout

    @patch("gather_manager.cli.main.PortalService")
    def test_portal_export_command_json(
        self, mock_portal_service_class, cli_runner, mock_portal_service
    ):
        """Test the portal export command with JSON format."""
        # Setup the mock
        mock_portal_service_class.return_value = mock_portal_service
        mock_portal_service.export_portals.return_value = "portals.json"

        # Run the command
        result = cli_runner.invoke(
            app,
            [
                "portals",
                "export",
                "--space-id",
                "test_space_id",
                "--format",
                "json",
            ],
        )

        # Verify the command was successful
        assert result.exit_code == 0

        # Verify the service was called with the correct parameters
        mock_portal_service.export_portals.assert_called_once_with(
            format="json", output_dir="data"
        )

        # Verify the output contains the expected information
        assert "Portal data exported to" in result.stdout
        assert "portals.json" in result.stdout

    @patch("gather_manager.cli.main.PortalService")
    def test_portal_export_command_csv(
        self, mock_portal_service_class, cli_runner, mock_portal_service
    ):
        """Test the portal export command with CSV format."""
        # Setup the mock
        mock_portal_service_class.return_value = mock_portal_service
        mock_portal_service.export_portals.return_value = "portals.csv"

        # Run the command
        result = cli_runner.invoke(
            app,
            [
                "portals",
                "export",
                "--space-id",
                "test_space_id",
                "--format",
                "csv",
            ],
        )

        # Verify the command was successful
        assert result.exit_code == 0

        # Verify the service was called with the correct parameters
        mock_portal_service.export_portals.assert_called_once_with(
            format="csv", output_dir="data"
        )

        # Verify the output contains the expected information
        assert "Portal data exported to" in result.stdout
        assert "portals.csv" in result.stdout
