"""
Service for analyzing portals in Gather.town spaces.
"""
import json
import csv
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

from gather_manager.models.portal import Portal
from gather_manager.api.client import GatherClient


class PortalService:
    """Service for analyzing portals in Gather.town spaces."""

    def __init__(self, api_client: GatherClient):
        """
        Initialize the PortalService.
        
        Args:
            api_client: The API client to use for accessing Gather.town data.
        """
        self.api_client = api_client

    def validate_portals(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Validate all portals across all maps in the space.
        
        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing lists of valid and invalid portals.
        """
        valid_portals = []
        invalid_portals = []
        
        # Get all maps in the space
        maps = self.api_client.get_maps()
        
        # Process each map
        for map_data in maps:
            map_id = map_data["id"]
            
            # Get all objects in the map
            map_objects = self.api_client.get_map_objects(map_id)
            
            # Filter for portal objects (type 4)
            portal_objects = [obj for obj in map_objects.get("objects", []) if obj.get("type") == 4]
            
            # Process each portal
            for portal_obj in portal_objects:
                # Add map_id to the portal object
                portal_obj["map_id"] = map_id
                
                # Create a Portal model instance
                try:
                    portal = Portal.model_validate(portal_obj)
                    
                    # Check if the portal is valid
                    if portal.is_valid():
                        valid_portals.append({
                            "id": portal.id,
                            "map_id": map_id,
                            "x": portal.x,
                            "y": portal.y,
                            "target_map": portal.properties.target_map,
                            "target_x": portal.properties.target_x,
                            "target_y": portal.properties.target_y,
                            "is_valid": True
                        })
                    else:
                        # Determine the reason for invalidity
                        reason = self._get_invalidity_reason(portal)
                        
                        invalid_portals.append({
                            "id": portal.id,
                            "map_id": map_id,
                            "x": portal.x,
                            "y": portal.y,
                            "target_map": portal.properties.target_map,
                            "target_x": portal.properties.target_x,
                            "target_y": portal.properties.target_y,
                            "is_valid": False,
                            "reason": reason
                        })
                except Exception as e:
                    # If the portal can't be validated, add it to the invalid list
                    invalid_portals.append({
                        "id": portal_obj.get("id", "unknown"),
                        "map_id": map_id,
                        "is_valid": False,
                        "reason": f"Validation error: {str(e)}"
                    })
        
        return {
            "valid_portals": valid_portals,
            "invalid_portals": invalid_portals
        }

    def analyze_connections(self) -> List[Dict[str, Any]]:
        """
        Analyze portal connections between maps.
        
        Returns:
            List[Dict[str, Any]]: A list of connections between maps.
        """
        connections = {}
        
        # Get all maps in the space
        maps = self.api_client.get_maps()
        
        # Process each map
        for map_data in maps:
            source_map_id = map_data["id"]
            
            # Get all objects in the map
            map_objects = self.api_client.get_map_objects(source_map_id)
            
            # Filter for portal objects (type 4)
            portal_objects = [obj for obj in map_objects.get("objects", []) if obj.get("type") == 4]
            
            # Process each portal
            for portal_obj in portal_objects:
                # Add map_id to the portal object
                portal_obj["map_id"] = source_map_id
                
                # Create a Portal model instance
                try:
                    portal = Portal.model_validate(portal_obj)
                    
                    # Check if the portal is valid
                    if portal.is_valid():
                        destination_map_id = portal.properties.target_map
                        
                        # Create a connection key
                        connection_key = f"{source_map_id}:{destination_map_id}"
                        
                        # Increment the portal count for this connection
                        if connection_key in connections:
                            connections[connection_key]["portal_count"] += 1
                        else:
                            connections[connection_key] = {
                                "source_map": source_map_id,
                                "destination_map": destination_map_id,
                                "portal_count": 1
                            }
                except Exception:
                    # Skip invalid portals
                    continue
        
        return list(connections.values())

    def get_portal_details(self, map_id: str) -> List[Dict[str, Any]]:
        """
        Get detailed information about portals in a specific map.
        
        Args:
            map_id: The ID of the map to get portal details for.
            
        Returns:
            List[Dict[str, Any]]: A list of portal details.
        """
        portal_details = []
        
        # Get all objects in the map
        map_objects = self.api_client.get_map_objects(map_id)
        
        # Filter for portal objects (type 4)
        portal_objects = [obj for obj in map_objects.get("objects", []) if obj.get("type") == 4]
        
        # Process each portal
        for portal_obj in portal_objects:
            # Add map_id to the portal object
            portal_obj["map_id"] = map_id
            
            # Create a Portal model instance
            try:
                portal = Portal.model_validate(portal_obj)
                
                # Add the portal details
                portal_details.append({
                    "id": portal.id,
                    "map_id": map_id,
                    "x": portal.x,
                    "y": portal.y,
                    "target_map": portal.properties.target_map,
                    "target_x": portal.properties.target_x,
                    "target_y": portal.properties.target_y,
                    "is_valid": portal.is_valid()
                })
            except Exception as e:
                # If the portal can't be validated, add basic information
                portal_details.append({
                    "id": portal_obj.get("id", "unknown"),
                    "map_id": map_id,
                    "x": portal_obj.get("x", 0),
                    "y": portal_obj.get("y", 0),
                    "is_valid": False,
                    "error": str(e)
                })
        
        return portal_details

    def export_portals(self, format: str = "json", output_dir: str = "data") -> str:
        """
        Export portal data to a file.
        
        Args:
            format: The format to export to ("json" or "csv").
            output_dir: The directory to export to.
            
        Returns:
            str: The path to the exported file.
        """
        # Create the output directory if it doesn't exist
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Get all portals
        all_portals = []
        
        # Get all maps in the space
        maps = self.api_client.get_maps()
        
        # Process each map
        for map_data in maps:
            map_id = map_data["id"]
            
            # Get portal details for this map
            portal_details = self.get_portal_details(map_id)
            
            # Add to the list of all portals
            all_portals.extend(portal_details)
        
        # Generate a timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format.lower() == "json":
            # Export to JSON
            file_path = output_path / f"portals_{timestamp}.json"
            with open(file_path, "w") as f:
                json.dump(all_portals, f, indent=2)
        elif format.lower() == "csv":
            # Export to CSV
            file_path = output_path / f"portals_{timestamp}.csv"
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    "ID", "Map ID", "X", "Y", 
                    "Target Map", "Target X", "Target Y", 
                    "Valid"
                ])
                
                # Write portal data
                for portal in all_portals:
                    writer.writerow([
                        portal.get("id", ""),
                        portal.get("map_id", ""),
                        portal.get("x", ""),
                        portal.get("y", ""),
                        portal.get("target_map", ""),
                        portal.get("target_x", ""),
                        portal.get("target_y", ""),
                        "Yes" if portal.get("is_valid", False) else "No"
                    ])
        else:
            raise ValueError(f"Unsupported export format: {format}")
        
        return str(file_path)

    def _get_invalidity_reason(self, portal: Portal) -> str:
        """
        Get the reason why a portal is invalid.
        
        Args:
            portal: The portal to check.
            
        Returns:
            str: The reason for invalidity.
        """
        if portal.properties.target_map is None:
            return "Missing target map"
        elif portal.properties.target_x is None:
            return "Missing target X coordinate"
        elif portal.properties.target_y is None:
            return "Missing target Y coordinate"
        else:
            return "Unknown reason" 