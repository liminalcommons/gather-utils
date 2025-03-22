# Comprehensive BDD Best Practices

## Table of Contents
1. [Feature File Organization](#feature-file-organization)
2. [Step Definitions](#step-definitions)
3. [Testing Tools and Analysis](#testing-tools-and-analysis)
4. [Documentation Requirements](#documentation-requirements)
5. [Quality Standards](#quality-standards)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Maintenance and Updates](#maintenance-and-updates)

## Feature File Organization

### Directory Structure
```
tests/bdd/features/
├── portal/              # Portal-related features
├── cli/                 # CLI-related features
├── documentation/       # Documentation-related features
├── testing/            # Testing-related features
├── system/             # Development system features
├── bdd/                # BDD-related features
└── agent/              # Agent-related features
```

### Feature File Template
```gherkin
@DOMAIN-TAG
Feature: [Feature Name]
  As a [Role]
  I want [Capability]
  So that [Benefit]

  Background:
    Given [common setup steps]

  # [Group 1] scenarios
  @REQ-MODULE-NUMBER @REL-NUMBER @COMPONENT
  Scenario: [Scenario Name]
    Given [precondition]
    When [action]
    Then [expected outcome]
    And [additional verification]
```

### Feature Writing Guidelines
1. **Single Responsibility**
   - Each feature should focus on one specific functionality
   - Group related scenarios within a feature
   - Use clear and descriptive names

2. **Proper Tagging**
   - Domain tags: `@DOMAIN-TAG`
   - Requirement tags: `@REQ-MODULE-NUMBER`
   - Release tags: `@REL-NUMBER`
   - Component tags: `@COMPONENT`

3. **Scenario Organization**
   - Group related scenarios with comments
   - Use Background for common setup
   - Keep scenarios independent
   - One behavior per scenario

## Step Definitions

### Organization
```python
# tests/bdd/steps/[domain]/[feature]_steps.py

"""Step definitions for [feature name]."""

from behave import given, when, then
from typing import Dict, List, Optional

@given('precondition')
def step_given_precondition(context) -> None:
    """Implement the step for: Given precondition"""
    try:
        # Implementation
        pass
    except Exception as e:
        raise AssertionError(f"Setup failed: {str(e)}")
```

### Best Practices
1. **Naming Convention**
   - Format: `step_<type>_<description>`
   - Types: given, when, then
   - Use lowercase and underscores
   - Be descriptive but concise

2. **Documentation**
   - Include comprehensive docstrings
   - Document parameters and return values
   - Explain error conditions
   - Add examples for complex steps

3. **Error Handling**
   - Use appropriate exception types
   - Provide clear error messages
   - Include context in errors
   - Clean up resources properly

4. **Code Organization**
   - Group related steps together
   - Use helper functions for common operations
   - Keep steps focused and simple
   - Follow DRY principles

## Testing Tools and Analysis

### BDD Validator
```bash
# Run BDD validation
python tools/bdd_validator.py

# Run as part of health check
python tools/repo_health_check.py --validate-bdd
```

### Analysis Tools
```bash
# Comprehensive analysis
python tools/bdd_comprehensive_analyzer.py

# Coverage report
python tools/bdd_coverage_report.py

# Duplication detection
python tools/bdd_duplication_analyzer.py --threshold 0.7
```

## Documentation Requirements

### Required Documentation
1. **Feature Level**
   - Clear user story format
   - Comprehensive scenarios
   - Tagged requirements
   - Usage examples

2. **Step Level**
   - Function documentation
   - Parameter descriptions
   - Error conditions
   - Example usage

3. **Project Level**
   - BDD overview
   - Best practices
   - Templates
   - Validation rules

### Status Tracking
```markdown
## BDD Implementation Status

### Current Phase
- Phase: [phase name]
- Completion: [percentage]
- Recent Changes:
  - [change 1]
  - [change 2]

### Feature Status Matrix
| Feature Group | Structure | Consolidated | Steps | Tests |
|--------------|-----------|--------------|-------|-------|
| Portal       | ✅        | ✅           | ✅    | ✅    |
| CLI          | ✅        | ❌           | ❌    | ❌    |
```

## Quality Standards

### Required Standards
1. **Traceability**
   - Every scenario has requirement tags
   - Clear mapping to requirements
   - Documented dependencies
   - Version tracking

2. **Code Quality**
   - Consistent naming
   - Proper error handling
   - Type hints
   - Documentation

3. **Test Quality**
   - Independent scenarios
   - Clear preconditions
   - Verifiable outcomes
   - Proper cleanup

4. **Documentation Quality**
   - Up-to-date
   - Clear and concise
   - Examples included
   - Properly formatted

## Troubleshooting Guide

### Common Issues

1. **Missing Steps**
   - Check existing step files
   - Verify step wording
   - Create new step if needed
   - Update documentation

2. **Import Errors**
   - Use absolute imports
   - Check dependencies
   - Verify module paths
   - Update requirements

3. **Parser Issues**
   - Review parser definitions
   - Check for conflicts
   - Use dedicated utilities
   - Test with examples

4. **Context Problems**
   - Verify initialization
   - Check data sharing
   - Ensure cleanup
   - Test isolation

## Maintenance and Updates

### Regular Tasks
1. **Monthly**
   - Run comprehensive analysis
   - Update documentation
   - Review test coverage
   - Check for duplicates

2. **Per Release**
   - Update status documents
   - Verify all features
   - Update templates
   - Review best practices

3. **Continuous**
   - Run validation on changes
   - Update documentation
   - Fix failing tests
   - Review pull requests

### Version Control
1. **Commit Messages**
   - Tag BDD-related commits
   - Include requirement IDs
   - Describe changes clearly
   - Reference issues

2. **Documentation Updates**
   - Keep README current
   - Update status documents
   - Maintain change history
   - Document decisions

## Support and Resources

### Getting Help
1. Check documentation
2. Review examples
3. Run validation tools
4. Contact team

### Additional Resources
- [Project Documentation](../README.md)
- [Technical Requirements](../TECHNICAL_REQUIREMENTS.md)
- [Definition of Done](../DEFINITION_OF_DONE.md)
- [BDD Test Status](../BDD_TEST_STATUS.md) 