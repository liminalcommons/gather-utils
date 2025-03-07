"""Custom exceptions for the gather-manager package."""


class GatherManagerError(Exception):
    """Base exception for the gather-manager package."""
    pass


class GatherApiError(GatherManagerError):
    """Raised when an API request fails."""
    pass


class PortalError(GatherManagerError):
    """Raised when there's an issue with portal operations."""
    pass


class ContainerError(GatherManagerError):
    """Raised when there's an issue with container operations."""
    pass 