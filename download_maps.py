#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import json
from dotenv import load_dotenv

load_dotenv()

from gather_manager.api.client import GatherClient


def download_maps():
    # Get config values from environment variables
    API_KEY = os.getenv("GATHER_API_KEY", "***REMOVED***")
    # The space ID in .env might be formatted as "***REMOVED***\\Liminal Commons" 
    # Remove quotes if present
    raw_space_id = os.getenv("GATHER_SPACE_ID", "***REMOVED***\\Liminal Commons")
    SPACE_ID, SPACE_NAME = raw_space_id.split('\\') if '\\' in raw_space_id else (raw_space_id, "Liminal Commons")

    print(f"Using API_KEY: {API_KEY}")
    print(f"Using Space ID: {SPACE_ID}")
    print(f"Using Space Name: {SPACE_NAME}")

    # For code, use backslash between SPACE_ID and SPACE_NAME
    code_space_id = f"{SPACE_ID}\\{SPACE_NAME}"
    client = GatherClient(api_key=API_KEY)

    maps = client.get_maps(code_space_id)
    print(f"Found {len(maps)} maps.")

    # Get base output directory from environment variable (default current directory)
    base_output_dir = os.getenv("OUTPUT_DIR", ".")
    output_dir = os.path.join(base_output_dir, SPACE_NAME)
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
        print(f"Downloaded map {map_id} to file {file_path}")


if __name__ == "__main__":
    download_maps() 