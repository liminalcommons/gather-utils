"""
Portal model for representing Gather.town portals.
"""
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class PortalProperties(BaseModel):
    """Properties specific to portal objects."""
    target_map: Optional[str] = Field(None, alias="targetMap")
    target_x: Optional[int] = Field(None, alias="targetX")
    target_y: Optional[int] = Field(None, alias="targetY")
    normal: Optional[bool] = None
    
    class Config:
        """Pydantic model configuration."""
        populate_by_name = True


class Portal(BaseModel):
    """Model representing a portal in Gather.town."""
    id: str
    type: int
    x: int
    y: int
    properties: PortalProperties
    
    class Config:
        """Pydantic model configuration."""
        populate_by_name = True
    
    def is_valid(self) -> bool:
        """
        Check if the portal has all required properties to be valid.
        
        Returns:
            bool: True if the portal is valid, False otherwise.
        """
        return (
            self.properties.target_map is not None and
            self.properties.target_x is not None and
            self.properties.target_y is not None
        )
    
    def get_destination(self) -> Dict[str, Any]:
        """
        Get the destination of the portal.
        
        Returns:
            Dict[str, Any]: A dictionary containing the destination map ID and coordinates.
        """
        return {
            "map_id": self.properties.target_map,
            "x": self.properties.target_x,
            "y": self.properties.target_y
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the portal to a dictionary.
        
        Returns:
            Dict[str, Any]: A dictionary representation of the portal.
        """
        return {
            "id": self.id,
            "type": self.type,
            "x": self.x,
            "y": self.y,
            "target_map": self.properties.target_map,
            "target_x": self.properties.target_x,
            "target_y": self.properties.target_y,
            "is_valid": self.is_valid()
        } 