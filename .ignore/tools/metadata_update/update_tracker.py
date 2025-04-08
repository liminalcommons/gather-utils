#!/usr/bin/env python3
"""
Tool: Metadata Update Tracker
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Track and report on the progress of the Tool Metadata Compliance Project
Dependencies: json, datetime, pandas, tabulate
Lifecycle:
    - Created: To support the Tool Metadata Compliance Project
    - Active: Used during the tool metadata compliance initiative
    - Obsolescence Conditions:
        1. When all tools have been updated with proper metadata
        2. When replaced by a more integrated metadata management system
Last Validated: 2025-03-21

This script tracks the progress of the tool metadata update project, allowing
users to initialize tracking, update tool status, and generate reports.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import pandas as pd
    from tabulate import tabulate
except ImportError:
    print("Required dependencies not found. Install with:")
    print("poetry install")
    sys.exit(1)

# Constants
TRACKING_DIR = "reports/tool_metadata_compliance"
TRACKING_FILE = os.path.join(TRACKING_DIR, "update_progress.json")
DEFAULT_BATCH_SIZE = 5


def ensure_tracking_dir():
    """Ensure the tracking directory exists."""
    os.makedirs(TRACKING_DIR, exist_ok=True)


def initialize_tracking(reset=False):
    """
    Initialize or reset the tracking file.

    Args:
        reset: Whether to reset an existing tracking file

    Returns:
        bool: Success status
    """
    ensure_tracking_dir()

    if os.path.exists(TRACKING_FILE) and not reset:
        print(f"Tracking file already exists at {TRACKING_FILE}")
        print("Use --reset to create a new tracking file")
        return False

    # Import here to avoid circular import
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    )
    from tools.tool_inventory_manager import (
        extract_metadata,
        find_tools,
        parse_metadata,
    )

    tools = find_tools()

    tracking_data = {
        "project_info": {
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_tools": len(tools),
            "completed_tools": 0,
            "remaining_tools": len(tools),
            "completion_percentage": 0.0,
        },
        "tools": [],
    }

    for tool_path in tools:
        metadata_str = extract_metadata(tool_path)
        metadata = parse_metadata(metadata_str) if metadata_str else {}

        tool_data = {
            "path": tool_path,
            "name": os.path.basename(tool_path),
            "status": "Completed" if metadata.get("Tool") else "Pending",
            "metadata_valid": bool(metadata.get("Tool")),
            "updated_date": "",
            "batch": "",
        }

        tracking_data["tools"].append(tool_data)

    # Initial count of completed tools
    completed = sum(
        1 for tool in tracking_data["tools"] if tool["status"] == "Completed"
    )
    tracking_data["project_info"]["completed_tools"] = completed
    tracking_data["project_info"]["remaining_tools"] = len(tools) - completed
    tracking_data["project_info"]["completion_percentage"] = (
        (completed / len(tools)) * 100 if tools else 0
    )

    with open(TRACKING_FILE, "w") as f:
        json.dump(tracking_data, f, indent=2)

    print(f"Tracking initialized with {len(tools)} tools")
    print(f"{completed} tools already have valid metadata")
    print(f"{len(tools) - completed} tools require updates")

    return True


def load_tracking_data():
    """
    Load tracking data from file.

    Returns:
        dict: Tracking data or None if file doesn't exist
    """
    if not os.path.exists(TRACKING_FILE):
        print(f"Tracking file not found: {TRACKING_FILE}")
        print(
            "Run 'python tools/metadata_update/update_tracker.py --init' to initialize tracking"
        )
        return None

    with open(TRACKING_FILE, "r") as f:
        return json.load(f)


def save_tracking_data(tracking_data):
    """
    Save tracking data to file.

    Args:
        tracking_data: The tracking data to save
    """
    # Update project info
    total = len(tracking_data["tools"])
    completed = sum(
        1 for tool in tracking_data["tools"] if tool["status"] == "Completed"
    )

    tracking_data["project_info"]["last_updated"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    tracking_data["project_info"]["completed_tools"] = completed
    tracking_data["project_info"]["remaining_tools"] = total - completed
    tracking_data["project_info"]["completion_percentage"] = (
        (completed / total) * 100 if total else 0
    )

    with open(TRACKING_FILE, "w") as f:
        json.dump(tracking_data, f, indent=2)


def mark_tool_completed(tool_path, batch=""):
    """
    Mark a tool as completed.

    Args:
        tool_path: Path to the tool
        batch: Optional batch identifier

    Returns:
        bool: Success status
    """
    tracking_data = load_tracking_data()
    if not tracking_data:
        return False

    # Find the tool in the tracking data
    for tool in tracking_data["tools"]:
        if tool["path"] == tool_path:
            tool["status"] = "Completed"
            tool["updated_date"] = datetime.now().strftime("%Y-%m-%d")
            if batch:
                tool["batch"] = batch
            save_tracking_data(tracking_data)
            print(f"✅ Marked {tool_path} as completed")
            return True

    print(f"❌ Tool not found in tracking data: {tool_path}")
    return False


def suggest_next_batch(batch_size=DEFAULT_BATCH_SIZE):
    """
    Suggest the next batch of tools to update.

    Args:
        batch_size: Number of tools to include in the batch

    Returns:
        list: List of tool paths
    """
    tracking_data = load_tracking_data()
    if not tracking_data:
        return []

    # Filter for pending tools
    pending_tools = [
        tool for tool in tracking_data["tools"] if tool["status"] == "Pending"
    ]

    # Sort by name for consistent batching
    pending_tools.sort(key=lambda x: x["name"])

    # Return the first batch_size tools
    return [tool["path"] for tool in pending_tools[:batch_size]]


def generate_status_report():
    """
    Generate a status report for the metadata update project.

    Returns:
        str: Markdown-formatted status report
    """
    tracking_data = load_tracking_data()
    if not tracking_data:
        return "No tracking data available"

    info = tracking_data["project_info"]

    report = [
        "# Tool Metadata Compliance Project Status",
        "",
        f"Last Updated: {info['last_updated']}",
        "",
        "## Progress",
        f"- Total tools: {info['total_tools']}",
        f"- Tools with valid metadata: {info['completed_tools']}/{info['total_tools']} ({info['completion_percentage']:.1f}%)",
        f"- Tools remaining: {info['remaining_tools']}",
        "",
        "## Recently Updated Tools",
    ]

    # Get recently updated tools (sort by updated_date, descending)
    updated_tools = [t for t in tracking_data["tools"] if t["updated_date"]]
    updated_tools.sort(key=lambda x: x["updated_date"], reverse=True)

    # Add the 5 most recently updated tools
    for tool in updated_tools[:5]:
        report.append(
            f"1. [{os.path.basename(tool['path'])}] - {tool['updated_date']}"
        )

    # If no tools have been updated
    if not updated_tools:
        report.append("No tools have been updated yet")

    # Add the next batch
    report.extend(
        [
            "",
            f"## Next Batch (Suggested)",
        ]
    )

    next_batch = suggest_next_batch()
    if next_batch:
        for i, tool_path in enumerate(next_batch, 1):
            report.append(f"{i}. {os.path.basename(tool_path)}")
    else:
        report.append("All tools have been updated!")

    return "\n".join(report)


def save_status_report():
    """
    Save a status report to file.

    Returns:
        str: Path to the saved report
    """
    ensure_tracking_dir()
    report = generate_status_report()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(TRACKING_DIR, f"status_report_{timestamp}.md")

    with open(report_path, "w") as f:
        f.write(report)

    return report_path


def main():
    """Main entry point for the tool."""
    parser = argparse.ArgumentParser(
        description="Track and report on the progress of the Tool Metadata Compliance Project"
    )

    # Command groups
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--init", action="store_true", help="Initialize tracking"
    )
    group.add_argument("--reset", action="store_true", help="Reset tracking")
    group.add_argument(
        "--status", action="store_true", help="Show current status"
    )
    group.add_argument(
        "--report", action="store_true", help="Generate status report"
    )
    group.add_argument(
        "--mark-completed",
        metavar="TOOL_PATH",
        help="Mark a tool as completed",
    )
    group.add_argument(
        "--next-batch", action="store_true", help="Suggest next batch of tools"
    )

    # Additional options
    parser.add_argument(
        "--batch",
        metavar="BATCH_ID",
        help="Batch identifier for marking tools",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help="Batch size for suggestions",
    )

    args = parser.parse_args()

    # If no arguments, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    # Initialize tracking
    if args.init or args.reset:
        initialize_tracking(reset=args.reset)
        return 0

    # Show current status
    if args.status:
        tracking_data = load_tracking_data()
        if not tracking_data:
            return 1

        info = tracking_data["project_info"]
        print(f"Tool Metadata Compliance Project Status")
        print(f"Started: {info['start_date']}")
        print(f"Last Updated: {info['last_updated']}")
        print(
            f"Progress: {info['completed_tools']}/{info['total_tools']} ({info['completion_percentage']:.1f}%)"
        )
        print(f"Remaining: {info['remaining_tools']}")
        return 0

    # Generate status report
    if args.report:
        report_path = save_status_report()
        print(f"Status report saved to {report_path}")
        return 0

    # Mark a tool as completed
    if args.mark_completed:
        success = mark_tool_completed(args.mark_completed, args.batch)
        return 0 if success else 1

    # Suggest next batch
    if args.next_batch:
        batch = suggest_next_batch(args.batch_size)
        if not batch:
            return 1

        print(f"Suggested next batch ({len(batch)} tools):")
        for i, tool_path in enumerate(batch, 1):
            print(f"{i}. {tool_path}")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
