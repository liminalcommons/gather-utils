# BDD Documentation

This directory contains automatically generated documentation for our BDD implementation.

Last Updated: 2024-03-21

## Related Documentation

- [BDD Testing Guide](../../tests/bdd/README.md): Guide for writing and running BDD tests
- [BDD Tools](../../tools/README.md#bdd-tools): Documentation for BDD-specific tools
- [BDD Conventions](../project/bdd/conventions.md): Standards for BDD features

## Structure

```
docs/bdd/
├── features/          # Individual feature documentation
├── steps/            # Step definition catalog
├── requirements/     # Requirements coverage analysis
└── index.md         # Main documentation index
```

## Documentation Components

1. **Feature Documentation**
   - Detailed feature specifications
   - Scenario descriptions
   - Example tables
   - Implementation details
   - Requirement traceability

2. **Step Catalog**
   - Available step definitions
   - Implementation details
   - Usage examples
   - Best practices

3. **Requirements Coverage**
   - Feature-requirement mapping
   - Coverage analysis
   - Implementation status
   - Domain-based organization

## Generation

The documentation is automatically generated using the `tools/bdd_docs_generator.py` script. This happens:
1. Automatically on commit (via pre-commit hook)
2. During CI/CD pipeline execution
3. On-demand using the script directly

### Manual Generation

To generate the documentation manually:

```bash
python tools/bdd_docs_generator.py
```

### Configuration

The documentation generator uses templates in `tools/templates/`:
- `index.md.j2`: Main index template
- `feature.md.j2`: Feature documentation template
- `step_catalog.md.j2`: Step catalog template
- `requirements.md.j2`: Requirements coverage template

## Best Practices

1. **Documentation Updates**
   - Documentation is generated automatically
   - Don't edit generated files manually
   - Update templates if format changes are needed

2. **Feature Writing**
   - Follow the user story format
   - Include proper tags
   - Provide clear descriptions
   - Use consistent wording

3. **Step Definitions**
   - Write comprehensive docstrings
   - Include type hints
   - Document exceptions
   - Follow naming conventions

4. **Requirements**
   - Use proper requirement tags
   - Maintain traceability
   - Keep coverage high
   - Document changes

## Integration

The documentation system integrates with:
1. Pre-commit hooks
2. CI/CD pipeline
3. Development workflow
4. Code review process

For more information about the BDD refactoring initiative, see:
- [BDD Refactoring Plan](../project/plan-bdd-refactoring.md)
- [BDD Refactoring Status](../project/bdd_refactoring_release2_status.md)
- [Project Status](../project/PROJECT_STATUS.md)

## Contributing

When contributing:
1. Ensure features are well-documented
2. Follow the established formats
3. Update templates if needed
4. Review generated docs before commit
