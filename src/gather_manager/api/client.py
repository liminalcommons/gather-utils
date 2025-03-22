"""Client for interacting with the Gather.town API."""

from typing import Any, Dict, List, Optional, Union
import os
import logging
import requests
from pydantic import BaseModel
from urllib.parse import quote

from gather_manager.models.space import Space, Map, MapData, Object, Portal
from gather_manager.utils.exceptions import GatherApiError

logger = logging.getLogger(__name__)


class GatherClient:
    """Client for interacting with the Gather.town API."""
    
    # Role constants
    ROLE_MEMBER = "MEMBER"       # Current role name (previously was "GENERAL_MEMBER")
    ROLE_MODERATOR = "MODERATOR"
    ROLE_ADMIN = "ADMIN"
    ROLE_BUILDER = "BUILDER"
    
    # Other constants
    DEFAULT_BASE_URL = "https://api.gather.town"
    API_VERSION = "v2"
    
    def __init__(self, api_key: Optional[str] = None, base_url: str = DEFAULT_BASE_URL):
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
        """Make a request to the Gather.town API with enhanced error handling.
        
        Args:
            method: HTTP method (GET, POST, etc)
            endpoint: API endpoint path
            data: Request body data
            params: Query parameters
            
        Returns:
            Response data as JSON
            
        Raises:
            GatherApiError: If the API request fails, with context-specific message
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
            
            # Handle common error codes with specific messages
            if response.status_code == 404:
                error_context = f"Resource not found at {method} {endpoint}"
                if "space" in endpoint:
                    space_id = endpoint.split("/spaces/")[1].split("/")[0]
                    error_context = f"Space '{space_id}' not found"
                    if "maps" in endpoint and len(endpoint.split("/maps/")) > 1:
                        map_id = endpoint.split("/maps/")[1].split("/")[0]
                        error_context = f"Map '{map_id}' not found in space '{space_id}'"
                raise GatherApiError(f"404 Not Found: {error_context}", status_code=404, endpoint=endpoint)
                
            if response.status_code == 403:
                raise GatherApiError(
                    "403 Forbidden: You don't have permission to access this resource. Check your API key and space permissions.", 
                    status_code=403, 
                    endpoint=endpoint
                )
                
            if response.status_code == 429:
                raise GatherApiError(
                    "429 Too Many Requests: Rate limit exceeded. Please reduce request frequency.",
                    status_code=429,
                    endpoint=endpoint
                )
                
            # For other errors, use response.raise_for_status() to get the default error
            response.raise_for_status()
            
            # If we've made it here, the request was successful
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            # For any other HTTP errors not caught above
            status_code = e.response.status_code if hasattr(e, 'response') and e.response is not None else None
            error_msg = f"API request failed: {str(e)}"
            
            if hasattr(e, 'response') and e.response is not None:
                try:
                    # Try to extract error details from JSON response
                    error_data = e.response.json()
                    if isinstance(error_data, dict) and "error" in error_data:
                        error_msg += f" - {error_data['error']}"
                    elif isinstance(error_data, dict) and "message" in error_data:
                        error_msg += f" - {error_data['message']}"
                    else:
                        error_msg += f" - {e.response.text}"
                except ValueError:
                    # If response is not JSON
                    error_msg += f" - {e.response.text}"
            
            logger.error(error_msg)
            raise GatherApiError(error_msg, status_code=status_code, endpoint=endpoint) from e
            
        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error while accessing Gather API: {str(e)}"
            logger.error(error_msg)
            raise GatherApiError(error_msg, endpoint=endpoint) from e
            
        except requests.exceptions.Timeout as e:
            error_msg = f"Timeout while waiting for Gather API response: {str(e)}"
            logger.error(error_msg)
            raise GatherApiError(error_msg, endpoint=endpoint) from e
            
        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            logger.error(error_msg)
            raise GatherApiError(error_msg, endpoint=endpoint) from e
    
    # === Space Operations ===
    
    def create_space(
        self, 
        name: str, 
        source_space: str, 
        reason: Optional[str] = None
    ) -> Space:
        """Create a new Gather.town space by copying an existing template.
        
        Args:
            name: Name for the new space
            source_space: ID of the source space to use as a template
            reason: Optional reason for creating the space
        
        Returns:
            Space: The created space information
        
        Raises:
            GatherApiError: If the space cannot be created
        """
        # Format the source space ID according to API requirements
        formatted_source_space = source_space.replace("/", "\\")
        
        data = {
            "name": name,
            "sourceSpace": formatted_source_space
        }
        
        if reason:
            data["reason"] = reason
        
        response = self._request("POST", f"api/{self.API_VERSION}/spaces", data=data)
        return Space.model_validate(response)
    
    def get_space(self, space_id: str) -> Space:
        """Get information about a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            Space information
        
        Raises:
            GatherApiError: If the space cannot be found or accessed
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request("GET", f"api/{self.API_VERSION}/spaces/{formatted_space_id}")
        return Space.model_validate(data)
    
    def get_spaces(self, role: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get a list of spaces accessible to the API key.
        
        Args:
            role: Optional role filter (e.g., GatherClient.ROLE_BUILDER, GatherClient.ROLE_ADMIN)
            
        Returns:
            List of space information dictionaries
            
        Raises:
            GatherApiError: If the API request fails
        """
        params = {}
        if role:
            params["role"] = role
            
        return self._request("GET", f"api/{self.API_VERSION}/users/me/spaces", params=params)
    
    # === Map Operations ===
    
    def get_maps(self, space_id: str) -> List[Map]:
        """Get list of maps in a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            List of maps
            
        Raises:
            GatherApiError: If the maps cannot be retrieved
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request(
            "GET", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/maps", 
            params={"useV2Map": "true"}
        )
        return [Map.model_validate(map_data) for map_data in data]
    
    def get_map_data(self, space_id: str, map_id: str) -> MapData:
        """Get detailed data for a specific map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            Map data including objects
            
        Raises:
            GatherApiError: If the map data cannot be retrieved
        """
        formatted_space_id = self._format_space_id(space_id)
        data = self._request(
            "GET", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/maps/{map_id}", 
            params={"useV2Map": "true"}
        )
        return MapData.model_validate(data)
    
    def update_map(self, space_id: str, map_id: str, map_data: Union[MapData, Dict[str, Any]]) -> MapData:
        """Update a map with new data.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map to update
            map_data: Either a MapData instance or a dictionary with map data
        
        Returns:
            Updated MapData object
        
        Raises:
            TypeError: If map_data is not a MapData instance or dictionary
            GatherApiError: If the map cannot be updated
        """
        formatted_space_id = self._format_space_id(space_id)
        
        # Convert MapData to dict if needed
        if isinstance(map_data, MapData):
            content = map_data.model_dump()
        elif isinstance(map_data, dict):
            content = map_data
        else:
            raise TypeError("map_data must be a MapData instance or a dictionary")
        
        # Wrap the data in a content field as per API docs
        data = {"content": content}
        
        response = self._request(
            "POST", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/maps/{map_id}",
            data=data,
            params={"useV2Map": "true"}
        )
        return MapData.model_validate(response)
    
    def update_map_background(self, space_id: str, map_id: str, background: str) -> MapData:
        """Update the background for a given room map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map to update
            background: New background identifier or URL
        
        Returns:
            Updated MapData object
            
        Raises:
            GatherApiError: If the background cannot be updated
        """
        formatted_space_id = self._format_space_id(space_id)
        
        # Wrap the data in a content field and use POST as per API docs
        data = {"content": {"background": background}}
        
        response = self._request(
            "POST", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/maps/{map_id}",
            data=data,
            params={"useV2Map": "true"}
        )
        return MapData.model_validate(response)
    
    def update_map_objects(
        self, 
        space_id: str, 
        map_id: str, 
        objects: List[Object]
    ) -> MapData:
        """Update objects on a map without changing other map data.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            objects: List of Object instances to set on the map
        
        Returns:
            Updated MapData object
            
        Raises:
            GatherApiError: If the map objects cannot be updated
        """
        # First get the current map data
        map_data = self.get_map_data(space_id, map_id)
        
        # Update only the objects field
        map_data.objects = objects
        
        # Send the updated map data
        return self.update_map(space_id, map_id, map_data)
    
    # === Object Operations ===
    
    def get_map_objects(self, space_id: str, map_id: str) -> List[Object]:
        """Get all objects from a map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of objects in the map
            
        Raises:
            GatherApiError: If the map objects cannot be retrieved
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
            
        Raises:
            GatherApiError: If the portals cannot be retrieved
        """
        objects = self.get_map_objects(space_id, map_id)
        
        # Enhanced portal detection logic
        portals = []
        for obj in objects:
            # Case 1: Object has type "portal" (string)
            if obj.type == "portal":
                portals.append(obj)
                continue
                
            # Case 2: Object has targetMap property (most reliable indicator of a portal)
            if obj.targetMap is not None:
                portals.append(obj)
                continue
                
            # Case 3: Object has properties that suggest it's a portal
            if obj.properties and any(k in str(obj.properties).lower() for k in ["portal", "target", "teleport", "warp"]):
                portals.append(obj)
                continue
                
            # Case 4: Object has a specific integer type that we've identified as portals
            if isinstance(obj.type, int) and obj.type in [4, 5, 6, 7]:  # Potential portal type values
                portals.append(obj)
                continue
        
        # Log the number of portals found with each detection method
        logger.debug(f"Found {len(portals)} potential portals in map {map_id}")
        
        return portals
    
    def get_portal_objects(self, space_id: str, map_id: str) -> List[Portal]:
        """Get all portal objects from a map as Portal instances.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of Portal instances
            
        Raises:
            GatherApiError: If the portal objects cannot be retrieved
        """
        portal_objects = self.get_portals(space_id, map_id)
        return [Portal.from_object(obj) for obj in portal_objects]
    
    # === User Management ===
    
    def get_user_id_by_email(self, email: str) -> str:
        """Get a user's ID from their email address.
        
        This is needed for management operations like adding/removing users from spaces.
        
        Args:
            email: The email address of the user
        
        Returns:
            str: The user's ID

        Raises:
            GatherApiError: If the user can't be found or other API errors occur
        
        Note:
            This endpoint has strict rate limits (approximately 25 requests/5 minutes)
        """
        try:
            data = self._request("GET", f"api/{self.API_VERSION}/user-id", params={"email": email})
            if not data or "userId" not in data:
                raise GatherApiError(f"User ID not found for email: {email}")
            return data["userId"]
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None and e.response.status_code == 429:
                raise GatherApiError(
                    "Rate limit exceeded for user lookup. This endpoint is limited to ~25 requests/5 minutes.",
                    status_code=429
                ) from e
            raise
    
    def add_user_to_space(self, space_id: str, email: str, role: str = ROLE_MEMBER) -> Dict[str, Any]:
        """Add a user to a space with a specific role.
        
        Args:
            space_id: ID of the space
            email: User's email address
            role: Role to assign (use GatherClient.ROLE_* constants)
        
        Returns:
            Dict containing the response from the API
        
        Raises:
            GatherApiError: If the user can't be added or other API errors occur
        """
        # First get the user ID from email
        user_id = self.get_user_id_by_email(email)
        
        # Then assign the role
        formatted_space_id = self._format_space_id(space_id)
        
        data = {"roles": [role]}
        return self._request(
            "PUT", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/users/{user_id}/roles",
            data=data
        )
    
    def remove_user_from_space(self, space_id: str, email: str) -> Dict[str, Any]:
        """Remove a user from a space by setting an empty roles list.
        
        Args:
            space_id: ID of the space
            email: User's email address
        
        Returns:
            Dict containing the response from the API
        
        Raises:
            GatherApiError: If the user can't be removed or other API errors occur
        """
        # First get the user ID from email
        user_id = self.get_user_id_by_email(email)
        
        # Then remove all roles (empty array)
        formatted_space_id = self._format_space_id(space_id)
        
        data = {"roles": []}
        return self._request(
            "PUT", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/users/{user_id}/roles",
            data=data
        )
    
    def get_space_users(self, space_id: str, role: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get a list of users in a space, optionally filtered by role.
        
        Args:
            space_id: ID of the space
            role: Optional role to filter by (use GatherClient.ROLE_* constants)
        
        Returns:
            List of user dictionaries
        
        Raises:
            GatherApiError: If the API request fails
        """
        formatted_space_id = self._format_space_id(space_id)
        params = {}
        if role:
            params["role"] = role
            
        return self._request(
            "GET", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/users",
            params=params
        )
    
    # === Spawn Token Support ===
    
    def create_spawn_token(
        self, 
        space_id: str, 
        map_id: str, 
        spawn_name: str, 
        expires_in_seconds: Optional[int] = None
    ) -> Dict[str, Any]:
        """Create a spawn token for a specific spawn point in a map.
        
        Spawn tokens can be used for calendar integrations or to generate URLs
        that take users directly to a specific location.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map containing the spawn point
            spawn_name: Name of the spawn point
            expires_in_seconds: Optional expiration time in seconds
            
        Returns:
            Dict containing the spawn token information
        
        Raises:
            GatherApiError: If the API request fails
        """
        formatted_space_id = self._format_space_id(space_id)
        
        data = {
            "room": map_id,
            "spawn": spawn_name,
            "type": "SpawnTile"
        }
        
        # Add expiration if provided
        if expires_in_seconds is not None:
            data["expiresIn"] = expires_in_seconds
        
        response = self._request(
            "POST", 
            f"api/{self.API_VERSION}/spaces/{formatted_space_id}/spawn-tokens",
            data=data
        )
        
        return response