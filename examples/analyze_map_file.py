#!/usr/bin/env python3
"""
Script to analyze a downloaded map file and extract portal information.
This script works with the JSON files downloaded by download_maps.py.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Add the project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gather_manager.models.space import Object, Portal


def extract_portals_from_file(file_path: str) -> List[Dict[str, Any]]:
    """Extract portal information from a map file.
    
    Args:
        file_path: Path to the map JSON file
        
    Returns:
        List of portal objects
    """
    with open(file_path, 'r') as f:
        map_data = json.load(f)
    
    portals = []
    
    # Handle different object formats
    objects = map_data.get('objects', {})
    
    # If objects is a dictionary (ID -> object data)
    if isinstance(objects, dict):
        for obj_id, obj_data in objects.items():
            if obj_data.get('type') == 'portal':
                # Add ID if not present
                if 'id' not in obj_data:
                    obj_data['id'] = obj_id
                portals.append(obj_data)
    
    # If objects is a list
    elif isinstance(objects, list):
        for obj in objects:
            if obj.get('type') == 'portal':
                portals.append(obj)
    
    return portals


def analyze_map(file_path: str) -> None:
    """Analyze a map file and print portal information.
    
    Args:
        file_path: Path to the map JSON file
    """
    print(f"Analyzing map file: {file_path}")
    
    try:
        portals = extract_portals_from_file(file_path)
        
        print(f"Found {len(portals)} portals in the map")
        
        if portals:
            print("\nPortal details:")
            for i, portal in enumerate(portals, 1):
                print(f"\nPortal {i}:")
                print(f"  ID: {portal.get('id', 'Unknown')}")
                print(f"  Position: ({portal.get('x', '?')}, {portal.get('y', '?')})")
                print(f"  Target: {portal.get('targetMap', '?')} at ({portal.get('targetX', '?')}, {portal.get('targetY', '?')})")
                
                # Print additional properties if present
                if 'normal' in portal:
                    print(f"  Normal: {portal['normal']}")
                if 'orientation' in portal:
                    print(f"  Orientation: {portal['orientation']}")
                if 'width' in portal or 'height' in portal:
                    print(f"  Size: {portal.get('width', 1)}x{portal.get('height', 1)}")
        
        # Save portals to a separate file
        output_path = Path(file_path).with_name(f"portals_{Path(file_path).stem}.json")
        with open(output_path, 'w') as f:
            json.dump(portals, f, indent=2)
        
        print(f"\nSaved portal data to: {output_path}")
        
    except Exception as e:
        print(f"Error analyzing map: {e}")


def main():
    """Main function to parse arguments and analyze map files."""
    parser = argparse.ArgumentParser(description="Analyze a Gather.town map file and extract portal information")
    parser.add_argument("file", help="Path to the map JSON file")
    args = parser.parse_args()
    
    analyze_map(args.file)


if __name__ == "__main__":
    main() 