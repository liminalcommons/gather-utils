# BDD Refactoring Examples

This directory contains examples that demonstrate our BDD refactoring tools and the standardized conventions we've established.

## Directory Structure

- `api_authentication.feature`: Example feature file following our conventions
- `steps/api_authentication_steps.py`: Example step definitions for the feature
- `generate_feature_example.sh`: Shell script demonstrating how to use the feature template generator

## Using the Feature Template Generator

The `generate_feature_example.sh` script demonstrates how to use our `bdd_feature_template.py` tool to generate standardized BDD feature files and step definitions. Run it to see the tool in action:

```bash
./examples/generate_feature_example.sh
```

This will create a new feature file and step definitions in the `examples/features/api` and `examples/steps/api` directories.

## API Authentication Example

The `api_authentication.feature` file demonstrates our standardized format:

- Feature-level and scenario-level tags following our conventions
- Well-structured Given-When-Then scenarios
- Background section for common setup
- Proper requirement and release tagging
- Scenario outlines with examples table

The matching `steps/api_authentication_steps.py` file shows:

- Standard step definition format
- Consistent method naming
- Proper error handling
- Use of assertions and matchers
- Documentation for each step

## BDD Conventions Demonstrated

These examples demonstrate several key conventions:

1. **Naming Conventions**:
   - Feature files: `<domain>_<functionality>.feature`
   - Step files: `<domain>_<functionality>_steps.py`

2. **Tag Conventions**:
   - Domain tags: `@API`
   - Functionality tags: `@AUTHENTICATION`
   - Requirement tags: `@REQ-API-101`
   - Release tags: `@REL-1`
   - Process tags: `@PROC-VALIDATION`

3. **Directory Structure**:
   - Features organized by domain
   - Step definitions matching feature organization

4. **Scenario Structure**:
   - Clear, descriptive scenario names
   - Consistent Given-When-Then format
   - Background for common preconditions
   - Scenario outlines for data-driven tests

## Using These Examples

Use these examples as templates when creating new BDD features or refactoring existing ones. The standardized format ensures consistency across the project and improves maintainability.

For more details, refer to the full BDD conventions document at `docs/project/bdd_conventions.md`.
