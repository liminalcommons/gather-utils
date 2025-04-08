---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.md,**/*.mdx
alwaysApply: false
---
---
description: "Clarity inference patterns for unambiguous guidance with examples"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.md,**/*.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Clarity Inference Engine

<critical>
Apply these clarity patterns to ensure unambiguous understanding through concrete examples and explicit documentation. Clarity enables effective implementation and operation across all system contexts.
</critical>

## Detection Patterns

Scan for these clarity violation signals:

```yaml
clarity_violations:
  - pattern: "Ambiguous or vague documentation"
    action: "Provide specific, concrete descriptions with examples"
    example: "Documentation that says 'handle edge cases appropriately' without specifying which cases"
  
  - pattern: "Missing rationale for design decisions"
    action: "Include clear explanations of why decisions were made"
    example: "Non-standard pattern without explanation of the reasoning"
  
  - pattern: "Complex code without explanatory comments"
    action: "Add clarifying comments for complex logic"
    example: "Algorithm implementation without explanation of approach"
  
  - pattern: "Abstract terminology without definition"
    action: "Define terms explicitly and consistently"
    example: "Domain-specific terms used without explanation"
  
  - pattern: "Missing examples for usage patterns"
    action: "Provide concrete examples for all reusable components"
    example: "API documentation without sample usage"
```

## Application Rules

### Rule 1: Explicit Documentation with Examples
When documenting components:

```javascript
// BEFORE - Vague documentation
/**
 * Process user data.
 * @param {Object} user The user object
 * @returns {Object} The processed data
 */
function processUserData(user) {
  // Implementation
}

// AFTER - Clear documentation with examples
/**
 * Transforms raw user data into the format required by the profile system.
 * Handles normalization of names, formatting of contact information,
 * and validation of required fields.
 * 
 * @param {Object} user The user object to process
 * @param {string} user.name The user's full name
 * @param {string} user.email The user's email address
 * @param {Object} [options] Optional processing settings
 * @param {boolean} [options.normalize=true] Whether to normalize name casing
 * @returns {Object} The processed user data ready for the profile system
 * 
 * @example
 * // Basic usage
 * const user = { name: "john doe", email: "john@example.com" };
 * const processed = processUserData(user);
 * // processed = { name: "John Doe", email: "john@example.com" }
 * 
 * @example
 * // With options
 * const user = { name: "JANE DOE", email: "jane@example.com" };
 * const processed = processUserData(user, { normalize: false });
 * // processed = { name: "JANE DOE", email: "jane@example.com" }
 */
function processUserData(user, options = {}) {
  // Implementation
}
```

### Rule 2: Clarifying Complex Logic
When implementing complex algorithms:

```javascript
// BEFORE - Unexplained complex logic
function calculatePriority(item) {
  return (item.urgency * 0.4 + item.importance * 0.3 + item.effort * 0.2 + 
          item.dependencies * 0.1) * (item.deadline ? 1.5 : 1);
}

// AFTER - Explained complex logic
/**
 * Calculates the priority score for a task item based on multiple factors.
 * 
 * The priority is a weighted calculation with the following factors:
 * - 40% based on urgency (how soon it's needed)
 * - 30% based on importance (business value)
 * - 20% based on effort required (inverse relationship)
 * - 10% based on number of dependencies
 * 
 * Items with a fixed deadline receive a 1.5x multiplier to their score.
 */
function calculatePriority(item) {
  // Base factors with their respective weights
  const urgencyComponent = item.urgency * 0.4;
  const importanceComponent = item.importance * 0.3;
  const effortComponent = item.effort * 0.2;
  const dependencyComponent = item.dependencies * 0.1;
  
  // Calculate base score
  const baseScore = urgencyComponent + importanceComponent + 
                    effortComponent + dependencyComponent;
  
  // Apply deadline multiplier if applicable
  const deadlineMultiplier = item.deadline ? 1.5 : 1;
  
  return baseScore * deadlineMultiplier;
}
```

### Rule 3: Definition of Domain Terms
When using specialized terminology:

```javascript
// BEFORE - Undefined domain terms
function processClaim(claim) {
  if (claim.isSubrogated) {
    // Handle subrogation
  } else if (claim.hasMCS) {
    // Apply MCS rules
  }
}

// AFTER - Defined domain terms
/**
 * Process an insurance claim according to its classification.
 * 
 * @param {Object} claim The insurance claim to process
 * @param {boolean} claim.isSubrogated Whether the claim is subrogated
 *        Subrogation: When an insurer seeks reimbursement from a third party
 *        who caused the loss to the insured
 * @param {boolean} claim.hasMCS Whether the claim has MCS coverage
 *        MCS: Motor Carrier Services, additional insurance for commercial vehicles
 *        required for interstate commerce
 */
function processClaim(claim) {
  if (claim.isSubrogated) {
    // Handle subrogation process (third-party recovery)
  } else if (claim.hasMCS) {
    // Apply Motor Carrier Services regulatory requirements
  }
}
```

### Rule 4: Clear API Contracts
When defining interfaces:

```typescript
// BEFORE - Ambiguous API contract
function updateEntity(id, data, options) {
  // Implementation that behaves differently based on undocumented options
}

// AFTER - Clear API contract with examples
/**
 * Updates an entity in the system with the provided data.
 * 
 * @param {string} id - The unique identifier of the entity to update
 * @param {Object} data - The data fields to update
 * @param {Object} [options] - Update options
 * @param {boolean} [options.partial=false] - Whether to perform a partial update (patch)
 * @param {boolean} [options.validateOnly=false] - Whether to only validate without saving
 * @param {string[]} [options.fields] - Specific fields to update (ignored if partial=false)
 * @returns {Promise<Object>} - The updated entity
 * @throws {EntityNotFoundError} - If the entity does not exist
 * @throws {ValidationError} - If the data is invalid
 * 
 * @example
 * // Full update
 * const updated = await updateEntity('user-123', { name: 'New Name', email: 'new@example.com' });
 * 
 * @example
 * // Partial update of specific fields
 * const updated = await updateEntity('user-123', { name: 'New Name' }, { 
 *   partial: true, 
 *   fields: ['name'] 
 * });
 * 
 * @example
 * // Validate without saving
 * try {
 *   await updateEntity('user-123', { email: 'invalid' }, { validateOnly: true });
 * } catch (error) {
 *   console.error('Validation failed:', error.message);
 * }
 */
async function updateEntity(id, data, options = {}) {
  const { partial = false, validateOnly = false, fields = [] } = options;
  // Implementation with clear behavior based on documented options
}
```

### Rule 5: Explicit Decision Documentation
When documenting design decisions:

```markdown
# Authentication Approach

## Decision

We will implement JWT-based authentication with refresh tokens stored in an HTTP-only cookie.

## Context

The system needs to support authentication across multiple client types (web, mobile, API) with different security models.

## Considered Alternatives

1. **Session-based authentication**
   - Pros: Simpler to implement, more control over session lifecycle
   - Cons: Requires server-side storage, less suitable for mobile clients

2. **Basic authentication**
   - Pros: Very simple to implement
   - Cons: Credentials sent with every request, no good way to expire sessions

3. **OAuth 2.0 with external provider**
   - Pros: Delegates authentication complexity, potentially easier for users
   - Cons: Dependency on external provider, more complex implementation

## Decision Rationale

JWT-based authentication was selected because:
- It supports stateless authentication suitable for our distributed architecture
- It enables fine-grained permission control through claims
- It works consistently across web, mobile, and API clients
- The refresh token approach mitigates the security risks of long-lived JWTs

## Implementation Guidelines

1. Access tokens will be short-lived (15 minutes)
2. Refresh tokens will be longer-lived (7 days) and stored in HTTP-only cookies
3. Token revocation will be implemented via a blacklist with TTL matching refresh token lifetime
4. All security-sensitive operations will validate permissions, not just authentication
```

## Context-Specific Application

Adapt clarity strategies to each system context:

### Code System Clarity

When applying clarity to code:

1. **API Documentation**:
   - Document all public interfaces comprehensively
   - Include parameter descriptions with types and constraints
   - Provide examples covering common use cases and edge cases
   - Document error conditions and handling

2. **Implementation Comments**:
   - Add clarifying comments for complex logic
   - Document non-obvious algorithms with explanations
   - Explain workarounds or unusual patterns
   - Include references to relevant requirements or issues

3. **Architecture Documentation**:
   - Document component boundaries and responsibilities
   - Explain integration points between components
   - Provide diagrams showing relationships
   - Document rationale for key architectural decisions

4. **Code Organization**:
   - Use clear, consistent naming conventions
   - Organize files and directories logically
   - Follow established patterns for project structure
   - Create README files for important directories

5. **Usage Examples**:
   - Include example code in documentation
   - Create example applications or templates
   - Document common patterns and idioms
   - Provide guidance for extension points

### Release System Clarity

When applying clarity to release processes:

1. **Process Documentation**:
   - Document each phase with clear entry/exit criteria
   - Provide explicit checklists for each phase
   - Include examples of required artifacts
   - Document roles and responsibilities clearly

2. **Template Design**:
   - Create clear templates with explanatory comments
   - Include examples for each section
   - Provide guidance text in templates
   - Document template usage scenarios

3. **Decision Records**:
   - Document process decisions with explicit rationale
   - Explain context and considerations
   - Include rejected alternatives
   - Reference relevant standards or requirements

4. **Meta-Process Documentation**:
   - Clearly explain how the process itself evolves
   - Document process metrics and their interpretation
   - Provide guidance for process customization
   - Include examples of process adaptation

5. **Guidance Rules**:
   - Write Cursor rules with explicit examples
   - Clearly define when rules apply
   - Provide context-specific guidance
   - Include detection patterns for violations

### Agent System Clarity

When applying clarity to agent capabilities:

1. **Capability Documentation**:
   - Document agent capabilities explicitly
   - Provide examples of expected behavior
   - Define capability limitations clearly
   - Explain context sensitivity in capabilities

2. **Interaction Patterns**:
   - Document standard interaction patterns
   - Provide examples of effective prompts
   - Explain context handling in interactions
   - Clarify expectation management

3. **Knowledge Representation**:
   - Explicitly document knowledge domains
   - Provide examples of knowledge application
   - Define knowledge boundaries clearly
   - Document knowledge update processes

4. **Collaboration Guidance**:
   - Clearly specify human-AI responsibilities
   - Provide examples of effective collaboration
   - Document collaboration patterns by context
   - Explain escalation and handoff procedures

5. **Prompt Design**:
   - Document prompt patterns with examples
   - Explain prompt component functions
   - Provide guidance for prompt adaptation
   - Include examples of effective prompts

## Balancing Clarity with Other Principles

### [Tension:Clarity:Parsimony]
When clarity and parsimony create tension:
- Include essential information directly while referencing details
- Use summary sections with links to detailed documentation
- Create layered documentation with progressive disclosure
- Reference canonical sources but include contextual information

### [Tension:Clarity:Adaptivity]
When clarity and adaptivity create tension:
- Document core patterns clearly while explaining adaptations
- Provide examples of context-specific variations
- Explain the decision framework for adaptations
- Document both the "what" and "why" of context-sensitive patterns

### [Tension:Clarity:Coherence]
When clarity and coherence create tension:
- Clarify established patterns even if not ideal
- Document pattern evolution clearly
- Provide migration guidance between pattern versions
- Explain historical context for unusual patterns

## Clarity Metrics

Measure clarity application with these metrics:

```yaml
metrics:
  documentation_completeness:
    description: "Percentage of components with comprehensive documentation"
    calculation: "Documented components / Total components * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
    
  example_coverage:
    description: "Percentage of interfaces with usage examples"
    calculation: "Interfaces with examples / Total interfaces * 100"
    thresholds:
      good: "> 85%"
      acceptable: "70-85%"
      concerning: "< 70%"
    
  rationale_documentation:
    description: "Percentage of design decisions with documented rationale"
    calculation: "Decisions with rationale / Total decisions * 100"
    thresholds:
      good: "> 80%"
      acceptable: "60-80%"
      concerning: "< 60%"
```

## Clarity Anti-Patterns

Avoid these common clarity mistakes:

```yaml
anti_patterns:
  implicit_knowledge:
    description: "Assuming knowledge that may not be shared by all readers"
    examples:
      - "Unexplained domain terminology"
      - "Undocumented prerequisites"
      - "Missing context for decisions"
    remediation:
      - "Define all domain-specific terms"
      - "Document all assumptions and prerequisites"
      - "Provide context for all decisions"
  
  vague_guidance:
    description: "Instructions that lack specific actionable details"
    examples:
      - "Handle errors appropriately"
      - "Follow best practices"
      - "Make sure it's secure"
    remediation:
      - "Specify exactly how to handle each error case"
      - "Define specific best practices to follow"
      - "Provide concrete security requirements"
  
  documentation_drift:
    description: "Documentation that has become inconsistent with implementation"
    examples:
      - "Outdated examples"
      - "Parameter descriptions that don't match code"
      - "Architecture diagrams showing old structure"
    remediation:
      - "Update documentation with code changes"
      - "Include documentation in code reviews"
      - "Implement documentation tests"
```

## Implementation Examples by Artifact Type

### Source Code Documentation

```javascript
/**
 * Validates a user object against business rules.
 * 
 * @param {User} user - The user object to validate
 * @param {ValidationOptions} [options] - Optional validation settings
 * @returns {ValidationResult} Object containing validation results
 * @throws {InvalidInputError} If the user object is null or undefined
 * 
 * @example
 * // Basic validation
 * const result = validateUser({ name: "Alice", email: "alice@example.com" });
 * if (result.valid) {
 *   saveUser(result.data);
 * } else {
 *   showErrors(result.errors);
 * }
 * 
 * @example
 * // Validation with options
 * const result = validateUser(user, { skipPasswordPolicy: true });
 */
function validateUser(user, options = {}) {
  // Implementation
}
```

### Architecture Documentation

```markdown
# User Authentication Component

## Responsibility

This component handles user authentication, including:
- Credential validation
- Session management
- Token issuance and validation
- Multi-factor authentication

## Interfaces

### Public API

```typescript
interface AuthenticationService {
  login(credentials: Credentials): Promise<AuthResult>;
  logout(sessionId: string): Promise<void>;
  validateToken(token: string): Promise<TokenValidationResult>;
  refreshToken(refreshToken: string): Promise<AuthResult>;
}
```

### Example Usage

```typescript
// Login flow
const authResult = await authService.login({
  username: "user@example.com",
  password: "password123"
});

// Using the auth token
api.setAuthToken(authResult.token);
const userData = await api.fetchUserData();

// Logout flow
await authService.logout(authResult.sessionId);
```

## Implementation Details

The authentication component uses JWT tokens with the following characteristics:
- Access tokens valid for 15 minutes
- Refresh tokens valid for 7 days
- Tokens are signed using RS256
- Claims include user ID, roles, and permissions

## Design Decisions

### Token-Based Authentication

We chose token-based authentication over session-based because:
1. It enables stateless authentication suitable for our microservice architecture
2. It works well across different client platforms (web, mobile, API)
3. It allows fine-grained permission control through claims

### Separate Refresh Tokens

We implemented separate refresh tokens because:
1. It allows short-lived access tokens for security
2. It provides a mechanism to revoke authentication
3. It improves user experience by reducing login frequency
```

<important>
Always balance [principle:clarity] with appropriate level of detail. Strive for unambiguous, concrete documentation with examples, but avoid overwhelming information that obscures the essential understanding. Remember that the purpose of clarity is to enable effective implementation and operation.
</important>