---
description: 
globs: **/process/deployment/*.md,**/process/deployment/*.mdx,**/releases/*/process_deployment.md,**/releases/*/process_deployment.mdx
alwaysApply: false
---
---
description: "Release process-specific guidance for the deployment phase of the release lifecycle"
globs: "**/process/deployment/*.md,**/process/deployment/*.mdx,**/releases/*/process_deployment.md,**/releases/*/process_deployment.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Release System Deployment Guidance

<critical>
This rule provides specialized guidance for the deployment phase when the primary system context is release process evolution. Apply these guidelines in conjunction with the core deployment phase rules.
</critical>

## Release Process Deployment Approach

When deploying changes to the release process itself, focus on these key areas:

### 1. Process Transition Planning

Plan the transition to the new process:

```markdown
## Process Transition Plan

### Current Process Baseline
- **Current Process Version**: [Version]
- **Key Components**: [List of components]
- **Known Issues**: [List of issues being addressed]
- **Key Metrics**: [Current performance metrics]

### Transition Strategy
- **Approach**: [Big bang/Incremental/Parallel/Phased]
- **Timeline**: [Start and end dates for transition]
- **Affected Teams**: [Teams impacted by the change]
- **Training Requirements**: [Training needed for the new process]

### Transition Phases
| Phase | Description | Start Date | End Date | Success Criteria | 
|-------|-------------|------------|----------|------------------|
| [Phase 1] | [Description] | [Date] | [Date] | [Criteria] |
| [Phase 2] | [Description] | [Date] | [Date] | [Criteria] |
| [Phase 3] | [Description] | [Date] | [Date] | [Criteria] |

### In-Progress Work Handling
- **Current Cycle Treatment**: [How in-progress releases will be handled]
- **Transition Rules**: [Rules for when to apply old vs. new process]
- **Exception Process**: [How to handle special cases]
- **Backlog Treatment**: [How existing backlog items will be transitioned]
```

### 2. Documentation Deployment

Manage documentation updates effectively:

```markdown
## Documentation Deployment Plan

### Documentation Updates
| Document | Current Version | New Version | Changes | Location |
|----------|----------------|-------------|---------|----------|
| [Document 1] | [Version] | [Version] | [Summary of changes] | [Location] |
| [Document 2] | [Version] | [Version] | [Summary of changes] | [Location] |

### Documentation Deployment Approach
- **Release Method**: [How documentation will be released]
- **Version Control**: [How versions will be managed]
- **Archiving Strategy**: [How old documentation will be archived]
- **Notification Process**: [How users will be notified of updates]

### Verification Steps
- **Link Validation**: [How to verify all links work]
- **Content Validation**: [How to validate content accuracy]
- **Formatting Verification**: [How to check formatting]
- **Cross-reference Integrity**: [How to verify cross-references]

### Access Control
- **Permission Updates**: [Changes to documentation access]
- **Role Assignments**: [Documentation role assignments]
- **Security Review**: [Security verification for sensitive docs]
```

### 3. Tool and Configuration Updates

Manage tools and configurations supporting the release process:

```markdown
## Tool and Configuration Deployment

### Tool Updates
| Tool | Current Version | New Version | Changes | Deployment Method |
|------|----------------|-------------|---------|-------------------|
| [Tool 1] | [Version] | [Version] | [Changes] | [Method] |
| [Tool 2] | [Version] | [Version] | [Changes] | [Method] |

### Configuration Changes
| System | Configuration | Current Value | New Value | Impact |
|--------|--------------|---------------|-----------|--------|
| [System 1] | [Config Item] | [Value] | [Value] | [Impact] |
| [System 2] | [Config Item] | [Value] | [Value] | [Impact] |

### Integration Updates
- **API Changes**: [Updates to APIs]
- **Webhook Updates**: [Changes to webhooks]
- **Authentication Updates**: [Changes to authentication]
- **Data Exchange Format**: [Changes to data formats]

### Deployment Sequence
1. **[Step 1]**: [Description and verification]
2. **[Step 2]**: [Description and verification]
3. **[Step 3]**: [Description and verification]
```

### 4. Cursor Rule Deployment

Update Cursor rules systematically:

```markdown
## Cursor Rule Deployment

### Rule Updates
| Rule File | Current Version | New Version | Changes | Status |
|-----------|----------------|-------------|---------|--------|
| [Rule Path] | [Version] | [Version] | [Changes] | ✅/❌ |
| [Rule Path] | [Version] | [Version] | [Changes] | ✅/❌ |

### Rule Testing
- **Test Scenarios**: [Scenarios used to test rules]
- **Expected Behavior**: [How rules should behave]
- **Actual Results**: [Observed behavior]
- **Adjustments Made**: [Changes made based on testing]

### Deployment Strategy
- **Deployment Order**: [Sequence for rule deployment]
- **Verification Steps**: [How to verify rules are working]
- **Fallback Approach**: [How to revert to previous rules]
- **Compatibility Considerations**: [Compatibility with existing assets]

### Rule Documentation
- **Rule Purpose Documentation**: [Documentation of rule intent]
- **Usage Examples**: [Examples of rule application]
- **Integration Documentation**: [How rules integrate with process]
```

### 5. Template Deployment

Update templates supporting the release process:

```markdown
## Template Deployment

### Template Updates
| Template | Current Version | New Version | Changes | Location |
|----------|----------------|-------------|---------|----------|
| [Template 1] | [Version] | [Version] | [Changes] | [Location] |
| [Template 2] | [Version] | [Version] | [Changes] | [Location] |

### Example Migration
- **Old Format Example**: [Example of old template]
- **New Format Example**: [Example of new template]
- **Migration Guidance**: [How to convert from old to new]
- **Backward Compatibility**: [How backward compatibility is handled]

### Template Verification
- **Validation Tests**: [Tests performed on templates]
- **Usability Feedback**: [Feedback from testers]
- **Edge Case Testing**: [Testing with unusual inputs]
- **Integration Testing**: [Testing with other system components]

### Deployment Approach
- **Distribution Method**: [How templates will be distributed]
- **User Notification**: [How users will be notified]
- **Support Resources**: [Resources for template assistance]
- **Feedback Collection**: [How feedback will be gathered]
```

### 6. Training and Communication

Prepare stakeholders for the process change:

```markdown
## Training and Communication Plan

### Stakeholder Analysis
| Stakeholder Group | Impact Level | Training Needs | Communication Channel |
|-------------------|--------------|---------------|----------------------|
| [Group 1] | [High/Medium/Low] | [Training needs] | [Channels] |
| [Group 2] | [High/Medium/Low] | [Training needs] | [Channels] |

### Communication Timeline
| Date | Event | Audience | Message | Medium | Responsibility |
|------|-------|----------|---------|--------|----------------|
| [Date] | [Event] | [Audience] | [Message] | [Medium] | [Person] |
| [Date] | [Event] | [Audience] | [Message] | [Medium] | [Person] |

### Training Materials
- **Documentation**: [Process documentation]
- **Tutorials**: [Step-by-step guides]
- **Workshops**: [Interactive training sessions]
- **FAQ**: [Frequently asked questions]

### Support Strategy
- **Support Channels**: [How users can get help]
- **Support Period**: [Duration of enhanced support]
- **Escalation Path**: [How to escalate issues]
- **Feedback Mechanism**: [How to provide feedback]
```

### 7. Process Verification

Verify the new process works as intended:

```markdown
## Process Verification Plan

### Verification Scope
- **Process Components**: [Components to be verified]
- **Critical Paths**: [Critical process paths to test]
- **Edge Cases**: [Edge cases to be verified]
- **Integration Points**: [Integration points to verify]

### Test Cases
| ID | Scenario | Expected Outcome | Actual Outcome | Status |
|----|----------|------------------|----------------|--------|
| [ID] | [Scenario] | [Expected] | [Actual] | ✅/❌ |
| [ID] | [Scenario] | [Expected] | [Actual] | ✅/❌ |

### Process Simulation
- **Simulation Approach**: [How process will be simulated]
- **Test Data**: [Data to be used in simulation]
- **Participants**: [Who will participate in simulation]
- **Success Criteria**: [Criteria for successful simulation]

### Metrics Collection
- **Key Metrics**: [Metrics to be tracked]
- **Baseline Comparison**: [Comparison to previous process]
- **Performance Targets**: [Expected performance improvements]
- **Measurement Method**: [How metrics will be collected]
```

### 8. Rollback Planning

Prepare for potential process rollback:

```markdown
## Rollback Plan

### Rollback Triggers
- **Critical Failures**: [Conditions that trigger immediate rollback]
- **Performance Degradation**: [Performance thresholds for rollback]
- **User Feedback**: [Feedback patterns that may trigger rollback]
- **Decision Authority**: [Who can authorize rollback]

### Rollback Process
1. **Communication**: [How rollback will be communicated]
2. **Documentation Restoration**: [How to restore previous documentation]
3. **Tool Configuration**: [How to restore previous configuration]
4. **Rule Rollback**: [How to restore previous rules]
5. **Template Restoration**: [How to restore previous templates]

### In-Progress Work Handling
- **Treatment Guidance**: [How to handle in-progress work during rollback]
- **Data Migration**: [How to migrate data if needed]
- **User Instructions**: [Instructions for users during rollback]
- **Support Escalation**: [Enhanced support during rollback]

### Post-Rollback Analysis
- **Failure Analysis**: [How to analyze what went wrong]
- **Improvement Identification**: [Process for identifying improvements]
- **Re-deployment Planning**: [Planning for subsequent deployment]
- **Documentation**: [How to document the rollback]
```

## Meta-Systemic Principle Application

### Parsimony in Process Deployment
- Create single source of truth for process documentation
- Use reference links instead of duplicating information
- Maintain version-controlled assets with clear provenance
- Develop shared resources that can be referenced across documents

Example:
```markdown
### Documentation Structure

The process documentation is structured according to parsimony principles:

1. **Canonical Definitions**: Core process concepts are defined once in the `.cursor/rules/_kernel` directory and referenced elsewhere
2. **Process Diagrams**: Centralized in the `diagrams` repository and referenced by ID
3. **Term Glossary**: Single glossary maintained for consistent terminology
4. **Template Repository**: Templates stored in a central location and linked from documentation

This approach ensures consistency and minimizes duplication while making updates more manageable.
```

### Tensegrity in Process Deployment
- Design mutual support between process components
- Create balanced responsibilities across teams
- Establish bidirectional feedback mechanisms
- Ensure resilient connections between process phases

Example:
```markdown
### Process Component Relationships

The process implementation demonstrates tensegrity through:

1. **Phase Integration**: Each phase both provides input to and consumes output from adjacent phases
2. **Balanced Responsibilities**: Workload is distributed across teams with complementary responsibilities
3. **Reciprocal Validation**: Components validate each other's outputs before proceeding
4. **Feedback Loops**: Structured feedback mechanisms between process components

This balanced approach ensures that process components support each other while maintaining overall integrity.
```

### Modularity in Process Deployment
- Define clear boundaries between process phases
- Establish explicit interfaces between components
- Create well-defined entry and exit criteria
- Enable independent evolution of process components

Example:
```markdown
### Process Modularity

The process design implements modularity through:

1. **Phase Encapsulation**: Each phase has clear boundaries with explicit entry and exit criteria
2. **Interface Contracts**: Standardized artifact formats define interfaces between phases
3. **Component Independence**: Components can evolve independently as long as they maintain interface contracts
4. **Responsible Ownership**: Each component has clear ownership and maintenance responsibilities

This modular approach allows individual process components to evolve while maintaining system integrity.
```

### Coherence in Process Deployment
- Apply consistent patterns across the process
- Use standard terminology throughout documentation
- Implement similar approaches for similar tasks
- Maintain structural consistency in artifacts

Example:
```markdown
### Process Coherence

Process coherence is maintained through:

1. **Pattern Consistency**: Similar activities follow consistent patterns across phases
2. **Terminology Alignment**: Standard terminology used throughout all documentation
3. **Structural Similarity**: Artifacts follow consistent structures appropriate to their purpose
4. **Interaction Patterns**: Standardized interaction patterns between roles and components

This coherent approach makes the process more intuitive and reduces cognitive load for participants.
```

### Clarity in Process Deployment
- Provide concrete examples for all process steps
- Document rationale for process decisions
- Include visual aids to clarify workflows
- Supply templates with guidance and examples

Example:
```markdown
### Process Clarity

The process documentation emphasizes clarity through:

1. **Explicit Examples**: Each process component includes concrete examples of artifacts and activities
2. **Visual Workflows**: Process flows are visualized with annotated diagrams
3. **Decision Rationale**: Key process decisions include explanations of their purpose and intent
4. **Progressive Detail**: Documentation provides both high-level overview and detailed implementation guidance

This clear approach ensures that all participants understand both what to do and why they're doing it.
```

### Adaptivity in Process Deployment
- Design context-sensitive process variations
- Create appropriate adaptations for different release types
- Provide guidance for scaling effort to release scope
- Establish clear adaptation boundaries and principles

Example:
```markdown
### Process Adaptivity

The process is designed for appropriate adaptation through:

1. **Context-Sensitive Guidance**: Process guidance adapts to release type and complexity
2. **Scaling Framework**: Clear guidance on how to scale effort based on release scope
3. **Explicit Variation Points**: Documented points where the process can be appropriately adapted
4. **Adaptation Boundaries**: Clear limits on adaptation to maintain process integrity

This adaptive approach ensures appropriate process application across different contexts while maintaining core integrity.
```

## Process Transition Strategies

### Complete Transition Strategy
- Switch entirely from old to new process
- All teams migrate simultaneously
- Comprehensive training before transition
- Clean break with previous process

Example:
```markdown
## Complete Transition Approach

This release uses a complete transition strategy:

### Transition Timeline
- **Preparation Phase**: [Dates] - All documentation, training, and tools prepared
- **Training Phase**: [Dates] - All teams trained on new process
- **Cutover Date**: [Date] - Complete switch to new process
- **Support Phase**: [Dates] - Enhanced support during initial adoption

### Current Work Handling
- All in-progress releases will complete using the old process
- New releases starting after [Date] will use the new process
- No parallel operation period

### Success Metrics
- 100% of new releases following new process
- All teams trained prior to cutover
- Documentation and tools fully updated before transition
```

### Incremental Transition Strategy
- Phase in process changes gradually
- Implement changes in logical groupings
- Train teams progressively as changes affect them
- Build on each incremental change

Example:
```markdown
## Incremental Transition Approach

This release uses an incremental transition strategy:

### Transition Increments
1. **Phase 1: Documentation Updates** [Dates]
   - New templates and guidance deployed
   - Teams trained on new documentation
   - Both old and new documentation available

2. **Phase 2: Process Flow Changes** [Dates]
   - New workflow implemented
   - Task transitions updated
   - Teams trained on new flows

3. **Phase 3: Tool Integration** [Dates]
   - Tool configurations updated
   - Automation implemented
   - Technical training provided

### Increment Success Criteria
- Each increment must be successfully validated before proceeding
- Feedback incorporated between increments
- User acceptance verified at each step
```

### Parallel Operation Strategy
- Run old and new processes concurrently
- Allow teams to choose transition timing
- Gather feedback from early adopters
- Gradually transition all teams

Example:
```markdown
## Parallel Operation Approach

This release uses a parallel operation strategy:

### Parallel Timeline
- **Setup Phase**: [Dates] - New process fully documented and available
- **Early Adoption**: [Dates] - Volunteer teams use new process
- **General Availability**: [Dates] - All teams may choose which process to use
- **Sunset Old Process**: [Date] - Old process retired, all teams on new process

### Team Migration
- Teams may opt in to the new process starting [Date]
- Teams must commit to full migration (not mixing processes)
- Early adopter support and feedback mechanisms established
- Migration assistance provided to teams as they transition

### Transition Tracking
- Migration dashboard tracks team adoption
- Weekly feedback sessions during parallel period
- Process refinements implemented based on feedback
- Success metrics tracked for both processes during transition
```

## Release Type-Specific Considerations

### Major Process Change Deployment
- Comprehensive transition planning
- Extensive training program
- Detailed communication strategy
- Complete documentation overhaul
- Extended support during transition

### Minor Process Enhancement Deployment
- Focused transition for affected components
- Targeted training for specific changes
- Standard communication approach
- Updated documentation for changed elements
- Regular support during transition

### Process Refinement Deployment
- Minimal transition requirements
- Notification rather than formal training
- Brief communication of changes
- Documentation updates for specific items
- Standard support during transition

### Emergency Process Fix Deployment
- Expedited deployment of critical process fixes
- Just-in-time notification and guidance
- Focused communication on affected areas
- Essential documentation updates
- Enhanced support for affected process steps

## Release System Deployment Checklist

Before concluding the deployment phase, verify that:

- [ ] All process documentation has been updated and published
- [ ] Supporting tools and configurations have been deployed
- [ ] Cursor rules have been updated and verified
- [ ] Templates have been updated and distributed
- [ ] Training has been provided to affected stakeholders
- [ ] Process has been verified through appropriate testing
- [ ] Communication plan has been fully executed
- [ ] Feedback mechanisms are in place
- [ ] Support resources are available
- [ ] Rollback plan has been verified

## Human-AI Collaboration in Process Deployment

In our two-person team:

### Human Team Member Focus
- Make strategic decisions about transition approach
- Evaluate stakeholder readiness and impact
- Validate process effectiveness from user perspective
- Provide domain expertise for edge cases
- Approve final process documentation and training

### AI Agent Focus
- Generate comprehensive documentation updates
- Ensure cross-reference integrity across documents
- Develop detailed process verification plans
- Create consistent templates based on process requirements
- Maintain alignment with meta-systemic principles

<important>
The deployment of release process changes requires careful planning and coordination to ensure a smooth transition while maintaining system integrity. Focus on comprehensive documentation, appropriate training, and thorough verification to ensure the new process is effectively adopted.
</important>