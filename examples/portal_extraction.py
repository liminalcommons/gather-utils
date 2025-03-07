#!/usr/bin/env python3
"""
Example script to test portal extraction from real map data.
This script loads map data from JSON files and extracts portal information.
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

# Add the project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables
load_dotenv()

from gather_manager.api.client import GatherClient
from gather_manager.models.space import Portal


def main():
    """Extract and analyze portals from map data."""
    # Get API key and space ID from environment
    api_key = os.getenv("GATHER_API_KEY")
    space_id = os.getenv("GATHER_SPACE_ID")
    
    if not api_key or not space_id:
        print("Error: GATHER_API_KEY and GATHER_SPACE_ID must be set in .env file")
        return
    
    # Create API client
    client = GatherClient(api_key=api_key)
    
    # Get maps in the space
    print(f"Fetching maps for space: {space_id}")
    maps = client.get_maps(space_id)
    print(f"Found {len(maps)} maps")
    
    # Create output directory
    output_dir = Path("data/portals")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each map
    total_portals = 0
    portal_connections = {}
    
    for map_obj in maps:
        map_id = map_obj.id
        map_name = map_obj.name or map_id
        
        print(f"\nAnalyzing map: {map_name} (ID: {map_id})")
        
        # Get portals for this map
        portals = client.get_portals(space_id, map_id)
        
        print(f"Found {len(portals)} portals in this map")
        total_portals += len(portals)
        
        # Save portal data
        portal_data = [p.model_dump() for p in portals]
        output_file = output_dir / f"portals_{map_id}.json"
        with open(output_file, "w") as f:
            json.dump(portal_data, f, indent=2)
        
        # Track connections
        for portal in portals:
            source = map_id
            target = portal.targetMap
            
            if source not in portal_connections:
                portal_connections[source] = set()
            
            portal_connections[source].add(target)
    
    # Save connection summary
    connection_summary = {
        source: list(targets) 
        for source, targets in portal_connections.items()
    }
    
    with open(output_dir / "portal_connections.json", "w") as f:
        json.dump(connection_summary, f, indent=2)
    
    # Print summary
    print("\nPortal Analysis Summary:")
    print(f"Total maps: {len(maps)}")
    print(f"Total portals: {total_portals}")
    print(f"Maps with portals: {len(portal_connections)}")
    print(f"Results saved to: {output_dir}")


if __name__ == "__main__":
    main() 