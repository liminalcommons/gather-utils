---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.md,**/*.mdx
alwaysApply: false
---
---
description: "Parsimony inference patterns for optimizing information density across the release lifecycle"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.md,**/*.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Parsimony Inference Engine

<critical>
Apply these parsimony patterns to optimize information density and minimize duplication across the system. Each concept should be defined once in a canonical location and referenced elsewhere to maintain system integrity.
</critical>

## Detection Patterns

Scan for these parsimony violation signals:

```yaml
parsimony_violations:
  - pattern: "Similar function implementations across files"
    action: "Extract common functionality to a shared utility"
    example: "Similar validation functions in multiple components"
  
  - pattern: "Duplicated documentation sections"
    action: "Refactor to reference canonical documentation"
    example: "Same API parameters described in multiple places"
  
  - pattern: "Repeated constant definitions"
    action: "Consolidate constants in a shared constants file"
    example: "Error codes defined in multiple files"
  
  - pattern: "Copy-pasted code blocks with minor variations"
    action: "Parameterize the pattern as a shared function"
    example: "Similar data transformation logic with different field names"
  
  - pattern: "Redundant type definitions"
    action: "Define types once and import/reference them"
    example: "Interface definitions duplicated across modules"
```

## Application Rules

### Rule 1: Extract Shared Functionality
When similar logic appears in multiple places:

```javascript
// BEFORE - Violation of parsimony
function componentA() {
  // Complex data transformation logic here
}

function componentB() {
  // Nearly identical data transformation logic here
}

// AFTER - Following parsimony
function transformData(data, options) {
  // Shared transformation logic
}

function componentA() {
  return transformData(data, { forA: true });
}

function componentB() {
  return transformData(data, { forB: true });
}
```

### Rule 2: Centralize Type Definitions
When types are used across boundaries:

```typescript
// types.ts - Canonical type definition
export interface User {
  id: string;
  name: string;
  email: string;
}

// user-service.ts - Importing canonical types
import { User } from '../types';

function processUser(user: User) {
  // Implementation using ule 3: Reference Documentation
When documentation needs to appear in multiple places:

```markdown
# Component Documentation

## API Parameters

See the [API Reference Documentation](mdc:../api-reference.md#parameters) for the complete list of parameters.

## Component-Specific Usage

When using with this component, note these specific behaviors...
```

### Rule 4: Constant Management
When constants are needed across components:

```javascript
// constants.js - Centralized constant definitions
export const ERROR_CODES = {
  NOT_FOUND: 'E404',
  UNAUTHORIZED: 'E401',
  SERVER_ERROR: 'E500'
};

// error-handler.js - Importing constants
import { ERROR_CODES } from '../constants';

function handleError(type) {
  const code = ERROR_CODES[type];
  // Implementation using the constant
}
```

### Rule 5: Domain Model Centralization
When domain concepts appear across the codebase:

```typescript
// domain/user.ts - Canonical domain model
export class User {
  constructor(
    public id: string,
    public name: string,
    public email: string,
    public role: UserRole
  ) {}
  
  isAdmin(): boolean {
    return this.role === UserRole.ADMIN;
  }
  
  canAccess(resource: Resource): boolean {
    // Permission logic
    return this.isAdmin() || resource.isPublic();
  }
}

// auth-service.ts - Using domain model
import { User } from '../domain/user';

class AuthService {
  authenticate(credentials): User {
    // Authentication logic
    return new User(...);
  }
}

// access-control.ts - Using same domain model
import { User } from '../domain/user';

class AccessControl {
  checkAccess(user: User, resource: Resource): boolean {
    return user.canAccess(resource);
  }
}
```

## Context-Specific Application

Adapt parsimony application based on the system context:

### Code System Application

When applying parsimony to code:

1. **Type System**:
   - Define canonical types in dedicated files
   - Use import/export mechanisms to share types
   - Ensure consistent type usage across components

2. **Shared Utilities**:
   - Create utility libraries for common functionality
   - Organize utilities by domain or function
   - Provide clear documentation for utility functions

3. **Constants and Configuration**:
   - Centralize constants in dedicated files
   - Group constants by domain or purpose
   - Use configuration management for environment-specific values

4. **Pattern Implementation**:
   - Implement standard patterns once in reusable form
   - Parameterize patterns for context-specific usage
   - Document pattern variants and when to use them

5. **Documentation**:
   - Maintain single source of truth for component documentation
   - Use cross-references instead of duplicating information
   - Keep API documentation with the code to maintain locality

### Release System Application

When applying parsimony to release processes:

1. **Process Definitions**:
   - Define process steps in canonical documentation
   - Reference standard processes rather than redefining
   - Use templates to ensure consistency

2. **Artifact Structure**:
   - Create reusable templates for common artifacts
   - Define standard sections for all documentation
   - Maintain consistent metadata across artifacts

3. **Guidance and Rules**:
   - Organize Cursor rules to minimize duplication
   - Reference shared principles from specialized rules
   - Maintain hierarchical rule structure

4. **Validation Criteria**:
   - Define standard validation criteria in one place
   - Reference criteria sets for different contexts
   - Maintain versioned criteria definitions

5. **Metrics and Measurements**:
   - Define standard metrics once with clear calculations
   - Reference metrics consistently across processes
   - Maintain a canonical metrics glossary

### Agent System Application

When applying parsimony to agent capabilities:

1. **Knowledge Representation**:
   - Maintain canonical knowledge sources
   - Reference rather than duplicate domain knowledge
   - Create hierarchical knowledge structure

2. **Guidance Patterns**:
   - Define standard interaction patterns once
   - Reference patterns in specific guidance
   - Parameterize patterns for different contexts

3. **Prompt Design**:
   - Create reusable prompt components
   - Reference standard components in complex prompts
   - Maintain prompt library with versioning

4. **Collaboration Models**:
   - Define standard collaboration patterns
   - Reference patterns in specific scenarios
   - Document pattern variations with rationale

5. **Capability Documentation**:
   - Maintain canonical capability documentation
   - Reference capabilities in task-specific guidance
   - Update capability documentation as a single source of truth

## Balancing Parsimony with Other Principles

### [Tension:Parsimony:Clarity]
When clarity requires some duplication:
- Include essential context for clarity but reference details
- Use clear references with descriptive text
- Consider "information staging" - summary with reference to details

### [Tension:Parsimony:Adaptivity]
When adaptation requires context-specific variations:
- Extract common patterns while allowing parameterization
- Document relationships between canonical source and variations
- Use inheritance or composition to extend base implementations

### [Tension:Parsimony:Tensegrity]
When relationships require complementary definitions:
- Define relationship once but reference in both components
- Ensure references are bidirectional and consistent
- Document the relationship model in a canonical location

## Parsimony Metrics

Measure parsimony application with these metrics:

```yaml
metrics:
  duplication_rate:
    description: "Percentage of duplicate code or content"
    calculation: "Duplicate lines / Total lines * 100"
    thresholds:
      good: "< 3%"
      acceptable: "3-7%"
      concerning: "> 7%"
    
  reference_usage:
    description: "Usage of references instead of duplication"
    calculation: "Referenced concepts / Total concept usages * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
    
  concept_consolidation:
    description: "Degree to which similar concepts are consolidated"
    calculation: "Consolidated concepts / Total similar concepts * 100"
    thresholds:
      good: "> 85%"
      acceptable: "70-85%"
      concerning: "< 70%"
```

## Parsimony Anti-Patterns

Avoid these common parsimony mistakes:

```yaml
anti_patterns:
  dry_violation:
    description: "Violations of Don't Repeat Yourself principle"
    examples:
      - "Copy-pasted code across files"
      - "Reimplemented utility functions"
      - "Duplicated validation logic"
    detection:
      - "Code similarity analysis"
      - "Function signature comparison"
      - "Logic pattern matching"
  
  over_normalization:
    description: "Excessive abstraction that harms clarity or performance"
    examples:
      - "Single-use abstractions"
      - "Overly generic utilities"
      - "Indirection without benefit"
    detection:
      - "Usage frequency analysis"
      - "Abstraction depth measurement"
      - "Performance impact assessment"
  
  hidden_duplication:
    description: "Duplication disguised as different implementations"
    examples:
      - "Similar logic with different variable names"
      - "Reordered operations with same effect"
      - "Different approaches to same problem"
    detection:
      - "Semantic code analysis"
      - "Output equivalence testing"
      - "Behavior similarity comparison"
```

## Specific Guidance by Artifact Type

### Source Code Files

1. **Import and Share**:
   - Import shared types, constants, and utilities
   - Use dependency injection for shared services
   - Leverage language-specific module systems

2. **Abstraction Levels**:
   - Extract common patterns to appropriate level of abstraction
   - Create utilities at the right scope (function, module, global)
   - Balance abstraction with locality of reference

3. **Code Organization**:
   - Group related functionality in logical units
   - Maintain separation of concerns
   - Use consistent file and directory structure

### Documentation Files

1. **Reference Structure**:
   - Use links to reference canonical documentation
   - Embed summaries with references to details
   - Organize documentation hierarchically

2. **Knowledge Management**:
   - Establish a documentation hierarchy
   - Define terms in a glossary and reference consistently
   - Use templates for consistent structure

3. **Version Control**:
   - Keep documentation with related code
   - Ensure documentation evolves with implementation
   - Maintain backward references in documentation history

<important>
Always balance [principle:parsimony] with [principle:clarity]. When duplication significantly improves clarity in critical areas, prefer clarity but document the relationship to the canonical source.
</important>