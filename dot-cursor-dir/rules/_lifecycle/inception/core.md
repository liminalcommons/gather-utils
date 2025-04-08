---
description: 
globs: **/inception/*.md,**/inception/*.mdx,**/releases/*/definition.md,**/releases/*/definition.mdx
alwaysApply: false
---
---
description: "Core guidance for the inception phase of the release lifecycle"
globs: "**/inception/*.md,**/inception/*.mdx,**/releases/*/definition.md,**/releases/*/definition.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Inception Phase Guidance

<critical>
The inception phase establishes the foundation for the entire release lifecycle. During this phase, clearly define the release scope, objectives, and context to ensure proper application of meta-systemic principles throughout subsequent phases.
</critical>

## Core Inception Activities

The inception phase consists of these essential activities:

1. **Scope Definition**: Establish clear boundaries for what is included in the release
2. **Classification**: Determine the release type (major, minor, patch, emergency)
3. **Context Assessment**: Identify relevant system factors for appropriate principle application
4. **Objective Formulation**: Define clear, measurable objectives for the release
5. **Stakeholder Alignment**: Ensure stakeholders understand and agree to the release scope

## Required Metadata

Every release definition document must include:

```yaml
---
title: "[Release Name] Definition"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date]"
last_updated: "[Last Update Date]"
system_context: "[Code|Release|Agent]"
owner: "[Release Owner]"
status: "[Draft|Approved|In Progress|Completed]"
---
```

## Release Definition Structure

Structure your release definition document as follows:

### 1. Executive Summary
Brief overview of the release, its primary purpose, and key deliverables.

### 2. Objectives
Clear, measurable objectives for the release, following the SMART criteria:
- Specific
- Measurable
- Achievable
- Relevant
- Time-bound

### 3. Scope Definition
Detailed description of what is included in the release, with explicit boundaries.

#### 3.1 In Scope
Specific features, changes, or components included in the release.

#### 3.2 Out of Scope
Explicit statement of what is not included to prevent scope creep.

### 4. Context Assessment
Analysis of the system context to guide principle application:

```markdown
## Context Assessment

### System Type
[Code|Release|Agent] System

### Release Classification
[Major|Minor|Patch|Emergency] Release

### System Factors
- **Maturity**: [Early Exploration|Active Development|Maintenance|Legacy]
- **Architecture**: [Monolithic|Modular|Microservices|Hybrid]
- **Team Structure**: [Solo|Small Team|Multiple Teams|Distributed]

### Activity Factors
- **Complexity**: [Low|Medium|High|Very High]
- **Criticality**: [Low|Medium|High|Very High]
- **Time Sensitivity**: [Low|Medium|High|Very High]
```

### 5. Principle Application Strategy
Description of how meta-systemic principles will be applied in this release:

```markdown
## Principle Application Strategy

Based on our [context assessment](mdc:#context-assessment), we will emphasize the following principles:

- **Primary Focus**: [Principle 1], [Principle 2]
- **Secondary Focus**: [Principle 3], [Principle 4]
- **Monitored**: [Principle 5], [Principle 6]

### Key Principle Applications
1. [Principle 1] will be applied through [specific approach]
2. [Principle 2] will be applied through [specific approach]
```

### 6. Dependencies
Identification of external and internal dependencies:

```markdown
## Dependencies

### External Dependencies
- [Dependency 1]: [Description and impact]
- [Dependency 2]: [Description and impact]

### Internal Dependencies
- [Component/Team 1]: [Description and impact]
- [Component/Team 2]: [Description and impact]
```

### 7. Timeline
High-level timeline for the release:

```markdown
## Timeline

- **Planning Phase**: [Start Date] - [End Date]
- **Development Phase**: [Start Date] - [End Date]
- **Validation Phase**: [Start Date] - [End Date]
- **Pre-Release Review**: [Review Date]
- **Deployment**: [Target Date]
- **Post-Release Evaluation**: [Evaluation Date]
```

### 8. Stakeholders
List of stakeholders and their roles:

```markdown
## Stakeholders

| Name/Role | Responsibility | Involvement |
|-----------|----------------|-------------|
| [Name/Role] | [Responsibility] | [Approval/Consulted/Informed] |
```

### 9. Risks and Mitigations
Key risks and mitigation strategies:

```markdown
## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation Strategy |
|------|--------|------------|---------------------|
| [Risk 1] | [High/Medium/Low] | [High/Medium/Low] | [Strategy] |
```

## Meta-Systemic Principle Application

### Parsimony
- Reference existing requirements from canonical sources
- Maintain clear links to source requirements
- Define concepts once and reference consistently throughout

### Tensegrity
- Identify bidirectional dependencies between components
- Ensure balanced responsibilities across teams
- Document how components support each other

### Modularity
- Define clear boundaries for the release scope
- Specify interfaces with existing components
- Identify integration points and contracts

### Coherence
- Ensure release aligns with existing patterns
- Maintain consistent terminology throughout
- Follow established classification criteria

### Clarity
- Include concrete examples for complex concepts
- Define terminology explicitly
- Explain rationale for key decisions

### Adaptivity
- Tailor the inception process to the release context
- Adapt level of detail based on release complexity
- Preserve core elements while allowing contextual variation

## Context-Specific Guidance

### For Code System Releases
- Focus on technical boundaries and interfaces
- Define API changes and compatibility considerations
- Map features to specific components and repositories
- Include performance and security considerations

### For Release Process Releases
- Emphasize process improvement objectives
- Define transition plans from existing processes
- Include meta-process metrics for evaluation
- Map changes to specific workflow phases

### For Agent System Releases
- Focus on agent capability enhancements
- Define interaction pattern changes
- Include knowledge domain impacts
- Specify human-AI collaboration changes

## Inception Phase Validation Checklist

Before proceeding to the planning phase, verify that:

- [ ] Release objectives are clear and measurable
- [ ] Scope boundaries are explicitly defined
- [ ] Context assessment is comprehensive and accurate
- [ ] Principle application strategy is appropriate for the context
- [ ] Dependencies are identified with mitigation plans
- [ ] Timeline is realistic and accounts for dependencies
- [ ] Stakeholders have been consulted and are aligned
- [ ] Risks have been identified with mitigation strategies
- [ ] Release definition adheres to meta-systemic principles

<important>
The quality of the inception phase significantly impacts all subsequent phases. Invest appropriate time to create a robust release definition that provides clear direction while allowing for appropriate adaptivity as the release progresses.
</important>