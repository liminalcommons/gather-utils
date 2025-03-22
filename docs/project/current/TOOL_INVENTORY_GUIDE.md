# Tool Inventory Management Guide

This guide explains how to manage your tools inventory, evaluate tools, and maintain an organized toolset.

Last Updated: 2024-03-21

## Overview

The `tool_inventory_manager.py` tool provides a comprehensive system for:

1. Inventorying all tools in the codebase
2. Evaluating tool metadata and compliance
3. Finding the right tools when you need them
4. Managing tool lifecycle (deprecation and archival)
5. Maintaining up-to-date documentation

## Getting Started

### Prerequisites

The tool requires the following dependencies:
- pandas
- tabulate

These dependencies are included in the project's `pyproject.toml`. To install them:

```bash
# Install dependencies using Poetry
poetry install
```

### Basic Usage

To get a quick overview of your tools ecosystem:

```bash
python tools/tool_inventory_manager.py
```

This will display a summary with counts of Active, Deprecated, Archived, and Unknown status tools, as well as any metadata validation issues.

### Generating Inventory Reports

To generate a detailed inventory report:

```bash
# Generate HTML report (default)
python tools/tool_inventory_manager.py --inventory

# Generate other formats
python tools/tool_inventory_manager.py --inventory --format csv
python tools/tool_inventory_manager.py --inventory --format json
python tools/tool_inventory_manager.py --inventory --format markdown
```

Reports are saved in the `reports/tool_inventory/` directory with timestamped filenames.

## Finding the Right Tool

When you need to find a tool for a specific task:

```bash
# Search by keyword in name, purpose, or lifecycle information
python tools/tool_inventory_manager.py --search "BDD"
python tools/tool_inventory_manager.py --search "report"
python tools/tool_inventory_manager.py --search "consolidation"
```

Search results show the tool name, status, purpose, and path.

## Maintaining Tool Metadata

### Validating Metadata

Ensure all tools have proper metadata:

```bash
python tools/tool_inventory_manager.py --validate
```

Or use the repository health check:

```bash
python tools/repo_health_check.py --check-tool-metadata
```

### Required Metadata

All tools must include this metadata header:

```python
"""
Tool: [Tool Name]
Created: [YYYY-MM-DD]
Author: [Team/Individual]
Status: Active|Deprecated|Archived
Purpose: [Clear description of tool's purpose]
Dependencies: [Required packages/tools]
Lifecycle:
    - Created: [Why the tool was created]
    - Active: [Current usage status]
    - Obsolescence Conditions:
        1. [Condition under which tool becomes obsolete]
        2. [Additional condition if applicable]
Last Validated: [YYYY-MM-DD]

Detailed description...
"""
```

## Managing Tool Lifecycle

### Deprecating Tools

When a tool is being phased out but still needed:

```bash
python tools/tool_inventory_manager.py --deprecate tools/old_tool.py --reason "Being replaced by new implementation" --replacement "new_tool.py"
```

This updates the tool's status to "Deprecated" and adds a deprecation note with replacement information.

### Archiving Tools

When a tool is no longer actively used but has reference value:

```bash
python tools/tool_inventory_manager.py --archive tools/obsolete_tool.py --reason "Task completed, retaining for reference"
```

This:
1. Updates the tool's status to "Archived"
2. Adds an archival note with the reason
3. Moves the file to `tools/archive/`
4. Removes the original file

### Updating Documentation

After making changes to tool status or organization:

```bash
python tools/tool_inventory_manager.py --update-readme
```

This updates the `tools/README.md` file with the current inventory, categorized by tool type.

## Quarterly Review Process

Follow this process for quarterly tool inventory review:

1. **Generate Inventory Report**
   ```bash
   python tools/tool_inventory_manager.py --inventory
   ```

2. **Review Metadata Validity**
   ```bash
   python tools/tool_inventory_manager.py --validate
   ```

3. **Review Each Active Tool**
   - Check if it's still needed
   - Update "Last Validated" date in metadata

4. **Deprecate Tools Being Phased Out**
   ```bash
   python tools/tool_inventory_manager.py --deprecate tools/old_tool.py --reason "Reason" --replacement "replacement.py"
   ```

5. **Archive Tools No Longer Needed**
   ```bash
   python tools/tool_inventory_manager.py --archive tools/obsolete_tool.py --reason "Reason"
   ```

6. **Update Documentation**
   ```bash
   python tools/tool_inventory_manager.py --update-readme
   ```

7. **Commit Changes with Explanatory Message**
   ```bash
   git commit -m "Quarterly tool inventory update: archived X tools, deprecated Y tools"
   ```

## Integration with Development Workflow

1. **Creating New Tools**
   - Use the template: `cp tools/templates/tool_template.py tools/your_new_tool.py`
   - Fill in all metadata fields, especially lifecycle and obsolescence conditions
   - For one-off tools, clearly document when they'll be obsolete

2. **Before Committing**
   - Run `python tools/repo_health_check.py --check-tool-metadata`
   - Fix any metadata issues

3. **After Completing One-Off Tasks**
   - Archive the tool with a clear reason
   - Update the README

4. **Discovering Existing Tools**
   - Use `--search` to find tools for specific tasks before creating new ones

## Best Practices

1. **Tool Design**
   - Keep tools focused on a single responsibility
   - Clearly document dependencies
   - Include examples in docstrings

2. **Metadata Management**
   - Be specific about obsolescence conditions
   - Keep "Last Validated" date current
   - Document purpose clearly for searchability

3. **Archival Decisions**
   - Archive (don't delete) tools with reference value
   - Only delete tools with no future reference value
   - Document archival decisions in commit messages

4. **Documentation**
   - Keep README.md current
   - Generate inventory reports before team reviews
   - Document tool categories clearly 