# Repository Maintenance Guidelines

This document outlines guidelines for maintaining the repository in a clean and organized state.

## Documentation Guidelines

1. **Living Documentation**
   - README.md - Project overview, getting started, and current status
   - docs/project/PROJECT_STATUS.md - Detailed project status
   - docs/project/DEFINITION_OF_DONE.md - Definition of Done criteria
   - .cursor/rules/agent_guidelines.mdc - Guidelines for AI agents
   - .cursor/rules/bdd_agent_guidelines.mdc - BDD-specific guidelines for AI agents

2. **Archived Documentation**
   - docs/archive/ - Completed project documents
   - Each archived document should have a header indicating when it was archived

3. **Documentation Review Schedule**
   - Review README.md monthly
   - Review PROJECT_STATUS.md bi-weekly
   - Review other documentation quarterly

## Code Guidelines

1. **Code Organization**
   - src/ - Source code
   - tests/ - All tests (unit, integration, BDD)
   - tools/ - Utility scripts and tools
   - examples/ - Example code and usage

2. **Code Quality**
   - All code must pass linters
   - All code must have tests
   - Test coverage must meet thresholds (80% minimum)

3. **Code Review**
   - All changes must be reviewed
   - Automated checks must pass before merge

4. **Tool Management**
   - One-off tools should be documented with a clear purpose and expected lifecycle
   - After successful use, one-off tools should be:
     a. Archived if they might be needed for reference
     b. Deleted if they serve no future purpose
   - Document the decision to keep or remove tools in the commit message
   - Update relevant documentation to reflect tool removal
   - Consider generalizing useful one-off tools for broader use cases

## Testing Guidelines

1. **Test Organization**
   - tests/unit/ - Unit tests (TDD)
   - tests/integration/ - Integration tests
   - tests/bdd/ - BDD tests

2. **Test Quality**
   - Tests must be independent
   - Tests must be deterministic
   - Tests must be fast

3. **Test Coverage**
   - Unit test coverage: 80% minimum
   - Feature coverage: 100% of user stories

## Maintenance Schedule

1. **Weekly**
   - Run repo_health_check.py
   - Address any issues found

2. **Monthly**
   - Review and update README.md
   - Archive completed documentation
   - Clean up temporary files

3. **Quarterly**
   - Comprehensive repository review
   - Update maintenance guidelines as needed

## Agent Navigation Guidelines

1. **Repository Structure**
   - Maintain consistent directory structure
   - Use the repository health check tool to validate structure
   - Run `python tools/repo_health_check.py --validate-for-agent` to verify

2. **File Naming Conventions**
   - Python modules: `snake_case.py`
   - Test files: `test_*.py`
   - BDD feature files: `*.feature`
   - Documentation: `UPPERCASE_WITH_UNDERSCORES.md`

3. **Documentation for Agents**
   - Keep agent guidelines in `.cursor/rules/` up-to-date
   - Document navigation patterns
   - Include examples of common tasks

4. **Code Organization for Agent Navigation**
   - Group related functionality in modules
   - Use consistent import patterns
   - Maintain clear separation of concerns
   - Add descriptive docstrings to all modules and functions

5. **Agent-Friendly Practices**
   - Use descriptive variable and function names
   - Add comments for complex logic
   - Maintain consistent code style
   - Document design decisions and rationale
