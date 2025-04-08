---
description: 
globs: **/code/validation/*.md,**/code/validation/*.mdx,**/releases/*/code_validation.md,**/releases/*/code_validation.mdx
alwaysApply: false
---
---
description: "Code-specific guidance for the validation phase of the release lifecycle"
globs: "**/code/validation/*.md,**/code/validation/*.mdx,**/releases/*/code_validation.md,**/releases/*/code_validation.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code System Validation Guidance

<critical>
This rule provides specialized guidance for the validation phase when the primary system context is code-based system development. Apply these guidelines in conjunction with the core validation phase rules.
</critical>

## Code System Validation Approach

When validating code-based systems, focus on these specialized aspects:

### 1. Technical Validation Strategy

Define a comprehensive validation strategy for code systems:

```markdown
## Technical Validation Strategy

### Testing Pyramid
Implement a balanced testing approach following the testing pyramid:

- **Unit Tests**: 70% of testing effort
  - Test individual functions and classes in isolation
  - Verify component behavior under various conditions
  - Focus on edge cases and error handling

- **Integration Tests**: 20% of testing effort
  - Verify component interactions work correctly
  - Test across module boundaries
  - Validate data flow between components

- **End-to-End Tests**: 10% of testing effort
  - Validate complete user workflows
  - Test system behavior from user perspective
  - Verify business requirements

### Validation Environments
- **Developer Environment**: Unit tests and initial integration tests
- **CI Environment**: Automated test suite execution
- **QA Environment**: Manual testing and exploratory testing
- **Staging Environment**: Performance testing and final validation
- **Production-Like Environment**: Security testing and load testing
```

### 2. Code Quality Validation

Establish comprehensive quality standards:

```markdown
## Code Quality Validation

### Static Analysis
- **Linting**: Enforce coding standards and identify potential issues
  - Tools: [Specify appropriate tools for language/framework]
  - Configuration: [Link to standard configuration]
  - Critical Rules: [List critical rules that must be followed]

- **Complexity Analysis**: Identify overly complex components
  - Cyclomatic Complexity: Maximum 15 per function/method
  - Cognitive Complexity: Maximum 20 per function/method
  - File Size: Maximum 500 lines per file
  - Method Size: Maximum 50 lines per method

- **Dependency Analysis**: Validate dependency structure
  - Check for circular dependencies
  - Verify appropriate dependency direction
  - Identify excessive dependencies

### Code Review
- **Review Checklist**: [Link to standard review checklist]
- **Review Process**: [Brief description of review process]
- **Review Focus Areas**:
  - Design pattern application
  - Error handling approach
  - Security considerations
  - Performance implications
  - Documentation quality
```

### 3. Technical Debt Assessment

Evaluate and manage technical debt:

```markdown
## Technical Debt Assessment

### Debt Identification
- **Planned Debt**: Document technical trade-offs made during development
  - Nature of the debt
  - Reason for accepting debt
  - Impact assessment
  - Proposed remediation timeline

- **Legacy Debt**: Identify pre-existing technical debt affected by changes
  - Impact on current implementation
  - Opportunity assessment for debt reduction
  - Mitigation strategy

- **Unintentional Debt**: Capture debt introduced during implementation
  - Root cause analysis
  - Impact assessment
  - Remediation plan

### Debt Metrics
- **Debt Ratio**: percentage of code needing improvement
- **Debt Cost**: estimated effort to address all debt
- **Debt Density**: number of debt items per component
- **Debt Severity**: weighted impact of identified debt

### Debt Management
- **Remediation Plan**: Schedule for addressing critical debt
- **Prevention Strategy**: Approach to prevent new debt
- **Monitoring Plan**: Process for tracking debt over time
```

### 4. Performance Validation

Verify system performance meets requirements:

```markdown
## Performance Validation

### Performance Test Types
- **Load Testing**: System behavior under expected load
  - Concurrent users: [Target number]
  - Transaction rate: [Target transactions per second]
  - Response time targets: [P95, P99 targets]

- **Stress Testing**: System behavior under extreme conditions
  - Maximum load testing
  - Resource constraint testing
  - Recovery testing

- **Endurance Testing**: System behavior over time
  - Duration: [Typical test duration]
  - Metrics to monitor
  - Degradation thresholds

- **Scalability Testing**: System behavior with increasing load
  - Scaling dimensions to test
  - Scaling thresholds
  - Scaling efficiency metrics

### Performance Metrics
| Metric | Description | Baseline | Target | Actual |
|--------|-------------|----------|--------|--------|
| Response Time (P95) | 95th percentile response time | [Baseline] | [Target] | [Actual] |
| Throughput | Transactions per second | [Baseline] | [Target] | [Actual] |
| Error Rate | Percentage of failed requests | [Baseline] | [Target] | [Actual] |
| Resource Utilization | CPU, memory, disk, network usage | [Baseline] | [Target] | [Actual] |

### Performance Test Scenarios
- **Critical Path Testing**: Primary user workflows
- **Data-Intensive Operations**: Search, reporting, data processing
- **Concurrent Operation Testing**: Simultaneous user activities
- **Background Process Testing**: Batch jobs, scheduled tasks
```

### 5. Security Validation

Ensure system meets security requirements:

```markdown
## Security Validation

### Security Testing Approach
- **Static Application Security Testing (SAST)**
  - Tools: [List SAST tools]
  - Critical vulnerability types to scan for
  - False positive management approach

- **Dynamic Application Security Testing (DAST)**
  - Tools: [List DAST tools]
  - Critical endpoints to test
  - Test authentication requirements

- **Dependency Scanning**
  - Vulnerability database to check against
  - Remediation threshold (e.g., Critical and High issues)
  - Exception management process

- **Manual Security Review**
  - High-risk components requiring manual review
  - Review checklist
  - Expert reviewer requirements

### Security Test Coverage
| Security Control | Testing Method | Coverage | Result |
|------------------|----------------|----------|--------|
| Authentication | [Methods] | [Coverage] | [Result] |
| Authorization | [Methods] | [Coverage] | [Result] |
| Data Protection | [Methods] | [Coverage] | [Result] |
| Input Validation | [Methods] | [Coverage] | [Result] |
| Output Encoding | [Methods] | [Coverage] | [Result] |
| Session Management | [Methods] | [Coverage] | [Result] |

### Security Acceptance Criteria
- Zero critical vulnerabilities
- Zero high vulnerabilities without documented mitigation
- All security requirements explicitly validated
- Security review completed and signed off
```

### 6. Architecture Validation

Assess system architecture and design:

```markdown
## Architecture Validation

### Architectural Compliance
- **Design Principles**: Verify alignment with established principles
  - [List key design principles]
  - Assessment methodology
  - Compliance metrics

- **Architectural Patterns**: Validate correct pattern application
  - [List key architectural patterns]
  - Implementation assessment
  - Pattern adaptation validation

- **Technology Standards**: Confirm compliance with standards
  - [List key technology standards]
  - Standard deviations and justifications
  - Technology compatibility assessment

### System Quality Attributes
| Quality Attribute | Assessment Method | Result | Evidence |
|-------------------|-------------------|--------|----------|
| Scalability | [Method] | [Result] | [Evidence] |
| Maintainability | [Method] | [Result] | [Evidence] |
| Reliability | [Method] | [Result] | [Evidence] |
| Availability | [Method] | [Result] | [Evidence] |
| Security | [Method] | [Result] | [Evidence] |
| Performance | [Method] | [Result] | [Evidence] |
```

### 7. API and Interface Validation

Verify all interfaces and APIs:

```markdown
## API and Interface Validation

### Interface Contract Validation
- **API Specification Compliance**: Verify implementation matches specification
  - OpenAPI/Swagger validation
  - Contract test coverage
  - Documentation accuracy

- **Interface Stability**: Assess backward compatibility
  - Breaking change assessment
  - Versioning strategy compliance
  - Migration path validation

- **Error Handling**: Verify consistent error responses
  - Error code consistency
  - Error message quality
  - Error handling completeness

### Integration Testing
- **Service Integration Tests**: Verify service interactions
  - Service boundary testing
  - Fault tolerance verification
  - Retry mechanism validation

- **External System Integration**: Validate third-party integrations
  - Authentication testing
  - Data exchange verification
  - Failure scenario handling

- **Consumer-Driven Contract Tests**: Verify client requirements
  - Client expectation documentation
  - Contract test implementation
  - Compatibility verification
```

### 8. Data Validation

Verify data handling and integrity:

```markdown
## Data Validation

### Data Integrity
- **CRUD Operation Validation**: Verify data operations
  - Creation validation
  - Retrieval validation
  - Update validation
  - Deletion validation

- **Transaction Management**: Verify transaction handling
  - Atomic operation verification
  - Consistency validation
  - Isolation level testing
  - Durability verification

- **Data Migration**: Validate data migration processes
  - Migration script testing
  - Data integrity verification
  - Rollback capability testing

### Data Quality
- **Validation Rules**: Verify data validation implementation
  - Input validation completeness
  - Business rule enforcement
  - Edge case handling

- **Data Consistency**: Validate cross-system consistency
  - Cross-reference verification
  - Eventual consistency testing
  - Conflict resolution validation
```

## Meta-Systemic Principle Validation for Code Systems

### Parsimony Validation

When validating parsimony in code systems:

```markdown
## Parsimony Validation

### Focus Areas
- **Code Duplication**: Verify minimal code duplication
  - Duplicate code detection results
  - Shared utility usage assessment
  - Common pattern identification

- **Component Reuse**: Assess appropriate reuse of components
  - Library and framework usage
  - Internal component reuse
  - Abstraction effectiveness

- **Knowledge Organization**: Verify effective information organization
  - Documentation structure
  - Comment quality and necessity
  - Self-documenting code practices

### Validation Methods
- Static analysis tools for duplication detection
- Component dependency analysis
- Documentation structure review
- Code organization assessment

### Evidence Collection
- Duplication metrics and trends
- Reuse rate calculation
- Knowledge reference effectiveness examples
```

### Tensegrity Validation

When validating tensegrity in code systems:

```markdown
## Tensegrity Validation

### Focus Areas
- **Component Relationships**: Verify balanced dependencies
  - Bidirectional relationship assessment
  - Dependency load distribution
  - Mutual support patterns

- **Resilience Mechanisms**: Assess failure handling
  - Fault tolerance implementation
  - Graceful degradation capabilities
  - Recovery mechanisms

- **System Balance**: Verify appropriate responsibility distribution
  - Component size and complexity distribution
  - Responsibility allocation assessment
  - Resource utilization balance

### Validation Methods
- Dependency graph analysis
- Failure scenario testing
- Load distribution assessment
- Responsibility mapping review

### Evidence Collection
- Dependency balance metrics
- Resilience test results
- System balance visualization
- Component interaction examples
```

### Modularity Validation

When validating modularity in code systems:

```markdown
## Modularity Validation

### Focus Areas
- **Boundary Integrity**: Verify clear component boundaries
  - Interface definition assessment
  - Encapsulation effectiveness
  - Implementation hiding validation

- **Coupling Assessment**: Verify appropriate coupling level
  - Afferent coupling measurement
  - Efferent coupling measurement
  - Layer isolation verification

- **Component Cohesion**: Assess logical grouping of functionality
  - Single responsibility verification
  - Functional cohesion assessment
  - Component purpose clarity

### Validation Methods
- Static analysis of component boundaries
- Dependency structure matrix analysis
- Cohesion metrics calculation
- Module isolation testing

### Evidence Collection
- Boundary violation examples
- Coupling metric trends
- Cohesion assessment results
- Interface contract documentation
```

### Coherence Validation

When validating coherence in code systems:

```markdown
## Coherence Validation

### Focus Areas
- **Pattern Consistency**: Verify consistent implementation patterns
  - Design pattern application assessment
  - Naming convention adherence
  - Structural consistency verification

- **Standard Compliance**: Assess adherence to defined standards
  - Coding standard compliance
  - Architectural standard alignment
  - Documentation standard adherence

- **Conceptual Integrity**: Verify consistent approach to similar problems
  - Solution approach consistency
  - Terminology consistency
  - Mental model alignment

### Validation Methods
- Pattern implementation review
- Style guide compliance checking
- Conceptual model assessment
- Terminology usage analysis

### Evidence Collection
- Pattern deviation examples
- Standard compliance metrics
- Conceptual consistency evidence
- Terminology consistency assessment
```

### Clarity Validation

When validating clarity in code systems:

```markdown
## Clarity Validation

### Focus Areas
- **Code Readability**: Verify code is easily understood
  - Naming quality assessment
  - Function/method size evaluation
  - Complexity assessment

- **Documentation Quality**: Assess documentation effectiveness
  - Interface documentation completeness
  - Example coverage assessment
  - Use case documentation

- **Intent Expression**: Verify clear expression of purpose
  - Comment quality assessment
  - Self-documenting code practices
  - Design rationale documentation

### Validation Methods
- Readability metrics calculation
- Documentation coverage analysis
- Peer review for clarity assessment
- Example validation

### Evidence Collection
- Readability assessment examples
- Documentation quality metrics
- Clarity improvement suggestions
- Example effectiveness evaluation
```

### Adaptivity Validation

When validating adaptivity in code systems:

```markdown
## Adaptivity Validation

### Focus Areas
- **Extension Points**: Verify appropriate extension mechanisms
  - Plugin architecture assessment
  - Configuration flexibility validation
  - Extension implementation review

- **Context Adaptation**: Assess context-sensitive behavior
  - Configuration-based adaptation
  - Environment-specific behavior
  - Feature flag implementation

- **Evolution Support**: Verify support for future changes
  - Versioning strategy assessment
  - Deprecation approach validation
  - Migration path verification

### Validation Methods
- Extension point testing
- Context variation testing
- Evolution scenario analysis
- Adaptation pattern review

### Evidence Collection
- Extension mechanism examples
- Context adaptation test results
- Evolution readiness assessment
- Adaptivity pattern implementations
```

## Validation Methodology by Component Type

### UI Component Validation

When validating user interface components:

```markdown
## UI Component Validation

### Functional Validation
- User interaction flow testing
- Input validation verification
- Form submission handling
- Error state display
- Edge case behavior

### Usability Validation
- Accessibility compliance (WCAG standards)
- Responsive design verification
- Cross-browser compatibility
- User experience assessment
- Internationalization support

### Performance Validation
- Render time measurement
- Interaction responsiveness
- Animation smoothness
- Memory usage monitoring
- Network efficiency

### Recommended Tools
- Browser developer tools
- Accessibility checkers
- Performance profiling tools
- Visual regression tools
- User experience testing frameworks
```

### API Component Validation

When validating API components:

```markdown
## API Component Validation

### Functional Validation
- Endpoint correctness verification
- Parameter handling validation
- Response structure verification
- Status code appropriateness
- Content type validation

### Contract Validation
- API specification compliance
- Documentation accuracy
- Versioning strategy verification
- Backward compatibility assessment
- Client expectation alignment

### Performance Validation
- Response time measurement
- Throughput assessment
- Concurrency handling
- Resource utilization
- Connection management

### Security Validation
- Authentication mechanism testing
- Authorization rule verification
- Input validation assessment
- Sensitive data handling
- Rate limiting effectiveness

### Recommended Tools
- API testing frameworks
- Contract testing tools
- Load testing tools
- Security scanning tools
- API documentation validators
```

### Data Component Validation

When validating data components:

```markdown
## Data Component Validation

### Functional Validation
- Query correctness verification
- Data manipulation accuracy
- Transaction handling
- Constraint enforcement
- Index effectiveness

### Integrity Validation
- Referential integrity verification
- Validation rule enforcement
- Consistency checking
- Corruption resistance
- Recovery capability

### Performance Validation
- Query performance assessment
- Write performance measurement
- Index effectiveness
- Connection utilization
- Resource consumption

### Security Validation
- Access control verification
- Data encryption assessment
- Audit logging validation
- Sensitive data handling
- Injection prevention

### Recommended Tools
- Database testing frameworks
- Performance monitoring tools
- Data comparison tools
- Schema validation tools
- Security assessment tools
```

## Validation Report Structure for Code Systems

Organize code system validation reports as follows:

```markdown
# Code System Validation Report

## 1. Executive Summary
Brief overview of validation results, issues, and recommendation.

## 2. Functional Validation
Comprehensive assessment of functional requirements.

## 3. Technical Quality Assessment
Code quality, architecture, and technical debt evaluation.

## 4. Non-Functional Validation
Performance, security, scalability assessment.

## 5. Meta-Systemic Principle Validation
Evaluation of principle application effectiveness.

## 6. Component-Specific Validation
Detailed validation results by component type.

## 7. Issue Summary and Resolution
Comprehensive list of issues with resolution plan.

## 8. Release Readiness Assessment
Final assessment and recommendation.

## 9. Appendices
Detailed test results, metrics, and evidence.
```

## Release Scope-Specific Validation for Code Systems

### Major Release Validation for Code Systems
- Comprehensive validation of all components
- Full regression testing suite execution
- Complete security assessment
- Extensive performance testing
- Thorough meta-systemic principle validation
- Architecture and design review
- Comprehensive documentation validation

### Minor Release Validation for Code Systems
- Focused validation on new and changed components
- Targeted regression testing suite
- Security assessment of affected areas
- Performance testing for changed components
- Selected meta-systemic principle validation
- Interface validation for changed APIs
- Documentation validation for new features

### Patch Release Validation for Code Systems
- Focused validation on fixed issues
- Regression testing of affected areas
- Limited security validation if relevant
- Performance validation only if performance-related
- Minimal meta-systemic principle validation
- API contract validation for stability
- Documentation update verification

### Emergency Release Validation for Code Systems
- Critical path validation only
- Essential regression testing
- Focused security validation if security-related
- Performance impact assessment
- Post-deployment comprehensive validation planning
- Minimal documentation verification
- Technical debt documentation for emergency solutions

## Code System Validation Checklist

Before completing code system validation, verify that:

- [ ] All functional requirements have been validated
- [ ] Code quality metrics meet defined standards
- [ ] Performance requirements have been verified
- [ ] Security assessment is complete
- [ ] Meta-systemic principles have been validated
- [ ] Technical debt has been documented
- [ ] Architecture alignment has been verified
- [ ] API contracts have been validated
- [ ] UI components meet usability standards
- [ ] Documentation is accurate and complete

## Human-AI Collaboration for Code System Validation

In our two-person team:

### Human Team Member Focus
- Evaluating subjective quality aspects
- Assessing architectural alignment
- Validating complex business logic
- Making technical tradeoff decisions
- Providing domain expertise

### AI Agent Focus
- Comprehensive test coverage analysis
- Systematic meta-systemic principle validation
- Pattern consistency verification
- Documentation completeness checking
- Comprehensive validation report generation

<important>
Code system validation ensures that implemented functionality works as expected, meets quality standards, and adheres to meta-systemic principles. Thorough validation builds confidence in the release and ensures it's ready for deployment.
</important>