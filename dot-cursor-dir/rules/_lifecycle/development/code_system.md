---
description: 
globs: **/code/development/*.md,**/code/development/*.mdx,**/releases/*/code_development.md,**/releases/*/code_development.mdx,**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Code-specific guidance for the development phase of the release lifecycle"
globs: "**/src/**/*.{py,js,ts,jsx,tsx,java,c,cpp,cs,go,rs,php,rb},**/tests/**/*.{py,js,ts,jsx,tsx,java,feature,test.*,spec.*}"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code System Development Guidance

<critical>
This rule provides specialized guidance for the development phase when the primary system context is code-based system development. Apply these guidelines in conjunction with the core development phase rules to ensure high-quality implementation that adheres to meta-systemic principles.
</critical>

## Code System Implementation Approach

When implementing code-based system changes:

### 1. Technical Foundation

Begin by establishing the proper technical foundation:

```markdown
## Technical Foundation

### Development Environment Setup
- Configure consistent development environment across team members
- Set up required dependencies, libraries, and tools
- Establish proper version control workflow
- Configure automated builds and quality checks
- Set up appropriate logging and debugging tools

### Code Organization
- Follow established project structure conventions
- Maintain logical file and module organization
- Use consistent naming patterns across the codebase
- Place files according to their functional responsibilities
- Establish clear interfaces between components

### Reference Implementation
- Identify canonical examples of similar patterns in the codebase
- Review architectural documentation for guidance
- Understand integration points with existing components
- Examine related test implementations
```

### 2. Incremental Implementation Strategy

Break down implementation into clear, manageable increments:

```markdown
## Incremental Implementation Strategy

### Foundation Increment
- Establish basic structure and interfaces
- Create minimal skeleton implementation
- Set up required infrastructure
- Focus on architectural correctness
- Create foundational tests

### Core Functionality Increment
- Implement primary features and functionality
- Focus on the happy path scenarios
- Ensure basic functionality works end-to-end
- Implement core business logic
- Create comprehensive unit tests

### Robustness Increment
- Add error handling and edge cases
- Implement validation and error recovery
- Add logging and observability
- Enhance security controls
- Create tests for error scenarios

### Optimization Increment
- Improve performance and efficiency
- Refine algorithms and data structures
- Optimize resource usage
- Address technical debt
- Benchmark and validate performance
```

### 3. Test-Driven Development Approach

Apply test-driven development where appropriate:

```markdown
## Test-Driven Development Approach

### TDD Workflow
1. **Write failing test** that defines expected behavior
2. **Implement minimum code** to pass the test
3. **Refactor** while keeping tests passing
4. **Repeat** for each specific behavior

### Test Strategy
- **Unit tests**: Verify isolated component behavior
- **Integration tests**: Verify component interactions
- **Functional tests**: Verify feature behavior
- **Performance tests**: Verify efficiency and scalability
- **Security tests**: Verify security controls

### Test Design
- Test one behavior per test case
- Use descriptive test names that explain intent
- Structure tests with arrange-act-assert pattern
- Include tests for error cases and edge conditions
- Create data factories for consistent test data
```

### 4. Code Quality Standards

Maintain high code quality throughout development:

```markdown
## Code Quality Standards

### Readability
- Write self-documenting code with clear intent
- Choose descriptive names for variables, functions, and classes
- Keep functions and methods focused on single responsibilities
- Use consistent formatting and style
- Follow language idioms and conventions

### Maintainability
- Keep complexity manageable (cyclomatic complexity < 10)
- Limit function/method size (preferably < 30 lines)
- Create modular, reusable components
- Document non-obvious design decisions
- Minimize dependencies between components

### Robustness
- Validate inputs and preconditions
- Handle errors gracefully and consistently
- Implement comprehensive error recovery
- Design for resilience against failures
- Create defensive coding practices

### Performance
- Optimize critical paths for efficiency
- Minimize resource usage and contention
- Reduce unnecessary operations
- Use appropriate data structures and algorithms
- Consider caching for expensive operations
```

### 5. Component Integration

Ensure proper integration between components:

```markdown
## Component Integration

### Interface Contracts
- Define clear contracts between components
- Document expected inputs and outputs
- Specify error handling responsibilities
- Define performance expectations
- Document thread safety and concurrency assumptions

### Integration Patterns
- Implement dependency injection for loose coupling
- Use interface-based design for flexible integration
- Apply consistent error propagation
- Create resilient communication between components
- Document integration points clearly

### Backward Compatibility
- Maintain compatibility with existing clients when possible
- Implement versioning for breaking changes
- Create migration paths for incompatible changes
- Document breaking changes clearly
- Consider supporting both old and new interfaces during transition
```

### 6. Technical Documentation

Create appropriate technical documentation:

```markdown
## Technical Documentation

### Code-Level Documentation
- Document public APIs comprehensively
- Add comments for complex algorithms or non-obvious code
- Include examples for usage patterns
- Document preconditions and postconditions
- Explain important design decisions

### Component Documentation
- Create high-level component documentation
- Document component responsibilities and boundaries
- Explain integration with other components
- Include configuration options
- Provide troubleshooting guidance

### Implementation Notes
- Document performance characteristics
- Note potential issues or limitations
- Document workarounds for known problems
- Include future enhancement opportunities
- Record implementation trade-offs
```

## Meta-Systemic Principle Application

### Parsimony
- Reuse existing code patterns and components
- Leverage shared libraries and utilities
- Avoid duplicating functionality
- Create reusable abstractions for common patterns

Example:
```typescript
// INSTEAD OF duplicating validation logic:
function validateUserInput(input) {
  // Duplicate validation logic here
}

// DO THIS - reference shared validation module:
import { validateInput } from '@/common/validation';

function validateUserInput(input) {
  return validateInput(input, 'user');
}
```

### Tensegrity
- Create balanced dependencies between components
- Design for resilience when dependencies fail
- Establish clear responsibility boundaries
- Implement supportive component relationships

Example:
```typescript
// Balanced component relationship
class OrderService {
  constructor(
    private productService: ProductService,
    private customerService: CustomerService,
    private notificationService: NotificationService
  ) {}
  
  // OrderService uses ProductService
  async createOrder(order: OrderData): Promise<Order> {
    // Verify products are available
    await this.productService.checkAvailability(order.items);
    // Create order implementation
    // ...
  }
  
  // OrderService provides value to ProductService
  async getOrdersForProduct(productId: string): Promise<Order[]> {
    // Retrieve orders for a specific product
    return this.orderRepository.findByProductId(productId);
  }
}
```

### Modularity
- Define clear component boundaries
- Create explicit interfaces between modules
- Encapsulate internal implementation details
- Design for independent evolution of components

Example:
```typescript
// Clear interface definition
interface PaymentProcessor {
  processPayment(amount: number, method: PaymentMethod): Promise<PaymentResult>;
  refundPayment(transactionId: string, amount: number): Promise<RefundResult>;
  getTransactionStatus(transactionId: string): Promise<TransactionStatus>;
}

// Implementation with encapsulated details
class StripePaymentProcessor implements PaymentProcessor {
  private apiClient: StripeClient;
  
  constructor(config: StripeConfig) {
    this.apiClient = new StripeClient(config);
  }
  
  // Implementation of public interface
  async processPayment(amount: number, method: PaymentMethod): Promise<PaymentResult> {
    // Implementation details hidden from consumers
    // ...
  }
  
  // Other interface methods...
}
```

### Coherence
- Follow consistent patterns across the codebase
- Use established naming conventions
- Implement standard error handling approaches
- Apply consistent architectural patterns

Example:
```typescript
// Consistent error handling pattern
class ServiceError extends Error {
  constructor(message: string, public readonly code: string, public readonly context: Record<string, any>) {
    super(message);
    this.name = this.constructor.name;
  }
}

class ResourceNotFoundError extends ServiceError {
  constructor(resource: string, id: string, context?: Record<string, any>) {
    super(`${resource} with ID ${id} not found`, 'NOT_FOUND', { resource, id, ...context });
  }
}

// Usage in services
class UserService {
  async getUser(id: string): Promise<User> {
    const user = await this.userRepository.findById(id);
    if (!user) {
      throw new ResourceNotFoundError('User', id);
    }
    return user;
  }
}

class ProductService {
  async getProduct(id: string): Promise<Product> {
    const product = await this.productRepository.findById(id);
    if (!product) {
      throw new ResourceNotFoundError('Product', id);
    }
    return product;
  }
}
```

### Clarity
- Write self-documenting code with clear intent
- Include comments for complex logic
- Create comprehensive documentation
- Provide examples for non-obvious usage

Example:
```typescript
/**
 * Processes payment for an order using the specified payment method.
 * 
 * @param orderId - The ID of the order to process payment for
 * @param paymentDetails - Payment information including method and credentials
 * @param options - Additional options for payment processing
 * @returns A result object containing the transaction ID and status
 * @throws PaymentValidationError if payment details are invalid
 * @throws PaymentProcessingError if payment cannot be processed
 * 
 * @example
 * // Process a standard credit card payment
 * const result = await processPayment('order-123', {
 *   method: 'credit_card',
 *   cardToken: 'tok_visa',
 *   billingAddress: { ... }
 * });
 * 
 * @example
 * // Process payment with custom options
 * const result = await processPayment('order-123', {
 *   method: 'paypal',
 *   accountToken: 'pp_token'
 * }, { 
 *   captureImmediately: true,
 *   sendReceipt: true
 * });
 */
async function processPayment(
  orderId: string, 
  paymentDetails: PaymentDetails,
  options: PaymentOptions = {}
): Promise<PaymentResult> {
  // Implementation with clear, descriptive variable names
  // and well-structured logic
}
```

### Adaptivity
- Design for different operational contexts
- Create flexible implementations that handle varying requirements
- Allow appropriate customization while maintaining core functionality
- Document context-specific adaptations

Example:
```typescript
// Context-sensitive implementation
class LoggingService {
  constructor(private config: LoggingConfig) {}
  
  // Base log method that adapts to context
  log(level: LogLevel, message: string, context?: Record<string, any>): void {
    // Adapt to different environments
    if (this.config.environment === 'production') {
      this.productionLog(level, message, context);
    } else if (this.config.environment === 'testing') {
      this.testingLog(level, message, context);
    } else {
      this.developmentLog(level, message, context);
    }
  }
  
  // Context-specific implementations
  private productionLog(level: LogLevel, message: string, context?: Record<string, any>): void {
    // Structured logging to centralized service
    // Sensitive data filtering
    // Rate limiting logic
  }
  
  private testingLog(level: LogLevel, message: string, context?: Record<string, any>): void {
    // Capture logs for test assertions
    // More verbose output
    // Test-specific context
  }
  
  private developmentLog(level: LogLevel, message: string, context?: Record<string, any>): void {
    // Console-friendly format
    // Full detail for debugging
    // Sourcemap support
  }
}
```

## Implementation Patterns by Architecture Type

### Monolithic Architecture

When developing monolithic applications:

1. **Component Boundaries**:
   - Use namespaces or modules to establish logical boundaries
   - Define clear interfaces between components
   - Maintain separation of concerns through package structure
   - Document component dependencies explicitly

2. **Shared Resources**:
   - Manage shared state carefully with proper access controls
   - Create service layers for shared functionality
   - Document shared resource usage patterns
   - Implement appropriate locking or concurrency control

3. **Layered Design**:
   - Implement clear separation between layers (presentation, business, data)
   - Control dependencies between layers (upper layers depend on lower layers)
   - Create appropriate abstraction at each layer boundary
   - Document flow through layers

### Microservice Architecture

When developing microservices:

1. **Service Boundaries**:
   - Define clear service responsibilities and boundaries
   - Design cohesive services around business capabilities
   - Implement strict encapsulation of service data
   - Document service APIs comprehensively

2. **Inter-Service Communication**:
   - Design resilient communication patterns
   - Implement proper error handling across service boundaries
   - Create backward-compatible API changes
   - Document communication contracts

3. **Service Independence**:
   - Design for independent deployment
   - Minimize runtime dependencies between services
   - Implement proper service discovery
   - Create resilience patterns for service failures

### Frontend Architecture

When developing frontend applications:

1. **Component Design**:
   - Create reusable UI components with clear interfaces
   - Implement proper state management
   - Design responsive and accessible interfaces
   - Document component usage with examples

2. **Data Flow**:
   - Implement consistent data flow patterns
   - Create clear separation between data and presentation
   - Design efficient backend communication
   - Document data transformation and handling

3. **User Experience**:
   - Implement consistent interaction patterns
   - Design for performance and responsiveness
   - Create appropriate loading and error states
   - Document UX decisions and patterns

## Technology-Specific Guidelines

### Object-Oriented Development

When using object-oriented programming:

1. **Class Design**:
   - Follow SOLID principles consistently
   - Create clear class hierarchies with appropriate inheritance
   - Use composition over inheritance where appropriate
   - Document class responsibilities and relationships

2. **Inheritance and Polymorphism**:
   - Design inheritance hierarchies carefully
   - Use interfaces to define contracts
   - Apply the Liskov Substitution Principle
   - Document intent of abstract classes and interfaces

3. **Design Patterns**:
   - Apply appropriate design patterns for common problems
   - Document pattern usage and rationale
   - Adapt patterns to specific context needs
   - Maintain consistency in pattern application

### Functional Development

When using functional programming:

1. **Pure Functions**:
   - Create pure functions without side effects
   - Design for immutability
   - Separate pure logic from side effects
   - Document function contracts clearly

2. **Composition**:
   - Compose functions to build complex behavior
   - Design appropriate data transformation pipelines
   - Use higher-order functions effectively
   - Document composition patterns

3. **State Management**:
   - Manage state changes explicitly
   - Use appropriate immutable data structures
   - Implement state transitions as transformations
   - Document state flow and transitions

### Asynchronous Development

When implementing asynchronous code:

1. **Async Patterns**:
   - Use consistent async patterns (promises, async/await, observables)
   - Handle errors properly in async contexts
   - Manage async resources appropriately
   - Document async behavior and expectations

2. **Concurrency**:
   - Design for appropriate concurrency control
   - Manage shared resources in concurrent contexts
   - Implement proper cancellation patterns
   - Document concurrency assumptions and limitations

3. **Error Handling**:
   - Implement consistent error handling for async operations
   - Propagate errors appropriately
   - Provide proper error context
   - Document error recovery strategies

## Quality Assurance Approaches

### Code Reviews

Effective code review approaches:

1. **Review Checklist**:
   - Verify principle application (parsimony, tensegrity, etc.)
   - Check adherence to coding standards
   - Validate test coverage and quality
   - Ensure documentation completeness

2. **Review Process**:
   - Review code in small, focused chunks
   - Provide constructive, specific feedback
   - Verify fixes for identified issues
   - Document significant design discussions

3. **Continuous Improvement**:
   - Identify patterns for improvement
   - Document learnings from reviews
   - Update standards based on review findings
   - Share knowledge across the team

### Automated Testing

Comprehensive testing approaches:

1. **Test Suite Structure**:
   - Organize tests to mirror code organization
   - Create appropriate test categories
   - Balance test types for effective coverage
   - Document test suite organization

2. **Test Quality**:
   - Write deterministic, reliable tests
   - Create tests that verify behavior, not implementation
   - Design tests for maintainability
   - Document test intent and assumptions

3. **Continuous Testing**:
   - Integrate tests into development workflow
   - Run tests automatically on changes
   - Prioritize fast feedback cycles
   - Document test execution environment

### Performance Optimization

Systematic performance improvement:

1. **Measurement**:
   - Establish baseline performance metrics
   - Measure against objective criteria
   - Use appropriate benchmarking tools
   - Document performance requirements and measurements

2. **Profiling**:
   - Identify performance bottlenecks systematically
   - Use appropriate profiling tools
   - Analyze resource usage patterns
   - Document profiling results and insights

3. **Optimization**:
   - Optimize critical paths based on measurements
   - Verify improvements with benchmarks
   - Document optimization techniques
   - Create performance regression tests

## Release Scope-Specific Considerations

### Major Release Development

For major release development:

- Comprehensive architecture and design documentation
- Thorough testing at all levels
- Detailed tracking of dependencies and interfaces
- Extensive knowledge sharing and team alignment
- Careful management of breaking changes

### Minor Release Development

For minor release development:

- Focused documentation for new features
- Targeted testing of new functionality with regression tests
- Management of interfaces for backward compatibility
- Appropriate knowledge sharing for feature changes
- Minimization of breaking changes

### Patch Release Development

For patch release development:

- Precise issue analysis and fixing
- Targeted testing focusing on fixed issues
- Minimal interface changes
- Documentation of bug fixes and workarounds
- Strong regression testing

### Emergency Release Development

For emergency release development:

- Surgical code changes with minimal scope
- Critical path testing with regression coverage
- No interface changes if possible
- Clear documentation of fixes
- Post-implementation comprehensive review

## Development Phase Quality Checklist

Before concluding the development phase, verify that:

- [ ] All planned functionality is implemented
- [ ] Code adheres to project quality standards
- [ ] Documentation is complete and accurate
- [ ] Test coverage is appropriate and all tests pass
- [ ] Performance meets requirements
- [ ] Security controls are properly implemented
- [ ] Accessibility requirements are met
- [ ] Code has been reviewed according to standards
- [ ] Technical debt has been documented
- [ ] Meta-systemic principles have been applied appropriately

## Human-AI Collaboration in Code Development

In our two-person team:

### Human Team Member Focus
- Making critical architecture and design decisions
- Providing domain expertise and business context
- Evaluating trade-offs for implementation approaches
- Identifying edge cases from experience
- Approving significant design choices

### AI Agent Focus
- Generating implementation based on established patterns
- Ensuring consistent application of coding standards
- Providing comprehensive documentation
- Identifying potential principle violations
- Suggesting optimization opportunities

<important>
Code system development requires balancing technical excellence with practical delivery. Focus on incremental implementation, proper application of meta-systemic principles, and continuous validation to ensure high-quality, maintainable code that achieves business objectives while evolving the system architecture appropriately.
</important>