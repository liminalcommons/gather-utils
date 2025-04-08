---
description: 
globs: **/code/review/*.md,**/code/review/*.mdx,**/releases/*/code_review.md,**/releases/*/code_review.mdx
alwaysApply: false
---
---
description: "Code-specific guidance for the pre-release review phase of the release lifecycle"
globs: "**/code/review/*.md,**/code/review/*.mdx,**/releases/*/code_review.md,**/releases/*/code_review.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code System Pre-Release Review Guidance

<critical>
This rule provides specialized guidance for the pre-release review phase when the primary system context is code-based system development. Apply these guidelines in conjunction with the core pre-release review rules to ensure code-specific quality assessment before deployment.
</critical>

## Code System Review Purpose

The pre-release review for code systems serves to:

1. Verify that all code-specific requirements have been implemented correctly
2. Confirm that quality standards have been met across all components
3. Ensure the implementation maintains technical integrity and architectural alignment
4. Validate that all technical risks have been identified and mitigated
5. Make an informed go/no-go decision for deployment based on technical evidence

## Code-Specific Review Components

When conducting pre-release review for code systems, include these specialized components:

### 1. Code Quality Assessment

Comprehensive assessment of code quality metrics:

```markdown
## Code Quality Assessment

### Quality Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Test Coverage | >85% | 87% | ✅ Pass |
| Code Duplication | <3% | 2.1% | ✅ Pass |
| Cyclomatic Complexity | <15 | 12 avg | ✅ Pass |
| Technical Debt Ratio | <5% | 4.2% | ✅ Pass |
| Security Scan | 0 Critical/High | 0 | ✅ Pass |
| Performance Benchmarks | Within 5% of baseline | +2% | ✅ Pass |

### Static Analysis Results
- **Linting**: All files pass linting standards
- **Code Style**: Complies with project style guide
- **Type Safety**: All type errors resolved
- **Deprecated APIs**: No usage of deprecated APIs

### Technical Debt Assessment
- **New Technical Debt**: [Document any new technical debt introduced]
- **Technical Debt Reduction**: [Document any technical debt paid down]
- **Technical Debt Ratio**: Current ratio compared to previous release
```

### 2. Architecture Compliance Review

Assessment of architectural alignment and integrity:

```markdown
## Architecture Compliance Review

### Architecture Alignment
- **Component Boundaries**: Implementation adheres to defined component boundaries
- **Interface Contracts**: All interfaces implement specified contracts
- **Dependency Management**: Dependencies align with architectural guidelines
- **Design Patterns**: Implementation follows approved design patterns

### Architecture Decisions
| Decision | Implementation Assessment | Evidence |
|----------|---------------------------|----------|
| [ADR-001: Authentication Approach] | Correctly implemented with JWT | [Link to implementation review] |
| [ADR-002: Database Schema Design] | Schema follows decision with minor variations | [Link to schema review] |
| [ADR-003: API Structure] | Fully compliant | [Link to API review] |

### Technical Standards Compliance
- **API Standards**: API endpoints follow RESTful standards
- **Security Standards**: Implementation meets security requirements
- **Performance Standards**: Meets performance criteria
- **Accessibility Standards**: Meets accessibility requirements
```

### 3. Technical Risk Assessment

Review of technical risks and mitigations:

```markdown
## Technical Risk Assessment

### Identified Technical Risks
| Risk | Impact | Likelihood | Mitigation | Status |
|------|--------|------------|------------|--------|
| [Risk 1: Database scaling under peak load] | High | Medium | Implemented connection pooling and caching | ✅ Mitigated |
| [Risk 2: API rate limiting for external users] | Medium | High | Implemented token bucket algorithm | ✅ Mitigated |
| [Risk 3: Browser compatibility] | Medium | Medium | Tested on target browsers, documented limitations | ✅ Mitigated |

### Security Risk Assessment
- **Vulnerability Scan Results**: [Summary of security scan findings]
- **Penetration Test Results**: [Summary of penetration testing]
- **Security Review Signoff**: [Security team assessment]
- **Data Protection Assessment**: [Privacy and data protection review]

### Operational Risk Assessment
- **Deployment Risk**: Assessment of deployment complexity and rollback capability
- **Monitoring Readiness**: Confirmation of monitoring capabilities
- **Support Readiness**: Assessment of support documentation and training
- **Scalability Assessment**: Evaluation of scale testing results
```

### 4. Technical Verification Demonstration

Live demonstration of key technical components:

```markdown
## Technical Verification Demonstration

### Demonstration Scenarios
| Scenario | Participants | Focus Areas | Result |
|----------|--------------|-------------|--------|
| Core Functionality | Product Team, Engineering | Feature completeness, user flows | ✅ Verified |
| Performance Under Load | Platform Team | Response times, resource utilization | ✅ Verified |
| Error Handling | QA Team, Support | Edge cases, recovery mechanisms | ✅ Verified |
| Security Controls | Security Team | Access controls, data protection | ✅ Verified |

### Demonstration Environment
- **Environment**: [Staging/Pre-Production]
- **Data Set**: [Description of test data]
- **Configuration**: [Specific configuration settings]
- **Access**: [How stakeholders accessed the demonstration]

### Stakeholder Feedback
- **Technical Feedback**: [Summary of technical feedback]
- **Functional Feedback**: [Summary of functional feedback]
- **Usability Feedback**: [Summary of usability feedback]
- **Overall Assessment**: [Stakeholder consensus]
```

### 5. Technical Documentation Review

Assessment of technical documentation completeness:

```markdown
## Technical Documentation Review

### Documentation Completeness
| Documentation Type | Status | Reviewer | Notes |
|-------------------|--------|----------|-------|
| API Documentation | ✅ Complete | [Name] | All endpoints documented with examples |
| Architecture Documentation | ✅ Complete | [Name] | Component diagrams updated |
| Deployment Documentation | ✅ Complete | [Name] | Includes rollback procedures |
| Operational Documentation | ⚠️ Partial | [Name] | Monitoring docs need enhancement |

### Documentation Quality Assessment
- **Accuracy**: Documentation accurately reflects implementation
- **Clarity**: Documentation is clear and understandable
- **Completeness**: All required aspects are documented
- **Consistency**: Terminology and structure are consistent

### Developer Onboarding Assessment
- **Development Setup**: Documentation for setting up development environment
- **Contribution Guidelines**: Process for making changes is documented
- **Code Navigation**: Structure and organization are documented
- **Test Documentation**: Testing approach and procedures are documented
```

### 6. Release Artifacts Verification

Verification of required release artifacts:

```markdown
## Release Artifacts Verification

### Build Artifacts
| Artifact | Verification Method | Status | Verified By |
|----------|---------------------|--------|-------------|
| Application Binary | SHA-256 checksum, smoke test | ✅ Verified | [Name] |
| Database Migration Scripts | Code review, test execution | ✅ Verified | [Name] |
| Client Libraries | API compatibility testing | ✅ Verified | [Name] |
| Documentation Packages | Completeness check | ✅ Verified | [Name] |

### Release Notes
- **Completeness**: All changes are documented
- **Accuracy**: Changes are accurately described
- **Clarity**: Changes are clearly explained
- **Audience Appropriateness**: Notes are suitable for intended audience

### Deployment Readiness
- **Deployment Scripts**: Verified through rehearsal
- **Configuration Files**: Validated for all environments
- **Feature Flags**: Correctly configured
- **Rollback Procedures**: Verified through rehearsal
```

## Meta-Systemic Principle Application

### Parsimony
- Reference canonical architecture documentation
- Link to automated test results rather than duplicating
- Refer to established quality standards
- Reference existing documentation rather than summarizing

Example:
```markdown
The implementation adheres to the architecture defined in the [System Architecture Document](../architecture/system-architecture.md), with specific attention to the component boundaries and interface contracts.

For detailed test results, see the [Automated Test Report](../test-results/automated-test-report.md), which shows 87% overall coverage exceeding our 85% target.
```

### Tensegrity
- Identify bidirectional dependencies between components
- Validate reciprocal relationships between services
- Ensure balanced responsibility distribution
- Verify support mechanisms between components

Example:
```markdown
## Component Relationship Assessment

| Component | Provides To | Consumes From | Balance Assessment |
|-----------|-------------|---------------|-------------------|
| User Service | Authentication Service, Profile Service | Notification Service, Authorization Service | ✅ Balanced |
| Content Service | Search Service, Analytics Service | User Service, Storage Service | ✅ Balanced |
| Notification Service | User Service, Admin Service | Message Queue, Template Service | ⚠️ Slightly Overloaded |
```

### Modularity
- Verify clear component boundaries
- Validate interface contracts
- Ensure proper encapsulation
- Confirm independent component testability

Example:
```markdown
## Modularity Assessment

| Component | Boundary Clarity | Interface Definition | Encapsulation | Independent Testing |
|-----------|-----------------|---------------------|---------------|---------------------|
| Authentication | ✅ Clear | ✅ Well-defined | ✅ Strong | ✅ Comprehensive |
| User Management | ✅ Clear | ✅ Well-defined | ⚠️ Some leakage | ✅ Comprehensive |
| Content Service | ✅ Clear | ⚠️ Some ambiguity | ✅ Strong | ⚠️ Some gaps |
```

### Coherence
- Verify consistent pattern application
- Validate naming convention adherence
- Ensure consistent error handling
- Confirm architectural pattern alignment

Example:
```markdown
## Pattern Consistency Assessment

| Pattern Type | Consistency | Areas for Improvement |
|--------------|-------------|----------------------|
| Error Handling | ⚠️ Moderate | Inconsistent approach in API controllers |
| Naming Conventions | ✅ Strong | Consistently applied across codebase |
| State Management | ✅ Strong | Consistent redux pattern throughout |
| API Design | ✅ Strong | Consistent RESTful design |
```

### Clarity
- Verify documentation clarity for all components
- Ensure code comments explain complex logic
- Validate API documentation with examples
- Confirm clear rationale for technical decisions

Example:
```markdown
## Documentation Clarity Assessment

| Documentation | Clarity | Examples | Rationale | Actionable |
|---------------|---------|----------|-----------|------------|
| API Documentation | ✅ High | ✅ Comprehensive | ✅ Clear | ✅ Yes |
| Architecture Docs | ✅ High | ⚠️ Limited | ✅ Clear | ✅ Yes |
| Deployment Docs | ✅ High | ✅ Comprehensive | ⚠️ Partial | ✅ Yes |
| Developer Guide | ⚠️ Moderate | ⚠️ Limited | ⚠️ Partial | ⚠️ Partially |
```

### Adaptivity
- Verify appropriate adaptations to context
- Validate context-specific implementations
- Ensure pattern evolution maintains integrity
- Confirm context-sensitive configuration

Example:
```markdown
## Context Adaptation Assessment

| Feature | Context Adaptation | Integrity Maintenance | Assessment |
|---------|-------------------|------------------------|------------|
| Authentication | Adapted for enterprise SSO | Core flow preserved | ✅ Appropriate |
| Data Storage | Context-specific storage engine | Interface abstraction maintained | ✅ Appropriate |
| UI Components | Responsive design variations | Design system adherence | ✅ Appropriate |
| API Rate Limiting | Context-sensitive limits | Consistent implementation | ⚠️ Needs Improvement |
```

## Release Scope-Specific Considerations

### Major Release Review
- Comprehensive architectural assessment
- Detailed technical debt analysis
- Full component interaction review
- Extensive stakeholder demonstrations
- Complete documentation review
- Performance validation across all components

### Minor Release Review
- Focused architectural impact assessment
- Technical debt change analysis
- Affected component interaction review
- Targeted stakeholder demonstrations
- Updated documentation review
- Performance validation for changed components

### Patch Release Review
- Specific fix verification
- Regression testing validation
- Minimal component interaction review
- Limited stakeholder demonstrations
- Focused documentation updates review
- Performance validation for affected operations

### Emergency Release Review
- Critical fix verification
- Core regression testing validation
- Essential component interaction review
- Minimal stakeholder notification
- Critical path documentation verification
- Performance validation on critical path only

## Technical Go/No-Go Decision Guidance

Framework for making the technical release decision:

```markdown
## Technical Go/No-Go Decision

### Critical Criteria (Must All Pass)
- [ ] All functional requirements implemented and verified
- [ ] All automated tests passing
- [ ] No critical or high security vulnerabilities
- [ ] Performance within acceptable thresholds
- [ ] No data integrity risks identified
- [ ] Deployment and rollback procedures verified

### Important Criteria (Majority Should Pass)
- [ ] Code quality metrics meet standards
- [ ] Technical debt within acceptable levels
- [ ] Documentation complete and accurate
- [ ] Monitoring capabilities in place
- [ ] Support team prepared for deployment
- [ ] Known issues documented with workarounds

### Decision Options
1. **Go**: All critical criteria pass, majority of important criteria pass
2. **Conditional Go**: All critical criteria pass, some important criteria need attention post-release
3. **No-Go**: Any critical criteria fail or too many important criteria fail

### Decision Rationale
[Document the rationale for the go/no-go decision, including any conditions or follow-up actions]
```

## Human-AI Team Collaboration

In our two-person team:

### Human Team Member Focus
- Make final go/no-go decisions
- Evaluate subjective quality aspects
- Assess business risk of technical issues
- Provide domain expertise for edge cases
- Validate complex technical demonstrations

### AI Agent Focus
- Systematically validate metrics against criteria
- Generate comprehensive review documentation
- Identify potential issues from pattern analysis
- Ensure complete coverage of review areas
- Track resolution of previously identified issues

<important>
The pre-release review is the final quality gate before deployment. A thorough technical review ensures that the implementation meets all requirements, follows architectural guidelines, and maintains system integrity, while being adapted appropriately to the specific context.
</important>