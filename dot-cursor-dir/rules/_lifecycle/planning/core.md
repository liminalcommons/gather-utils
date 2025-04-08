---
description: 
globs: **/planning/*.md,**/planning/*.mdx,**/releases/*/plan.md,**/releases/*/plan.mdx
alwaysApply: false
---
---
description: "Core guidance for the planning phase of the release lifecycle"
globs: "**/planning/*.md,**/planning/*.mdx,**/releases/*/plan.md,**/releases/*/plan.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Planning Phase Guidance

<critical>
The planning phase translates release objectives into actionable implementation plans. During this phase, define detailed tasks, allocate resources, map dependencies, and establish validation criteria to guide subsequent phases.
</critical>

## Core Planning Activities

The planning phase consists of these essential activities:

1. **Task Decomposition**: Break down release objectives into implementable tasks
2. **Dependency Mapping**: Identify and document relationships between tasks
3. **Resource Allocation**: Assign responsibility and estimate effort for each task
4. **Risk Assessment**: Identify potential issues and develop mitigation strategies
5. **Timeline Development**: Establish a realistic schedule with key milestones
6. **Validation Planning**: Define validation criteria and testing approach

## Required Metadata

Every release plan document must include:

```yaml
---
title: "[Release Name] Plan"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date]"
last_updated: "[Last Update Date]"
system_context: "[Code|Release|Agent]"
owner: "[Planning Owner]"
status: "[Draft|Approved|In Progress|Completed]"
related_definition: "[Link to Release Definition Document]"
---
```

## Release Plan Structure

Structure your release plan document as follows:

### 1. Executive Summary
Brief overview of the planning approach, key milestones, and critical path.

### 2. Objectives and Scope Reference
Concise reference to the objectives and scope established in the release definition:

```markdown
## Objectives and Scope Reference

This plan implements the objectives and scope defined in the [Release 2.3.0 Definition](mdc:../definition/release-2.3.0-definition.md).

### Key Objectives
1. **[Objective 1]**: [Brief description]
2. **[Objective 2]**: [Brief description]

### Scope Summary
- **In Scope**: [Brief summary of in-scope items]
- **Out of Scope**: [Brief summary of out-of-scope items]
```

### 3. Task Breakdown
Hierarchical breakdown of the work to be completed:

```markdown
## Task Breakdown

### 1. [Major Component/Feature 1]

#### 1.1 [Subcomponent/Task 1.1]
- **Description**: [Detailed description of the task]
- **Acceptance Criteria**: 
  - [Criterion 1]
  - [Criterion 2]
- **Dependencies**: [Dependencies on other tasks]
- **Assignee**: [Person/Role responsible]
- **Effort Estimate**: [Estimate in appropriate units]
- **Technical Approach**: [Brief description of implementation approach]

#### 1.2 [Subcomponent/Task 1.2]
...

### 2. [Major Component/Feature 2]
...
```

### 4. Dependency Graph
Visual or structured representation of task dependencies:

```markdown
## Dependency Graph

### Critical Path
The following tasks form the critical path for this release:
1. Task 1.1 → Task 2.3 → Task 3.2 → Task 4.1

### Dependency Matrix
| Task | Depends On | Required For |
|------|------------|--------------|
| 1.1  | None       | 1.2, 2.3     |
| 1.2  | 1.1        | 3.1          |
| 2.1  | None       | 2.2          |

### Visualization
See the [dependency graph visualization](mdc:../diagrams/release-2.3.0-dependencies.png) for a complete view of all task relationships.
```

### 5. Resource Allocation
Allocation of resources to tasks:

```markdown
## Resource Allocation

### Team Assignments
| Team/Person | Primary Responsibilities | Secondary Responsibilities |
|-------------|--------------------------|----------------------------|
| [Team/Person 1] | Tasks 1.1, 1.2, 1.3 | Support for Task 2.1 |
| [Team/Person 2] | Tasks 2.1, 2.2 | Support for Tasks 3.1, 3.2 |

### Specialized Resource Requirements
- **Testing Environment**: Required from [date] to [date]
- **Security Review**: Required during week of [date]
- **Performance Testing Infrastructure**: Required during [date range]
```

### 6. Timeline and Milestones
Detailed schedule with key milestones:

```markdown
## Timeline and Milestones

### Key Milestones
- **Planning Complete**: [Date]
- **Development Start**: [Date]
- **Feature Freeze**: [Date]
- **Testing Complete**: [Date]
- **Release Candidate**: [Date]
- **Deployment**: [Date]

### Detailed Schedule
| Week | Focus | Key Deliverables |
|------|-------|------------------|
| Week 1 (Mar 28-Apr 3) | Initial Development | Tasks 1.1, 2.1 completed |
| Week 2 (Apr 4-10) | Core Features | Tasks 1.2, 2.2, 3.1 completed |
| Week 3 (Apr 11-17) | Feature Completion | Tasks 3.2, 4.1 completed |
| Week 4 (Apr 18-24) | Testing & Refinement | All validation completed |
```

### 7. Risk Assessment and Mitigation
Identification of risks with mitigation strategies:

```markdown
## Risk Assessment and Mitigation

| Risk | Impact | Likelihood | Mitigation Strategy | Owner |
|------|--------|------------|---------------------|-------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [Strategy description] | [Owner] |
| [Risk 2] | High/Medium/Low | High/Medium/Low | [Strategy description] | [Owner] |

### Contingency Planning
- **Schedule Buffer**: 2 days added to each major milestone
- **Scope Contingency**: Features prioritized with minimum viable scope identified
- **Resource Contingency**: [Team/Person] available for additional support if needed
```

### 8. Validation Planning
Strategy for validating the release:

```markdown
## Validation Planning

### Validation Approach
[Overview of the validation approach for this release]

### Test Strategy
- **Unit Testing**: [Approach and coverage goals]
- **Integration Testing**: [Approach and key integration points]
- **System Testing**: [Approach and environment]
- **Performance Testing**: [Approach and criteria]
- **Security Testing**: [Approach and standards]

### Validation Criteria
| Feature/Component | Validation Method | Success Criteria |
|-------------------|-------------------|------------------|
| [Feature 1] | [Method] | [Criteria] |
| [Feature 2] | [Method] | [Criteria] |

### Meta-Systemic Validation
[Approach for validating adherence to meta-systemic principles]
```

### 9. Communication Plan
Communication approach during development:

```markdown
## Communication Plan

### Regular Updates
- **Daily Standups**: [Time, participants, format]
- **Weekly Status Reports**: [Day, distribution, template]
- **Milestone Reviews**: [Schedule, participants, format]

### Status Tracking
- **Issue Tracking**: [Tool, approach]
- **Status Dashboard**: [Location, update frequency]
- **Risk Register**: [Location, update frequency]

### Escalation Path
- **Technical Issues**: [Primary contact] → [Secondary contact] → [Final authority]
- **Resource Issues**: [Primary contact] → [Secondary contact] → [Final authority]
- **Timeline Issues**: [Primary contact] → [Secondary contact] → [Final authority]
```

## Meta-Systemic Principle Application

### Parsimony
- Reference existing requirements rather than duplicating
- Reuse established task templates and structures
- Maintain a single source of truth for each aspect of the plan
- Reference canonical documentation for technical approaches

### Tensegrity
- Balance responsibilities across team members
- Ensure tasks have clear owners but shared understanding
- Document bidirectional dependencies between tasks
- Design schedule with appropriate load balancing

### Modularity
- Define clear interfaces between components
- Establish distinct phases of work with defined boundaries
- Create independent work streams where possible
- Document integration points explicitly

### Coherence
- Follow consistent planning patterns
- Maintain terminology alignment with requirements
- Ensure planning approach matches release type
- Apply consistent estimation approaches

### Clarity
- Define unambiguous task descriptions
- Provide concrete examples for complex work
- Establish clear acceptance criteria
- Document technical approaches explicitly

### Adaptivity
- Scale planning detail to release complexity
- Adapt validation intensity to release risk
- Tailor communication approach to team distribution
- Adjust timeline precision to uncertainty level

## Context-Specific Planning Approaches

### For Code System Planning
- Focus on technical task breakdown
- Include architecture and design considerations
- Address code dependencies and integration points
- Plan for technical validation and testing
- Include development environment requirements

### For Release System Planning
- Focus on process task breakdown
- Include template and documentation updates
- Address process integration and transition
- Plan for meta-process validation
- Include training and communication requirements

### For Agent System Planning
- Focus on capability enhancement planning
- Include knowledge domain updates
- Address interaction pattern development
- Plan for capability validation
- Include human-AI collaboration considerations

## Release Scope-Specific Considerations

### Major Release Planning
- Comprehensive dependency mapping
- Detailed risk assessment
- Phased implementation approach
- Multiple validation checkpoints
- Extensive stakeholder communication

### Minor Release Planning
- Focused dependency mapping
- Targeted risk assessment
- Streamlined implementation approach
- Key validation checkpoints
- Regular stakeholder updates

### Patch Release Planning
- Essential dependency identification
- Critical risk assessment
- Efficient implementation approach
- Focused validation on affected areas
- Notification-based communication

### Emergency Release Planning
- Minimal dependency analysis
- Expedited implementation approach
- Critical-path validation only
- Just-in-time communication
- Explicit post-deployment verification

## Planning Phase Validation Checklist

Before concluding the planning phase, verify that:

- [ ] All requirements have been decomposed into implementable tasks
- [ ] Each task has clear ownership and acceptance criteria
- [ ] Dependencies are fully mapped and documented
- [ ] The timeline is realistic and accounts for dependencies
- [ ] Risks have been identified with mitigation strategies
- [ ] Resource allocation is balanced and sufficient
- [ ] Validation approach is comprehensive and appropriate
- [ ] Communication plan is established and agreed upon
- [ ] Planning approach is adapted to the specific context
- [ ] Meta-systemic principles have been appropriately applied

## Human-AI Collaboration in Planning

In our two-person team:

### Human Team Member Focus
- Establishing priorities and critical path
- Evaluating technical feasibility of approaches
- Making resource allocation decisions
- Assessing risk likelihood and impact
- Setting realistic timeline expectations

### AI Agent Focus
- Generating comprehensive task breakdowns
- Documenting dependencies systematically
- Ensuring consistent planning structure
- Tracking principle application
- Maintaining planning document integrity

<important>
The planning phase establishes the roadmap for implementation. Invest appropriate time in comprehensive planning to reduce execution risk and ensure the release objectives are achieved efficiently and effectively.
</important>