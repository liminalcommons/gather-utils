---
description: 
globs: 
alwaysApply: true
---
---
description: "Context detection framework for appropriate principle application throughout the release lifecycle"
globs: "*"
priority: 1
alwaysApply: true
type: "Always"
---

# Context Detection Framework

<critical>
Principle application must be adjusted based on contextual factors. Analyze the context before applying principles and adapt their application intensity accordingly. This framework enables consistent yet flexible application of meta-systemic principles across different contexts.
</critical>

## Multi-Dimensional Context Analysis

When approaching any release activity, analyze these four key context dimensions:

1. **System Type**: Which system is being modified (code, release process, agent)
2. **Release Scope**: The scope of changes being made (major, minor, patch, emergency)
3. **System Factors**: Characteristics of the system (maturity, architecture, team structure)
4. **Activity Factors**: Nature of the current activity (complexity, criticality, time sensitivity)

## System Type Context

### Code System
- **Definition**: Changes to the product codebase
- **Indicators**:
  - Modifying source code files
  - Updating tests
  - Changing APIs or data models
  - Modifying system configuration
- **Example Files**: `src/**/*.{py,js,ts}`, `tests/**/*`

### Release System
- **Definition**: Changes to the release process itself
- **Indicators**:
  - Modifying Cursor rules
  - Updating templates
  - Changing process documentation
  - Modifying validation criteria
- **Example Files**: `.cursor/rules/**/*.mdc`, `docs/process/**/*.md`

### Agent System
- **Definition**: Changes to AI agent capabilities
- **Indicators**:
  - Updating agent guidelines
  - Modifying prompt templates
  - Changing knowledge representation
  - Altering interaction patterns
- **Example Files**: `docs/agent/**/*.md`, `prompts/**/*.md`

## Release Scope Context

### Major Release
- **Definition**: Significant functional changes, architectural modifications
- **Indicators**:
  - New major features
  - Breaking API changes
  - Architectural changes
  - Database schema changes
  - Version number format: X.0.0
- **Typical Timeframe**: 2-6 months

### Minor Release
- **Definition**: New features without significant architectural change
- **Indicators**:
  - Non-breaking new features
  - Enhancements to existing functionality
  - Limited scope changes
  - Version number format: 0.X.0
- **Typical Timeframe**: 2-6 weeks

### Patch Release
- **Definition**: Bug fixes, small improvements to existing functionality
- **Indicators**:
  - Bug fixes
  - Performance improvements
  - Documentation updates
  - No new features
  - Version number format: 0.0.X
- **Typical Timeframe**: 1-2 weeks

### Emergency Release
- **Definition**: Critical fixes requiring expedited processing
- **Indicators**:
  - Critical bugs affecting users
  - Security vulnerabilities
  - Data integrity issues
  - Requires immediate deployment
- **Typical Timeframe**: Hours to days

## System Factors

### System Maturity
- **Early Exploration**: Experimental, rapidly changing
- **Active Development**: Evolving with established patterns
- **Maintenance**: Stable with incremental changes
- **Legacy**: Established, high stability requirements

### Architectural Approach
- **Monolithic**: Single integrated application
- **Modular**: Component-based with clear boundaries
- **Microservices**: Distributed with service boundaries
- **Hybrid**: Mixed architectural patterns

### Team Structure
- **Solo**: One human and one AI agent
- **Small Team**: 2-5 team members
- **Multiple Teams**: Several teams with coordination needs
- **Distributed**: Geographically or organizationally distributed

## Activity Factors

### Complexity Level
- **Low**: Straightforward, well-understood changes
- **Medium**: Moderately complex changes with some unknowns
- **High**: Complex changes with significant unknowns
- **Very High**: Highly complex changes with numerous dependencies

### Criticality Level
- **Low**: Non-critical changes with minimal risk
- **Medium**: Important changes with moderate risk
- **High**: Critical changes with significant risk
- **Very High**: Mission-critical changes with extreme risk

### Time Sensitivity
- **Low**: No urgent timeline
- **Medium**: Normal release timeline
- **High**: Accelerated timeline needed
- **Very High**: Urgent, immediate action required

## Context Detection Process

Follow this process to determine the appropriate context for any release activity:

1. **Identify System Type**:
   - Examine the files being changed
   - Determine primary system context
   - Note any cross-system impacts

2. **Classify Release Scope**:
   - Review the nature of changes
   - Determine appropriate release classification
   - Consider version numbering impact

3. **Assess System Factors**:
   - Evaluate system maturity
   - Consider architectural approach
   - Account for team structure

4. **Determine Activity Factors**:
   - Gauge complexity level
   - Assess criticality
   - Evaluate time sensitivity

5. **Document Context Classification**:
   ```
   # Context Classification
   - System Type: [Code|Release|Agent]
   - Release Scope: [Major|Minor|Patch|Emergency]
   - System Maturity: [Early|Active|Maintenance|Legacy]
   - Architectural Approach: [Monolithic|Modular|Microservices|Hybrid]
   - Team Structure: [Solo|Small|Multiple|Distributed]
   - Complexity: [Low|Medium|High|Very High]
   - Criticality: [Low|Medium|High|Very High]
   - Time Sensitivity: [Low|Medium|High|Very High]
   ```

## Context-Based Principle Application

Adjust principle application intensity based on the detected context:

```yaml
context_mapping:
  # System Type Mappings
  code_system:
    emphasis:
      modularity: high
      coherence: high
      clarity: high
      parsimony: moderate
      tensegrity: moderate
      adaptivity: moderate

  release_system:
    emphasis:
      parsimony: high
      coherence: high
      adaptivity: high
      modularity: moderate
      clarity: moderate
      tensegrity: moderate

  agent_system:
    emphasis:
      clarity: high
      adaptivity: high
      tensegrity: high
      coherence: moderate
      modularity: moderate
      parsimony: moderate

  # Release Scope Mappings
  major_release:
    emphasis:
      modularity: high
      tensegrity: high
      coherence: high
      clarity: high
      parsimony: high
      adaptivity: moderate

  minor_release:
    emphasis:
      coherence: high
      clarity: high
      modularity: high
      parsimony: moderate
      tensegrity: moderate
      adaptivity: moderate
      
  patch_release:
    emphasis:
      coherence: very high
      clarity: high
      modularity: high
      parsimony: moderate
      tensegrity: low
      adaptivity: low
      
  emergency_release:
    emphasis:
      clarity: very high
      coherence: high
      modularity: moderate
      parsimony: low
      tensegrity: low
      adaptivity: low

  # System Maturity Mappings
  early_exploration:
    emphasis:
      clarity: high
      adaptivity: high
      modularity: moderate
      coherence: low
      parsimony: low
      tensegrity: low

  active_development:
    emphasis:
      modularity: high
      clarity: high
      coherence: moderate
      tensegrity: moderate
      adaptivity: moderate
      parsimony: moderate

  maintenance:
    emphasis:
      coherence: high
      parsimony: high
      modularity: high
      clarity: moderate
      tensegrity: moderate
      adaptivity: low

  legacy:
    emphasis:
      coherence: high
      parsimony: high
      clarity: high
      modularity: moderate
      tensegrity: low
      adaptivity: low
```

## Cross-Dimensional Context Analysis

When multiple context dimensions indicate different principle emphasis:

1. **Primary Context**: Give highest weight to System Type and Release Scope
2. **Secondary Context**: Consider System Factors for adjustments
3. **Tertiary Context**: Use Activity Factors for fine-tuning
4. **Principle Calculation**: Average emphasis across dimensions, with weighting for priority

Example calculation:
```
Context:
- System Type: Code System (modularity: high)
- Release Scope: Patch Release (coherence: very high)
- System Maturity: Maintenance (coherence: high)
- Activity: High Criticality (clarity: high)

Principle Emphasis Calculation:
1. modularity = (high + high + high + moderate) ÷ 4 = high
2. coherence = (high + very high + high + moderate) ÷ 4 = high
3. clarity = (high + high + moderate + high) ÷ 4 = high
4. parsimony = (moderate + moderate + high + low) ÷ 4 = moderate
5. tensegrity = (moderate + low + moderate + low) ÷ 4 = low-moderate
6. adaptivity = (moderate + low + low + low) ÷ 4 = low
```

## Context Validation

To validate context detection:

1. **Context Consistency**: Ensure context is classified consistently
2. **Appropriate Mapping**: Verify that principle emphasis matches context
3. **Context Documentation**: Document context in release artifacts
4. **Cross-Context Integrity**: Maintain consistency across related contexts

## Human-AI Collaboration for Context Detection

In our two-person team:

1. **Human Role**:
   - Make final context classification decisions
   - Resolve ambiguous context indicators
   - Validate context-appropriate principle emphasis
   - Provide experience-based judgment

2. **AI Agent Role**:
   - Identify initial context indicators
   - Propose context classification
   - Calculate principle emphasis
   - Document context assessment

<important>
Always state the detected context explicitly when providing guidance and justify principle application based on this context. Use the multi-dimensional approach to ensure balanced principle application that adapts to specific circumstances while maintaining system integrity.
</important>