"""Data models for Gather.town spaces, maps, and objects."""

from typing import List, Optional, Dict, Any, Union, ClassVar
from pydantic import BaseModel, Field, field_validator, model_validator


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


class Portal(Object):
    """Portal object that connects different maps."""
    type: str = "portal"
    targetMap: str  # Required for portals
    targetX: int    # Required for portals
    targetY: int    # Required for portals
    
    @field_validator('type')
    @classmethod
    def validate_type(cls, v):
        """Validate that the type is 'portal'."""
        if v != "portal":
            raise ValueError("Portal type must be 'portal'")
        return v
    
    @classmethod
    def from_object(cls, obj: Object) -> 'Portal':
        """Convert a generic Object to a Portal if it has the required fields."""
        if obj.type != "portal":
            raise ValueError("Cannot convert non-portal object to Portal")
        
        # Convert to dict and create a Portal instance
        obj_dict = obj.model_dump()
        return cls(**obj_dict)


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
    
    @model_validator(mode='before')
    @classmethod
    def convert_objects(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert objects from different formats to a list of objects."""
        if not isinstance(data, dict):
            return data
            
        # Handle case where objects is a dictionary with IDs as keys
        if 'objects' in data and isinstance(data['objects'], dict):
            objects_dict = data['objects']
            objects_list = []
            
            for obj_id, obj_data in objects_dict.items():
                # Add the ID to the object data if not present
                if 'id' not in obj_data and obj_id:
                    obj_data['id'] = obj_id
                objects_list.append(obj_data)
                
            data['objects'] = objects_list
            
        return data
    
    class Config:
        extra = "allow"


class Space(BaseModel):
    """Gather.town space information."""
    id: str
    name: Optional[str] = None
    # Add other space properties as discovered
    
    class Config:
        extra = "allow" 