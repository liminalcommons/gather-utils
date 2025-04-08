---
Title: Repository Health Check Enhancements for Lifecycle Management
Created: 2024-03-21
Last Updated: 2024-03-21
Status: Draft
Owner: Development Team
Purpose: Define enhancements to repo_health_check.py for lifecycle metadata validation
Audience: Development Team
Lifecycle:
  - Created: To ensure consistent validation of lifecycle metadata
  - Active: To be implemented after review
  - Obsolescence Conditions:
    1. When implemented in the actual tool
    2. If replaced by a more comprehensive validation approach
Last Validated: 2024-03-21
---

# Repository Health Check Enhancements for Lifecycle Management

This document outlines the proposed enhancements to the `repo_health_check.py` tool to validate lifecycle metadata across all artifact types, ensuring consistency and completeness.

## Overview

The repository health check tool should be extended to validate lifecycle metadata for:
1. Tools
2. Documentation
3. BDD artifacts
4. Project management documents
5. Code components

## Validation Rules

### Common Metadata Fields

For all artifacts, validate:
- Creation date exists and is in valid format (YYYY-MM-DD)
- Last updated date exists and is in valid format
- Status is specified and is one of: Draft, Active, Deprecated, Archived
- Last validated date exists and is not more than 90 days old
- Obsolescence conditions are defined

### Tool-Specific Validation

For tools (`tools/*.py`):
- Complete metadata header exists
- Tool purpose is clearly defined
- Dependencies are listed
- One-off tools have cleanup plan

### Documentation-Specific Validation

For documentation (`docs/**/*.md`):
- Title is specified
- Purpose is defined
- Audience is specified
- Lifecycle stages are documented

### BDD-Specific Validation

For BDD features (`tests/bdd/features/**/*.feature`):
- Metadata header exists
- Status is specified
- Owner is identified
- Acceptance criteria are defined

### Project Management-Specific Validation

For project documents (`docs/project/current/*.md`):
- Project scope and objectives are defined
- Success criteria are specified
- Timeline information exists
- Current status is up-to-date

## Implementation Approach

### 1. Add Metadata Validation Classes

```python
class LifecycleMetadataValidator:
    """Base class for validating lifecycle metadata."""

    def validate(self, file_path):
        """Validate common metadata fields."""
        # Implementation

    def validate_dates(self, metadata):
        """Validate date formats and recency."""
        # Implementation

    def validate_status(self, metadata):
        """Validate status field."""
        # Implementation


class ToolMetadataValidator(LifecycleMetadataValidator):
    """Validates tool-specific metadata."""

    def validate(self, file_path):
        """Validate tool metadata."""
        super().validate(file_path)
        # Tool-specific validation


class DocumentationMetadataValidator(LifecycleMetadataValidator):
    """Validates documentation-specific metadata."""

    def validate(self, file_path):
        """Validate documentation metadata."""
        super().validate(file_path)
        # Documentation-specific validation

# Similar classes for BDD, Project Management, and Code
```

### 2. Add Command-Line Option

```python
parser.add_argument(
    "--validate-lifecycle-metadata",
    action="store_true",
    help="Validate lifecycle metadata across all artifact types"
)
```

### 3. Integration with Existing Checks

```python
def validate_repository_health(args):
    """Validate repository health based on command line args."""
    # Existing validation code

    if args.validate_lifecycle_metadata:
        validate_lifecycle_metadata()

def validate_lifecycle_metadata():
    """Validate lifecycle metadata across all artifact types."""
    # Implementation using validator classes
```

## Reporting

The tool should generate a comprehensive report showing:
1. Overall compliance percentage
2. Missing metadata fields by artifact type
3. Artifacts needing validation (last validated > 90 days)
4. Artifacts with unclear obsolescence conditions
5. Recommendations for improvement

## Success Criteria

The enhanced tool should:
1. Detect at least 95% of metadata issues
2. Generate clear, actionable reports
3. Provide specific line numbers and file locations for issues
4. Include suggestions for fixing common issues
5. Run efficiently (< 30 seconds for full validation)

## Next Steps

1. Implement metadata parsing for each artifact type
2. Develop validation rules
3. Create reporting mechanism
4. Add command-line options
5. Test with various artifacts
6. Document usage in tool help text

## Integration with CI/CD

This validation should be integrated into the CI/CD pipeline to:
1. Flag PRs that introduce metadata issues
2. Generate periodic reports on lifecycle metadata health
3. Track improvement over time
