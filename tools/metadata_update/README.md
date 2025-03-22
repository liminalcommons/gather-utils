# Tool Metadata Compliance Project

This directory contains tools to support the Tool Metadata Compliance Project, which aims to ensure all tools in the repository have standardized, complete metadata headers.

## Project Goals

1. Update all 32 tools with unknown status
2. Fix the 33 tools with invalid metadata 
3. Ensure 100% compliance with metadata standards

## Tools Overview

This package includes the following tools:

### 1. Metadata Injector (`metadata_injector.py`)

Injects standardized metadata into tool files, ensuring consistent format and required fields.

```bash
# Example usage
python tools/metadata_update/metadata_injector.py tools/bdd_coverage_report.py \
  --tool-name "BDD Coverage Report Generator" \
  --purpose "Generates coverage reports for BDD features and scenarios" \
  --dependencies "pandas, tabulate, matplotlib" \
  --created-reason "To visualize BDD test coverage" \
  --active-status "Used for regular coverage reporting" \
  --obsolescence "When replaced by integrated coverage solution" "When BDD testing approach changes"
```

### 2. Update Tracker (`update_tracker.py`)

Tracks progress of the metadata update project, providing status reports and suggesting batches of tools to update.

```bash
# Initialize tracking
python tools/metadata_update/update_tracker.py --init

# Show current status
python tools/metadata_update/update_tracker.py --status

# Generate status report
python tools/metadata_update/update_tracker.py --report

# Get next batch of tools to process
python tools/metadata_update/update_tracker.py --next-batch

# Mark a tool as completed
python tools/metadata_update/update_tracker.py --mark-completed tools/some_tool.py --batch "batch_1"
```

### 3. Batch Processor (`batch_processor.py`)

Processes multiple tools at once, automatically analyzing their content to suggest appropriate metadata.

```bash
# Process next batch of tools (default: 5)
python tools/metadata_update/batch_processor.py

# Process specific tools
python tools/metadata_update/batch_processor.py --tools tools/tool1.py tools/tool2.py

# Process larger batch
python tools/metadata_update/batch_processor.py --batch-size 10

# Process with custom batch ID
python tools/metadata_update/batch_processor.py --batch-id "bdd_tools_batch1"
```

## Workflow

### Setup

1. Initialize the tracking system:
   ```bash
   python tools/metadata_update/update_tracker.py --init
   ```

2. Generate initial status report:
   ```bash
   python tools/metadata_update/update_tracker.py --report
   ```

### Daily Update Process

1. Check current status:
   ```bash
   python tools/metadata_update/update_tracker.py --status
   ```

2. Process the next batch of tools:
   ```bash
   python tools/metadata_update/batch_processor.py
   ```

3. Verify updates:
   ```bash
   python tools/tool_inventory_manager.py --validate
   ```

4. Review status report:
   ```bash
   # View most recent report
   ls -ltr reports/tool_metadata_compliance/status_report_*.md | tail -1 | xargs cat
   ```

### Manual Updates

For tools requiring more specific metadata:

1. Analyze the tool:
   ```bash
   python tools/metadata_update/batch_processor.py --tools tools/specific_tool.py --batch-id "manual"
   ```

2. If needed, manually update using the metadata injector with more specific parameters:
   ```bash
   python tools/metadata_update/metadata_injector.py tools/specific_tool.py \
     --tool-name "Specific Tool Name" \
     --purpose "Detailed description of the tool's purpose" \
     --dependencies "dep1, dep2, dep3" \
     --created-reason "Specific reason for creation" \
     --active-status "Current detailed usage" \
     --obsolescence "Specific condition 1" "Specific condition 2"
   ```

3. Mark as completed:
   ```bash
   python tools/metadata_update/update_tracker.py --mark-completed tools/specific_tool.py --batch "manual"
   ```

## Project Completion

Once all tools have been updated:

1. Verify full compliance:
   ```bash
   python tools/tool_inventory_manager.py --validate
   ```

2. Update tools README:
   ```bash
   python tools/tool_inventory_manager.py --update-readme
   ```

3. Generate final status report:
   ```bash
   python tools/metadata_update/update_tracker.py --report
   ```

## Metadata Standards

All tools should include the following metadata:

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
"""
```

## Best Practices

1. **Batch Processing**: Process 5-7 tools per day to maintain quality
2. **Verification**: Always verify updates with `tool_inventory_manager.py --validate`
3. **Commit Strategy**: Commit each batch with a clear message: `"Update metadata for batch X (Y tools)"`
4. **Progress Tracking**: Regularly generate status reports for documentation
5. **Documentation**: Update the README.md with categorized tool inventory when complete

## Project Timeline

- Phase 1: Analysis and Planning (1 week)
- Phase 2: Template Creation (2-3 days)
- Phase 3: Implementation (2-3 weeks)
- Phase 4: Validation and Documentation (1 week)

Total project duration: 4-5 weeks 