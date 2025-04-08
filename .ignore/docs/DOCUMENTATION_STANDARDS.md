# Documentation Standards

This document outlines the standards for creating, maintaining, and archiving documentation within the Portal Explorer project.

Last Updated: 2024-03-21

## Documentation Lifecycle Management

### 1. Documentation Categories

Documentation in our codebase falls into the following categories:

- **Core Documentation**: Essential project structure and processes (e.g., README.md, DEVELOPER_README.md)
- **Technical Documentation**: Implementation details and architecture
- **Process Documentation**: Development workflows and standards
- **User Documentation**: End-user guides and tutorials
- **API Documentation**: API references and usage guides
- **Temporary Documentation**: For interim solutions or time-limited features

### 2. Required Metadata

All documentation files should include a metadata header:

```markdown
---
Title: Documentation Title
Created: YYYY-MM-DD
Last Updated: YYYY-MM-DD
Status: Active|Deprecated|Archived
Owner: Team/Individual
Purpose: Clear description of document's purpose
Audience: Developers/Users/Admins/etc.
Lifecycle:
  - Created: Why the document was created
  - Active: Current usage status
  - Obsolescence Conditions:
    1. Condition under which document becomes obsolete
    2. Additional condition if applicable
Last Validated: YYYY-MM-DD
---
```

### 3. Documentation Statuses

- **Active**: Currently relevant and maintained
- **Deprecated**: Still available but being phased out (with replacement indicated)
- **Archived**: Preserved for historical reference but no longer actively maintained

### 4. Lifecycle Management Workflow

1. **Creation**:
   - Use the appropriate template from `docs/templates/`
   - Fill in all metadata fields
   - Establish clear purpose and audience

2. **Validation**:
   - Update "Last Validated" date when confirming a document is still relevant
   - Run quarterly validation on all active documentation
   - Review for technical accuracy and clarity

3. **Maintenance**:
   - Update "Last Updated" date whenever content changes
   - Periodically review for accuracy and completeness
   - Keep formatting and style consistent

4. **Archival/Removal**:
   - Archive documents with historical value in `docs/archive/`
   - Remove obsolete documentation that has no reference value
   - Document archival/removal decisions in commit messages

## Documentation Standards

### 1. Structure and Organization

- All documentation should be in Markdown format
- Use consistent heading hierarchy (# for title, ## for sections, etc.)
- Include a table of contents for documents longer than 200 lines
- Group related documentation in appropriate directories

### 2. Content Quality

- Use clear, concise language
- Include examples for complex concepts
- Define technical terms on first use
- Use diagrams when appropriate to illustrate concepts
- Break up large documents into logical sections

### 3. Formatting

- Use consistent formatting for code blocks, notes, and warnings
- Properly format code with syntax highlighting
- Use numbered lists for sequential steps
- Use bulleted lists for non-sequential items
- Use tables for structured data

### 4. Links and References

- Use relative links for internal documentation
- Ensure all links are valid and accessible
- Include version information for external references
- Provide context for why a link is relevant

## Documentation Types

### 1. README.md

Every significant directory should include a README.md that:
- Explains the purpose of the directory
- Lists important files and their purposes
- Provides instructions for common tasks
- Links to more detailed documentation

### 2. Technical Documentation

Technical documentation should:
- Describe the architecture and components
- Explain design decisions and tradeoffs
- Include diagrams (architecture, data flow, etc.)
- Document APIs and interfaces

### 3. Process Documentation

Process documentation should:
- Provide step-by-step instructions
- Explain the rationale for each step
- Include troubleshooting guidance
- Be updated whenever processes change

### 4. User Documentation

User documentation should:
- Be organized by user tasks
- Include screenshots or examples
- Use simple, non-technical language
- Provide troubleshooting guidance

## Templates

Use the following templates to create new documentation:

1. **General Documentation**: `docs/templates/general_template.md`
2. **Technical Design**: `docs/templates/technical_design_template.md`
3. **User Guide**: `docs/templates/user_guide_template.md`
4. **Process Documentation**: `docs/templates/process_template.md`

## Automation and Enforcement

1. **Repository Health Check**:
   - `repo_health_check.py` validates documentation metadata
   - Run before commits to ensure compliance

2. **CI/CD Integration**:
   - Automated link validation
   - Markdown linting
   - Metadata validation

3. **Quarterly Review**:
   - Review all documentation for relevance
   - Update "Last Validated" dates
   - Archive or delete obsolete documentation

## Best Practices

1. **Keep Documentation Focused**:
   - Each document should have a single responsibility
   - Consider breaking complex documents into smaller components

2. **Synchronize with Code**:
   - Update documentation when code changes
   - Consider documentation updates part of code changes

3. **Use Examples**:
   - Provide real-world examples
   - Include code snippets
   - Show expected outputs

4. **Consider Audience**:
   - Write for the intended audience's technical level
   - Define technical terms where necessary
   - Provide context for complex concepts

5. **Lifecycle Planning**:
   - Consider obsolescence conditions at creation time
   - Plan for eventual replacement or archival
   - Document dependencies that might affect lifecycle
