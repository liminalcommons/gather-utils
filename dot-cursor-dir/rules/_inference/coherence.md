---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Coherence inference patterns for consistent implementation"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Coherence Inference Engine

<critical>
Apply these coherence patterns to maintain consistent implementation patterns across the system.
</critical>

## Detection Patterns

Scan for these coherence violation signals:

```yaml
coherence_violations:
  - pattern: "Inconsistent naming conventions"
    action: "Standardize naming according to project conventions"
    example: "Mixed camelCase and snake_case within the same codebase"
  
  - pattern: "Different approaches to similar problems"
    action: "Identify the canonical pattern and align implementations"
    example: "Multiple ways of handling async operations throughout the codebase"
  
  - pattern: "Isolated pattern evolutions without propagation"
    action: "Update all instances of a pattern when it evolves"
    example: "New error handling pattern used only in new code"
  
  - pattern: "Framework or paradigm inconsistency"
    action: "Maintain consistent architecture and paradigm choices"
    example: "Mixing functional and class-based approaches arbitrarily"
  
  - pattern: "Inconsistent file and directory organization"
    action: "Apply consistent structure across the codebase"
    example: "Different structuring patterns across modules"
```

## Application Rules

### Rule 1: Consistent Naming Conventions
When working with identifiers:

```typescript
// BEFORE - Inconsistent naming
function getUserData() { /* ... */ }
function process_payment() { /* ... */ }
class userProfile { /* ... */ }
const API_ENDPOINT = "/api";
let activeSession = null;

// AFTER - Consistent naming (example using camelCase convention)
function getUserData() { /* ... */ }
function processPayment() { /* ... */ }
class UserProfile { /* ... */ }
const apiEndpoint = "/api";
let activeSession = null;
```

### Rule 2: Consistent Pattern Application
When implementing recurring functionality:

```typescript
// BEFORE - Inconsistent async patterns
// Some functions use callbacks
function loadData(callback) {
  fetchData((error, data) => {
    callback(error, data);
  });
}

// Some use promises
function processData(data) {
  return new Promise((resolve, reject) => {
    // Processing
    resolve(result);
  });
}

// Some use async/await
async function displayData() {
  const data = await fetchDataSomehow();
  // Display logic
}

// AFTER - Consistent async pattern (standardized on async/await)
async function loadData() {
  try {
    return await fetchData();
  } catch (error) {
    throw new DataLoadError("Failed to load data", error);
  }
}

async function processData(data) {
  // Processing
  return result;
}

async function displayData() {
  try {
    const data = await loadData();
    const processed = await processData(data);
    // Display logic
  } catch (error) {
    handleError(error);
  }
}
```

### Rule 3: Consistent Error Handling
When managing errors:

```typescript
// BEFORE - Inconsistent error handling approaches
function serviceA() {
  try {
    // Logic
  } catch (e) {
    console.error(e);
    return null;
  }
}

function serviceB() {
  try {
    // Logic
  } catch (e) {
    throw new Error(`Service B failed: ${e.message}`);
  }
}

// AFTER - Consistent error handling pattern
class ServiceError extends Error {
  constructor(message, originalError, context) {
    super(message);
    this.originalError = originalError;
    this.context = context;
    this.name = this.constructor.name;
  }
}

function serviceA() {
  try {
    // Logic
  } catch (e) {
    throw new ServiceError(
      "Service A operation failed",
      e,
      { service: "A", operation: "process" }
    );
  }
}

function serviceB() {
  try {
    // Logic
  } catch (e) {
    throw new ServiceError(
      "Service B operation failed",
      e,
      { service: "B", operation: "process" }
    );
  }
}
```

### Rule 4: Consistent File/Directory Structure
When organizing code:

```
// BEFORE - Inconsistent module organization
/src
  /users
    user-controller.js
    user-service.js
  /products
    ProductController.js
    services/
      product-service.js
  /auth
    /controllers
      auth.js
    /services
      authentication-service.js

// AFTER - Consistent module organization
/src
  /users
    /controllers
      user-controller.js
    /services
      user-service.js
  /products
    /controllers
      product-controller.js
    /services
      product-service.js
  /auth
    /controllers
      auth-controller.js
    /services
      auth-service.js
```

## Context-Sensitive Application

Adjust coherence application based on context:

```yaml
coherence_contexts:
  high_coherence:
    applies_to: [mature_system, large_team, production_system]
    strategies:
      - "Comprehensive pattern documentation and enforcement"
      - "Systematic pattern propagation when they evolve"
      - "Regular coherence audits with automated validation"
      - "Pattern governance across teams"
  
  moderate_coherence:
    applies_to: [active_development, growing_system]
    strategies:
      - "Document key patterns with examples"
      - "Evolve patterns explicitly with adoption plans"
      - "Periodic coherence reviews during development"
      - "Focus on critical patterns first"
  
  low_coherence:
    applies_to: [early_exploration, prototype]
    strategies:
      - "Identify emergent patterns for future standardization"
      - "Maintain local coherence within modules"
      - "Document pattern experiments with rationale"
      - "Plan for increased coherence as patterns stabilize"
```

## Coherence Metrics

Measure coherence application using these metrics:

```yaml
metrics:
  pattern_consistency:
    description: "Consistency of pattern implementation across components"
    calculation: "Consistent pattern instances / Total pattern instances * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
  
  naming_convention_adherence:
    description: "Adherence to naming conventions"
    calculation: "Compliant identifiers / Total identifiers * 100"
    thresholds:
      good: "> 95%"
      acceptable: "85-95%"
      concerning: "< 85%"
  
  structural_consistency:
    description: "Consistency of code organization"
    calculation: "Components with standard structure / Total components * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
```

## Coherence Anti-Patterns

Avoid these common coherence mistakes:

```yaml
anti_patterns:
  pattern_divergence:
    description: "Different implementations of the same concept"
    examples:
      - "Multiple error handling approaches"
      - "Different state management patterns"
    remediation:
      - "Identify the canonical pattern"
      - "Document the pattern explicitly"
      - "Refactor divergent implementations"
      - "Create migration guides for legacy code"
  
  convention_drift:
    description: "Inconsistent application of naming and structure conventions"
    examples:
      - "Mixed naming styles"
      - "Inconsistent file organization"
    remediation:
      - "Document conventions explicitly"
      - "Implement automated linting"
      - "Create convention migration guides"
      - "Prioritize critical areas for alignment"
  
  isolated_evolution:
    description: "Patterns evolve in isolation without system-wide updates"
    examples:
      - "New code uses updated patterns while old code remains unchanged"
      - "Different teams use different versions of the same pattern"
    remediation:
      - "Create pattern evolution processes"
      - "Document pattern versions and transitions"
      - "Implement systematic updates across the codebase"
      - "Measure and track pattern adoption"
```

## Code System Coherence Patterns

When applying coherence to code systems:

1. **Naming Conventions**:
   - Use consistent casing conventions (camelCase, PascalCase, snake_case)
   - Apply consistent naming patterns for similar concepts
   - Maintain consistent terminology across the codebase
   - Follow language-specific naming conventions

2. **Code Structure**:
   - Organize files and directories consistently
   - Apply consistent module organization
   - Structure similar components in similar ways
   - Maintain consistent import patterns

3. **Design Patterns**:
   - Apply the same design patterns for similar problems
   - Document canonical patterns for common challenges
   - Evolve patterns systematically across the codebase
   - Maintain pattern integrity during refactoring

4. **Testing Approaches**:
   - Follow consistent testing patterns
   - Structure tests similarly across components
   - Apply consistent validation approaches
   - Maintain naming consistency in test code

5. **Error Handling**:
   - Implement consistent error management
   - Use the same error hierarchy across components
   - Apply consistent error reporting patterns
   - Handle similar errors in similar ways

## Release System Coherence Patterns

When applying coherence to release processes:

1. **Document Structure**:
   - Maintain consistent artifact structures
   - Apply the same templates across release types
   - Use consistent terminology in process documentation
   - Organize content consistently across artifacts

2. **Process Flow**:
   - Follow consistent processes for similar releases
   - Apply the same phase structure across release types
   - Maintain consistent approval workflows
   - Handle exceptions in a standard way

3. **Validation Approaches**:
   - Implement consistent validation criteria
   - Apply the same quality gates across releases
   - Maintain consistent testing approaches
   - Document validation outcomes consistently

4. **Communication Patterns**:
   - Follow consistent communication templates
   - Apply the same status reporting structure
   - Maintain consistent escalation paths
   - Document decisions in a standard format

5. **Measurement Metrics**:
   - Track the same metrics across similar releases
   - Apply consistent measurement approaches
   - Maintain comparable reporting formats
   - Evaluate success using consistent criteria

## Agent System Coherence Patterns

When applying coherence to agent systems:

1. **Interaction Patterns**:
   - Implement consistent interaction formats
   - Apply the same dialog structures for similar tasks
   - Maintain consistent response patterns
   - Handle similar queries in similar ways

2. **Knowledge Representation**:
   - Organize knowledge domains consistently
   - Apply consistent knowledge reference patterns
   - Maintain consistent terminology
   - Structure similar knowledge in similar ways

3. **Capability Implementation**:
   - Implement similar capabilities in consistent ways
   - Apply the same patterns for capability extension
   - Maintain consistent capability boundaries
   - Document capabilities in a standard format

4. **Collaboration Models**:
   - Follow consistent collaboration patterns
   - Apply the same role divisions across contexts
   - Maintain consistent handoff protocols
   - Document collaboration approaches consistently

5. **Guidance Application**:
   - Implement consistent guidance formats
   - Apply the same principle application patterns
   - Maintain consistent recommendation structures
   - Document guidance rationale in a standard way

## Balancing Coherence with Other Principles

### [Tension:Coherence:Adaptivity]
When coherence and adaptivity create tension:
- Maintain core pattern integrity while allowing context-specific adaptations
- Document variations and their rationale
- Evolve patterns systematically rather than ad-hoc
- Balance standardization with appropriate flexibility

### [Tension:Coherence:Modularity]
When coherence and modularity create tension:
- Apply consistent patterns at module boundaries
- Allow appropriate internal variation within modules
- Standardize interfaces while allowing implementation flexibility
- Balance cross-component consistency with modular independence

### [Tension:Coherence:Clarity]
When coherence and clarity create tension:
- Prioritize clear communication over rigid pattern adherence
- Document pattern exceptions with clear rationale
- Adapt standard patterns to improve understandability
- Balance consistent structure with accessible explanations

## Human-AI Team Collaboration for Coherence

In our two-person team:

### Human Team Member Focus
- Make final decisions on canonical patterns
- Evaluate pattern evolution proposals
- Judge the value of coherence versus other concerns
- Provide experience-based pattern recognition

### AI Agent Focus
- Identify pattern inconsistencies systematically
- Suggest coherent pattern applications
- Document pattern usage consistently
- Track pattern evolution across artifacts

<important>
Always balance [principle:coherence] with [principle:adaptivity]. When established patterns don't fit a new context, document the variation and its rationale rather than forcing a poor fit or creating arbitrary inconsistency.
</important>