---
description: USE WHEN implementing testing activities: Apply meta-systemic principles to test design, organization, and execution across all testing levels from unit to system testing.
globs: 
alwaysApply: false
---
---
description: "Testing patterns for applying meta-systemic principles across all testing activities"
globs: "**/*.test.js,**/*.test.ts,**/*.spec.js,**/*.spec.ts,**/tests/**/*.js,**/tests/**/*.ts,**/tests/**/*.py,**/tests/**/*.go,**/tests/**/*.java,**/tests/**/*.rb,**/*.feature"
priority: 2
alwaysApply: false
type: "Agent-Requested"
---

# Testing Patterns

<critical>
Apply these testing patterns when designing, implementing, and executing tests to ensure comprehensive validation while embodying meta-systemic principles across all system contexts.
</critical>

## Pattern Application Process

When working with tests, follow this process:

1. **IDENTIFY** the testing scope and context
2. **SELECT** the appropriate testing patterns
3. **APPLY** the patterns consistently across test suites
4. **VALIDATE** that tests effectively verify system behavior while maintaining principle integrity

## Core Testing Patterns

### Test Organization Pattern

```yaml
pattern:
  name: "Hierarchical Test Organization"
  principles: [modularity, coherence]
  context: "All testing types"
  application:
    - "Organize tests to mirror system component structure"
    - "Group tests by functionality and test level"
    - "Maintain consistent naming conventions"
    - "Create clear test boundaries with appropriate granularity"
  example: |
    // Project structure
    /src
      /components
        /auth
          auth-service.ts
          token-service.ts
        /users
          user-service.ts
          user-repository.ts
    
    // Mirrored test structure
    /tests
      /unit
        /components
          /auth
            auth-service.test.ts
            token-service.test.ts
          /users
            user-service.test.ts
            user-repository.test.ts
      /integration
        /auth
          authentication-flow.test.ts
        /users
          user-management.test.ts
      /e2e
        user-journey.test.ts
```

### Test Case Design Pattern

```yaml
pattern:
  name: "Comprehensive Test Case Design"
  principles: [clarity, coherence]
  context: "All testing types"
  application:
    - "Define clear test descriptions that explain intent"
    - "Structure tests with arrange-act-assert pattern"
    - "Cover happy path, edge cases, and error scenarios"
    - "Document test rationale for complex scenarios"
  example: |
    /**
     * User authentication tests
     */
    describe('UserAuthService', () => {
      // Happy path scenario
      it('should successfully authenticate with valid credentials', async () => {
        // Arrange
        const validCredentials = {
          username: 'testuser',
          password: 'correct-password'
        };
        const userService = new UserAuthService(mockUserRepository, mockTokenService);
        
        // Act
        const result = await userService.authenticate(validCredentials);
        
        // Assert
        expect(result.success).toBe(true);
        expect(result.token).toBeDefined();
        expect(result.user.username).toBe(validCredentials.username);
      });
      
      // Error scenario
      it('should reject authentication with invalid password', async () => {
        // Arrange
        const invalidCredentials = {
          username: 'testuser',
          password: 'wrong-password'
        };
        const userService = new UserAuthService(mockUserRepository, mockTokenService);
        
        // Act
        const result = await userService.authenticate(invalidCredentials);
        
        // Assert
        expect(result.success).toBe(false);
        expect(result.token).toBeUndefined();
        expect(result.error).toBe('Invalid credentials');
      });
      
      // Edge case
      it('should handle special characters in username correctly', async () => {
        // Arrange
        const specialUsername = {
          username: 'test@user+special',
          password: 'correct-password'
        };
        const userService = new UserAuthService(mockUserRepository, mockTokenService);
        
        // Act
        const result = await userService.authenticate(specialUsername);
        
        // Assert
        expect(result.success).toBe(true);
        expect(result.user.username).toBe(specialUsername.username);
      });
    });
```

### Test Independence Pattern

```yaml
pattern:
  name: "Isolated and Independent Tests"
  principles: [modularity, tensegrity]
  context: "All testing types"
  application:
    - "Design tests to be independent and self-contained"
    - "Properly set up and tear down test environments"
    - "Avoid dependencies between test cases"
    - "Prevent side effects that could affect other tests"
  example: |
    /**
     * Example of test independence with proper setup and teardown
     */
    describe('UserRepository', () => {
      // Setup before each test
      beforeEach(async () => {
        // Create a fresh database connection for each test
        testDb = await createTestDatabase();
        
        // Initialize with known test data
        await testDb.query(
          'INSERT INTO users (id, username, email) VALUES ($1, $2, $3)',
          ['test-id', 'testuser', 'test@example.com']
        );
        
        // Create repository with test database
        userRepository = new UserRepository(testDb);
      });
      
      // Cleanup after each test
      afterEach(async () => {
        // Clean up any data created during the test
        await testDb.query('DELETE FROM users');
        
        // Close the database connection
        await testDb.close();
      });
      
      it('should find user by id', async () => {
        const user = await userRepository.findById('test-id');
        expect(user).not.toBeNull();
        expect(user.username).toBe('testuser');
      });
      
      it('should create new user', async () => {
        const newUser = {
          id: 'new-id',
          username: 'newuser',
          email: 'new@example.com'
        };
        
        await userRepository.save(newUser);
        
        const saved = await userRepository.findById('new-id');
        expect(saved).not.toBeNull();
        expect(saved.username).toBe('newuser');
      });
    });
```

### Test Data Management Pattern

```yaml
pattern:
  name: "Structured Test Data Management"
  principles: [parsimony, coherence]
  context: "All testing types"
  application:
    - "Create reusable test data factories"
    - "Separate test data from test logic"
    - "Use consistent data patterns across tests"
    - "Generate appropriate test data for different scenarios"
  example: |
    /**
     * Test data factory for creating consistent test objects
     */
    class UserTestFactory {
      // Create a default valid user
      static createValidUser(override = {}) {
        return {
          id: 'test-id-123',
          username: 'testuser',
          email: 'test@example.com',
          created: new Date('2023-01-01'),
          roles: ['user'],
          active: true,
          ...override
        };
      }
      
      // Create an invalid user with specific validation issues
      static createInvalidUser(validationErrors = {}) {
        const user = this.createValidUser();
        
        // Apply specific validation errors
        Object.keys(validationErrors).forEach(key => {
          user[key] = validationErrors[key];
        });
        
        return user;
      }
      
      // Create a collection of test users
      static createUsers(count, template = {}) {
        return Array.from({ length: count }, (_, index) => 
          this.createValidUser({
            id: `test-id-${index}`,
            username: `testuser${index}`,
            email: `test${index}@example.com`,
            ...template
          })
        );
      }
    }
    
    // Usage in tests
    describe('UserService', () => {
      it('should filter active users', () => {
        // Create test data
        const users = [
          UserTestFactory.createValidUser({ active: true }),
          UserTestFactory.createValidUser({ active: false }),
          UserTestFactory.createValidUser({ active: true })
        ];
        
        const userService = new UserService();
        
        // Act
        const activeUsers = userService.filterActiveUsers(users);
        
        // Assert
        expect(activeUsers.length).toBe(2);
        expect(activeUsers.every(user => user.active)).toBe(true);
      });
    });
```

### Test Mocking Pattern

```yaml
pattern:
  name: "Controlled Dependency Mocking"
  principles: [modularity, tensegrity]
  context: "Unit and integration testing"
  application:
    - "Mock external dependencies for controlled testing"
    - "Define clear mock interfaces that match real components"
    - "Create reusable mock factories with consistent behavior"
    - "Balance between realistic and simplified mock behavior"
  example: |
    /**
     * Mock factory for creating consistent dependency mocks
     */
    class AuthServiceMock {
      // Factory method to create a mock with customizable behavior
      static create(options = {}) {
        // Default behaviors
        const defaults = {
          authenticate: jest.fn().mockResolvedValue({ success: true, token: 'mock-token' }),
          verifyToken: jest.fn().mockResolvedValue({ valid: true, userId: 'mock-user-id' }),
          generateToken: jest.fn().mockResolvedValue('mock-new-token'),
          shouldAuthenticationFail: false,
          shouldVerificationFail: false
        };
        
        // Apply options
        const config = { ...defaults, ...options };
        
        // Create mock instance
        const mock = {
          authenticate: jest.fn(async (credentials) => {
            if (config.shouldAuthenticationFail) {
              return { success: false, error: 'Authentication failed' };
            }
            return config.authenticate(credentials);
          }),
          
          verifyToken: jest.fn(async (token) => {
            if (config.shouldVerificationFail) {
              return { valid: false, error: 'Invalid token' };
            }
            return config.verifyToken(token);
          }),
          
          generateToken: config.generateToken,
          
          // Helper to simulate failure
          simulateAuthFailure() {
            config.shouldAuthenticationFail = true;
            return this;
          },
          
          simulateVerificationFailure() {
            config.shouldVerificationFail = true;
            return this;
          }
        };
        
        return mock;
      }
    }
    
    // Usage in tests
    describe('UserController', () => {
      it('should return user data when authentication succeeds', async () => {
        // Create mock with specific behavior
        const authServiceMock = AuthServiceMock.create({
          authenticate: jest.fn().mockResolvedValue({
            success: true,
            token: 'specific-token',
            user: { id: 'user-123', name: 'Test User' }
          })
        });
        
        const userController = new UserController(authServiceMock);
        
        // Act
        const response = await userController.login({
          username: 'testuser',
          password: 'password'
        });
        
        // Assert
        expect(response.status).toBe(200);
        expect(response.body.token).toBe('specific-token');
        expect(response.body.user.name).toBe('Test User');
      });
      
      it('should return error when authentication fails', async () => {
        // Use the helper to simulate failure
        const authServiceMock = AuthServiceMock.create().simulateAuthFailure();
        
        const userController = new UserController(authServiceMock);
        
        // Act
        const response = await userController.login({
          username: 'testuser',
          password: 'wrong-password'
        });
        
        // Assert
        expect(response.status).toBe(401);
        expect(response.body.error).toBeDefined();
      });
    });
```

### Test Validation Pattern

```yaml
pattern:
  name: "Comprehensive Assertion Strategy"
  principles: [clarity, coherence]
  context: "All testing types"
  application:
    - "Use explicit and specific assertions"
    - "Validate all relevant aspects of system behavior"
    - "Include positive and negative assertions"
    - "Use consistent assertion patterns"
  example: |
    /**
     * Comprehensive assertion example
     */
    describe('Order Processing', () => {
      it('should process valid order correctly', async () => {
        // Arrange
        const order = OrderTestFactory.createValidOrder();
        const orderProcessor = new OrderProcessor(mockInventory, mockPayment);
        
        // Act
        const result = await orderProcessor.process(order);
        
        // Assert - Multiple aspects validated
        
        // 1. Check operation success
        expect(result.success).toBe(true);
        
        // 2. Validate generated order ID
        expect(result.orderId).toMatch(/ORD-[0-9A-F]{8}/);
        
        // 3. Verify order status
        expect(result.status).toBe('processed');
        
        // 4. Check inventory interaction
        expect(mockInventory.reserveItems).toHaveBeenCalledWith(
          order.items.map(item => item.productId),
          order.items.map(item => item.quantity)
        );
        
        // 5. Verify payment processing
        expect(mockPayment.processPayment).toHaveBeenCalledWith(
          result.orderId,
          order.totalAmount,
          order.paymentDetails
        );
        
        // 6. Check generated timestamps
        expect(result.processedAt instanceof Date).toBe(true);
        expect(result.processedAt.getTime()).toBeLessThanOrEqual(Date.now());
        
        // 7. Validate idempotency
        expect(result.idempotencyKey).toBe(order.idempotencyKey);
      });
    });
```

### Test Automation Pattern

```yaml
pattern:
  name: "Reliable Test Automation"
  principles: [adaptivity, tensegrity]
  context: "All automated testing"
  application:
    - "Design tests to be reliable and deterministic"
    - "Handle asynchronous operations properly"
    - "Create appropriate retry and timeout strategies"
    - "Implement proper error handling and logging"
  example: |
    /**
     * Reliable async testing with proper error handling
     */
    describe('AsyncDataService', () => {
      // Helper for reliable async testing
      const waitForCondition = async (condition, timeout = 5000, interval = 100) => {
        const startTime = Date.now();
        
        while (Date.now() - startTime < timeout) {
          if (await condition()) {
            return true;
          }
          await new Promise(resolve => setTimeout(resolve, interval));
        }
        
        throw new Error(`Condition not met within ${timeout}ms timeout`);
      };
      
      it('should eventually process all queue items', async () => {
        // Arrange
        const queueItems = [
          { id: 'item1', data: 'test1' },
          { id: 'item2', data: 'test2' },
          { id: 'item3', data: 'test3' }
        ];
        
        const processor = new AsyncDataProcessor();
        const processedItems = [];
        
        processor.on('itemProcessed', item => {
          processedItems.push(item);
        });
        
        // Act
        processor.addItems(queueItems);
        processor.startProcessing();
        
        // Assert with reliable waiting
        try {
          await waitForCondition(
            () => processedItems.length === queueItems.length,
            10000 // Reasonable timeout
          );
          
          // Verify all items were processed
          expect(processedItems.length).toBe(queueItems.length);
          expect(processedItems.map(item => item.id).sort())
            .toEqual(queueItems.map(item => item.id).sort());
            
        } catch (error) {
          // Provide helpful debug information
          console.error('Test failed with state:', {
            processedItems,
            processorState: processor.getState(),
            error: error.message
          });
          throw error;
        } finally {
          // Ensure cleanup happens even on failure
          processor.stopProcessing();
        }
      });
    });
```

## Test Types and Specific Patterns

### Unit Testing Patterns

When implementing unit tests:

```yaml
unit_testing:
  purpose: "Verify individual components in isolation"
  focus:
    - "Component behavior with controlled dependencies"
    - "Complete code path coverage"
    - "Edge case handling"
    - "Error paths and exception handling"
  specific_patterns:
    - name: "Component Isolation"
      example: |
        /**
         * Unit test demonstrating proper component isolation
         */
        describe('UserValidator', () => {
          // Creating dependencies with controlled behavior
          let emailValidator;
          let passwordValidator;
          let userValidator;
          
          beforeEach(() => {
            // Mock dependencies with specific behavior
            emailValidator = {
              validate: jest.fn(email => {
                return email.includes('@') && email.includes('.');
              })
            };
            
            passwordValidator = {
              validate: jest.fn(password => {
                return password.length >= 8;
              }),
              getStrength: jest.fn(password => {
                return password.length >= 12 ? 'strong' : 'weak';
              })
            };
            
            // System under test with injected dependencies
            userValidator = new UserValidator(emailValidator, passwordValidator);
          });
          
          it('should validate a user with valid email and password', () => {
            // Arrange
            const user = {
              name: 'Test User',
              email: 'test@example.com',
              password: 'securePassword123'
            };
            
            // Act
            const result = userValidator.validate(user);
            
            // Assert
            expect(result.valid).toBe(true);
            expect(emailValidator.validate).toHaveBeenCalledWith('test@example.com');
            expect(passwordValidator.validate).toHaveBeenCalledWith('securePassword123');
          });
          
          it('should reject a user with invalid email', () => {
            // Arrange
            const user = {
              name: 'Test User',
              email: 'invalid-email',
              password: 'securePassword123'
            };
            
            // Act
            const result = userValidator.validate(user);
            
            // Assert
            expect(result.valid).toBe(false);
            expect(result.errors.email).toBeDefined();
            expect(emailValidator.validate).toHaveBeenCalledWith('invalid-email');
          });
          
          it('should provide password strength assessment', () => {
            // Arrange
            const user = {
              name: 'Test User',
              email: 'test@example.com',
              password: 'short'
            };
            
            // Act
            const result = userValidator.validate(user);
            
            // Assert
            expect(result.valid).toBe(false);
            expect(result.passwordStrength).toBe('weak');
            expect(passwordValidator.getStrength).toHaveBeenCalledWith('short');
          });
        });
```

### Integration Testing Patterns

When implementing integration tests:

```yaml
integration_testing:
  purpose: "Verify interactions between components"
  focus:
    - "Component integration with real or realistic dependencies"
    - "Cross-component workflows"
    - "Data flow between components"
    - "Integration contract compliance"
  specific_patterns:
    - name: "Boundary Integration"
      example: |
        /**
         * Integration test focusing on component boundaries
         */
        describe('Authentication Flow', () => {
          // Use actual implementations for primary components
          let userRepository;
          let authService;
          let tokenService;
          
          beforeEach(async () => {
            // Set up test database
            const testDb = await createTestDatabase();
            
            // Seed database with test data
            await seedTestUsers(testDb);
            
            // Create actual components with some controlled dependencies
            userRepository = new UserRepository(testDb);
            tokenService = new TokenService(
              config,
              mockTimeProvider // Control time-based behaviors
            );
            
            // System under test with real dependencies
            authService = new AuthService(userRepository, tokenService);
          });
          
          afterEach(async () => {
            await cleanupTestDatabase();
          });
          
          it('should authenticate user and generate valid token', async () => {
            // Arrange
            const credentials = {
              username: 'testuser',
              password: 'correct-password'
            };
            
            // Act: Test the complete authentication flow
            const authResult = await authService.authenticate(credentials);
            
            // Assert: Verify complete flow results
            expect(authResult.success).toBe(true);
            expect(authResult.token).toBeDefined();
            
            // Verify token validity using the real token service
            const verificationResult = await tokenService.verifyToken(authResult.token);
            expect(verificationResult.valid).toBe(true);
            expect(verificationResult.userId).toBeDefined();
            
            // Verify user data was accessed correctly
            const user = await userRepository.findById(verificationResult.userId);
            expect(user).not.toBeNull();
            expect(user.username).toBe(credentials.username);
          });
          
          it('should update last login timestamp on successful authentication', async () => {
            // Arrange
            const credentials = {
              username: 'testuser',
              password: 'correct-password'
            };
            const beforeAuth = new Date();
            
            // Act
            await authService.authenticate(credentials);
            
            // Assert: Verify the side effect of updating login timestamp
            const user = await userRepository.findByUsername(credentials.username);
            expect(user.lastLoginAt).toBeInstanceOf(Date);
            expect(user.lastLoginAt.getTime()).toBeGreaterThanOrEqual(beforeAuth.getTime());
          });
        });
```

### System Testing Patterns

When implementing system tests:

```yaml
system_testing:
  purpose: "Verify complete system behavior"
  focus:
    - "End-to-end workflows"
    - "System-level behavior"
    - "Performance characteristics"
    - "Cross-functional requirements"
  specific_patterns:
    - name: "End-to-End Workflow"
      example: |
        /**
         * System test verifying complete application workflows
         */
        describe('Order Management Workflow', () => {
          // Setup complete system with minimal mocking
          let app;
          let testUser;
          let testProduct;
          
          beforeAll(async () => {
            // Start application with test configuration
            app = await startApplication({
              config: testConfig,
              database: testDatabase,
              // Mock external payment gateway only
              paymentGateway: mockPaymentGateway
            });
            
            // Create test data in system
            testUser = await createTestUser(app);
            testProduct = await createTestProduct(app);
          });
          
          afterAll(async () => {
            await cleanupTestData(app);
            await stopApplication(app);
          });
          
          it('should complete the order process from cart to fulfillment', async () => {
            // 1. Add product to cart
            const cartResponse = await app.api.request({
              method: 'POST',
              url: '/api/cart/items',
              headers: { Authorization: `Bearer ${testUser.token}` },
              data: {
                productId: testProduct.id,
                quantity: 2
              }
            });
            
            expect(cartResponse.status).toBe(200);
            const cartId = cartResponse.data.cartId;
            
            // 2. Proceed to checkout
            const checkoutResponse = await app.api.request({
              method: 'POST',
              url: '/api/checkout',
              headers: { Authorization: `Bearer ${testUser.token}` },
              data: {
                cartId,
                shippingAddress: testUser.address,
                paymentDetails: {
                  method: 'credit_card',
                  cardToken: 'test-card-token'
                }
              }
            });
            
            expect(checkoutResponse.status).toBe(200);
            const orderId = checkoutResponse.data.orderId;
            
            // 3. Verify order was created properly
            const orderResponse = await app.api.request({
              method: 'GET',
              url: `/api/orders/${orderId}`,
              headers: { Authorization: `Bearer ${testUser.token}` }
            });
            
            expect(orderResponse.status).toBe(200);
            expect(orderResponse.data.status).toBe('pending_payment');
            expect(orderResponse.data.items).toHaveLength(1);
            expect(orderResponse.data.items[0].productId).toBe(testProduct.id);
            
            // 4. Simulate payment completion (normally triggered by webhook)
            await app.services.paymentWebhookHandler.handlePaymentSuccess({
              orderId,
              transactionId: 'test-transaction-123',
              amount: orderResponse.data.totalAmount
            });
            
            // 5. Verify order status updated after payment
            const paidOrderResponse = await app.api.request({
              method: 'GET',
              url: `/api/orders/${orderId}`,
              headers: { Authorization: `Bearer ${testUser.token}` }
            });
            
            expect(paidOrderResponse.status).toBe(200);
            expect(paidOrderResponse.data.status).toBe('paid');
            
            // 6. Verify inventory was updated
            const inventoryResponse = await app.api.request({
              method: 'GET',
              url: `/api/products/${testProduct.id}`,
              headers: { Authorization: `Bearer ${testUser.token}` }
            });
            
            expect(inventoryResponse.status).toBe(200);
            expect(inventoryResponse.data.stockLevel).toBe(testProduct.initialStock - 2);
          });
        });
```

### Acceptance Testing Patterns

When implementing acceptance tests:

```yaml
acceptance_testing:
  purpose: "Verify system meets business requirements"
  focus:
    - "Business requirements verification"
    - "User acceptance criteria"
    - "Business process validation"
    - "User experience verification"
  specific_patterns:
    - name: "Behavior-Driven Testing"
      example: |
        /**
         * BDD-style acceptance test
         */
        // user-registration.feature
        Feature: User Registration
          As a new user
          I want to create an account
          So that I can access personalized features
          
          Scenario: Successful registration with valid information
            Given I am on the registration page
            When I enter "newuser@example.com" in the email field
            And I enter "John Doe" in the name field
            And I enter "SecurePassword123" in the password field
            And I enter "SecurePassword123" in the confirm password field
            And I click the "Register" button
            Then I should see a confirmation message
            And I should receive a welcome email at "newuser@example.com"
            And I should be able to log in with "newuser@example.com" and "SecurePassword123"
          
          Scenario: Registration fails with existing email
            Given I am on the registration page
            And a user exists with email "existing@example.com"
            When I enter "existing@example.com" in the email field
            And I enter "John Doe" in the name field
            And I enter "SecurePassword123" in the password field
            And I enter "SecurePassword123" in the confirm password field
            And I click the "Register" button
            Then I should see an error message "Email already in use"
            And I should remain on the registration page
        
        // Step definitions
        const { Given, When, Then } = require('@cucumber/cucumber');
        
        Given('I am on the registration page', async function() {
          await this.browser.navigate('/register');
          const pageTitle = await this.browser.getTitle();
          assert.include(pageTitle, 'Register');
        });
        
        Given('a user exists with email {string}', async function(email) {
          await this.database.createUser({
            email,
            name: 'Existing User',
            passwordHash: await this.hashPassword('ExistingPassword123')
          });
        });
        
        When('I enter {string} in the {word} field', async function(value, fieldName) {
          const fieldMap = {
            email: '#email',
            name: '#fullName',
            password: '#password',
            'confirm': '#confirmPassword'
          };
          
          await this.browser.type(fieldMap[fieldName], value);
        });
        
        When('I click the {string} button', async function(buttonText) {
          await this.browser.clickButton(buttonText);
        });
        
        Then('I should see a confirmation message', async function() {
          const confirmationElement = await this.browser.findElement('.confirmation-message');
          const message = await confirmationElement.getText();
          assert.include(message, 'Registration successful');
        });
        
        Then('I should receive a welcome email at {string}', async function(email) {
          // Check the test email service for received emails
          const emails = await this.emailService.getEmailsSentTo(email);
          assert.isAtLeast(emails.length, 1);
          
          const welcomeEmail = emails.find(email => 
            email.subject.includes('Welcome')
          );
          
          assert.exists(welcomeEmail);
        });
        
        Then('I should be able to log in with {string} and {string}', async function(email, password) {
          await this.browser.navigate('/login');
          await this.browser.type('#email', email);
          await this.browser.type('#password', password);
          await this.browser.clickButton('Login');
          
          // Verify successful login
          const dashboardElement = await this.browser.waitForElement('#dashboard');
          assert.exists(dashboardElement);
        });
        
        Then('I should see an error message {string}', async function(errorMessage) {
          const errorElement = await this.browser.findElement('.error-message');
          const message = await errorElement.getText();
          assert.include(message, errorMessage);
        });
        
        Then('I should remain on the registration page', async function() {
          const currentUrl = await this.browser.getCurrentUrl();
          assert.include(currentUrl, '/register');
        });
```

### Performance Testing Patterns

When implementing performance tests:

```yaml
performance_testing:
  purpose: "Verify system performance characteristics"
  focus:
    - "Response time and latency"
    - "Throughput and capacity"
    - "Resource utilization"
    - "Scalability and elasticity"
  specific_patterns:
    - name: "Baseline Performance Verification"
      example: |
        /**
         * Performance test with baselines and thresholds
         */
        describe('Search API Performance', () => {
          // Performance testing configuration
          const performanceConfig = {
            baselines: {
              p50Latency: 120, // ms
              p95Latency: 250, // ms
              throughput: 100, // requests per second
            },
            thresholds: {
              maxP50Latency: 150, // ms
              maxP95Latency: 300, // ms
              minThroughput: 80, // requests per second
              maxErrorRate: 0.01, // 1%
              maxCpuUtilization: 0.7, // 70%
              maxMemoryUtilization: 0.8, // 80%
            },
            testParams: {
              duration: 60, // seconds
              rampUp: 15, // seconds
              concurrentUsers: 50,
              requestsPerUser: 10,
            }
          };
          
          // Load test driver
          let loadTest;
          let metrics;
          
          beforeAll(async () => {
            // Set up test environment
            await setupTestEnvironment();
            
            // Initialize load test driver
            loadTest = new LoadTestDriver({
              target: 'https://test-api.example.com/api/search',
              params: performanceConfig.testParams,
            });
            
            // Run the load test
            metrics = await loadTest.run();
          });
          
          afterAll(async () => {
            await cleanupTestEnvironment();
          });
          
          it('should meet latency requirements', () => {
            // Assert on P50 latency
            expect(metrics.latency.p50).toBeLessThanOrEqual(
              performanceConfig.thresholds.maxP50Latency
            );
            
            // Assert on P95 latency
            expect(metrics.latency.p95).toBeLessThanOrEqual(
              performanceConfig.thresholds.maxP95Latency
            );
            
            // Log detailed metrics for analysis
            console.info('Latency Metrics:', {
              min: metrics.latency.min,
              max: metrics.latency.max,
              mean: metrics.latency.mean,
              p50: metrics.latency.p50,
              p90: metrics.latency.p90,
              p95: metrics.latency.p95,
              p99: metrics.latency.p99,
            });
          });
          
          it('should meet throughput requirements', () => {
            expect(metrics.throughput.average).toBeGreaterThanOrEqual(
              performanceConfig.thresholds.minThroughput
            );
            
            console.info('Throughput Metrics:', {
              average: metrics.throughput.average,
              peak: metrics.throughput.peak,
              bySecond: metrics.throughput.bySecond, // Time series data
            });
          });
          
          it('should maintain acceptable error rate', () => {
            expect(metrics.errorRate).toBeLessThanOrEqual(
              performanceConfig.thresholds.maxErrorRate
            );
            
            console.info('Error Metrics:', {
              rate: metrics.errorRate,
              byType: metrics.errors.byType,
            });
          });
          
          it('should maintain acceptable resource utilization', () => {
            expect(metrics.resources.cpu.max).toBeLessThanOrEqual(
              performanceConfig.thresholds.maxCpuUtilization
            );
            
            expect(metrics.resources.memory.max).toBeLessThanOrEqual(
              performanceConfig.thresholds.maxMemoryUtilization
            );
            
            console.info('Resource Utilization Metrics:', {
              cpu: metrics.resources.cpu,
              memory: metrics.resources.memory,
              io: metrics.resources.io,
              network: metrics.resources.network,
            });
          });
        });
```

### Security Testing Patterns

When implementing security tests:

```yaml
security_testing:
  purpose: "Verify system security controls"
  focus:
    - "Authentication and authorization"
    - "Data protection and privacy"
    - "Input validation and sanitization"
    - "Security configurations"
  specific_patterns:
    - name: "Authentication Testing"
      example: |
        /**
         * Security tests for authentication mechanisms
         */
        describe('Authentication Security', () => {
          // Security testing configuration
          const securityConfig = {
            endpoints: {
              login: '/api/auth/login',
              resetPassword: '/api/auth/reset-password',
              changeEmail: '/api/auth/change-email',
            },
            users: {
              admin: { username: 'admin', password: 'correct-password' },
              regular: { username: 'user', password: 'correct-password' },
            }
          };
          
          describe('Authentication Mechanisms', () => {
            it('should reject invalid credentials', async () => {
              const response = await request(app)
                .post(securityConfig.endpoints.login)
                .send({
                  username: securityConfig.users.admin.username,
                  password: 'wrong-password'
                });
              
              expect(response.status).toBe(401);
              expect(response.body.token).toBeUndefined();
            });
            
            it('should implement account lockout after multiple failures', async () => {
              // Attempt login with wrong password multiple times
              for (let i = 0; i < 5; i++) {
                await request(app)
                  .post(securityConfig.endpoints.login)
                  .send({
                    username: securityConfig.users.regular.username,
                    password: 'wrong-password'
                  });
              }
              
              // Now try with correct password, should still be locked
              const response = await request(app)
                .post(securityConfig.endpoints.login)
                .send({
                  username: securityConfig.users.regular.username,
                  password: securityConfig.users.regular.password
                });
              
              expect(response.status).toBe(403);
              expect(response.body.error).toContain('locked');
            });
            
            it('should use secure password reset tokens', async () => {
              // Request password reset
              const resetResponse = await request(app)
                .post(`${securityConfig.endpoints.resetPassword}/request`)
                .send({
                  email: 'user@example.com'
                });
              
              expect(resetResponse.status).toBe(200);
              
              // Get token from test email service
              const emails = await testEmailService.getEmailsSentTo('user@example.com');
              const resetEmail = emails.find(email => 
                email.subject.includes('Reset')
              );
              
              // Extract token using regex
              const tokenMatch = resetEmail.body.match(/token=([a-zA-Z0-9_-]+)/);
              const token = tokenMatch ? tokenMatch[1] : null;
              
              expect(token).not.toBeNull();
              
              // Verify token format and length (should be secure)
              expect(token.length).toBeGreaterThanOrEqual(32);
              
              // Verify token can only be used once
              const firstUse = await request(app)
                .post(`${securityConfig.endpoints.resetPassword}/confirm`)
                .send({
                  token,
                  newPassword: 'NewSecurePassword123'
                });
              
              expect(firstUse.status).toBe(200);
              
              const secondUse = await request(app)
                .post(`${securityConfig.endpoints.resetPassword}/confirm`)
                .send({
                  token,
                  newPassword: 'AnotherPassword456'
                });
              
              expect(secondUse.status).toBe(400); // Token already used
            });
          });
          
          describe('Authorization Controls', () => {
            let adminToken;
            let userToken;
            
            beforeEach(async () => {
              // Get auth tokens
              const adminAuth = await request(app)
                .post(securityConfig.endpoints.login)
                .send(securityConfig.users.admin);
              
              const userAuth = await request(app)
                .post(securityConfig.endpoints.login)
                .send(securityConfig.users.regular);
                
              adminToken = adminAuth.body.token;
              userToken = userAuth.body.token;
            });
            
            it('should enforce permission checks for admin actions', async () => {
              // Admin can access admin endpoint
              const adminResponse = await request(app)
                .get('/api/admin/users')
                .set('Authorization', `Bearer ${adminToken}`);
              
              expect(adminResponse.status).toBe(200);
              
              // Regular user cannot access admin endpoint
              const userResponse = await request(app)
                .get('/api/admin/users')
                .set('Authorization', `Bearer ${userToken}`);
              
              expect(userResponse.status).toBe(403);
            });
            
            it('should implement proper permission checks for resource access', async () => {
              // Setup test resources
              const userResource = await createTestResource(securityConfig.users.regular.username);
              
              // User can access own resource
              const ownResourceResponse = await request(app)
                .get(`/api/resources/${userResource.id}`)
                .set('Authorization', `Bearer ${userToken}`);
              
              expect(ownResourceResponse.status).toBe(200);
              
              // User cannot access another user's resource
              const otherResource = await createTestResource('otheruser');
              
              const otherResourceResponse = await request(app)
                .get(`/api/resources/${otherResource.id}`)
                .set('Authorization', `Bearer ${userToken}`);
              
              expect(otherResourceResponse.status).toBe(403);
              
              // Admin can access any resource
              const adminAccessResponse = await request(app)
                .get(`/api/resources/${userResource.id}`)
                .set('Authorization', `Bearer ${adminToken}`);
              
              expect(adminAccessResponse.status).toBe(200);
            });
          });
        });
```

## Meta-Systemic Principle Application

### Parsimony in Testing
- Create reusable test utilities and fixtures
- Define test data factories for consistent test objects
- Implement common assertion helpers
- Maintain single source of truth for test configuration

Example:
```javascript
// INSTEAD OF duplicating test data setup:
describe('UserService', () => {
  it('test one', () => {
    const user = { id: '123', name: 'Test User', email: 'test@example.com', active: true };
    // Test implementation
  });
  
  it('test two', () => {
    const user = { id: '123', name: 'Test User', email: 'test@example.com', active: false };
    // Test implementation
  });
});

// DO THIS - use test factories:
// In test-factories.js
export const createTestUser = (overrides = {}) => ({
  id: '123',
  name: 'Test User',
  email: 'test@example.com',
  active: true,
  ...overrides
});

// In tests
import { createTestUser } from './test-factories';

describe('UserService', () => {
  it('test one', () => {
    const user = createTestUser();
    // Test implementation
  });
  
  it('test two', () => {
    const user = createTestUser({ active: false });
    // Test implementation
  });
});
```

### Tensegrity in Testing
- Design tests that support each other through shared utilities
- Create balanced test infrastructure across test types
- Implement appropriate test hooks for setup and teardown
- Establish test reliability through mutual support

Example:
```javascript
// Balanced test infrastructure with mutual support
const setupTestDatabase = async () => {
  // Implementation
};

const seedTestData = async (db) => {
  // Implementation
};

const cleanupTestDatabase = async (db) => {
  // Implementation
};

// Unit tests provide base verification
describe('UserRepository', () => {
  let db;
  
  beforeEach(async () => {
    db = await setupTestDatabase();
    await seedTestData(db);
  });
  
  afterEach(async () => {
    await cleanupTestDatabase(db);
  });
  
  it('should find user by id', async () => {
    // Tests basic repository functionality
  });
});

// Integration tests build upon unit test components
describe('Authentication Flow', () => {
  let db;
  let userRepository;
  let authService;
  
  beforeEach(async () => {
    db = await setupTestDatabase();
    await seedTestData(db);
    
    userRepository = new UserRepository(db);
    authService = new AuthService(userRepository);
  });
  
  afterEach(async () => {
    await cleanupTestDatabase(db);
  });
  
  it('should authenticate valid user', async () => {
    // Tests authentication using repository
  });
});
```

### Modularity in Testing
- Organize tests to mirror system structure
- Create independent test cases that can run in isolation
- Define clear test boundaries and responsibilities
- Design for independent test execution

Example:
```javascript
// Modular test organization
// /tests
//   /unit
//     /components
//       /auth
//         auth-service.test.js
//       /users
//         user-service.test.js
//   /integration
//     /auth
//       authentication-flow.test.js

// auth-service.test.js
describe('AuthService', () => {
  // Independent test setup
  let dependencies;
  
  beforeEach(() => {
    dependencies = createDependencies();
  });
  
  // Independent test cases
  it('should authenticate with valid credentials', () => {
    // Test implementation
  });
  
  it('should reject invalid credentials', () => {
    // Test implementation
  });
});

// authentication-flow.test.js
describe('Authentication Flow', () => {
  // Independent integration test
  // Can run regardless of unit test status
});
```

### Coherence in Testing
- Apply consistent testing patterns
- Use standard assertion approaches
- Maintain similar test structure across components
- Follow established naming conventions

Example:
```javascript
// Coherent test structure
// User service tests
describe('UserService', () => {
  describe('createUser', () => {
    it('should create a valid user', () => {
      // Arrange
      // Act
      // Assert
    });
    
    it('should reject invalid data', () => {
      // Arrange
      // Act
      // Assert
    });
  });
});

// Product service tests - same pattern
describe('ProductService', () => {
  describe('createProduct', () => {
    it('should create a valid product', () => {
      // Arrange
      // Act
      // Assert
    });
    
    it('should reject invalid data', () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

### Clarity in Testing
- Write descriptive test names that explain intent
- Structure tests with clear arrange-act-assert phases
- Document complex test scenarios
- Include context information in assertions

Example:
```javascript
// Clear test intent and structure
describe('Payment Processing', () => {
  // Descriptive test name
  it('should process credit card payment and apply discount for premium customers', async () => {
    // Arrange - Clear setup for test context
    const premiumCustomer = createTestUser({ accountType: 'premium' });
    const paymentDetails = createTestPayment({ type: 'credit_card' });
    const order = createTestOrder({ total: 100 });
    const paymentService = new PaymentService(mockGateway, mockDiscountService);
    
    // Act - Clear action being tested
    const result = await paymentService.processPayment(
      premiumCustomer, order, paymentDetails
    );
    
    // Assert - Clear expectations with context
    // Verify payment was processed
    expect(mockGateway.processPayment).toHaveBeenCalledWith(
      paymentDetails, order.total * 0.9 // 10% discount
    );
    
    // Verify discount was applied
    expect(result.appliedDiscount).toBe(10); // 10% discount
    expect(result.finalAmount).toBe(90); // 100 - 10% discount
    
    // Verify receipt was generated
    expect(result.receipt).toContain('Premium Discount: 10%');
  });
});
```

### Adaptivity in Testing
- Adjust test approach to system context
- Apply appropriate testing strategies for different components
- Scale test coverage based on code criticality
- Adapt test patterns to technology stack

Example:
```javascript
// Adaptive testing based on component type and risk
// High-risk component with thorough testing
describe('PaymentProcessor', () => {
  // Extensive test cases for high-risk functionality
  it('should process valid payment', () => { /* ... */ });
  it('should handle network failures gracefully', () => { /* ... */ });
  it('should retry failed transactions', () => { /* ... */ });
  it('should log transaction attempts', () => { /* ... */ });
  it('should prevent duplicate charges', () => { /* ... */ });
  it('should validate payment details', () => { /* ... */ });
  it('should handle various payment methods', () => { /* ... */ });
  // Many more test cases...
});

// Lower-risk component with focused testing
describe('UserPreferences', () => {
  // Focused testing on core functionality
  it('should store user preferences', () => { /* ... */ });
  it('should retrieve user preferences', () => { /* ... */ });
  it('should handle missing preferences', () => { /* ... */ });
});
```

## Testing Strategy by System Context

### Testing in Early Exploration Context
- Focus on flexibility and rapid iteration
- Emphasize unit testing for core concepts
- Use exploratory testing for new features
- Maintain minimal but effective test coverage
- Establish foundation for future test expansion

### Testing in Active Development Context
- Create comprehensive test coverage
- Balance between different test types
- Implement continuous testing practices
- Evolve test suite alongside system changes
- Focus on regression prevention

### Testing in Maintenance Context
- Emphasize regression testing
- Maintain high test coverage
- Focus on system stability
- Implement performance and security verification
- Create thorough documentation for tests

### Testing in Legacy Context
- Create characterization tests for existing behavior
- Focus on non-intrusive testing approaches
- Implement monitoring alongside testing
- Document system behavior through tests
- Prioritize risk-based testing

## Testing Tools and Infrastructure

### Test Runner Configuration

Effective test runner setup:

```javascript
// Jest configuration example
// jest.config.js
module.exports = {
  // Base test directory structure
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  
  // File patterns to identify tests
  testMatch: [
    '**/__tests__/**/*.js',
    '**/*.{spec,test}.js'
  ],
  
  // Coverage configuration
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.d.ts',
    '!src/index.js',
    '!src/setupTests.js'
  ],
  
  // Coverage thresholds
  coverageThreshold: {
    global: {
      statements: 80,
      branches: 70,
      functions: 80,
      lines: 80
    },
    'src/components/': {
      statements: 90,
      branches: 85,
      functions: 90,
      lines: 90
    }
  },
  
  // Setup and teardown files
  setupFilesAfterEnv: ['<rootDir>/tests/setup.js'],
  
  // Mock configuration
  moduleNameMapper: {
    // Mock non-JS assets
    '\\.(jpg|jpeg|png|gif|svg)$': '<rootDir>/tests/mocks/fileMock.js',
    '\\.(css|less|scss)$': '<rootDir>/tests/mocks/styleMock.js',
    // Alias paths for imports
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  
  // Test environment
  testEnvironment: 'jsdom',
  
  // Transform files
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': 'babel-jest'
  },
  
  // Watchman configuration
  watchPlugins: [
    'jest-watch-typeahead/filename',
    'jest-watch-typeahead/testname'
  ]
};
```

### Test Data Management

Approaches for managing test data:

```javascript
// Test data management
// test-data/factories.js
const faker = require('faker');

// Base factories for common entities
const createUser = (overrides = {}) => ({
  id: faker.datatype.uuid(),
  name: faker.name.findName(),
  email: faker.internet.email(),
  createdAt: faker.date.past(),
  active: true,
  ...overrides
});

const createProduct = (overrides = {}) => ({
  id: faker.datatype.uuid(),
  name: faker.commerce.productName(),
  price: faker.commerce.price(),
  category: faker.commerce.department(),
  inStock: true,
  ...overrides
});

// Specialized factories for specific test scenarios
const createPremiumUser = (overrides = {}) => 
  createUser({
    subscription: 'premium',
    paymentMethod: {
      type: 'credit_card',
      lastFour: '1234'
    },
    ...overrides
  });

const createOutOfStockProduct = (overrides = {}) =>
  createProduct({
    inStock: false,
    ...overrides
  });

// Collection generators
const createUsers = (count, template = {}) =>
  Array.from({ length: count }, () => createUser(template));

const createProducts = (count, template = {}) =>
  Array.from({ length: count }, () => createProduct(template));

// Complete test scenario factories
const createCheckoutScenario = (options = {}) => {
  const user = options.user || createUser();
  const products = options.products || [
    createProduct({ price: 10 }),
    createProduct({ price: 20 })
  ];
  
  return {
    user,
    products,
    cart: {
      id: faker.datatype.uuid(),
      userId: user.id,
      items: products.map(product => ({
        productId: product.id,
        quantity: faker.datatype.number({ min: 1, max: 5 }),
        price: product.price
      }))
    },
    paymentDetails: {
      method: 'credit_card',
      cardToken: 'test_token'
    }
  };
};

module.exports = {
  createUser,
  createProduct,
  createPremiumUser,
  createOutOfStockProduct,
  createUsers,
  createProducts,
  createCheckoutScenario
};
```

### Mock Management

Approaches for managing mocks:

```javascript
// Mock management
// test-utils/mocks.js
const createMockRepository = (entityType, data = []) => {
  const dataMap = new Map(data.map(item => [item.id, item]));
  
  return {
    findById: jest.fn(async (id) => dataMap.get(id) || null),
    
    findAll: jest.fn(async () => Array.from(dataMap.values())),
    
    findBy: jest.fn(async (criteria) => {
      return Array.from(dataMap.values()).filter(item => {
        return Object.entries(criteria).every(([key, value]) => item[key] === value);
      });
    }),
    
    save: jest.fn(async (entity) => {
      if (!entity.id) {
        entity.id = `${entityType}-${Date.now()}`;
      }
      dataMap.set(entity.id, {...entity});
      return entity;
    }),
    
    update: jest.fn(async (id, updates) => {
      const existing = dataMap.get(id);
      if (!existing) return null;
      
      const updated = {...existing, ...updates};
      dataMap.set(id, updated);
      return updated;
    }),
    
    delete: jest.fn(async (id) => {
      return dataMap.delete(id);
    }),
    
    // Helper to access internal state for assertions
    _getData: () => Array.from(dataMap.values()),
    
    // Helper to reset state
    _reset: (newData = []) => {
      dataMap.clear();
      newData.forEach(item => dataMap.set(item.id, item));
    }
  };
};

const createMockService = (serviceName, methods = {}) => {
  const defaultMethods = {
    // Common service methods that return success by default
    // but can be overridden with specific behaviors
  };
  
  const mockService = {
    ...defaultMethods,
    ...methods,
    
    // Failure simulation helpers
    _simulateError: (methodName, error) => {
      const originalMethod = mockService[methodName];
      mockService[methodName] = jest.fn().mockRejectedValue(error);
      
      return {
        restore: () => {
          mockService[methodName] = originalMethod;
        }
      };
    },
    
    // Reset all mocks
    _reset: () => {
      Object.values(mockService)
        .filter(value => typeof value === 'function' && value.mockReset)
        .forEach(mockFn =>