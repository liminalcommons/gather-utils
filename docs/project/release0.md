# Creating a Sophisticated Python Environment for Gather.town API Exploration

A truly sophisticated Python environment goes beyond basic scripts to embrace professional software engineering practices. Let's design a robust environment for our Gather.town exploration project:

## Comprehensive Environment Setup

### 1. Modern Project Structure
```
gather-town-manager/
├── .github/                  # GitHub workflows and templates
├── src/                      # Source code
│   └── gather_manager/       # Main package
│       ├── __init__.py       # Package initialization
│       ├── api/              # API interaction layer
│       ├── models/           # Data models/schemas
│       ├── services/         # Business logic
│       ├── cli/              # Command-line interface
│       └── utils/            # Utility functions
├── tests/                    # Test suite
│   ├── conftest.py           # Test configuration
│   ├── test_api/             # API tests
│   └── test_services/        # Service tests
├── docs/                     # Documentation
├── examples/                 # Example usage
├── .env.example              # Example environment variables
├── pyproject.toml           # Project dependencies and metadata (Poetry)
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
└── README.md                # Project documentation
```

### 2. Dependency Management with Poetry
Poetry provides a modern approach to Python package management with dependency resolution, virtual environments, and package building capabilities:

```toml
# pyproject.toml
[tool.poetry]
name = "gather-manager"
version = "0.1.0"
description = "Tools for managing Gather.town spaces and containers"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.2"
pydantic = "^2.3.0"
typer = "^0.9.0"
rich = "^13.4.2"
python-dotenv = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.1"
pytest-cov = "^4.1.0"
black = "^23.3.0"
isort = "^5.12.0"
mypy = "^1.3.0"
flake8 = "^6.0.0"
pre-commit = "^3.3.2"
pytest-mock = "^3.10.0"
responses = "^0.23.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
gather-manager = "gather_manager.cli.main:app"
```

### 3. Code Quality Configuration

#### Type Checking with MyPy
```toml
# pyproject.toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

#### Code Formatting with Black & isort
```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39']

[tool.isort]
profile = "black"
multi_line_output = 3
```

#### Pre-commit Configuration
```yaml
# .pre-commit-config.yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    -   id: isort

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-docstrings]
```

## Core Implementation Files

### 1. API Client Module
```python
# src/gather_manager/api/client.py
from typing import Any, Dict, List, Optional, Union
import os
import logging
import requests
from pydantic import BaseModel

from gather_manager.models.space import Space, Map, MapData, Object
from gather_manager.utils.exceptions import GatherApiError

logger = logging.getLogger(__name__)

class GatherClient:
    """Client for interacting with the Gather.town API."""
    
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://gather.town/api"):
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
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
    
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
        data = self._request("GET", f"v2/spaces/{space_id}")
        return Space.model_validate(data)
    
    def get_maps(self, space_id: str) -> List[Map]:
        """Get list of maps in a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            List of maps
        """
        data = self._request("GET", f"v2/spaces/{space_id}/maps")
        return [Map.model_validate(map_data) for map_data in data]
    
    def get_map_data(self, space_id: str, map_id: str) -> MapData:
        """Get detailed data for a specific map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            Map data including objects
        """
        data = self._request("GET", f"v2/spaces/{space_id}/maps/{map_id}")
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
```

### 2. Data Models
```python
# src/gather_manager/models/space.py
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field

class Position(BaseModel):
    """Position with x and y coordinates."""
    x: int
    y: int

class Portal(BaseModel):
    """Portal object properties."""
    type: str = "portal"
    x: int
    y: int
    width: int = 1
    height: int = 1
    targetMap: str
    targetX: int
    targetY: int
    # Add other properties as discovered

class Object(BaseModel):
    """Base model for map objects."""
    id: Optional[str] = None
    type: str
    x: int
    y: int
    width: Optional[int] = 1
    height: Optional[int] = 1
    properties: Optional[Dict[str, Any]] = None
    # Include other common fields, extend as needed

class Map(BaseModel):
    """Map information."""
    id: str
    name: Optional[str] = None
    description: Optional[str] = None

class MapData(BaseModel):
    """Detailed map data including objects."""
    id: str
    name: Optional[str] = None
    objects: List[Object] = Field(default_factory=list)
    # Add other map properties as discovered

class Space(BaseModel):
    """Gather.town space information."""
    id: str
    name: Optional[str] = None
    # Add other space properties as discovered
```

### 3. Custom Exceptions
```python
# src/gather_manager/utils/exceptions.py
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
```

### 4. Portal Explorer Service
```python
# src/gather_manager/services/explorer.py
import json
import os
import logging
from typing import Dict, List, Optional, Any

from gather_manager.api.client import GatherClient
from gather_manager.models.space import Object

logger = logging.getLogger(__name__)

class PortalExplorer:
    """Service for exploring and analyzing portal structures in Gather.town."""
    
    def __init__(self, client: Optional[GatherClient] = None, output_dir: str = "data"):
        """Initialize with optional client and output directory.
        
        Args:
            client: GatherClient instance or None to create a new one
            output_dir: Directory to store output data
        """
        self.client = client or GatherClient()
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def analyze_map_portals(self, space_id: str, map_id: str) -> List[Object]:
        """Analyze portal structures in a specific map.
        
        Args:
            space_id: ID of the space
            map_id: ID of the map
            
        Returns:
            List of portal objects
        """
        logger.info(f"Analyzing portals in map {map_id} of space {space_id}")
        
        # Get all portals in the map
        portals = self.client.get_portals(space_id, map_id)
        
        if not portals:
            logger.info(f"No portals found in map {map_id}")
            return []
        
        logger.info(f"Found {len(portals)} portals in map {map_id}")
        
        # Save portals to file
        self._save_to_json(
            data=portals,
            filename=f"portals_{map_id}.json",
            message=f"Saved {len(portals)} portals from map {map_id}"
        )
        
        # Get full map data for context
        map_data = self.client.get_map_data(space_id, map_id)
        self._save_to_json(
            data=map_data.model_dump(),
            filename=f"map_{map_id}.json",
            message=f"Saved full map data for {map_id}"
        )
        
        return portals
    
    def analyze_all_maps(self, space_id: str) -> Dict[str, List[Object]]:
        """Analyze portals in all maps of a space.
        
        Args:
            space_id: ID of the space
            
        Returns:
            Dictionary mapping map IDs to lists of portal objects
        """
        logger.info(f"Analyzing all maps in space {space_id}")
        
        # Get all maps in the space
        maps = self.client.get_maps(space_id)
        logger.info(f"Found {len(maps)} maps in space {space_id}")
        
        # Save maps list
        self._save_to_json(
            data=[m.model_dump() for m in maps],
            filename=f"maps_list_{space_id}.json",
            message=f"Saved list of {len(maps)} maps"
        )
        
        # Analyze portals in each map
        results = {}
        for map_obj in maps:
            map_id = map_obj.id
            portals = self.analyze_map_portals(space_id, map_id)
            results[map_id] = portals
        
        # Save summary
        summary = {
            map_id: len(portals) 
            for map_id, portals in results.items()
        }
        
        self._save_to_json(
            data=summary,
            filename=f"portal_summary_{space_id}.json",
            message=f"Saved portal summary for all maps"
        )
        
        return results
    
    def _save_to_json(self, data: Any, filename: str, message: Optional[str] = None):
        """Save data to a JSON file in the output directory.
        
        Args:
            data: Data to save
            filename: Name of the file
            message: Optional message to log after saving
        """
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        if message:
            logger.info(f"{message} to {filepath}")
```

### 5. Command Line Interface
```python
# src/gather_manager/cli/main.py
import os
import typer
import logging
from rich.console import Console
from rich.logging import RichHandler
from typing import Optional

from gather_manager.services.explorer import PortalExplorer
from gather_manager.api.client import GatherClient
from gather_manager.utils.exceptions import GatherManagerError

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger("gather_manager")
console = Console()
app = typer.Typer()

@app.callback()
def callback():
    """
    Gather.town Manager - Tool for exploring and managing Gather.town spaces
    """
    pass

@app.command()
def explore(
    space_id: str = typer.Option(
        ..., 
        envvar="GATHER_SPACE_ID",
        help="Gather.town space ID to explore"
    ),
    map_id: Optional[str] = typer.Option(
        None,
        help="Specific map ID to analyze (analyzes all maps if not specified)"
    ),
    output_dir: str = typer.Option(
        "data",
        help="Directory to store output data"
    )
):
    """
    Explore and analyze portal structures in Gather.town spaces.
    """
    try:
        explorer = PortalExplorer(output_dir=output_dir)
        
        if map_id:
            console.print(f"[bold]Analyzing portals in map:[/] {map_id}")
            portals = explorer.analyze_map_portals(space_id, map_id)
            console.print(f"[green]Found {len(portals)} portals[/]")
        else:
            console.print(f"[bold]Analyzing all maps in space:[/] {space_id}")
            results = explorer.analyze_all_maps(space_id)
            total_portals = sum(len(portals) for portals in results.values())
            console.print(f"[green]Analyzed {len(results)} maps, found {total_portals} portals total[/]")
        
        console.print(f"[bold]Results saved to:[/] {output_dir}/")
    
    except GatherManagerError as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/] {str(e)}")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(code=1)

@app.command()
def list_maps(
    space_id: str = typer.Option(
        ..., 
        envvar="GATHER_SPACE_ID",
        help="Gather.town space ID"
    )
):
    """
    List all maps in a Gather.town space.
    """
    try:
        client = GatherClient()
        maps = client.get_maps(space_id)
        
        console.print(f"[bold]Maps in space {space_id}:[/]")
        for i, map_obj in enumerate(maps, 1):
            console.print(f"{i}. [cyan]{map_obj.id}[/] - {map_obj.name or 'Unnamed'}")
    
    except GatherManagerError as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
        raise typer.Exit(code=1)
```

### 6. Package Initialization
```python
# src/gather_manager/__init__.py
"""Tools for exploring and managing Gather.town spaces and containers."""

__version__ = "0.1.0"
```

## Testing Setup

### 1. Test Configuration
```python
# tests/conftest.py
import pytest
import os
import json
from pathlib import Path
from typing import Dict, Any

from gather_manager.api.client import GatherClient

# Test data directory
TEST_DATA_DIR = Path(__file__).parent / "data"

@pytest.fixture
def mock_api_key():
    """Fixture to provide a mock API key."""
    return "test_api_key_12345"

@pytest.fixture
def sample_portal_data() -> Dict[str, Any]:
    """Fixture to provide sample portal data."""
    portal_path = TEST_DATA_DIR / "sample_portal.json"
    with open(portal_path, "r") as f:
        return json.load(f)

@pytest.fixture
def sample_map_data() -> Dict[str, Any]:
    """Fixture to provide sample map data."""
    map_path = TEST_DATA_DIR / "sample_map.json"
    with open(map_path, "r") as f:
        return json.load(f)
```

### 2. API Tests
```python
# tests/test_api/test_client.py
import pytest
import responses
from gather_manager.api.client import GatherClient
from gather_manager.utils.exceptions import GatherApiError

@pytest.fixture
def client(mock_api_key):
    """Fixture to provide a GatherClient instance."""
    return GatherClient(api_key=mock_api_key)

class TestGatherClient:
    
    def test_init_without_api_key(self):
        """Test initialization fails without API key."""
        with pytest.raises(ValueError, match="API key is required"):
            GatherClient(api_key=None)
    
    @responses.activate
    def test_get_space(self, client, sample_map_data):
        """Test getting space information."""
        # Mock API response
        responses.add(
            responses.GET,
            "https://gather.town/api/v2/spaces/test-space",
            json={"id": "test-space", "name": "Test Space"},
            status=200
        )
        
        space = client.get_space("test-space")
        assert space.id == "test-space"
        assert space.name == "Test Space"
    
    @responses.activate
    def test_get_maps(self, client):
        """Test getting list of maps."""
        # Mock API response
        responses.add(
            responses.GET,
            "https://gather.town/api/v2/spaces/test-space/maps",
            json=[
                {"id": "map1", "name": "Map 1"},
                {"id": "map2", "name": "Map 2"}
            ],
            status=200
        )
        
        maps = client.get_maps("test-space")
        assert len(maps) == 2
        assert maps[0].id == "map1"
        assert maps[1].name == "Map 2"
    
    @responses.activate
    def test_get_portals(self, client, sample_map_data):
        """Test getting portals from a map."""
        # Create sample map data with portals
        map_data = {
            "id": "test-map",
            "objects": [
                {"id": "obj1", "type": "portal", "x": 10, "y": 20, "targetMap": "map2", "targetX": 5, "targetY": 5},
                {"id": "obj2", "type": "image", "x": 15, "y": 25},
                {"id": "obj3", "type": "portal", "x": 30, "y": 40, "targetMap": "map3", "targetX": 1, "targetY": 1}
            ]
        }
        
        # Mock API response
        responses.add(
            responses.GET,
            "https://gather.town/api/v2/spaces/test-space/maps/test-map",
            json=map_data,
            status=200
        )
        
        portals = client.get_portals("test-space", "test-map")
        assert len(portals) == 2
        assert portals[0].type == "portal"
        assert portals[0].targetMap == "map2"
        assert portals[1].targetMap == "map3"
```

## Usage Examples

### 1. Basic Usage
```python
# examples/basic_exploration.py
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
        logger.info("Analysis results saved to data directory")

if __name__ == "__main__":
    main()
```

## Installation and Setup Instructions

1. **Install Python 3.9+ and Poetry**
   ```bash
   # Install Poetry if you don't have it
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone and setup the project**
   ```bash
   # Clone the repository (or create from scratch)
   git clone <repository-url>
   cd gather-town-manager
   
   # Install dependencies with Poetry
   poetry install
   
   # Activate the virtual environment
   poetry shell
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file from template
   cp .env.example .env
   
   # Edit .env with your API key and space ID
   # GATHER_API_KEY=your_api_key_here
   # GATHER_SPACE_ID=your_space_id_here
   ```

4. **Run the CLI tool**
   ```bash
   # List maps in your space
   gather-manager list-maps
   
   # Explore portals in all maps
   gather-manager explore
   
   # Explore portals in a specific map
   gather-manager explore --map-id=your_map_id
   ```

5. **Examine the results**
   ```bash
   # Check the data directory for JSON files with results
   ls -la data/
   ```

This sophisticated environment provides a solid foundation for exploring the Gather.town API and developing your container management system. The modular design, proper testing, and good practices make it extensible and maintainable as your project grows.