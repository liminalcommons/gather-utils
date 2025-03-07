"""Command line interface for the Gather.town API Explorer."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import typer
import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
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
    Gather.town API Explorer - Tool for analyzing portal structures in Gather.town spaces
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
    ),
    analyze_properties: bool = typer.Option(
        False,
        "--analyze-properties", "-p",
        help="Perform detailed analysis of portal properties"
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
            
            if portals:
                # Display a sample portal
                console.print("\n[bold]Sample portal structure:[/]")
                sample = portals[0].model_dump(exclude_none=False)
                for key, value in sample.items():
                    console.print(f"  [cyan]{key}:[/] {value}")
        else:
            console.print(f"[bold]Analyzing all maps in space:[/] {space_id}")
            results = explorer.analyze_all_maps(space_id)
            total_portals = sum(len(portals) for portals in results.values())
            console.print(f"[green]Analyzed {len(results)} maps, found {total_portals} portals total[/]")
            
            # If requested, perform detailed property analysis
            if analyze_properties and total_portals > 0:
                console.print("\n[bold]Performing detailed portal property analysis...[/]")
                analysis = explorer.analyze_portal_properties(space_id)
                
                # Display property frequency
                if "property_frequency" in analysis:
                    table = Table(title="Portal Properties")
                    table.add_column("Property", style="cyan")
                    table.add_column("Count", justify="right")
                    table.add_column("Percentage", justify="right")
                    
                    for prop, data in analysis["property_frequency"].items():
                        table.add_row(
                            prop,
                            str(data["count"]),
                            f"{data['percentage']}%"
                        )
                    
                    console.print(table)
                
                # Display directional analysis if available
                if "directional_analysis" in analysis and analysis["directional_analysis"]:
                    console.print("\n[bold]Directional Properties Analysis:[/]")
                    for prop, data in analysis["directional_analysis"].items():
                        appears = "[green]Yes[/]" if data["appears_directional"] else "[red]No[/]"
                        console.print(f"  [cyan]{prop}[/] appears directional: {appears}")
                        console.print(f"    Values: {data['values']}")
        
        console.print(f"\n[bold]Results saved to:[/] {explorer.session_dir}/")
    
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
        
        if not maps:
            console.print(f"[yellow]No maps found in space {space_id}[/]")
            return
        
        table = Table(title=f"Maps in space {space_id}")
        table.add_column("#", style="dim")
        table.add_column("Map ID", style="cyan")
        table.add_column("Name")
        
        for i, map_obj in enumerate(maps, 1):
            table.add_row(
                str(i),
                map_obj.id,
                map_obj.name or "[dim]Unnamed[/dim]"
            )
        
        console.print(table)
    
    except GatherManagerError as e:
        console.print(f"[bold red]Error:[/] {str(e)}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app() 