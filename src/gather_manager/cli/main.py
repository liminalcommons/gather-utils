"""Command line interface for the Gather.town API Explorer."""

import configparser
import os
import sys
from pathlib import Path

from dotenv import load_dotenv


# Load environment variables from .env files in multiple locations
def load_environment():
    """
    Load environment variables from .env files in the following order of precedence:
    1. .env file in the current directory
    2. .env file in the user's home directory (~/.gather-manager/.env)
    """
    # Load from current directory first
    load_dotenv()

    # Then try to load from user's home directory
    home_env_path = Path.home() / ".gather-manager" / ".env"
    if home_env_path.exists():
        load_dotenv(dotenv_path=home_env_path)


# Load configuration from config file
def load_config():
    """
    Load configuration from ~/.gather-manager/config.ini
    This sets environment variables for API key and space ID if they're not already set.
    """
    config = configparser.ConfigParser()
    config_path = Path.home() / ".gather-manager" / "config.ini"

    if config_path.exists():
        config.read(config_path)
        if "gather" in config and "api_key" in config["gather"]:
            os.environ.setdefault(
                "GATHER_API_KEY", config["gather"]["api_key"]
            )
        if "gather" in config and "space_id" in config["gather"]:
            os.environ.setdefault(
                "GATHER_SPACE_ID", config["gather"]["space_id"]
            )


# Load environment variables and configuration
# Order of precedence:
# 1. Command line arguments (handled by Typer)
# 2. Environment variables (from .env files)
# 3. Configuration file
load_environment()
load_config()

import logging
from typing import List, Optional

import typer
from rich.console import Console
from rich.logging import RichHandler
from rich.prompt import Confirm, Prompt
from rich.table import Table

from gather_manager import __version__
from gather_manager.api.client import GatherClient
from gather_manager.services import PortalService
from gather_manager.services.explorer import PortalExplorer
from gather_manager.utils.exceptions import GatherApiError, GatherManagerError

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("gather_manager")
console = Console()
app = typer.Typer()

# Create a sub-app for portal commands
portals_app = typer.Typer(help="Commands for analyzing portals")
app.add_typer(portals_app, name="portals")


def version_callback(value: bool):
    if value:
        console.print(f"gather-manager version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    )
):
    """
    Gather.town API Explorer - Tool for analyzing portal structures in Gather.town spaces
    """
    pass


@app.command()
def explore(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID to explore"
    ),
    map_id: Optional[str] = typer.Option(
        None,
        help="Specific map ID to analyze (analyzes all maps if not specified)",
    ),
    output_dir: str = typer.Option(
        "data", help="Directory to store output data"
    ),
    analyze_properties: bool = typer.Option(
        False,
        "--analyze-properties",
        "-p",
        help="Perform detailed analysis of portal properties",
    ),
):
    """
    Explore and analyze portal structures in Gather.town spaces.
    """
    try:
        explorer = PortalExplorer(output_dir=output_dir)

        # Check access to the space first
        if not explorer.check_space_access(space_id):
            console.print(
                f"[bold red]Error:[/] Cannot access space {space_id}. Please check your API key and permissions."
            )
            raise typer.Exit(code=1)

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
            console.print(
                f"[green]Analyzed {len(results)} maps, found {total_portals} portals total[/]"
            )

            # If requested, perform detailed property analysis
            if analyze_properties and total_portals > 0:
                console.print(
                    "\n[bold]Performing detailed portal property analysis...[/]"
                )
                analysis = explorer.analyze_portal_properties(space_id)

                # Display property frequency
                if "property_frequency" in analysis:
                    table = Table(title="Portal Properties")
                    table.add_column("Property", style="cyan")
                    table.add_column("Count", justify="right")
                    table.add_column("Percentage", justify="right")

                    for prop, data in analysis["property_frequency"].items():
                        table.add_row(
                            prop, str(data["count"]), f"{data['percentage']}%"
                        )

                    console.print(table)

                # Display directional analysis if available
                if (
                    "directional_analysis" in analysis
                    and analysis["directional_analysis"]
                ):
                    console.print(
                        "\n[bold]Directional Properties Analysis:[/]"
                    )
                    for prop, data in analysis["directional_analysis"].items():
                        appears = (
                            "[green]Yes[/]"
                            if data["appears_directional"]
                            else "[red]No[/]"
                        )
                        console.print(
                            f"  [cyan]{prop}[/] appears directional: {appears}"
                        )
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
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
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
                str(i), map_obj.id, map_obj.name or "[dim]Unnamed[/dim]"
            )

        console.print(table)

    except GatherApiError as e:
        console.print(f"[bold red]API Error:[/] {str(e)}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/] {str(e)}")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(code=1)


@app.command()
def list_spaces(
    role: Optional[str] = typer.Option(
        None, help="Filter spaces by role (ADMIN, BUILDER, MEMBER, MODERATOR)"
    )
):
    """
    List all spaces accessible with your API key.
    """
    try:
        client = GatherClient()

        # Map role string to role constant if provided
        if role:
            role_upper = role.upper()
            role_constants = {
                "ADMIN": client.ROLE_ADMIN,
                "BUILDER": client.ROLE_BUILDER,
                "MEMBER": client.ROLE_MEMBER,
                "MODERATOR": client.ROLE_MODERATOR,
            }

            if role_upper not in role_constants:
                console.print(
                    f"[bold yellow]Warning:[/] Unknown role '{role}'. Using as-is."
                )
                role_to_use = role
            else:
                role_to_use = role_constants[role_upper]
        else:
            role_to_use = None

        spaces = client.get_spaces(role=role_to_use)

        if not spaces:
            console.print(
                f"[yellow]No spaces found{' with role ' + role if role else ''}[/]"
            )
            return

        table = Table(
            title=f"Accessible Spaces{' (Role: ' + role + ')' if role else ''}"
        )
        table.add_column("#", style="dim")
        table.add_column("Space ID", style="cyan")
        table.add_column("Name")

        for i, space in enumerate(spaces, 1):
            table.add_row(
                str(i),
                space.get("id", "Unknown"),
                space.get("name", "[dim]Unnamed[/dim]"),
            )

        console.print(table)
        console.print(f"\n[green]Found {len(spaces)} spaces[/]")

    except GatherApiError as e:
        console.print(f"[bold red]API Error:[/] {str(e)}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/] {str(e)}")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(code=1)


@app.command()
def manage_users(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    list_users: bool = typer.Option(
        False, "--list", "-l", help="List users in the space"
    ),
    add_user: bool = typer.Option(
        False, "--add", "-a", help="Add a user to the space"
    ),
    remove_user: bool = typer.Option(
        False, "--remove", "-r", help="Remove a user from the space"
    ),
    email: Optional[str] = typer.Option(
        None, help="Email of the user to add or remove"
    ),
    role: Optional[str] = typer.Option(
        "MEMBER",
        help="Role to assign to the user (ADMIN, BUILDER, MEMBER, MODERATOR)",
    ),
):
    """
    Manage users in a Gather.town space.
    """
    try:
        client = GatherClient()

        # Map role string to role constant
        role_upper = role.upper() if role else "MEMBER"
        role_constants = {
            "ADMIN": client.ROLE_ADMIN,
            "BUILDER": client.ROLE_BUILDER,
            "MEMBER": client.ROLE_MEMBER,
            "MODERATOR": client.ROLE_MODERATOR,
        }

        if role_upper not in role_constants:
            console.print(
                f"[bold yellow]Warning:[/] Unknown role '{role}'. Using as-is."
            )
            role_to_use = role
        else:
            role_to_use = role_constants[role_upper]

        # List users
        if list_users:
            console.print(f"[bold]Listing users in space:[/] {space_id}")
            users = client.get_space_users(space_id)

            if not users:
                console.print("[yellow]No users found in this space[/]")
                return

            table = Table(title=f"Users in space {space_id}")
            table.add_column("#", style="dim")
            table.add_column("User ID", style="cyan")
            table.add_column("Name")
            table.add_column("Email")
            table.add_column("Roles")

            for i, user in enumerate(users, 1):
                table.add_row(
                    str(i),
                    user.get("id", "Unknown"),
                    user.get("name", "[dim]Unknown[/dim]"),
                    user.get("email", "[dim]Unknown[/dim]"),
                    ", ".join(user.get("roles", [])),
                )

            console.print(table)
            console.print(f"\n[green]Found {len(users)} users[/]")
            return

        # Add user
        if add_user:
            if not email:
                email = Prompt.ask("[bold]Enter user email")

            console.print(
                f"[bold]Adding user[/] {email} to space {space_id} with role {role_upper}"
            )
            client.add_user_to_space(space_id, email, role=role_to_use)
            console.print(
                f"[green]Successfully added user {email} with role {role_upper}[/]"
            )
            return

        # Remove user
        if remove_user:
            if not email:
                email = Prompt.ask("[bold]Enter user email")

            if Confirm.ask(
                f"[bold yellow]Are you sure you want to remove user {email} from space {space_id}?[/]"
            ):
                console.print(
                    f"[bold]Removing user[/] {email} from space {space_id}"
                )
                client.remove_user_from_space(space_id, email)
                console.print(f"[green]Successfully removed user {email}[/]")
            return

        # If no operation specified, show help
        console.print(
            "[yellow]Please specify an operation: --list, --add, or --remove[/]"
        )

    except GatherApiError as e:
        console.print(f"[bold red]API Error:[/] {str(e)}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/] {str(e)}")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(code=1)


@app.command()
def create_spawn_token(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    map_id: str = typer.Option(
        ..., help="ID of the map containing the spawn point"
    ),
    spawn_name: str = typer.Option(..., help="Name of the spawn point"),
    expires_in: Optional[int] = typer.Option(
        None, help="Expiration time in seconds"
    ),
):
    """
    Create a spawn token for a specific spawn point in a map.
    """
    try:
        client = GatherClient()

        console.print(
            f"[bold]Creating spawn token for[/] {spawn_name} in map {map_id}"
        )
        result = client.create_spawn_token(
            space_id, map_id, spawn_name, expires_in_seconds=expires_in
        )

        console.print(f"[green]Successfully created spawn token:[/]")
        console.print(
            f"  [cyan]Token:[/] {result.get('spawnToken', 'Unknown')}"
        )
        if "url" in result:
            console.print(f"  [cyan]URL:[/] {result.get('url')}")
        if expires_in:
            console.print(f"  [cyan]Expires:[/] In {expires_in} seconds")

    except GatherApiError as e:
        console.print(f"[bold red]API Error:[/] {str(e)}")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]Unexpected error:[/] {str(e)}")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(code=1)


@portals_app.command("validate")
def validate_portals(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    api_key: str = typer.Option(
        ..., envvar="GATHER_API_KEY", help="Gather.town API key"
    ),
):
    """Validate portals across all maps in a space."""
    console = Console()

    with console.status("Validating portals..."):
        # Create API client
        api_client = GatherClient(api_key=api_key)

        # Create portal service
        portal_service = PortalService(api_client=api_client)

        # Validate portals
        validation_result = portal_service.validate_portals()

    # Display valid portals
    console.print("\n[bold green]Valid Portals:[/bold green]")
    if validation_result["valid_portals"]:
        table = Table(show_header=True)
        table.add_column("ID")
        table.add_column("Map")
        table.add_column("Position")
        table.add_column("Destination")

        for portal in validation_result["valid_portals"]:
            table.add_row(
                portal["id"],
                portal["map_id"],
                f"({portal['x']}, {portal['y']})",
                f"{portal['target_map']} ({portal['target_x']}, {portal['target_y']})",
            )

        console.print(table)
    else:
        console.print("[italic]No valid portals found.[/italic]")

    # Display invalid portals
    console.print("\n[bold red]Invalid Portals:[/bold red]")
    if validation_result["invalid_portals"]:
        table = Table(show_header=True)
        table.add_column("ID")
        table.add_column("Map")
        table.add_column("Position")
        table.add_column("Reason")

        for portal in validation_result["invalid_portals"]:
            table.add_row(
                portal["id"],
                portal["map_id"],
                f"({portal.get('x', '?')}, {portal.get('y', '?')})",
                portal["reason"],
            )

        console.print(table)
    else:
        console.print("[italic]No invalid portals found.[/italic]")


@portals_app.command("connections")
def analyze_connections(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    api_key: str = typer.Option(
        ..., envvar="GATHER_API_KEY", help="Gather.town API key"
    ),
):
    """Analyze portal connections between maps."""
    console = Console()

    with console.status("Analyzing portal connections..."):
        # Create API client
        api_client = GatherClient(api_key=api_key)

        # Create portal service
        portal_service = PortalService(api_client=api_client)

        # Analyze connections
        connections = portal_service.analyze_connections()

    # Display connections
    console.print("\n[bold blue]Map Connections:[/bold blue]")
    if connections:
        table = Table(show_header=True)
        table.add_column("Source Map")
        table.add_column("Destination Map")
        table.add_column("Portal Count")

        for connection in connections:
            portal_count = connection["portal_count"]
            portal_text = (
                f"{portal_count} portal{'s' if portal_count != 1 else ''}"
            )

            table.add_row(
                connection["source_map"],
                connection["destination_map"],
                portal_text,
            )

        console.print(table)
    else:
        console.print("[italic]No connections found between maps.[/italic]")


@portals_app.command("details")
def portal_details(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    api_key: str = typer.Option(
        ..., envvar="GATHER_API_KEY", help="Gather.town API key"
    ),
    map_id: str = typer.Option(
        ..., help="ID of the map to get portal details for"
    ),
):
    """View detailed information about portals in a specific map."""
    console = Console()

    with console.status(f"Getting portal details for {map_id}..."):
        # Create API client
        api_client = GatherClient(api_key=api_key)

        # Create portal service
        portal_service = PortalService(api_client=api_client)

        # Get portal details
        portal_details = portal_service.get_portal_details(map_id=map_id)

    # Display portal details
    console.print(f"\n[bold]Portal Details for {map_id}:[/bold]")
    if portal_details:
        for portal in portal_details:
            console.print(f"\n[bold cyan]Portal: {portal['id']}[/bold cyan]")
            console.print(f"Position: ({portal['x']}, {portal['y']})")

            if portal.get("is_valid", False):
                console.print(
                    f"Destination: {portal['target_map']} ({portal['target_x']}, {portal['target_y']})"
                )
                console.print("Valid: [green]Yes[/green]")
            else:
                if "target_map" in portal and portal["target_map"] is not None:
                    console.print(
                        f"Destination: {portal['target_map']} ({portal.get('target_x', '?')}, {portal.get('target_y', '?')})"
                    )
                else:
                    console.print(
                        "Destination: [italic]Not specified[/italic]"
                    )

                console.print("Valid: [red]No[/red]")
                if "error" in portal:
                    console.print(f"Error: {portal['error']}")
                elif "reason" in portal:
                    console.print(f"Reason: {portal['reason']}")
    else:
        console.print("[italic]No portals found in this map.[/italic]")


@portals_app.command("export")
def export_portals(
    space_id: str = typer.Option(
        ..., envvar="GATHER_SPACE_ID", help="Gather.town space ID"
    ),
    api_key: str = typer.Option(
        ..., envvar="GATHER_API_KEY", help="Gather.town API key"
    ),
    format: str = typer.Option("json", help="Export format (json or csv)"),
    output_dir: str = typer.Option(
        "data", help="Directory to store output data"
    ),
):
    """Export portal data to a file."""
    console = Console()

    with console.status(
        f"Exporting portal data to {format.upper()} format..."
    ):
        # Create API client
        api_client = GatherClient(api_key=api_key)

        # Create portal service
        portal_service = PortalService(api_client=api_client)

        # Export portals
        file_path = portal_service.export_portals(
            format=format, output_dir=output_dir
        )

    console.print(f"\nPortal data exported to [bold]{file_path}[/bold]")


if __name__ == "__main__":
    app()
