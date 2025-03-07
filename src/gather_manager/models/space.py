"""Data models for Gather.town spaces, maps, and objects."""

from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field


class Position(BaseModel):
    """Position with x and y coordinates."""
    x: int
    y: int


class Object(BaseModel):
    """Base model for map objects."""
    id: Optional[str] = None
    type: str
    x: int
    y: int
    width: Optional[int] = 1
    height: Optional[int] = 1
    properties: Optional[Dict[str, Any]] = None
    # We'll add more fields as we discover them from the API
    
    # Additional fields that might be present in portal objects
    targetMap: Optional[str] = None
    targetX: Optional[int] = None
    targetY: Optional[int] = None
    normal: Optional[str] = None  # Possible directional property
    orientation: Optional[str] = None  # Possible directional property
    
    # Allow additional properties to be captured
    class Config:
        extra = "allow"


class Map(BaseModel):
    """Map information."""
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    
    class Config:
        extra = "allow"


class MapData(BaseModel):
    """Detailed map data including objects."""
    id: str
    name: Optional[str] = None
    objects: List[Object] = Field(default_factory=list)
    # Add other map properties as discovered
    
    class Config:
        extra = "allow"


class Space(BaseModel):
    """Gather.town space information."""
    id: str
    name: Optional[str] = None
    # Add other space properties as discovered
    
    class Config:
        extra = "allow" 