---
description: 
globs: **/process/inception/*.md,**/process/inception/*.mdx,**/releases/*/process_definition.md,**/releases/*/process_definition.mdx
alwaysApply: false
---
---
description: "Release process-specific guidance for the inception phase of the release lifecycle"
globs: "**/process/inception/*.md,**/process/inception/*.mdx,**/releases/*/process_definition.md,**/releases/*/process_definition.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Release System Inception Guidance

<critical>
This rule provides specialized guidance for the inception phase when the primary system context is release system evolution. Apply these guidelines in conjunction with the core inception phase rules.
</critical>

## Release System Definition

When defining releases for release process systems, emphasize these additional aspects:

### 1. Process Scope Definition

Define process boundaries with precision:

```markdown
## Process Scope

### Process Boundaries
- **Affected Process Phases**: [List of specific process phases affected]
- **Unchanged Process Phases**: [List of related phases explicitly not changing]
- **New Process Elements**: [List of new process elements being introduced]

### Interface Changes
- **Handoff Modifications**: [List changes to phase handoffs with backward compatibility notes]
- **Artifact Template Changes**: [List changes to artifact templates]
- **Tool Integration Changes**: [List changes to tool integrations]

### Compatibility Requirements
- **Required Backward Compatibility**: [Specific compatibility requirements]
- **Breaking Changes**: [List of acceptable breaking changes, if any]
- **Migration Paths**: [Required migration support for breaking changes]
```

### 2. Meta-Process Assessment

Evaluate process debt and improvement opportunities:

```markdown
## Meta-Process Assessment

### Current Process State
- **Process Strengths**: [Areas where the current process works well]
- **Process Pain Points**: [Areas where the current process needs improvement]
- **Process Metrics**: [Key metrics indicating current process performance]

### Process Improvement Strategy
- **Process Debt Reduction**: [Process inefficiencies being addressed]
- **New Process Capabilities**: [New capabilities being introduced]
- **Process Simplification**: [Areas being simplified or streamlined]
```

### 3. Governance and Standards Impact

Analyze implications for governance and standards:

```markdown
## Governance and Standards Impact

### Policy Changes
- **Affected Policies**: [Policies that will need updating]
- **New Policy Requirements**: [New policies that need to be created]
- **Policy Compliance Approach**: [How compliance will be maintained]

### Standard Modifications
- **Artifact Standards**: [Changes to artifact standards]
- **Process Standards**: [Changes to process standards]
- **Quality Standards**: [Changes to quality standards]

### Governance Implications
- **Approval Processes**: [Changes to approval workflows]
- **Oversight Mechanisms**: [Changes to oversight activities]
- **Metrics and Reporting**: [Changes to process metrics and reporting]
```

### 4. Rule and Template Considerations

Address changes to Cursor rules and templates:

```markdown
## Rule and Template Considerations

### Cursor Rule Changes
- **New Rules Required**: [New rules that need to be created]
- **Rules to Modify**: [Existing rules that need updating]
- **Rules to Deprecate**: [Rules that will be removed or replaced]
- **Rule Evolution Strategy**: [Approach to rule transition]

### Template Updates
- **New Templates**: [New templates to be created]
- **Template Modifications**: [Existing templates to be updated]
- **Template Migration**: [How existing artifacts will be migrated to new templates]
- **Template Compatibility**: [How template compatibility will be maintained]

### Documentation Changes
- **Process Documentation**: [Updates needed to process documentation]
- **Training Materials**: [Updates needed to training materials]
- **Reference Guides**: [Updates needed to reference materials]
```

## Meta-Systemic Principle Application

### Parsimony in Release System Inception

1. **Consolidate process documentation**:
   - Maintain a single source of truth for process definitions
   - Reference canonical process documentation rather than duplicating
   - Create standardized template libraries

2. **Optimize information flow**:
   - Identify and eliminate redundant information collection
   - Streamline artifact chains to reduce duplication
   - Create shared information repositories

3. **Simplify process elements**:
   - Remove unnecessary process steps and approvals
   - Consolidate similar activities and artifacts
   - Create clear knowledge references across process phases

Example:
```markdown
## Process Documentation Approach

Instead of having separate documentation for each tool and phase, we will:

1. Create a canonical process documentation in the central repository
2. Reference the canonical source from tool-specific guidance
3. Implement a standardized cross-reference system between artifacts
4. Maintain a centralized term glossary for consistency

This approach reduces documentation duplication by an estimated 40% while improving consistency.
```

### Tensegrity in Release System Inception

1. **Design balanced phase relationships**:
   - Ensure clear bidirectional handoffs between phases
   - Create mutual support mechanisms between process roles
   - Balance responsibilities across the process

2. **Establish feedback mechanisms**:
   - Create explicit feedback channels between phases
   - Design process loops that improve outcomes
   - Implement cross-phase metrics to assess balance

3. **Build resilient processes**:
   - Design processes that can handle exceptions
   - Create appropriate escalation paths
   - Implement flexible but robust approvals

Example:
```markdown
## Phase Relationship Design

The revised planning and development phases will have these bidirectional relationships:

- **Planning → Development**: Provides clear task breakdown, priorities, and dependencies
- **Development → Planning**: Provides implementation feedback, scope adjustment needs, and technical constraint discoveries

To support this relationship:
1. We'll create a formal "Implementation Feedback" artifact
2. Establish weekly synchronization points
3. Implement shared progress visualization
4. Create a balanced escalation process for blockers

This balances control and flexibility while ensuring mutual value exchange between phases.
```

### Modularity in Release System Inception

1. **Create clear phase boundaries**:
   - Define explicit entry and exit criteria for each phase
   - Establish clean interfaces between process phases
   - Design phase activities to be independent where possible

2. **Separate concerns across the process**:
   - Clearly separate planning, execution, and validation activities
   - Assign distinct responsibilities to different roles
   - Create independent but connected artifact chains

3. **Enable process customization**:
   - Design a modular process framework
   - Allow phase-specific customizations without disrupting the whole
   - Create pluggable process components

Example:
```markdown
## Modular Process Design

The new release process will follow a modular design with:

1. **Clear Phase Boundaries**:
   - Explicit entry/exit criteria for each phase
   - Standardized handoff artifacts
   - Independent phase execution capability

2. **Pluggable Components**:
   - Optional validation activities based on release risk
   - Customizable approval workflows by release type
   - Extensible artifact templates with required and optional sections

3. **Interface Contracts**:
   - Standardized information exchange formats
   - Consistent status reporting interfaces
   - Formal escalation protocols
```

### Coherence in Release System Inception

1. **Maintain consistent process patterns**:
   - Apply the same patterns across similar process phases
   - Use consistent terminology throughout the process
   - Create standardized artifacts and workflows

2. **Align with organizational patterns**:
   - Ensure the process aligns with broader organizational approaches
   - Maintain consistency with related processes
   - Use established organizational terminology

3. **Create process pattern libraries**:
   - Document standard process patterns
   - Create reusable workflow templates
   - Establish pattern governance

Example:
```markdown
## Process Pattern Standardization

To ensure coherence, we will:

1. **Standardize Phase Patterns**:
   - Apply the "Plan-Execute-Validate-Approve" pattern to all major phases
   - Use consistent milestone naming conventions
   - Implement standardized status reporting

2. **Standardize Artifact Patterns**:
   - Create consistent artifact templates with standard sections
   - Apply uniform metadata requirements
   - Implement consistent review processes

3. **Maintain Pattern Library**:
   - Document all standard process patterns
   - Provide examples of correct pattern application
   - Establish pattern governance process
```

### Clarity in Release System Inception

1. **Create explicit process documentation**:
   - Document the process clearly with examples
   - Create visual process flows and diagrams
   - Provide concrete examples of artifacts and deliverables

2. **Define terminology precisely**:
   - Create a glossary of process terms
   - Use consistent terminology across artifacts
   - Avoid ambiguous language in process definitions

3. **Explain process rationale**:
   - Document the reasons behind process requirements
   - Clarify how the process supports business objectives
   - Explain how different process elements work together

Example:
```markdown
## Process Clarity Approach

To ensure the process is clear to all participants:

1. **Visual Process Documentation**:
   - Create end-to-end process flow diagrams
   - Provide RACI matrices for all process activities
   - Develop interactive process guides

2. **Example-Based Documentation**:
   - Include concrete examples for all artifacts
   - Provide before/after examples for process changes
   - Create scenario-based guides for common situations

3. **Terminology Management**:
   - Develop a comprehensive process glossary
   - Highlight defined terms in documentation
   - Include term definitions in artifact templates
```

### Adaptivity in Release System Inception

1. **Design for different release contexts**:
   - Create appropriate process variations for different release types
   - Scale the process based on release size and risk
   - Allow context-appropriate customization

2. **Enable process evolution**:
   - Design for incremental process improvement
   - Create mechanisms to capture and implement process lessons
   - Allow for experimental process variations

3. **Support organizational changes**:
   - Make the process resilient to organizational changes
   - Design role-based rather than person-based processes
   - Create appropriate process abstraction levels

Example:
```markdown
## Adaptive Process Framework

The new process will adapt to different contexts:

1. **Release Type Adaptations**:
   - **Major Releases**: Comprehensive process with all phases and formal approvals
   - **Minor Releases**: Streamlined process with abbreviated planning and validation
   - **Patch Releases**: Lightweight process focusing on critical paths only
   - **Emergency Releases**: Expedited process with post-implementation governance

2. **Team Context Adaptations**:
   - Flexible role assignments based on team size
   - Scalable artifact detail based on team distribution
   - Customizable communication intensity based on team structure

3. **Evolution Mechanisms**:
   - Built-in retrospective process for continuous improvement
   - Formal process experimentation framework
   - Regular process effectiveness reviews
```

## Release System-Specific Artifact Requirements

### Process Definition Document

Include a comprehensive process definition:

```markdown
## Process Definition

This document defines the process changes being implemented in this release.

### Current Process
![Current Process Flow](mdc:../diagrams/current-process-flow.png)

This diagram shows the current process with pain points highlighted in red.

### Proposed Process Changes
![New Process Flow](mdc:../diagrams/new-process-flow.png)

The proposed changes address these pain points by:
1. Streamlining the approval workflow
2. Automating the validation reporting
3. Standardizing handoff artifacts

### Implementation Approach
The process changes will be implemented through:
- Revised Cursor rules for affected phases
- Updated artifact templates
- New automation for validation reporting
- Updated process documentation and training

### Backward Compatibility
The process changes maintain backward compatibility through:
- Support for both old and new artifact formats during transition
- Conversion utilities for existing artifacts
- Parallel process paths during the transition period
```

### Meta-Process Metrics Specification

Define metrics to assess process effectiveness:

```markdown
## Meta-Process Metrics

This section defines the metrics that will be used to evaluate the process changes.

### Efficiency Metrics
| Metric | Current Baseline | Target | Measurement Method |
|--------|------------------|--------|-------------------|
| Cycle Time | 15 days avg | 10 days avg | Time from inception to deployment |
| Handoff Efficiency | 2 days avg | 1 day avg | Time between phase completions |
| Artifact Creation Time | 3 hours avg | 1.5 hours avg | Time to create key artifacts |
| Approval Cycle Time | 3 days avg | 1 day avg | Time to obtain approvals |

### Quality Metrics
| Metric | Current Baseline | Target | Measurement Method |
|--------|------------------|--------|-------------------|
| Defect Escape Rate | 15% | < 5% | Defects found post-validation |
| Rework Rate | 25% | < 10% | Percentage of work requiring revision |
| Validation Effectiveness | 75% | > 90% | Issues found in validation vs. production |

### Adoption Metrics
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Process Compliance | > 95% | Percentage of releases following new process |
| Process Satisfaction | > 80% | Team survey results |
| Artifact Quality | > 90% | Quality assessment of produced artifacts |
```

### Process Transition Plan

Outline the approach to transitioning to the new process:

```markdown
## Process Transition Plan

This section outlines how we will transition from the current process to the new process.

### Transition Approach
We will use a phased approach to minimize disruption:

1. **Phase 1: Documentation and Training**
   - Update all process documentation
   - Create transition guides
   - Conduct training sessions

2. **Phase 2: Pilot Implementation**
   - Select 2-3 upcoming releases as pilots
   - Apply new process with additional support
   - Collect detailed feedback and metrics

3. **Phase 3: Incremental Rollout**
   - Gradually expand to all release types
   - Implement supporting tools and automation
   - Refine based on ongoing feedback

4. **Phase 4: Full Implementation**
   - Complete transition to new process
   - Retire old process artifacts and documentation
   - Establish ongoing improvement mechanism

### Support Mechanisms
During the transition, we will provide:
- Transition coaches for each team
- Office hours for questions and support
- Detailed guides for common scenarios
- Regular check-ins and feedback sessions
```

## Release Scope Classification Guidelines

Apply these guidelines to classify release system releases:

### Major Release System Indicators
- Significant changes to the overall process flow
- Introduction of new process phases or major artifacts
- Changes requiring substantial retraining
- Process changes affecting organizational interfaces
- New governance or compliance requirements
- Significant changes to tools and integrations

### Minor Release System Indicators
- Refinements to existing process phases
- Enhancement of existing artifacts
- Limited retraining requirements
- Process changes contained within organizational boundaries
- Adjustments to existing governance procedures
- Incremental improvements to tools and integrations

### Patch Release System Indicators
- Small adjustments to specific process steps
- Corrections to artifact templates
- Clarification of existing documentation
- No retraining required
- No changes to governance procedures
- Minor tool adjustments or fixes

### Emergency Release System Indicators
- Critical process fixes needed for compliance
- Corrections to prevent process failures
- Documentation clarifications to prevent errors
- Immediate governance or regulatory requirements
- Critical tool or integration fixes

## Release System-Specific Validation Checklist

Before completing the inception phase, validate:

- [ ] Process changes are clearly defined and documented
- [ ] Impact on existing processes is fully assessed
- [ ] Process metrics are identified with baselines and targets
- [ ] Affected Cursor rules and templates are identified
- [ ] Process transition approach is defined
- [ ] Backward compatibility considerations are addressed
- [ ] Meta-process debt is documented and assessed
- [ ] Process governance implications are identified
- [ ] Stakeholder impacts are evaluated
- [ ] Training and documentation needs are planned

## Context Transition Guidance

As you complete the release system inception phase and prepare for planning:

1. **Validate Completeness**:
   - Ensure all process aspects are addressed
   - Verify alignment with organizational objectives
   - Confirm feasibility of process changes

2. **Prepare for Planning**:
   - Gather necessary process specifications
   - Identify areas needing further investigation
   - Prepare for task breakdown

3. **Stakeholder Alignment**:
   - Ensure process changes are understood
   - Address process concerns and questions
   - Validate approach with key stakeholders

<important>
The release system inception phase establishes the foundation for process evolution. Be thorough in defining process boundaries and changes to ensure clear communication and prevent scope creep during implementation.
</important>