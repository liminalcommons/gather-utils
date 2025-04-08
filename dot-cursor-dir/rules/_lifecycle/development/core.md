---
description: 
globs: **/development/*.md,**/development/*.mdx,**/releases/*/development.md,**/releases/*/development.mdx
alwaysApply: false
---
---
description: "Core guidance for the development phase of the release lifecycle"
globs: "**/development/*.md,**/development/*.mdx,**/releases/*/development.md,**/releases/*/development.mdx"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Development Phase Guidance

<critical>
The development phase is where plans are transformed into actual implementation. During this phase, ensure that changes adhere to meta-systemic principles while delivering the planned functionality effectively and efficiently.
</critical>

## Core Development Activities

The development phase consists of these essential activities:

1. **Incremental Implementation**: Build features methodically, delivering small functional increments
2. **Pattern Application**: Apply established patterns consistently while adapting to specific contexts
3. **Component Integration**: Ensure proper interaction between new and existing components
4. **Documentation**: Document implementation details alongside the code
5. **Continuous Validation**: Verify functional and non-functional requirements throughout development

## Implementation Approach

Structure your development activities as follows:

### 1. Preparation and Environment

Before beginning development, ensure:

```markdown
## Development Preparation

### Environment Setup
- Development environment configured with required dependencies
- Access to necessary resources and systems established
- Required tools and libraries installed and configured
- Reference implementations or examples identified

### Reference Documentation
- Architecture references gathered
- Pattern documentation accessible
- Existing component documentation reviewed
- Technical specifications clarified

### Quality Expectations
- Acceptance criteria reviewed and understood
- Non-functional requirements (performance, security, etc.) clear
- Validation approach established
- Coding standards and patterns identified
```

### 2. Incremental Implementation

Break down development into small, manageable increments:

```markdown
## Incremental Development

### Implementation Increments
1. **[Increment 1: Core Framework]**
   - Minimal implementation that demonstrates the basic approach
   - Focus on core architecture without all features
   - Establish patterns that will be followed throughout
   - Early integration with existing components

2. **[Increment 2: Key Functionality]**
   - Implement primary user-facing features
   - Focus on functionality over optimization
   - Address key technical challenges
   - Verify against core requirements

3. **[Increment 3: Feature Completion]**
   - Implement remaining functionality
   - Complete integration with all dependent systems
   - Ensure comprehensive error handling
   - Implement logging and observability

4. **[Increment 4: Refinement]**
   - Optimize performance
   - Enhance error handling and edge cases
   - Complete documentation
   - Final integration validation

### Increment Validation
- Each increment should be fully functional
- Validate increment before proceeding to next
- Document progress and challenges after each increment
- Adjust subsequent increments based on learnings
```

### 3. Pattern Application

Apply established patterns consistently:

```markdown
## Pattern Application

### Identify Applicable Patterns
- Reference established patterns for similar functionality
- Consult pattern documentation in `.cursor/rules/_patterns`
- Examine existing implementations of similar components
- Determine appropriate adaptations based on context

### Apply Patterns Consistently
- Follow consistent naming conventions
- Maintain structural consistency with established patterns
- Ensure behavior consistency across similar components
- Document any adaptations with clear rationale

### Pattern Evolution
- When patterns need to evolve, discuss with the team
- Document pattern enhancements or adaptations
- Preserve core intent while allowing appropriate evolution
- Ensure pattern changes are propagated to similar components
```

### 4. Component Integration

Ensure proper integration between components:

```markdown
## Component Integration

### Interface Contracts
- Clearly define interface contracts between components
- Document expected inputs, outputs, and error conditions
- Verify interface compatibility with existing components
- Create integration tests for all component interactions

### Data Flow
- Document data transformations between components
- Ensure consistent data formats across boundaries
- Validate data integrity through the system
- Implement appropriate error handling at integration points

### Dependency Management
- Clearly document component dependencies
- Manage version compatibility between components
- Minimize coupling between components
- Design for fault tolerance when dependencies fail
```

### 5. Continuous Validation

Verify throughout the development process:

```markdown
## Continuous Validation

### Automated Testing
- Implement unit tests for all components
- Create integration tests for component interactions
- Develop end-to-end tests for critical paths
- Automate test execution for quick feedback

### Manual Validation
- Perform exploratory testing for complex scenarios
- Validate edge cases not covered by automated tests
- Verify user experience for user-facing components
- Review error handling and recovery procedures

### Non-Functional Validation
- Verify performance against requirements
- Validate security controls and practices
- Test for accessibility compliance
- Ensure observability and monitoring
```

### 6. Documentation

Document implementation alongside development:

```markdown
## Implementation Documentation

### Code Documentation
- Document interfaces and public APIs
- Include comments for complex logic
- Document design decisions and rationale
- Provide examples for non-obvious usage

### Technical Documentation
- Update design documents with implementation details
- Document configuration options and parameters
- Create operational documentation for deployment and monitoring
- Document known limitations and constraints

### Knowledge Transfer
- Document lessons learned during implementation
- Create onboarding materials for new team members
- Document troubleshooting approaches
- Update FAQ and knowledge base
```

## Meta-Systemic Principle Application

### Parsimony
- Reuse existing components where appropriate
- Create shared utilities for common functionality
- Define canonical data structures and reference them
- Avoid duplicating functionality across components

Example:
```typescript
// INSTEAD OF duplicating validation logic:
function validateUserInput(input) {
  // Duplicate validation logic
}

// DO THIS - reference shared validation module:
import { validateInput } from '../common/validation';

function validateUserInput(input) {
  return validateInput(input, 'user');
}
```

### Tensegrity
- Ensure components provide value to each other
- Design resilient connections between components
- Balance responsibilities across the system
- Document bidirectional dependencies

Example:
```typescript
// Define how components support each other
class UserService {
  constructor(
    private profileService: ProfileService,
    private notificationService: NotificationService
  ) {}
  
  // UserService provides value to NotificationService
  getUserNotificationPreferences(userId: string): NotificationPreferences {
    return this.profileService.getNotificationPreferences(userId);
  }
  
  // UserService consumes value from NotificationService
  async updateUser(user: User): Promise<User> {
    const updatedUser = await this.saveUser(user);
    await this.notificationService.notifyUserUpdated(user.id);
    return updatedUser;
  }
}
```

### Modularity
- Maintain clear component boundaries
- Define explicit interfaces between components
- Encapsulate implementation details
- Design for independent evolution

Example:
```typescript
// Define clear interfaces
interface DataStore {
  get(key: string): Promise<any>;
  set(key: string, value: any): Promise<void>;
  delete(key: string): Promise<void>;
}

// Implement behind interface
class RedisDataStore implements DataStore {
  // Implementation details encapsulated
  private client: RedisClient;
  
  constructor(config: RedisConfig) {
    this.client = new RedisClient(config);
  }
  
  async get(key: string): Promise<any> {
    const data = await this.client.get(key);
    return data ? JSON.parse(data) : null;
  }
  
  // Other methods...
}
```

### Coherence
- Follow consistent patterns across the codebase
- Use established naming conventions
- Apply error handling consistently
- Structure similar components similarly

Example:
```typescript
// Consistent error handling pattern
async function fetchUserData(userId: string): Promise<UserData> {
  try {
    const response = await api.get(`/users/${userId}`);
    return response.data;
  } catch (error) {
    if (error.status === 404) {
      throw new ResourceNotFoundError('User not found', { userId });
    }
    throw new ApiError('Failed to fetch user data', { userId, cause: error });
  }
}

async function fetchProductData(productId: string): Promise<ProductData> {
  try {
    const response = await api.get(`/products/${productId}`);
    return response.data;
  } catch (error) {
    if (error.status === 404) {
      throw new ResourceNotFoundError('Product not found', { productId });
    }
    throw new ApiError('Failed to fetch product data', { productId, cause: error });
  }
}
```

### Clarity
- Document interfaces with examples
- Explain complex logic with comments
- Use clear, descriptive naming
- Document design decisions and rationale

Example:
```typescript
/**
 * Processes user data according to application rules.
 * 
 * @param userData - Raw user data to process
 * @param options - Processing options
 * @returns Processed user data ready for storage
 * 
 * @example
 * // Process user with default options
 * const processed = processUserData({ name: "John Doe", email: "john@example.com" });
 * 
 * @example
 * // Process user with specific options
 * const processed = processUserData(
 *   { name: "John Doe", email: "john@example.com" },
 *   { normalizeNames: true, validateEmail: true }
 * );
 */
function processUserData(userData: UserInput, options: ProcessOptions = {}): UserData {
  // Implementation with clear comments
}
```

### Adaptivity
- Adapt implementation to specific contexts
- Preserve core patterns while allowing variation
- Document context-specific adaptations
- Design for future evolution

Example:
```typescript
// Base pattern with context-specific adaptations
interface PaymentProcessor {
  processPayment(amount: number, paymentInfo: PaymentInfo): Promise<PaymentResult>;
}

// Context: Standard e-commerce
class StandardPaymentProcessor implements PaymentProcessor {
  async processPayment(amount: number, paymentInfo: PaymentInfo): Promise<PaymentResult> {
    // Standard implementation
  }
}

// Context: High-security financial transactions
class SecurePaymentProcessor implements PaymentProcessor {
  async processPayment(amount: number, paymentInfo: PaymentInfo): Promise<PaymentResult> {
    // Enhanced security implementation
    // Additional verification steps
    // More extensive logging
  }
}
```

## Context-Specific Development Approaches

### For Code System Development
- Focus on technical implementation details
- Apply design patterns appropriate to the technology stack
- Emphasize code quality and testability
- Create comprehensive automated tests
- Document APIs and integration points

Example approaches:
- Test-Driven Development for core components
- Behavior-Driven Development for user-facing features
- Pair programming for complex implementations
- Code reviews for quality assurance

### For Release System Development
- Focus on process implementation and workflow
- Develop templates and documentation
- Create rule files and validation criteria
- Update process guidance
- Emphasize documentation and examples

Example approaches:
- Template-driven development
- Documentation-first approach
- Example-based implementation
- Validation-driven development

### For Agent System Development
- Focus on capability enhancement and knowledge integration
- Develop prompt templates and interaction patterns
- Create knowledge structures and references
- Update guidance rules
- Emphasize example-based validation

Example approaches:
- Example-driven development
- Interaction pattern modeling
- Knowledge graph enhancement
- Capability-based implementation

## Release Scope-Specific Considerations

### Major Release Development
- Comprehensive implementation of new architecture
- Careful refactoring of existing components
- Extensive testing at all levels
- Detailed documentation updates
- Cross-component integration planning

### Minor Release Development
- Focused feature implementation
- Limited refactoring of affected components
- Feature-specific testing with regression tests
- Targeted documentation updates
- Component-level integration

### Patch Release Development
- Minimal, precise code changes
- No architectural changes
- Targeted testing of fixed issues with regression tests
- Focused documentation updates
- Minimal integration impact

### Emergency Release Development
- Surgical code changes only
- Strict focus on the specific issue
- Critical path testing only
- Essential documentation updates
- Minimal integration footprint

## Development Phase Quality Checklist

Before concluding the development phase, verify that:

- [ ] All planned functionality is implemented
- [ ] Implementations follow established patterns
- [ ] Components are properly integrated
- [ ] Documentation is complete and accurate
- [ ] Automated tests verify functional requirements
- [ ] Non-functional requirements are validated
- [ ] Code quality standards are met
- [ ] Technical debt is documented if created
- [ ] Implementation aligns with architectural guidance
- [ ] Meta-systemic principles have been applied appropriately

## Human-AI Collaboration in Development

In our two-person team:

### Human Team Member Focus
- Making key architectural decisions
- Resolving complex technical challenges
- Evaluating trade-offs and priorities
- Providing domain expertise
- Approving significant design changes

### AI Agent Focus
- Generating implementation based on established patterns
- Ensuring documentation completeness
- Verifying consistency across components
- Identifying potential principle violations
- Suggesting optimization approaches

<important>
The development phase is where the quality of the final delivery is established. Focus on incremental delivery, consistent pattern application, and continuous validation to ensure that the implementation meets requirements while maintaining system integrity.
</important>