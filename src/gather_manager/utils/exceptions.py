"""Exceptions for the Gather Manager package."""

from typing import Optional, Any


class GatherManagerError(Exception):
    """Base exception for all Gather Manager errors."""
    
    def __init__(self, message: str, *args: Any):
        self.message = message
        super().__init__(message, *args)


class GatherApiError(GatherManagerError):
    """Exception raised when the Gather.town API returns an error."""
    
    def __init__(
        self, 
        message: str, 
        status_code: Optional[int] = None,
        endpoint: Optional[str] = None,
        *args: Any
    ):
        self.status_code = status_code
        self.endpoint = endpoint
        
        # Format detailed message if additional info provided
        detailed_message = message
        if status_code:
            detailed_message = f"{status_code} - {detailed_message}"
        if endpoint:
            detailed_message = f"{detailed_message} (endpoint: {endpoint})"
            
        super().__init__(detailed_message, *args)


class ValidationError(GatherManagerError):
    """Exception raised when input validation fails."""
    pass


class ConfigurationError(GatherManagerError):
    """Exception raised when there's an issue with configuration."""
    pass