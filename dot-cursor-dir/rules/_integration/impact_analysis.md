---
description: USE WHEN evaluating cross-context changes: Provide structured framework for analyzing how changes in one system context impact other contexts, with comprehensive assessment techniques and mitigation strategies.
globs: 
alwaysApply: false
---
---
description: "Comprehensive impact analysis framework for changes that affect multiple contexts"
globs: "**/impact/*.md,**/impact/*.mdx,**/releases/*/impact.md,**/releases/*/impact.mdx"
priority: 1
alwaysApply: false
type: "Agent-Requested"
---

# Impact Analysis Framework

<critical>
Apply this framework when analyzing the impact of changes that affect multiple system contexts. Thorough impact analysis identifies ripple effects, uncovers hidden dependencies, and enables appropriate risk mitigation strategies for complex changes.
</critical>

## Impact Analysis Purpose

Impact analysis serves to:

1. **Identify Affected Components**: Determine all components affected by a change, including indirect impacts
2. **Uncover Hidden Dependencies**: Reveal non-obvious connections between components and contexts
3. **Assess Change Magnitude**: Evaluate the scope and complexity of required changes
4. **Identify Risks**: Recognize potential issues and unintended consequences
5. **Develop Mitigation Strategies**: Create approaches to address identified risks
6. **Guide Implementation Planning**: Inform the sequencing and coordination of changes

## Multi-Dimensional Impact Analysis

Changes must be analyzed across multiple dimensions:

### 1. System Context Dimension

Analyze impact across system contexts:

```markdown
## System Context Impact

### Code System Impact
- **Components Directly Affected**: [List of components]
- **Components Indirectly Affected**: [List of components]
- **Interface Changes Required**: [Description of interface changes]
- **Data Model Impact**: [Description of data model impacts]

### Release System Impact
- **Process Changes Required**: [Description of process changes]
- **Artifact Template Updates**: [List of affected templates]
- **Validation Approach Changes**: [Description of validation changes]
- **Deployment Strategy Impact**: [Description of deployment impacts]

### Agent System Impact
- **Knowledge Domain Updates**: [Description of knowledge updates]
- **Guidance Changes Required**: [Description of guidance changes]
- **Interaction Pattern Adjustments**: [Description of interaction changes]
- **Capability Enhancement Needs**: [Description of capability needs]
```

### 2. Principle Impact Dimension

Analyze how the change affects meta-systemic principles:

```markdown
## Principle Impact Analysis

### Parsimony Impact
- **New Concepts Introduced**: [List of new concepts]
- **Existing Concepts Modified**: [List of modified concepts]
- **Knowledge Reference Changes**: [Description of reference changes]
- **Information Duplication Risks**: [Description of duplication risks]

### Tensegrity Impact
- **Relationship Changes**: [Description of relationship changes]
- **Responsibility Shifts**: [Description of responsibility shifts]
- **Support Structure Modifications**: [Description of support changes]
- **Connection Point Adjustments**: [Description of connection changes]

### Modularity Impact
- **Boundary Changes**: [Description of boundary changes]
- **Interface Modifications**: [Description of interface changes]
- **Encapsulation Effects**: [Description of encapsulation impacts]
- **Coupling Implications**: [Description of coupling changes]

### Coherence Impact
- **Pattern Consistency Effects**: [Description of pattern impacts]
- **Naming Convention Implications**: [Description of naming impacts]
- **Structural Consistency Changes**: [Description of structural impacts]
- **Design Philosophy Alignment**: [Description of philosophy impacts]

### Clarity Impact
- **Documentation Requirements**: [Description of documentation needs]
- **Example Updates Needed**: [Description of example updates]
- **Explanation Complexity Changes**: [Description of explanation impacts]
- **Terminology Implications**: [Description of terminology impacts]

### Adaptivity Impact
- **Context Sensitivity Changes**: [Description of context sensitivity impacts]
- **Variation Management Needs**: [Description of variation management needs]
- **Evolution Path Implications**: [Description of evolution implications]
- **Standardization Versus Adaptation Tensions**: [Description of tensions]
```

### 3. Lifecycle Phase Dimension

Analyze impact across release lifecycle phases:

```markdown
## Lifecycle Phase Impact

### Inception Phase Impact
- **Definition Document Changes**: [Description of definition impacts]
- **Scope Delineation Changes**: [Description of scope impacts]
- **Objective Definition Impact**: [Description of objective impacts]
- **Classification Implications**: [Description of classification impacts]

### Planning Phase Impact
- **Task Breakdown Changes**: [Description of task breakdown impacts]
- **Dependency Mapping Implications**: [Description of dependency impacts]
- **Resource Allocation Adjustments**: [Description of resource impacts]
- **Timeline Implications**: [Description of timeline impacts]

### Development Phase Impact
- **Implementation Approach Changes**: [Description of implementation impacts]
- **Pattern Application Adjustments**: [Description of pattern impacts]
- **Component Integration Changes**: [Description of integration impacts]
- **Documentation Approach Impact**: [Description of documentation impacts]

### Validation Phase Impact
- **Validation Strategy Changes**: [Description of validation strategy impacts]
- **Test Coverage Implications**: [Description of test coverage impacts]
- **Quality Criteria Adjustments**: [Description of quality criteria impacts]
- **Verification Approach Changes**: [Description of verification impacts]

### Pre-Release Review Impact
- **Review Process Adjustments**: [Description of review process impacts]
- **Stakeholder Involvement Changes**: [Description of stakeholder impacts]
- **Go/No-Go Criteria Implications**: [Description of criteria impacts]
- **Approval Process Changes**: [Description of approval process impacts]

### Deployment Phase Impact
- **Deployment Strategy Adjustments**: [Description of deployment strategy impacts]
- **Rollout Approach Changes**: [Description of rollout impacts]
- **Verification Procedure Impacts**: [Description of verification impacts]
- **Rollback Capability Implications**: [Description of rollback impacts]

### Post-Release Evaluation Impact
- **Success Criteria Adjustments**: [Description of success criteria impacts]
- **Metrics Collection Changes**: [Description of metrics impacts]
- **Learning Capture Approach**: [Description of learning capture impacts]
- **Improvement Identification Methods**: [Description of improvement identification impacts]
```

### 4. Stakeholder Dimension

Analyze impact across stakeholder groups:

```markdown
## Stakeholder Impact

### Development Team Impact
- **Workflow Changes**: [Description of workflow impacts]
- **Tooling Adjustments**: [Description of tooling impacts]
- **Skill Requirements**: [Description of skill impacts]
- **Knowledge Needs**: [Description of knowledge needs]

### Operations Team Impact
- **Operational Procedure Changes**: [Description of procedure impacts]
- **Monitoring Adjustments**: [Description of monitoring impacts]
- **Support Process Implications**: [Description of support impacts]
- **Incident Response Changes**: [Description of incident response impacts]

### User Impact
- **User Experience Changes**: [Description of UX impacts]
- **Learning Curve Implications**: [Description of learning curve impacts]
- **Transition Requirements**: [Description of transition requirements]
- **Value Delivery Adjustments**: [Description of value delivery impacts]

### Business Stakeholder Impact
- **Business Process Changes**: [Description of business process impacts]
- **Value Proposition Implications**: [Description of value proposition impacts]
- **Compliance Implications**: [Description of compliance impacts]
- **Strategic Alignment Effects**: [Description of strategic alignment impacts]
```

## Impact Analysis Methods

### Dependency Mapping

Map dependencies to discover ripple effects:

```markdown
## Dependency Map

### Primary Dependencies
- **Component A** depends on **Component B** through [Interface X]
- **Component B** depends on **Component C** through [Data Flow Y]

### Secondary Dependencies
- **Component A** indirectly depends on **Component C** through **Component B**
- **Component D** indirectly depends on **Component A** through [Service Z]

### Cross-Context Dependencies
- **Code Component A** depends on **Agent Knowledge X**
- **Release Process B** depends on **Code Interface Y**

### Dependency Graph
[Include visual representation of dependency network]
```

### Change Vector Analysis

Analyze the direction and magnitude of changes:

```markdown
## Change Vector Analysis

### Change Vectors
| Component | Direction of Change | Magnitude | Complexity | Uncertainty |
|-----------|---------------------|-----------|------------|-------------|
| Component A | [Direction] | High/Medium/Low | High/Medium/Low | High/Medium/Low |
| Component B | [Direction] | High/Medium/Low | High/Medium/Low | High/Medium/Low |
| Component C | [Direction] | High/Medium/Low | High/Medium/Low | High/Medium/Low |

### Aggregate Change Characteristics
- **Overall Magnitude**: High/Medium/Low
- **Complexity Profile**: High/Medium/Low
- **Uncertainty Level**: High/Medium/Low
- **Risk Concentration**: [Areas of concentrated risk]
```

### Ripple Effect Analysis

Identify how changes propagate through the system:

```markdown
## Ripple Effect Analysis

### First-Order Effects
- Change to **Component A** directly affects **Components B, C, and D**
- Specific impacts: [List specific impacts]

### Second-Order Effects
- Effects on **Component B** propagate to **Components E and F**
- Effects on **Component C** propagate to **Component G**
- Specific impacts: [List specific impacts]

### Third-Order Effects
- Effects on **Component E** propagate to **Components H and I**
- Specific impacts: [List specific impacts]

### Propagation Paths
- Path 1: A → B → E → H → ...
- Path 2: A → C → G → ...
- Path 3: A → D → ...

### Propagation Termination
- Path 1 terminates at **Component J** because [reason]
- Path 2 terminates at **Component K** because [reason]
```

### CRUD Impact Analysis

Analyze Create, Read, Update, Delete operations affected:

```markdown
## CRUD Impact Analysis

### Data Entities Affected
| Entity | Create | Read | Update | Delete | Impacted Components |
|--------|--------|------|--------|--------|---------------------|
| Entity A | Yes/No | Yes/No | Yes/No | Yes/No | [Components] |
| Entity B | Yes/No | Yes/No | Yes/No | Yes/No | [Components] |
| Entity C | Yes/No | Yes/No | Yes/No | Yes/No | [Components] |

### Schema Changes
- **Entity A**: [Description of schema changes]
- **Entity B**: [Description of schema changes]
- **Entity C**: [Description of schema changes]

### Data Migration Requirements
- **Migration Path**: [Description of migration path]
- **Data Transformation Rules**: [Description of transformation rules]
- **Validation Requirements**: [Description of validation requirements]
```

### Interface Change Analysis

Analyze impacts on component interfaces:

```markdown
## Interface Change Analysis

### Interface Modifications
| Interface | Change Type | Breaking? | Affected Consumers | Migration Strategy |
|-----------|-------------|-----------|---------------------|-------------------|
| Interface A | [Type] | Yes/No | [Consumers] | [Strategy] |
| Interface B | [Type] | Yes/No | [Consumers] | [Strategy] |
| Interface C | [Type] | Yes/No | [Consumers] | [Strategy] |

### API Contract Changes
- **Endpoint A**: [Description of changes]
- **Endpoint B**: [Description of changes]
- **Endpoint C**: [Description of changes]

### Compatibility Strategy
- **Versioning Approach**: [Description of versioning approach]
- **Transition Period**: [Description of transition period]
- **Deprecation Timeline**: [Description of deprecation timeline]
```

## Impact Assessment and Risk Identification

### Comprehensive Risk Assessment

Identify risks based on impact analysis:

```markdown
## Risk Assessment

### Technical Risks
| Risk | Impact Area | Severity | Likelihood | Risk Score | Detection Method |
|------|-------------|----------|------------|------------|------------------|
| [Risk 1] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 2] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 3] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |

### Process Risks
| Risk | Impact Area | Severity | Likelihood | Risk Score | Detection Method |
|------|-------------|----------|------------|------------|------------------|
| [Risk 1] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 2] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 3] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |

### Organizational Risks
| Risk | Impact Area | Severity | Likelihood | Risk Score | Detection Method |
|------|-------------|----------|------------|------------|------------------|
| [Risk 1] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 2] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
| [Risk 3] | [Area] | High/Medium/Low | High/Medium/Low | [Score] | [Method] |
```

### Risk Mitigation Strategies

Develop mitigation approaches for identified risks:

```markdown
## Risk Mitigation Strategies

### Primary Mitigation Strategies
| Risk | Mitigation Approach | Responsibility | Effectiveness | Residual Risk |
|------|---------------------|----------------|---------------|---------------|
| [Risk 1] | [Approach] | [Owner] | High/Medium/Low | High/Medium/Low |
| [Risk 2] | [Approach] | [Owner] | High/Medium/Low | High/Medium/Low |
| [Risk 3] | [Approach] | [Owner] | High/Medium/Low | High/Medium/Low |

### Contingency Plans
- **Scenario 1**: [Description of risk scenario]
  - **Response Plan**: [Action plan]
  - **Trigger Conditions**: [Conditions]
  - **Decision Maker**: [Role]

- **Scenario 2**: [Description of risk scenario]
  - **Response Plan**: [Action plan]
  - **Trigger Conditions**: [Conditions]
  - **Decision Maker**: [Role]

### Risk Monitoring Approach
- **Key Risk Indicators**: [List of indicators]
- **Monitoring Frequency**: [Frequency]
- **Escalation Thresholds**: [Thresholds]
- **Reporting Process**: [Process]
```

## Implementation Planning Guidance

### Change Sequencing Recommendations

Recommend implementation sequence based on impact analysis:

```markdown
## Change Sequencing

### Recommended Implementation Sequence
1. **Phase 1**: [Components/changes] - [Rationale]
2. **Phase 2**: [Components/changes] - [Rationale]
3. **Phase 3**: [Components/changes] - [Rationale]

### Key Dependencies Driving Sequence
- **Dependency 1**: [Description]
- **Dependency 2**: [Description]
- **Dependency 3**: [Description]

### Critical Path Analysis
- **Critical Path**: [List of critical path items]
- **Bottlenecks**: [List of bottlenecks]
- **Parallel Opportunities**: [List of parallelizable work]
```

### Resource Allocation Guidance

Provide guidance on resource allocation based on impact:

```markdown
## Resource Allocation Guidance

### Skill Requirements
| Phase | Required Skills | Estimated Effort | Special Considerations |
|-------|----------------|------------------|------------------------|
| Phase 1 | [Skills] | [Effort] | [Considerations] |
| Phase 2 | [Skills] | [Effort] | [Considerations] |
| Phase 3 | [Skills] | [Effort] | [Considerations] |

### Critical Resources
- **Resource 1**: [Importance and allocation strategy]
- **Resource 2**: [Importance and allocation strategy]
- **Resource 3**: [Importance and allocation strategy]

### External Dependencies
- **Dependency 1**: [Management strategy]
- **Dependency 2**: [Management strategy]
- **Dependency 3**: [Management strategy]
```

### Testing and Validation Recommendations

Provide guidance on testing based on impact analysis:

```markdown
## Testing and Validation Guidance

### Critical Test Areas
| Area | Test Approach | Coverage Requirements | Validation Criteria |
|------|--------------|----------------------|---------------------|
| [Area 1] | [Approach] | [Coverage] | [Criteria] |
| [Area 2] | [Approach] | [Coverage] | [Criteria] |
| [Area 3] | [Approach] | [Coverage] | [Criteria] |

### Integration Test Focus
- **Integration Point 1**: [Testing strategy]
- **Integration Point 2**: [Testing strategy]
- **Integration Point 3**: [Testing strategy]

### Validation Sequence
1. **Stage 1**: [Validation focus] - [Approach]
2. **Stage 2**: [Validation focus] - [Approach]
3. **Stage 3**: [Validation focus] - [Approach]
```

## Context-Specific Impact Analysis

### Code System Impact Analysis

When analyzing impact on code systems:

1. **Component Analysis**:
   - Analyze direct code dependencies through import statements and API calls
   - Map data flow between components to identify hidden dependencies
   - Analyze schema dependencies and data model impacts
   - Review interaction with external systems and services

2. **Architecture Impact**:
   - Assess impact on architectural patterns and system structure
   - Identify cross-cutting concerns affected (logging, security, error handling)
   - Analyze performance and scalability implications
   - Review deployment architecture impacts

3. **Interface Evolution**:
   - Analyze public API changes and backward compatibility
   - Identify breaking vs. non-breaking changes
   - Determine versioning requirements
   - Plan interface migration approaches

4. **Quality Impact**:
   - Assess impact on testing strategy and coverage
   - Identify security implications
   - Analyze observability and monitoring impacts
   - Review error handling and resilience implications

### Release System Impact Analysis

When analyzing impact on release systems:

1. **Process Analysis**:
   - Identify affected release process steps
   - Analyze changes to process flow and dependencies
   - Review impact on approval workflows
   - Assess changes to validation procedures

2. **Artifact Impact**:
   - Identify templates requiring updates
   - Analyze changes to artifact structure and content
   - Review impact on artifact relationships
   - Assess documentation update requirements

3. **Tooling Impact**:
   - Analyze changes to CI/CD pipelines
   - Identify deployment tool modifications
   - Review testing infrastructure impacts
   - Assess monitoring and alerting changes

4. **Governance Impact**:
   - Review impacts on approval processes
   - Assess changes to quality gates
   - Analyze compliance implications
   - Identify stakeholder involvement changes

### Agent System Impact Analysis

When analyzing impact on agent systems:

1. **Knowledge Impact**:
   - Identify knowledge domains requiring updates
   - Analyze changes to conceptual models
   - Review impacts on knowledge references
   - Assess knowledge integration implications

2. **Capability Impact**:
   - Identify capabilities requiring enhancement
   - Analyze changes to capability boundaries
   - Review impacts on capability interactions
   - Assess new capability requirements

3. **Interaction Impact**:
   - Identify affected interaction patterns
   - Analyze changes to collaboration models
   - Review impacts on guidance effectiveness
   - Assess changes to communication approaches

4. **Guidance Impact**:
   - Identify guidance requiring updates
   - Analyze changes to examples and patterns
   - Review impacts on principle applications
   - Assess context-specific adaptation needs

## Meta-Systemic Impact Analysis

### Analyzing Principle Tensions

Identify and address principle tensions created by changes:

```markdown
## Principle Tension Analysis

### Identified Tensions

1. **[Principle A] vs. [Principle B]**
   - **Tension Description**: [Description of the tension]
   - **Affected Components**: [List of components]
   - **Current Balance**: [Description of current balance]
   - **Impact of Change**: [How the change affects this tension]
   - **Recommended Resolution**: [Approach to resolve or balance]

2. **[Principle C] vs. [Principle D]**
   - **Tension Description**: [Description of the tension]
   - **Affected Components**: [List of components]
   - **Current Balance**: [Description of current balance]
   - **Impact of Change**: [How the change affects this tension]
   - **Recommended Resolution**: [Approach to resolve or balance]
```

### Analyzing Principle Application Change

Assess how changes affect principle application:

```markdown
## Principle Application Change

### [Principle Name] Application Changes

- **Current Application**: [Description of current application]
- **Target Application**: [Description of target application]
- **Change Magnitude**: High/Medium/Low
- **Transition Approach**: [Description of transition approach]
- **Success Criteria**: [Criteria for successful transition]

### Cross-Principle Impact
| Principle | Impact | Adaptations Required |
|-----------|--------|----------------------|
| [Principle 1] | High/Medium/Low | [Required adaptations] |
| [Principle 2] | High/Medium/Low | [Required adaptations] |
| [Principle 3] | High/Medium/Low | [Required adaptations] |
```

## Impact Analysis Report Structure

Use this structure for comprehensive impact analysis reports:

```markdown
# Impact Analysis Report: [Change Name]

## 1. Executive Summary
Brief overview of the change, key impacts, critical risks, and recommended approach.

## 2. Change Description
Detailed description of the proposed change.

## 3. System Context Impact
Analysis of impact across code, release, and agent contexts.

## 4. Principle Impact
Analysis of impact on meta-systemic principle application.

## 5. Lifecycle Phase Impact
Analysis of impact across release lifecycle phases.

## 6. Stakeholder Impact
Analysis of impact on different stakeholder groups.

## 7. Dependency Analysis
Mapping of dependencies and ripple effects.

## 8. Risk Assessment
Comprehensive risk identification and mitigation strategies.

## 9. Implementation Recommendations
Guidance on sequencing, resources, and testing.

## 10. Conclusion
Summary of key findings and recommendations.
```

## Human-AI Collaboration in Impact Analysis

In our two-person team:

### Human Team Member Focus

1. **Strategic Impact Assessment**: Evaluate high-level business and strategic impacts
2. **Risk Prioritization**: Determine which risks are most significant
3. **Domain-Specific Analysis**: Provide specialized domain knowledge for impact assessment
4. **Subjective Impact Evaluation**: Assess qualitative impacts that require judgment
5. **Stakeholder Impact**: Evaluate impacts on stakeholder relationships and satisfaction

### AI Agent Focus

1. **Systematic Dependency Analysis**: Comprehensively map technical dependencies
2. **Pattern Recognition**: Identify similar patterns from previous changes
3. **Comprehensive Coverage**: Ensure all components and dimensions are analyzed
4. **Documentation**: Maintain detailed, structured impact documentation
5. **Consistency Checking**: Verify consistency of impact assessments across areas

## Impact Analysis Quality Checklist

Before finalizing impact analysis, verify that:

- [ ] All system contexts have been assessed (code, release, agent)
- [ ] All principles have been evaluated for impact
- [ ] All lifecycle phases have been analyzed
- [ ] All critical stakeholders have been considered
- [ ] Dependencies have been systematically mapped
- [ ] Ripple effects have been traced to termination
- [ ] Risks have been identified with mitigation strategies
- [ ] Implementation guidance is provided for planning
- [ ] Resources and skills needed are clearly identified
- [ ] Testing and validation approach is clearly defined

<important>
Thorough impact analysis is critical for complex changes, especially those spanning multiple system contexts. By systematically analyzing impacts across all dimensions, you can identify hidden dependencies, mitigate risks, and develop an effective implementation strategy that maintains system integrity.
</important>