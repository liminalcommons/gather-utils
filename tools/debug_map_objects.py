#!/usr/bin/env python
"""
Debug script to analyze objects in a Gather.town map.
This script helps identify what objects exist and their properties.
"""

import os
import sys
import json
from collections import Counter
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

# Load environment variables from .env file
load_dotenv()

# Add the src directory to the path if running from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from gather_manager.api.client import GatherClient
from gather_manager.utils.exceptions import GatherManagerError

console = Console()

def analyze_map_objects(space_id, map_id):
    """Analyze objects in a map to help identify portals."""
    try:
        # Initialize the client
        client = GatherClient()
        console.print(f"[green]✓[/] Successfully initialized client with API key")
        
        # Get map objects
        console.print(f"Getting objects from map: {map_id}")
        objects = client.get_map_objects(space_id, map_id)
        console.print(f"[green]✓[/] Found {len(objects)} objects in the map")
        
        # Analyze object types
        type_counter = Counter()
        for obj in objects:
            type_counter[str(obj.type)] += 1
        
        # Display object type distribution
        console.print("\n[bold]Object Type Distribution:[/]")
        type_table = Table()
        type_table.add_column("Type", style="cyan")
        type_table.add_column("Count", justify="right")
        type_table.add_column("Percentage", justify="right")
        
        for type_val, count in type_counter.most_common():
            percentage = f"{count / len(objects) * 100:.1f}%"
            type_table.add_row(type_val, str(count), percentage)
        
        console.print(type_table)
        
        # Look for objects with targetMap property
        portal_candidates = [obj for obj in objects if obj.targetMap is not None]
        console.print(f"\nFound {len(portal_candidates)} objects with targetMap property (likely portals)")
        
        if portal_candidates:
            # Display sample portal candidates
            console.print("\n[bold]Sample Portal Candidates:[/]")
            for i, obj in enumerate(portal_candidates[:5]):  # Show up to 5 samples
                console.print(f"\n[bold cyan]Portal Candidate {i+1}:[/]")
                obj_dict = obj.model_dump(exclude_none=True)
                console.print(json.dumps(obj_dict, indent=2))
            
            # Analyze common properties of portal candidates
            console.print("\n[bold]Common Properties of Portal Candidates:[/]")
            common_props = Counter()
            for obj in portal_candidates:
                for key in obj.model_dump(exclude_none=True).keys():
                    common_props[key] += 1
            
            props_table = Table()
            props_table.add_column("Property", style="cyan")
            props_table.add_column("Count", justify="right")
            props_table.add_column("Percentage", justify="right")
            
            for prop, count in common_props.most_common():
                percentage = f"{count / len(portal_candidates) * 100:.1f}%"
                props_table.add_row(prop, str(count), percentage)
            
            console.print(props_table)
        
        # Save results to a file for further analysis
        output_file = f"map_{map_id}_analysis.json"
        with open(output_file, "w") as f:
            analysis = {
                "map_id": map_id,
                "total_objects": len(objects),
                "type_distribution": {k: v for k, v in type_counter.items()},
                "portal_candidates_count": len(portal_candidates),
                "sample_portal_candidates": [obj.model_dump(exclude_none=True) for obj in portal_candidates[:5]]
            }
            json.dump(analysis, f, indent=2)
        
        console.print(f"\n[green]✓[/] Analysis saved to {output_file}")
        
        return True
    except GatherManagerError as e:
        console.print(f"[bold red]API Error:[/] {str(e)}")
        return False
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/] {str(e)}")
        return False

if __name__ == "__main__":
    console.print("[bold]Gather.town Map Object Analyzer[/]\n")
    
    # Get space ID and map ID
    space_id = os.environ.get("GATHER_SPACE_ID")
    if not space_id:
        console.print("[bold red]Error:[/] GATHER_SPACE_ID environment variable not found.")
        sys.exit(1)
    
    if len(sys.argv) < 2:
        console.print("[bold red]Error:[/] Please provide a map ID as an argument.")
        console.print("Usage: python debug_map_objects.py <map_id>")
        sys.exit(1)
    
    map_id = sys.argv[1]
    console.print(f"Analyzing objects in map {map_id} of space {space_id}\n")
    
    analyze_map_objects(space_id, map_id) 