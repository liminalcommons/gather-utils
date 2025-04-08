"""
Tool: Check Env
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Validate system configuration and dependencies
Dependencies: dotenv
Lifecycle:
    - Created: To automate common development tasks
    - Active: Currently used in development workflows
    - Obsolescence Conditions:
        1. When project requirements change significantly
        2. When replaced by more comprehensive tooling
Last Validated: 2025-03-21

"""

#!/usr/bin/env python3
"""
Simple script to check how environment variables are being loaded from the .env file.
"""

import os
import sys

from dotenv import load_dotenv

# Print Python version for debugging
print(f"Python version: {sys.version}")

# Try to load environment variables from .env file
print("Attempting to load .env file...")
load_dotenv(verbose=True)

# Get API key and space ID from environment variables
API_KEY = os.getenv("GATHER_API_KEY")
SPACE_ID = os.getenv("GATHER_SPACE_ID")
OUTPUT_DIR = os.getenv("OUTPUT_DIR")

# Print raw values as they are loaded
print("\nRaw environment variables:")
print(f"GATHER_API_KEY: {API_KEY}")
print(f"GATHER_SPACE_ID: {SPACE_ID}")
print(f"OUTPUT_DIR: {OUTPUT_DIR}")

# Check if SPACE_ID has quotes
if SPACE_ID and (SPACE_ID.startswith('"') and SPACE_ID.endswith('"')):
    print("\nSPACE_ID has quotes, removing them...")
    SPACE_ID = SPACE_ID[1:-1]
    print(f"SPACE_ID after removing quotes: {SPACE_ID}")

# Check for double backslashes and replace with single
if SPACE_ID and "\\\\" in SPACE_ID:
    print("\nSPACE_ID has double backslashes, replacing with single...")
    SPACE_ID = SPACE_ID.replace("\\\\", "\\")
    print(f"SPACE_ID after replacing double backslashes: {SPACE_ID}")

# Print the actual content of the .env file
print("\nActual content of .env file:")
try:
    with open(".env", "r") as f:
        print(f.read())
except Exception as e:
    print(f"Error reading .env file: {str(e)}")

# Try to manually read and parse the .env file
print("\nManually parsing .env file:")
try:
    with open(".env", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                print(f"{key}: {value}")
except Exception as e:
    print(f"Error parsing .env file: {str(e)}")
