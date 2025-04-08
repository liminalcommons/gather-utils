#!/usr/bin/env python3
"""
Tool: Metadata Batch Processor
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Process multiple tools at once to update their metadata
Dependencies: json, subprocess, os
Lifecycle:
    - Created: To support the Tool Metadata Compliance Project
    - Active: Used during the tool metadata compliance initiative
    - Obsolescence Conditions:
        1. When all tools have been updated with proper metadata
        2. When replaced by a more integrated metadata management system
Last Validated: 2025-03-21

This script processes multiple tools in a batch, updating their metadata
and tracking progress using the update_tracker.py tool.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime


def get_next_batch(batch_size=5):
    """
    Get the next batch of tools to process.

    Args:
        batch_size: Number of tools to include in batch

    Returns:
        list: List of tool paths
    """
    result = subprocess.run(
        [
            sys.executable,
            "tools/metadata_update/update_tracker.py",
            "--next-batch",
            "--batch-size",
            str(batch_size),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error getting next batch: {result.stderr}")
        return []

    # Parse the output to extract tool paths
    tools = []
    for line in result.stdout.splitlines():
        if line.startswith("Suggested next batch"):
            continue
        if line.strip() and ". " in line:
            tool_path = line.split(". ", 1)[1].strip()
            tools.append(tool_path)

    return tools


def analyze_tool(tool_path):
    """
    Analyze a tool to determine its purpose, dependencies, etc.

    Args:
        tool_path: Path to the tool file

    Returns:
        dict: Tool metadata information
    """
    metadata = {
        "name": os.path.basename(tool_path)
        .replace(".py", "")
        .replace("_", " ")
        .title(),
        "dependencies": "",
        "purpose": "",
        "created_reason": "",
        "active_status": "",
        "obsolescence": [],
    }

    # Read the tool file to analyze its contents
    with open(tool_path, "r") as f:
        content = f.read()

    # Extract existing docstrings to analyze original purpose
    docstring_pattern = r'"""([\s\S]*?)"""'
    docstring_matches = re.findall(docstring_pattern, content)

    # If we have docstrings, analyze them for purpose statements
    if docstring_matches:
        for docstring in docstring_matches:
            # Look for purpose statements in docstrings
            purpose_match = re.search(
                r"(?:Purpose|This (?:script|tool|utility))(?:[\s:]*)([^\n\.]*(?:\.[^\n\.]*){0,2})",
                docstring,
                re.IGNORECASE,
            )
            if purpose_match and not metadata["purpose"]:
                metadata["purpose"] = purpose_match.group(1).strip()

            # Look for what the tool was created for
            created_match = re.search(
                r"(?:Created to|Developed to|(?:^|\n)- Created to)(?:[\s:]*)([^\n\.]*(?:\.[^\n\.]*){0,2})",
                docstring,
                re.IGNORECASE,
            )
            if created_match and not metadata["created_reason"]:
                metadata["created_reason"] = created_match.group(1).strip()

    # Analyze main function docstring if available
    main_docstring_match = re.search(
        r'def main\(\):([\s\S]*?)"""([\s\S]*?)"""', content
    )
    if main_docstring_match and not metadata["purpose"]:
        main_doc = main_docstring_match.group(2)
        # Extract first sentence as purpose
        sentences = re.split(r"(?<=[.!?])\s+", main_doc.strip())
        if sentences:
            metadata["purpose"] = sentences[0].strip()

    # Determine dependencies by looking for imports
    imports = []
    for line in content.splitlines():
        if line.startswith("import ") or line.startswith("from "):
            # Extract the package name
            if line.startswith("import "):
                package = line.split()[1].split(".")[0]
            else:  # from X import Y
                package = line.split()[1].split(".")[0]

            # Skip standard library packages
            if package not in imports and package not in [
                "os",
                "sys",
                "re",
                "json",
                "datetime",
                "pathlib",
                "argparse",
                "typing",
                "collections",
                "math",
                "time",
                "logging",
                "subprocess",
                "contextlib",
                "shutil",
                "tempfile",
                "functools",
                "itertools",
            ]:
                imports.append(package)

    if imports:
        metadata["dependencies"] = ", ".join(imports)
    else:
        # Look for setup.py-related dependencies or requirements
        req_match = re.search(
            r"(?:requirements|install_requires)[^\]]*\[(.*?)\]",
            content,
            re.DOTALL,
        )
        if req_match:
            cleaned_reqs = re.sub(r'[\'",\s]', " ", req_match.group(1))
            metadata["dependencies"] = ", ".join(
                [r.strip() for r in cleaned_reqs.split() if r.strip()]
            )
        else:
            metadata["dependencies"] = "None"

    # Try to determine purpose from content analysis if we don't have it yet
    if not metadata["purpose"]:
        # First check for class-level docstrings for main classes
        class_matches = re.finditer(
            r'class\s+(\w+).*?"""([\s\S]*?)"""', content
        )
        for match in class_matches:
            class_name = match.group(1)
            class_doc = match.group(2)
            if (
                class_name.endswith("Analyzer")
                or class_name.endswith("Generator")
                or class_name.endswith("Manager")
            ):
                sentences = re.split(r"(?<=[.!?])\s+", class_doc.strip())
                if sentences:
                    metadata["purpose"] = (
                        f"Provides a {class_name} to {sentences[0].lower().strip()}"
                    )
                    break

    # Fallback to filename-based purpose if still not determined
    if not metadata["purpose"]:
        name_parts = os.path.basename(tool_path).replace(".py", "").split("_")

        # Check if it's a BDD-related tool
        if "bdd" in name_parts:
            if "coverage" in name_parts:
                metadata["purpose"] = (
                    "Generate coverage reports for BDD features and scenarios"
                )
            elif "validator" in name_parts:
                metadata["purpose"] = (
                    "Validate BDD feature files for compliance with standards"
                )
            elif "feature" in name_parts and "consolidator" in name_parts:
                metadata["purpose"] = (
                    "Consolidate similar or duplicate BDD features"
                )
            elif "analyzer" in name_parts:
                metadata["purpose"] = (
                    "Analyze BDD features and scenarios for patterns and issues"
                )
            elif "tag" in name_parts:
                metadata["purpose"] = "Standardize tags in BDD feature files"
            elif "docs" in name_parts or "documentation" in name_parts:
                metadata["purpose"] = (
                    "Generate documentation from BDD feature files"
                )
            elif "test" in name_parts or "runner" in name_parts:
                metadata["purpose"] = "Run BDD tests and generate reports"
            else:
                metadata["purpose"] = (
                    "Support BDD testing and development workflows"
                )
        elif "repo" in name_parts:
            if "health" in name_parts:
                metadata["purpose"] = (
                    "Check repository health and compliance with standards"
                )
            elif "reconcile" in name_parts:
                metadata["purpose"] = (
                    "Reconcile repository structure with project standards"
                )
            else:
                metadata["purpose"] = (
                    "Manage repository structure and organization"
                )
        elif "tool" in name_parts and "inventory" in name_parts:
            metadata["purpose"] = (
                "Manage and validate tool inventory and metadata"
            )
        elif "metadata" in name_parts:
            if "injector" in name_parts:
                metadata["purpose"] = (
                    "Inject standardized metadata into tool files"
                )
            elif "update" in name_parts and "tracker" in name_parts:
                metadata["purpose"] = (
                    "Track and report on metadata update progress"
                )
            elif "processor" in name_parts:
                metadata["purpose"] = (
                    "Process multiple tools for metadata updates"
                )
            else:
                metadata["purpose"] = (
                    "Manage tool metadata and standards compliance"
                )
        elif "build" in name_parts and "docs" in name_parts:
            metadata["purpose"] = "Build documentation from source files"
        elif "setup" in name_parts:
            metadata["purpose"] = (
                "Set up development environment and dependencies"
            )
        elif "fix" in name_parts and "style" in name_parts:
            metadata["purpose"] = (
                "Fix code style issues according to project standards"
            )
        else:
            metadata["purpose"] = (
                f"Support {' '.join(name_parts)} functionality"
            )

    # Determine created reason if not found in docstrings
    if not metadata["created_reason"]:
        if "bdd" in tool_path:
            metadata["created_reason"] = (
                "To improve BDD testing capabilities and workflows"
            )
        elif "metadata" in tool_path:
            metadata["created_reason"] = (
                "To support metadata standardization across tools"
            )
        elif "repo" in tool_path:
            metadata["created_reason"] = (
                "To maintain repository health and standards"
            )
        elif "docs" in tool_path or "documentation" in tool_path:
            metadata["created_reason"] = (
                "To improve project documentation generation and management"
            )
        elif "archive" in tool_path:
            metadata["created_reason"] = (
                "To support historical functionality that may be needed for reference"
            )
        else:
            metadata["created_reason"] = (
                "To automate common development tasks and improve workflow efficiency"
            )

    # Determine active status
    if "archive" in tool_path:
        metadata["active_status"] = (
            "Archived for reference but no longer actively used"
        )
    elif any(
        term in tool_path
        for term in ["metadata_update", "batch_processor", "update_tracker"]
    ):
        metadata["active_status"] = "Used for metadata compliance and tracking"
    elif "bdd" in tool_path:
        metadata["active_status"] = (
            "Used in BDD testing workflows and automation"
        )
    elif "repo" in tool_path or "tool_inventory" in tool_path:
        metadata["active_status"] = (
            "Used for repository maintenance and health checks"
        )
    else:
        metadata["active_status"] = "Used in current development workflows"

    # Determine obsolescence conditions
    if "bdd" in tool_path:
        metadata["obsolescence"] = [
            "When BDD testing approach is fundamentally changed",
            "When testing framework is replaced or significantly upgraded",
        ]
    elif "repo" in tool_path or "health" in tool_path:
        metadata["obsolescence"] = [
            "When repository structure standards change significantly",
            "When integrated into a more comprehensive repository management system",
        ]
    elif "metadata" in tool_path or "tool_inventory" in tool_path:
        metadata["obsolescence"] = [
            "When all tools have complete and standardized metadata",
            "When integrated into a more comprehensive project management system",
        ]
    elif "archive" in tool_path:
        metadata["obsolescence"] = [
            "When historical reference is no longer needed",
            "After complete migration to new architecture",
        ]
    else:
        metadata["obsolescence"] = [
            "When project requirements change significantly",
            "When functionality is integrated into the core system",
        ]

    return metadata


def update_tool_metadata(tool_path, batch_id="auto"):
    """
    Update metadata for a single tool.

    Args:
        tool_path: Path to the tool
        batch_id: Batch identifier

    Returns:
        bool: Success status
    """
    # Analyze the tool
    metadata = analyze_tool(tool_path)

    if not batch_id or batch_id == "auto":
        batch_id = f"batch_{datetime.now().strftime('%Y%m%d')}"

    # Run the metadata injector
    result = subprocess.run(
        [
            sys.executable,
            "tools/metadata_update/metadata_injector.py",
            tool_path,
            "--tool-name",
            metadata["name"],
            "--purpose",
            metadata["purpose"],
            "--dependencies",
            metadata["dependencies"],
            "--created-reason",
            metadata["created_reason"],
            "--active-status",
            metadata["active_status"],
            "--obsolescence",
            metadata["obsolescence"][0],
            metadata["obsolescence"][1],
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Error updating metadata for {tool_path}: {result.stderr}")
        return False

    # Mark as completed in the tracker
    track_result = subprocess.run(
        [
            sys.executable,
            "tools/metadata_update/update_tracker.py",
            "--mark-completed",
            tool_path,
            "--batch",
            batch_id,
        ],
        capture_output=True,
        text=True,
    )

    if track_result.returncode != 0:
        print(f"Error marking tool as completed: {track_result.stderr}")
        return False

    print(f"✅ Updated metadata for {tool_path}")
    return True


def process_batch(tools, batch_id="auto"):
    """
    Process a batch of tools.

    Args:
        tools: List of tool paths
        batch_id: Batch identifier

    Returns:
        int: Number of successfully processed tools
    """
    if not batch_id or batch_id == "auto":
        batch_id = f"batch_{datetime.now().strftime('%Y%m%d')}"

    print(f"Processing batch: {batch_id}")
    print(f"Tools to process: {len(tools)}")

    success_count = 0
    for i, tool_path in enumerate(tools, 1):
        print(f"\nProcessing ({i}/{len(tools)}): {tool_path}")
        if update_tool_metadata(tool_path, batch_id):
            success_count += 1

    print(f"\nBatch processing complete")
    print(f"Successfully processed: {success_count}/{len(tools)}")

    # Generate a status report
    subprocess.run(
        [sys.executable, "tools/metadata_update/update_tracker.py", "--report"]
    )

    return success_count


def main():
    """Main entry point for the tool."""
    parser = argparse.ArgumentParser(
        description="Process multiple tools to update their metadata"
    )

    # Arguments
    parser.add_argument(
        "--tools",
        nargs="+",
        metavar="TOOL_PATH",
        help="Paths to tools to process (default: get next batch)",
    )
    parser.add_argument(
        "--batch-id",
        default="auto",
        help="Batch identifier (default: auto-generated)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Number of tools to process if getting next batch",
    )

    args = parser.parse_args()

    # Get tools to process
    tools = args.tools if args.tools else get_next_batch(args.batch_size)

    if not tools:
        print("No tools to process")
        return 0

    # Process the batch
    success_count = process_batch(tools, args.batch_id)

    # Return success if all tools were processed successfully
    return 0 if success_count == len(tools) else 1


if __name__ == "__main__":
    sys.exit(main())
