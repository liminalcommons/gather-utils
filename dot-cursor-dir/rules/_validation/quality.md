---
description: 
globs: globs: "**/validation/*.md,**/validation/*.mdx,**/releases/*/validation.md,**/releases/*/validation.mdx"
alwaysApply: false
---
---
description: "Quality validation process for meta-systemic principles throughout the release lifecycle"
globs: "**/validation/*.{md,mdx},**/releases/*/validation.{md,mdx}"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Quality Validation Process

<critical>
Apply this validation process to ensure consistent application of meta-systemic principles across all system contexts throughout the release lifecycle.
</critical>

## Core Validation Framework

This framework provides a systematic approach to validating the application of meta-systemic principles. Use this process when reviewing code, documentation, process changes, or agent enhancements.

### Validation Process

1. **Identify Context**: Determine the system context and which principles are most relevant
2. **Apply Criteria**: Use the principle-specific criteria to evaluate quality
3. **Document Findings**: Record validation results with specific recommendations
4. **Prioritize Improvements**: Categorize improvements by impact and effort

## Context-Specific Validation Approach

Adapt validation based on the system context:

### Code System Validation

When validating code changes:
- Focus on component boundaries and interfaces
- Verify pattern consistency across similar components
- Check for knowledge duplication and references
- Validate bidirectional relationships between components
- Ensure clear documentation with examples

### Release System Validation

When validating process changes:
- Verify process consistency across release types
- Check for clear phase boundaries and interfaces
- Validate knowledge references across process documentation
- Ensure appropriate adaptations for different release scopes
- Verify clear examples for all process steps

### Agent System Validation

When validating agent enhancements:
- Check for consistent guidance across contexts
- Verify clear knowledge domain boundaries
- Validate balanced human-AI responsibilities
- Ensure clear examples of expected behaviors
- Check for appropriate context adaptation

## Principle-Specific Validation Criteria

### Parsimony Validation

```yaml
validation:
  principle: "parsimony"
  description: "Each concept defined once and referenced elsewhere"
  key_indicators:
    - "Canonical definitions are established and referenced"
    - "Similar code/content is consolidated"
    - "Information is not unnecessarily duplicated"
    - "References are used to maintain knowledge relationships"
  metrics:
    - name: "Duplication rate"
      target: "< 3% duplicate content"
      measurement: "Lines of duplicate content / Total lines"
    - name: "Reference validity"
      target: "> 98% valid references"
      measurement: "Valid references / Total references"
    - name: "Canonical definition coverage"
      target: "> 95% of concepts have canonical definitions"
      measurement: "Concepts with canonical definitions / Total concepts"
  validation_questions:
    - "Is there a single source of truth for each concept?"
    - "Are references used instead of duplication?"
    - "Do similar patterns use shared implementations?"
    - "Is knowledge organized efficiently?"
  improvement_guidance:
    - "Identify and consolidate duplicated content"
    - "Establish canonical sources for frequently used concepts"
    - "Convert duplication to references to canonical sources"
    - "Maintain a knowledge map of concept relationships"
  
  context_specific_guidance:
    code_system:
      - "Check for duplicated code patterns"
      - "Verify shared utility functions for common operations"
      - "Ensure consistent type definitions across components"
    release_system:
      - "Check for duplicated process definitions"
      - "Verify canonical reference for process concepts"
      - "Ensure templates are reused where appropriate"
    agent_system:
      - "Check for duplicated guidance across contexts"
      - "Verify canonical knowledge references"
      - "Ensure consistent pattern definitions"
```

### Tensegrity Validation

```yaml
validation:
  principle: "tensegrity"
  description: "Elements both support and are supported by others"
  key_indicators:
    - "Components have balanced dependency relationships"
    - "Bidirectional value exchange exists between components"
    - "No component is critically overloaded"
    - "Connections between components are resilient"
  metrics:
    - name: "Bidirectional relationship rate"
      target: "> 90% of relationships are bidirectional"
      measurement: "Bidirectional relationships / Total relationships"
    - name: "Dependency balance ratio"
      target: "< 5:1 max dependency ratio"
      measurement: "Max dependencies on one component / Average dependencies per component"
    - name: "Component connection resilience"
      target: "> 90% of connections have graceful degradation"
      measurement: "Resilient connections / Total connections"
  validation_questions:
    - "Do components provide value to each other?"
    - "Are dependencies balanced across the system?"
    - "Can components adapt to changes in their dependencies?"
    - "Does the system maintain integrity even when parts change?"
  improvement_guidance:
    - "Identify one-way dependencies and create reciprocal value"
    - "Redistribute responsibilities from overloaded components"
    - "Strengthen connection points with resilience patterns"
    - "Document explicit relationships between components"
  
  context_specific_guidance:
    code_system:
      - "Check for balanced service dependencies"
      - "Verify graceful degradation when dependencies fail"
      - "Ensure components provide mutual value"
    release_system:
      - "Check for balanced relationships between process phases"
      - "Verify that no phase is disproportionately burdened"
      - "Ensure phases support each other with clear handoffs"
    agent_system:
      - "Check for balanced human-AI responsibilities"
      - "Verify complementary capabilities"
      - "Ensure knowledge transfer in both directions"
```

### Modularity Validation

```yaml
validation:
  principle: "modularity"
  description: "Clear boundaries with well-defined interfaces"
  key_indicators:
    - "Component boundaries are well-defined"
    - "Interfaces are explicit and complete"
    - "Implementation details are properly encapsulated"
    - "Components can evolve independently"
  metrics:
    - name: "Interface clarity"
      target: "> 95% of interfaces have explicit contracts"
      measurement: "Interfaces with explicit contracts / Total interfaces"
    - name: "Encapsulation integrity"
      target: "< 5% of implementation details exposed"
      measurement: "Exposed implementation details / Total implementation details"
    - name: "Component coupling"
      target: "< 20% of components have tight coupling"
      measurement: "Tightly coupled components / Total components"
  validation_questions:
    - "Are component boundaries clearly defined?"
    - "Are interfaces explicit and complete?"
    - "Are implementation details properly encapsulated?"
    - "Can components evolve independently?"
  improvement_guidance:
    - "Define explicit interfaces for all components"
    - "Encapsulate implementation details within boundaries"
    - "Use dependency injection to reduce coupling"
    - "Document component boundaries and responsibilities"
  
  context_specific_guidance:
    code_system:
      - "Check for interface contracts between components"
      - "Verify encapsulation of internal implementation"
      - "Ensure components can be tested in isolation"
    release_system:
      - "Check for clear phase boundaries in the process"
      - "Verify explicit entry/exit criteria for each phase"
      - "Ensure process phases can evolve independently"
    agent_system:
      - "Check for well-defined knowledge domain boundaries"
      - "Verify clear interfaces for human-AI interaction"
      - "Ensure agent guidance can evolve without disruption"
```

### Coherence Validation

```yaml
validation:
  principle: "coherence"
  description: "Consistent patterns across implementation"
  key_indicators:
    - "Similar problems use similar solutions"
    - "Naming conventions are consistent"
    - "Implementation patterns are applied uniformly"
    - "Code organization follows consistent structure"
  metrics:
    - name: "Pattern consistency"
      target: "> 90% pattern consistency across codebase"
      measurement: "Consistent pattern instances / Total pattern instances"
    - name: "Naming convention adherence"
      target: "> 95% adherence to naming conventions"
      measurement: "Compliant identifiers / Total identifiers"
    - name: "Structural consistency"
      target: "> 90% consistent structure across components"
      measurement: "Components with standard structure / Total components"
  validation_questions:
    - "Are similar patterns implemented consistently?"
    - "Do naming conventions follow a clear standard?"
    - "Is code organization consistent across the codebase?"
    - "Are architectural patterns applied uniformly?"
  improvement_guidance:
    - "Document standard patterns for common problems"
    - "Establish and enforce naming conventions"
    - "Refactor inconsistent implementations to match standards"
    - "Create templates for new components"
  
  context_specific_guidance:
    code_system:
      - "Check for consistent coding patterns across components"
      - "Verify naming convention adherence"
      - "Ensure architectural patterns are applied consistently"
    release_system:
      - "Check for consistent process patterns across release types"
      - "Verify consistent artifact structure"
      - "Ensure terminology is used consistently"
    agent_system:
      - "Check for consistent interaction patterns"
      - "Verify consistency in knowledge representation"
      - "Ensure guidance follows established patterns"
```

### Clarity Validation

```yaml
validation:
  principle: "clarity"
  description: "Unambiguous guidance with examples"
  key_indicators:
    - "Documentation is clear and comprehensive"
    - "Complex logic includes explanatory comments"
    - "Concepts are explained with concrete examples"
    - "Design decisions include rationale"
  metrics:
    - name: "Documentation coverage"
      target: "> 90% of code and interfaces documented"
      measurement: "Documented elements / Total elements"
    - name: "Example coverage"
      target: "> 85% of concepts have examples"
      measurement: "Concepts with examples / Total concepts"
    - name: "Design rationale documentation"
      target: "> 80% of design decisions include rationale"
      measurement: "Decisions with rationale / Total decisions"
  validation_questions:
    - "Is documentation clear and comprehensive?"
    - "Are complex concepts explained with examples?"
    - "Is the rationale for design decisions documented?"
    - "Would a new team member understand the system easily?"
  improvement_guidance:
    - "Add examples for complex concepts and APIs"
    - "Document rationale for non-obvious decisions"
    - "Add explanatory comments for complex logic"
    - "Create onboarding guides for new team members"
  
  context_specific_guidance:
    code_system:
      - "Check for clear API documentation with examples"
      - "Verify comments for complex algorithms"
      - "Ensure design decisions include rationale"
    release_system:
      - "Check for clear process documentation with examples"
      - "Verify each step has clear guidance"
      - "Ensure process changes include rationale"
    agent_system:
      - "Check for clear interaction examples"
      - "Verify guidance includes concrete scenarios"
      - "Ensure capabilities are clearly documented"
```

### Adaptivity Validation

```yaml
validation:
  principle: "adaptivity"
  description: "Context-sensitive evolution while maintaining system integrity"
  key_indicators:
    - "Existing patterns are understood before changes"
    - "Implementations adapt to context appropriately"
    - "Core intent is preserved during evolution"
    - "Standards balanced with contextual needs"
  metrics:
    - name: "Contextual adaptation quality"
      target: "> 90% of adaptations preserve core intent"
      measurement: "Adaptations preserving intent / Total adaptations"
    - name: "Pattern discovery rate"
      target: "> 95% of changes account for existing patterns"
      measurement: "Changes with pattern discovery / Total changes"
    - name: "Context-appropriate variation"
      target: "> 85% of variations have documented rationale"
      measurement: "Justified variations / Total variations"
  validation_questions:
    - "Are existing patterns understood before changes?"
    - "Do adaptations preserve the core intent?"
    - "Are variations justified by contextual needs?"
    - "Is there a balance between standardization and adaptation?"
  improvement_guidance:
    - "Document pattern discovery process"
    - "Record rationale for contextual adaptations"
    - "Define core intents that must be preserved"
    - "Establish guidelines for appropriate variation"
  
  context_specific_guidance:
    code_system:
      - "Check that implementations adapt to different use cases"
      - "Verify variations have documented justification"
      - "Ensure core functionality is preserved across contexts"
    release_system:
      - "Check that processes adapt to different release scopes"
      - "Verify process variations are documented"
      - "Ensure core process integrity across adaptations"
    agent_system:
      - "Check that guidance adapts to different scenarios"
      - "Verify adaptation preserves consistent behavior"
      - "Ensure knowledge application is context-appropriate"
```

## Release Scope-Specific Validation Requirements

Adjust validation intensity based on release scope:

### Major Release Validation
- Comprehensive validation across all principles
- Full coverage of all components affected
- Extensive documentation review
- Cross-component integration validation
- Complete validation report required

### Minor Release Validation
- Focused validation on affected areas
- Emphasis on coherence and modularity
- Targeted documentation review
- Component-level validation
- Abbreviated validation report acceptable

### Patch Release Validation
- Targeted validation of specific changes
- Emphasis on coherence and clarity
- Minimal documentation review
- Focused validation of affected functionality
- Brief validation summary acceptable

### Emergency Release Validation
- Critical path validation only
- Emphasis on clarity and coherence
- Essential documentation review
- Focused validation of the fix
- Post-deployment comprehensive validation required

## Validation Workflow

When conducting a quality validation:

```yaml
workflow:
  preparation:
    - "Define validation scope (component, module, system)"
    - "Identify relevant context factors"
    - "Select applicable validation criteria"
    - "Define validation goals"
  
  execution:
    - "Analyze artifacts against criteria"
    - "Record observations for each principle"
    - "Measure against quantitative metrics"
    - "Identify patterns of strength and weakness"
  
  documentation:
    - "Summarize findings by principle"
    - "Document specific issues with examples"
    - "Calculate metric values"
    - "Prioritize improvement opportunities"
  
  follow_up:
    - "Create improvement plan"
    - "Assign responsibilities for improvements"
    - "Schedule follow-up validation"
    - "Track metrics over time"
```

## Validation Report Template

```markdown
# Quality Validation Report

## Validation Context
- **Scope**: [component, module, or system]
- **Date**: [validation date]
- **Validator**: [validator name]
- **System Context**: [code_system, release_system, or agent_system]
- **Release Scope**: [major, minor, patch, or emergency]

## Executive Summary
Brief overview of findings and key recommendations.

## Principle-Specific Findings

### Parsimony
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

### Tensegrity
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

### Modularity
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

### Coherence
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

### Clarity
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

### Adaptivity
- **Score**: [metric values]
- **Strengths**: [observed strengths]
- **Areas for Improvement**: [specific issues]
- **Recommendations**: [actionable improvements]

## Improvement Plan
Prioritized list of actions with responsible parties and timelines.

## Next Validation
Scheduled date for follow-up validation.
```

## Human-AI Collaboration for Validation

In our two-person team:

1. **Human Role**:
   - Make final validation judgments
   - Assess subjective quality factors
   - Provide experience-based evaluation
   - Prioritize improvements

2. **AI Agent Role**:
   - Calculate objective metrics
   - Identify pattern violations
   - Generate initial validation report
   - Track validation coverage

<important>
Validation is a constructive process focused on continuous improvement, not criticism. Always connect validation findings to concrete, actionable recommendations that are appropriate for the specific system context and release scope.
</important>