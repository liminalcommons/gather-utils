# BDD Naming and Organization Conventions

## Overview

This document defines the standardized naming conventions, tagging system, and organizational structure for Behavior-Driven Development (BDD) features in our project. Following these conventions ensures consistency, improves maintainability, and enhances traceability between requirements and tests.

## File Structure

### Directory Organization

BDD files should be organized in the following directory structure:

```
tests/bdd/
├── features/               # Gherkin feature files
│   ├── core/               # Core functionality features
│   ├── cli/                # Command-line interface features
│   ├── api/                # API functionality features
│   ├── models/             # Data model features
│   ├── process/            # Process improvement features
│   └── release_plans/      # Release planning features
├── steps/                  # Step definitions
│   ├── core/               # Core functionality step definitions
│   ├── cli/                # CLI step definitions
│   ├── api/                # API step definitions
│   ├── models/             # Data model step definitions
│   ├── process/            # Process step definitions
│   └── common/             # Shared step definitions
└── environment.py          # Test environment configuration
```

### File Naming Conventions

#### Feature Files

Feature files should follow this naming pattern:
```
[domain]_[functionality].feature
```

Examples:
- `cli_command_execution.feature`
- `api_client_authentication.feature`
- `model_portal_validation.feature`
- `process_development_improvement.feature`

#### Step Definition Files

Step definition files should match their corresponding feature files:
```
[domain]_[functionality]_steps.py
```

Examples:
- `cli_command_execution_steps.py`
- `api_client_authentication_steps.py`
- `model_portal_validation_steps.py`
- `process_development_improvement_steps.py`

Common steps that are shared across multiple features should be placed in:
```
common_[functionality]_steps.py
```

## Feature File Structure

### Feature Description

Each feature file should start with a clear feature description following this format:

```gherkin
Feature: [Concise Feature Name]
  As a [role]
  I want [capability]
  So that [benefit/value]
```

Example:
```gherkin
Feature: Portal Exploration Command
  As a Space Administrator
  I want to explore portals through a command-line interface
  So that I can quickly analyze portal structures in my Gather.town space
```

### Background Section

Use Background sections for common preconditions that apply to all scenarios in a feature:

```gherkin
Background:
  Given [common precondition]
  And [another common precondition]
```

Example:
```gherkin
Background:
  Given I have a valid API key
  And I have access to a Gather.town space
```

### Scenario Structure

Scenarios should follow this structure:

```gherkin
@[tags]
Scenario: [Descriptive Name]
  Given [precondition]
  When [action]
  Then [expected outcome]
  And [additional verification]
```

Example:
```gherkin
@REQ-CLI-1 @Portal
Scenario: List portals in a specific map
  Given I have a map with ID "abcd1234"
  When I run the command "gather-manager explore --map-id abcd1234"
  Then I should see a list of portals in the map
  And each portal should display its coordinates and target
```

### Scenario Outlines

For data-driven tests, use Scenario Outlines:

```gherkin
@[tags]
Scenario Outline: [Descriptive Name with Parameters]
  Given [precondition with <parameter>]
  When [action with <parameter>]
  Then [expected outcome with <parameter>]

  Examples:
    | parameter | other_parameter |
    | value1    | result1         |
    | value2    | result2         |
```

## Tagging Conventions

### Requirement Tags

Requirement tags link scenarios to specific requirements:

```
@REQ-[domain]-[number]
```

Examples:
- `@REQ-CLI-1` - Command Line Interface requirement #1
- `@REQ-API-3` - API requirement #3
- `@REQ-MODEL-2` - Model requirement #2

### Release Tags

Release tags indicate which release a scenario is part of:

```
@REL-[number]
```

Examples:
- `@REL-1` - Part of Release 1
- `@REL-2` - Part of Release 2

### Component Tags

Component tags categorize scenarios by component:

```
@[ComponentName]
```

Examples:
- `@Portal` - Related to portal functionality
- `@API` - Related to API functionality
- `@CLI` - Related to command-line interface

### Process Tags

Process tags categorize scenarios related to development processes:

```
@[ProcessName]
```

Examples:
- `@BDD` - Related to BDD process
- `@TDD` - Related to TDD process
- `@DoD` - Related to Definition of Done

## Step Definition Conventions

### Step Definition Format

Step definitions should follow this pattern:

```python
@[step_type]("[step pattern]")
def step_impl(context):
    # Implementation
    pass
```

### Naming Conventions

Step definition functions should be named descriptively:

```python
@given("I have a valid API key")
def given_i_have_valid_api_key(context):
    # Implementation
    pass
```

### Parameter Passing

For steps with parameters, use proper regex patterns:

```python
@when('I run the command "gather-manager {command}"')
def when_i_run_command(context, command):
    # Implementation using the command parameter
    pass
```

### Step Groups

Group related steps together in the step definition files, with clear comments:

```python
# Authentication steps
@given("I have a valid API key")
def given_i_have_valid_api_key(context):
    # Implementation
    pass

# Command execution steps
@when('I run the command "gather-manager {command}"')
def when_i_run_command(context, command):
    # Implementation
    pass
```

## Scenario Detail Guidelines

### Level of Detail

Scenarios should:
- Be specific enough to clearly communicate intent
- Not be overly detailed with implementation specifics
- Focus on behavior rather than implementation
- Include only relevant preconditions and verifications

### Good Examples

```gherkin
# Good - Clear, focused on behavior
Scenario: List portals in a specific map
  Given I have a map with ID "abcd1234"
  When I run the command "gather-manager explore --map-id abcd1234"
  Then I should see a list of portals in the map
  And each portal should display its coordinates and target
```

### Poor Examples

```gherkin
# Too vague
Scenario: Explore map
  Given I have a map
  When I explore it
  Then I should see information
  
# Too implementation-specific
Scenario: List portals in a specific map
  Given I have instantiated a GatherClient with API key "xyz123"
  And I have created a MapExplorer object for map ID "abcd1234"
  When I call the explore_map method with parameters format="table", depth=1
  Then the output should contain a JSON array with portal objects
  And each JSON object should have x, y, targetX, targetY fields
```

## Traceability Guidelines

### Requirement to Feature Mapping

Each BDD feature should clearly indicate which requirements it covers through tags.

### Feature to Scenario Mapping

Within each feature, scenarios should cover specific aspects of the requirements.

### Scenario to Step Mapping

Steps should implement the detailed verification of the scenarios.

### Documentation

The relationships between requirements, features, scenarios, and steps should be documented in:
- BDD coverage reports
- Requirements traceability matrix
- Release validation criteria

## Implementation Guidelines

### New Features

When creating new features:
1. Check if the requirement is already covered
2. Follow the naming conventions
3. Use appropriate tags
4. Create step definitions in the correct files
5. Verify the feature executes without errors

### Modifying Features

When modifying existing features:
1. Maintain consistent tagging
2. Update step definitions as needed
3. Verify no regressions in existing functionality
4. Update documentation

## Success Criteria

A well-structured BDD feature should:
- Follow the naming conventions
- Use appropriate tags
- Have clear scenarios
- Be organized in the correct directory
- Have implemented step definitions
- Execute successfully
- Be traceable to requirements

By following these conventions, we ensure a consistent, maintainable, and traceable BDD framework that supports our development process. 