#!/usr/bin/env python3
"""
Tool: Metadata Injector
Created: 2025-03-21
Author: Development Team
Status: Active
Purpose: Inject standardized metadata into tool files to ensure compliance with tool development standards
Dependencies: re, datetime
Lifecycle:
    - Created: To support the Tool Metadata Compliance Project
    - Active: Used during the tool metadata compliance initiative
    - Obsolescence Conditions:
        1. When all tools have been updated with proper metadata
        2. When replaced by a more integrated metadata management system
Last Validated: 2025-03-21

This script helps inject standardized metadata into tool files, ensuring
consistency and compliance with the project's tool development standards.
"""

import argparse
import re
import sys
from datetime import datetime


def inject_metadata(file_path, tool_name, author, purpose, dependencies, created_reason, active_status, obsolescence):
    """
    Inject standard metadata into a tool file.
    
    Args:
        file_path: Path to the tool file
        tool_name: Name of the tool
        author: Author of the tool
        purpose: Clear description of tool's purpose
        dependencies: Required packages/tools
        created_reason: Why the tool was created
        active_status: Current usage status
        obsolescence: Conditions for obsolescence
    """
    created_date = datetime.now().strftime("%Y-%m-%d")
    
    metadata = f'''"""
Tool: {tool_name}
Created: {created_date}
Author: {author}
Status: Active
Purpose: {purpose}
Dependencies: {dependencies}
Lifecycle:
    - Created: {created_reason}
    - Active: {active_status}
    - Obsolescence Conditions:
        1. {obsolescence[0]}
        2. {obsolescence[1] if len(obsolescence) > 1 else "When project requirements change significantly"}
Last Validated: {created_date}

"""
'''
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if there's an existing docstring to replace
    docstring_pattern = r'"""[\s\S]*?"""'
    if re.match(docstring_pattern, content.strip()):
        updated_content = re.sub(docstring_pattern, metadata, content, count=1)
    else:
        # Add metadata at the beginning of the file
        updated_content = metadata + content
    
    with open(file_path, 'w') as f:
        f.write(updated_content)
    
    print(f"✅ Metadata injected into {file_path}")


def main():
    """Main entry point for the tool."""
    parser = argparse.ArgumentParser(description="Inject metadata into tool files")
    parser.add_argument("file_path", help="Path to the tool file")
    parser.add_argument("--tool-name", required=True, help="Name of the tool")
    parser.add_argument("--author", default="Development Team", help="Author of the tool")
    parser.add_argument("--purpose", required=True, help="Clear description of tool's purpose")
    parser.add_argument("--dependencies", default="None", help="Required packages/tools")
    parser.add_argument("--created-reason", required=True, help="Why the tool was created")
    parser.add_argument("--active-status", required=True, help="Current usage status")
    parser.add_argument("--obsolescence", nargs="+", required=True, help="Conditions for obsolescence")
    
    args = parser.parse_args()
    
    inject_metadata(
        args.file_path,
        args.tool_name,
        args.author,
        args.purpose,
        args.dependencies,
        args.created_reason,
        args.active_status,
        args.obsolescence
    )
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 