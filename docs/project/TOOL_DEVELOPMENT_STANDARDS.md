# Tool Development Standards

This document outlines the standards for developing, documenting, and maintaining tools within the Portal Explorer project.

Last Updated: 2024-03-21

## Tool Lifecycle Management

### 1. Tool Categories

Tools in our codebase fall into the following categories:

- **Core Tools**: Essential for regular development (e.g., `repo_health_check.py`)
- **Feature-specific Tools**: Support specific features or components
- **One-off Tools**: Developed for a single specific task
- **Analysis Tools**: Used for codebase or data analysis
- **CI/CD Tools**: Support continuous integration and deployment

### 2. Required Metadata

All tools must include a metadata header at the top of the file:

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

### 3. Tool Statuses

- **Active**: Currently used and maintained
- **Deprecated**: Still available but being phased out (with replacement indicated)
- **Archived**: Moved to archive for reference but no longer actively used

### 4. Lifecycle Management Workflow

1. **Creation**:
   - Use the template at `tools/templates/tool_template.py`
   - Fill in all metadata fields
   - Document dependencies and usage

2. **Validation**:
   - Update "Last Validated" date when confirming a tool is still needed
   - Run quarterly validation on all active tools
   - Use `python tools/tool_inventory_manager.py --validate` to check metadata compliance

3. **Cleanup**:
   - Archive tools that have reference value using `python tools/tool_inventory_manager.py --archive`
   - Delete tools that serve no future purpose
   - Document cleanup decisions in commit messages
   - Use `python tools/tool_inventory_manager.py --update-readme` to update documentation

## Development Standards

### 1. Code Organization

- All tools should be placed in the `tools/` directory
- Complex tools may use subdirectories for organization
- Templates should be placed in `tools/templates/`

### 2. Code Quality

- All tools must follow project code style guidelines
- Include appropriate error handling
- Use argparse for command-line arguments
- Provide helpful usage information via --help

### 3. Testing

- Core tools should have unit tests
- One-off tools may have minimal or manual testing
- Document test procedures for complex tools

### 4. Documentation

- Include usage examples in docstrings
- Update README.md when adding new tools
- Document any side effects or file modifications

## Implementation Patterns

### 1. Simple Scripts

For simple one-off scripts:
```python
#!/usr/bin/env python3
"""
Tool: Simple Script
...metadata...
"""

def main():
    # Simple implementation
    pass

if __name__ == "__main__":
    main()
```

### 2. Complex Tools

For tools with multiple functions and complex logic:
```python
#!/usr/bin/env python3
"""
Tool: Complex Tool
...metadata...
"""

import argparse
# other imports

class ToolName:
    """Class encapsulating tool functionality."""
    
    def __init__(self, args):
        # Setup
        pass
        
    def method1(self):
        # Implementation
        pass
        
    # Other methods

def parse_args():
    # Argument parsing
    pass

def main():
    args = parse_args()
    tool = ToolName(args)
    # Run tool
    
if __name__ == "__main__":
    main()
```

### 3. Analysis Tools

For data analysis tools:
```python
#!/usr/bin/env python3
"""
Tool: Analysis Tool
...metadata...
"""

import pandas as pd
# other imports

def load_data(path):
    # Data loading
    pass
    
def analyze_data(data):
    # Analysis
    pass
    
def generate_report(results, output_path):
    # Report generation
    pass
    
def main():
    # Orchestration
    pass
    
if __name__ == "__main__":
    main()
```

## Automation and Enforcement

1. **Repository Health Check**:
   - `repo_health_check.py` validates tool metadata
   - Run before commits to ensure compliance
   - Use `python tools/repo_health_check.py --check-tool-metadata` for specific checks

2. **Tool Inventory Management**:
   - Use `tool_inventory_manager.py` to maintain tool inventory
   - Generate reports with `--inventory` option
   - Search tools with `--search` option
   - Archive tools with `--archive` option
   - Deprecate tools with `--deprecate` option

3. **CI/CD Integration**:
   - Automated validation of tool metadata
   - Fail pipelines for non-compliant tools

4. **Quarterly Review**:
   - Review all tools for relevance
   - Update "Last Validated" dates
   - Archive or delete obsolete tools
   - Generate inventory report for documentation

## Templates

Use the following template to create new tools:
```bash
cp tools/templates/tool_template.py tools/your_new_tool.py
```

This provides a pre-filled metadata block and basic structure.

## Best Practices

1. **Keep Tools Focused**:
   - Each tool should have a single responsibility
   - Consider breaking complex tools into smaller components

2. **Error Handling**:
   - Provide clear error messages
   - Return appropriate exit codes
   - Log errors with context

3. **Documentation**:
   - Document edge cases and limitations
   - Include example commands
   - Explain outputs and side effects

4. **Lifecycle Planning**:
   - Consider obsolescence conditions at creation time
   - Plan for eventual replacement or cleanup
   - Document dependencies that might affect lifecycle 