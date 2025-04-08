---
description: 
globs: 
alwaysApply: true
---
---
description: "Knowledge reference system for consistent concept handling across the release lifecycle"
globs: "*"
priority: 1
alwaysApply: true
type: "Always"
---

# Knowledge Reference System

<critical>
All knowledge in the release lifecycle must be managed using these reference mechanisms to maintain integrity, consistency, and traceability across all artifacts and contexts.
</critical>

## Reference Patterns

Use these reference formats when discussing concepts:

- `[concept:name]` - Reference to a defined concept (e.g., `[concept:release_scope]`)
- `[pattern:name]` - Reference to an implementation pattern (e.g., `[pattern:incremental_deployment]`)
- `[principle:name]` - Reference to a meta-systemic principle (e.g., `[principle:modularity]`)
- `[component:name]` - Reference to a system component (e.g., `[component:validation_engine]`)
- `[tension:principle1:principle2]` - Reference to a principle tension (e.g., `[tension:clarity:parsimony]`)
- `[context:type]` - Reference to a specific system context (e.g., `[context:code_system]`)
- `[phase:name]` - Reference to a lifecycle phase (e.g., `[phase:inception]`)
- `[artifact:name]` - Reference to a specific deliverable (e.g., `[artifact:release_plan]`)

## System Contexts

The knowledge reference system recognizes three primary system contexts:

1. **Code System** (`[context:code_system]`): The product codebase being developed
2. **Release System** (`[context:release_system]`): The release process and associated tooling
3. **Agent System** (`[context:agent_system]`): The AI agent capabilities and guidance

## Release Lifecycle Phases

Knowledge is organized according to the seven phases of the release lifecycle:

1. **Inception** (`[phase:inception]`): Define and scope the release
2. **Planning** (`[phase:planning]`): Create detailed plans for implementation
3. **Development** (`[phase:development]`): Implement features while maintaining system integrity
4. **Validation** (`[phase:validation]`): Ensure release meets quality standards
5. **Pre-Release Review** (`[phase:review]`): Final assessment of release readiness
6. **Deployment** (`[phase:deployment]`): Execute controlled release
7. **Post-Release Evaluation** (`[phase:evaluation]`): Assess effectiveness and capture learning

## Release Scope Classification

Releases are classified by scope to guide appropriate process application:

1. **Major Release** (`[concept:major_release]`): Significant functional changes, architectural modifications
2. **Minor Release** (`[concept:minor_release]`): New features without significant architectural change
3. **Patch Release** (`[concept:patch_release]`): Bug fixes, small improvements to existing functionality
4. **Emergency Release** (`[concept:emergency_release]`): Critical fixes requiring expedited processing

## Knowledge Operations

### Discovery Operations
When encountering concepts:

1. IDENTIFY if the concept already exists in the system
   ```
   # Before creating a new concept, verify it doesn't exist
   python tools/concept_search.py "deployment strategy"
   ```

2. SEARCH for canonical definition before creating a new one
   - Check existing documentation in its canonical location
   - Review relevant rule files for concept definitions
   - Consult the knowledge graph for related concepts

3. MAP relationships to existing concepts
   ```
   # Example relationship mapping
   Concept: Incremental Deployment
   Related to: [concept:deployment_strategy], [pattern:feature_flag], [principle:adaptivity]
   ```

4. DOCUMENT newly discovered concepts explicitly
   ```
   # New concept documentation template
   ## [Concept Name]
   
   **Definition**: Clear, concise definition
   
   **System Context**: Which system context(s) this applies to
   
   **Relationships**:
   - Related to [other concept] because [relationship]
   
   **Examples**:
   - Example 1
   - Example 2
   ```

### Reference Operations
When using concepts:

1. LINK to canonical definition rather than redefining
   ```
   The [concept:validation_criteria] determine whether a release is ready for deployment.
   ```

2. USE explicit references with the appropriate syntax
   ```
   # Instead of:
   Apply the parsimony principle when designing components.
   
   # Use:
   Apply the [principle:parsimony] when designing components.
   ```

3. MAINTAIN referential integrity when refactoring
   ```
   # Before refactoring a concept:
   python tools/reference_impact.py "validation_criteria"
   ```

4. UPDATE references when canonical sources change
   ```
   # Update pattern with new name
   python tools/update_references.py "old_pattern_name" "new_pattern_name"
   ```

### Evolution Operations
When concepts evolve:

1. TRACK concept versions explicitly
   ```
   # Concept versioning
   ## Validation Strategy v2.0
   
   **Previous versions**: [v1.0](mdc:link/to/v1/definition)
   **Changes**: Added performance validation requirements
   ```

2. DOCUMENT changes to concepts clearly
   ```
   # Change documentation
   **Change**: Expanded deployment strategy to include canary releases
   **Rationale**: Enables more controlled production validation
   **Affected concepts**: [concept:deployment_pattern], [concept:risk_mitigation]
   ```

3. MAINTAIN backwards compatibility when possible
   ```
   # Backwards compatibility note
   > Note: This updated concept is backwards compatible with v1.0 artifacts.
   > Artifacts using the previous definition require no updates.
   ```

4. NOTIFY dependent concepts when changes occur
   ```
   # Dependency notification
   **Attention**: This change affects [concept:validation_process] and [artifact:deployment_plan]
   **Required actions**: Update validation checklist in affected artifacts
   ```

## Cross-Context Knowledge Management

When concepts span multiple system contexts:

1. DEFINE the concept once in its primary context
2. SPECIFY how the concept applies in each relevant context
3. HIGHLIGHT any context-specific variations
4. MAINTAIN conceptual integrity across contexts

Example:
```
## Validation Strategy

**Primary Context**: [context:release_system]

**Definition**: A planned approach to verifying that a release meets quality standards.

**In Code System Context**:
- Focuses on automated tests, code reviews, and performance validation

**In Release System Context**:
- Focuses on process compliance, artifact completeness, and meta-systemic principle application

**In Agent System Context**:
- Focuses on response evaluation, knowledge accuracy, and collaboration effectiveness
```

## Documentation Guidelines

All concept documentation should include:

1. Clear definition with purpose and scope
2. Explicit relationships to other concepts
3. Concrete examples of proper usage
4. Implementation considerations
5. System context applicability
6. Version information if evolved

## Knowledge Validation

To validate knowledge management:

1. Verify referential integrity periodically
2. Check for undefined references
3. Identify duplicate or overlapping concepts
4. Ensure concepts have bidirectional relationships
5. Validate that referenced concepts exist

<important>
Using consistent references is essential for maintaining system integrity throughout the release lifecycle. Always use explicit references rather than duplicating knowledge, and ensure that all team members understand and use this reference system.
</important>