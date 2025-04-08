---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Modularity inference patterns for clear component boundaries"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Modularity Inference Engine

<critical>
Apply these modularity patterns to maintain clear boundaries and well-defined interfaces between components. Proper modularity enables independent evolution while ensuring effective integration.
</critical>

## Detection Patterns

Scan for these modularity violation signals:

```yaml
modularity_violations:
  - pattern: "Direct access to internal implementation details"
    action: "Encapsulate details and provide proper interfaces"
    example: "Directly accessing internal state of another component"
  
  - pattern: "Tangled dependencies across module boundaries"
    action: "Refactor to respect module boundaries"
    example: "Circular dependencies between components"
  
  - pattern: "Ambiguous responsibility boundaries"
    action: "Clarify and enforce component responsibilities"
    example: "Feature implemented across multiple components without clear ownership"
  
  - pattern: "Inconsistent interface contracts"
    action: "Standardize interfaces and maintain clear contracts"
    example: "Similar operations with different parameter patterns"
  
  - pattern: "God modules with too many responsibilities"
    action: "Split into focused modules with single responsibilities"
    example: "Utility class handling authentication, data processing, and UI rendering"
```

## Application Rules

### Rule 1: Clear Interface Contracts
When defining component interfaces:

```typescript
// BEFORE - Ambiguous interface without clear contract
function processData(data) {
  // Implementation varies based on mysterious data properties
  if (data.type === 'special') {
    // Special handling
  }
}

// AFTER - Clear interface contract
interface ProcessingOptions {
  strict?: boolean;
  format?: 'json' | 'xml' | 'text';
  version?: string;
}

function processData(data: Data, options?: ProcessingOptions): Result {
  // Implementation with clear expectations about inputs/outputs
  const config = { strict: false, format: 'json', ...options };
  // Processing with well-defined behavior
  return result;
}
```

### Rule 2: Proper Encapsulation
When organizing component internals:

```typescript
// BEFORE - Exposing implementation details
class UserManager {
  userRecords = []; // Directly accessible
  authenticationState = { loggedIn: false }; // Directly accessible
  
  login(username, password) {
    // Implementation
  }
}

// AFTER - Proper encapsulation
class UserManager {
  #userRecords = []; // Private implementation
  #authenticationState = { loggedIn: false }; // Private implementation
  
  login(username, password) {
    // Implementation
  }
  
  isLoggedIn() {
    return this.#authenticationState.loggedIn;
  }
  
  getUserCount() {
    return this.#userRecords.length;
  }
}
```

### Rule 3: Clear Responsibility Boundaries
When organizing functionality:

```typescript
// BEFORE - Mixed responsibilities
class DataHandler {
  fetchData() { /* Network code */ }
  processData() { /* Business logic */ }
  renderData() { /* UI rendering */ }
  saveToDatabase() { /* Database code */ }
}

// AFTER - Clear responsibility boundaries
class DataService {
  fetchData() { /* Network code */ }
  saveToDatabase() { /* Database code */ }
}

class DataProcessor {
  processData(rawData) { /* Business logic */ }
}

class DataRenderer {
  renderData(processedData) { /* UI rendering */ }
}

// Orchestrator that composes the components
class DataController {
  constructor(
    private service: DataService,
    private processor: DataProcessor,
    private renderer: DataRenderer
  ) {}
  
  async handleDataRequest() {
    const rawData = await this.service.fetchData();
    const processedData = this.processor.processData(rawData);
    this.renderer.renderData(processedData);
  }
}
```

### Rule 4: Dependency Inversion
When managing cross-module dependencies:

```typescript
// BEFORE - Direct dependency on implementation
class ReportGenerator {
  generateReport() {
    const database = new Database(); // Direct coupling
    const data = database.query('SELECT * FROM users');
    // Process and generate report
  }
}

// AFTER - Dependency inversion with interfaces
interface DataProvider {
  getData(): Promise<any[]>;
}

class DatabaseProvider implements DataProvider {
  getData(): Promise<any[]> {
    const database = new Database();
    return database.query('SELECT * FROM users');
  }
}

class ReportGenerator {
  constructor(private dataProvider: DataProvider) {}
  
  async generateReport() {
    const data = await this.dataProvider.getData();
    // Process and generate report
  }
}
```

### Rule 5: Consistent Boundary Protection
When establishing module boundaries:

```typescript
// BEFORE - Inconsistent boundary protection
class UserService {
  // Some methods validate input
  createUser(userData) {
    if (!userData.email) throw new Error('Email required');
    // Implementation
  }
  
  // Some methods don't validate
  updateUser(id, userData) {
    // Implementation without validation
  }
}

// AFTER - Consistent boundary protection
class UserService {
  // Input validation at all public boundaries
  createUser(userData) {
    this.validateUserData(userData);
    // Implementation
  }
  
  updateUser(id, userData) {
    this.validateId(id);
    this.validateUserData(userData, false); // false = partial validation for updates
    // Implementation
  }
  
  // Private validation methods
  private validateId(id) {
    if (!id) throw new Error('ID required');
    // Additional validation
  }
  
  private validateUserData(userData, isCreate = true) {
    // Common validation logic
    if (isCreate && !userData.email) throw new Error('Email required');
    // Additional validation
  }
}
```

## Context-Specific Application

Adapt modularity application based on the system context:

### Code System Application

When applying modularity to code:

1. **Component Boundaries**:
   - Define explicit public APIs for each component
   - Establish clear ownership for each module
   - Use language features to enforce encapsulation
   - Create interface contracts for cross-component interactions

2. **Dependency Management**:
   - Use dependency injection for cross-component dependencies
   - Apply dependency inversion at module boundaries
   - Create abstraction layers between major subsystems
   - Make dependencies explicit rather than implicit

3. **Package Organization**:
   - Group related functionality within cohesive packages
   - Separate interface definitions from implementations
   - Organize code to reflect architectural boundaries
   - Control visibility of internal implementation details

4. **Testing Isolation**:
   - Design components to be testable in isolation
   - Create test doubles for external dependencies
   - Verify behavior at component boundaries
   - Test interface contracts explicitly

5. **API Design**:
   - Design explicit, consistent APIs at module boundaries
   - Establish versioning strategies for public interfaces
   - Document interface contracts comprehensively
   - Provide client libraries for complex interfaces

### Release System Application

When applying modularity to release processes:

1. **Phase Boundaries**:
   - Define clear entry and exit criteria for each phase
   - Establish explicit interfaces between phases
   - Document phase responsibilities precisely
   - Create distinct artifacts at phase boundaries

2. **Process Modularity**:
   - Separate process concerns into cohesive activities
   - Create modular process components that can evolve independently
   - Define interfaces between process components
   - Maintain clear responsibility assignments

3. **Rule Organization**:
   - Structure rules to reflect natural boundaries
   - Separate core principles from specific applications
   - Create clear relationships between rule modules
   - Design rules for independent evolution

4. **Template Modularity**:
   - Create modular templates with clear sections
   - Allow section-specific evolution without affecting the whole
   - Establish consistent interfaces between template sections
   - Support template composition from modular components

5. **Documentation Structure**:
   - Organize documentation to reflect system boundaries
   - Create clear navigation between documentation modules
   - Maintain responsibility separation in documentation
   - Allow documentation components to evolve independently

### Agent System Application

When applying modularity to agent capabilities:

1. **Knowledge Domain Boundaries**:
   - Define clear knowledge domain boundaries
   - Establish interfaces between knowledge domains
   - Document domain responsibilities explicitly
   - Support independent evolution of domains

2. **Capability Modularity**:
   - Design capabilities as modular, composable units
   - Define clear interfaces for capability invocation
   - Separate core capabilities from context-specific adaptations
   - Enable independent enhancement of capabilities

3. **Interaction Patterns**:
   - Create modular, reusable interaction patterns
   - Define clear boundaries for different interaction types
   - Establish interfaces between interaction phases
   - Support pattern composition and adaptation

4. **Responsibility Boundaries**:
   - Define clear boundaries between human and AI responsibilities
   - Establish explicit handoff points between team members
   - Document responsibility interfaces comprehensively
   - Design for independent evolution of responsibilities

5. **Prompt Modularity**:
   - Design prompts with modular components
   - Create reusable prompt sections with clear interfaces
   - Support prompt composition from modular elements
   - Enable independent evolution of prompt components

## Modularity Metrics

Measure modularity application with these metrics:

```yaml
metrics:
  interface_completeness:
    description: "Percentage of components with explicit interface contracts"
    calculation: "Components with explicit interfaces / Total components * 100"
    thresholds:
      good: "> 95%"
      acceptable: "80-95%"
      concerning: "< 80%"
    
  encapsulation_integrity:
    description: "Percentage of implementation details properly encapsulated"
    calculation: "Properly encapsulated components / Total components * 100"
    thresholds:
      good: "> 90%"
      acceptable: "75-90%"
      concerning: "< 75%"
    
  dependency_inversion_rate:
    description: "Percentage of cross-module dependencies using dependency inversion"
    calculation: "Inverted dependencies / Total cross-module dependencies * 100"
    thresholds:
      good: "> 85%"
      acceptable: "70-85%"
      concerning: "< 70%"
```

## Modularity Anti-Patterns

Avoid these common modularity mistakes:

```yaml
anti_patterns:
  shotgun_surgery:
    description: "Changes requiring updates to multiple unrelated modules"
    examples:
      - "Simple feature requiring changes across 10+ files"
      - "Configuration change requiring updates to every module"
    remediation:
      - "Consolidate related functionality"
      - "Abstract common behavior"
      - "Implement proper dependency inversion"
      - "Create intermediate abstraction layers"
  
  feature_envy:
    description: "Module that excessively uses another module's internals"
    examples:
      - "Function accessing multiple private properties of another class"
      - "Component duplicating another component's logic"
    remediation:
      - "Move behavior to the appropriate module"
      - "Create proper interfaces for necessary access"
      - "Apply the Tell Don't Ask principle"
      - "Design for proper encapsulation"
  
  swiss_army_knife:
    description: "Module trying to do everything without clear focus"
    examples:
      - "Utility class with 100+ unrelated methods"
      - "Service implementing multiple unrelated responsibilities"
    remediation:
      - "Split into single-responsibility modules"
      - "Group related functionality in cohesive units"
      - "Define clear responsibility boundaries"
      - "Design explicit interfaces between modules"
```

## Balancing Modularity with Other Principles

### [Tension:Modularity:Tensegrity]
When modularity and tensegrity create tension:
- Design clear interfaces that enable strong relationships
- Create explicit communication channels without breaking encapsulation
- Use well-defined events and messaging for cross-boundary communication
- Maintain module independence while enabling effective collaboration

### [Tension:Modularity:Parsimony]
When modularity and parsimony create tension:
- Define canonical types at boundary interfaces
- Create shared modules for truly common functionality
- Use composition over inheritance to enable reuse while maintaining boundaries
- Balance module independence with appropriate sharing of common elements

### [Tension:Modularity:Adaptivity]
When modularity and adaptivity create tension:
- Create extension points and plugins for context-specific adaptations
- Design interfaces that accommodate variations without breaking
- Use strategy patterns to encapsulate variable behavior
- Balance stability of interfaces with flexibility of implementation

## Human-AI Team Collaboration for Modularity

In our two-person team:

### Human Team Member Focus
- Make architectural boundary decisions
- Define core component responsibilities
- Evaluate appropriateness of interfaces
- Assess tradeoffs between modularity and other concerns

### AI Agent Focus
- Identify potential boundary violations systematically
- Suggest interface improvements
- Generate consistent interface contracts
- Document boundaries and interfaces clearly

<important>
Modularity creates system integrity through clear boundaries and well-defined interfaces. When components have explicit responsibilities and clean interfaces, they can evolve independently while maintaining effective integration. Always balance [principle:modularity] with other principles, especially [principle:tensegrity], to ensure components maintain both independence and effective collaboration.
</important>