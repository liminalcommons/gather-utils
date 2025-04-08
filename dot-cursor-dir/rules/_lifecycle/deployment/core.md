---
description: 
globs: **/deployment/*.md,**/deployment/*.mdx,**/releases/*/deployment.md,**/releases/*/deployment.mdx
alwaysApply: false
---
---
description: "Core guidance for the deployment phase of the release lifecycle"
globs: "**/deployment/*.md,**/deployment/*.mdx,**/releases/*/deployment.md,**/releases/*/deployment.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Deployment Phase Guidance

<critical>
The deployment phase represents the critical transition of changes into production. This phase requires careful coordination, validation, and risk management to ensure system integrity during and after deployment.
</critical>

## Core Deployment Activities

The deployment phase consists of these essential activities:

1. **Pre-Deployment Validation**: Final verification that the release is ready for deployment
2. **Deployment Planning**: Detailed sequence of steps for implementing the changes
3. **Execution**: Controlled implementation of the changes
4. **Verification**: Confirming the changes were applied correctly and function as expected
5. **Monitoring**: Observing system behavior after deployment
6. **Contingency Management**: Handling any issues that arise during deployment

## Required Metadata

Every deployment plan document must include:

```yaml
---
title: "[Release Name] Deployment Plan"
version: "[Release Version]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date]"
last_updated: "[Last Update Date]"
system_context: "[Code|Release|Agent]"
owner: "[Deployment Owner]"
status: "[Draft|Approved|In Progress|Completed]"
---
```

## Deployment Plan Structure

Structure your deployment plan document as follows:

### 1. Executive Summary
Brief overview of the release being deployed, its purpose, and deployment approach.

### 2. Pre-Deployment Checklist
Comprehensive list of items that must be verified before deployment begins:

```markdown
## Pre-Deployment Checklist

| Item | Status | Verified By | Verification Date |
|------|--------|-------------|-------------------|
| All tests passed | ✅/❌ | [Name] | [Date] |
| Documentation updated | ✅/❌ | [Name] | [Date] |
| Security review completed | ✅/❌ | [Name] | [Date] |
| Performance validation completed | ✅/❌ | [Name] | [Date] |
| Stakeholder approvals received | ✅/❌ | [Name] | [Date] |
| Required resources available | ✅/❌ | [Name] | [Date] |
| Deployment window confirmed | ✅/❌ | [Name] | [Date] |
| Rollback plan verified | ✅/❌ | [Name] | [Date] |
```

### 3. Deployment Strategy
Description of the overall deployment approach:

```markdown
## Deployment Strategy

### Approach
[Describe the deployment strategy: big bang, incremental, blue-green, canary, etc.]

### Rationale
[Explain why this strategy was chosen for this specific release]

### Risk Assessment
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [Mitigation strategy] |

### Change Window
- **Start Date/Time**: [Date and time]
- **End Date/Time**: [Date and time]
- **Timezone**: [Timezone]
```

### 4. Detailed Deployment Steps
Step-by-step instructions for the deployment:

```markdown
## Deployment Steps

### 1. [Step Name]
- **Description**: [Detailed description of the step]
- **Executor**: [Person/Role responsible]
- **Expected Duration**: [Time estimate]
- **Verification Method**: [How to verify this step was successful]
- **Dependencies**: [Any dependencies on previous steps]

### 2. [Step Name]
...
```

### 5. Verification Plan
Procedures to verify the deployment was successful:

```markdown
## Verification Plan

### Functional Verification
| Feature | Verification Method | Success Criteria |
|---------|---------------------|------------------|
| [Feature 1] | [Method] | [Criteria] |

### Technical Verification
| Component | Verification Method | Success Criteria |
|-----------|---------------------|------------------|
| [Component 1] | [Method] | [Criteria] |

### Performance Verification
| Metric | Baseline | Target | Verification Method |
|--------|----------|--------|---------------------|
| [Metric 1] | [Baseline value] | [Target value] | [Method] |
```

### 6. Rollback Plan
Procedures to revert changes if necessary:

```markdown
## Rollback Plan

### Rollback Triggers
- [Condition that would trigger rollback]
- [Condition that would trigger rollback]

### Rollback Decision Authority
- **Authority**: [Person/Role who can make rollback decision]
- **Secondary Authority**: [Backup person/role]

### Rollback Steps
1. [Detailed rollback step]
2. [Detailed rollback step]

### Post-Rollback Verification
- [Verification to perform after rollback]
```

### 7. Post-Deployment Monitoring
Plan for monitoring system after deployment:

```markdown
## Post-Deployment Monitoring

### Key Metrics to Monitor
| Metric | Normal Range | Alert Threshold | Response |
|--------|--------------|-----------------|----------|
| [Metric 1] | [Range] | [Threshold] | [Response action] |

### Monitoring Duration
- **Intensive Monitoring Period**: [Time period]
- **Extended Monitoring Period**: [Time period]

### Monitoring Responsibility
- **Primary**: [Person/Role]
- **Secondary**: [Person/Role]
```

### 8. Communication Plan
Plan for communications during and after deployment:

```markdown
## Communication Plan

### Pre-Deployment Communication
| Audience | Message | Timing | Channel | Responsible |
|----------|---------|--------|---------|-------------|
| [Audience] | [Message] | [When] | [Channel] | [Who] |

### During Deployment
| Event | Audience | Message | Channel | Responsible |
|-------|----------|---------|---------|-------------|
| [Event] | [Audience] | [Message] | [Channel] | [Who] |

### Post-Deployment
| Timing | Audience | Message | Channel | Responsible |
|--------|----------|---------|---------|-------------|
| [When] | [Audience] | [Message] | [Channel] | [Who] |
```

## Meta-Systemic Principle Application

### Parsimony
- Reference deployment patterns from canonical sources
- Use templates for consistent deployment documentation
- Avoid duplicating verification procedures
- Maintain single source of truth for deployment status

### Tensegrity
- Ensure balanced responsibilities across deployment team
- Define clear handoffs between deployment steps
- Establish bidirectional verification between dependent components
- Design deployment steps with mutual support

### Modularity
- Create clear boundaries between deployment phases
- Define explicit interfaces between deployment and verification
- Encapsulate component-specific deployment details
- Maintain separation between deployment and rollback procedures

### Coherence
- Follow consistent deployment patterns appropriate to context
- Maintain terminology consistency throughout documentation
- Align verification approaches across components
- Use consistent communication patterns

### Clarity
- Provide detailed steps with examples where needed
- Include explicit success criteria for verification
- Document rollback triggers unambiguously
- Explain rationale for deployment decisions

### Adaptivity
- Tailor deployment approach to release context
- Adapt verification intensity to change risk
- Adjust monitoring based on system criticality
- Scale communication to deployment complexity

## Context-Specific Deployment Approaches

### For Code System Deployment
- Focus on technical deployment sequence
- Include database migration plans if applicable
- Specify infrastructure changes
- Detail service restart sequences
- Include cache invalidation steps

### For Release Process Deployment
- Focus on process transition timeline
- Include documentation updates
- Specify training requirements
- Detail old/new process overlap period
- Include process verification steps

### For Agent System Deployment
- Focus on knowledge transfer verification
- Include capability validation
- Specify prompt/guidance updates
- Detail collaboration pattern changes
- Include continuity verification

## Deployment Phase Validation Checklist

Before concluding the deployment phase, verify that:

- [ ] All deployment steps have been completed successfully
- [ ] All verifications have passed
- [ ] System is functioning as expected in production
- [ ] Monitoring is in place and showing normal patterns
- [ ] Post-deployment communications have been sent
- [ ] Deployment documentation is complete and accurate
- [ ] Lessons learned have been captured for evaluation phase
- [ ] Any issues encountered have been documented

## Release Scope-Specific Considerations

### Major Release Deployment
- More extensive pre-deployment validation
- Longer monitoring period
- More comprehensive communications
- Detailed coordination across teams
- Incremental deployment where possible

### Minor Release Deployment
- Standard pre-deployment validation
- Normal monitoring period
- Targeted communications
- Focused coordination
- Standard deployment approach

### Patch Release Deployment
- Focused pre-deployment validation
- Abbreviated monitoring for non-critical areas
- Minimal communications
- Streamlined coordination
- Efficient deployment process

### Emergency Release Deployment
- Critical-path validation only
- Intensive monitoring
- Urgent, clear communications
- Direct coordination
- Expedited deployment with enhanced oversight

<important>
The deployment phase represents the culmination of the release lifecycle. Careful planning, precise execution, thorough verification, and attentive monitoring are essential to ensure successful deployment with minimal disruption to users and the system.
</important>