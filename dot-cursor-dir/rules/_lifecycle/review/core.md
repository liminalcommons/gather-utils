---
description: USE WHEN conducting final release evaluations: Guide the pre-release review process to ensure complete validation, stakeholder alignment, and proper go/no-go decision making before deployment.
globs: 
alwaysApply: false
---
---
description: "Core guidance for the pre-release review phase of the release lifecycle"
globs: "**/review/*.md,**/review/*.mdx,**/releases/*/review.md,**/releases/*/review.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Pre-Release Review Guidance

<critical>
The pre-release review phase is a critical quality gate that determines if a release is ready for deployment. This phase ensures that all requirements have been met, quality standards are satisfied, and stakeholders approve the release.
</critical>

## Core Review Activities

The pre-release review phase consists of these essential activities:

1. **Readiness Assessment**: Evaluate if the release is ready for deployment
2. **Validation Verification**: Ensure all validation has been completed successfully
3. **Risk Evaluation**: Assess remaining risks and mitigation strategies
4. **Stakeholder Approval**: Obtain necessary approvals for deployment
5. **Go/No-Go Decision**: Make a formal decision to proceed with or delay deployment

## Required Metadata

Every pre-release review document must include:

```yaml
---
title: "[Release Name] Pre-Release Review"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date]"
last_updated: "[Last Update Date]"
system_context: "[Code|Release|Agent]"
owner: "[Review Owner]"
status: "[Draft|In Progress|Completed]"
related_validation: "[Link to Validation Report]"
---
```

## Review Approach

Structure your review activities as follows:

### 1. Release Readiness Assessment

Comprehensively evaluate release readiness:

```markdown
## Release Readiness Assessment

### Objectives Achievement
| Objective | Success Criteria | Result | Evidence | Assessment |
|-----------|-----------------|--------|----------|------------|
| [Objective 1] | [Criteria] | [Result] | [Evidence] | ✅/⚠️/❌ |
| [Objective 2] | [Criteria] | [Result] | [Evidence] | ✅/⚠️/❌ |

### Requirements Completion
| Category | Total Requirements | Completed | Deferred | Failed | Completion Rate |
|----------|-------------------|-----------|----------|--------|----------------|
| Functional | [Count] | [Count] | [Count] | [Count] | [Percentage] |
| Non-Functional | [Count] | [Count] | [Count] | [Count] | [Percentage] |
| Security | [Count] | [Count] | [Count] | [Count] | [Percentage] |
| Compliance | [Count] | [Count] | [Count] | [Count] | [Percentage] |

### Quality Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| [Metric 1] | [Target] | [Actual] | ✅/⚠️/❌ |
| [Metric 2] | [Target] | [Actual] | ✅/⚠️/❌ |

### Open Issues
| Severity | Count | Description | Impact on Release |
|----------|-------|-------------|-------------------|
| Critical | [Count] | [Description] | [Impact] |
| High | [Count] | [Description] | [Impact] |
| Medium | [Count] | [Description] | [Impact] |
| Low | [Count] | [Description] | [Impact] |

### Overall Readiness
- **Requirements Status**: ✅/⚠️/❌
- **Quality Status**: ✅/⚠️/❌
- **Risk Status**: ✅/⚠️/❌
- **Overall Assessment**: ✅/⚠️/❌
```

### 2. Validation Completeness Verification

Verify all validation activities have been completed:

```markdown
## Validation Completeness

### Validation Activity Summary
| Validation Activity | Status | Findings | Resolution | Sign-off |
|---------------------|--------|----------|------------|----------|
| [Activity 1] | Complete/Partial/Not Started | [Key Findings] | [Resolution] | [Who] |
| [Activity 2] | Complete/Partial/Not Started | [Key Findings] | [Resolution] | [Who] |

### Test Coverage Analysis
- **Functional Coverage**: [Percentage] coverage of functional requirements
- **Non-Functional Coverage**: [Percentage] coverage of non-functional requirements
- **Regression Coverage**: [Percentage] coverage of regression test cases
- **Coverage Gaps**: [Description of any significant coverage gaps]

### Performance Validation
- **Performance Testing Completed**: Yes/No/Partial
- **Performance Criteria Met**: All/Most/Some/None
- **Performance Issues**: [Description of any performance issues]
- **Performance Resolution**: [How performance issues were resolved]

### Security Validation
- **Security Testing Completed**: Yes/No/Partial
- **Security Requirements Met**: All/Most/Some/None
- **Security Issues**: [Description of any security issues]
- **Security Resolution**: [How security issues were resolved]

### Meta-Systemic Validation
- **Principle Application Validated**: Yes/No/Partial
- **Principle Compliance**: [Assessment of principle application]
- **Meta-Systemic Issues**: [Description of any meta-systemic issues]
- **Issue Resolution**: [How meta-systemic issues were resolved]
```

### 3. Risk Assessment and Mitigation

Evaluate remaining risks and mitigation strategies:

```markdown
## Risk Assessment

### Residual Risks
| Risk | Description | Likelihood | Impact | Risk Level | Mitigation | Owner |
|------|-------------|------------|--------|------------|------------|-------|
| [Risk 1] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |
| [Risk 2] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |

### Deployment Risks
| Risk | Description | Likelihood | Impact | Risk Level | Mitigation | Owner |
|------|-------------|------------|--------|------------|------------|-------|
| [Risk 1] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |
| [Risk 2] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |

### Post-Deployment Risks
| Risk | Description | Likelihood | Impact | Risk Level | Mitigation | Owner |
|------|-------------|------------|--------|------------|------------|-------|
| [Risk 1] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |
| [Risk 2] | [Description] | H/M/L | H/M/L | H/M/L | [Mitigation] | [Owner] |

### Risk Acceptance
| Risk | Rationale for Acceptance | Approved By |
|------|--------------------------|-------------|
| [Risk 1] | [Rationale] | [Approver] |
| [Risk 2] | [Rationale] | [Approver] |

### Contingency Planning
- **Rollback Plan**: [Summary of rollback approach]
- **Emergency Response**: [How critical issues will be handled]
- **Communication Plan**: [How issues will be communicated]
- **Support Readiness**: [Support plan for post-deployment issues]
```

### 4. Stakeholder Review and Approval

Document stakeholder reviews and approvals:

```markdown
## Stakeholder Review

### Stakeholder Feedback
| Stakeholder | Role | Feedback | Resolution | Approval Status |
|-------------|------|----------|------------|-----------------|
| [Name] | [Role] | [Feedback] | [Resolution] | Approved/Pending/Rejected |
| [Name] | [Role] | [Feedback] | [Resolution] | Approved/Pending/Rejected |

### Approval Requirements
| Approval | Required For | Status | Approver | Date |
|----------|--------------|--------|----------|------|
| [Approval 1] | [Requirement] | Granted/Pending/Rejected | [Name] | [Date] |
| [Approval 2] | [Requirement] | Granted/Pending/Rejected | [Name] | [Date] |

### Stakeholder Concerns
| Concern | Raised By | Resolution | Status |
|---------|-----------|------------|--------|
| [Concern 1] | [Stakeholder] | [Resolution] | Resolved/Open |
| [Concern 2] | [Stakeholder] | [Resolution] | Resolved/Open |

### External Dependencies
| Dependency | Status | Contact | Notes |
|------------|--------|---------|-------|
| [Dependency 1] | Ready/Not Ready | [Contact] | [Notes] |
| [Dependency 2] | Ready/Not Ready | [Contact] | [Notes] |
```

### 5. Deployment Readiness

Verify deployment preparations are complete:

```markdown
## Deployment Readiness

### Deployment Plan Status
- **Deployment Plan**: Complete/Incomplete
- **Deployment Timeline**: Defined/Undefined
- **Resource Availability**: Confirmed/Unconfirmed
- **Dependencies**: Ready/Not Ready

### Environment Readiness
| Environment | Status | Issues | Resolution |
|-------------|--------|--------|------------|
| [Environment 1] | Ready/Not Ready | [Issues] | [Resolution] |
| [Environment 2] | Ready/Not Ready | [Issues] | [Resolution] |

### Documentation Readiness
| Documentation | Status | Responsible | Notes |
|---------------|--------|-------------|-------|
| User Documentation | Complete/Incomplete | [Owner] | [Notes] |
| Release Notes | Complete/Incomplete | [Owner] | [Notes] |
| Support Documentation | Complete/Incomplete | [Owner] | [Notes] |
| Training Materials | Complete/Incomplete | [Owner] | [Notes] |

### Operational Readiness
- **Monitoring Plan**: Ready/Not Ready
- **Support Plan**: Ready/Not Ready
- **Escalation Procedures**: Defined/Undefined
- **Rollback Procedures**: Tested/Untested
```

### 6. Go/No-Go Decision

Make and document the final release decision:

```markdown
## Go/No-Go Decision

### Decision Criteria
| Criterion | Threshold | Status | Assessment |
|-----------|-----------|--------|------------|
| [Criterion 1] | [Threshold] | [Status] | Go/No-Go |
| [Criterion 2] | [Threshold] | [Status] | Go/No-Go |
| [Criterion 3] | [Threshold] | [Status] | Go/No-Go |

### Decision Summary
- **Decision**: Go/No-Go/Conditional Go
- **Decision Date**: [Date]
- **Decision Maker**: [Name/Role]
- **Decision Rationale**: [Explanation for the decision]

### Conditions (if applicable)
| Condition | Resolution Required By | Owner | Status |
|-----------|------------------------|-------|--------|
| [Condition 1] | [Date/Milestone] | [Owner] | Open/Resolved | [Date/Milestone] | [Owner] | Open/Resolved |

###o**: [Steps to proceed with deployment]
- **If No issues before re-review]
- **If Conditional Go**: [Steps to resolve conditions]
```

## Meta-Systemic Principle Application

### Parsimony
- Reference existing artifacts rather than duplicating them
- Focus review on unique insights rather than repeating validation
- Maintain consistent assessment approaches across reviews
- Link to detailed evidence rather than duplicating it

Example:
```markdown
This review is based on the comprehensive validation findings documented in the [Validation Report](mdc:../validation/validation-report.md) and focuses on readiness assessment rather than repeating validation details.

For complete test results, see the [Test Execution Report](mdc:../testing/test-execution-report.md).
```

### Tensegrity
- Connect review findings to specific validation activities
- Link readiness assessment to deployment prerequisites
- Establish clear relationships between risks and mitigations
- Create balanced responsibility for addressing findings

Example:
```markdown
## Risk-Mitigation Traceability

| Risk | Source Validation | Mitigation | Mitigation Validation | Owner |
|------|-------------------|------------|------------------------|-------|
| Performance degradation under high load | Performance testing | Implemented caching layer | Cache hit rate >90% verified | Performance Team |
| Security vulnerability in authentication | Security assessment | Implemented additional verification | Penetration testing verified fix | Security Team |
```

### Modularity
- Organize review by distinct aspects of readiness
- Separate functional, quality, and risk assessments
- Create clear boundaries between evaluation areas
- Enable independent assessment of different criteria

Example:
```markdown
## Review Structure

This review is organized into independent modules that can be assessed separately:

1. **Functional Completeness**: Verification that requirements are met
2. **Quality Assessment**: Evaluation against quality standards
3. **Risk Evaluation**: Assessment of remaining risks
4. **Operational Readiness**: Verification of deployment preparations

Each section can be reviewed independently while the Go/No-Go decision considers all aspects together.
```

### Coherence
- Apply consistent assessment criteria across the review
- Use standard metrics and evaluation approaches
- Follow established decision-making frameworks
- Maintain coherent structure across reviews

Example:
```markdown
This review follows our standard assessment framework with consistent criteria application. We use the same evaluation framework applied to previousing direct comparison of readiness levels and trend analysis.
```

### Clarity
- Provide explicit assessment of each readiness aspect
- Include concrete evidence for all evaluations
- Use visual indicators for status clarity
- Explain decision criteria and rationale clearly

Example:
```markdown
## Security Assessment Findings

The security assessment revealed three significant findings:

1. **Authentication Token Exposure** ⚠️
   - **Finding**: Authentication tokens were transmitted in URL parameters
   - **Impact**: Potential token theft through browser history or server logs
   - **Resolution**: Moved token transmission to secure headers
   - **Verification**: Penetration testing confirmed the vulnerability is resolved
   - **Status**: ✅ RESOLVED

2. **Insufficient Password Controls** ⚠️
   - **Finding**: Password policy did not enforce sufficient complexity
   - **Impact**: Increased risk of credential compromise
   - **Resolution**: Implemented enhanced password policy
   - **Verification**: Policy enforcement verified in all authentication paths
   - **Status**: ✅ RESOLVED

3. **Session Timeout Configuration** ⚠️
   - **Finding**: Session timeout was set to 24 hours
   - **Impact**: Extended window of opportunity if session is compromised
   - **Resolution**: Reduced timeout to 4 hours with sliding expiration
   - **Verification**: Timeout behavior verified in all user interfaces
   - **Status**: ✅ RESOLVED
```

### Adaptivity
- Scale review depth to release complexity and risk
- Adapt decision criteria to release context
- Apply appropriate level of formality based on release type
- Adjust stakeholder involvement based on impact

Example:
```markdown
## Adaptive Review Approach

This review applies a context-sensitive approach based on:
- Release classification (Minor)
- Risk assessment (Medium)
- Complexity (Moderate)
- Business impact (Significant)

Based on these factors, we applied:
- Standard functional validation for all components
- In-depth performance validation for the search functionality
- Focused security assessment on authentication changes
- Targeted stakeholder reviews from the most affected teams
```

## Context-Specific Review Approaches

### For Code System Reviews
- Focus on technical readiness and quality
- Verify feature completeness and correctness
- Assess performance and security considerations
- Evaluate technical documentation completeness
- Verify operational readiness and monitoring

### For Release System Reviews
- Focus on process compliance and effectiveness
- Verify artifact completeness and quality
- Assess meta-process effectiveness
- Evaluate documentation and training materials
- Verify organizational readiness for process changes

### For Agent System Reviews
- Focus on capability effectiveness and safety
- Verify knowledge accuracy and completeness
- Assess interaction quality and user experience
- Evaluate documentation of capabilities and limitations
- Verify integration with human workflows

## Release Scope-Specific Review Requirements

### Major Release Review
- Comprehensive review of all readiness aspects
- Formal stakeholder approval process
- Detailed risk assessment and mitigation
- Complete documentation verification
- Formal go/no-go decision meeting

### Minor Release Review
- Focused review on changed components
- Standard stakeholder approval process
- Targeted risk assessment
- Verification of updated documentation
- Standard go/no-go decision process

### Patch Release Review
- Minimal review focused on specific fixes
- Limited stakeholder notification
- Risk assessment for affected areas only
- Verification of release notes
- Streamlined go/no-go decision

### Emergency Release Review
- Critical path verification only
- Expedited approval process
- Focused risk assessment
- Essential documentation only
- Accelerated go/no-go decision

## Pre-Release Review Checklist

Before concluding the pre-release review phase, verify that:

- [ ] All release objectives have been evaluated
- [ ] All validation activities have been completed
- [ ] Quality metrics have been assessed against targets
- [ ] Remaining issues have been documented and classified
- [ ] Risks have been identified with appropriate mitigations
- [ ] Stakeholder reviews and approvals have been obtained
- [ ] Deployment preparations have been verified
- [ ] Go/no-go decision has been made and documented
- [ ] Next steps have been clearly defined
- [ ] Review documentation is complete and accurate

## Human-AI Collaboration in Pre-Release Review

In our two-person team:

### Human Team Member Focus
- Making final readiness assessments
- Evaluating subjective quality aspects
- Assessing business and organizational impact
- Making go/no-go decisions
- Communicating with stakeholders
- Evaluating risk acceptance

### AI Agent Focus
- Conducting comprehensive readiness analysis
- Tracking validation completeness
- Documenting issues and resolutions
- Generating consistent review documentation
- Identifying potential gaps or inconsistencies
- Ensuring review thoroughness and consistency

<important>
The pre-release review is the final quality gate before deployment. A thorough and objective assessment is essential to ensure the release is truly ready for deployment, protecting both users and the organization from preventable issues.
</important>