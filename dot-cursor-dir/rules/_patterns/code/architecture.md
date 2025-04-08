---
description: 
globs: **/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs
alwaysApply: false
---
---
description: "Code architecture patterns for meta-systemic principles"
globs: "**/*.py,**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.java,**/*.c,**/*.cpp,**/*.go,**/*.rs,**/*.php,**/*.rb,**/*.cs"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Code Architecture Patterns

<critical>
Apply these architecture patterns when designing, implementing, or refactoring code to embody meta-systemic principles. These patterns ensure structural integrity and maintainability across the codebase.
</critical>

## Pattern Application Process

When working with code architecture, follow this process:

1. **IDENTIFY** which principles are most relevant to the current architectural context
2. **SELECT** the appropriate patterns to apply
3. **IMPLEMENT** the patterns with context-appropriate adaptations
4. **VALIDATE** that the implementation maintains system integrity

## Core Architecture Patterns

### Component Boundary Patterns

```yaml
pattern:
  name: "Explicit Component Boundary"
  principles: [modularity, clarity]
  context: "Defining interfaces between components"
  application:
    - "Define explicit public interfaces"
    - "Hide implementation details"
    - "Document interface contracts"
    - "Validate boundary integrity"
  example: |
    // TypeScript example
    
    // Public interface definition
    export interface UserService {
      /**
       * Retrieves a user by their unique identifier.
       * @param id The user ID
       * @returns A promise that resolves to the user or null if not found
       * @throws AuthorizationError if the caller lacks permission
       */
      getUser(id: string): Promise<User | null>;
      
      /**
       * Creates a new user in the system.
       * @param userData The user data to create
       * @returns A promise that resolves to the created user
       * @throws ValidationError if the user data is invalid
       * @throws DuplicateError if a user with the same identifier exists
       */
      createUser(userData: UserCreationData): Promise<User>;
      
      // Other public methods...
    }
    
    // Implementation with hidden details
    class UserServiceImpl implements UserService {
      // Private implementation details
      #userRepository: UserRepository;
      #authService: AuthService;
      #validator: UserValidator;
      
      constructor(
        userRepository: UserRepository,
        authService: AuthService,
        validator: UserValidator
      ) {
        this.#userRepository = userRepository;
        this.#authService = authService;
        this.#validator = validator;
      }
      
      // Public interface implementation
      async getUser(id: string): Promise<User | null> {
        // Implementation of public method
        this.#validateAuthorization('getUser');
        return this.#userRepository.findById(id);
      }
      
      async createUser(userData: UserCreationData): Promise<User> {
        // Implementation of public method
        this.#validateAuthorization('createUser');
        this.#validator.validateUserCreation(userData);
        await this.#checkForDuplicates(userData);
        return this.#userRepository.create(userData);
      }
      
      // Private methods
      #validateAuthorization(operation: string): void {
        // Internal implementation detail
      }
      
      async #checkForDuplicates(userData: UserCreationData): Promise<void> {
        // Internal implementation detail
      }
    }
```

### Dependency Management Patterns

```yaml
pattern:
  name: "Explicit Dependency Injection"
  principles: [tensegrity, modularity]
  context: "Managing dependencies between components"
  application:
    - "Declare dependencies explicitly"
    - "Inject dependencies through constructors or parameters"
    - "Use interfaces for dependencies"
    - "Support testing with mock implementations"
  example: |
    // TypeScript example
    
    // Interface-based dependencies
    interface Logger {
      debug(message: string, context?: object): void;
      info(message: string, context?: object): void;
      warn(message: string, context?: object): void;
      error(message: string, error?: Error, context?: object): void;
    }
    
    interface ConfigProvider {
      get<T>(key: string, defaultValue?: T): T;
      has(key: string): boolean;
    }
    
    interface DatabaseConnection {
      query<T>(sql: string, params?: any[]): Promise<T[]>;
      execute(sql: string, params?: any[]): Promise<void>;
      transaction<T>(callback: (trx: Transaction) => Promise<T>): Promise<T>;
    }
    
    // Service with explicit dependencies
    class UserRepository {
      constructor(
        private readonly db: DatabaseConnection,
        private readonly logger: Logger,
        private readonly config: ConfigProvider
      ) {}
      
      async findById(id: string): Promise<User | null> {
        this.logger.debug('Looking up user by ID', { id });
        
        const tableName = this.config.get('tables.users', 'users');
        const query = `SELECT * FROM ${tableName} WHERE id = ?`;
        
        try {
          const results = await this.db.query<UserRecord>(query, [id]);
          return results.length > 0 ? this.mapToUser(results[0]) : null;
        } catch (error) {
          this.logger.error('Failed to find user by ID', error as Error, { id });
          throw new RepositoryError('Failed to find user', { cause: error });
        }
      }
      
      private mapToUser(record: UserRecord): User {
        // Mapping implementation
      }
    }
    
    // Testing with mock dependencies
    describe('UserRepository', () => {
      it('should find a user by ID', async () => {
        // Mock dependencies
        const mockDb = {
          query: jest.fn().mockResolvedValue([{ id: 'user1', name: 'Test User' }])
        } as unknown as DatabaseConnection;
        
        const mockLogger = {
          debug: jest.fn(),
          info: jest.fn(),
          warn: jest.fn(),
          error: jest.fn()
        } as Logger;
        
        const mockConfig = {
          get: jest.fn().mockReturnValue('users'),
          has: jest.fn()
        } as ConfigProvider;
        
        // Create repository with mock dependencies
        const repository = new UserRepository(mockDb, mockLogger, mockConfig);
        
        // Test the method
        const user = await repository.findById('user1');
        
        // Verify the result
        expect(user).not.toBeNull();
        expect(user?.id).toBe('user1');
        
        // Verify the dependencies were used correctly
        expect(mockDb.query).toHaveBeenCalledWith(
          'SELECT * FROM users WHERE id = ?',
          ['user1']
        );
        expect(mockLogger.debug).toHaveBeenCalled();
      });
    });
```

### Error Handling Patterns

```yaml
pattern:
  name: "Structured Error Management"
  principles: [clarity, coherence]
  context: "Handling and communicating errors"
  application:
    - "Create domain-specific error hierarchy"
    - "Include context information in errors"
    - "Preserve error chains for debugging"
    - "Handle errors at appropriate levels"
  example: |
    // TypeScript example
    
    // Base error class
    export class ApplicationError extends Error {
      constructor(
        message: string,
        public readonly code: string,
        public readonly context: Record<string, any> = {},
        public readonly cause?: Error
      ) {
        super(message);
        this.name = this.constructor.name;
        
        // Capture stack trace
        if (Error.captureStackTrace) {
          Error.captureStackTrace(this, this.constructor);
        }
        
        // Include cause in stack if available
        if (cause?.stack) {
          this.stack = `${this.stack}\nCaused by: ${cause.stack}`;
        }
      }
      
      // Helper to convert to response-safe format
      toPublicError(): PublicError {
        return {
          message: this.message,
          code: this.code,
          // Exclude sensitive context information
        };
      }
    }
    
    // Domain-specific error classes
    export class ValidationError extends ApplicationError {
      constructor(
        message: string,
        public readonly validationErrors: Record<string, string[]>,
        context: Record<string, any> = {},
        cause?: Error
      ) {
        super(
          message,
          'VALIDATION_ERROR',
          { ...context, validationErrors },
          cause
        );
      }
    }
    
    export class AuthorizationError extends ApplicationError {
      constructor(
        message: string,
        context: Record<string, any> = {},
        cause?: Error
      ) {
        super(message, 'AUTHORIZATION_ERROR', context, cause);
      }
    }
    
    export class ResourceNotFoundError extends ApplicationError {
      constructor(
        resource: string,
        id: string,
        context: Record<string, any> = {},
        cause?: Error
      ) {
        super(
          `${resource} with ID ${id} not found`,
          'RESOURCE_NOT_FOUND',
          { ...context, resource, id },
          cause
        );
      }
    }
    
    // Error handling in business logic
    class UserService {
      async updateUser(id: string, data: Partial<User>): Promise<User> {
        try {
          // Validate data
          const validationResult = this.validator.validate(data);
          if (!validationResult.valid) {
            throw new ValidationError(
              'Invalid user data',
              validationResult.errors,
              { userId: id }
            );
          }
          
          // Check authorization
          if (!this.authService.canUpdateUser(id)) {
            throw new AuthorizationError('Not authorized to update user', { userId: id });
          }
          
          // Find user
          const user = await this.userRepository.findById(id);
          if (!user) {
            throw new ResourceNotFoundError('User', id);
          }
          
          // Update user
          return await this.userRepository.update(id, data);
        } catch (error) {
          // Add context and rethrow if it's already our error type
          if (error instanceof ApplicationError) {
            throw error;
          }
          
          // Wrap unknown errors
          throw new ApplicationError(
            'Failed to update user',
            'UPDATE_USER_ERROR',
            { userId: id },
            error instanceof Error ? error : undefined
          );
        }
      }
    }
    
    // API layer error handling
    async function handleUserUpdate(req, res) {
      try {
        const user = await userService.updateUser(req.params.id, req.body);
        res.json(user);
      } catch (error) {
        if (error instanceof ValidationError) {
          return res.status(400).json(error.toPublicError());
        }
        
        if (error instanceof AuthorizationError) {
          return res.status(403).json(error.toPublicError());
        }
        
        if (error instanceof ResourceNotFoundError) {
          return res.status(404).json(error.toPublicError());
        }
        
        // Log unexpected errors
        logger.error('Unhandled error in user update', error);
        
        // Return generic error to client
        res.status(500).json({
          message: 'An unexpected error occurred',
          code: 'INTERNAL_ERROR'
        });
      }
    }
```

### Domain Model Patterns

```yaml
pattern:
  name: "Rich Domain Model"
  principles: [parsimony, coherence]
  context: "Implementing business logic in domain objects"
  application:
    - "Encapsulate business logic in domain objects"
    - "Define clear domain boundaries"
    - "Use value objects for immutable concepts"
    - "Validate domain invariants"
  example: |
    // TypeScript example
    
    // Value object
    class EmailAddress {
      private readonly value: string;
      
      constructor(email: string) {
        if (!EmailAddress.isValid(email)) {
          throw new ValidationError('Invalid email address', { email });
        }
        this.value = email.toLowerCase();
      }
      
      static isValid(email: string): boolean {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
      }
      
      toString(): string {
        return this.value;
      }
      
      equals(other: EmailAddress): boolean {
        return this.value === other.value;
      }
    }
    
    // Entity with business logic
    class User {
      private _name: string;
      private _email: EmailAddress;
      private _roles: Set<Role>;
      private _lastLoginAt: Date | null;
      private _failedLoginAttempts: number;
      private _lockedUntil: Date | null;
      
      constructor(
        readonly id: string,
        name: string,
        email: string,
        roles: Role[] = []
      ) {
        this._name = name;
        this._email = new EmailAddress(email);
        this._roles = new Set(roles);
        this._lastLoginAt = null;
        this._failedLoginAttempts = 0;
        this._lockedUntil = null;
      }
      
      // Getters
      get name(): string { return this._name; }
      get email(): string { return this._email.toString(); }
      get roles(): Role[] { return Array.from(this._roles); }
      get lastLoginAt(): Date | null { return this._lastLoginAt; }
      get isLocked(): boolean { 
        return this._lockedUntil !== null && this._lockedUntil > new Date();
      }
      
      // Business logic methods
      
      addRole(role: Role): void {
        this._roles.add(role);
      }
      
      removeRole(role: Role): void {
        if (this._roles.size === 1) {
          throw new BusinessRuleError('User must have at least one role');
        }
        this._roles.delete(role);
      }
      
      hasRole(role: Role): boolean {
        return this._roles.has(role);
      }
      
      hasPermission(permission: Permission): boolean {
        return this.roles.some(role => role.hasPermission(permission));
      }
      
      recordSuccessfulLogin(): void {
        this._lastLoginAt = new Date();
        this._failedLoginAttempts = 0;
        this._lockedUntil = null;
      }
      
      recordFailedLogin(): void {
        this._failedLoginAttempts++;
        
        if (this._failedLoginAttempts >= 5) {
          // Lock account for increasing duration based on failures
          const lockMinutes = Math.min(Math.pow(2, this._failedLoginAttempts - 5), 60);
          const lockUntil = new Date();
          lockUntil.setMinutes(lockUntil.getMinutes() + lockMinutes);
          this._lockedUntil = lockUntil;
        }
      }
      
      updateEmail(email: string): void {
        // Create new email address will validate format
        this._email = new EmailAddress(email);
      }
      
      updateName(name: string): void {
        if (!name || name.trim().length === 0) {
          throw new ValidationError('Name cannot be empty');
        }
        this._name = name.trim();
      }
    }
    
    // Domain service using the entity
    class AuthenticationService {
      constructor(
        private userRepository: UserRepository,
        private passwordHasher: PasswordHasher,
        private eventBus: EventBus
      ) {}
      
      async authenticate(email: string, password: string): Promise<User> {
        const user = await this.userRepository.findByEmail(email);
        
        if (!user) {
          throw new AuthenticationError('Invalid credentials');
        }
        
        if (user.isLocked) {
          throw new AccountLockedError('Account is locked');
        }
        
        const passwordValid = await this.passwordHasher.verify(
          password,
          user.passwordHash
        );
        
        if (!passwordValid) {
          user.recordFailedLogin();
          await this.userRepository.save(user);
          this.eventBus.publish(new FailedLoginEvent(user.id));
          throw new AuthenticationError('Invalid credentials');
        }
        
        user.recordSuccessfulLogin();
        await this.userRepository.save(user);
        this.eventBus.publish(new SuccessfulLoginEvent(user.id));
        
        return user;
      }
    }
```

### Data Access Patterns

```yaml
pattern:
  name: "Repository Pattern"
  principles: [modularity, tensegrity]
  context: "Data access and persistence"
  application:
    - "Abstract data storage behind repositories"
    - "Define repository interfaces based on domain concepts"
    - "Encapsulate query logic in repositories"
    - "Maintain clear separation from domain logic"
  example: |
    // TypeScript example
    
    // Repository interface
    interface UserRepository {
      findById(id: string): Promise<User | null>;
      findByEmail(email: string): Promise<User | null>;
      findAll(options?: QueryOptions): Promise<User[]>;
      save(user: User): Promise<User>;
      delete(id: string): Promise<boolean>;
    }
    
    // Repository implementation
    class PostgresUserRepository implements UserRepository {
      constructor(
        private readonly db: DatabaseConnection,
        private readonly logger: Logger
      ) {}
      
      async findById(id: string): Promise<User | null> {
        try {
          const query = `
            SELECT u.*, r.id as role_id, r.name as role_name
            FROM users u
            LEFT JOIN user_roles ur ON u.id = ur.user_id
            LEFT JOIN roles r ON ur.role_id = r.id
            WHERE u.id = $1
          `;
          
          const result = await this.db.query(query, [id]);
          
          if (result.length === 0) {
            return null;
          }
          
          return this.mapToUser(result);
        } catch (error) {
          this.logger.error('Failed to find user by ID', error as Error, { id });
          throw new RepositoryError('Database query failed', { cause: error });
        }
      }
      
      async findByEmail(email: string): Promise<User | null> {
        try {
          const query = `
            SELECT u.*, r.id as role_id, r.name as role_name
            FROM users u
            LEFT JOIN user_roles ur ON u.id = ur.user_id
            LEFT JOIN roles r ON ur.role_id = r.id
            WHERE u.email = $1
          `;
          
          const result = await this.db.query(query, [email.toLowerCase()]);
          
          if (result.length === 0) {
            return null;
          }
          
          return this.mapToUser(result);
        } catch (error) {
          this.logger.error('Failed to find user by email', error as Error, { email });
          throw new RepositoryError('Database query failed', { cause: error });
        }
      }
      
      async save(user: User): Promise<User> {
        const trx = await this.db.startTransaction();
        
        try {
          // First, update the user record
          if (await this.exists(user.id)) {
            await trx.query(
              `UPDATE users SET name = $1, email = $2, updated_at = NOW() WHERE id = $3`,
              [user.name, user.email, user.id]
            );
          } else {
            await trx.query(
              `INSERT INTO users (id, name, email, created_at, updated_at) 
               VALUES ($1, $2, $3, NOW(), NOW())`,
              [user.id, user.name, user.email]
            );
          }
          
          // Then, sync roles
          await trx.query(`DELETE FROM user_roles WHERE user_id = $1`, [user.id]);
          
          for (const role of user.roles) {
            await trx.query(
              `INSERT INTO user_roles (user_id, role_id) VALUES ($1, $2)`,
              [user.id, role.id]
            );
          }
          
          await trx.commit();
          return user;
        } catch (error) {
          await trx.rollback();
          this.logger.error('Failed to save user', error as Error, { userId: user.id });
          throw new RepositoryError('Failed to save user', { cause: error });
        }
      }
      
      // Additional repository methods...
      
      private async exists(id: string): Promise<boolean> {
        const result = await this.db.query(
          `SELECT 1 FROM users WHERE id = $1`,
          [id]
        );
        return result.length > 0;
      }
      
      private mapToUser(rows: any[]): User {
        // Group by user and map the roles
        const userData = rows[0];
        const roles = rows
          .filter(row => row.role_id)
          .map(row => new Role(row.role_id, row.role_name));
        
        return new User(
          userData.id,
          userData.name,
          userData.email,
          roles
        );
      }
    }
    
    // Usage in service
    class UserService {
      constructor(private userRepository: UserRepository) {}
      
      async findUserByEmail(email: string): Promise<User | null> {
        return this.userRepository.findByEmail(email);
      }
      
      async updateUser(id: string, data: UserUpdateData): Promise<User> {
        const user = await this.userRepository.findById(id);
        
        if (!user) {
          throw new ResourceNotFoundError('User', id);
        }
        
        if (data.name) {
          user.updateName(data.name);
        }
        
        if (data.email) {
          user.updateEmail(data.email);
        }
        
        return this.userRepository.save(user);
      }
    }
```

### Configuration Management Patterns

```yaml
pattern:
  name: "Hierarchical Configuration"
  principles: [parsimony, adaptivity]
  context: "Managing application configuration"
  application:
    - "Implement layered configuration sources"
    - "Support environment-specific overrides"
    - "Provide sensible defaults"
    - "Validate configuration integrity"
  example: |
    // TypeScript example
    
    // Configuration interface
    interface ConfigProvider {
      get<T>(key: string, defaultValue?: T): T;
      has(key: string): boolean;
      getAll(): Record<string, any>;
    }
    
    // Hierarchical configuration implementation
    class HierarchicalConfig implements ConfigProvider {
      private readonly values: Record<string, any>;
      
      constructor(
        private readonly defaultConfig: Record<string, any>,
        private readonly envConfig: Record<string, any>,
        private readonly overrideConfig: Record<string, any> = {}
      ) {
        // Merge configurations with increasing precedence
        this.values = {
          ...defaultConfig,
          ...envConfig,
          ...overrideConfig
        };
        
        this.validateConfig();
      }
      
      get<T>(key: string, defaultValue?: T): T {
        const parts = key.split('.');
        let current: any = this.values;
        
        for (const part of parts) {
          if (current === undefined || current === null) {
            return defaultValue as T;
          }
          current = current[part];
        }
        
        return (current !== undefined && current !== null) 
          ? current as T 
          : defaultValue as T;
      }
      
      has(key: string): boolean {
        const parts = key.split('.');
        let current: any = this.values;
        
        for (const part of parts) {
          if (current === undefined || current === null) {
            return false;
          }
          current = current[part];
        }
        
        return current !== undefined && current !== null;
      }
      
      getAll(): Record<string, any> {
        return { ...this.values };
      }
      
      private validateConfig(): void {
        // Validate required configuration
        const requiredKeys = [
          'database.host',
          'database.port',
          'database.name',
          'api.port',
          'auth.tokenExpiration'
        ];
        
        const missingKeys = requiredKeys.filter(key => !this.has(key));
        
        if (missingKeys.length > 0) {
          throw new ConfigurationError(
            `Missing required configuration: ${missingKeys.join(', ')}`
          );
        }
        
        // Validate types
        if (typeof this.get('api.port') !== 'number') {
          throw new ConfigurationError(
            'Invalid configuration: api.port must be a number'
          );
        }
        
        if (typeof this.get('database.port') !== 'number') {
          throw new ConfigurationError(
            'Invalid configuration: database.port must be a number'
          );
        }
      }
    }
    
    // Configuration factory
    function createConfig(): ConfigProvider {
      // Default configuration
      const defaults = {
        api: {
          port: 3000,
          cors: {
            enabled: true,
            origins: ['http://localhost:8080']
          }
        },
        database: {
          port: 5432,
          pool: {
            min: 2,
            max: 10
          }
        },
        auth: {
          tokenExpiration: 3600
        },
        logging: {
          level: 'info'
        }
      };
      
      // Environment-specific configuration
      const envConfig = loadEnvConfig();
      
      // Override configuration
      const overrides = process.env.NODE_ENV === 'test'
        ? { database: { name: 'test_db' } }
        : {};
      
      return new HierarchicalConfig(defaults, envConfig, overrides);
    }
    
    // Usage example
    const config = createConfig();
    
    const dbConfig = {
      host: config.get('database.host'),
      port: config.get('database.port'),
      database: config.get('database.name'),
      user: config.get('database.user'),
      password: config.get('database.password'),
      pool: {
        min: config.get('database.pool.min', 2),
        max: config.get('database.pool.max', 10)
      }
    };
    
    const db = createDatabaseConnection(dbConfig);
```

## Context-Specific Patterns

### Application Architecture Patterns

For application-level architecture:

1. **Layered Architecture**:
   - Presentation layer (UI/API)
   - Application layer (use cases)
   - Domain layer (business logic)
   - Infrastructure layer (external systems, persistence)

2. **Clean Architecture**:
   - Core domain with business rules
   - Application services orchestrating use cases
   - Interface adapters translating data
   - Framework and driver integrations

3. **Hexagonal Architecture (Ports and Adapters)**:
   - Core domain logic at center
   - Ports defining interfaces
   - Adapters implementing interfaces
   - Clear distinction between inside and outside

### API Architecture Patterns

For API design:

1. **RESTful Resource Modeling**:
   - Resource-oriented design
   - Standard HTTP methods
   - Consistent URL structure
   - Hypermedia links

2. **GraphQL Schema Design**:
   - Type-based schema definition
   - Query and mutation separation
   - Field-level resolution
   - Explicit relationships

3. **API Gateway Pattern**:
   - Centralized entry point
   - Request routing
   - Composition of multiple services
   - Cross-cutting concerns (auth, logging)

### Data Architecture Patterns

For data management:

1. **Event Sourcing**:
   - Events as primary record
   - Derived state projections
   - Complete history preservation
   - Temporal queries

2. **CQRS (Command Query Responsibility Segregation)**:
   - Separate read and write models
   - Specialized data structures
   - Optimized query performance
   - Command validation

3. **Data Mapper**:
   - Separation of domain and persistence
   - Bidirectional mapping
   - Identity map pattern
   - Unit of work pattern

## Meta-Systemic Validation

### Modularity Validation

Verify that:
- Components have clear, explicit boundaries
- External APIs are well-defined
- Internal implementation details are hidden
- Testing can be performed in isolation

### Tensegrity Validation

Verify that:
- Components have balanced dependencies
- Bidirectional relationships are explicit
- Responsibility distribution is appropriate
- Interfaces are resilient to change

### Parsimony Validation

Verify that:
- Common patterns are extracted and reused
- Domain concepts have canonical definitions
- Similar functionality is consolidated
- Duplication is minimized

### Coherence Validation

Verify that:
- Similar problems use similar solutions
- Architectural patterns are consistently applied
- Naming conventions are consistent
- Error handling follows a consistent approach

### Clarity Validation

Verify that:
- Interfaces are clearly documented
- Complex logic includes explanatory comments
- Design decisions include rationale
- Examples demonstrate usage patterns

### Adaptivity Validation

Verify that:
- Architecture can evolve with changing requirements
- Different contexts can be accommodated
- Extensibility is built into key interfaces
- Core patterns can be adapted while preserving intent

## Balancing Architecture Patterns with System Context

### Early Exploration Context

- Focus on flexible, adaptable patterns
- Prefer lightweight, simple architectures
- Defer complex architectural decisions
- Maintain core boundaries for later expansion

### Active Development Context

- Implement clear architectural patterns
- Establish consistent component structure
- Define explicit interfaces
- Balance flexibility with standardization

### Maintenance Context

- Strengthen existing architectural patterns
- Improve documentation and examples
- Refactor toward better principle adherence
- Enhance testability and maintainability

### Legacy Context

- Document existing architecture
- Implement incremental improvements
- Maintain compatibility with existing patterns
- Prioritize backward compatibility

<important>
Architecture patterns create the foundation for system integrity. Apply these patterns with appropriate context sensitivity to create maintainable, adaptable systems that embody meta-systemic principles. Remember that architecture should enhance development, not constrain it unnecessarily.
</important>