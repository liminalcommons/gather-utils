---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Adaptivity inference patterns for context-sensitive evolution"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Adaptivity Inference Engine

<critical>
Apply these adaptivity patterns to enable context-sensitive evolution while maintaining system integrity.
</critical>

## Detection Patterns

Scan for these adaptivity violation signals:

```yaml
adaptivity_violations:
  - pattern: "Forced conformity to patterns despite context mismatch"
    action: "Adapt patterns to the specific context needs"
    example: "Applying microservice patterns to a simple app that would work better as a monolith"
  
  - pattern: "Rigid implementations that resist necessary evolution"
    action: "Introduce flexibility points at change boundaries"
    example: "Hardcoded business rules that frequently change"
  
  - pattern: "Fragmented adaptations without coherent direction"
    action: "Establish adaptive guidelines that preserve core principles"
    example: "Every developer implementing their own approach to the same problem"
  
  - pattern: "Ignoring established patterns without justification"
    action: "Understand existing patterns before replacing them"
    example: "Rewriting utility functions without understanding their design"
  
  - pattern: "Over-abstraction preventing contextual optimization"
    action: "Balance abstraction with contextual specialization"
    example: "Interfaces too generic to be efficiently implemented"
```

## Application Rules

### Rule 1: Discover Before Changing
When approaching existing code:

```typescript
// BEFORE implementing changes:

// 1. EXAMINE existing implementations
// Understand the current approach thoroughly
function existingImplementation() {
  // Carefully study this implementation
  // Identify the patterns and their rationale
}

// 2. IDENTIFY the underlying pattern
/* 
 * Pattern identified:
 * - Factory pattern for component creation
 * - Context-based configuration
 * - Lazy initialization
 */

// 3. THEN implement changes that preserve the pattern essence
function enhancedImplementation() {
  // Add new functionality while respecting the existing pattern
  // Preserve the factory approach
  // Maintain the context-based configuration
  // Keep the lazy initialization
}
```

### Rule 2: Context-Sensitive Implementation
When implementing patterns in different contexts:

```typescript
// Base pattern definition
interface DataProcessor<T> {
  process(data: T): Promise<T>;
}

// BEFORE - Rigid implementation ignoring context
class StandardProcessor<T> implements DataProcessor<T> {
  async process(data: T): Promise<T> {
    // One-size-fits-all implementation
    return processedData;
  }
}

// AFTER - Context-sensitive implementations
// Financial context
class FinancialDataProcessor implements DataProcessor<FinancialData> {
  async process(data: FinancialData): Promise<FinancialData> {
    // Financial-specific processing
    // Uses domain terminology
    // Implements financial-specific validations
    return processedData;
  }
}

// Healthcare context
class PatientDataProcessor implements DataProcessor<PatientData> {
  async process(data: PatientData): Promise<PatientData> {
    // Healthcare-specific processing
    // Handles HIPAA compliance
    // Implements healthcare-specific validations
    return processedData;
  }
}
```

### Rule 3: Flexible Extension Points
When designing systems that will evolve:

```typescript
// BEFORE - Rigid design with fixed functionality
class AuthenticationService {
  authenticate(username: string, password: string): Promise<User> {
    // Fixed implementation that can't be extended
  }
}

// AFTER - Design with extension points
class AuthenticationService {
  constructor(
    private strategies: AuthenticationStrategy[] = [new DefaultAuthStrategy()]
  ) {}

  // Extension point 1: Configurable strategies
  addStrategy(strategy: AuthenticationStrategy): void {
    this.strategies.push(strategy);
  }
  
  // Extension point 2: Strategy-based implementation
  async authenticate(credentials: Credentials): Promise<User> {
    // Try each strategy until one succeeds
    for (const strategy of this.strategies) {
      if (strategy.canHandle(credentials)) {
        return strategy.authenticate(credentials);
      }
    }
    throw new AuthenticationError("No suitable authentication method");
  }
}

// Extension point 3: Pluggable strategy interface
interface AuthenticationStrategy {
  canHandle(credentials: Credentials): boolean;
  authenticate(credentials: Credentials): Promise<User>;
}

// Extension implementations
class PasswordStrategy implements AuthenticationStrategy {
  canHandle(credentials: Credentials): boolean {
    return credentials.type === 'password';
  }
  
  authenticate(credentials: PasswordCredentials): Promise<User> {
    // Password-based authentication
  }
}

class OAuthStrategy implements AuthenticationStrategy {
  canHandle(credentials: Credentials): boolean {
    return credentials.type === 'oauth';
  }
  
  authenticate(credentials: OAuthCredentials): Promise<User> {
    // OAuth-based authentication
  }
}
```

### Rule 4: Preserving Intent During Evolution
When evolving patterns:

```typescript
// Original pattern with clear intent: Separation of data access from business logic
interface UserRepository {
  findById(id: string): Promise<User>;
  save(user: User): Promise<void>;
}

class UserService {
  constructor(private repository: UserRepository) {}
  
  async updateUser(id: string, data: UserData): Promise<User> {
    const user = await this.repository.findById(id);
    // Business logic for updating user
    return this.repository.save(user);
  }
}

// POOR EVOLUTION - Loses the intent by mixing concerns
class EnhancedUserService {
  constructor(private database: Database) {}
  
  async updateUser(id: string, data: UserData): Promise<User> {
    // Direct database access bypasses repository pattern
    const user = await this.database.query('SELECT * FROM users WHERE id = ?', [id]);
    // Business logic mixed with data access
    await this.database.query('UPDATE users SET ...', [...]);
    return user;
  }
}

// GOOD EVOLUTION - Preserves the intent while enhancing functionality
interface EnhancedUserRepository extends UserRepository {
  findByEmail(email: string): Promise<User>;
  findWithProfile(id: string): Promise<UserWithProfile>;
}

class EnhancedUserService {
  constructor(private repository: EnhancedUserRepository) {}
  
  async updateUser(id: string, data: UserData): Promise<User> {
    // Still uses repository, preserving separation of concerns
    const user = await this.repository.findById(id);
    // Enhanced business logic
    return this.repository.save(user);
  }
  
  // New functionality while preserving the pattern
  async updateByEmail(email: string, data: UserData): Promise<User> {
    const user = await this.repository.findByEmail(email);
    // Business logic
    return this.repository.save(user);
  }
}
```

## Context-Specific Application

Adjust adaptivity application based on context:

```yaml
adaptivity_contexts:
  high_adaptivity:
    applies_to: [early_exploration, prototype, rapidly_changing_domain]
    strategies:
      - "Focus on flexible extension points"
      - "Favor composition over inheritance for flexibility"
      - "Design explicitly for experimentation"
      - "Document underlying patterns while allowing variation"
  
  moderate_adaptivity:
    applies_to: [active_development, growing_system]
    strategies:
      - "Balance consistent patterns with contextual needs"
      - "Create explicit variation points in stable interfaces"
      - "Document pattern variations with rationale"
      - "Establish pattern evolution guidance"
  
  low_adaptivity:
    applies_to: [mature_system, regulated_domain]
    strategies:
      - "Formalize change processes for established patterns"
      - "Focus evolution on well-defined extension points"
      - "Create thorough pattern documentation with examples"
      - "Validate adaptations against system integrity"
```

## Adaptivity Metrics

Measure adaptivity effectiveness using these metrics:

```yaml
metrics:
  context_adaptation_rate:
    description: "Percentage of patterns with appropriate context adaptations"
    calculation: "Context-appropriate adaptations / Total adaptations * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
  
  pattern_intent_preservation:
    description: "Success in preserving core intent during adaptations"
    calculation: "Adaptations preserving intent / Total adaptations * 100"
    thresholds:
      good: "> 95%"
      acceptable: "85-95%"
      concerning: "< 85%"
  
  adaptation_documentation_quality:
    description: "Completeness of adaptation documentation"
    calculation: "Well-documented adaptations / Total adaptations * 100"
    thresholds:
      good: "> 90%"
      acceptable: "70-90%"
      concerning: "< 70%"
```

## Adaptivity Anti-Patterns

Avoid these common adaptivity mistakes:

```yaml
anti_patterns:
  blind_conformity:
    description: "Forcing pattern application without considering context"
    examples:
      - "Applying microservice architecture to a simple application"
      - "Using complex design patterns for simple problems"
    remediation:
      - "Consider context before applying patterns"
      - "Document adaptations with rationale"
      - "Create context-specific guidance"
      - "Focus on goals rather than specific implementations"
  
  pattern_fragmentation:
    description: "Inconsistent adaptations creating system incoherence"
    examples:
      - "Different teams adapting patterns differently"
      - "Similar problems solved with divergent approaches"
    remediation:
      - "Document adaptation principles"
      - "Create context classification system"
      - "Review adaptations for consistency"
      - "Capture and share successful adaptations"
  
  over_flexibility:
    description: "Excessive flexibility making the system hard to understand"
    examples:
      - "Too many configuration options"
      - "Overly abstract interfaces"
    remediation:
      - "Focus on common use cases first"
      - "Apply the principle of least power"
      - "Balance flexibility with usability"
      - "Create sensible defaults"
```

## Code System Adaptivity Patterns

When applying adaptivity to code systems:

1. **API Evolution Strategy**:
   - Design versioned APIs from the start
   - Provide backward compatibility periods
   - Create extension points for future needs
   - Document API evolution strategy

2. **Configuration Management**:
   - Implement hierarchical configuration
   - Support environment-specific overrides
   - Create context-based configuration
   - Allow runtime configuration changes

3. **Feature Toggles**:
   - Implement feature flags for controlled rollout
   - Create context-based feature activation
   - Support gradual feature adoption
   - Enable experimentation with new features

4. **Plug-in Architecture**:
   - Design clear extension points
   - Create plugin discovery mechanisms
   - Support versioned plugin interfaces
   - Document plugin development process

5. **Context-Sensitive Design**:
   - Identify relevant contexts explicitly
   - Create context-specific implementations
   - Document context detection logic
   - Test behavior across different contexts

## Release System Adaptivity Patterns

When applying adaptivity to release processes:

1. **Release Type Specialization**:
   - Define different processes for different release types
   - Create context-appropriate artifacts
   - Scale validation based on release scope
   - Adapt timeline to release complexity

2. **Flexible Process Flows**:
   - Support different paths through the lifecycle
   - Create alternative flows for different contexts
   - Allow appropriate process customization
   - Document process variations clearly

3. **Contextual Validation**:
   - Adapt validation criteria to release context
   - Apply appropriate validation intensity
   - Focus validation on relevant areas
   - Document context-specific validation requirements

4. **Evolutionary Improvement**:
   - Create process feedback mechanisms
   - Capture and apply lessons learned
   - Experiment with process improvements
   - Document process evolution over time

5. **Template Variability**:
   - Create context-specific artifact templates
   - Support different detail levels based on context
   - Provide adaptation guidance in templates
   - Document template selection criteria

## Agent System Adaptivity Patterns

When applying adaptivity to agent systems:

1. **Context-Sensitive Guidance**:
   - Adapt guidance to specific contexts
   - Create context detection mechanisms
   - Provide different guidance levels
   - Document context-specific recommendations

2. **Knowledge Domain Adaptation**:
   - Organize knowledge by context relevance
   - Apply different knowledge based on context
   - Support domain-specific terminology
   - Document knowledge application guidelines

3. **Interaction Pattern Variation**:
   - Adapt interaction styles to context
   - Support different collaboration models
   - Vary communication detail based on context
   - Document interaction adaptation principles

4. **Capability Adaptation**:
   - Enable or disable capabilities based on context
   - Adjust capability behavior to specific needs
   - Support capability composition
   - Document capability adaptation guidelines

5. **Context-Based Learning**:
   - Capture successful adaptations
   - Learn from context-specific interactions
   - Apply learned patterns appropriately
   - Document adaptation effectiveness

## Balancing Adaptivity with Other Principles

### [Tension:Adaptivity:Coherence]
When adaptivity and coherence create tension:
- Preserve core pattern intent while allowing contextual variation
- Document variations explicitly with rationale
- Create adaptation guidelines that maintain system integrity
- Balance flexibility with consistency across the system

### [Tension:Adaptivity:Modularity]
When adaptivity and modularity create tension:
- Create adaptation points at module boundaries
- Define clear interfaces that allow implementation flexibility
- Document module adaptation capabilities
- Balance boundary stability with implementation flexibility

### [Tension:Adaptivity:Parsimony]
When adaptivity and parsimony create tension:
- Create adaptable abstractions that remain efficient
- Document relationships between variations and canonical patterns
- Support reuse while allowing necessary specialization
- Balance adaptation with knowledge management

## Human-AI Team Collaboration for Adaptivity

In our two-person team:

### Human Team Member Focus
- Identify when context requires adaptation
- Make final decisions on appropriate adaptations
- Provide domain-specific context knowledge
- Judge adaptation effectiveness

### AI Agent Focus
- Analyze existing patterns systematically
- Document adaptation rationale clearly
- Ensure pattern intent preservation
- Track adaptations across the system

<important>
Always balance [principle:adaptivity] with [principle:coherence]. When adapting patterns to specific contexts, preserve the core intent and document the relationship to the standard pattern to maintain system coherence.
</important>