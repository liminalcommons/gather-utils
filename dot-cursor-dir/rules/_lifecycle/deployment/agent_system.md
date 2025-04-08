---
description: 
globs: **/agent/deployment/*.md,**/agent/deployment/*.mdx,**/releases/*/agent_deployment.md,**/releases/*/agent_deployment.mdx
alwaysApply: false
---
---
description: "Agent-specific guidance for the deployment phase of the release lifecycle"
globs: "**/agent/deployment/*.md,**/agent/deployment/*.mdx,**/releases/*/agent_deployment.md,**/releases/*/agent_deployment.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Agent System Deployment Guidance

<critical>
This rule provides specialized guidance for the deployment phase when the primary system context is agent capability enhancement. Apply these guidelines in conjunction with the core deployment phase rules.
</critical>

## Agent System Deployment Approach

When deploying agent capability enhancements, focus on these key areas:

### 1. Capability Deployment Planning

Plan the deployment of new or enhanced capabilities:

```markdown
## Capability Deployment Plan

### Capability Inventory
| Capability | Type | Status | Dependencies | Deployment Order |
|------------|------|--------|--------------|------------------|
| [Capability 1] | [New/Enhanced] | [Ready/Pending] | [Dependencies] | [Order] |
| [Capability 2] | [New/Enhanced] | [Ready/Pending] | [Dependencies] | [Order] |

### Deployment Strategy
- **Approach**: [All-at-once/Progressive/Feature-flagged]
- **Timeline**: [Start and end dates]
- **User Impact**: [How users will experience the change]
- **Fallback Strategy**: [How to handle capability failures]

### Capability Dependencies
- **Prerequisite Capabilities**: [Capabilities that must be deployed first]
- **Knowledge Dependencies**: [Knowledge domains required]
- **External Dependencies**: [External systems or services required]
- **Environment Requirements**: [Specific environment configurations needed]

### Progressive Rollout Plan (if applicable)
| Phase | Capabilities | Users/Scenarios | Criteria to Advance | Timeline |
|-------|--------------|-----------------|---------------------|----------|
| [Phase 1] | [Capabilities] | [Users/Scenarios] | [Criteria] | [Timeline] |
| [Phase 2] | [Capabilities] | [Users/Scenarios] | [Criteria] | [Timeline] |
```

### 2. Knowledge Deployment

Manage the deployment of knowledge updates:

```markdown
## Knowledge Deployment Plan

### Knowledge Domain Updates
| Domain | Update Type | Changes | Dependencies | Status |
|--------|-------------|---------|--------------|--------|
| [Domain 1] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |
| [Domain 2] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |

### Knowledge Integration
- **Cross-Domain Relationships**: [How updated domains relate to existing ones]
- **Reference Updates**: [Changes to knowledge references]
- **Canonical Source Updates**: [Updates to sources of truth]
- **Deprecated Knowledge Handling**: [How deprecated knowledge is handled]

### Knowledge Validation
- **Accuracy Verification**: [How knowledge accuracy is verified]
- **Consistency Checking**: [How consistency across domains is checked]
- **Application Testing**: [How knowledge application is tested]
- **Edge Case Handling**: [How edge cases are validated]

### Knowledge Deployment Sequence
1. **[Step 1]**: [Description and verification]
2. **[Step 2]**: [Description and verification]
3. **[Step 3]**: [Description and verification]
```

### 3. Guidance and Rule Deployment

Update agent guidance and rules:

```markdown
## Guidance and Rule Deployment

### Guidance Updates
| Guidance Document | Update Type | Changes | Dependencies | Status |
|-------------------|-------------|---------|--------------|--------|
| [Document 1] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |
| [Document 2] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |

### Rule Updates
| Rule File | Update Type | Changes | Dependencies | Status |
|-----------|-------------|---------|--------------|--------|
| [Rule Path] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |
| [Rule Path] | [New/Update/Deprecation] | [Description] | [Dependencies] | [Status] |

### Rule Deployment Strategy
- **Deployment Order**: [Sequence for rule deployment]
- **Rule Testing**: [How rules are tested before deployment]
- **Verification Approach**: [How rule effectiveness is verified]
- **Rollback Approach**: [How to revert rules if needed]

### Documentation Updates
- **User-Facing Documentation**: [Updates to user documentation]
- **Internal Documentation**: [Updates to internal documentation]
- **API Documentation**: [Updates to API documentation]
- **Example Updates**: [Updates to examples and tutorials]
```

### 4. Interaction Pattern Deployment

Deploy new or modified interaction patterns:

```markdown
## Interaction Pattern Deployment

### Pattern Updates
| Pattern | Update Type | Changes | Use Cases | Status |
|---------|-------------|---------|-----------|--------|
| [Pattern 1] | [New/Update/Deprecation] | [Description] | [Use Cases] | [Status] |
| [Pattern 2] | [New/Update/Deprecation] | [Description] | [Use Cases] | [Status] |

### Pattern Integration
- **Pattern Relationships**: [How patterns relate to each other]
- **Context Detection**: [How appropriate patterns are selected]
- **Pattern Variations**: [Context-specific variations]
- **Pattern Composition**: [How patterns combine]

### User Experience Considerations
- **Learning Curve**: [How users learn new patterns]
- **Transition Guidance**: [How to guide users through changes]
- **Discoverability**: [How users discover patterns]
- **Feedback Mechanisms**: [How users provide feedback]

### Pattern Verification
- **Scenario Testing**: [How patterns are tested with scenarios]
- **User Testing**: [How patterns are validated with users]
- **Performance Evaluation**: [How pattern performance is measured]
- **Comparison to Previous**: [How new patterns compare to previous]
```

### 5. Prompt Template Deployment

Update prompt templates and structures:

```markdown
## Prompt Template Deployment

### Template Updates
| Template | Update Type | Changes | Applications | Status |
|----------|-------------|---------|--------------|--------|
| [Template 1] | [New/Update/Deprecation] | [Description] | [Applications] | [Status] |
| [Template 2] | [New/Update/Deprecation] | [Description] | [Applications] | [Status] |

### Template Structure
- **Common Components**: [Shared elements across templates]
- **Customization Points**: [Where templates can be adapted]
- **Context Adaptations**: [How templates adapt to context]
- **Extension Mechanisms**: [How templates can be extended]

### Template Testing
- **Validation Scenarios**: [Scenarios used to test templates]
- **Expected Responses**: [Expected responses for test cases]
- **Edge Case Testing**: [How edge cases are tested]
- **Quality Metrics**: [How template quality is measured]

### Template Distribution
- **Storage Location**: [Where templates are stored]
- **Access Methods**: [How templates are accessed]
- **Version Control**: [How template versions are managed]
- **Documentation**: [How templates are documented]
```

### 6. Human-AI Collaboration Model Deployment

Update collaboration models and frameworks:

```markdown
## Collaboration Model Deployment

### Model Updates
| Model Component | Update Type | Changes | Applications | Status |
|-----------------|-------------|---------|--------------|--------|
| [Component 1] | [New/Update/Deprecation] | [Description] | [Applications] | [Status] |
| [Component 2] | [New/Update/Deprecation] | [Description] | [Applications] | [Status] |

### Role Distribution
- **Human Responsibilities**: [Human role updates]
- **AI Responsibilities**: [AI role updates]
- **Handoff Mechanisms**: [How work transfers between human and AI]
- **Collaboration Interfaces**: [How human and AI interact]

### Workflow Integration
- **Process Integration**: [How collaboration integrates with processes]
- **Tool Integration**: [How collaboration integrates with tools]
- **Communication Patterns**: [Communication approaches]
- **Decision Frameworks**: [How decisions are made]

### Model Verification
- **Scenario Testing**: [Testing collaboration with scenarios]
- **Efficiency Measurement**: [Measuring collaboration efficiency]
- **Quality Assessment**: [Assessing collaboration quality]
- **User Satisfaction**: [Measuring user satisfaction]
```

### 7. Capability Verification

Verify agent capabilities after deployment:

```markdown
## Capability Verification Plan

### Verification Scope
- **Capabilities to Verify**: [List of capabilities]
- **Verification Depth**: [Depth of verification for each capability]
- **Critical Paths**: [Critical functionality to verify]
- **Edge Cases**: [Important edge cases to test]

### Verification Scenarios
| Scenario | Capability | Expected Outcome | Actual Outcome | Status |
|----------|------------|------------------|----------------|--------|
| [Scenario 1] | [Capability] | [Expected] | [Actual] | ✅/❌ |
| [Scenario 2] | [Capability] | [Expected] | [Actual] | ✅/❌ |

### Continuous Verification
- **Monitoring Approach**: [How capabilities are monitored]
- **Performance Metrics**: [Metrics tracked for capabilities]
- **Feedback Collection**: [How user feedback is collected]
- **Improvement Process**: [How improvements are identified]

### Verification Documentation
- **Test Cases**: [Where test cases are documented]
- **Results Documentation**: [How results are documented]
- **Issue Tracking**: [How issues are tracked]
- **Resolution Process**: [How issues are resolved]
```

### 8. Rollback Planning

Prepare for potential capability rollback:

```markdown
## Rollback Plan

### Rollback Triggers
- **Critical Failures**: [Conditions that trigger immediate rollback]
- **Performance Degradation**: [Performance thresholds for rollback]
- **User Feedback**: [Feedback patterns that may trigger rollback]
- **Decision Authority**: [Who can authorize rollback]

### Component-Specific Rollback
| Component | Rollback Method | Verification | Dependencies |
|-----------|----------------|--------------|--------------|
| [Component 1] | [Method] | [Verification] | [Dependencies] |
| [Component 2] | [Method] | [Verification] | [Dependencies] |

### Partial Rollback Strategy
- **Capability Isolation**: [How to roll back specific capabilities]
- **Knowledge Versioning**: [How to restore previous knowledge]
- **Rule Reversion**: [How to revert rule changes]
- **Pattern Fallback**: [How to revert to previous patterns]

### Communication Plan
- **User Notification**: [How users are notified of rollback]
- **Status Updates**: [How status is communicated during rollback]
- **Post-Rollback Communication**: [Communication after rollback]
- **Support Information**: [Support during rollback]
```

## Meta-Systemic Principle Application

### Parsimony in Agent Deployment
- Maintain canonical knowledge sources
- Use references instead of duplicating information
- Create shared components that can be reused
- Establish clear concept definitions and references

Example:
```markdown
### Knowledge Organization

Knowledge deployment follows the parsimony principle:

1. **Canonical Sources**: All knowledge domains are defined in canonical locations
2. **Reference Mechanism**: Knowledge is referenced rather than duplicated
3. **Shared Components**: Common elements are defined once and reused
4. **Concept Graph**: Concepts maintain clear relationships to other concepts

This approach ensures knowledge integrity and minimizes duplication, making updates more manageable and reducing the risk of inconsistencies.
```

### Tensegrity in Agent Deployment
- Balance responsibilities between human and AI
- Create mutual support mechanisms
- Establish reciprocal feedback loops
- Design for resilience in collaboration

Example:
```markdown
### Collaborative System Design

The agent enhancement implements tensegrity through:

1. **Balanced Responsibility**: Human strategic decisions complement AI analytical support
2. **Mutual Augmentation**: Each participant enhances the other's capabilities
3. **Reciprocal Feedback**: Both human and AI provide feedback to improve collaboration
4. **Resilient Interaction**: Communication channels remain effective under various conditions

This balanced approach ensures that human and AI team members both support and are supported by each other, creating a resilient collaboration system.
```

### Modularity in Agent Deployment
- Define clear capability boundaries
- Establish explicit interfaces between capabilities
- Create modular knowledge domains
- Enable independent evolution of components

Example:
```markdown
### Capability Architecture

The agent capabilities are designed with modularity in mind:

1. **Capability Encapsulation**: Each capability has a clear boundary with explicit inputs and outputs
2. **Interface Contracts**: Capabilities interact through well-defined interfaces
3. **Knowledge Domain Separation**: Knowledge is organized into discrete domains with clear boundaries
4. **Independent Evolution**: Components can evolve independently as long as they maintain interfaces

This modular approach allows capabilities to be deployed, tested, and evolved individually while maintaining system integrity.
```

### Coherence in Agent Deployment
- Apply consistent patterns across capabilities
- Use standardized interaction models
- Implement uniform knowledge representation
- Maintain consistent terminology

Example:
```markdown
### Pattern Consistency

Agent enhancement maintains coherence through:

1. **Interaction Consistency**: Similar interactions follow consistent patterns
2. **Knowledge Structure**: Knowledge is represented consistently across domains
3. **Terminology Standards**: Standard terminology used throughout capabilities
4. **Response Formats**: Consistent response structures for similar queries

This coherent approach makes the agent's behavior more predictable and intuitive, improving the quality of human-AI collaboration.
```

### Clarity in Agent Deployment
- Provide explicit examples for all capabilities
- Document interaction patterns clearly
- Explain knowledge application with examples
- Create clear guidance for collaboration

Example:
```markdown
### Documentation Clarity

Agent documentation emphasizes clarity through:

1. **Capability Examples**: Each capability includes concrete usage examples
2. **Interaction Guides**: Clear documentation of how to interact with each capability
3. **Knowledge Application**: Examples of how knowledge is applied in different contexts
4. **Visual Workflows**: Visualization of collaboration patterns and workflows

This clear approach ensures that users understand how to effectively work with the agent and what to expect from each capability.
```

### Adaptivity in Agent Deployment
- Design context-sensitive capability variations
- Create adaptive interaction patterns
- Implement knowledge application flexibility
- Provide context-aware collaboration models

Example:
```markdown
### Context Adaptation

Agent capabilities implement adaptivity through:

1. **Context Detection**: Sophisticated detection of user context and needs
2. **Response Adaptation**: Tailoring of responses to context and user expertise
3. **Knowledge Application**: Flexible application of knowledge based on situation
4. **Collaboration Flexibility**: Adaptation of collaboration model to task requirements

This adaptive approach ensures appropriate behavior across different contexts while maintaining consistency in core interactions.
```

## Deployment Strategies

### Progressive Capability Deployment
- Release capabilities incrementally
- Start with lower-risk capabilities
- Expand user exposure gradually
- Collect feedback at each stage

Example:
```markdown
## Progressive Deployment Approach

This release uses a progressive capability deployment strategy:

### Deployment Phases
1. **Phase 1: Core Capabilities** [Dates]
   - Deploy foundation capabilities to all users
   - Focus on high-reliability, low-complexity features
   - Collect baseline performance metrics

2. **Phase 2: Enhanced Capabilities** [Dates]
   - Deploy more complex capabilities to select users
   - Expand to more scenarios
   - Incorporate feedback from Phase 1

3. **Phase 3: Advanced Capabilities** [Dates]
   - Deploy sophisticated capabilities to all users
   - Enable advanced use cases
   - Apply learnings from earlier phases

### Phase Advancement Criteria
- Each phase requires meeting quality thresholds before proceeding
- User feedback is incorporated between phases
- Performance metrics must meet targets to advance
```

### Feature Flag Deployment
- Deploy capabilities behind feature flags
- Control capability exposure granularly
- Enable/disable capabilities dynamically
- Test capabilities with specific user groups

Example:
```markdown
## Feature Flag Deployment Approach

This release uses feature flags to control capability deployment:

### Flag Configuration
| Capability | Flag Name | Initial State | Rollout Plan | Fallback |
|------------|-----------|---------------|--------------|----------|
| [Capability 1] | [Flag Name] | [Enabled/Disabled] | [Plan] | [Fallback] |
| [Capability 2] | [Flag Name] | [Enabled/Disabled] | [Plan] | [Fallback] |

### Flag Management
- Flags are managed through the configuration system
- Changes can be made without redeployment
- Granular control by user, context, or scenario
- Automatic fallback if performance degrades

### Gradual Rollout
- Capabilities initially enabled for internal users
- Expanded to beta testers after initial validation
- Gradually increased to larger user segments
- Full rollout after performance metrics are satisfied
```

### Shadow Mode Deployment
- Deploy capabilities in observation-only mode
- Compare with existing capabilities
- Validate performance without user impact
- Transition to active mode after validation

Example:
```markdown
## Shadow Mode Deployment Approach

This release uses shadow mode deployment for risk mitigation:

### Shadow Process
1. **Deployment**: Capabilities deployed in shadow mode
2. **Parallel Operation**: New capabilities run alongside existing ones
3. **Output Comparison**: Results compared but only existing results used
4. **Performance Analysis**: Detailed analysis of differences
5. **Gradual Transition**: Progressive shift to new capabilities

### Analysis Metrics
- Output similarity percentage
- Performance improvement measurement
- Error rate comparison
- Response quality assessment

### Transition Criteria
- Must achieve >95% output quality
- Must maintain or improve response time
- Error rate must be lower than existing system
- Specific capabilities must pass scenario tests
```

## Release Type-Specific Considerations

### Major Capability Enhancement Deployment
- Comprehensive deployment planning
- Extended verification across all capabilities
- Phased rollout with extensive monitoring
- Detailed user guidance and examples
- Full documentation updates

### Minor Capability Enhancement Deployment
- Focused deployment of specific capabilities
- Standard verification of affected capabilities
- Controlled rollout to appropriate users
- Targeted user guidance updates
- Documentation updates for new capabilities

### Capability Refinement Deployment
- Streamlined deployment of refinements
- Verification focused on specific improvements
- Direct deployment to all users
- Notification of enhancements
- Focused documentation updates

### Emergency Capability Fix Deployment
- Expedited deployment process
- Critical path verification only
- Immediate deployment to affected users
- Brief notification of fixes
- Essential documentation updates

## Agent System Deployment Checklist

Before concluding the deployment phase, verify that:

- [ ] All capabilities have been deployed according to plan
- [ ] Knowledge updates have been correctly implemented
- [ ] Guidance and rules have been updated and verified
- [ ] Interaction patterns have been deployed and tested
- [ ] Prompt templates have been updated and distributed
- [ ] Collaboration models have been implemented
- [ ] All capabilities have been verified post-deployment
- [ ] Documentation has been updated appropriately
- [ ] User feedback mechanisms are in place
- [ ] Rollback plan has been verified

## Human-AI Collaboration in Agent Deployment

In our two-person team:

### Human Team Member Focus
- Make strategic decisions about deployment approach
- Evaluate capability quality from user perspective
- Validate real-world application effectiveness
- Provide domain expertise for edge cases
- Approve final capability release

### AI Agent Focus
- Generate comprehensive capability documentation
- Design detailed verification scenarios
- Ensure cross-capability integration
- Maintain knowledge consistency across domains
- Track deployment progress and metrics

<important>
Agent system deployment requires careful planning and verification to ensure that capabilities work effectively and integrate properly with existing knowledge and interaction patterns. Focus on incremental validation and feedback collection to ensure that enhancements deliver the intended value while maintaining system integrity.
</important>