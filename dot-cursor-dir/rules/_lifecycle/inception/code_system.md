---
description: 
globs: **/code/inception/*.md,**/code/inception/*.mdx,**/releases/*/code_definition.md,**/releases/*/code_definition.mdx
alwaysApply: false
---
---
description: "Code-specific guidance for the inception phase of the release lifecycle"
globs: "**/code/inception/*.md,**/code/inception/*.mdx,**/releases/*/code_definition.md,**/releases/*/code_definition.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code System Inception Guidance

<critical>
This rule provides specialized guidance for the inception phase when the primary system context is code-based system development. Apply these guidelines in conjunction with the core inception phase rules.
</critical>

## Code System Release Definition

When defining releases for code-based systems, emphasize these additional aspects:

### 1. Technical Scope Definition

Define technical boundaries with precision:

```markdown
## Technical Scope

### Component Boundaries
- **Affected Components**: [List of specific components affected]
- **Unchanged Components**: [List of related components explicitly not changing]
- **New Components**: [List of new components being introduced]

### Interface Changes
- **Public API Modifications**: [List API changes with backward compatibility notes]
- **Internal Interface Changes**: [List internal interface changes]
- **Data Model Changes**: [List schema or model changes]

### Compatibility Requirements
- **Required Backward Compatibility**: [Specific compatibility requirements]
- **Breaking Changes**: [List of acceptable breaking changes, if any]
- **Migration Paths**: [Required migration support for breaking changes]
```

### 2. Technical Debt Assessment

Evaluate technical debt impact:

```markdown
## Technical Debt Assessment

### Existing Technical Debt
- **Affected Areas**: [Areas of technical debt affected by this release]
- **Impact on Implementation**: [How existing debt will impact the release]

### Technical Debt Strategy
- **Debt Reduction**: [Technical debt being addressed in this release]
- **New Technical Debt**: [Acceptable technical debt being introduced]
- **Mitigation Strategy**: [How we'll manage technical debt impact]
```

### 3. Architecture Impact Analysis

Analyze architectural implications:

```markdown
## Architecture Impact Analysis

### Architectural Changes
- **Pattern Changes**: [Architectural patterns being modified]
- **Component Architecture**: [Component-level architectural changes]
- **Infrastructure Changes**: [Required infrastructure modifications]

### System Quality Attributes
- **Performance Impact**: [Expected performance impacts]
- **Security Implications**: [Security considerations and changes]
- **Scalability Changes**: [How changes affect system scaling]
- **Maintainability Impact**: [Effects on system maintainability]
```

### 4. Development Considerations

Address development-specific factors:

```markdown
## Development Considerations

### Technical Feasibility
- **Technical Risks**: [Key technical risks and unknowns]
- **Proof of Concept Needs**: [Required prototyping or exploration]
- **Technical Constraints**: [Constraints affecting implementation]

### Implementation Approach
- **Development Strategy**: [Overall implementation approach]
- **Test Strategy**: [Testing approach for the changes]
- **Refactoring Requirements**: [Necessary refactoring work]

### Development Dependencies
- **Tooling Requirements**: [New or updated tools needed]
- **Library Dependencies**: [External dependencies and versions]
- **Environmental Requirements**: [Environment changes needed]
```

## Meta-Systemic Principle Application

### Parsimony in Code System Inception

1. **Reference existing specifications**:
   - Link to canonical requirements rather than duplicating
   - Reference existing architectural documentation
   - Reuse standard component templates

2. **Consolidate similar requirements**:
   - Group related features to minimize duplication
   - Identify common patterns across features
   - Create shared implementation approaches

### Tensegrity in Code System Inception

1. **Map bidirectional dependencies**:
   - Identify both incoming and outgoing dependencies
   - Document how components support each other
   - Ensure balanced responsibility distribution

2. **Strengthen integration points**:
   - Define clear contracts for component interactions
   - Specify error handling across boundaries
   - Document retry and resilience strategies

### Modularity in Code System Inception

1. **Define clear component boundaries**:
   - Specify public APIs for each component
   - Document internal vs. external interfaces
   - Define data ownership boundaries

2. **Plan for independent evolution**:
   - Design for component-level deployability
   - Specify versioning strategy for interfaces
   - Define compatibility requirements

### Coherence in Code System Inception

1. **Align with existing patterns**:
   - Reference established architectural patterns
   - Use consistent naming conventions
   - Follow existing component structures

2. **Maintain consistent approaches**:
   - Use standard error handling approaches
   - Apply consistent security patterns
   - Follow established state management patterns

### Clarity in Code System Inception

1. **Document with concrete examples**:
   - Include example API usages
   - Provide sample data structures
   - Illustrate workflows with sequence diagrams

2. **Explain key technical decisions**:
   - Document architecture decisions with rationale
   - Explain tradeoffs in approach selection
   - Address alternatives considered

### Adaptivity in Code System Inception

1. **Accommodate different deployment contexts**:
   - Plan for different environments
   - Consider configuration variations
   - Address scale differences

2. **Allow for implementation flexibility**:
   - Define outcomes rather than strict implementations
   - Allow for technology-specific adaptations
   - Consider extensibility points

## Code-Specific Artifact Requirements

### System Context Diagram

Include a system context diagram showing:

```markdown
## System Context Diagram

![System Context](mdc:../diagrams/system-context.png)

This diagram shows:
- The components being modified (highlighted in blue)
- External system dependencies
- Key data flows
- User interaction points

The highlighted areas represent the scope of this release.
```

### Technical Requirements Mapping

Map business requirements to technical requirements:

```markdown
## Technical Requirements Mapping

| Business Requirement | Technical Requirements | Components Affected |
|----------------------|------------------------|---------------------|
| REQ-001: Users can reset passwords | TECH-001: Implement password reset API<br>TECH-002: Create email notification<br>TECH-003: Add password reset UI | Authentication Service<br>Notification Service<br>User Interface |
```

### API Specification

Include preliminary API specifications:

```markdown
## API Specification

### User Authentication API

#### POST /api/auth/login

Request:
```json
{
  "username": "string",
  "password": "string",
  "mfaToken": "string (optional)"
}
```

Response (200 OK):
```json
{
  "token": "string",
  "expiresAt": "ISO8601 timestamp",
  "user": {
    "id": "string",
    "name": "string",
    "email": "string"
  }
}
```

Errors:
- 401 Unauthorized: Invalid credentials
- 403 Forbidden: Account locked
- 400 Bad Request: Invalid input format
```

### Data Model Changes

Document data model modifications:

```markdown
## Data Model Changes

### User Entity Updates

```diff
type User {
  id: ID!
  username: String!
  email: String!
+ phoneNumber: String
+ phoneVerified: Boolean
  password: String!
  createdAt: DateTime!
  updatedAt: DateTime!
}
```

### New Entity: VerificationToken

```typescript
type VerificationToken {
  id: ID!
  token: String!
  userId: ID!
  type: VerificationType!
  expiresAt: DateTime!
  createdAt: DateTime!
}

enum VerificationType {
  EMAIL
  PHONE
  PASSWORD_RESET
}
```
```

## Release Scope Classification Guidelines

Apply these guidelines to classify code system releases:

### Major Release Indicators
- Introduction of new significant features
- Breaking API changes
- Database schema changes requiring migrations
- Architectural pattern changes
- UI redesigns
- Major dependency version upgrades

### Minor Release Indicators
- New non-breaking features
- Enhanced existing functionality
- Non-breaking API additions
- Performance improvements
- Minor UI improvements
- Dependency updates without breaking changes

### Patch Release Indicators
- Bug fixes
- Security patches
- Performance optimizations
- Documentation improvements
- Minor UI adjustments
- No functional additions

### Emergency Release Indicators
- Critical security vulnerabilities
- Production-blocking bugs
- Data integrity issues
- Compliance violations

## Code-Specific Validation Checklist

Before completing the inception phase, validate:

- [ ] All affected components are identified
- [ ] API changes are explicitly documented
- [ ] Technical risks are identified and assessed
- [ ] Architecture impact is fully analyzed
- [ ] Development approach is defined
- [ ] Testing strategy is outlined
- [ ] Technical debt strategy is documented
- [ ] Required resources and skills are identified
- [ ] Interface contracts are defined
- [ ] Security and performance implications are assessed

## Context Transition Guidance

As you complete the code system inception phase and prepare for planning:

1. **Validate Completeness**:
   - Ensure all technical aspects are addressed
   - Verify alignment with business requirements
   - Confirm technical feasibility

2. **Prepare for Planning**:
   - Gather necessary technical specifications
   - Identify areas needing further investigation
   - Prepare for task breakdown

3. **Stakeholder Alignment**:
   - Ensure technical direction is understood
   - Address technical concerns and questions
   - Validate approach with technical stakeholders

<important>
The code system inception phase establishes the technical foundation for the release. Be thorough in defining technical boundaries and interfaces to ensure clear communication and prevent scope creep during implementation.
</important>