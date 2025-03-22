"""Data models for Gather.town spaces, maps, and objects."""

from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator


class Position(BaseModel):
    """Position with x and y coordinates."""

    x: int
    y: int


class Object(BaseModel):
    """Base model for map objects."""

    id: Optional[str] = None
    type: Union[str, int]  # Accept both string and integer
    x: int
    y: int
    width: Optional[int] = 1
    height: Optional[int] = 1
    properties: Optional[Dict[str, Any]] = None
    # Additional fields that might be present in portal objects
    targetMap: Optional[str] = None
    targetX: Optional[int] = None
    targetY: Optional[int] = None
    normal: Optional[str] = None  # Possible directional property
    orientation: Optional[Union[str, int]] = (
        None  # Accept both string and integer
    )
    direction: Optional[Union[str, int]] = (
        None  # Additional directional property
    )

    class Config:
        extra = "allow"  # Allow additional properties to be captured


class Portal(Object):
    """Portal object that connects different maps."""

    type: Union[str, int] = "portal"  # Accept both string and integer
    targetMap: Optional[str] = (
        None  # Make optional for detection, but will be required for valid portals
    )
    targetX: Optional[int] = None  # Make optional for detection
    targetY: Optional[int] = None  # Make optional for detection

    @field_validator("type")
    @classmethod
    def validate_type(cls, v):
        """Validate that the type is acceptable for a portal."""
        # Allow any type value for portals - we'll validate based on other properties
        return v

    @model_validator(mode="after")
    def validate_portal(self):
        """Validate that this is a valid portal with required fields."""
        # For a portal to be valid, it must have a targetMap
        if not self.targetMap:
            raise ValueError("Portal must have a targetMap")

        # If targetX or targetY is missing, set default values
        if self.targetX is None:
            self.targetX = 0
        if self.targetY is None:
            self.targetY = 0

        return self

    @classmethod
    def from_object(cls, obj: Object) -> "Portal":
        """Convert a generic Object to a Portal if it has the required fields."""
        # Check if it's a portal by having targetMap (most reliable indicator)
        if obj.targetMap is None:
            raise ValueError(
                "Cannot convert object to Portal: missing targetMap"
            )

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
    background: Optional[str] = None
    dimensions: Optional[List[int]] = None
    # Add other map properties as needed

    @model_validator(mode="before")
    @classmethod
    def convert_objects(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert objects from different formats to a list of objects."""
        if not isinstance(data, dict):
            return data

        # Handle case where objects is a dictionary with IDs as keys
        if "objects" in data and isinstance(data["objects"], dict):
            objects_dict = data["objects"]
            objects_list = []

            for obj_id, obj_data in objects_dict.items():
                # Add the ID to the object data if not present
                if "id" not in obj_data and obj_id:
                    obj_data["id"] = obj_id
                objects_list.append(obj_data)

            data["objects"] = objects_list

        return data

    class Config:
        extra = "allow"


class Space(BaseModel):
    """Gather.town space information."""

    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    moderatorAccess: Optional[bool] = None
    builderAccess: Optional[bool] = None

    class Config:
        extra = "allow"
