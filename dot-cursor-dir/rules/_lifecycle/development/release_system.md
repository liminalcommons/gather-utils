---
description: 
globs: **/.cursor/rules/**/*.mdc,**/process/**/*.md,**/process/**/*.mdx,**/templates/**/*.md,**/templates/**/*.mdx
alwaysApply: false
---
---
description: "Release-specific guidance for the development phase of the release lifecycle"
globs: "**/.cursor/rules/**/*.mdc,**/process/**/*.md,**/process/**/*.mdx,**/templates/**/*.md,**/templates/**/*.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Release System Development Guidance

<critical>
This rule provides specialized guidance for the development phase when the primary system context is release process evolution. Apply these guidelines in conjunction with the core development phase rules to ensure effective implementation of process changes while maintaining meta-systemic principles.
</critical>

## Release System Implementation Approach

When implementing changes to the release process:

### 1. Process Foundation

Begin by establishing the proper foundation for process changes:

```markdown
## Process Foundation

### Current State Assessment
- Document the existing process in detail
- Identify pain points and improvement opportunities
- Establish baseline metrics for process effectiveness
- Map current process to meta-systemic principles
- Understand stakeholder needs and perspectives

### Process Change Scope
- Define clear boundaries for the process changes
- Identify affected phases and artifacts
- Document integration points with other processes
- Specify changes to roles and responsibilities
- Establish transition approach from old to new process

### Reference Implementation
- Identify successful patterns from existing processes
- Review process documentation for guidance
- Understand how meta-systemic principles apply
- Examine related process implementations
```

### 2. Incremental Implementation Strategy

Break down implementation into clear, manageable increments:

```markdown
## Incremental Implementation Strategy

### Foundation Increment
- Establish process framework and core concepts
- Create initial templates and guidance
- Define key metrics and validation approach
- Focus on process integrity and coherence
- Document core process workflow

### Core Functionality Increment
- Implement primary process components and artifacts
- Create detailed workflow and phase transitions
- Develop meta-systemic rule implementation
- Establish primary validation criteria
- Document detailed process steps

### Integration Increment
- Connect process with existing systems and workflows
- Implement transitions between old and new processes
- Create compatibility layers where needed
- Address integration challenges
- Document integration points and dependencies

### Refinement Increment
- Optimize process efficiency
- Address edge cases and exceptions
- Refine templates and guidance
- Enhance documentation with examples
- Create additional supporting materials
```

### 3. Template Development

Create effective templates and artifacts:

```markdown
## Template Development

### Template Design Principles
- Design templates that enforce meta-systemic principles
- Create clear structure with logical organization
- Include guidance text within templates
- Provide examples for complex sections
- Design for appropriate adaptability to context

### Template Types
- **Phase-specific templates**: For each lifecycle phase
- **Artifact templates**: For specific deliverables
- **Process templates**: For process execution guidance
- **Validation templates**: For quality verification
- **Review templates**: For approval and feedback

### Template Documentation
- Provide clear usage instructions
- Document template structure and sections
- Explain when to use each template
- Include examples of completed templates
- Document adaptation guidelines for different contexts
```

### 4. Rule Development

Implement Cursor rules effectively:

```markdown
## Rule Development

### Rule Design Principles
- Create rules that enforce meta-systemic principles
- Design rules with appropriate scope and application
- Include clear guidance and examples
- Establish consistent rule structure
- Create appropriate rule triggers

### Rule Types
- **Core principle rules**: Fundamental meta-systemic concepts
- **Inference rules**: Principle-specific application guidance
- **Lifecycle phase rules**: Phase-specific guidance
- **Artifact rules**: Artifact-specific guidance
- **Validation rules**: Quality verification guidance

### Rule Documentation
- Document rule purpose and application
- Explain intended behavior and outcomes
- Include examples of proper application
- Document rule relationships and dependencies
- Provide guidance for rule adaptation
```

### 5. Process Documentation

Create comprehensive process documentation:

```markdown
## Process Documentation

### Documentation Types
- **Process Overview**: High-level explanation of process purpose and flow
- **Phase Guides**: Detailed guidance for each lifecycle phase
- **Role Documentation**: Responsibilities for each role
- **Workflow Documentation**: Step-by-step process instructions
- **Transition Guide**: How to move from old to new process

### Documentation Structure
- Clear organization with logical flow
- Explicit guidance with examples
- Visual aids (diagrams, flowcharts)
- Cross-references to related documentation
- Appropriate level of detail for the audience

### Documentation Maintenance
- Version control for documentation
- Change tracking and history
- Update process for documentation
- Review and validation procedures
- Feedback mechanism for improvements
```

### 6. Process Validation

Verify process effectiveness:

```markdown
## Process Validation

### Validation Approaches
- **Walkthrough**: Step-by-step review of the process
- **Simulation**: Apply process to hypothetical scenarios
- **Pilot Implementation**: Test process on limited scope
- **Metrics Analysis**: Measure process effectiveness
- **Stakeholder Feedback**: Gather input from users

### Validation Criteria
- Effectiveness in achieving process goals
- Efficiency in time and resources
- Clarity and understandability
- Adherence to meta-systemic principles
- Appropriate adaptability to context

### Validation Documentation
- Document validation approach and results
- Record identified issues and resolutions
- Capture metrics and benchmarks
- Document stakeholder feedback
- Create validation report with findings
```

## Meta-Systemic Principle Application

### Parsimony
- Define process concepts once and reference elsewhere
- Create consistent templates that avoid duplication
- Establish canonical process documentation
- Reuse effective patterns across the process

Example:
```markdown
## Process Documentation Approach

This process documentation follows the parsimony principle by:

1. Defining each process concept in a single location
2. Using references to canonical definitions throughout documentation
3. Creating templates that reference shared components
4. Establishing standard sections that appear consistently

For example, rather than redefining meta-systemic principles in each document, we reference the canonical definitions in the [Core Meta-Systemic Principles](mdc:../_kernel/00_principles.mdc) document and provide context-specific application guidance.
```

### Tensegrity
- Balance responsibilities across process phases
- Create supportive relationships between artifacts
- Ensure phases both provide and receive value
- Design resilient processes with appropriate handoffs

Example:
```markdown
## Process Phase Relationships

The planning phase demonstrates tensegrity by:

1. Receiving validated requirements from the inception phase
2. Providing detailed implementation guidance to the development phase
3. Supporting the validation phase by defining verification criteria
4. Receiving feedback from previous releases via the evaluation phase

Each phase both depends on and provides value to other phases, creating a balanced system of mutual support.
```

### Modularity
- Create clear boundaries between process phases
- Define explicit interfaces between components
- Encapsulate phase-specific details
- Design for independent evolution of process components

Example:
```markdown
## Process Modularity

The release process demonstrates modularity through:

1. Clearly defined phase boundaries with explicit entry/exit criteria
2. Standard interfaces for phase transitions (artifacts, approvals)
3. Encapsulation of phase-specific activities and responsibilities
4. Independence of phase implementation details

This modularity allows phases to evolve independently while maintaining system integrity through well-defined interfaces.
```

### Coherence
- Apply consistent patterns across the process
- Use standard terminology and definitions
- Maintain structural similarity for related artifacts
- Create predictable workflows and transitions

Example:
```markdown
## Process Coherence

The release documentation system demonstrates coherence by:

1. Using consistent document structures across all artifacts
2. Applying standard naming conventions for artifacts and activities
3. Maintaining consistent workflow patterns between phases
4. Using standardized metadata across all documentation

This coherence makes the process predictable and understandable, reducing cognitive load for users.
```

### Clarity
- Provide explicit guidance with examples
- Create clear, unambiguous documentation
- Include visual representations where helpful
- Document process rationale and intent

Example:
```markdown
## Documentation Clarity

The release plan template demonstrates clarity through:

1. Explicit section guidance with concrete examples
2. Clear explanation of purpose for each section
3. Visual workflow diagrams showing process flow
4. Example snippets for complex sections

For instance, the dependency mapping section includes this example:

```
## Dependency Graph

### Critical Path
The following tasks form the critical path for this release:
1. Task 1.1 → Task 2.3 → Task 3.2 → Task 4.1

### Dependency Matrix
| Task | Depends On | Required For |
|------|------------|--------------|
| 1.1  | None       | 1.2, 2.3     |
| 1.2  | 1.1        | 3.1          |
```
```

### Adaptivity
- Design process for different release contexts
- Create appropriate variations for different release types
- Allow context-specific process adaptations
- Document adaptation patterns and rationale

Example:
```markdown
## Process Adaptivity

The release process demonstrates adaptivity by:

1. Scaling process detail based on release scope
2. Providing specialized guidance for different release types
3. Allowing appropriate streamlining for emergency releases
4. Documenting context-specific adaptations with rationale

For example, the validation phase adapts to release scope:
- **Major releases**: Comprehensive validation of all aspects
- **Minor releases**: Focused validation on changed components
- **Patch releases**: Targeted validation of specific fixes
- **Emergency releases**: Critical path validation only
```

## Process Development by Lifecycle Phase

### Inception Phase Development

When evolving the inception phase:

1. **Requirement Definition Processes**:
   - Design templates for capturing requirements
   - Create processes for requirement validation
   - Implement guidance for scope definition
   - Develop context assessment frameworks

2. **Release Classification Processes**:
   - Implement classification criteria and workflows
   - Create decision frameworks for release typing
   - Develop guidance for borderline cases
   - Document classification implications

3. **Stakeholder Alignment Processes**:
   - Design approval workflows and templates
   - Create stakeholder identification frameworks
   - Implement communication strategies
   - Develop consensus-building approaches

### Planning Phase Development

When evolving the planning phase:

1. **Task Breakdown Processes**:
   - Design work breakdown structures
   - Create estimation frameworks
   - Implement dependency mapping tools
   - Develop validation criteria for completeness

2. **Resource Allocation Processes**:
   - Design capacity planning tools
   - Create role assignment frameworks
   - Implement skill matching processes
   - Develop resource conflict resolution approaches

3. **Risk Management Processes**:
   - Design risk identification frameworks
   - Create impact and likelihood assessment tools
   - Implement mitigation planning processes
   - Develop risk monitoring approaches

### Development Phase Development

When evolving the development phase:

1. **Implementation Tracking Processes**:
   - Design progress tracking frameworks
   - Create status reporting templates
   - Implement milestone monitoring processes
   - Develop early warning systems for issues

2. **Quality Management Processes**:
   - Design quality gates and criteria
   - Create review workflows and templates
   - Implement technical debt tracking
   - Develop continuous improvement processes

3. **Knowledge Sharing Processes**:
   - Design documentation standards
   - Create knowledge transfer workflows
   - Implement collaboration frameworks
   - Develop learning capture processes

### Validation Phase Development

When evolving the validation phase:

1. **Validation Planning Processes**:
   - Design validation strategy frameworks
   - Create test planning templates
   - Implement coverage analysis tools
   - Develop risk-based testing approaches

2. **Validation Execution Processes**:
   - Design validation workflows and procedures
   - Create defect tracking and resolution processes
   - Implement validation reporting frameworks
   - Develop regression testing approaches

3. **Meta-Systemic Validation Processes**:
   - Design principle verification frameworks
   - Create principle balance assessment tools
   - Implement tension resolution tracking
   - Develop meta-process validation approaches

### Pre-Release Review Phase Development

When evolving the pre-release review phase:

1. **Readiness Assessment Processes**:
   - Design readiness criteria frameworks
   - Create verification checklists
   - Implement readiness scoring tools
   - Develop evidence collection processes

2. **Decision-Making Processes**:
   - Design go/no-go decision frameworks
   - Create decision documentation templates
   - Implement stakeholder alignment processes
   - Develop conditional approval mechanisms

3. **Release Documentation Processes**:
   - Design release note templates
   - Create documentation packaging workflows
   - Implement knowledge transfer processes
   - Develop deployment guide standards

### Deployment Phase Development

When evolving the deployment phase:

1. **Deployment Planning Processes**:
   - Design deployment strategy frameworks
   - Create deployment sequence planning tools
   - Implement resource coordination processes
   - Develop communication planning templates

2. **Execution Processes**:
   - Design deployment workflow management
   - Create verification checkpoint processes
   - Implement status tracking and reporting
   - Develop issue management procedures

3. **Rollback Processes**:
   - Design rollback decision frameworks
   - Create rollback procedure templates
   - Implement recovery validation processes
   - Develop post-incident analysis approaches

### Post-Release Evaluation Phase Development

When evolving the post-release evaluation phase:

1. **Metrics Collection Processes**:
   - Design metrics framework
   - Create data collection processes
   - Implement analysis and reporting tools
   - Develop trend analysis approaches

2. **Retrospective Processes**:
   - Design retrospective frameworks
   - Create lesson capture templates
   - Implement improvement tracking tools
   - Develop knowledge integration processes

3. **Feedback Loop Processes**:
   - Design process improvement frameworks
   - Create action item tracking tools
   - Implement effectiveness measurement
   - Develop process evolution approaches

## Template Types and Patterns

### Document Templates

When creating documentation templates:

1. **Structure Elements**:
   - Create consistent header/footer formats
   - Design standard section patterns
   - Implement metadata requirements
   - Develop cross-reference standards

2. **Content Guidance**:
   - Include inline guidance text
   - Add example content for reference
   - Create context-specific variations
   - Develop formatting standards

3. **Template Documentation**:
   - Document template purpose and usage
   - Explain when to use each template
   - Provide examples of completed templates
   - Document adaptation guidelines

### Process Templates

When creating process templates:

1. **Workflow Elements**:
   - Design activity sequence patterns
   - Create role responsibility matrices
   - Implement decision point frameworks
   - Develop input/output specifications

2. **Execution Guidance**:
   - Include process execution instructions
   - Add context-specific variations
   - Create exception handling procedures
   - Develop communication protocols

3. **Template Documentation**:
   - Document process flow and rationale
   - Explain process adaptation guidelines
   - Provide examples of successful execution
   - Document integration with other processes

### Rule Templates

When creating rule templates:

1. **Rule Structure**:
   - Design consistent rule formats
   - Create standard section patterns
   - Implement priority and application logic
   - Develop glob pattern guidelines

2. **Content Guidance**:
   - Include enforcement mechanism guidance
   - Add example content for reference
   - Create context-specific variations
   - Develop formatting standards

3. **Template Documentation**:
   - Document rule development workflow
   - Explain rule testing and validation
   - Provide examples of effective rules
   - Document rule maintenance procedures

## Release Scope-Specific Considerations

### Major Release Process Development

For major release process development:

- Comprehensive documentation of process changes
- Detailed transition plans for process adoption
- Extensive stakeholder communication and training
- Full process validation across contexts
- Thorough integration with existing processes

### Minor Release Process Development

For minor release process development:

- Focused documentation for process enhancements
- Targeted updates to affected artifacts and templates
- Appropriate stakeholder notification and guidance
- Validation of specific process changes
- Integration with affected process components

### Patch Release Process Development

For patch release process development:

- Precise updates to specific process elements
- Minimal template and artifact changes
- Focused stakeholder notification
- Targeted validation of process fixes
- Careful integration with existing process

### Emergency Release Process Development

For emergency release process development:

- Simplified process documentation focused on critical path
- Essential template updates only
- Key stakeholder communication
- Validation of critical process elements
- Minimal disruption to existing processes

## Process Implementation Quality Checklist

Before concluding the development phase, verify that:

- [ ] All planned process changes are implemented
- [ ] Templates and artifacts are complete and validated
- [ ] Rules are configured and tested
- [ ] Documentation is comprehensive and clear
- [ ] Transition plans are established
- [ ] Stakeholder communication is prepared
- [ ] Process metrics are defined
- [ ] Training materials are developed
- [ ] Integration with existing processes is verified
- [ ] Meta-systemic principles are applied appropriately

## Human-AI Collaboration in Process Development

In our two-person team:

### Human Team Member Focus
- Making key process design decisions
- Providing organizational context and constraints
- Evaluating stakeholder needs and feedback
- Identifying potential adoption challenges
- Approving process changes and artifacts

### AI Agent Focus
- Generating consistent documentation and templates
- Ensuring meta-systemic principle application
- Maintaining coherence across process artifacts
- Identifying potential process issues or gaps
- Suggesting process optimizations and improvements

<important>
Release system development requires careful balance between process rigor and practical usability. Focus on creating clear, adaptable processes that guide users effectively while maintaining meta-systemic integrity. Invest in comprehensive documentation and templates that make the process easy to follow and adapt to different contexts.
</important>