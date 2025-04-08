#!/usr/bin/env python3
"""
Tool: Tool Inventory Manager
Created: 2024-03-21
Author: Development Team
Status: Active
Purpose: Inventory, evaluate, and manage tools in the codebase
Dependencies: pandas, tabulate
Lifecycle:
    - Created: To address the need for better tool organization and discovery
    - Active: Used for managing tool lifecycle and metadata
    - Obsolescence Conditions:
        1. When replaced by a more comprehensive tool management system
        2. When project tooling approach changes significantly
Last Validated: 2024-03-21

This tool helps inventory, evaluate, and manage the lifecycle of tools in the codebase.
It allows users to:
1. Generate an inventory of all tools with their metadata
2. Evaluate tools based on their usage and relevance
3. Find the right tools for specific tasks using search
4. Archive or delete obsolete tools
5. Validate tool metadata compliance
"""

import argparse
import glob
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import pandas as pd
    from tabulate import tabulate
except ImportError:
    print("Required dependencies not found. Install with:")
    print("poetry install")
    sys.exit(1)

# Constants
TOOLS_DIR = "tools"
ARCHIVE_DIR = os.path.join(TOOLS_DIR, "archive")
REPORTS_DIR = "reports/tool_inventory"
CATEGORIES = [
    "Core Tools",
    "Feature-specific Tools",
    "One-off Tools",
    "Analysis Tools",
    "CI/CD Tools",
]
METADATA_PATTERN = r'"""[\s\S]*?Tool:[\s\S]*?(?:"""|\n\n)'
REQUIRED_METADATA_FIELDS = [
    "Tool",
    "Created",
    "Author",
    "Status",
    "Purpose",
    "Dependencies",
    "Lifecycle",
    "Last Validated",
]
VALID_STATUS_VALUES = ["Active", "Deprecated", "Archived"]

# ANSI color codes for terminal output
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def find_tools() -> List[str]:
    """
    Find all Python tool files in the tools directory.

    Returns:
        List[str]: A list of paths to tool files.
    """
    tools = []

    # Find all Python files in tools directory
    for root, _, files in os.walk(TOOLS_DIR):
        for file in files:
            if file.endswith(".py"):
                tools.append(os.path.join(root, file))

    return tools


def extract_metadata(file_path: str) -> Optional[str]:
    """
    Extract metadata docstring from a tool file.

    Args:
        file_path (str): Path to the tool file.

    Returns:
        Optional[str]: Extracted metadata string or None if not found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find docstring that has metadata
        match = re.search(METADATA_PATTERN, content)
        if match:
            metadata_str = match.group(0)
            return metadata_str

        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def parse_metadata(metadata_str: str) -> Dict[str, Any]:
    """
    Parse metadata string into a dictionary.

    Args:
        metadata_str (str): The metadata string to parse.

    Returns:
        Dict[str, Any]: Dictionary of metadata fields.
    """
    metadata = {}
    if not metadata_str:
        return metadata

    # Extract lines from docstring
    lines = metadata_str.split("\n")
    current_field = None
    in_lifecycle = False
    lifecycle_data = {
        "Created": "",
        "Active": "",
        "Obsolescence Conditions": [],
    }

    for line in lines:
        line = line.strip()

        # Look for Tool: line - special case for tool name
        if line.startswith("Tool:"):
            metadata["Tool"] = line[5:].strip()
            continue

        # Main metadata fields with colon
        if (
            ":" in line
            and not line.startswith("-")
            and not line.startswith("#")
        ):
            parts = line.split(":", 1)
            if len(parts) == 2:
                key, value = parts
                key = key.strip()
                value = value.strip()

                if key == "Lifecycle":
                    in_lifecycle = True
                    continue
                elif (
                    key in ["Created", "Last Updated", "Last Validated"]
                    and len(value) >= 10
                ):
                    # For date fields, extract YYYY-MM-DD
                    if (
                        value[0:4].isdigit()
                        and value[5:7].isdigit()
                        and value[8:10].isdigit()
                    ):
                        metadata[key] = value[0:10]
                    else:
                        metadata[key] = value
                else:
                    metadata[key] = value

        # Handle lifecycle section
        elif in_lifecycle:
            if line.startswith("- Created:"):
                lifecycle_data["Created"] = line[10:].strip()
            elif line.startswith("- Active:"):
                lifecycle_data["Active"] = line[9:].strip()
            elif line.startswith("- Obsolescence Conditions:"):
                continue  # Just a header, content follows
            elif (
                line.startswith("1.")
                or line.startswith("2.")
                or line.startswith("3.")
            ):
                lifecycle_data["Obsolescence Conditions"].append(
                    line[2:].strip()
                )

    metadata["Lifecycle"] = lifecycle_data
    return metadata


def validate_metadata(file_path: str, metadata: Dict[str, Any]) -> List[str]:
    """
    Validate metadata for required fields and values.

    Args:
        file_path (str): Path to the tool file.
        metadata (Dict[str, Any]): Parsed metadata.

    Returns:
        List[str]: List of validation errors.
    """
    errors = []

    # Check for required fields
    for field in REQUIRED_METADATA_FIELDS:
        if field not in metadata:
            errors.append(f"Missing required field: {field}")

    # Validate Status field
    if "Status" in metadata and metadata["Status"] not in VALID_STATUS_VALUES:
        errors.append(
            f"Invalid Status value: {metadata['Status']}. "
            f"Must be one of {VALID_STATUS_VALUES}"
        )

    # Validate dates - only check format if field exists
    for date_field in ["Created", "Last Validated"]:
        if date_field in metadata:
            try:
                # Only try to parse if it looks like a date
                if (
                    len(metadata[date_field]) >= 10
                    and metadata[date_field].count("-") == 2
                ):
                    datetime.strptime(metadata[date_field][:10], "%Y-%m-%d")
            except ValueError:
                errors.append(
                    f"Invalid date format for {date_field}: {metadata[date_field]}. "
                    "Use YYYY-MM-DD"
                )

    # Check lifecycle data
    if "Lifecycle" in metadata:
        lifecycle = metadata["Lifecycle"]
        if not lifecycle.get("Created"):
            errors.append("Missing Lifecycle Created reason")
        if not lifecycle.get("Active"):
            errors.append("Missing Lifecycle Active status")
        if not lifecycle.get("Obsolescence Conditions"):
            errors.append("Missing Lifecycle Obsolescence Conditions")

    return errors


def validate_tool_metadata(
    file_path: str,
) -> Tuple[bool, Dict[str, Any], List[str]]:
    """
    Validate metadata for a tool file.

    Args:
        file_path (str): Path to the tool file.

    Returns:
        Tuple[bool, Dict[str, Any], List[str]]: Success status, metadata dict, and list of errors.
    """
    metadata_str = extract_metadata(file_path)
    if not metadata_str:
        return False, {}, ["No metadata found in tool file"]

    metadata = parse_metadata(metadata_str)
    errors = validate_metadata(file_path, metadata)

    return len(errors) == 0, metadata, errors


def generate_tool_inventory() -> pd.DataFrame:
    """
    Generate an inventory of all tools with their metadata.

    Returns:
        pd.DataFrame: DataFrame containing tool inventory.
    """
    tools = find_tools()
    inventory_data = []

    for file_path in tools:
        valid, metadata, errors = validate_tool_metadata(file_path)

        relative_path = os.path.relpath(file_path, os.path.dirname(TOOLS_DIR))

        tool_data = {
            "Path": relative_path,
            "Name": metadata.get("Tool", os.path.basename(file_path)),
            "Status": metadata.get("Status", "Unknown"),
            "Purpose": metadata.get("Purpose", "Unknown"),
            "Created": metadata.get("Created", "Unknown"),
            "Last Validated": metadata.get("Last Validated", "Unknown"),
            "Author": metadata.get("Author", "Unknown"),
            "Dependencies": metadata.get("Dependencies", "Unknown"),
            "Metadata Valid": valid,
        }

        # Add lifecycle data if available
        if "Lifecycle" in metadata:
            tool_data["Created Reason"] = metadata["Lifecycle"].get(
                "Created", "Unknown"
            )
            tool_data["Active Status"] = metadata["Lifecycle"].get(
                "Active", "Unknown"
            )
            tool_data["Obsolescence Conditions"] = "; ".join(
                metadata["Lifecycle"].get(
                    "Obsolescence Conditions", ["Unknown"]
                )
            )

        inventory_data.append(tool_data)

    # Create DataFrame
    df = pd.DataFrame(inventory_data)

    # Sort by status (Active first) and then by name
    df = df.sort_values(
        by=["Status", "Name"],
        key=lambda x: x.map(
            {"Active": 0, "Deprecated": 1, "Archived": 2, "Unknown": 3}
            if x.name == "Status"
            else x
        ),
    )

    return df


def save_inventory_report(df: pd.DataFrame, format: str = "html") -> str:
    """
    Save inventory report to a file.

    Args:
        df (pd.DataFrame): DataFrame containing tool inventory.
        format (str): Output format (html, csv, json, markdown).

    Returns:
        str: Path to the saved report.
    """
    # Create reports directory if it doesn't exist
    os.makedirs(REPORTS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_filename = f"tool_inventory_{timestamp}"

    if format == "html":
        # Generate HTML report with styling
        html_file = os.path.join(REPORTS_DIR, f"{base_filename}.html")
        html_content = f"""
        <html>
        <head>
            <title>Tool Inventory Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                h2 {{ color: #34495e; margin-top: 20px; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th {{ background-color: #3498db; color: white; padding: 8px; text-align: left; }}
                td {{ padding: 8px; border-bottom: 1px solid #ddd; }}
                tr:nth-child(even) {{ background-color: #f2f2f2; }}
                tr:hover {{ background-color: #e2e2e2; }}
                .metadata-valid {{ color: green; }}
                .metadata-invalid {{ color: red; }}
                .status-active {{ color: green; }}
                .status-deprecated {{ color: orange; }}
                .status-archived {{ color: gray; }}
                .summary {{ margin: 20px 0; padding: 10px; background-color: #f8f9fa; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h1>Tool Inventory Report</h1>
            <div class="summary">
                <h2>Summary</h2>
                <p>Total Tools: {len(df)}</p>
                <p>Active Tools: {len(df[df['Status'] == 'Active'])}</p>
                <p>Deprecated Tools: {len(df[df['Status'] == 'Deprecated'])}</p>
                <p>Archived Tools: {len(df[df['Status'] == 'Archived'])}</p>
                <p>Tools with Invalid Metadata: {len(df[df['Metadata Valid'] == False])}</p>
                <p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            </div>
        """

        # Add tables by status
        for status in ["Active", "Deprecated", "Archived", "Unknown"]:
            status_df = df[df["Status"] == status]
            if len(status_df) > 0:
                # Convert to HTML with custom styling for status and metadata validity
                status_html = status_df.to_html(
                    index=False, escape=False, classes="table"
                )

                # Replace values with styled versions
                status_html = status_html.replace(
                    ">True<", ' class="metadata-valid">Valid<'
                )
                status_html = status_html.replace(
                    ">False<", ' class="metadata-invalid">Invalid<'
                )
                status_html = status_html.replace(
                    f">{status}<",
                    f' class="status-{status.lower()}">{status}<',
                )

                html_content += f"""
                <h2>{status} Tools</h2>
                {status_html}
                """

        html_content += """
        </body>
        </html>
        """

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        return html_file

    elif format == "csv":
        csv_file = os.path.join(REPORTS_DIR, f"{base_filename}.csv")
        df.to_csv(csv_file, index=False)
        return csv_file

    elif format == "json":
        json_file = os.path.join(REPORTS_DIR, f"{base_filename}.json")
        df.to_json(json_file, orient="records", indent=2)
        return json_file

    elif format == "markdown":
        md_file = os.path.join(REPORTS_DIR, f"{base_filename}.md")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write("# Tool Inventory Report\n\n")
            f.write(
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            f.write("## Summary\n\n")
            f.write(f"- Total Tools: {len(df)}\n")
            f.write(f"- Active Tools: {len(df[df['Status'] == 'Active'])}\n")
            f.write(
                f"- Deprecated Tools: {len(df[df['Status'] == 'Deprecated'])}\n"
            )
            f.write(
                f"- Archived Tools: {len(df[df['Status'] == 'Archived'])}\n"
            )
            f.write(
                f"- Tools with Invalid Metadata: {len(df[df['Metadata Valid'] == False])}\n\n"
            )

            for status in ["Active", "Deprecated", "Archived", "Unknown"]:
                status_df = df[df["Status"] == status]
                if len(status_df) > 0:
                    f.write(f"## {status} Tools\n\n")
                    f.write(
                        tabulate(status_df, headers="keys", tablefmt="pipe")
                    )
                    f.write("\n\n")

        return md_file

    else:
        raise ValueError(f"Unsupported format: {format}")


def search_tools(
    query: str, inventory_df: Optional[pd.DataFrame] = None
) -> pd.DataFrame:
    """
    Search for tools matching the given query string in name, purpose, or other fields.

    Args:
        query (str): Search query.
        inventory_df (Optional[pd.DataFrame]): Existing inventory DataFrame or None to generate new one.

    Returns:
        pd.DataFrame: DataFrame containing matching tools.
    """
    if inventory_df is None:
        inventory_df = generate_tool_inventory()

    # Convert query to lowercase for case-insensitive search
    query = query.lower()

    # Search in all relevant text columns
    mask = False
    for col in [
        "Name",
        "Purpose",
        "Created Reason",
        "Active Status",
        "Obsolescence Conditions",
    ]:
        if col in inventory_df.columns:
            mask = mask | inventory_df[col].str.lower().str.contains(
                query, na=False
            )

    return inventory_df[mask]


def archive_tool(tool_path: str, reason: str) -> bool:
    """
    Archive a tool by moving it to the archive directory.

    Args:
        tool_path (str): Path to the tool to archive.
        reason (str): Reason for archiving.

    Returns:
        bool: True if the tool was archived successfully, False otherwise.
    """
    try:
        # Ensure archive directory exists
        os.makedirs(ARCHIVE_DIR, exist_ok=True)

        # Get absolute paths
        abs_tool_path = os.path.abspath(tool_path)
        abs_archive_path = os.path.abspath(ARCHIVE_DIR)

        # Get destination filename
        filename = os.path.basename(abs_tool_path)
        dest_path = os.path.join(abs_archive_path, filename)

        # Check if file exists in archive already
        if os.path.exists(dest_path):
            print(
                f"{COLOR_YELLOW}Warning: {filename} already exists in archive.{COLOR_RESET}"
            )
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dest_path = os.path.join(
                abs_archive_path,
                f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}",
            )

        # Read the file content
        with open(abs_tool_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract metadata docstring
        metadata_str = extract_metadata(abs_tool_path)

        if metadata_str:
            # Parse and update metadata
            metadata = parse_metadata(metadata_str)

            # Update status in metadata
            updated_metadata = metadata_str.replace(
                f'Status: {metadata.get("Status", "Active")}',
                f"Status: Archived",
            )

            # Add archival note
            archive_note = (
                f'Archived: {datetime.now().strftime("%Y-%m-%d")} - {reason}'
            )
            if "Last Validated:" in updated_metadata:
                updated_metadata = updated_metadata.replace(
                    "Last Validated:",
                    f"Archived: {datetime.now().strftime('%Y-%m-%d')} - {reason}\nLast Validated:",
                )
            else:
                # Add it before the closing triple quote
                updated_metadata = updated_metadata.replace(
                    '"""', f'{archive_note}\n"""', 1
                )

            # Replace metadata in content
            content = content.replace(metadata_str, updated_metadata)

        # Write updated content to the archive location
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Move the file to archive
        print(
            f"{COLOR_GREEN}Successfully archived {filename} to {dest_path}{COLOR_RESET}"
        )

        # Remove the original file
        os.remove(abs_tool_path)
        print(
            f"{COLOR_GREEN}Removed original file at {abs_tool_path}{COLOR_RESET}"
        )

        return True

    except Exception as e:
        print(f"{COLOR_RED}Error archiving {tool_path}: {e}{COLOR_RESET}")
        return False


def mark_deprecated(
    tool_path: str, reason: str, replacement: Optional[str] = None
) -> bool:
    """
    Mark a tool as deprecated by updating its metadata.

    Args:
        tool_path (str): Path to the tool to deprecate.
        reason (str): Reason for deprecation.
        replacement (Optional[str]): Replacement tool if any.

    Returns:
        bool: True if the tool was marked as deprecated successfully, False otherwise.
    """
    try:
        # Get absolute path
        abs_tool_path = os.path.abspath(tool_path)

        # Read the file content
        with open(abs_tool_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract metadata docstring
        metadata_str = extract_metadata(abs_tool_path)

        if not metadata_str:
            print(
                f"{COLOR_RED}Error: No metadata found in {tool_path}{COLOR_RESET}"
            )
            return False

        # Parse metadata
        metadata = parse_metadata(metadata_str)

        # Update status in metadata
        updated_metadata = metadata_str.replace(
            f'Status: {metadata.get("Status", "Active")}',
            f"Status: Deprecated",
        )

        # Add deprecation note
        deprecation_note = (
            f'Deprecated: {datetime.now().strftime("%Y-%m-%d")} - {reason}'
        )
        if replacement:
            deprecation_note += f" Replaced by: {replacement}"

        if "Last Validated:" in updated_metadata:
            updated_metadata = updated_metadata.replace(
                "Last Validated:", f"{deprecation_note}\nLast Validated:"
            )
        else:
            # Add it before the closing triple quote
            updated_metadata = updated_metadata.replace(
                '"""', f'{deprecation_note}\n"""', 1
            )

        # Replace metadata in content
        content = content.replace(metadata_str, updated_metadata)

        # Write updated content back to the file
        with open(abs_tool_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(
            f"{COLOR_GREEN}Successfully marked {os.path.basename(tool_path)} as deprecated{COLOR_RESET}"
        )
        return True

    except Exception as e:
        print(
            f"{COLOR_RED}Error marking {tool_path} as deprecated: {e}{COLOR_RESET}"
        )
        return False


def update_tool_readme(inventory_df: pd.DataFrame) -> bool:
    """
    Update the tools/README.md file with the latest tool inventory.

    Args:
        inventory_df (pd.DataFrame): DataFrame containing tool inventory.

    Returns:
        bool: True if the README was updated successfully, False otherwise.
    """
    try:
        readme_path = os.path.join(TOOLS_DIR, "README.md")

        # Read existing README
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()

        # Create new section for available tools
        available_tools_section = "## Available Tools\n\n"

        # Group tools by category (using first word of purpose as a heuristic)
        tool_categories = {}

        for _, row in inventory_df[
            inventory_df["Status"] == "Active"
        ].iterrows():
            tool_name = row["Name"]
            purpose = row["Purpose"]
            path = row["Path"]

            # Determine category
            category = "Core Tools"  # Default category
            if "BDD" in tool_name or "bdd" in path:
                category = "BDD Tools"
            elif "TDD" in tool_name or "tdd" in path:
                category = "TDD Tools"
            elif any(
                kw in purpose.lower() for kw in ["style", "lint", "format"]
            ):
                category = "Style Tools"
            elif any(kw in purpose.lower() for kw in ["repo", "repository"]):
                category = "Repository Tools"
            elif any(kw in purpose.lower() for kw in ["doc", "documentation"]):
                category = "Documentation Tools"
            elif any(kw in purpose.lower() for kw in ["ci", "cd", "pipeline"]):
                category = "CI/CD Tools"
            elif any(kw in purpose.lower() for kw in ["analysis", "analyze"]):
                category = "Analysis Tools"

            if category not in tool_categories:
                tool_categories[category] = []

            tool_categories[category].append(
                {"name": tool_name, "path": path, "purpose": purpose}
            )

        # Generate markdown for each category
        for category, tools in sorted(tool_categories.items()):
            available_tools_section += f"### {category}\n\n"

            for tool in tools:
                filename = os.path.basename(tool["path"])
                purpose = tool["purpose"].split(".")[0]  # Get first sentence
                available_tools_section += f"- `{filename}`: {purpose}\n"

            available_tools_section += "\n"

        # Add archived tools section
        available_tools_section += "## Archived Tools\n\n"
        available_tools_section += "The following tools have been archived in `tools/archive/` for reference:\n"

        for _, row in inventory_df[
            inventory_df["Status"] == "Archived"
        ].iterrows():
            filename = os.path.basename(row["Path"])
            purpose = row["Purpose"].split(".")[0]  # Get first sentence
            available_tools_section += f"- `{filename}`: {purpose}\n"

        available_tools_section += "\n"

        # Replace the existing tools section in the README
        if (
            "## Available Tools" in readme_content
            and "## Usage" in readme_content
        ):
            start_idx = readme_content.find("## Available Tools")
            end_idx = readme_content.find("## Usage", start_idx)

            updated_readme = (
                readme_content[:start_idx]
                + available_tools_section
                + readme_content[end_idx:]
            )
        else:
            # If the structure is different, just append to the end
            updated_readme = readme_content + "\n\n" + available_tools_section

        # Write updated content back to README
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)

        print(f"{COLOR_GREEN}Successfully updated {readme_path}{COLOR_RESET}")
        return True

    except Exception as e:
        print(f"{COLOR_RED}Error updating README: {e}{COLOR_RESET}")
        return False


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Tool Inventory Manager - Inventory, evaluate, and manage tools in the codebase"
    )

    parser.add_argument(
        "--inventory",
        action="store_true",
        help="Generate a tool inventory report",
    )

    parser.add_argument(
        "--format",
        type=str,
        choices=["html", "csv", "json", "markdown"],
        default="html",
        help="Format for the inventory report (default: html)",
    )

    parser.add_argument(
        "--validate", action="store_true", help="Validate tool metadata"
    )

    parser.add_argument(
        "--search", type=str, help="Search for tools matching the given query"
    )

    parser.add_argument(
        "--archive",
        type=str,
        help="Archive a tool (provide the path relative to workspace)",
    )

    parser.add_argument(
        "--reason", type=str, help="Reason for archiving or deprecating a tool"
    )

    parser.add_argument(
        "--deprecate",
        type=str,
        help="Mark a tool as deprecated (provide the path relative to workspace)",
    )

    parser.add_argument(
        "--replacement",
        type=str,
        help="Replacement tool for a deprecated tool",
    )

    parser.add_argument(
        "--update-readme",
        action="store_true",
        help="Update the tools/README.md file with the latest tool inventory",
    )

    return parser.parse_args()


def main() -> int:
    """
    Main entry point for the tool.

    Returns:
        int: Exit code (0 for success, non-zero for failure).
    """
    args = parse_arguments()

    # Generate inventory as it's used by multiple commands
    inventory_df = generate_tool_inventory()

    # Perform actions based on arguments
    if args.inventory:
        report_file = save_inventory_report(inventory_df, args.format)
        print(
            f"{COLOR_GREEN}Inventory report saved to {report_file}{COLOR_RESET}"
        )

    if args.validate:
        valid_count = len(inventory_df[inventory_df["Metadata Valid"] == True])
        invalid_count = len(
            inventory_df[inventory_df["Metadata Valid"] == False]
        )

        print(f"{COLOR_BLUE}Validation Results:{COLOR_RESET}")
        print(f"{COLOR_GREEN}Valid: {valid_count}{COLOR_RESET}")
        print(f"{COLOR_RED}Invalid: {invalid_count}{COLOR_RESET}")

        if invalid_count > 0:
            print(f"{COLOR_YELLOW}Invalid tools:{COLOR_RESET}")
            for _, row in inventory_df[
                inventory_df["Metadata Valid"] == False
            ].iterrows():
                print(f"  {COLOR_RED}✗ {row['Path']}{COLOR_RESET}")

            return 1

    if args.search:
        results_df = search_tools(args.search, inventory_df)

        if len(results_df) > 0:
            print(
                f"{COLOR_GREEN}Found {len(results_df)} tools matching '{args.search}':{COLOR_RESET}"
            )
            print(
                tabulate(
                    results_df[["Name", "Status", "Purpose", "Path"]],
                    headers="keys",
                    tablefmt="grid",
                )
            )
        else:
            print(
                f"{COLOR_YELLOW}No tools found matching '{args.search}'{COLOR_RESET}"
            )

    if args.archive:
        if not args.reason:
            print(
                f"{COLOR_RED}Error: --reason is required when archiving a tool{COLOR_RESET}"
            )
            return 1

        success = archive_tool(args.archive, args.reason)
        if not success:
            return 1

    if args.deprecate:
        if not args.reason:
            print(
                f"{COLOR_RED}Error: --reason is required when deprecating a tool{COLOR_RESET}"
            )
            return 1

        success = mark_deprecated(
            args.deprecate, args.reason, args.replacement
        )
        if not success:
            return 1

    if args.update_readme:
        success = update_tool_readme(inventory_df)
        if not success:
            return 1

    # If no action specified, show help
    if not any(
        [
            args.inventory,
            args.validate,
            args.search,
            args.archive,
            args.deprecate,
            args.update_readme,
        ]
    ):
        print(f"{COLOR_BLUE}Tool Inventory Manager{COLOR_RESET}")
        print(
            f"{COLOR_YELLOW}No action specified. Use --help to see available options.{COLOR_RESET}"
        )
        print("\nQuick summary:")
        print(f"Total tools: {len(inventory_df)}")
        print(
            f"Active: {len(inventory_df[inventory_df['Status'] == 'Active'])}"
        )
        print(
            f"Deprecated: {len(inventory_df[inventory_df['Status'] == 'Deprecated'])}"
        )
        print(
            f"Archived: {len(inventory_df[inventory_df['Status'] == 'Archived'])}"
        )
        print(
            f"Unknown: {len(inventory_df[inventory_df['Status'] == 'Unknown'])}"
        )
        print(
            f"Invalid metadata: {len(inventory_df[inventory_df['Metadata Valid'] == False])}"
        )

        print("\nAvailable commands:")
        print("  --inventory        Generate inventory report")
        print("  --validate         Validate tool metadata")
        print("  --search QUERY     Search for tools")
        print("  --archive PATH     Archive a tool")
        print("  --deprecate PATH   Mark a tool as deprecated")
        print("  --update-readme    Update README.md with latest inventory")

        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
