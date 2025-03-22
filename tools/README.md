# Development Tools

This directory contains tools for development, testing, and maintenance of the Portal Explorer project.

Last Updated: 2024-03-21

## Available Tools

### BDD Tools

- `bdd_test_runner.py`: Primary test runner for BDD tests with parallel execution, performance metrics, and detailed reporting
- `bdd_duplication_analyzer.py`: Analyze BDD features and scenarios for patterns and issues
- `bdd_feature_template.py`: Supports BDD testing and development workflows
- `bdd_verification.py`: Supports BDD testing and development workflows
- `bdd_feature_reorganizer.py`: Supports BDD testing and development workflows
- `bdd_docs_generator.py`: Generate documentation from BDD feature files
- `run_bdd_tests.py`: Supports BDD testing and development workflows
- `bdd_tag_standardizer.py`: Standardize tags in BDD feature files
- `bdd_scenario_generator.py`: Supports BDD testing and development workflows
- `cleanup_bdd_structure.py`: Supports BDD testing and development workflows
- `bdd_traceability_matrix.py`: Supports BDD testing and development workflows
- `bdd_coverage_report.py`: Generates coverage reports for BDD features and scenarios
- `update_bdd_docs.py`: Generate documentation from BDD feature files
- `bdd_validator.py`: Validate BDD feature files for compliance with standards
- `bdd_gap_analysis.py`: Supports BDD testing and development workflows
- `bdd_feature_consolidator.py`: Consolidate similar or duplicate BDD features
- `bdd_comprehensive_analyzer.py`: Analyze BDD features and scenarios for patterns and issues

### CI/CD Tools

- `repo_health_check.py`: Validate system configuration and dependencies
- `check_env.py`: Validate system configuration and dependencies

### Core Tools

- `setup_style_tools.py`: Set up development environment or tools
- `tool_inventory_manager.py`: Inventory, evaluate, and manage tools in the codebase
- `fix_style_issues.py`: Fix issues or clean up in the codebase
- `final_cleanup.py`: Fix issues or clean up in the codebase
- `step_definition_consolidation.py`: Tool for step definition consolidation
- `feature_file_consolidation.py`: Tool for feature file consolidation
- `config_cleanup.py`: Fix issues or clean up in the codebase
- `step_verification.py`: Tool for step verification
- `manage_releases.py`: Tool for manage releases
- `tool_template.py`: Tool for tool template
- `batch_processor.py`: Process multiple tools at once to update their metadata
- `metadata_injector.py`: Inject standardized metadata into tool files to ensure compliance with tool development standards

### Documentation Tools

- `build_docs.py`: Build project artifacts or documentation

### Repository Tools

- `repo_reconcile.py`: Tool for repo reconcile
- `update_tracker.py`: Track and report on the progress of the Tool Metadata Compliance Project

### TDD Tools

- `tdd_validator.py`: Tool for tdd validator

## Archived Tools

The following tools have been archived in `tools/archive/` for reference:
- `migrate_missing_steps.py`: Tool for migrate missing steps
- `bdd_consolidation.py`: Supports BDD testing and development workflows
- `migrate_bdd_tests.py`: Supports BDD testing and development workflows

## Usage

### Repository Validation

```bash
python tools/repo_health_check.py --validate-for-agent
```

### BDD Testing

```bash
# Run BDD tests with specific tags
python tools/run_bdd_tests.py --tags=REQ-1.1

# Generate BDD coverage report
python tools/bdd_coverage_report.py

# Generate BDD documentation
python tools/bdd_docs_generator.py
```

### Style Management

```bash
# Set up style tools
python tools/setup_style_tools.py

# Fix style issues
python tools/fix_style_issues.py --check
```

### Tool Management

```bash
# Generate a tool inventory report
python tools/tool_inventory_manager.py --inventory

# Search for tools matching a keyword
python tools/tool_inventory_manager.py --search "BDD"

# Validate tool metadata
python tools/tool_inventory_manager.py --validate

# Archive an obsolete tool
python tools/tool_inventory_manager.py --archive tools/obsolete_tool.py --reason "Functionality now provided by new_tool.py"

# Mark a tool as deprecated
python tools/tool_inventory_manager.py --deprecate tools/old_tool.py --reason "Being phased out" --replacement "new_tool.py"

# Update the tools/README.md with current tool inventory
python tools/tool_inventory_manager.py --update-readme
```

## Integration with CI

These tools are integrated with the CI pipeline using GitHub Actions:
- `.github/workflows/bdd-tests.yml`: BDD test workflow
- `.github/workflows/style-checks.yml`: Style check workflow
- `.github/workflows/docs-generation.yml`: Documentation generation workflow

## Best Practices

1. **Before Commits**:
   - Run repository validation
   - Run style checks
   - Run BDD tests
   - Generate documentation

2. **During Development**:
   - Use feature template generator for new features
   - Run duplication analyzer when modifying features
   - Use coverage reports to ensure test coverage

3. **Documentation**:
   - Keep documentation up-to-date
   - Use documentation generator for BDD docs
   - Update this README when adding new tools

4. **Tool Management**:
   - Document purpose and expected lifecycle when creating new tools
   - After successful use of one-off tools:
     - Archive if needed for reference (in tools/archive/)
     - Delete if no longer needed
   - Document tool status changes in commit messages
   - Consider generalizing useful one-off tools

5. **Required Tool Metadata**:
   Each tool must include a metadata header with:
   ```python
   """
   Tool: [Tool Name]
   Created: [Creation Date]
   Author: [Team/Individual]
   Status: [Active/Archived/Deprecated]
   Purpose: [Clear description of tool's purpose]
   Dependencies: [Required packages/tools]
   Lifecycle:
       - Created: [Why the tool was created]
       - Active: [Current usage status]
       - Obsolescence Conditions: [Conditions under which tool becomes obsolete]
   Last Validated: [Date last checked for relevance]
   """
   ```
   This metadata helps track tool lifecycle and makes cleanup decisions more systematic.

## Tool Inventory and Lifecycle Management

The `tool_inventory_manager.py` helps maintain a well-organized tools directory by:

1. **Tool Inventory**:
   - Automatically generates a comprehensive inventory of all tools
   - Creates reports in HTML, CSV, JSON, or Markdown formats
   - Shows tool status, metadata validity, and lifecycle information

2. **Tool Discovery**:
   - Provides search functionality to find the right tool for a job
   - Organizes tools by category and status
   - Updates README.md with categorized tool listings

3. **Tool Lifecycle Management**:
   - Validates tool metadata compliance
   - Allows marking tools as deprecated or archived
   - Manages the archival process (updating metadata and moving to archive)

4. **Recommended Workflow**:
   - Run quarterly tool inventory: `python tools/tool_inventory_manager.py --inventory`
   - Validate metadata compliance: `python tools/tool_inventory_manager.py --validate`
   - For one-off tools, add archival conditions in metadata
   - After successful completion of one-off task, archive the tool
   - For deprecated tools, indicate replacement in metadata

5. **Integration with repo_health_check.py**:
   - Tool metadata validation is part of repository health checks
   - Ensure all tools have valid metadata before commits
   - Run `python tools/repo_health_check.py --check-tool-metadata` to validate

## Archived Tools

The following tools have been archived in `tools/archive/` for reference:
- `bdd_consolidation.py`: Main BDD consolidation orchestrator
- `analyze_bdd_features.sh`: BDD analysis patterns and scripts
- `migrate_bdd_tests.py`: Test migration patterns and procedures
- `migrate_missing_steps.py`: Step definition migration procedures

These tools document important processes and patterns but are not actively used.

For more information about the development process and tools, see:
- [Project System Documentation](../docs/project/README.md)
- [BDD Documentation](../docs/bdd/README.md)
- [BDD Testing Guide](../tests/bdd/README.md)
