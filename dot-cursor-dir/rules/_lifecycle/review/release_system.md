---
description: 
globs: **/process/review/*.md,**/process/review/*.mdx,**/releases/*/process_review.md,**/releases/*/process_review.mdx
alwaysApply: false
---
---
description: "Release process-specific guidance for the pre-release review phase"
globs: "**/process/review/*.md,**/process/review/*.mdx,**/releases/*/process_review.md,**/releases/*/process_review.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Release System Pre-Release Review Guidance

<critical>
This rule provides specialized guidance for the pre-release review phase when the primary system context is the release process itself. Apply these guidelines in conjunction with the core pre-release review rules to ensure process-specific quality assessment before deployment.
</critical>

## Release System Review Purpose

The pre-release review for release systems serves to:

1. Verify that all process changes have been properly implemented
2. Confirm that process documentation and artifacts meet quality standards
3. Ensure the process changes maintain meta-systemic integrity
4. Validate that process risks have been identified and mitigated
5. Make an informed go/no-go decision for implementing process changes

## Process-Specific Review Components

When conducting pre-release review for release process changes, include these specialized components:

### 1. Process Change Assessment

Comprehensive assessment of process changes:

```markdown
## Process Change Assessment

### Process Requirement Implementation
| Requirement | Implementation Status | Verification Method | Verified By |
|-------------|----------------------|---------------------|-------------|
| Enhanced validation checklist | ✅ Complete | Document review, simulation | [Name] |
| Streamlined approval workflow | ✅ Complete | Process walkthrough | [Name] |
| Updated artifact templates | ✅ Complete | Template review | [Name] |
| New rule implementation | ✅ Complete | Rule application test | [Name] |

### Process Change Quality
| Change Area | Quality Assessment | Evidence | Areas for Improvement |
|-------------|-------------------|----------|------------------------|
| Phase Structure | ✅ High Quality | Process simulation results | None identified |
| Documentation | ✅ High Quality | Template completeness assessment | None identified |
| Rule Guidance | ⚠️ Needs Improvement | Rule application test | Add more examples |
| Integration Points | ✅ High Quality | Cross-phase testing | None identified |

### Process Documentation Assessment
- **Completeness**: Documentation covers all process elements
- **Clarity**: Instructions are clear and unambiguous
- **Consistency**: Terminology is consistent throughout
- **Examples**: Appropriate examples are provided
```

### 2. Process Integrity Validation

Assessment of meta-systemic integrity of process changes:

```markdown
## Process Integrity Validation

### Meta-Systemic Principle Application
| Principle | Application Assessment | Evidence | Improvement Opportunities |
|-----------|------------------------|----------|---------------------------|
| Parsimony | ✅ Strong | Minimal duplication across documentation | None identified |
| Tensegrity | ✅ Strong | Balanced responsibilities across phases | None identified |
| Modularity | ✅ Strong | Clear phase boundaries with defined interfaces | None identified |
| Coherence | ⚠️ Moderate | Some terminology inconsistency | Standardize terminology |
| Clarity | ✅ Strong | Clear examples and guidance | None identified |
| Adaptivity | ✅ Strong | Context-sensitive process variations | None identified |

### Process Structure Integrity
- **Phase Boundaries**: Clear entry and exit criteria for each phase
- **Information Flow**: Smooth flow of information between phases
- **Responsibility Allocation**: Clear and balanced responsibilities
- **Decision Points**: Well-defined with appropriate authority

### Process Evolution Integrity
- **Backward Compatibility**: Changes maintain compatibility with existing artifacts
- **Migration Path**: Clear guidance for transition to new process
- **Historical Continuity**: Changes preserve core process intent
- **Documentation Evolution**: Documentation reflects process changes
```

### 3. Process Risk Assessment

Evaluation of risks associated with process changes:

```markdown
## Process Risk Assessment

### Identified Process Risks
| Risk | Impact | Likelihood | Mitigation | Status |
|------|--------|------------|------------|--------|
| Learning curve for new process | Medium | High | Comprehensive documentation, training sessions | ✅ Mitigated |
| Transition period confusion | High | Medium | Phased rollout, clear transition guidelines | ✅ Mitigated |
| Tool integration issues | Medium | Low | Thorough testing of all integrations | ✅ Mitigated |
| Resistance to change | Medium | Medium | Stakeholder engagement, clear benefits communication | ✅ Mitigated |

### Process Gap Analysis
- **Identified Gaps**: [List any gaps in the process implementation]
- **Gap Severity**: [Assessment of the impact of identified gaps]
- **Gap Mitigation**: [Approach to addressing any gaps]
- **Residual Risk**: [Remaining risk after mitigation]

### Cross-Phase Risk Assessment
- **Handoff Risks**: Assessment of risks at phase transitions
- **Artifact Consistency**: Evaluation of artifact consistency across phases
- **Communication Risks**: Analysis of potential communication issues
- **Scalability Risks**: Assessment of process scalability to different contexts
```

### 4. Process Simulation Results

Documentation of process testing through simulation:

```markdown
## Process Simulation Results

### Simulation Scenarios
| Scenario | Focus | Participants | Result |
|----------|-------|--------------|--------|
| Major Release Simulation | End-to-end process | Full team | ✅ Successful |
| Minor Release Simulation | Streamlined workflow | Core team | ✅ Successful |
| Emergency Release Simulation | Expedited process | Key stakeholders | ✅ Successful |
| Multi-Team Coordination | Cross-team collaboration | Team representatives | ⚠️ Partial Success |

### Simulation Findings
- **Process Flow**: [Assessment of process flow effectiveness]
- **Bottlenecks**: [Identification of any process bottlenecks]
- **Efficiency**: [Assessment of process efficiency]
- **Clarity**: [Evaluation of process clarity and understanding]

### Simulation Metrics
| Metric | Baseline | Target | Simulation Result | Assessment |
|--------|----------|--------|-------------------|------------|
| Process Duration | 21 days | 18 days | 17 days | ✅ Exceeds Target |
| Documentation Effort | 25% of total | 20% of total | 18% of total | ✅ Exceeds Target |
| Approval Cycle Time | 3 days | 1 day | 1 day | ✅ Meets Target |
| Error Rate | 5% | 2% | 2% | ✅ Meets Target |

### Participant Feedback
- **Usability**: [Feedback on process usability]
- **Pain Points**: [Identified pain points]
- **Improvement Suggestions**: [Suggestions from participants]
- **Overall Assessment**: [Overall evaluation from participants]
```

### 5. Process Artifact Verification

Verification of all process artifacts:

```markdown
## Process Artifact Verification

### Template Quality Assessment
| Template | Completeness | Clarity | Usability | Verified By |
|----------|--------------|--------|-----------|-------------|
| Release Definition Template | ✅ Complete | ✅ Clear | ✅ Usable | [Name] |
| Release Plan Template | ✅ Complete | ✅ Clear | ✅ Usable | [Name] |
| Validation Report Template | ✅ Complete | ✅ Clear | ✅ Usable | [Name] |
| Deployment Plan Template | ✅ Complete | ⚠️ Needs Clarification | ⚠️ Minor Issues | [Name] |

### Documentation Verification
- **Process Guide**: Comprehensive, clear, and accurate
- **Phase-Specific Guidance**: Complete for all phases
- **Rule Documentation**: Clear guidance with examples
- **Training Materials**: Effective for onboarding

### Tool Configuration Verification
- **Project Management Tool**: Correctly configured for new process
- **Document Repository**: Properly organized for artifact storage
- **Communication Tools**: Appropriately configured for process needs
- **Automation Scripts**: Validated for accuracy and reliability
```

### 6. Process Rollout Readiness

Assessment of readiness for process implementation:

```markdown
## Process Rollout Readiness

### Implementation Approach
- **Rollout Strategy**: [Phased/Immediate/Hybrid approach]
- **Timeline**: [Planned implementation timeline]
- **Transition Support**: [Support mechanisms during transition]
- **Feedback Collection**: [Approach to gathering implementation feedback]

### Training Readiness
- **Training Materials**: Complete and validated
- **Training Sessions**: Scheduled with appropriate participants
- **Reference Documentation**: Available and accessible
- **Support Process**: Established for questions and issues

### Communication Readiness
- **Announcement Plan**: Prepared with key messages
- **Stakeholder Communication**: Tailored for different audiences
- **Expectation Setting**: Clear communication of changes and benefits
- **Feedback Channels**: Established for process improvement

### Success Criteria
- **Adoption Metrics**: Defined to measure implementation success
- **Quality Metrics**: Established to assess process effectiveness
- **Satisfaction Metrics**: Planned to evaluate stakeholder acceptance
- **Efficiency Metrics**: Identified to measure process improvements
```

## Meta-Systemic Principle Application

### Parsimony
- Reference canonical process documentation
- Link to detailed simulation results rather than duplicating
- Refer to established process standards
- Maintain single source of truth for process definitions

Example:
```markdown
The updated release lifecycle process is defined in the [Release Lifecycle Framework](../process/release-lifecycle-framework.md) document, which serves as the canonical reference for all process elements.

For detailed simulation results, see the [Process Simulation Report](../simulation/process-simulation-report.md), which contains comprehensive data from all simulation scenarios.
```

### Tensegrity
- Evaluate balance between process phases
- Assess reciprocal value between process elements
- Verify mutual support between roles and responsibilities
- Ensure appropriate distribution of activities

Example:
```markdown
## Phase Relationship Assessment

| Phase Relationship | Value Exchange | Balance Assessment |
|-------------------|---------------|-------------------|
| Inception → Planning | Clear objectives enable effective planning | ✅ Balanced |
| Planning → Development | Detailed plan guides implementation | ✅ Balanced |
| Development → Validation | Incremental delivery enables effective validation | ✅ Balanced |
| Validation → Review | Comprehensive validation enables informed review | ✅ Balanced |
| Review → Deployment | Clear decision provides deployment confidence | ✅ Balanced |

The revised process maintains balanced relationships between phases, with each phase providing clear value to subsequent phases while receiving necessary inputs from preceding phases.
```

### Modularity
- Verify clear boundaries between process phases
- Validate interface contracts between phases
- Ensure appropriate encapsulation of phase activities
- Confirm independent evolution capability

Example:
```markdown
## Process Modularity Assessment

| Process Element | Boundary Clarity | Interface Definition | Encapsulation |
|-----------------|-----------------|---------------------|---------------|
| Inception Phase | ✅ Clear | ✅ Well-defined | ✅ Strong |
| Planning Phase | ✅ Clear | ✅ Well-defined | ✅ Strong |
| Development Phase | ✅ Clear | ✅ Well-defined | ✅ Strong |
| Validation Phase | ✅ Clear | ✅ Well-defined | ✅ Strong |
| Review Phase | ✅ Clear | ✅ Well-defined | ✅ Strong |

The process redesign has strengthened phase boundaries with explicit entry and exit criteria, clear artifact interfaces between phases, and proper encapsulation of phase-specific activities. This modularity enables independent evolution of individual phases while maintaining overall process integrity.
```

### Coherence
- Assess terminology consistency across documentation
- Verify consistent patterns across similar activities
- Ensure standard approaches for common elements
- Validate structural consistency across artifacts

Example:
```markdown
## Process Coherence Assessment

| Coherence Aspect | Assessment | Improvement Opportunities |
|------------------|------------|---------------------------|
| Terminology | ⚠️ Moderate | Standardize approval terminology across phases |
| Activity Patterns | ✅ Strong | None identified |
| Documentation Structure | ✅ Strong | None identified |
| Artifact Format | ✅ Strong | None identified |

The process demonstrates strong coherence in most areas, with consistent approaches applied to similar activities across phases. The terminology inconsistency in approval processes should be addressed before finalizing the process implementation.
```

### Clarity
- Verify clear documentation for all process elements
- Ensure concrete examples for complex activities
- Validate unambiguous guidance for process execution
- Confirm explicit rationale for process decisions

Example:
```markdown
## Process Clarity Assessment

| Documentation Element | Clarity Assessment | Examples | Actionable |
|-----------------------|-------------------|----------|------------|
| Phase Descriptions | ✅ High | ✅ Comprehensive | ✅ Yes |
| Activity Guides | ✅ High | ✅ Comprehensive | ✅ Yes |
| Artifact Templates | ✅ High | ✅ Comprehensive | ✅ Yes |
| Role Definitions | ⚠️ Moderate | ⚠️ Limited | ⚠️ Partially |

The process documentation provides clear guidance with comprehensive examples for most elements. The role definitions would benefit from more concrete examples of responsibilities and activities for each role.
```

### Adaptivity
- Validate context-sensitive process variations
- Assess appropriate adaptations for different release types
- Verify balanced standardization and flexibility
- Confirm preservation of core intent across adaptations

Example:
```markdown
## Process Adaptation Assessment

| Context Variation | Adaptation Approach | Effectiveness | Integrity Preservation |
|-------------------|---------------------|--------------|------------------------|
| Major Release | Comprehensive process | ✅ Effective | ✅ Maintained |
| Minor Release | Streamlined reviews | ✅ Effective | ✅ Maintained |
| Patch Release | Focused validation | ✅ Effective | ✅ Maintained |
| Emergency Release | Expedited workflow | ✅ Effective | ✅ Maintained |

The process adaptations appropriately adjust rigor and detail based on release type while maintaining the core structure and intent of the process. Each adaptation preserves essential quality controls while eliminating unnecessary overhead for smaller-scope releases.
```

## Release Scope-Specific Review Considerations

### Major Process Change Review
- Comprehensive review of all process elements
- In-depth simulation across multiple scenarios
- Thorough stakeholder engagement and feedback
- Detailed migration plan assessment
- Complete documentation review

### Minor Process Change Review
- Focused review on changed process elements
- Targeted simulation of affected activities
- Relevant stakeholder consultation
- Specific update guidance
- Review of updated documentation

### Process Refinement Review
- Specific review of refined process elements
- Validation of refinement effectiveness
- Limited stakeholder verification
- Minimal transition requirements
- Review of amended documentation

### Emergency Process Change Review
- Critical assessment of process modification
- Verification of critical path effectiveness
- Essential stakeholder notification
- Immediate implementation guidance
- Review of critical documentation updates

## Process Go/No-Go Decision Guidance

Framework for making the process implementation decision:

```markdown
## Process Implementation Go/No-Go Decision

### Critical Criteria (Must All Pass)
- [ ] All required process changes implemented and verified
- [ ] Process documentation complete and validated
- [ ] Process simulation successfully completed
- [ ] No critical risks identified without mitigation
- [ ] Core stakeholders approved the changes
- [ ] Rollout and transition plan in place

### Important Criteria (Majority Should Pass)
- [ ] All process artifacts meet quality standards
- [ ] Training materials and support ready
- [ ] All tools properly configured
- [ ] Communication plan prepared
- [ ] Feedback mechanisms established
- [ ] Metrics defined for process evaluation

### Decision Options
1. **Go**: All critical criteria pass, majority of important criteria pass
2. **Conditional Go**: All critical criteria pass, some important criteria need attention post-implementation
3. **No-Go**: Any critical criteria fail or too many important criteria fail

### Decision Rationale
[Document the rationale for the go/no-go decision, including any conditions or follow-up actions]
```

## Human-AI Team Collaboration

In our two-person team:

### Human Team Member Focus
- Make final go/no-go decisions
- Evaluate subjective process effectiveness
- Assess organizational readiness for change
- Provide domain expertise for complex scenarios
- Validate stakeholder acceptance

### AI Agent Focus
- Systematically validate process documentation
- Generate comprehensive review documentation
- Identify potential issues from pattern analysis
- Ensure meta-systemic principle application
- Track resolution of previously identified issues

<important>
The pre-release review for process changes ensures that the release lifecycle itself continues to evolve while maintaining integrity. A thorough review validates that process changes are well-designed, properly documented, and ready for implementation, with appropriate support for the transition to the new process.
</important>