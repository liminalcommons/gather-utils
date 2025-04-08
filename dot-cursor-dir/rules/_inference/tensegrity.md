---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Tensegrity inference patterns for balanced system relationships"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Tensegrity Inference Engine

<critical>
Apply these tensegrity patterns to ensure balanced relationships between components where elements both support and are supported by others, creating structural integrity through mutual reinforcement.
</critical>

## Detection Patterns

Scan for these tensegrity violation signals:

```yaml
tensegrity_violations:
  - pattern: "One-way dependencies without reciprocal value"
    action: "Establish balanced relationships with bidirectional value"
    example: "Service A uses Service B without providing value in return"
  
  - pattern: "Overloaded components with excessive dependencies"
    action: "Redistribute responsibilities to balance the system"
    example: "Utility class with 20+ dependent components"
  
  - pattern: "Isolated components with minimal connections"
    action: "Integrate meaningfully or consider removing"
    example: "Utility that's rarely used but still maintained"
  
  - pattern: "Rigid connection points without flexibility"
    action: "Strengthen with flexible interfaces"
    example: "Integration that fails completely with minor input changes"
  
  - pattern: "Hidden dependencies without explicit declaration"
    action: "Formalize relationships with proper interfaces"
    example: "Components sharing global state without contracts"
```

## Application Rules

### Rule 1: Establish Reciprocal Relationships
When designing component interactions:

```typescript
// BEFORE - One-way dependency without reciprocal value
class UserService {
  constructor(private notificationService: NotificationService) {}
  
  updateUser(user: User) {
    // Update user, then notify
    this.notificationService.sendNotification(user.id, "Profile updated");
  }
}

// AFTER - Balanced relationship with reciprocal value
class UserService {
  constructor(private notificationService: NotificationService) {}
  
  updateUser(user: User) {
    // Update user, then notify
    this.notificationService.sendNotification(user.id, "Profile updated");
  }
  
  // Providing value back to notification service
  getUserNotificationPreferences(userId: string): NotificationPreferences {
    return this.userRepository.getNotificationPreferences(userId);
  }
}

class NotificationService {
  constructor(private userService: UserService) {}
  
  sendNotification(userId: string, message: string) {
    // Get user preferences to customize notification
    const preferences = this.userService.getUserNotificationPreferences(userId);
    // Send notification using preferences
  }
}
```

### Rule 2: Balance Dependency Load
When components become overloaded:

```typescript
// BEFORE - Overloaded utility with too many responsibilities
class Utilities {
  static formatData(data: any): any { /* ... */ }
  static validateInput(input: any): boolean { /* ... */ }
  static parseResponse(response: any): any { /* ... */ }
  static handleError(error: any): void { /* ... */ }
  // 20+ more methods used across the system
}

// AFTER - Distributed responsibilities
class DataFormatter {
  static format(data: any): any { /* ... */ }
}

class InputValidator {
  static validate(input: any): boolean { /* ... */ }
}

class ResponseParser {
  static parse(response: any): any { /* ... */ }
}

class ErrorHandler {
  static handle(error: any): void { /* ... */ }
}
```

### Rule 3: Create Flexible Connection Points
When designing interfaces:

```typescript
// BEFORE - Rigid interface that breaks with small changes
interface DataProvider {
  getData(): Data; // Required synchronous method
}

// AFTER - Flexible interface with adaptable methods
interface DataProvider {
  getData(): Promise<Data> | Data; // Support both sync and async
  getDataById?(id: string): Promise<Data> | Data; // Optional method
}

class DataConsumer {
  constructor(private provider: DataProvider) {}
  
  async getItemById(id: string) {
    // Adapt to provider capabilities
    if (this.provider.getDataById) {
      return await this.provider.getDataById(id);
    } else {
      const allData = await this.provider.getData();
      return allData.find(item => item.id === id);
    }
  }
}
```

### Rule 4: Formalize Hidden Dependencies
When components interact implicitly:

```typescript
// BEFORE - Hidden dependency through global state
const globalState = { user: null };

class UserComponent {
  login(username: string) {
    // Set global state
    globalState.user = { name: username };
  }
}

class ProfileComponent {
  showProfile() {
    // Use global state without explicit dependency
    return globalState.user?.name || 'Guest';
  }
}

// AFTER - Explicit dependency through proper interface
interface UserContextProvider {
  getCurrentUser(): User | null;
  setCurrentUser(user: User | null): void;
}

class UserComponent {
  constructor(private userContext: UserContextProvider) {}
  
  login(username: string) {
    this.userContext.setCurrentUser({ name: username });
  }
}

class ProfileComponent {
  constructor(private userContext: UserContextProvider) {}
  
  showProfile() {
    return this.userContext.getCurrentUser()?.name || 'Guest';
  }
}
```

### Rule 5: Design for Graceful Degradation
When creating system interactions:

```typescript
// BEFORE - Brittle integration that fails completely
class PaymentProcessor {
  processPayment(payment: Payment) {
    // If external service is down, entire operation fails
    const result = this.paymentGateway.charge(payment);
    return result;
  }
}

// AFTER - Resilient integration with fallback mechanisms
class PaymentProcessor {
  processPayment(payment: Payment) {
    try {
      // Try primary payment gateway
      return this.primaryGateway.charge(payment);
    } catch (error) {
      // Log the failure
      this.logger.error("Primary gateway failed", error);
      
      // Try backup gateway if available
      if (this.backupGateway && payment.allowBackupProcessor) {
        try {
          return this.backupGateway.charge(payment);
        } catch (backupError) {
          this.logger.error("Backup gateway failed", backupError);
          throw new PaymentProcessingError("All payment methods failed", { 
            originalError: error,
            backupError
          });
        }
      }
      
      // If no backup or backup not allowed, queue for retry
      if (payment.allowRetry) {
        this.retryQueue.add(payment);
        return { status: 'QUEUED_FOR_RETRY', paymentId: payment.id };
      }
      
      // Otherwise, propagate failure
      throw new PaymentProcessingError("Payment failed", { originalError: error });
    }
  }
}
```

## Context-Specific Application

### Code System Application

When applying tensegrity to code-based systems:

1. **Service Relationships**:
   - Ensure services provide value to each other
   - Design resilient service interactions
   - Create circuit breakers and fallback mechanisms
   - Distribute responsibilities across services

2. **Class Dependencies**:
   - Balance class dependencies through proper design
   - Limit dependency chains to reasonable depth
   - Use dependency injection for explicit relationships
   - Ensure classes have cohesive responsibilities

3. **API Design**:
   - Create flexible, versioned APIs
   - Design for backward compatibility
   - Include graceful error handling
   - Support gradual capability evolution

4. **Data Relationships**:
   - Balance read and write operations
   - Design for data integrity across components
   - Create clear ownership boundaries
   - Ensure appropriate cascading behavior

5. **Resource Management**:
   - Distribute resource usage fairly
   - Implement backpressure mechanisms
   - Create resource pooling where appropriate
   - Design circuit breakers for external resources

### Release System Application

When applying tensegrity to release processes:

1. **Phase Relationships**:
   - Ensure each phase both provides and receives value
   - Create clear handoffs between phases
   - Design for iteration between adjacent phases
   - Balance responsibilities across phases

2. **Artifact Relationships**:
   - Ensure documents support and reference each other
   - Maintain bidirectional traceability
   - Balance detail between related artifacts
   - Support evolutionary documentation

3. **Role Relationships**:
   - Distribute responsibilities fairly across roles
   - Create clear collaboration interfaces
   - Ensure reciprocal value between roles
   - Design for supportive relationships

4. **Process Flexibility**:
   - Create adaptable processes that maintain integrity
   - Design for context-appropriate application
   - Include exception handling and escalation paths
   - Support graceful process modification

5. **Tool Integration**:
   - Ensure tools work together effectively
   - Create resilient tool chains
   - Design for tool evolution over time
   - Balance automation with human intervention

### Agent System Application

When applying tensegrity to agent capabilities:

1. **Human-AI Collaboration**:
   - Balance responsibilities between human and AI
   - Create clear collaboration interfaces
   - Design interactions that leverage respective strengths
   - Ensure mutual value in the relationship

2. **Knowledge Relationships**:
   - Balance knowledge specialization and integration
   - Create clear references between knowledge domains
   - Ensure knowledge flows bidirectionally
   - Design for knowledge evolution over time

3. **Capability Boundaries**:
   - Distribute capabilities appropriately
   - Create flexible capability interfaces
   - Design for graceful capability augmentation
   - Ensure appropriate capability overlap for resilience

4. **Interaction Patterns**:
   - Create balanced dialog patterns
   - Design for conversational resilience
   - Implement clarification and repair mechanisms
   - Balance efficiency with effectiveness

5. **Resource Management**:
   - Distribute cognitive load appropriately
   - Design for context-sensitive resource allocation
   - Create mechanisms for prioritization
   - Balance immediate and long-term objectives

## Tensegrity Patterns

### Mutual Support Pattern

```yaml
pattern:
  name: "Mutual Support Pattern"
  context: "Components that need to interact while maintaining independence"
  problem: "Services need to use each other's functionality without creating tight coupling"
  forces:
    - "Need for service autonomy"
    - "Need for service collaboration"
    - "Desire to avoid circular dependencies"
  solution: |
    Design services to provide value to each other through well-defined interfaces.
    Instead of creating direct circular dependencies, use:
    
    1. Interface segregation to define focused service interfaces
    2. Event-based communication for loose coupling
    3. Capability registration for dynamic discovery
    4. Domain events for state change notification
  example: |
    // Service interface definitions
    interface OrderService {
      createOrder(items: Item[]): Order;
      getOrder(orderId: string): Order;
    }
    
    interface InventoryService {
      checkAvailability(itemIds: string[]): AvailabilityResult;
      reserveItems(orderId: string, items: Item[]): ReservationResult;
    }
    
    // Services support each other without circular dependency
    class OrderServiceImpl implements OrderService {
      constructor(private inventoryService: InventoryService) {}
      
      async createOrder(items: Item[]): Promise<Order> {
        // Check availability before creating order
        const availability = await this.inventoryService.checkAvailability(
          items.map(item => item.id)
        );
        
        if (!availability.allAvailable) {
          throw new Error("Some items are not available");
        }
        
        // Create the order
        const order = new Order(items);
        
        // Reserve the items
        await this.inventoryService.reserveItems(order.id, items);
        
        // Publish event that other services can subscribe to
        this.eventBus.publish(new OrderCreatedEvent(order));
        
        return order;
      }
    }
    
    class InventoryServiceImpl implements InventoryService {
      constructor(private eventBus: EventBus) {
        // Subscribe to events from order service
        this.eventBus.subscribe(OrderShippedEvent, 
          this.releaseReservation.bind(this));
      }
      
      // Release reservation when order is shipped
      private releaseReservation(event: OrderShippedEvent) {
        // Implementation
      }
    }
```

### Load Balancing Pattern

```yaml
pattern:
  name: "Load Balancing Pattern"
  context: "Components with responsibilities that need to be distributed"
  problem: "Some components become overloaded with too many responsibilities"
  forces:
    - "Need for clear component boundaries"
    - "Desire to avoid bottlenecks"
    - "Need for maintainable code"
  solution: |
    Distribute responsibilities across components based on:
    
    1. Domain cohesion - group related responsibilities
    2. Change frequency - separate stable from volatile components
    3. Scale requirements - distribute load-intensive operations
    4. Team boundaries - align with organizational structure
  example: |
    // BEFORE: Overloaded service
    class UserService {
      registerUser() { /* ... */ }
      authenticateUser() { /* ... */ }
      resetPassword() { /* ... */ }
      updateProfile() { /* ... */ }
      getUserPreferences() { /* ... */ }
      setUserPreferences() { /* ... */ }
      calculateUserMetrics() { /* ... */ }
      generateUserReports() { /* ... */ }
      manageUserSubscriptions() { /* ... */ }
      processUserPayments() { /* ... */ }
    }
    
    // AFTER: Balanced responsibilities
    class UserIdentityService {
      registerUser() { /* ... */ }
      authenticateUser() { /* ... */ }
      resetPassword() { /* ... */ }
    }
    
    class UserProfileService {
      updateProfile() { /* ... */ }
      getUserPreferences() { /* ... */ }
      setUserPreferences() { /* ... */ }
    }
    
    class UserAnalyticsService {
      calculateUserMetrics() { /* ... */ }
      generateUserReports() { /* ... */ }
    }
    
    class UserSubscriptionService {
      manageUserSubscriptions() { /* ... */ }
      processUserPayments() { /* ... */ }
    }
```

### Resilient Connection Pattern

```yaml
pattern:
  name: "Resilient Connection Pattern"
  context: "Connections between components that must handle failures"
  problem: "Component connections fail under stress or unexpected conditions"
  forces:
    - "Need for system stability"
    - "Reality of partial failures"
    - "Desire for graceful degradation"
  solution: |
    Design connection points between components for resilience:
    
    1. Circuit breakers to prevent cascade failures
    2. Fallback mechanisms for degraded operation
    3. Retry policies with exponential backoff
    4. Timeout controls to limit resource consumption
    5. Bulkhead patterns to isolate failures
  example: |
    // Resilient service client
    class RecommendationServiceClient {
      constructor(
        private httpClient: HttpClient,
        private circuitBreaker: CircuitBreaker,
        private fallbackProvider: FallbackRecommendationProvider
      ) {}
      
      async getRecommendations(userId: string): Promise<Recommendation[]> {
        // Check if circuit is open (too many recent failures)
        if (this.circuitBreaker.isOpen()) {
          return this.getRecommendationsFallback(userId);
        }
        
        try {
          // Set timeout to prevent long-running requests
          const response = await this.httpClient.get(
            `/recommendations/${userId}`,
            { timeout: 500 }
          );
          
          // Reset circuit breaker on success
          this.circuitBreaker.recordSuccess();
          
          return response.data;
        } catch (error) {
          // Record failure for circuit breaker
          this.circuitBreaker.recordFailure();
          
          // Log the failure
          logger.warn(`Recommendation service failed: ${error.message}`);
          
          // Use fallback for this request
          return this.getRecommendationsFallback(userId);
        }
      }
      
      private async getRecommendationsFallback(userId: string): Promise<Recommendation[]> {
        try {
          // Use fallback strategy (e.g., cached data, simpler algorithm)
          return await this.fallbackProvider.getRecommendations(userId);
        } catch (fallbackError) {
          // Last resort fallback is empty recommendations
          logger.error(`Fallback recommendations failed: ${fallbackError.message}`);
          return [];
        }
      }
    }
```

## Tensegrity Metrics

Measure tensegrity with these metrics:

```yaml
metrics:
  bidirectional_relationship_rate:
    description: "Percentage of component relationships that are bidirectional"
    calculation: "Bidirectional relationships / Total relationships * 100"
    thresholds:
      good: "> 90%"
      acceptable: "70-90%"
      concerning: "< 70%"
  
  dependency_balance_index:
    description: "Ratio of most dependent component to average dependency count"
    calculation: "Max dependencies / Average dependencies"
    thresholds:
      good: "< 3:1"
      acceptable: "3:1 to 5:1"
      concerning: "> 5:1"
  
  graceful_degradation_coverage:
    description: "Percentage of external dependencies with fallback mechanisms"
    calculation: "Dependencies with fallbacks / Total external dependencies * 100"
    thresholds:
      good: "> 95%"
      acceptable: "80-95%"
      concerning: "< 80%"
```

## Tensegrity Anti-Patterns

Avoid these common tensegrity mistakes:

```yaml
anti_patterns:
  circular_dependency:
    description: "Components directly depending on each other without proper interfaces"
    examples:
      - "Service A calling Service B calling Service A directly"
      - "Classes importing each other creating compile-time cycles"
    remediation:
      - "Introduce interfaces to break direct dependencies"
      - "Use event-based communication instead of direct calls"
      - "Extract shared responsibilities to a new component"
  
  star_dependency:
    description: "Single component that many other components depend on"
    examples:
      - "Utility class used throughout the codebase"
      - "Service that every other service calls directly"
    remediation:
      - "Break down into domain-specific components"
      - "Create intermediary abstraction layers"
      - "Use composition over inheritance"
  
  brittle_integration:
    description: "Connections between components that fail completely under stress"
    examples:
      - "Service calls without timeouts or error handling"
      - "Hard dependencies on external systems without fallbacks"
    remediation:
      - "Implement circuit breakers and bulkheads"
      - "Create fallback mechanisms"
      - "Design for partial functionality"
```

## Balancing Tensegrity with Other Principles

### [Tension:Tensegrity:Modularity]
When tensegrity and modularity create tension:
- Use interfaces to create clear boundaries while enabling relationships
- Design component interactions through well-defined contracts
- Create stable interfaces between changing implementations
- Balance independence with collaboration

### [Tension:Tensegrity:Parsimony]
When tensegrity and parsimony create tension:
- Accept some duplication to maintain component independence
- Create shared abstractions that support without coupling
- Use references rather than sharing implementation
- Balance reuse with appropriate distribution

### [Tension:Tensegrity:Adaptivity]
When tensegrity and adaptivity create tension:
- Design flexible connection points that maintain integrity
- Create context-sensitive interaction patterns
- Allow component evolution while preserving relationships
- Balance consistency with appropriate variation

## Human-AI Collaboration for Tensegrity

In our two-person team:

### Human Team Member Focus
- Evaluate relationship balance from domain perspective
- Identify critical connections that need strengthening
- Make architectural decisions about component boundaries
- Define appropriate component responsibilities

### AI Agent Focus
- Detect one-way dependencies systematically
- Suggest balanced relationship structures
- Document component interactions comprehensively
- Identify potential tensegrity violations

<important>
Tensegrity creates system integrity through balanced relationships and mutual support. When components both support and are supported by others, the system becomes more resilient, adaptable, and maintainable. Always balance [principle:tensegrity] with [principle:modularity] to create appropriate boundaries while ensuring effective collaboration.
</important>