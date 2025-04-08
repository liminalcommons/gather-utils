---
description: 
globs: **/agent/review/*.md,**/agent/review/*.mdx,**/releases/*/agent_review.md,**/releases/*/agent_review.mdx
alwaysApply: false
---
---
description: "Agent-specific guidance for the pre-release review phase of the release lifecycle"
globs: "**/agent/review/*.md,**/agent/review/*.mdx,**/releases/*/agent_review.md,**/releases/*/agent_review.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Agent System Pre-Release Review Guidance

<critical>
This rule provides specialized guidance for the pre-release review phase when the primary system context is agent capability enhancement. Apply these guidelines in conjunction with the core pre-release review rules.
</critical>

## Agent Capability Review

When reviewing agent system releases, focus on these key areas:

### 1. Capability Validation

Comprehensively assess agent capabilities:

```markdown
## Capability Validation Checklist

| Capability | Validation Method | Success Criteria | Status | Evidence |
|------------|-------------------|------------------|--------|----------|
| [Capability 1] | [Method] | [Criteria] | ✅/⚠️/❌ | [Link to Evidence] |
| [Capability 2] | [Method] | [Criteria] | ✅/⚠️/❌ | [Link to Evidence] |
| [Capability 3] | [Method] | [Criteria] | ✅/⚠️/❌ | [Link to Evidence] |

### Capability Scenarios
For each capability, verify performance across these scenarios:
- Standard use case scenario
- Edge case handling
- Error recovery scenario
- Integration with other capabilities
- Context-sensitive adaptation
```

### 2. Knowledge Domain Assessment

Evaluate the agent's knowledge domains:

```markdown
## Knowledge Domain Assessment

### Domain Coverage
- **Primary Knowledge Domains**: [List domains]
- **Interdomain Relationships**: [Describe how domains connect]
- **Knowledge Gaps**: [Identify any remaining gaps]

### Knowledge Application
| Domain | Application Scenario | Expected Response | Actual Response | Assessment |
|--------|---------------------|-------------------|-----------------|------------|
| [Domain 1] | [Scenario] | [Expected] | [Actual] | ✅/⚠️/❌ |
| [Domain 2] | [Scenario] | [Expected] | [Actual] | ✅/⚠️/❌ |

### Knowledge Evolution
- **Updated Knowledge Areas**: [List areas with updated knowledge]
- **Deprecated Knowledge**: [List deprecated knowledge with transition plan]
- **Knowledge Continuity**: [Describe how knowledge continuity is maintained]
```

### 3. Human-AI Collaboration Assessment

Review the collaboration model:

```markdown
## Human-AI Collaboration Assessment

### Collaboration Patterns
| Pattern | Use Case | Effectiveness | Improvement Areas |
|---------|----------|---------------|-------------------|
| [Pattern 1] | [Use Case] | [Rating] | [Areas] |
| [Pattern 2] | [Use Case] | [Rating] | [Areas] |

### Role Balance
- **Human Responsibilities**: [List key responsibilities]
- **AI Responsibilities**: [List key responsibilities]
- **Handoff Mechanisms**: [Describe how work transfers between human and AI]
- **Escalation Procedures**: [Document escalation paths]

### Communication Effectiveness
- **Clarity of AI Communication**: [Assessment]
- **Context Retention**: [Assessment]
- **Information Exchange Efficiency**: [Assessment]
- **Mutual Understanding**: [Assessment]
```

### 4. Interaction Pattern Review

Evaluate interaction designs:

```markdown
## Interaction Pattern Review

### Pattern Effectiveness
| Pattern | Purpose | Scenarios Tested | Effectiveness | User Feedback |
|---------|---------|------------------|---------------|---------------|
| [Pattern 1] | [Purpose] | [Scenarios] | [Rating] | [Feedback] |
| [Pattern 2] | [Purpose] | [Scenarios] | [Rating] | [Feedback] |

### Context Sensitivity
- **Context Detection Accuracy**: [Assessment]
- **Adaptation Appropriateness**: [Assessment]
- **Pattern Selection Logic**: [Assessment]
- **Context Transition Handling**: [Assessment]

### Usability Assessment
- **Learnability**: [Assessment]
- **Efficiency**: [Assessment]
- **Error Prevention/Recovery**: [Assessment]
- **User Satisfaction**: [Assessment]
```

## Meta-Systemic Principle Validation

### Parsimony in Agent System
- Assess canonical knowledge references instead of duplication
- Verify consistent knowledge organization
- Check for concept consolidation across contexts
- Evaluate knowledge reuse patterns

Example review findings:
```markdown
### Parsimony Assessment

**Strengths**:
- Strong use of canonical knowledge sources for meta-systemic principles
- Efficient representation of domain knowledge with minimal redundancy
- Effective concept linking between related knowledge areas

**Improvement Areas**:
- Some duplication in error handling guidance across different capabilities
- Opportunity to consolidate similar interaction patterns in the planning and review phases
- Knowledge references could be better organized in technical domains

**Recommendations**:
- Refactor error handling guidance into a shared module
- Create a canonical source for phase-specific interaction patterns
- Improve knowledge organization in technical domains
```

### Tensegrity in Agent System
- Evaluate balanced responsibilities between human and AI
- Check for reciprocal value in interactions
- Assess resilience of collaboration patterns
- Verify bidirectional knowledge transfer

Example review findings:
```markdown
### Tensegrity Assessment

**Strengths**:
- Well-balanced responsibilities between human and AI participants
- Strong support for human strategic decisions with AI analytical support
- Effective bidirectional knowledge transfer in technical domains

**Improvement Areas**:
- Some collaboration patterns lack resilience when context changes rapidly
- Occasional overreliance on human input for knowledge gap filling
- AI could be more proactive in offering complementary perspectives

**Recommendations**:
- Enhance collaboration resilience with clearer fallback mechanisms
- Implement more robust context detection for smoother transitions
- Develop more balanced insight generation in strategic discussions
```

### Modularity in Agent System
- Check for clear capability boundaries
- Assess interface clarity between capabilities
- Verify clean knowledge domain separation
- Evaluate independence of evolution

Example review findings:
```markdown
### Modularity Assessment

**Strengths**:
- Clear separation between knowledge domains with well-defined interfaces
- Capabilities have explicit boundaries and contracts
- Knowledge can evolve independently per domain
- Clean interfaces between human and AI responsibilities

**Improvement Areas**:
- Some capability boundaries blur in complex scenarios
- Cross-domain knowledge application could be more structured
- Interaction pattern modularity could be improved

**Recommendations**:
- Clarify capability boundaries in documentation
- Create explicit interfaces for cross-domain knowledge application
- Refactor interaction patterns for better modularity
```

### Coherence in Agent System
- Assess consistent interaction patterns
- Check pattern application across capabilities
- Verify terminology consistency
- Evaluate consistent behavior across contexts

Example review findings:
```markdown
### Coherence Assessment

**Strengths**:
- Consistent use of meta-systemic terminology
- Interaction patterns follow established conventions
- Similar capabilities use consistent implementation approaches
- Response formats maintain consistency across domains

**Improvement Areas**:
- Variable pattern application in edge case handling
- Some inconsistency in knowledge representation across domains
- Terminology drift in specialized technical areas

**Recommendations**:
- Standardize edge case handling patterns
- Align knowledge representation across domains
- Implement terminology governance for technical areas
```

### Clarity in Agent System
- Evaluate response clarity and comprehensibility
- Check for clear examples in guidance
- Assess explanation quality and depth
- Verify appropriate detail levels for context

Example review findings:
```markdown
### Clarity Assessment

**Strengths**:
- Excellent example quality across guidance materials
- Clear explanations with appropriate detail levels
- Well-structured responses with logical flow
- Effective use of visuals and formatting

**Improvement Areas**:
- Some technical explanations assume too much prior knowledge
- Complex scenarios could use more structured step-by-step guidance
- Occasional terminology overload in specialized domains

**Recommendations**:
- Add knowledge level detection to adapt explanation detail
- Enhance complex scenario guidance with clear step-by-step approaches
- Implement progressive disclosure for technical terminology
```

### Adaptivity in Agent System
- Check context-appropriate behavior
- Assess capability adaptation to different scenarios
- Verify preservation of core patterns while adapting
- Evaluate appropriate response variation

Example review findings:
```markdown
### Adaptivity Assessment

**Strengths**:
- Strong context detection with appropriate behavior adaptation
- Effective balance of consistency and contextual adaptation
- Good preservation of core patterns while varying implementation details
- Appropriate response variation based on user expertise

**Improvement Areas**:
- Occasional over-adaptation creating unnecessary variation
- Some context transitions could be smoother
- Core pattern preservation occasionally sacrificed for adaptation

**Recommendations**:
- Refine adaptation thresholds to prevent over-customization
- Implement smoother context transition mechanisms
- Strengthen core pattern preservation in adaptation processes
```

## Agent-Specific Review Protocols

### Scenario-Based Testing

Review using comprehensive scenario-based testing:

```markdown
## Scenario-Based Review Results

### Key Scenarios Tested
1. **[Scenario 1]**: [Description]
   - **Expected Behavior**: [Description]
   - **Actual Behavior**: [Description]
   - **Assessment**: ✅/⚠️/❌
   - **Observations**: [Details]

2. **[Scenario 2]**: [Description]
   - **Expected Behavior**: [Description]
   - **Actual Behavior**: [Description]
   - **Assessment**: ✅/⚠️/❌
   - **Observations**: [Details]

### Scenario Coverage Analysis
- **Well-Covered Areas**: [List areas]
- **Gap Areas**: [List areas]
- **Recommended Additional Scenarios**: [List recommended scenarios]
```

### Knowledge Accuracy Validation

Validate knowledge accuracy and application:

```markdown
## Knowledge Accuracy Validation

### Reference Validation
| Knowledge Domain | Reference Sources | Accuracy Assessment | Gaps Identified |
|------------------|-------------------|---------------------|-----------------|
| [Domain 1] | [Sources] | [Assessment] | [Gaps] |
| [Domain 2] | [Sources] | [Assessment] | [Gaps] |

### Application Validation
- **Correctly Applied Knowledge**: [Examples]
- **Misapplied Knowledge**: [Examples with corrections]
- **Knowledge Gap Handling**: [Assessment of how knowledge gaps are handled]
```

### Progressive Load Testing

Test capability under increasing complexity:

```markdown
## Progressive Load Testing

### Complexity Progression
| Complexity Level | Scenario | Performance | Observations |
|------------------|----------|-------------|--------------|
| Basic | [Scenario] | [Rating] | [Observations] |
| Intermediate | [Scenario] | [Rating] | [Observations] |
| Complex | [Scenario] | [Rating] | [Observations] |
| Edge Case | [Scenario] | [Rating] | [Observations] |

### Load Boundaries
- **Optimal Operating Range**: [Description]
- **Performance Degradation Point**: [Description]
- **Recovery Behavior**: [Description]
```

### Ethical and Bias Review

Assess for ethical considerations and biases:

```markdown
## Ethical and Bias Assessment

### Potential Bias Areas Evaluated
| Area | Methodology | Findings | Mitigations |
|------|-------------|----------|-------------|
| [Area 1] | [Method] | [Findings] | [Mitigations] |
| [Area 2] | [Method] | [Findings] | [Mitigations] |

### Ethical Considerations
- **Decision Support Guidance**: [Assessment]
- **Transparency Mechanisms**: [Assessment]
- **Accountability Structures**: [Assessment]
- **Potential Ethical Challenges**: [Assessment]
```

## Agent-Specific Go/No-Go Criteria

Define specific criteria for agent system approval:

```markdown
## Go/No-Go Decision Criteria

### Critical Criteria (All Required)
- [ ] All core capabilities meet acceptance criteria
- [ ] Knowledge domains demonstrate required accuracy
- [ ] Collaboration patterns function effectively
- [ ] No high-priority ethical concerns identified
- [ ] Security and privacy requirements satisfied

### Quality Criteria (Threshold Required)
| Category | Minimum Threshold | Actual Score | Status |
|----------|-------------------|--------------|--------|
| Capability Effectiveness | 90% | [Score] | ✅/⚠️/❌ |
| Knowledge Accuracy | 95% | [Score] | ✅/⚠️/❌ |
| Interaction Quality | 85% | [Score] | ✅/⚠️/❌ |
| Context Adaptation | 90% | [Score] | ✅/⚠️/❌ |

### Non-Blocking Issues
- Maximum of 3 low-priority issues permitted
- All identified issues must have documented remediation plans
- No issues affecting critical functionality
```

## Release Type-Specific Considerations

### Major Release Review (Agent System)
- Comprehensive review of all capabilities
- Full assessment of knowledge domains
- Complete evaluation of collaboration patterns
- Extended scenario-based testing
- Ethical review with external stakeholders

### Minor Release Review (Agent System)
- Focused review of new/changed capabilities
- Targeted assessment of affected knowledge domains
- Validation of modified collaboration patterns
- Scenario testing for new functionality
- Internal ethical review

### Patch Release Review (Agent System)
- Specific review of fixed issues
- Verification of knowledge corrections
- Regression testing for affected capabilities
- Limited scenario testing
- Focused ethical review if relevant

### Emergency Release Review (Agent System)
- Critical issue verification only
- Basic regression testing
- Essential capability validation
- Expedited review process
- Post-deployment comprehensive review

## Review Outcome Documentation

Document the review outcomes comprehensively:

```markdown
## Review Outcome Summary

### Overall Assessment
- **Status**: [Approved/Conditionally Approved/Not Approved]
- **Summary Finding**: [Brief assessment]
- **Key Strengths**: [List of strengths]
- **Critical Issues**: [List of issues]

### Principle Application Assessment
- **Parsimony**: [Strong/Adequate/Needs Improvement]
- **Tensegrity**: [Strong/Adequate/Needs Improvement]
- **Modularity**: [Strong/Adequate/Needs Improvement]
- **Coherence**: [Strong/Adequate/Needs Improvement]
- **Clarity**: [Strong/Adequate/Needs Improvement]
- **Adaptivity**: [Strong/Adequate/Needs Improvement]

### Action Items
| Item | Priority | Owner | Due Date | Resolution Criteria |
|------|----------|-------|----------|---------------------|
| [Item 1] | [Priority] | [Owner] | [Date] | [Criteria] |
| [Item 2] | [Priority] | [Owner] | [Date] | [Criteria] |

### Deployment Decision
- **Decision**: [Proceed/Delay/Redesign]
- **Conditions**: [Any conditions for deployment]
- **Special Instructions**: [Any special deployment instructions]
- **Verification Requirements**: [Post-deployment verification needed]
```

## Human-AI Collaboration in Review

In our two-person team:

### Human Team Member Focus
- Make final go/no-go decisions
- Evaluate subjective quality aspects
- Assess ethical considerations
- Validate contextual appropriateness
- Identify potential blindspots

### AI Agent Focus
- Provide structured evaluation against criteria
- Generate comprehensive scenario testing
- Document review findings systematically
- Track principle application throughout review
- Identify pattern inconsistencies or gaps

<important>
The pre-release review phase for agent systems is critical to ensure that capabilities function as intended, knowledge is accurate, and collaboration patterns are effective. A thorough review ensures that the agent enhancement provides the intended value while maintaining system integrity.
</important>