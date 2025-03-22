# BDD Implementation Guide

## Quick Reference

### Directory Structure
```
tests/bdd/
├── features/          # Feature files organized by domain
│   ├── portal/       # Portal-related features
│   ├── cli/          # CLI-related features
│   └── ...
├── steps/            # Step definitions
│   ├── portal/       # Portal-related steps
│   ├── cli/          # CLI-related steps
│   └── ...
└── environment.py    # Test environment setup
```

### Feature File Template
```gherkin
@DOMAIN-TAG
Feature: Feature Name
  As a [role]
  I want [capability]
  So that [benefit]

  @REQ-MODULE-NUMBER @REL-NUMBER @COMPONENT
  Scenario: Scenario Name
    Given [precondition]
    When [action]
    Then [expected outcome]
```

### Step Definition Template
```python
@given('precondition')
def step_given_precondition(context) -> None:
    """Implement the step for: Given precondition"""
    try:
        # Implementation
        pass
    except Exception as e:
        raise AssertionError(f"Setup failed: {str(e)}")
```

## Tools and Validation

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
```

## Documentation Structure

- [Best Practices](best_practices.md): Comprehensive guide to our BDD practices
- [Templates](templates/): Feature and step definition templates
- [Validation Rules](validation/bdd_rules.json): Machine-readable validation rules
- [Lifecycle Management](lifecycle_management.md): Guidelines for managing BDD artifacts throughout their lifecycle

## Getting Started

1. Read [best_practices.md](best_practices.md) for detailed guidelines
2. Use templates from the [templates](templates/) directory
3. Run validation tools before committing changes
4. Check example implementations in `tests/bdd/features/examples/`

## Integration Points

### CI/CD Pipeline
BDD validation is integrated into our CI/CD pipeline:
- Pre-commit hooks validate BDD files
- GitHub Actions run comprehensive validation
- Test results are reported in PR comments

### IDE Integration
VSCode settings for BDD development:
```json
{
  "files.associations": {
    "*.feature": "gherkin"
  },
  "editor.codeActionsOnSave": {
    "source.fixAll.bdd": true
  }
}
```

## Best Practices Summary

1. **Feature Organization**
   - Group related features by domain
   - Use consistent tagging
   - Include clear user stories

2. **Step Definitions**
   - Follow naming conventions
   - Include comprehensive docstrings
   - Handle errors appropriately
   - Use type hints

3. **Testing Principles**
   - Write scenarios from user perspective
   - One behavior per scenario
   - Use background for common setup
   - Keep steps focused and reusable

4. **Documentation**
   - Keep documentation up to date
   - Include examples
   - Document complex steps
   - Maintain traceability

## Contributing

1. Use templates for new features and steps
2. Run validation before committing
3. Update documentation as needed
4. Follow the [Definition of Done](../DEFINITION_OF_DONE.md)

## Related Documentation

- [Project Status](../PROJECT_STATUS.md)
- [Definition of Done](../DEFINITION_OF_DONE.md)
- [Technical Requirements](../TECHNICAL_REQUIREMENTS.md)
- [BDD Test Status](../BDD_TEST_STATUS.md)

## Support

For questions or issues:
1. Check existing documentation
2. Review example implementations
3. Run validation tools
4. Contact the development team
