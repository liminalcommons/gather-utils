# Agent Guidelines for BDD Refactoring Initiative

## Overview

This document provides guidelines for AI assistants working on the BDD Refactoring Initiative. Following these guidelines ensures consistency across sessions, maintains project momentum, and enables seamless transitions between work sessions.

## Core Responsibilities

1. **Project Understanding**: Maintain comprehensive understanding of the BDD Refactoring Initiative, including all releases, current status, and objectives.

2. **Documentation Management**: Keep all documentation updated, organized, and consistent with the overall project structure.

3. **Code Development**: Write clean, well-documented code that follows established conventions for the project.

4. **Status Tracking**: Regularly update status documents to reflect current progress, challenges, and accomplishments.

5. **Continuity Management**: Ensure smooth transitions between work sessions by providing appropriate context and continuation information.

## Documentation Standards

### General Guidelines

- Use consistent formatting across all project documents
- Include clear headings and subheadings for easy navigation
- Update "Last updated" timestamps when modifying documents
- Use status indicators (✅, ⏳, ❌) consistently
- Include concrete metrics wherever possible
- Reference related documents where appropriate

### Status Documents

Status documents should include:

- Current phase and overall progress percentage
- Recently completed tasks with dates
- In-progress and pending tasks
- Technical progress details
- Key metrics table showing targets vs. current status
- Next steps with owners and deadlines
- Risks and issues with mitigation strategies
- Dependencies and blockers
- Resources and support information

### Project Plans

Project plans should include:

- Clear overview of the release/phase objectives
- Detailed goals and success criteria
- Implementation plan broken down by phases
- Timeline with specific milestones
- Resource requirements
- Risk assessment and mitigation strategies
- Integration points with other systems or releases

## Code Development Guidelines

- Follow Python best practices (PEP 8)
- Include docstrings for all classes and methods
- Add appropriate error handling
- Write unit tests for new functionality
- Comment complex logic
- Use meaningful variable and function names
- Structure code to be modular and maintainable

## Session Management

### Beginning a Session

1. Review the latest project status documents
2. Check the continuation prompt from the previous session
3. Understand the current priorities and context
4. Acknowledge the current state and confirm the plan forward

### During a Session

1. Focus on specified tasks or requirements
2. Regularly communicate progress and challenges
3. Update documentation as work progresses
4. Ask clarifying questions when requirements are ambiguous

### Concluding a Session

1. **Update Project Status**: Always update the relevant status document(s) to reflect the latest progress, including:
   - Tasks completed during the session
   - Current status of in-progress tasks
   - Updated metrics and progress indicators
   - Revised timelines if applicable
   - New risks or issues identified

2. **Create/Update Continuation Prompt**: Create or update the continuation prompt document in `docs/project/continuation_prompt.md` with:
   - Summary of work completed in the current session
   - Current context and state of the project
   - Immediate next steps and priorities
   - Outstanding questions or decisions
   - References to relevant files or documents
   - Sufficient detail to allow the next session to continue seamlessly

3. **Provide Session Summary**: Conclude with a concise summary of:
   - What was accomplished in the session
   - Updated project status
   - Next steps
   - Location of the continuation prompt

## Continuation Prompt Format

The continuation prompt should follow this general structure:

```markdown
# BDD Refactoring Initiative - Continuation Context

## Current Status
[Brief description of the overall project status]

## Recent Accomplishments
[Bullet points of recently completed work]

## Current Context
[Detailed description of the current state of work, including any in-progress tasks]

## Next Steps
[Prioritized list of next actions to take]

## Reference Files
[List of key files relevant to continuing the work]

## Open Questions
[Any unresolved questions or decisions that need to be addressed]
```

## Example Conclusion

"To conclude today's session, I've updated the status document for Release 3 to reflect our progress on the traceability framework design. I've also created feature templates for the requirements connectors. The project is currently 15% complete with Release 3, focused on the traceability framework enhancement phase.

I've updated the continuation prompt in `docs/project/continuation_prompt.md` with the context needed to resume work on implementing the core traceability database in the next session.

The next steps will be to finalize the database schema and begin implementing the API services for traceability. All documentation has been updated to reflect the current status."

## Final Notes

Following these guidelines ensures that the BDD Refactoring Initiative maintains momentum across multiple work sessions and different collaborators. Consistent documentation and clear continuation contexts are essential for the project's success. 