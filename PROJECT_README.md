# Portal Explorer Project System

This document provides a high-level overview of the Portal Explorer project system for developers. For a more comprehensive guide, please refer to the [detailed project system documentation](docs/project/README.md).

## Quick Start for New Developers

1. **Set Up Your Environment**
   ```bash
   # Clone the repository
   git clone <repository-url>
   
   # Install dependencies
   poetry install
   
   # Set up pre-commit hooks
   python tools/setup_style_tools.py
   
   # Validate repository structure (REQUIRED)
   python tools/repo_health_check.py --validate-for-agent
   ```

2. **Configure API Credentials**
   See the main [README.md](README.md) for detailed instructions.

3. **Run Tests**
   ```bash
   # Run unit tests
   pytest tests/unit
   
   # Run BDD tests
   behave tests/bdd/features
   ```

## Key Development Processes

- We follow a hybrid approach combining **Behavior-Driven Development (BDD)** and **Test-Driven Development (TDD)**
- All code changes should be accompanied by appropriate tests
- All work must meet the criteria in our [Definition of Done](docs/project/DEFINITION_OF_DONE.md)

## Current Initiatives

1. **Portal Explorer Product Development** - Building and enhancing our core product
2. **BDD Refactoring Initiative** - Improving our testing framework (currently in Release 2 - 65% complete)

## Essential Development Tools

- **Repository Validation**: `python tools/repo_health_check.py --validate-for-agent`
- **BDD Test Execution**: `python tools/run_bdd_tests.py --tags=REQ-1.1`
- **Coverage Analysis**: `python tools/bdd_coverage_report.py`
- **Style Checking**: `python tools/fix_style_issues.py --check`

## AI Agent Workflow

When working with this codebase as an AI agent:

1. **Start Every Session** with repository validation:
   ```bash
   python tools/repo_health_check.py --validate-for-agent
   ```

2. **Check Project Status** before proposing solutions:
   - Review [PROJECT_STATUS.md](docs/project/PROJECT_STATUS.md)
   - Understand current priorities and in-progress work

3. **Follow Documentation-First Navigation**:
   - Begin with project documentation in `docs/project/`
   - Examine tests to understand expected behavior
   - Use targeted searches for specific code exploration

4. **Document Session Results**:
   - Update relevant status documents
   - Create/update continuation context in `docs/project/continuation_prompt.md`

## Key Resources for Developers

- [Project System Documentation](docs/project/README.md) - Comprehensive guide to the project system
- [Project Status](docs/project/PROJECT_STATUS.md) - Current status and upcoming priorities
- [BDD Conventions](docs/project/bdd_conventions.md) - Standards for BDD features
- [Maintenance Guidelines](docs/project/MAINTENANCE_GUIDELINES.md) - Repository maintenance
- [Definition of Done](docs/project/DEFINITION_OF_DONE.md) - Criteria for completed work

## Common Issues

See the [detailed project system documentation](docs/project/README.md#common-issues-and-solutions) for solutions to common issues that new developers might encounter.

## Repository Structure

```
portal-explorer/
├── src/                   # Source code
├── tests/                 # Test suite (unit, integration, bdd)
├── docs/                  # Documentation
│   └── project/           # Project documentation (including detailed README)
├── tools/                 # Utility scripts and tools
├── examples/              # Example code and usage
└── data/                  # Data files and analysis results
```

For more detailed information about the project system, development process, and current initiatives, please refer to the [detailed project system documentation](docs/project/README.md). 