"""
Environment setup for BDD tests.
This file contains hooks that run before and after certain events during testing.
"""

import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import MagicMock

from dotenv import load_dotenv

# Try to load environment variables from .env file
load_dotenv()


def before_all(context):
    """Set up the environment before all tests run."""
    # Create a temporary directory for test files
    context.temp_dir = tempfile.mkdtemp()
    print(f"Created temporary test directory: {context.temp_dir}")

    # Set up common configuration
    context.config = {"api_key": "test_api_key", "space_id": "test_space_id"}


def after_all(context):
    """Clean up after all tests have run."""
    # Remove the temporary directory
    if hasattr(context, "temp_dir") and os.path.exists(context.temp_dir):
        shutil.rmtree(context.temp_dir)
        print(f"Removed temporary test directory: {context.temp_dir}")


def before_feature(context, feature):
    """Set up before each feature runs."""
    print(f"Running feature: {feature.name}")

    # Create a feature-specific output directory
    if hasattr(context, "output_dir"):
        feature_dir = (
            context.output_dir / feature.name.replace(" ", "_").lower()
        )
        feature_dir.mkdir(exist_ok=True)
        context.feature_output_dir = feature_dir


def after_feature(context, feature):
    """Clean up after each feature has run."""
    print(f"Completed feature: {feature.name}")


def before_scenario(context, scenario):
    """Set up before each scenario runs."""
    print(f"Running scenario: {scenario.name}")

    # Create a mock client for each scenario
    context.mock_client = MagicMock()


def after_scenario(context, scenario):
    """Clean up after each scenario has run."""
    print(f"Completed scenario: {scenario.name}")
