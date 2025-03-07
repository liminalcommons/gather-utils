#!/usr/bin/env python3
"""Basic example of using the Gather.town API Explorer."""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv

from gather_manager.api.client import GatherClient
from gather_manager.services.explorer import PortalExplorer

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Run a basic exploration of a Gather.town space."""
    # Get API key and space ID from environment
    api_key = os.getenv("GATHER_API_KEY")
    space_id = os.getenv("GATHER_SPACE_ID")
    
    if not api_key or not space_id:
        logger.error("GATHER_API_KEY and GATHER_SPACE_ID must be set")
        return
    
    # Create API client
    client = GatherClient(api_key=api_key)
    
    # List maps in the space
    logger.info(f"Listing maps in space {space_id}")
    maps = client.get_maps(space_id)
    
    for i, map_obj in enumerate(maps, 1):
        logger.info(f"{i}. {map_obj.id} - {map_obj.name or 'Unnamed'}")
    
    # If maps exist, analyze the first one
    if maps:
        map_id = maps[0].id
        logger.info(f"Analyzing portals in map: {map_id}")
        
        explorer = PortalExplorer(client=client)
        portals = explorer.analyze_map_portals(space_id, map_id)
        
        logger.info(f"Found {len(portals)} portals in map {map_id}")
        
        # Display a sample portal if available
        if portals:
            sample = portals[0]
            logger.info(f"Sample portal: {sample.model_dump()}")
        
        logger.info("Analysis results saved to data directory")


if __name__ == "__main__":
    main() 