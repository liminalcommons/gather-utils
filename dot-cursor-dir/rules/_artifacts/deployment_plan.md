---
description: 
globs: **/deployment/*.md,**/deployment/*.mdx,**/releases/*/deployment.md,**/releases/*/deployment.mdx
alwaysApply: false
---
---
description: "Guidance for creating comprehensive deployment plan documents"
globs: "**/deployment/*.md,**/deployment/*.mdx,**/releases/*/deployment.md,**/releases/*/deployment.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Deployment Plan Guidance

<critical>
The deployment plan document provides a comprehensive roadmap for implementing changes into production. It must detail all deployment steps, verification procedures, rollback mechanisms, and communication strategies to ensure a controlled, successful transition.
</critical>

## Document Purpose

The deployment plan document serves to:

1. Define the detailed sequence of deployment steps
2. Establish verification processes to confirm deployment success
3. Provide rollback procedures in case of issues
4. Document communication strategies before, during, and after deployment
5. Define post-deployment monitoring and support plans
6. Identify and mitigate deployment-specific risks

## Required Metadata

Every deployment plan document must include this metadata section:

```yaml
---
title: "[Release Name] Deployment Plan"
version: "[Version Number]"
classification: "[Major|Minor|Patch|Emergency]"
created: "[Creation Date: YYYY-MM-DD]"
last_updated: "[Last Update Date: YYYY-MM-DD]"
system_context: "[Code|Release|Agent]"
owner: "[Deployment Owner: Name/Role]"
status: "[Draft|Approved|In Progress|Completed]"
related_plan: "[Link to Release Plan Document]"
---
```

## Document Structure Template

### 1. Executive Summary (Required)

A concise overview (2-3 paragraphs) of the deployment approach, including:
- Deployment strategy
- Schedule and timeline
- Key risks and mitigations
- Required resources and teams

Example:
```markdown
## Executive Summary

This deployment plan outlines the process for implementing Release 2.3.0, which enhances the document management system's search capabilities. We will use a phased deployment approach, starting with a canary release to 10% of users, followed by gradual expansion to all users over 48 hours.

The deployment is scheduled for April 17, 2025, beginning at 02:00 UTC during our standard maintenance window. The primary deployment team consists of three engineers with database, application, and frontend expertise, with additional support available from the QA and product teams.

The main risks include potential performance impacts on the search service and data migration duration uncertainty. These risks will be mitigated through extensive pre-deployment performance testing and a database backup strategy that allows for rapid rollback if needed.
```

### 2. Pre-Deployment Checklist (Required)

Comprehensive checklist that must be completed before deployment begins:

```markdown
## Pre-Deployment Checklist

| Item | Status | Verified By | Verification Date |
|------|--------|-------------|-------------------|
| All validation tests passed | ✅/❌ | [Name] | [Date] |
| Performance testing completed and meeting targets | ✅/❌ | [Name] | [Date] |
| Security review completed | ✅/❌ | [Name] | [Date] |
| Documentation updated | ✅/❌ | [Name] | [Date] |
| Required infrastructure provisioned | ✅/❌ | [Name] | [Date] |
| Stakeholder approvals received | ✅/❌ | [Name] | [Date] |
| Deployment team briefed | ✅/❌ | [Name] | [Date] |
| Rollback plan validated | ✅/❌ | [Name] | [Date] |
| All deployment dependencies available | ✅/❌ | [Name] | [Date] |
| Change management approval received | ✅/❌ | [Name] | [Date] |
```

### 3. Deployment Strategy (Required)

Description of the overall approach to deployment:

```markdown
## Deployment Strategy

### Approach
We will use a [Blue-Green/Canary/Rolling/All-at-Once] deployment strategy for this release.

### Rationale
This strategy was chosen because:
- [Reason 1 for choosing this strategy]
- [Reason 2 for choosing this strategy]
- [Reason 3 for choosing this strategy]

### Deployment Window
- **Start Date/Time**: [Date and time in specific timezone]
- **End Date/Time**: [Date and time in specific timezone]
- **Timezone**: [Timezone reference, e.g., UTC, EST]

### Personnel Requirements
- **Deployment Lead**: [Name/Role]
- **Technical Support**: [Names/Roles]
- **Validation Team**: [Names/Roles]
- **Business Stakeholders**: [Names/Roles]
- **Escalation Contact**: [Name/Role]

### Environment Information
- **Target Environments**: [List of environments]
- **Access Requirements**: [Access details/credentials location]
- **Environment Configuration**: [Configuration specifics or reference]
```

### 4. Detailed Deployment Steps (Required)

Step-by-step instructions for executing the deployment:

```markdown
## Deployment Steps

### Phase 1: [Phase Name, e.g., "Preparation"]

#### Step 1.1: [Step Name]
- **Description**: [Detailed description of what this step accomplishes]
- **Executor**: [Person/Role responsible]
- **Estimated Duration**: [Time estimate]
- **Commands/Actions**:
  ```bash
  # Example commands to execute
  command argument1 argument2
  ```
- **Expected Outcome**: [What should happen when successful]
- **Verification Method**: [How to verify this step was successful]
- **Rollback Procedure**: [How to undo this step if needed]

#### Step 1.2: [Step Name]
...

### Phase 2: [Phase Name, e.g., "Database Migration"]
...

### Phase 3: [Phase Name, e.g., "Application Deployment"]
...

### Phase 4: [Phase Name, e.g., "Verification"]
...
```

### 5. Verification Plan (Required)

Detailed procedures to verify the deployment was successful:

```markdown
## Verification Plan

### Functionality Verification
| Feature | Verification Method | Success Criteria | Owner |
|---------|---------------------|------------------|-------|
| [Feature 1] | [Method] | [Criteria] | [Owner] |
| [Feature 2] | [Method] | [Criteria] | [Owner] |

### Technical Verification
| Component | Verification Method | Success Criteria | Owner |
|-----------|---------------------|------------------|-------|
| [Component 1] | [Method] | [Criteria] | [Owner] |
| [Component 2] | [Method] | [Criteria] | [Owner] |

### Performance Verification
| Metric | Baseline | Target | Method | Owner |
|--------|----------|--------|--------|-------|
| [Metric 1] | [Baseline] | [Target] | [Method] | [Owner] |
| [Metric 2] | [Baseline] | [Target] | [Method] | [Owner] |

### User Acceptance Testing
| Test Case | Tester | Success Criteria | Priority |
|-----------|--------|------------------|----------|
| [Test Case 1] | [Tester] | [Criteria] | [Priority] |
| [Test Case 2] | [Tester] | [Criteria] | [Priority] |
```

### 6. Rollback Plan (Required)

Detailed procedures to revert changes if necessary:

```markdown
## Rollback Plan

### Rollback Triggers
The following conditions will trigger consideration of a rollback:
- [Condition 1, e.g., "Critical functionality X is not working"]
- [Condition 2, e.g., "Performance degradation exceeds 20%"]
- [Condition 3, e.g., "Error rate exceeds 1%"]

### Rollback Decision Authority
- **Primary Decision Maker**: [Name/Role]
- **Secondary Decision Maker**: [Name/Role]
- **Consultation Required With**: [Names/Roles]

### Rollback Steps

#### Step 1: [Step Name]
- **Description**: [Detailed description]
- **Executor**: [Person/Role responsible]
- **Estimated Duration**: [Time estimate]
- **Commands/Actions**:
  ```bash
  # Example commands to execute
  command argument1 argument2
  ```
- **Verification Method**: [How to verify this step was successful]

#### Step 2: [Step Name]
...

### Post-Rollback Verification
- [Verification step 1]
- [Verification step 2]
- [Verification step 3]

### Recovery Time Objective
- **Maximum Acceptable Downtime**: [Time period]
- **Expected Recovery Time**: [Time estimate]
```

### 7. Post-Deployment Monitoring (Required)

Plan for monitoring the system after deployment:

```markdown
## Post-Deployment Monitoring

### Critical Metrics
| Metric | Normal Range | Warning Threshold | Critical Threshold | Action If Exceeded |
|--------|--------------|-------------------|---------------------|-------------------|
| [Metric 1] | [Range] | [Warning Threshold] | [Critical Threshold] | [Action] |
| [Metric 2] | [Range] | [Warning Threshold] | [Critical Threshold] | [Action] |

### Monitoring Responsibilities
- **Primary Monitor**: [Name/Role]
- **Secondary Monitor**: [Name/Role]
- **Monitoring Tools**: [Tools/Dashboards]
- **Monitoring Duration**: [Duration, e.g., "72 hours post-deployment"]

### Escalation Path
- **Level 1**: [Name/Role, Response Time]
- **Level 2**: [Name/Role, Response Time]
- **Level 3**: [Name/Role, Response Time]

### Monitoring Schedule
| Timeframe | Monitoring Frequency | Responsible Team |
|-----------|----------------------|------------------|
| First 4 hours | Continuous | [Team] |
| 4-24 hours | Hourly | [Team] |
| 24-72 hours | Every 4 hours | [Team] |
```

### 8. Communication Plan (Required)

Plan for communications before, during, and after deployment:

```markdown
## Communication Plan

### Pre-Deployment Communications
| Audience | Message | Timing | Channel | Responsible |
|----------|---------|--------|---------|-------------|
| [Audience] | [Message] | [Timing] | [Channel] | [Responsible] |

### Deployment Status Updates
| Status Event | Audience | Message | Channel | Responsible |
|--------------|----------|---------|---------|-------------|
| Deployment Started | [Audience] | [Message] | [Channel] | [Responsible] |
| Phase Completion | [Audience] | [Message] | [Channel] | [Responsible] |
| Issues Encountered | [Audience] | [Message] | [Channel] | [Responsible] |
| Deployment Complete | [Audience] | [Message] | [Channel] | [Responsible] |

### Post-Deployment Communications
| Timing | Audience | Message | Channel | Responsible |
|--------|----------|---------|---------|-------------|
| Immediate | [Audience] | [Message] | [Channel] | [Responsible] |
| 24 Hours | [Audience] | [Message] | [Channel] | [Responsible] |
| 1 Week | [Audience] | [Message] | [Channel] | [Responsible] |
```

### 9. Risk Assessment and Mitigation (Required)

Detailed assessment of deployment-specific risks:

```markdown
## Risk Assessment and Mitigation

| Risk | Impact | Likelihood | Mitigation Strategy | Owner |
|------|--------|------------|---------------------|-------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [Strategy] | [Owner] |
| [Risk 2] | High/Medium/Low | High/Medium/Low | [Strategy] | [Owner] |

### Contingency Plans
- **Scenario 1**: [Description of scenario]
  - **Response Plan**: [Action plan]
  - **Required Resources**: [Resources]
  - **Decision Maker**: [Name/Role]

- **Scenario 2**: [Description of scenario]
  - **Response Plan**: [Action plan]
  - **Required Resources**: [Resources]
  - **Decision Maker**: [Name/Role]
```

### 10. System-Specific Sections (Conditional)

#### For Code System Deployments
- Infrastructure changes
- Data migration procedures
- Service dependencies and order
- Configuration updates

Example:
```markdown
## Code System Deployment Details

### Infrastructure Provisioning
- **New Resources**: [List of new resources]
- **Resource Modifications**: [List of modifications]
- **Infrastructure as Code Location**: [Repository/path]
- **Provisioning Steps**: [Steps or reference]

### Database Migration
- **Schema Changes**: [Description or reference]
- **Data Migration Scripts**: [Location]
- **Expected Duration**: [Estimate]
- **Migration Validation**: [Verification approach]

### Service Deployment Order
1. [Service 1]: [Rationale]
2. [Service 2]: [Rationale]
3. [Service 3]: [Rationale]

### Configuration Updates
- **Config Files**: [Files/locations]
- **Environment Variables**: [Variables]
- **Feature Flags**: [Flags and initial states]
```

#### For Release System Deployments
- Process documentation updates
- Template changes
- Rule updates
- Tool deployments

Example:
```markdown
## Release System Deployment Details

### Process Documentation Updates
- **Documents to Update**: [List of documents]
- **Update Procedure**: [Process]
- **Verification Method**: [Verification approach]

### Template Modifications
- **Templates to Update**: [List of templates]
- **Change Summary**: [Summary of changes]
- **Template Location**: [Location]

### Rule Updates
- **Rules to Deploy**: [List of rules]
- **Rule Locations**: [Locations]
- **Rule Validation**: [Validation process]

### Tool Deployments
- **Tools to Update**: [List of tools]
- **Deployment Procedure**: [Process]
- **Compatibility Verification**: [Verification approach]
```

#### For Agent System Deployments
- Capability updates
- Knowledge base changes
- Interaction pattern updates
- Testing approach

Example:
```markdown
## Agent System Deployment Details

### Capability Enhancements
- **New Capabilities**: [List of capabilities]
- **Capability Integration**: [Integration process]
- **Validation Method**: [Verification approach]

### Knowledge Base Updates
- **Knowledge Domains Updated**: [List of domains]
- **Knowledge Sources**: [Sources/locations]
- **Verification Process**: [Process]

### Interaction Pattern Updates
- **Updated Patterns**: [List of patterns]
- **User Experience Changes**: [Description]
- **Testing Approach**: [Approach]

### Prompt Template Updates
- **Templates to Update**: [List of templates]
- **Update Procedure**: [Process]
- **Template Validation**: [Validation approach]
```

## Meta-Systemic Application

### Parsimony
- Reference deployment procedures from canonical sources
- Avoid duplicating verification steps in multiple sections
- Link to existing documentation for standard procedures
- Reference the release plan and validation report

Example:
```markdown
This deployment follows our [Standard Blue-Green Deployment Process](mdc:../processes/blue-green-deployment.md) with the specific adaptations noted in the Deployment Strategy section.

For common verification procedures, refer to the [Standard Verification Checklist](mdc:../processes/verification-checklist.md). Only release-specific verification steps are detailed in this document.
```

### Tensegrity
- Define clear responsibilities and handoffs between teams
- Document bidirectional dependencies between deployment steps
- Balance responsibilities appropriately across the deployment team
- Ensure mutual support during critical operations

Example:
```markdown
### Team Responsibilities and Support Matrix

| Team | Primary Responsibilities | Supports | Supported By |
|------|--------------------------|----------|--------------|
| Database | Schema migration, data verification | Application deployment | Infrastructure, Monitoring |
| Application | Service deployment, configuration | Frontend deployment, Database migration | Infrastructure, QA |
| QA | Verification, user acceptance testing | All teams | None |
| Infrastructure | Environment preparation, scaling | All teams | None |
```

### Modularity
- Create clear boundaries between deployment phases
- Define explicit interfaces between teams and responsibilities
- Encapsulate environment-specific details
- Structure the plan for independent section execution

Example:
```markdown
### Phase Boundaries and Interfaces

Each deployment phase has explicit entry and exit criteria:

| Phase | Entry Criteria | Exit Criteria | Output Artifact |
|-------|---------------|---------------|-----------------|
| Preparation | Approval from Change Board | All resources provisioned | Environment Readiness Report |
| Database Migration | Environment Readiness Report | Schema and data verified | Database Validation Report |
| Application Deployment | Database Validation Report | All services deployed | Service Health Report |
| Verification | Service Health Report | All checks passed | Deployment Verification Report |
```

### Coherence
- Follow consistent step formats throughout the document
- Use standard terminology for deployment concepts
- Apply consistent verification approaches
- Maintain consistent communication patterns

Example:
```markdown
This deployment plan follows our standard format with consistent section structure, terminology, and step formats across all phases. All verification methods align with our standard verification framework, and communication follows our established notification templates.
```

### Clarity
- Provide detailed step-by-step instructions
- Include command examples for technical steps
- Document expected outcomes for each step
- Explain rationale for key decisions

Example:
```markdown
### Command Examples with Expected Output

For the database migration step, execute:

```bash
migrate-db --version 2.3.0 --environment production
```

Expected output:
```
Migration starting...
Creating backup... Done
Applying schema changes... Done
Verifying schema... Done
Migration completed successfully in 3m 24s
```

If you see errors in the "Verifying schema" step, stop and refer to the rollback procedure.
```

### Adaptivity
- Scale detail level based on deployment complexity
- Adapt communication plan to stakeholder needs
- Provide appropriate monitoring intensity based on risk
- Adjust verification depth based on change impact

Example:
```markdown
### Adaptive Monitoring Approach

This deployment uses our adaptive monitoring framework that scales based on:
- Release scope (Minor)
- Component criticality (Search is business-critical)
- Change complexity (Medium)
- Historical stability (High)

Based on these factors, we will implement Level 2 monitoring intensity with:
- 72-hour continuous monitoring period
- 15-minute metric evaluation frequency
- Automated alerts at 70% of normal thresholds
- Dedicated monitoring personnel for first 24 hours
```

## Release Scope-Specific Guidance

### Major Release Deployment
- Comprehensive step-by-step instructions
- Extended pre and post-deployment activities
- Detailed verification of all affected components
- Staged rollout with multiple validation gates
- Comprehensive communication plan
- Extended monitoring period

### Minor Release Deployment
- Focused deployment steps for changed components
- Standard pre and post-deployment activities
- Verification of directly affected functionality
- Controlled rollout with key validation points
- Standard communication to all stakeholders
- Normal monitoring period

### Patch Release Deployment
- Streamlined deployment steps
- Abbreviated pre and post-deployment activities
- Targeted verification of fixed issues
- Efficient rollout with minimal stages
- Focused communication to affected stakeholders
- Abbreviated monitoring focusing on fixed issues

### Emergency Release Deployment
- Critical path deployment steps only
- Essential pre-deployment validation
- Rapid deployment approach
- Specific verification of emergency fix
- Urgent stakeholder communication
- Intensive monitoring of affected components

## Deployment Plan Validation Checklist

Before finalizing the deployment plan, verify that:

- [ ] All deployment steps are clearly documented with responsible parties
- [ ] Verification procedures are comprehensive and specific
- [ ] Rollback plan is complete and tested
- [ ] Communication plan covers all stakeholders and contingencies
- [ ] Risk assessment identifies all significant risks with mitigations
- [ ] All pre-deployment requirements are specified
- [ ] Post-deployment monitoring is adequately defined
- [ ] System-specific considerations are addressed appropriately
- [ ] All required resources and personnel are identified
- [ ] The plan follows meta-systemic principles appropriate to the release scope

<important>
The deployment plan is critical to ensuring a smooth transition to production. Invest appropriate time in creating a comprehensive, clear plan that anticipates potential issues and provides explicit guidance for all scenarios.
</important>