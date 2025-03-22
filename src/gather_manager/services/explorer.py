"""Service for exploring and analyzing portal structures in Gather.town."""

import json
import os
import logging
from typing import Dict, List, Optional, Any, Set, Tuple
from datetime import datetime

from gather_manager.api.client import GatherClient
from gather_manager.models.space import Object, Map, MapData
from gather_manager.utils.exceptions import GatherApiError, GatherManagerError

logger = logging.getLogger(__name__)


class PortalExplorer:
    """Service for exploring and analyzing portal structures in Gather.town."""
    
    def __init__(self, client: Optional[GatherClient] = None, output_dir: str = "data"):
        """Initialize with optional client and output directory.
        
        Args:
            client: GatherClient instance or None to create a new one
            output_dir: Directory to store output data
            
        Raises:
            GatherManagerError: If there are issues initializing the client
        """
        try:
            self.client = client or GatherClient()
            self.output_dir = output_dir
            
            # Create timestamp for this exploration session
            self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Create session directory
            self.session_dir = os.path.join(output_dir, f"exploration_{self.timestamp}")
            os.makedirs(self.session_dir, exist_ok=True)
        except Exception as e:
            raise GatherManagerError(f"Failed to initialize PortalExplorer: {str(e)}") from e
    
    def analyze_map_portals(self, space_id: str, map_id: str) -> List[Object]:
        """Analyze portal structures in a specific map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of portal objects
            
        Raises:
            GatherManagerError: If there are issues retrieving portal information
        """
        logger.info(f"Analyzing portals in map {map_id} of space {space_id}")
        
        try:
            # Get all portals in the map - using the client's improved portal detection
            portals = self.client.get_portals(space_id, map_id)
            
            if not portals:
                logger.info(f"No portals found in map {map_id}")
                return []
            
            logger.info(f"Found {len(portals)} portals in map {map_id}")
            
            # Save portals to file
            self._save_to_json(
                data=[p.model_dump(exclude_none=False) for p in portals],
                filename=f"portals_{map_id}.json",
                message=f"Saved {len(portals)} portals from map {map_id}"
            )
            
            # Get full map data for context
            map_data = self.client.get_map_data(space_id, map_id)
            self._save_to_json(
                data=map_data.model_dump(exclude_none=False),
                filename=f"map_{map_id}.json",
                message=f"Saved full map data for {map_id}"
            )
            
            return portals
        except GatherApiError as e:
            logger.error(f"API error while analyzing map {map_id}: {str(e)}")
            raise GatherManagerError(f"Failed to analyze map {map_id}: {str(e)}") from e
        except Exception as e:
            logger.error(f"Unexpected error while analyzing map {map_id}: {str(e)}")
            raise GatherManagerError(f"Failed to analyze map {map_id}: {str(e)}") from e
    
    def analyze_all_maps(self, space_id: str) -> Dict[str, List[Object]]:
        """Analyze portals in all maps of a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            Dictionary mapping map IDs to lists of portal objects
            
        Raises:
            GatherManagerError: If there are issues retrieving or analyzing maps
        """
        logger.info(f"Analyzing all maps in space {space_id}")
        
        try:
            # Get all maps in the space
            maps = self.client.get_maps(space_id)
            logger.info(f"Found {len(maps)} maps in space {space_id}")
            
            # Save maps list
            self._save_to_json(
                data=[m.model_dump(exclude_none=False) for m in maps],
                filename=f"maps_list_{space_id}.json",
                message=f"Saved list of {len(maps)} maps"
            )
            
            # Analyze portals in each map
            results = {}
            for map_obj in maps:
                map_id = map_obj.id
                try:
                    portals = self.analyze_map_portals(space_id, map_id)
                    results[map_id] = portals
                except GatherManagerError as e:
                    logger.warning(f"Skipping map {map_id} due to error: {str(e)}")
                    results[map_id] = []
            
            # Generate and save portal connections
            connections = self._analyze_portal_connections(results)
            self._save_to_json(
                data=connections,
                filename=f"portal_connections_{space_id}.json",
                message=f"Saved portal connections analysis"
            )
            
            # Save summary
            summary = {
                "maps_count": len(maps),
                "portals_by_map": {map_id: len(portals) for map_id, portals in results.items()},
                "total_portals": sum(len(portals) for portals in results.values()),
                "connections": len(connections),
            }
            
            self._save_to_json(
                data=summary,
                filename=f"portal_summary_{space_id}.json",
                message=f"Saved portal summary for all maps"
            )
            
            return results
        except GatherApiError as e:
            logger.error(f"API error while analyzing maps in space {space_id}: {str(e)}")
            raise GatherManagerError(f"Failed to analyze maps in space {space_id}: {str(e)}") from e
        except Exception as e:
            logger.error(f"Unexpected error while analyzing maps in space {space_id}: {str(e)}")
            raise GatherManagerError(f"Failed to analyze maps in space {space_id}: {str(e)}") from e
    
    def _analyze_portal_connections(self, portal_map: Dict[str, List[Object]]) -> List[Dict[str, Any]]:
        """Analyze portal connections between maps.
        
        Args:
            portal_map: Dictionary mapping map IDs to lists of portal objects
            
        Returns:
            List of portal connection details
        """
        connections = []
        
        # Track which maps have been processed to avoid duplicates
        processed_connections: Set[Tuple[str, str, int, int, str, int, int]] = set()
        
        for source_map_id, portals in portal_map.items():
            for portal in portals:
                if portal.targetMap and portal.targetX is not None and portal.targetY is not None:
                    # Create a unique identifier for this connection
                    connection_id = (
                        source_map_id, 
                        portal.targetMap, 
                        portal.x, 
                        portal.y,
                        portal.targetMap,
                        portal.targetX,
                        portal.targetY
                    )
                    
                    # Skip if we've already processed this connection
                    if connection_id in processed_connections:
                        continue
                    
                    # Add to processed set
                    processed_connections.add(connection_id)
                    
                    # Create connection record
                    connection = {
                        "source_map": source_map_id,
                        "source_x": portal.x,
                        "source_y": portal.y,
                        "target_map": portal.targetMap,
                        "target_x": portal.targetX,
                        "target_y": portal.targetY,
                        "bidirectional": False,  # Will check this below
                        "portal_properties": portal.model_dump(exclude={"id", "x", "y", "targetMap", "targetX", "targetY"})
                    }
                    
                    # Check if there's a portal back
                    if portal.targetMap in portal_map:
                        target_portals = portal_map[portal.targetMap]
                        for target_portal in target_portals:
                            if (target_portal.targetMap == source_map_id and
                                target_portal.targetX == portal.x and
                                target_portal.targetY == portal.y and
                                target_portal.x == portal.targetX and
                                target_portal.y == portal.targetY):
                                connection["bidirectional"] = True
                                break
                    
                    connections.append(connection)
        
        return connections
    
    def _save_to_json(self, data: Any, filename: str, message: Optional[str] = None):
        """Save data to a JSON file in the session directory.
        
        Args:
            data: Data to save
            filename: Name of the file
            message: Optional message to log after saving
            
        Raises:
            GatherManagerError: If there are issues saving the file
        """
        filepath = os.path.join(self.session_dir, filename)
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            if message:
                logger.info(f"{message} to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save data to {filepath}: {str(e)}")
            raise GatherManagerError(f"Failed to save data to {filepath}: {str(e)}") from e
            
    def analyze_portal_properties(self, space_id: str) -> Dict[str, Any]:
        """Analyze common properties and patterns in portal objects.
        
        Args:
            space_id: ID of the space
            
        Returns:
            Dictionary with portal property analysis
            
        Raises:
            GatherManagerError: If there are issues analyzing portal properties
        """
        logger.info(f"Analyzing portal properties in space {space_id}")
        
        try:
            # Get all maps and their portals
            portal_map = self.analyze_all_maps(space_id)
            
            # Flatten all portals into a single list
            all_portals = [portal for portals in portal_map.values() for portal in portals]
            
            if not all_portals:
                logger.info("No portals found in any maps")
                return {"portal_count": 0}
            
            # Collect all property keys across all portals
            all_property_keys = set()
            for portal in all_portals:
                portal_dict = portal.model_dump(exclude_none=False)
                all_property_keys.update(portal_dict.keys())
            
            # Count occurrences of each property
            property_counts = {key: 0 for key in all_property_keys}
            property_values = {key: set() for key in all_property_keys}
            
            for portal in all_portals:
                portal_dict = portal.model_dump(exclude_none=False)
                for key in all_property_keys:
                    if key in portal_dict and portal_dict[key] is not None:
                        property_counts[key] += 1
                        
                        # For non-complex values, track the unique values
                        if isinstance(portal_dict[key], (str, int, float, bool)):
                            property_values[key].add(portal_dict[key])
            
            # Convert sets to lists for JSON serialization
            property_values = {k: list(v) for k, v in property_values.items()}
            
            # Analyze directional properties
            directional_analysis = self._analyze_directional_properties(all_portals)
            
            # Compile results
            results = {
                "portal_count": len(all_portals),
                "property_frequency": {
                    k: {
                        "count": v,
                        "percentage": round(v / len(all_portals) * 100, 2)
                    } 
                    for k, v in property_counts.items()
                },
                "property_values": property_values,
                "directional_analysis": directional_analysis
            }
            
            # Save results
            self._save_to_json(
                data=results,
                filename=f"portal_properties_analysis_{space_id}.json",
                message=f"Saved portal properties analysis"
            )
            
            return results
        except GatherManagerError as e:
            # Let GatherManagerError pass through
            raise
        except GatherApiError as e:
            logger.error(f"API error while analyzing portal properties: {str(e)}")
            raise GatherManagerError(f"Failed to analyze portal properties: {str(e)}") from e
        except Exception as e:
            logger.error(f"Unexpected error while analyzing portal properties: {str(e)}")
            raise GatherManagerError(f"Failed to analyze portal properties: {str(e)}") from e
    
    def _analyze_directional_properties(self, portals: List[Object]) -> Dict[str, Any]:
        """Analyze potential directional properties of portals.
        
        Args:
            portals: List of portal objects
            
        Returns:
            Dictionary with directional property analysis
        """
        # Properties that might indicate directionality
        directional_props = ["normal", "orientation", "direction"]
        
        results = {}
        
        for prop in directional_props:
            prop_values = {}
            for portal in portals:
                portal_dict = portal.model_dump(exclude_none=False)
                if prop in portal_dict and portal_dict[prop] is not None:
                    value = portal_dict[prop]
                    if value not in prop_values:
                        prop_values[value] = 0
                    prop_values[value] += 1
            
            if prop_values:
                results[prop] = {
                    "values": prop_values,
                    "appears_directional": len(prop_values) > 1
                }
        
        return results

    def check_space_access(self, space_id: str) -> bool:
        """Check if we have access to the specified space.
        
        Args:
            space_id: ID of the space to check
            
        Returns:
            True if we have access, False otherwise
            
        Raises:
            GatherManagerError: If there are unexpected issues checking access
        """
        try:
            # Try to get basic space information
            self.client.get_space(space_id)
            logger.info(f"Access verified for space {space_id}")
            return True
        except GatherApiError as e:
            if "403" in str(e):
                logger.warning(f"No access to space {space_id}: Permission denied")
                return False
            elif "404" in str(e):
                logger.warning(f"Space {space_id} not found")
                return False
            else:
                # For other API errors, raise a more specific message
                raise GatherManagerError(f"Error checking access to space {space_id}: {str(e)}") from e
        except Exception as e:
            raise GatherManagerError(f"Unexpected error checking access to space {space_id}: {str(e)}") from e