---
description: 
globs: **/validation/*.md,**/validation/*.mdx,**/releases/*/context.md,**/releases/*/context.mdx
alwaysApply: false
---
---
description: "Context-sensitive validation process for meta-systemic principles"
globs: "**/validation/*.md,**/validation/*.mdx,**/releases/*/context.md,**/releases/*/context.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Context-Sensitive Validation

<critical>
Apply this validation process to ensure principles are applied appropriately based on specific system contexts. Proper context detection and validation ensures that meta-systemic principles are applied with the appropriate intensity and balance for each situation.
</critical>

## Context Validation Framework

This framework provides a systematic approach to validating that meta-systemic principles are applied with appropriate intensity and balance based on the specific system context.

### Context Evaluation Process

1. **Detect Context**: Identify the relevant system context factors
2. **Determine Expected Balance**: Map the context to appropriate principle emphasis
3. **Validate Application**: Verify principles are applied with context-appropriate intensity
4. **Resolve Tensions**: Validate that principle tensions are resolved appropriately for the context

## Context Detection Criteria

### System Maturity Assessment

```yaml
maturity_contexts:
  early_exploration:
    indicators:
      - "Frequent major directional changes"
      - "Minimal established patterns"
      - "Evolving requirements and scope"
      - "Experimental implementations"
    principle_priorities:
      - "Clarity (high)"
      - "Adaptivity (high)"
      - "Modularity (moderate)"
      - "Coherence, Parsimony, Tensegrity (lower)"
  
  active_development:
    indicators:
      - "Clear direction with ongoing evolution"
      - "Established core patterns"
      - "Stable requirements with refinements"
      - "Growing codebase with active changes"
    principle_priorities:
      - "Clarity (high)"
      - "Modularity (high)"
      - "Tensegrity (high)"
      - "Adaptivity, Coherence (moderate)"
      - "Parsimony (moderate)"
  
  maintenance:
    indicators:
      - "Stable system with incremental changes"
      - "Well-established patterns"
      - "Minimal new features, mostly refinements"
      - "Focus on reliability and optimization"
    principle_priorities:
      - "Coherence (high)"
      - "Parsimony (high)"
      - "Tensegrity (high)"
      - "Modularity (high)"
      - "Clarity (moderate)"
      - "Adaptivity (low)"
  
  legacy:
    indicators:
      - "Limited active development"
      - "Historical patterns that may need preservation"
      - "Focus on stability and compatibility"
      - "Technical debt considerations"
    principle_priorities:
      - "Coherence (high)"
      - "Parsimony (high)"
      - "Clarity (high)"
      - "Modularity, Tensegrity (moderate)"
      - "Adaptivity (low)"
```

### Architectural Approach Assessment

```yaml
architectural_contexts:
  monolithic:
    indicators:
      - "Single deployable unit"
      - "Shared codebase and data model"
      - "In-process communication"
      - "Centralized management"
    principle_priorities:
      - "Coherence (high)"
      - "Clarity (high)"
      - "Modularity (internal boundaries)"
      - "Tensegrity (internal relationships)"
  
  modular:
    indicators:
      - "Clear component boundaries"
      - "Well-defined interfaces"
      - "Logical separation of concerns"
      - "Possibility of separate deployment"
    principle_priorities:
      - "Modularity (high)"
      - "Tensegrity (high)"
      - "Parsimony (high)"
      - "Coherence (across boundaries)"
  
  microservices:
    indicators:
      - "Independent deployable services"
      - "Service-specific data stores"
      - "Network communication"
      - "Distributed management"
    principle_priorities:
      - "Modularity (service boundaries)"
      - "Parsimony (avoid duplication)"
      - "Clarity (explicit contracts)"
      - "Adaptivity (service evolution)"
  
  hybrid:
    indicators:
      - "Mix of architectural patterns"
      - "Transitional architecture"
      - "Mixed communication patterns"
      - "Varied management approaches"
    principle_priorities:
      - "Clarity (high - boundary documentation)"
      - "Adaptivity (high - context variation)"
      - "Modularity (boundary enforcement)"
      - "Tensegrity (cross-boundary relationships)"
```

### Team Structure Assessment

```yaml
team_contexts:
  solo_developer:
    indicators:
      - "Single developer responsible for codebase"
      - "Minimal formal documentation needs"
      - "Rapid iteration capability"
      - "Knowledge centralized"
    principle_priorities:
      - "Parsimony (high)"
      - "Coherence (high)"
      - "Adaptivity (high)"
      - "Clarity (focused on future understanding)"
  
  small_team:
    indicators:
      - "2-7 developers with shared context"
      - "Informal communication channels"
      - "Collaborative decision making"
      - "Shared knowledge base"
    principle_priorities:
      - "Clarity (high)"
      - "Coherence (high)"
      - "Adaptivity (moderate)"
      - "Parsimony (focused organization)"
  
  multiple_teams:
    indicators:
      - "Multiple teams working on different components"
      - "Formal communication channels"
      - "Coordinated decision making"
      - "Distributed knowledge"
    principle_priorities:
      - "Modularity (high - clear boundaries)"
      - "Clarity (high - explicit documentation)"
      - "Tensegrity (high - team relationships)"
      - "Parsimony (shared understanding)"
  
  distributed:
    indicators:
      - "Geographically or organizationally distributed teams"
      - "Asynchronous communication"
      - "Formalized processes"
      - "Highly distributed knowledge"
    principle_priorities:
      - "Clarity (very high)"
      - "Modularity (very high)"
      - "Coherence (high)"
      - "Parsimony (canonical references)"
```

## System Type-Specific Context Assessment

### Code System Context Assessment

When assessing code system context:

1. **System Purpose**:
   - User-facing application
   - Infrastructure component
   - Internal tool
   - Shared library

2. **Technical Stack**:
   - Programming languages
   - Frameworks
   - Technology ecosystem
   - Deployment environment

3. **Domain Complexity**:
   - Business logic complexity
   - Domain model sophistication
   - Regulatory requirements
   - Integration complexity

4. **Performance Requirements**:
   - Throughput expectations
   - Latency constraints
   - Scalability needs
   - Resource limitations

### Release System Context Assessment

When assessing release process context:

1. **Release Frequency**:
   - Continuous delivery
   - Scheduled releases
   - On-demand releases
   - Infrequent major releases

2. **Process Maturity**:
   - Ad-hoc processes
   - Defined processes
   - Measured processes
   - Optimized processes

3. **Regulatory Requirements**:
   - Compliance needs
   - Audit requirements
   - Approval workflows
   - Documentation standards

4. **Team Distribution**:
   - Co-located teams
   - Partially distributed
   - Fully distributed
   - Cross-organizational

### Agent System Context Assessment

When assessing agent system context:

1. **Agent Role**:
   - Development assistant
   - Documentation assistant
   - Design collaborator
   - Process guide

2. **Collaboration Model**:
   - One-time interactions
   - Ongoing collaboration
   - Specialized tasks
   - General assistance

3. **Knowledge Requirements**:
   - Domain-specific knowledge
   - Technical knowledge
   - Process knowledge
   - General knowledge

4. **Interaction Patterns**:
   - Sequential interactions
   - Iterative refinement
   - Parallel work streams
   - Continuous availability

## Context-Appropriate Validation Criteria

### Adaptivity Balance

```yaml
adaptivity_validation:
  early_exploration:
    appropriate_patterns:
      - "Experimenting with multiple approaches"
      - "Lightweight patterns with easy evolution"
      - "Context-specific adaptations"
      - "Limited standardization"
    inappropriate_patterns:
      - "Rigid standardization"
      - "Heavyweight frameworks"
      - "Excessive abstraction layers"
      - "Premature optimization"
    validation_metrics:
      - name: "Exploration freedom"
        target: "> 80% of design choices allow evolution"
      - name: "Standardization burden"
        target: "< 20% of code bound by rigid standards"
  
  active_development:
    appropriate_patterns:
      - "Flexible but consistent patterns"
      - "Adaptable interfaces"
      - "Documented variations"
      - "Component-level standardization"
    inappropriate_patterns:
      - "Chaotic inconsistency"
      - "Over-generic interfaces"
      - "Undocumented variations"
      - "Rigid global standards"
    validation_metrics:
      - name: "Pattern adaptability"
        target: "> 70% of patterns allow for context variation"
      - name: "Variation documentation"
        target: "> 90% of variations have documented rationale"
  
  maintenance:
    appropriate_patterns:
      - "Controlled evolution paths"
      - "Well-documented standards"
      - "Careful pattern refinement"
      - "Backward compatibility"
    inappropriate_patterns:
      - "Frequent pattern overhauls"
      - "Ad-hoc variations"
      - "Inconsistent application"
      - "Breaking changes without migration"
    validation_metrics:
      - name: "Evolution control"
        target: "> 95% of changes follow documented evolution paths"
      - name: "Standard adherence"
        target: "> 90% compliance with established patterns"
  
  legacy:
    appropriate_patterns:
      - "Careful adaptation of existing patterns"
      - "Focus on backward compatibility"
      - "Isolated refinements"
      - "Documented adaptation strategies"
    inappropriate_patterns:
      - "Full rewrites without necessity"
      - "Pattern changes without migration"
      - "Modern patterns applied inappropriately"
      - "Inconsistent modernization"
    validation_metrics:
      - name: "Compatibility preservation"
        target: "> 98% of changes maintain compatibility"
      - name: "Adaptation documentation"
        target: "100% of adaptations have documented rationale"
```

### Principle Tension Resolution Validation

```yaml
tension_resolution:
  coherence_vs_adaptivity:
    early_exploration:
      appropriate_resolution: "Favor adaptivity over strict coherence"
      validation_criteria:
        - "Patterns are documented but not rigidly enforced"
        - "Variations are allowed with documented rationale"
        - "Focus on learning rather than standardization"
    
    maintenance:
      appropriate_resolution: "Favor coherence with controlled adaptation"
      validation_criteria:
        - "Strong pattern governance"
        - "Adaptations require explicit justification"
        - "Changes propagated systematically across the system"
  
  modularity_vs_tensegrity:
    microservices:
      appropriate_resolution: "Strong modularity with explicit relationships"
      validation_criteria:
        - "Well-defined service boundaries"
        - "Explicit integration contracts"
        - "Service relationship documentation"
    
    monolithic:
      appropriate_resolution: "Balanced internal boundaries with strong relationships"
      validation_criteria:
        - "Logical separation with clear communication paths"
        - "Shared resources managed through explicit interfaces"
        - "Strong relationship tracking between components"
  
  parsimony_vs_clarity:
    distributed_teams:
      appropriate_resolution: "Favor clarity even with some duplication"
      validation_criteria:
        - "Comprehensive documentation with examples"
        - "References to canonical sources"
        - "Self-contained component documentation"
    
    solo_developer:
      appropriate_resolution: "Favor parsimony with targeted clarity"
      validation_criteria:
        - "Efficient organization with minimal duplication"
        - "Clarity focused on complex or critical areas"
        - "Canonical sources for all major concepts"
```

## Release Scope-Specific Context Validation

Adapt validation approaches based on release scope:

### Major Release Context Validation
- Comprehensive context assessment
- Detailed principle balance analysis
- Full validation of all tensions
- Explicit documentation of context adaptations
- Focus on architectural alignment

### Minor Release Context Validation
- Focused context assessment for affected areas
- Targeted principle balance analysis
- Validation of relevant tensions
- Documentation of significant adaptations
- Focus on pattern consistency

### Patch Release Context Validation
- Limited context assessment for changed components
- Verification of principle applications in changes
- Focus on coherence and compatibility
- Documentation of any necessary adaptations
- Emphasis on minimizing context variations

### Emergency Release Context Validation
- Rapid context assessment for critical changes
- Focus on critical principle applications
- Emphasis on clarity and coherence
- Document context exceptions for future resolution
- Targeted post-deployment context validation

## Context Validation Workflow

When conducting a context-sensitive validation:

```yaml
workflow:
  context_assessment:
    - "Identify system maturity indicators"
    - "Evaluate architectural approach"
    - "Assess team structure and distribution"
    - "Determine dominant context factors"
  
  principle_balance_validation:
    - "Map context to expected principle emphasis"
    - "Review actual principle application"
    - "Identify misaligned principle application"
    - "Validate tension resolution approaches"
  
  adaptation_validation:
    - "Verify context-appropriate patterns"
    - "Check if variations have documented rationale"
    - "Validate that standards match context needs"
    - "Ensure adaptations maintain system integrity"
  
  documentation:
    - "Record context assessment findings"
    - "Document principle balance evaluation"
    - "Note tension resolution approaches"
    - "Create context-specific recommendations"
```

## Context Validation Report Template

```markdown
# Context-Sensitive Validation Report

## Context Assessment
- **System Maturity**: [early_exploration, active_development, maintenance, legacy]
- **Architectural Approach**: [monolithic, modular, microservices, hybrid]
- **Team Structure**: [solo_developer, small_team, multiple_teams, distributed]
- **Dominant Context**: [most influential context factor]

## Principle Balance Analysis
- **Expected Principle Emphasis**: [ordered list based on context]
- **Actual Principle Application**: [observed emphasis]
- **Balance Assessment**: [aligned or misaligned]
- **Specific Misalignments**: [details of inappropriate emphasis]

## Adaptation Validation
- **Pattern Appropriateness**: [context-appropriate or inappropriate]
- **Variation Documentation**: [well-documented or undocumented]
- **Standard Alignment**: [matches context needs or misaligned]
- **System Integrity**: [maintained or compromised]

## Tension Resolution Assessment
- **Key Tensions**: [list of principle tensions observed]
- **Resolution Approaches**: [how tensions were resolved]
- **Context Appropriateness**: [appropriate or inappropriate for context]
- **Improvement Recommendations**: [context-specific resolution strategies]

## Recommendations
Context-specific recommendations for improving principle application balance.
```

## Context Classification Examples

### Example 1: Early-Stage Startup Website

```markdown
## Context Classification

- **System Type**: Code System
- **System Maturity**: Early Exploration
- **Architectural Approach**: Modular
- **Team Structure**: Small Team
- **Complexity**: Medium
- **Criticality**: Medium
- **Time Sensitivity**: High

## Principle Emphasis
Given this context, the appropriate principle emphasis should be:

1. **Primary Focus**: Clarity, Adaptivity
2. **Secondary Focus**: Modularity
3. **Lighter Touch**: Coherence, Parsimony, Tensegrity

## Key Tension Resolutions
- **Coherence vs. Adaptivity**: Favor adaptivity to enable rapid exploration
- **Parsimony vs. Clarity**: Favor clarity to support team understanding
- **Modularity vs. Tensegrity**: Establish core boundaries while allowing flexible relationships
```

### Example 2: Enterprise Banking System

```markdown
## Context Classification

- **System Type**: Code System
- **System Maturity**: Maintenance
- **Architectural Approach**: Hybrid (Modular Monolith)
- **Team Structure**: Multiple Teams
- **Complexity**: High
- **Criticality**: Very High
- **Time Sensitivity**: Medium

## Principle Emphasis
Given this context, the appropriate principle emphasis should be:

1. **Primary Focus**: Coherence, Modularity, Tensegrity
2. **Secondary Focus**: Parsimony, Clarity
3. **Lighter Touch**: Adaptivity

## Key Tension Resolutions
- **Coherence vs. Adaptivity**: Favor coherence with careful, documented adaptations
- **Parsimony vs. Clarity**: Balance with comprehensive documentation and clear references
- **Modularity vs. Tensegrity**: Maintain strict boundaries with well-defined interfaces
```

### Example 3: Release Process Refinement

```markdown
## Context Classification

- **System Type**: Release System
- **System Maturity**: Active Development
- **Process Style**: Defined
- **Team Structure**: Distributed
- **Complexity**: Medium
- **Criticality**: High
- **Time Sensitivity**: Medium

## Principle Emphasis
Given this context, the appropriate principle emphasis should be:

1. **Primary Focus**: Clarity, Parsimony, Coherence
2. **Secondary Focus**: Adaptivity, Modularity
3. **Lighter Touch**: Tensegrity

## Key Tension Resolutions
- **Coherence vs. Adaptivity**: Balance with clear process standards and documented variations
- **Parsimony vs. Clarity**: Favor clarity for distributed team understanding
- **Modularity vs. Tensegrity**: Create clear phase boundaries with explicit handoffs
```

## Common Context Misclassifications

Avoid these common context assessment errors:

1. **Maturity Misclassification**:
   - Treating experimental systems as mature
   - Applying early-exploration patterns to maintenance systems
   - Ignoring legacy characteristics of old systems

2. **Architectural Mismatch**:
   - Applying microservice patterns to monoliths
   - Using monolithic approaches for distributed systems
   - Ignoring hybrid characteristics

3. **Team Structure Oversimplification**:
   - Treating multi-team projects as small team
   - Ignoring distribution factors
   - Overestimating knowledge sharing

4. **Complexity Underestimation**:
   - Treating complex systems as simple
   - Ignoring domain complexity
   - Undervaluing criticality

## Human-AI Team Collaboration for Context Validation

In our two-person team:

### Human Team Member Responsibilities

1. **Context Judgment**:
   - Provide experience-based context assessment
   - Judge relative importance of context factors
   - Make final context classification decisions
   - Evaluate subjective context characteristics

2. **Appropriate Adaptations**:
   - Determine necessary variations from standards
   - Judge appropriateness of adaptations
   - Prioritize principle tensions for resolution
   - Validate practicality of recommendations

### AI Agent Responsibilities

1. **Systematic Assessment**:
   - Identify context indicators systematically
   - Document context characteristics
   - Map context to appropriate principles
   - Track context consistency

2. **Pattern Recognition**:
   - Detect misaligned principle applications
   - Identify pattern inconsistencies
   - Compare to similar known contexts
   - Generate context-appropriate recommendations

<important>
Context validation is essential for effective meta-systemic architecture. Always validate that principles are applied with appropriate intensity based on the specific context rather than applying them uniformly across all situations.
</important>