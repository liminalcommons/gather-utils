#!/usr/bin/env python3
"""Debug script to check environment variables."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Find .env file
dotenv_path = find_dotenv()
print(f"Found .env file at: {dotenv_path}")

# Check if .env file exists
env_file = Path(".env")
print(f".env file exists: {env_file.exists()}")
if env_file.exists():
    print(f".env file content:")
    print(env_file.read_text())

# Load environment variables from .env file
load_dotenv(verbose=True)

# Print environment variables
print(f"\nEnvironment variables:")
print(f"GATHER_API_KEY: {os.environ.get('GATHER_API_KEY', 'not set')}")
print(f"GATHER_SPACE_ID: {os.environ.get('GATHER_SPACE_ID', 'not set')}")

# Print the actual values we're trying to use
print("\nActual values we want to use:")
print(f"GATHER_API_KEY: EbhxeTleNa0QvOrW")
print(f"GATHER_SPACE_ID: ELoGghDX4v3HEwI0") 