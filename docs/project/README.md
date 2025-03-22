# Project System Overview

Welcome to the Portal Explorer development team! This document provides an overview of our project system, development processes, and key resources to help you onboard smoothly and become productive quickly.

## Development Initiatives

Our project currently has two major initiatives:

1. **Portal Explorer Product Development** - Building and enhancing our core product for exploring Gather.town spaces.

2. **BDD Refactoring Initiative** - A comprehensive effort to improve our testing framework through standardization, consolidation, and improved traceability.

## Repository Structure

The repository is organized as follows:

```
portal-explorer/
├── src/                   # Source code
│   └── gather_manager/    # Main package
│       ├── api/           # API client
│       ├── cli/           # Command-line interface
│       ├── models/        # Data models
│       ├── services/      # Business logic
│       └── utils/         # Utility functions
├── tests/                 # Test suite
│   ├── unit/              # Unit tests (TDD)
│   ├── integration/       # Integration tests
│   └── bdd/               # BDD tests
│       ├── features/      # Feature files (organized by domain)
│       └── steps/         # Step definitions
├── docs/                  # Documentation
│   ├── project/           # Project documentation
│   ├── api/               # API documentation
│   ├── user_guide/        # User guide
│   └── archive/           # Archived documentation
├── tools/                 # Utility scripts and tools
├── examples/              # Example code and usage
└── data/                  # Data files and analysis results
```

## Development Process

We follow a hybrid approach combining:

1. **Behavior-Driven Development (BDD)** - For specifying behavior from a user's perspective
2. **Test-Driven Development (TDD)** - For implementing and testing components

### Workflow

1. **Feature Definition**: Create BDD feature files (or update existing ones) based on requirements
2. **Component Tests**: Write unit tests for components (TDD approach)
3. **Implementation**: Implement functionality to pass both unit and BDD tests
4. **Validation**: Ensure all tests pass and the Definition of Done is met

## Key Tools

### Development Tools

- **Python 3.8+**: Our primary programming language
- **Poetry**: For dependency management
- **Pre-commit hooks**: For code style enforcement
- **pytest**: For unit testing
- **behave**: For BDD testing

### Custom Tools

Several custom tools have been developed to assist with the development process, particularly for BDD management:

1. **BDD Analysis Tools**:
   - `tools/bdd_duplication_analyzer.py`: Identifies duplicate or similar features/scenarios
   - `tools/bdd_comprehensive_analyzer.py`: Orchestrates all analysis tools

2. **BDD Refactoring Tools**:
   - `tools/bdd_feature_consolidator.py`: Merges duplicate scenarios
   - `tools/bdd_feature_reorganizer.py`: Implements directory structure reorganization
   - `tools/bdd_tag_standardizer.py`: Standardizes tags across features
   - `tools/bdd_feature_template.py`: Generates compliant feature templates

3. **Development System Tools**:
   - `tools/setup_style_tools.py`: Sets up style enforcement tools
   - `tools/fix_style_issues.py`: Fixes common style issues
   - `tools/run_bdd_tests.py`: Runs BDD tests with custom options
   - `tools/repo_health_check.py`: Validates repository structure

## Current Initiatives

### BDD Refactoring Initiative

A comprehensive effort to improve our testing framework through several releases:

1. **Release 1: Analysis & Standardization** (Complete)
   - Established BDD conventions and standards
   - Developed analysis tools
   - Created documentation

2. **Release 2: Feature Consolidation & Organization** (In Progress - 65% Complete)
   - Consolidating duplicate features
   - Implementing standardized directory structure
   - Resolving dependencies between step definitions

3. **Release 3: Traceability Enhancement** (Planning - 10% Complete)
   - Enhancing connection between requirements and BDD tests
   - Implementing coverage visualization

4. **Release 4: CI/CD Integration** (Early Planning - 5% Complete)
   - Automating validation and enforcement
   - Implementing quality gates

For more details, see the comprehensive [BDD Refactoring Initiative Summary](./bdd_refactoring_initiative_summary.md).

## Documentation

### Key Documents for New Developers

1. **Project Status**: [PROJECT_STATUS.md](./PROJECT_STATUS.md) - Current status and next steps
2. **Definition of Done**: [DEFINITION_OF_DONE.md](./DEFINITION_OF_DONE.md) - Criteria for completed work
3. **BDD Conventions**: [bdd_conventions.md](./bdd_conventions.md) - Standards for BDD features
4. **Maintenance Guidelines**: [MAINTENANCE_GUIDELINES.md](./MAINTENANCE_GUIDELINES.md) - Repository maintenance

### Initiative-Specific Documents

1. **BDD Refactoring Plan**: [plan-bdd-refactoring.md](./plan-bdd-refactoring.md) - Detailed plan for BDD improvements
2. **BDD Release 2 Status**: [bdd_refactoring_release2_status.md](./bdd_refactoring_release2_status.md) - Current status of Release 2
3. **Consolidation Strategy**: [consolidation_strategy.md](../reports/bdd_analysis/consolidation_strategy.md) - Strategy for feature consolidation

## Getting Started

### First-Day Setup

1. Clone the repository
2. Install dependencies with Poetry: `poetry install`
3. Set up pre-commit hooks: `python tools/setup_style_tools.py`
4. Configure your API credentials (see the main README.md)
5. Run repository validation: `python tools/repo_health_check.py --validate-for-agent`

### First Tasks for New Developers

1. Read the [Definition of Done](./DEFINITION_OF_DONE.md) document
2. Review the [BDD Conventions](./bdd_conventions.md)
3. Run the unit tests: `pytest tests/unit`
4. Run the BDD tests: `behave tests/bdd/features`
5. Review the [Project Status](./PROJECT_STATUS.md) document to understand current work

### Contribution Workflow

1. Check the [Project Status](./PROJECT_STATUS.md) for current priorities
2. Select a task or contact your team lead for assignment
3. Create a branch for your work
4. Implement changes following TDD and BDD practices
5. Ensure all tests pass
6. Submit a pull request
7. Address any feedback from code reviews

## AI Agent Workflow

As an AI assistant working on this project, follow these specific workflows:

### Starting a New Task

1. **Repository Validation**: Always run `python tools/repo_health_check.py --validate-for-agent` first
2. **Project Status Check**: Review the current [Project Status](./PROJECT_STATUS.md)
3. **Task Analysis**: Determine whether the task involves implementation, analysis, or refactoring
4. **Agent Guidelines**: Review the agent guidelines in `.cursor/rules/agent_guidelines.mdc` and `.cursor/rules/bdd_agent_guidelines.mdc`

### Navigation Patterns

1. **Documentation-First Approach**:
   - Begin with project documentation in `docs/project/`
   - Examine tests to understand expected behavior
   - Use semantic search for targeted code exploration

2. **Decision Framework**:
   - For new features: Create BDD features first, then implement with TDD
   - For debugging: Run tests, analyze code, propose specific fixes
   - For refactoring: Ensure tests pass before and after changes

### Task Completion

1. **Verification Checklist**:
   - All relevant tests pass
   - Code passes linter checks
   - Documentation is updated
   - Changes comply with Definition of Done
   - No regression in existing functionality

2. **Session Documentation**:
   - Update relevant status documents
   - Create or update continuation context in `docs/project/continuation_prompt.md`
   - Provide a session summary of accomplishments and next steps

## Common Issues and Solutions

### BDD Test Failures

If BDD tests are failing, check:
1. Step definition imports - There may be dependency issues in progress
2. Feature file tags - Ensure they follow conventions
3. Parser references - Some step files may have parser reference issues

### Import Errors

If you encounter import errors:
1. Check the directory structure - We're in the process of reorganizing
2. Review recent changes to imports in affected files
3. Consult the consolidation strategy document for guidance

### Repository Structure Issues

If repository validation fails:
1. Check for missing required directories
2. Verify file naming conventions
3. Ensure documentation is in the correct location
4. Run `python tools/repo_health_check.py` for detailed error information

## Team Communication

- **Daily Standups**: 10:00 AM EST
- **Weekly Planning**: Mondays at 2:00 PM EST
- **Sprint Reviews**: Fridays at 3:00 PM EST
- **Documentation Updates**: Required for all completed tasks

## Seeking Help

1. Check this documentation first
2. Review related BDD features and step definitions
3. Consult the project's tools directory for utility scripts
4. Ask in the team channel
5. Contact the BDD Refactoring team for specific BDD-related questions

## Essential Commands Reference

```bash
# Validate repository structure
python tools/repo_health_check.py --validate-for-agent

# Run BDD tests with specific tags
python tools/run_bdd_tests.py --tags=REQ-1.1

# Generate BDD coverage report
python tools/bdd_coverage_report.py

# Check style issues
python tools/fix_style_issues.py --check

# Run feature consolidation
python tools/feature_file_consolidation.py
```

## Next Steps

After completing initial onboarding:

1. Familiarize yourself with the BDD Refactoring Initiative
2. Review the Portal Explorer code structure
3. Set up your local environment for both development and testing
4. Work on small tasks to understand the workflow
5. Join initiative discussions to provide fresh perspective

Welcome aboard! We're excited to have you join the team. 