"""Client for interacting with the Gather.town API."""

from typing import Any, Dict, List, Optional, Union
import os
import logging
import requests
from pydantic import BaseModel
from urllib.parse import quote

from gather_manager.models.space import Space, Map, MapData, Object
from gather_manager.utils.exceptions import GatherApiError

logger = logging.getLogger(__name__)


class GatherClient:
    """Client for interacting with the Gather.town API."""
    
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.gather.town"):
        """Initialize Gather.town API client.
        
        Args:
            api_key: Gather.town API key. If not provided, looks for GATHER_API_KEY env var.
            base_url: Base URL for the API.
        
        Raises:
            ValueError: If no API key is provided or found in environment.
        """
        self.api_key = api_key or os.environ.get("GATHER_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Provide it directly or set GATHER_API_KEY environment variable.")
        
        self.base_url = base_url
        self.headers = {
            "apiKey": self.api_key,
            "Content-Type": "application/json"
        }
    
    def _format_space_id(self, space_id: str) -> str:
        """Format space ID for use in URLs according to the API docs.
        
        The docs specify that forward slashes in spaceId must be replaced by backslashes.
        Then the entire string should be URL-encoded.
        
        Args:
            space_id: Original space ID string.
        
        Returns:
            URL-encoded space ID with backslashes.
        """
        formatted = space_id.replace("/", "\\")
        return quote(formatted, safe="")
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make a request to the Gather.town API.
        
        Args:
            method: HTTP method (GET, POST, etc)
            endpoint: API endpoint path
            data: Request body data
            params: Query parameters
            
        Returns:
            Response data as JSON
            
        Raises:
            GatherApiError: If the API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                error_msg += f" - {e.response.text}"
            logger.error(error_msg)
            raise GatherApiError(error_msg) from e
    
    def get_space(self, space_id: str) -> Space:
        """Get information about a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            Space information
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request("GET", f"api/v2/spaces/{formatted_space_id}")
        return Space.model_validate(data)
    
    def get_maps(self, space_id: str) -> List[Map]:
        """Get list of maps in a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            List of maps
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request("GET", f"api/v2/spaces/{formatted_space_id}/maps", params={"useV2Map": "true"})
        return [Map.model_validate(map_data) for map_data in data]
    
    def get_map_data(self, space_id: str, map_id: str) -> MapData:
        """Get detailed data for a specific map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            Map data including objects
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request("GET", f"api/v2/spaces/{formatted_space_id}/maps/{map_id}")
        return MapData.model_validate(data)
    
    def get_map_objects(self, space_id: str, map_id: str) -> List[Object]:
        """Get all objects from a map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of objects in the map
        """
        map_data = self.get_map_data(space_id, map_id)
        return map_data.objects
    
    def get_portals(self, space_id: str, map_id: str) -> List[Object]:
        """Get all portal objects from a map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of portal objects in the map
        """
        objects = self.get_map_objects(space_id, map_id)
        return [obj for obj in objects if obj.type == "portal"]
    
    def update_map_background(self, space_id: str, map_id: str, background: str) -> 'MapData':
        """Update the background for a given room map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map to update
            background: New background identifier or URL
        
        Returns:
            Updated MapData object
        """
        formatted_space_id = self._format_space_id(space_id)
        data = {"background": background}
        response = self._request("PUT", f"api/v2/spaces/{formatted_space_id}/maps/{map_id}", data=data)
        return MapData.model_validate(response) 