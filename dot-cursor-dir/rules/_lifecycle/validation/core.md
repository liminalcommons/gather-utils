---
description: 
globs: **/validation/*.md,**/validation/*.mdx,**/releases/*/validation.md,**/releases/*/validation.mdx
alwaysApply: false
---
---
description: "Core guidance for the validation phase of the release lifecycle"
globs: "**/validation/*.md,**/validation/*.mdx,**/releases/*/validation.md,**/releases/*/validation.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Validation Phase Guidance

<critical>
The validation phase ensures that the release meets all requirements and maintains system integrity. During this phase, verify functional and non-functional requirements, assess meta-systemic principle application, and identify any issues before proceeding to deployment.
</critical>

## Core Validation Activities

The validation phase consists of these essential activities:

1. **Requirements Verification**: Confirm all functional and non-functional requirements are met
2. **Quality Assessment**: Validate code quality, performance, security, and usability
3. **Principle Validation**: Verify proper application of meta-systemic principles
4. **Issue Identification**: Document and classify any identified issues
5. **Release Readiness**: Determine if the release is ready to proceed to deployment

## Required Metadata

Every validation report document must include:

```yaml
---
title: "[Release Name] Validation Report"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date]"
last_updated: "[Last Update Date]"
system_context: "[Code|Release|Agent]"
owner: "[Validation Owner]"
status: "[Draft|In Progress|Completed]"
related_plan: "[Link to Release Plan Document]"
---
```

## Validation Approach

Structure your validation activities as follows:

### 1. Validation Planning
Before beginning validation, establish a clear plan:

```markdown
## Validation Plan

### Scope and Objectives
- **Validation Scope**: [Define what is included in validation]
- **Primary Objectives**: [Key validation goals]
- **Success Criteria**: [Definition of successful validation]

### Validation Approach
- **Methodology**: [Overall approach to validation]
- **Environments**: [Where validation will occur]
- **Tools and Resources**: [Required validation tools]

### Validation Schedule
- **Timeline**: [Start and end dates]
- **Key Milestones**: [Major validation checkpoints]
- **Dependencies**: [Prerequisites for validation]

### Validation Team
- **Roles and Responsibilities**: [Who performs what validation]
- **Communication Plan**: [How validation status will be communicated]
- **Escalation Path**: [How to handle blocking issues]
```

### 2. Requirements Validation

Verify all functional and non-functional requirements:

```markdown
## Requirements Validation

### Functional Requirements

| Requirement | Description | Validation Method | Result | Evidence |
|-------------|-------------|-------------------|--------|----------|
| [REQ-001] | [Description] | [Method] | ✅/⚠️/❌ | [Link/Reference] |
| [REQ-002] | [Description] | [Method] | ✅/⚠️/❌ | [Link/Reference] |

### Non-Functional Requirements

| Requirement | Description | Validation Method | Result | Evidence |
|-------------|-------------|-------------------|--------|----------|
| [NFR-001] | [Description] | [Method] | ✅/⚠️/❌ | [Link/Reference] |
| [NFR-002] | [Description] | [Method] | [Method] | ✅/⚠️/❌ | [Link/Reference] |

### Validation Methods
- **Automated Testing**: [Extent and coverage of automated tests]
- **Manual Testing**: [Approach to manual validation]
- **Performance Testing**: [Performance validation methodology]
- **Security Assessment**: [Security validation approach]
- **User Acceptance Testing**: [UAT approach]
```

### 3. Quality Assessment

Assess the overall quality of the release:

```markdown
## Quality Assessment

### Code Quality

| Metric | Target | Actual | Result |
|--------|--------|--------|--------|
| Test Coverage | [Target] | [Actual] | ✅/⚠️/❌ |
| Code Complexity | [Target] | [Actual] | ✅/⚠️/❌ |
| Duplication | [Target] | [Actual] | ✅/⚠️/❌ |
| Documentation | [Target] | [Actual] | ✅/⚠️/❌ |

### Performance Assessment

| Metric | Baseline | Target | Actual | Result |
|--------|----------|--------|--------|--------|
| [Metric 1] | [Baseline] | [Target] | [Actual] | ✅/⚠️/❌ |
| [Metric 2] | [Baseline] | [Target] | [Actual] | ✅/⚠️/❌ |

### Security Assessment

| Category | Assessment | Issues | Remediation |
|----------|------------|--------|-------------|
| Authentication | ✅/⚠️/❌ | [Issues] | [Remediation] |
| Authorization | ✅/⚠️/❌ | [Issues] | [Remediation] |
| Data Protection | ✅/⚠️/❌ | [Issues] | [Remediation] |
| Secure Communications | ✅/⚠️/❌ | [Issues] | [Remediation] |

### Usability Assessment

| Aspect | Assessment | Feedback | Improvements |
|--------|------------|----------|--------------|
| [Aspect 1] | ✅/⚠️/❌ | [Feedback] | [Improvements] |
| [Aspect 2] | ✅/⚠️/❌ | [Feedback] | [Improvements] |
```

### 4. Meta-Systemic Principle Validation

Verify proper application of meta-systemic principles:

```markdown
## Meta-Systemic Validation

### Principle Assessment

| Principle | Assessment | Strengths | Areas for Improvement |
|-----------|------------|-----------|------------------------|
| Parsimony | ✅/⚠️/❌ | [Strengths] | [Improvements] |
| Tensegrity | ✅/⚠️/❌ | [Strengths] | [Improvements] |
| Modularity | ✅/⚠️/❌ | [Strengths] | [Improvements] |
| Coherence | ✅/⚠️/❌ | [Strengths] | [Improvements] |
| Clarity | ✅/⚠️/❌ | [Strengths] | [Improvements] |
| Adaptivity | ✅/⚠️/❌ | [Strengths] | [Improvements] |

### Principle Tension Analysis

| Tension | Resolution Approach | Assessment |
|---------|---------------------|------------|
| [Principle 1] vs [Principle 2] | [Approach] | ✅/⚠️/❌ |
| [Principle 3] vs [Principle 4] | [Approach] | ✅/⚠️/❌ |
```

### 5. Issue Management

Document and classify all identified issues:

```markdown
## Issue Management

### Issue Summary

| Severity | Count | Description |
|----------|-------|-------------|
| Critical | [Count] | Issues that block release |
| High | [Count] | Significant issues requiring resolution |
| Medium | [Count] | Important issues that should be addressed |
| Low | [Count] | Minor issues that could be deferred |

### Critical and High Issues

| ID | Description | Severity | Component | Impact | Resolution Plan |
|----|-------------|----------|-----------|--------|-----------------|
| [ID] | [Description] | [Severity] | [Component] | [Impact] | [Plan] |
| [ID] | [Description] | [Severity] | [Component] | [Impact] | [Plan] |

### Issue Resolution Strategy
- **Critical Issues**: [Approach to resolving critical issues]
- **High Issues**: [Approach to resolving high issues]
- **Medium Issues**: [Approach to resolving medium issues]
- **Low Issues**: [Approach to handling low issues]
```

### 6. Release Readiness Assessment

Determine overall readiness for deployment:

```markdown
## Release Readiness Assessment

### Go/No-Go Criteria

| Criterion | Status | Evidence | Notes |
|-----------|--------|----------|-------|
| All critical issues resolved | ✅/❌ | [Evidence] | [Notes] |
| All high issues resolved or mitigated | ✅/❌ | [Evidence] | [Notes] |
| Requirements validation complete | ✅/❌ | [Evidence] | [Notes] |
| Performance criteria met | ✅/❌ | [Evidence] | [Notes] |
| Security assessment complete | ✅/❌ | [Evidence] | [Notes] |
| Stakeholder approval received | ✅/❌ | [Evidence] | [Notes] |

### Overall Assessment
- **Status**: [Ready/Not Ready/Conditionally Ready]
- **Justification**: [Explanation of readiness status]
- **Conditions**: [If conditionally ready, list conditions]
- **Recommendations**: [Specific recommendations for proceeding]
```

## Meta-Systemic Principle Application

### Parsimony
- Reference existing requirements rather than duplicating them
- Link to test results instead of duplicating content
- Maintain a single source of truth for validation status
- Reuse validation criteria across similar components

Example:
```markdown
## Functional Requirements Validation

This validation verifies the requirements defined in the [Release 2.3.0 Definition](mdc:../definition/release-2.3.0-definition.md). See the [Automated Test Results](mdc:../results/automated-tests.md) for detailed test execution evidence.
```

### Tensegrity
- Establish clear relationships between requirements and validation methods
- Connect validation findings to development activities
- Link validation results with deployment prerequisites
- Create bidirectional traceability between components and tests

Example:
```markdown
## Requirement-Test Traceability

| Requirement | Test Cases | Validation Method | Component | Status |
|-------------|------------|-------------------|-----------|--------|
| REQ-001 | TC-001, TC-002 | Automated | Auth Service | ✅ Passed |
| REQ-002 | TC-003 | Manual | Admin UI | ✅ Passed |
| REQ-003 | TC-004, TC-005 | Performance | Search Engine | ⚠️ Partial |
```

### Modularity
- Separate validation of different components
- Create clear boundaries between validation types
- Structure validation reports with distinct sections
- Enable independent validation of different aspects

Example:
```markdown
## Validation Structure

The validation is organized into independent modules that can be conducted and reviewed separately:

1. **Functional Validation**: Verifies feature functionality
2. **Performance Validation**: Assesses system performance
3. **Security Validation**: Evaluates security controls
4. **Usability Validation**: Assesses user experience
5. **Meta-Systemic Validation**: Verifies principle application
```

### Coherence
- Apply consistent validation methods across the system
- Use standard assessment criteria
- Follow established validation patterns
- Maintain terminology consistency

Example:
```markdown
All components are validated using our standard validation framework with consistent terminology, metrics, and evaluation criteria. This ensures comparability across different parts of the system and enables trend analysis across releases.
```

### Clarity
- Document validation methods explicitly
- Provide clear evidence for all assessments
- Use concrete examples of issues and successes
- Create visual summaries for complex validation results

Example:
```markdown
## Performance Testing Example

**Test Scenario**: Search query with complex filters

**Method**: 
1. Execute 1,000 search queries with randomly generated complex filters
2. Measure response time at 95th percentile
3. Compare with baseline and target metrics

**Results**:
- Baseline: 250ms (P95)
- Target: 200ms (P95)
- Actual: 185ms (P95)

**Visual Evidence**:
![Performance Test Results](mdc:../images/perf-test-results.png)
```

### Adaptivity
- Scale validation effort based on risk and criticality
- Adjust validation intensity to release scope
- Apply context-appropriate validation methods
- Tailor validation reports to audience needs

Example:
```markdown
## Adaptive Validation Approach

This validation applies risk-based testing:

- **High-Risk Components**: Comprehensive validation including manual, automated, and exploratory testing
- **Medium-Risk Components**: Standard validation with automated tests and targeted manual validation
- **Low-Risk Components**: Basic validation with automated testing only

The validation intensity is adjusted based on:
- Component criticality
- Change complexity
- Historical defect patterns
- Release scope (Major/Minor/Patch/Emergency)
```

## Context-Specific Validation Approaches

### For Code System Validation
- Focus on technical functionality and quality
- Verify interfaces and integration points
- Validate non-functional requirements
- Assess code quality metrics
- Verify security controls

### For Release System Validation
- Focus on process compliance and effectiveness
- Verify artifact quality and completeness
- Validate meta-process metrics
- Assess rule application consistency
- Verify process adaptation appropriateness

### For Agent System Validation
- Focus on capability accuracy and effectiveness
- Verify knowledge application correctness
- Validate interaction pattern effectiveness
- Assess guidance quality
- Verify context-sensitive behavior

## Release Scope-Specific Validation Requirements

### Major Release Validation
- Comprehensive validation of all requirements
- Full regression testing
- Complete security assessment
- Thorough performance validation
- Extensive meta-systemic principle validation
- Formal stakeholder acceptance

### Minor Release Validation
- Focused validation of new and changed features
- Targeted regression testing
- Security assessment of affected areas
- Performance validation for changed components
- Meta-systemic principle validation for key aspects
- Stakeholder acceptance of new features

### Patch Release Validation
- Specific validation of fixed issues
- Limited regression testing of affected areas
- Focused security validation if relevant
- Performance validation only if performance-related
- Limited meta-systemic principle validation
- Minimal stakeholder notification

### Emergency Release Validation
- Critical path validation only
- Essential security validation
- Focused regression testing
- Performance validation only if critical
- Minimal principle validation
- Expedited stakeholder approval

## Validation Phase Quality Checklist

Before concluding the validation phase, verify that:

- [ ] All requirements have been validated
- [ ] All critical and high issues have been addressed
- [ ] Security assessment is complete
- [ ] Performance validation meets targets
- [ ] Meta-systemic principles have been validated
- [ ] Regression testing is complete
- [ ] Documentation is updated and accurate
- [ ] Validation report is comprehensive and clear
- [ ] Stakeholder acceptance has been obtained
- [ ] Go/No-Go decision is documented with rationale

## Human-AI Collaboration in Validation

In our two-person team:

### Human Team Member Focus
- Making judgments on subjective quality aspects
- Assessing overall release readiness
- Evaluating principle application effectiveness
- Providing domain expertise for validation
- Making final go/no-go decisions

### AI Agent Focus
- Comprehensive requirements traceability
- Systematic verification of principle application
- Generating comprehensive validation reports
- Identifying potential issues and patterns
- Ensuring validation completeness

<important>
The validation phase is critical for ensuring release quality and readiness. A thorough, systematic approach to validation identifies issues early, confirms requirements are met, and ensures meta-systemic principles are applied effectively throughout the release.
</important>