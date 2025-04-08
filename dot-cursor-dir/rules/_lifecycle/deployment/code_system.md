---
description: 
globs: **/code/deployment/*.md,**/code/deployment/*.mdx,**/releases/*/code_deployment.md,**/releases/*/code_deployment.mdx
alwaysApply: false
---
---
description: "Code-specific guidance for the deployment phase of the release lifecycle"
globs: "**/code/deployment/*.md,**/code/deployment/*.mdx,**/releases/*/code_deployment.md,**/releases/*/code_deployment.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code System Deployment Guidance

<critical>
This rule provides specialized guidance for the deployment phase when the primary system context is code-based system development. Apply these guidelines in conjunction with the core deployment phase rules.
</critical>

## Code System Deployment Approach

When deploying code-based systems, focus on these key areas:

### 1. Pre-Deployment Verification

Complete these essential verifications before deployment:

```markdown
## Pre-Deployment Verification Checklist

### Build Validation
- [ ] All CI/CD pipelines successfully completed
- [ ] Build artifacts correctly generated and versioned
- [ ] Build signature verification passed
- [ ] Dependency security scanning completed
- [ ] License compliance verified

### Environment Readiness
- [ ] Target environment configuration validated
- [ ] Required infrastructure provisioned and verified
- [ ] Environment-specific configuration prepared
- [ ] Required service accounts and permissions verified
- [ ] External system dependencies available and verified

### Data Readiness
- [ ] Database migration scripts validated
- [ ] Data backup completed
- [ ] Data integrity validation performed
- [ ] Data conversion/transformation tested
- [ ] Rollback data strategy verified

### Team Readiness
- [ ] Deployment team members and responsibilities assigned
- [ ] Support team notified and available
- [ ] Stakeholders informed of deployment schedule
- [ ] Communication channels established
- [ ] Escalation path documented and verified
```

### 2. Deployment Strategy

Select and document the appropriate deployment strategy:

```markdown
## Deployment Strategy Documentation

### Selected Strategy: [Strategy Name]
[Brief description of the selected deployment strategy]

| Strategy | Appropriate For | Advantages | Disadvantages | Selected |
|----------|----------------|------------|---------------|----------|
| Big Bang | Simple applications, offline systems | Simple, straightforward | High risk, significant downtime | ✓/✗ |
| Blue-Green | High-availability systems | Minimal downtime, easy rollback | Resource intensive, complex routing | ✓/✗ |
| Canary | User-facing applications | Progressive risk management, early feedback | Complex monitoring, slower deployment | ✓/✗ |
| Rolling | Distributed systems, clustered applications | Reduced resource needs, continuous availability | Complex orchestration, longer deployment time | ✓/✗ |
| Feature Flags | Complex applications, experimental features | Fine-grained control, separates deployment from release | Implementation complexity, technical debt | ✓/✗ |

### Strategy Rationale
[Explanation of why this strategy was selected for this specific release]

### Key Strategy Parameters
- **Deployment Velocity**: [e.g., Percentage/time for canary, batch size for rolling]
- **Observation Periods**: [e.g., Time between increments]
- **Success Metrics**: [e.g., Error rates, performance thresholds]
- **Automatic Progression Criteria**: [e.g., Conditions for advancing deployment]
- **Rollback Triggers**: [e.g., Conditions that will trigger automatic rollback]
```

### 3. Database Changes

Manage database changes safely:

```markdown
## Database Deployment Plan

### Schema Changes
| Change | Impact | Dependencies | Execution Order |
|--------|--------|--------------|----------------|
| [Change 1] | [Impact] | [Dependencies] | [Order] |
| [Change 2] | [Impact] | [Dependencies] | [Order] |

### Migration Strategy
- **Approach**: [e.g., Zero-downtime migration, scheduled downtime, schema evolution]
- **Backward Compatibility**: [How schema changes maintain backward compatibility]
- **Performance Impact**: [Expected impact on database performance]
- **Execution Method**: [e.g., ORM migrations, SQL scripts, database tools]

### Data Migration/Transformation
- **Data Volume**: [Amount of data affected]
- **Migration Method**: [How data will be migrated/transformed]
- **Validation Approach**: [How data integrity will be verified]
- **Performance Considerations**: [Performance impact and mitigation]

### Rollback Plan
- **Rollback Scripts**: [Location of rollback scripts]
- **Rollback Verification**: [How rollback will be tested]
- **Data Recovery Method**: [How to recover data if needed]
- **Rollback Decision Criteria**: [When to trigger database rollback]
```

### 4. Service Deployment Sequence

Document the precise deployment sequence:

```markdown
## Service Deployment Sequence

### Dependency Graph
[Visual or textual representation of service dependencies]

### Deployment Order
1. **[Service/Component 1]**
   - **Pre-requisites**: [Requirements before deployment]
   - **Deployment Steps**: [Specific deployment actions]
   - **Verification**: [How to verify successful deployment]
   - **Dependencies**: [Services that depend on this component]

2. **[Service/Component 2]**
   - **Pre-requisites**: [Requirements before deployment]
   - **Deployment Steps**: [Specific deployment actions]
   - **Verification**: [How to verify successful deployment]
   - **Dependencies**: [Services that depend on this component]

### Critical Path
- **Essential Services**: [Services on the critical path]
- **Deployment Windows**: [Time constraints for critical services]
- **Fallback Options**: [Alternative approaches if issues occur]
- **Decision Points**: [Where to pause and evaluate progress]
```

### 5. Configuration Management

Manage configuration effectively across environments:

```markdown
## Configuration Management

### Configuration Changes
| Parameter | Previous Value | New Value | Impact | Affected Services |
|-----------|----------------|-----------|--------|-------------------|
| [Parameter 1] | [Previous] | [New] | [Impact] | [Services] |
| [Parameter 2] | [Previous] | [New] | [Impact] | [Services] |

### Configuration Deployment
- **Method**: [How configuration will be deployed]
- **Validation**: [How configuration will be validated]
- **Secrets Management**: [How secrets will be handled]
- **Environment-Specific Values**: [How environment-specific values are managed]

### Configuration Rollback
- **Rollback Method**: [How configuration will be rolled back if needed]
- **Verification**: [How rollback will be verified]
- **Automation**: [Any automation for configuration rollback]
```

### 6. Verification and Monitoring

Implement comprehensive post-deployment verification:

```markdown
## Post-Deployment Verification

### Functional Verification
| Feature/Capability | Verification Method | Expected Result | Status |
|-------------------|---------------------|----------------|--------|
| [Feature 1] | [Method] | [Expected] | ✅/❌ |
| [Feature 2] | [Method] | [Expected] | ✅/❌ |

### Technical Verification
| Component | Metric | Expected | Actual | Status |
|-----------|--------|----------|--------|--------|
| [Component 1] | [Metric] | [Expected] | [Actual] | ✅/❌ |
| [Component 2] | [Metric] | [Expected] | [Actual] | ✅/❌ |

### Monitoring Strategy
- **Critical Metrics**: [Key metrics to monitor]
- **Alert Thresholds**: [When alerts should trigger]
- **Monitoring Duration**: [How long to maintain enhanced monitoring]
- **Responsible Team**: [Who will monitor the system]

### Smoke Test Suite
- **Location**: [Where smoke tests are defined]
- **Execution Method**: [How to run smoke tests]
- **Success Criteria**: [What constitutes successful smoke tests]
- **Failure Response**: [What to do if smoke tests fail]
```

### 7. Rollback Procedure

Document detailed rollback procedures:

```markdown
## Rollback Procedure

### Rollback Triggers
- **Automatic Triggers**: [Conditions for automatic rollback]
- **Manual Triggers**: [Criteria for manual rollback decision]
- **Decision Authority**: [Who can make rollback decisions]
- **Time Constraints**: [Maximum time after deployment to initiate rollback]

### Rollback Process
1. **Service Rollback**
   - **Rollback Order**: [Order of service rollback]
   - **Specific Commands/Procedures**: [Exact commands to execute]
   - **Verification Steps**: [How to verify successful rollback]

2. **Database Rollback**
   - **Schema Rollback**: [How to roll back schema changes]
   - **Data Recovery**: [How to recover or restore data]
   - **Verification**: [How to verify data integrity after rollback]

3. **Configuration Rollback**
   - **Method**: [How to restore previous configuration]
   - **Verification**: [How to verify configuration restoration]

### Post-Rollback Activities
- **Notification**: [Who to notify about the rollback]
- **Analysis**: [How to analyze what went wrong]
- **Recovery Planning**: [Planning the next deployment attempt]
- **Documentation**: [Documenting the rollback for learning]
```

### 8. Cutover and Traffic Management

Manage the transition of traffic to the new version:

```markdown
## Cutover and Traffic Management

### Traffic Transition Strategy
- **Approach**: [e.g., Gradual traffic shift, DNS change, load balancer update]
- **Timing**: [When and how fast traffic will be transitioned]
- **User Impact**: [Expected impact on users during transition]
- **Monitoring**: [How to monitor the traffic transition]

### Load Balancer Configuration
- **Configuration Changes**: [Specific load balancer updates]
- **Health Check Updates**: [Changes to health check configuration]
- **Validation**: [How to validate load balancer configuration]
- **Rollback**: [How to revert load balancer changes]

### DNS Changes
- **DNS Updates**: [Specific DNS changes needed]
- **TTL Considerations**: [DNS TTL settings and implications]
- **Propagation Monitoring**: [How to monitor DNS propagation]
- **Verification**: [How to verify DNS changes]

### CDN/Edge Configuration
- **Cache Invalidation**: [How to handle cache invalidation]
- **Edge Configuration**: [Changes to edge configurations]
- **Propagation Time**: [Expected time for changes to propagate]
- **Verification**: [How to verify edge configuration]
```

## Meta-Systemic Principle Application

### Parsimony in Code Deployment
- Reuse deployment scripts and processes across similar services
- Reference canonical deployment procedures rather than duplicating
- Maintain single source of truth for deployment configuration
- Define environment configurations with inheritance and specificity

Example:
```markdown
### Deployment Script Organization

Deployment scripts are organized following the parsimony principle:

- **Base Scripts**: Common deployment operations defined once in `/deploy/base`
- **Service-Specific Scripts**: Extend base scripts with only service-specific logic
- **Environment Configuration**: Hierarchical configuration with inheritance:
  - `config/base.yaml`: Base configuration for all environments
  - `config/[env].yaml`: Environment-specific overrides
  - `config/[env]/[service].yaml`: Service and environment specific settings

This structure minimizes duplication while allowing appropriate specialization.
```

### Tensegrity in Code Deployment
- Ensure services support each other during deployment
- Design resilient service connections during transition
- Balance deployment responsibilities across teams
- Create bidirectional verification between dependent services

Example:
```markdown
### Service Transition Resilience

The deployment implements tensegrity through:

1. **Backward Compatibility**: All services maintain compatibility with N-1 versions
2. **Feature Detection**: Services detect available capabilities in dependencies
3. **Graceful Degradation**: Core functionality continues when dependent services update
4. **Health Propagation**: Service health status is propagated to dependent services
5. **Coordinated Deployment**: Interdependent services are deployed in balanced batches

This approach ensures system integrity during the transition period while allowing incremental deployment.
```

### Modularity in Code Deployment
- Deploy components with clear boundaries and interfaces
- Use versioned APIs for service communication
- Isolate deployment failures to specific modules
- Enable independent service deployment where possible

Example:
```markdown
### Modular Deployment Architecture

The deployment respects modularity principles through:

1. **Service Boundaries**: Each service is deployed as an independent unit with clear interfaces
2. **Versioned APIs**: All service APIs are versioned to manage compatibility
3. **Deployment Isolation**: Failures in one service deployment don't affect others
4. **Interface Contracts**: Explicit contracts between services maintained during deployment
5. **Independent Scaling**: Services can scale independently based on demand

This architecture allows us to deploy and roll back individual services while maintaining system integrity.
```

### Coherence in Code Deployment
- Follow consistent deployment patterns across services
- Apply standardized verification procedures
- Use shared monitoring and alerting approaches
- Maintain consistent rollback procedures

Example:
```markdown
### Coherent Deployment Patterns

All services follow these consistent deployment patterns:

1. **Pre-Flight Verification**: Standard verification of service readiness
2. **Deployment Method**: Container-based deployment using our standard orchestration
3. **Health Validation**: Consistent health check endpoints and monitoring
4. **Log Format**: Standardized logging format for deployment events
5. **Metric Collection**: Common metrics gathered during and after deployment

This consistency ensures predictable behavior during deployment and simplifies troubleshooting if issues arise.
```

### Clarity in Code Deployment
- Document deployment procedures with concrete examples
- Provide clear success criteria for each deployment step
- Explain deployment decisions and trade-offs
- Use visual aids to clarify complex deployment sequences

Example:
```markdown
### Deployment Documentation Clarity

The deployment documentation provides clarity through:

1. **Explicit Procedures**: Step-by-step instructions with expected outcomes
2. **Command Examples**: Concrete examples of deployment commands
3. **Visual Sequence Diagram**: Clear visualization of deployment order
4. **Decision Documentation**: Explanation of key deployment decisions
5. **Troubleshooting Guides**: Common issues and their resolution

This clarity ensures that all team members understand the deployment process and can respond effectively to issues.
```

### Adaptivity in Code Deployment
- Adapt deployment approach to service characteristics
- Adjust monitoring intensity based on risk
- Vary rollout speed according to confidence
- Apply context-appropriate deployment strategies

Example:
```markdown
### Adaptive Deployment Strategy

The deployment adapts to different contexts:

1. **High-Risk Services**: Canary deployment with extended observation periods
2. **Infrastructure Services**: Blue-green deployment for minimal downtime
3. **User-Facing Services**: Feature flag deployment for controlled exposure
4. **Data Processing Services**: Rolling deployment with careful monitoring
5. **Utility Services**: Simple in-place deployment with basic verification

This adaptive approach applies appropriate deployment methods to each context while maintaining overall system integrity.
```

## Deployment Type-Specific Considerations

### Cloud-Based Deployment
- Focus on immutable infrastructure principles
- Use infrastructure-as-code for environment consistency
- Implement auto-scaling and self-healing mechanisms
- Design for cloud-native resilience and redundancy

Example:
```markdown
## Cloud Deployment Specific Instructions

### Infrastructure Management
- **Terraform Scripts**: Located in `/deploy/terraform`
- **Execution Order**: Follow dependency order in `deploy-order.txt`
- **State Management**: Use remote state in secured bucket
- **Sensitive Data**: Managed through cloud secret store

### Kubernetes Deployment
- **Manifest Location**: `/deploy/k8s`
- **Deployment Order**: Follow the order in `k8s-deploy-order.txt`
- **Helm Charts**: Use parameterized charts with values per environment
- **Service Mesh**: Update Istio configuration for traffic management

### Cloud Provider Specific
- **Region**: Primary deployment to `us-west-2`
- **Failover**: Secondary deployment to `us-east-1` after primary verification
- **Load Balancing**: Update load balancer configuration per `lb-config.yaml`
- **CDN**: Invalidate CDN cache after deployment verification
```

### On-Premises Deployment
- Focus on infrastructure preparation and validation
- Manage hardware resource allocation explicitly
- Plan for maintenance windows and coordination
- Address network and security constraints

Example:
```markdown
## On-Premises Deployment Specific Instructions

### Infrastructure Preparation
- **Server Provisioning**: Ensure target servers meet specifications in `server-specs.md`
- **Network Configuration**: Update firewall rules per `firewall-changes.md`
- **Storage**: Allocate additional storage as specified in `storage-requirements.md`
- **Backup**: Perform full system backup before deployment

### Deployment Execution
- **Maintenance Window**: Scheduled for [Date/Time] with [Duration]
- **Service Shutdown**: Follow shutdown sequence in `shutdown-order.txt`
- **Installation**: Execute installation scripts in `install-scripts/`
- **Service Startup**: Follow startup sequence in `startup-order.txt`

### Post-Deployment
- **Infrastructure Verification**: Execute `verify-infrastructure.sh`
- **Performance Baseline**: Collect new performance baseline
- **Monitoring Updates**: Update monitoring thresholds per `new-thresholds.md`
- **Documentation**: Update system documentation with new configuration
```

### Hybrid Deployment
- Coordinate changes across cloud and on-premises environments
- Ensure consistent configuration between environments
- Manage cross-environment dependencies carefully
- Verify connectivity and data synchronization

Example:
```markdown
## Hybrid Deployment Specific Instructions

### Environment Coordination
- **Deployment Sequence**: Cloud components first, then on-premises
- **Synchronization Points**: Wait for cloud verification before on-premises changes
- **Cross-Environment Configuration**: Update connection parameters in both environments
- **Connectivity Verification**: Test connectivity between environments post-deployment

### Data Synchronization
- **Replication Pause**: Pause data replication during deployment window
- **Schema Alignment**: Ensure consistent schema changes across environments
- **Resynchronization**: Execute data resynchronization procedures post-deployment
- **Consistency Validation**: Verify data consistency across environments

### Recovery Strategy
- **Partial Failure Handling**: Procedures for failures in only one environment
- **Synchronization Recovery**: How to recover cross-environment synchronization
- **Service Degradation**: Acceptable degraded modes during partial deployment
- **Complete Rollback**: Coordinated rollback across both environments
```

## Release Scope-Specific Considerations

### Major Release Deployment
- Comprehensive pre-deployment verification
- Carefully staged deployment with extensive validation
- Extended monitoring period post-deployment
- Full-scale rehearsal in staging environment
- Detailed communication plan and user preparation

### Minor Release Deployment
- Standard pre-deployment verification
- Regular deployment patterns with normal validation
- Standard monitoring period post-deployment
- Validation in staging environment
- Focused communication to affected users

### Patch Release Deployment
- Targeted pre-deployment verification
- Streamlined deployment focused on affected components
- Abbreviated monitoring with focus on fixed issues
- Limited staging validation
- Minimal user communication

### Emergency Release Deployment
- Critical path verification only
- Expedited deployment process
- Intensive monitoring of affected components
- Focused validation on the specific issue
- Just-in-time stakeholder communication

## Code System Deployment Checklist

Before concluding the deployment phase, verify that:

- [ ] All pre-deployment verifications completed successfully
- [ ] Deployment executed according to documented strategy
- [ ] Database changes applied and verified
- [ ] Services deployed in the correct sequence
- [ ] Configuration changes applied correctly
- [ ] Post-deployment verification passed
- [ ] Monitoring confirms system stability
- [ ] Rollback procedures verified
- [ ] Documentation updated with actual deployment results
- [ ] Lessons learned captured for retrospective

## Human-AI Collaboration in Deployment

In our two-person team:

### Human Team Member Focus
- Make critical go/no-go decisions during deployment
- Perform specialized technical actions requiring access
- Evaluate system behavior during deployment
- Communicate with stakeholders about progress
- Monitor system health during critical transitions

### AI Agent Focus
- Track deployment sequence and verification steps
- Provide detailed execution guidance for each step
- Parse and analyze monitoring data
- Document deployment progress and outcomes
- Generate status reports for stakeholders

<important>
Code system deployment is a critical phase where careful execution and verification are essential. Following a structured approach with appropriate validation at each step ensures a successful transition to production while maintaining system integrity.
</important>