"""
Step definitions for basic CLI command execution feature.

This module demonstrates basic step definition patterns and best practices.
"""

import os
import subprocess
from typing import Dict, Optional

from behave import given, then, when
from behave.runner import Context

# Constants
CLI_DIR = "src/cli"
DEFAULT_TIMEOUT = 30


class CLIContext:
    """Context manager for CLI operations."""

    def __init__(self, context: Context):
        self.original_dir = os.getcwd()
        self.context = context
        self.context.cli_output = ""
        self.context.cli_error = ""
        self.context.exit_code = 0

    def __enter__(self):
        """Set up CLI context."""
        os.chdir(CLI_DIR)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up CLI context."""
        os.chdir(self.original_dir)


@given("I have a valid API key")
def step_given_valid_api_key(context: Context) -> None:
    """
    Set up a valid API key in the context.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If API key cannot be set up
    """
    try:
        context.api_key = "test-api-key"
        os.environ["GATHER_API_KEY"] = context.api_key
    except Exception as e:
        raise AssertionError(f"Failed to set up API key: {str(e)}")


@given("I have a valid space ID")
def step_given_valid_space_id(context: Context) -> None:
    """
    Set up a valid space ID in the context.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If space ID cannot be set up
    """
    try:
        context.space_id = "test-space-id"
        os.environ["GATHER_SPACE_ID"] = context.space_id
    except Exception as e:
        raise AssertionError(f"Failed to set up space ID: {str(e)}")


@given("I am in the CLI directory")
def step_given_in_cli_directory(context: Context) -> None:
    """
    Ensure we're in the CLI directory.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If CLI directory is not accessible
    """
    try:
        context.cli_context = CLIContext(context)
        context.cli_context.__enter__()
    except Exception as e:
        raise AssertionError(f"Failed to access CLI directory: {str(e)}")


@given("the network connection is down")
def step_given_network_down(context: Context) -> None:
    """
    Simulate network connection being down.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If network simulation fails
    """
    try:
        # Simulate network being down by setting an invalid API endpoint
        os.environ["GATHER_API_ENDPOINT"] = "http://invalid-endpoint"
    except Exception as e:
        raise AssertionError(f"Failed to simulate network down: {str(e)}")


@when('I run the command "{command}"')
def step_when_run_command(context: Context, command: str) -> None:
    """
    Execute a CLI command.

    Args:
        context: Behave context containing test state
        command: Command to execute

    Raises:
        RuntimeError: If command execution fails unexpectedly
    """
    try:
        # Format command with context variables
        formatted_command = command.format(
            space_id=getattr(context, "space_id", ""),
            api_key=getattr(context, "api_key", ""),
        )

        # Execute command
        result = subprocess.run(
            formatted_command.split(),
            capture_output=True,
            text=True,
            timeout=DEFAULT_TIMEOUT,
        )

        # Store results in context
        context.cli_output = result.stdout
        context.cli_error = result.stderr
        context.exit_code = result.returncode

    except subprocess.TimeoutExpired:
        raise RuntimeError(
            f"Command timed out after {DEFAULT_TIMEOUT} seconds"
        )
    except Exception as e:
        raise RuntimeError(f"Command execution failed: {str(e)}")


@then("the command should succeed")
def step_then_command_succeeds(context: Context) -> None:
    """
    Verify command succeeded.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If command did not succeed
    """
    assert (
        context.exit_code == 0
    ), f"Command failed with exit code {context.exit_code}\nError: {context.cli_error}"


@then("the command should fail")
def step_then_command_fails(context: Context) -> None:
    """
    Verify command failed.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If command did not fail
    """
    assert (
        context.exit_code != 0
    ), "Command succeeded when it should have failed"


@then('the output should contain "{text}"')
def step_then_output_contains(context: Context, text: str) -> None:
    """
    Verify command output contains expected text.

    Args:
        context: Behave context containing test state
        text: Text to look for in output

    Raises:
        AssertionError: If text is not found in output
    """
    assert (
        text in context.cli_output
    ), f"Expected text '{text}' not found in output:\n{context.cli_output}"


@then('the error message should mention "{text}"')
def step_then_error_mentions(context: Context, text: str) -> None:
    """
    Verify error message contains expected text.

    Args:
        context: Behave context containing test state
        text: Text to look for in error message

    Raises:
        AssertionError: If text is not found in error message
    """
    assert (
        text in context.cli_error
    ), f"Expected text '{text}' not found in error:\n{context.cli_error}"


@then("a detailed error log should be created")
def step_then_error_log_created(context: Context) -> None:
    """
    Verify error log was created.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If error log is not found
    """
    try:
        log_file = "error.log"
        assert os.path.exists(log_file), "Error log file not created"
        with open(log_file) as f:
            content = f.read()
            assert context.cli_error in content, "Error details not logged"
    except Exception as e:
        raise AssertionError(f"Error log verification failed: {str(e)}")


@then("the space name should be displayed")
def step_then_space_name_displayed(context: Context) -> None:
    """
    Verify space name is displayed in output.

    Args:
        context: Behave context containing test state

    Raises:
        AssertionError: If space name is not found in output
    """
    assert (
        "name" in context.cli_output.lower()
    ), "Space name not found in output"
