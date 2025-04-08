---
description: USE WHEN enhancing AI capabilities: Design and implement agent capabilities with appropriate knowledge structures, interaction patterns, and collaborative models that embody meta-systemic principles.
globs: 
alwaysApply: false
---
---
description: "Agent capability patterns for applying meta-systemic principles across AI agent functions"
globs: "**/prompts/**/*.md,**/agent_guidelines/**/*.md,**/agent/**/*.md"
priority: 2
alwaysApply: false
type: "Agent-Requested"
---

# Agent Pattern Guidance

<critical>
Apply these patterns when developing or enhancing AI agent capabilities to ensure effective application of meta-systemic principles across all agent interactions and knowledge domains.
</critical>

## Pattern Application Process

When working with agent capabilities, follow this process:

1. **IDENTIFY** the capability type and interaction context
2. **SELECT** the appropriate patterns for that context
3. **APPLY** the patterns consistently across agent capabilities
4. **VALIDATE** that the capability effectively embodies meta-systemic principles

## Core Agent Patterns

### Knowledge Domain Pattern

```yaml
pattern:
  name: "Structured Knowledge Domain"
  principles: [modularity, parsimony]
  context: "AI agent knowledge management"
  application:
    - "Organize knowledge into clear domain boundaries"
    - "Establish canonical references for key concepts"
    - "Define relationships between knowledge domains"
    - "Enable context-sensitive knowledge application"
  example: |
    # Technical Knowledge Domain: Authentication
    
    <domain>
    name: "Authentication"
    category: "Security"
    related_domains: ["Authorization", "User Management", "Encryption"]
    canonical_concepts:
      - concept: "authentication_flow"
        definition: "The sequence of steps to verify user identity"
        references: ["security/authentication_flow.md"]
      - concept: "multi_factor_authentication"
        definition: "Authentication using multiple verification methods"
        references: ["security/mfa.md"]
    context_adaptations:
      - context: "web_application"
        emphasis: ["session_management", "cookie_security"]
      - context: "mobile_application"
        emphasis: ["token_management", "biometric_authentication"]
      - context: "api_service"
        emphasis: ["oauth_flow", "jwt_validation"]
    </domain>
    
    ## Authentication Flow
    
    The standard authentication flow consists of:
    
    1. **Credential Collection**: Gather user identification (username/email) and verification (password/token)
    2. **Credential Validation**: Verify credentials against stored data
    3. **Session Establishment**: Create secure session or issue authentication token
    4. **Authorization Mapping**: Determine user permissions and roles
    
    ## Authentication Methods
    
    Common authentication methods include:
    
    - **Password-based**: Traditional username/password verification
    - **Token-based**: JWT or similar token verification
    - **Certificate-based**: Using digital certificates
    - **Biometric**: Fingerprint, facial recognition, etc.
    - **Multi-factor**: Combining multiple authentication methods
    
    ## Implementation Considerations
    
    When implementing authentication:
    
    - Protect credentials in transit with TLS/SSL
    - Never store plaintext passwords
    - Use established hashing algorithms with proper salting
    - Implement account lockout mechanisms
    - Consider session timeout and renewal strategies
```

### Interaction Pattern Pattern

```yaml
pattern:
  name: "Context-Sensitive Interaction Pattern"
  principles: [clarity, adaptivity]
  context: "AI agent-human interactions"
  application:
    - "Define clear interaction flows with context adaptations"
    - "Structure dialogue with appropriate knowledge application"
    - "Include examples of successful interactions"
    - "Provide guidance for different interaction contexts"
  example: |
    # Interaction Pattern: Technical Problem Resolution
    
    <interaction_pattern>
    name: "Technical Problem Resolution"
    purpose: "Assist in diagnosing and resolving technical issues"
    phases:
      - name: "Problem Understanding"
        goal: "Establish clear understanding of the technical issue"
        techniques:
          - "Ask clarifying questions about symptoms and context"
          - "Confirm understanding before proceeding"
          - "Establish technical environment details"
        
      - name: "Diagnosis"
        goal: "Identify potential causes of the issue"
        techniques:
          - "Apply structured troubleshooting approach"
          - "Leverage relevant technical knowledge domains"
          - "Consider common failure patterns"
        
      - name: "Solution Development"
        goal: "Provide clear resolution steps"
        techniques:
          - "Present solutions in order of likelihood and simplicity"
          - "Explain rationale behind recommendations"
          - "Include verification steps for each solution"
        
      - name: "Verification"
        goal: "Ensure problem is resolved"
        techniques:
          - "Ask for confirmation of solution effectiveness"
          - "Provide additional guidance if needed"
          - "Capture resolution details for knowledge enhancement"
    
    context_adaptations:
      - context: "novice_user"
        adjustments:
          - "Use simpler technical terminology"
          - "Provide more detailed step-by-step instructions"
          - "Include explanations of technical concepts"
        
      - context: "expert_user"
        adjustments:
          - "Use more technical language"
          - "Focus on efficient diagnosis and resolution"
          - "Reference advanced techniques and tools"
        
      - context: "critical_system"
        adjustments:
          - "Emphasize safety and verification steps"
          - "Consider business impact of solutions"
          - "Include fallback and rollback procedures"
    </interaction_pattern>
    
    ## Example Dialogue
    
    ### Problem Understanding Phase
    
    **User**: I'm getting a "connection refused" error when trying to connect to my database.
    
    **Agent**: I'll help you troubleshoot that connection issue. To understand better:
    1. When did this issue start?
    2. What database system are you using (MySQL, PostgreSQL, etc.)?
    3. Have you made any recent changes to your network, server, or database configuration?
    
    **User**: It started about an hour ago. We're using PostgreSQL. We deployed some network changes this morning.
    
    **Agent**: Thank you for that information. So we have a PostgreSQL connection issue that started after network changes. Let me confirm: Can you access the database server through other means (like SSH)? And are other services or applications able to connect to the database?
    
    ### Diagnosis Phase
    
    **Agent**: Based on the timing coinciding with network changes and the "connection refused" error, this suggests a few potential causes:
    
    1. Firewall rules may be blocking the database port (typically 5432 for PostgreSQL)
    2. The database service might not be running
    3. PostgreSQL might be configured to listen only on specific interfaces
    4. Network routing issues between your client and the database
    
    Let's systematically check these possibilities.
    
    ### Solution Development Phase
    
    **Agent**: Let's start with the most likely issues:
    
    1. **Verify the database service is running**:
       ```bash
       sudo systemctl status postgresql
       # or on some systems
       sudo service postgresql status
       ```
    
    2. **Check PostgreSQL configuration**:
       Verify the `listen_addresses` setting in `postgresql.conf`:
       ```bash
       grep listen_addresses /etc/postgresql/*/main/postgresql.conf
       ```
       It should include '*' or the specific IP addresses needed.
    
    3. **Check firewall rules**:
       ```bash
       sudo iptables -L | grep 5432
       # or if using ufw
       sudo ufw status
       ```
    
    Would you like to start with these steps, or do you have additional information that might help narrow down the issue?
    
    ### Verification Phase
    
    **User**: I checked and the service is running, but the PostgreSQL config was only listening on localhost! I changed it to listen on all interfaces and restarted, now it works.
    
    **Agent**: Excellent! I'm glad to hear that solved the issue. The "connection refused" error is consistent with PostgreSQL only listening on localhost, especially after network changes.
    
    To summarize what we did:
    1. Identified that PostgreSQL was only listening on localhost interface
    2. Modified the `listen_addresses` setting in `postgresql.conf`
    3. Restarted the PostgreSQL service to apply changes
    
    For future reference, this is a common issue after network changes. If you're concerned about security, consider configuring PostgreSQL to listen only on specific IP addresses rather than all interfaces ('*'), and ensure your firewall rules are properly configured to allow only authorized access.
    
    Is there anything else you'd like help with regarding your database configuration?
```

### Capability Enhancement Pattern

```yaml
pattern:
  name: "Iterative Capability Enhancement"
  principles: [adaptivity, tensegrity]
  context: "AI agent capability development"
  application:
    - "Define clear capability scope and boundaries"
    - "Establish improvement metrics and evaluation criteria"
    - "Create adaptation mechanisms for different contexts"
    - "Build balanced relationship with human collaborators"
  example: |
    # Capability Enhancement: Code Quality Analysis
    
    <capability>
    name: "Code Quality Analysis"
    purpose: "Evaluate code quality and provide improvement recommendations"
    knowledge_domains: ["coding_standards", "design_patterns", "static_analysis"]
    
    evaluation_criteria:
      - criteria: "Detection Accuracy"
        description: "Ability to accurately identify quality issues"
        measurement: "% of true positives vs. false positives"
        target: ">90% accuracy across sample code"
      
      - criteria: "Recommendation Quality"
        description: "Usefulness and relevance of improvement suggestions"
        measurement: "User acceptance rate of recommendations"
        target: ">80% acceptance rate"
      
      - criteria: "Context Sensitivity"
        description: "Ability to adapt to different programming contexts"
        measurement: "Appropriate guidance across different languages/frameworks"
        target: "Correct adaptation in >85% of context shifts"
    
    evolution_stages:
      - stage: "Foundation"
        capabilities:
          - "Basic syntax and style issue detection"
          - "Common anti-pattern identification"
          - "Simple refactoring suggestions"
        
      - stage: "Enhancement"
        capabilities:
          - "Advanced pattern recognition"
          - "Performance issue detection"
          - "Security vulnerability identification"
          - "Architecture-level recommendations"
        
      - stage: "Optimization"
        capabilities:
          - "Context-specific best practice guidance"
          - "Team pattern consistency enforcement"
          - "Codebase-specific recommendation learning"
          - "Long-term quality trend analysis"
    
    human_collaboration:
      - role: "Human Developer"
        responsibilities:
          - "Provide context for code understanding"
          - "Evaluate recommendation relevance"
          - "Make final implementation decisions"
          - "Provide feedback for capability improvement"
        
      - role: "AI Agent"
        responsibilities:
          - "Perform systematic code analysis"
          - "Generate concrete improvement recommendations"
          - "Explain rationale for suggestions"
          - "Adapt recommendations to feedback"
        
      - collaboration_patterns:
        - pattern: "Pair Analysis"
          description: "Joint code review with developer leading and agent augmenting"
        - pattern: "Pre-Commit Review"
          description: "Agent provides review before code is committed"
        - pattern: "Learning Mode"
          description: "Agent observes developer refactoring to learn patterns"
    </capability>
    
    ## Implementation Examples
    
    ### Basic Style Issue Detection
    
    **Code with issues**:
    ```javascript
    function calculateTotal(items){
      let t = 0
      for(let i=0;i<items.length;i++){
        t += items[i].price
      }
      return t
    }
    ```
    
    **Agent analysis**:
    ```
    I've analyzed your function and found some style issues:
    
    1. Missing space after function parameters
    2. Variable name 't' is not descriptive
    3. Missing semicolons at line ends
    4. Missing spaces in for loop definition
    
    Suggested improvement:
    
    ```javascript
    function calculateTotal(items) {
      let total = 0;
      for (let i = 0; i < items.length; i++) {
        total += items[i].price;
      }
      return total;
    }
    ```
    
    This improves readability while maintaining the same functionality.
    ```
    
    ### Advanced Pattern Recognition
    
    **Code with issues**:
    ```javascript
    function getUser(userId) {
      return database.query(`SELECT * FROM users WHERE id = '${userId}'`);
    }
    ```
    
    **Agent analysis**:
    ```
    I've identified a critical security issue in your code:
    
    SQL Injection Vulnerability: The function directly interpolates the userId into the SQL query, which could allow SQL injection attacks if userId comes from user input.
    
    Recommendation:
    
    ```javascript
    function getUser(userId) {
      return database.query('SELECT * FROM users WHERE id = ?', [userId]);
    }
    ```
    
    This uses parameterized queries to prevent SQL injection attacks.
    
    Additional considerations:
    1. Consider whether you need all columns (`*`) or just specific ones
    2. Add error handling for cases where the user isn't found
    3. Consider validating userId format before querying
    ```
    
    ### Context-Specific Recommendations
    
    **Context information**: High-performance financial application using React
    
    **Code with issues**:
    ```javascript
    function StockDisplay({ stocks }) {
      const [filteredStocks, setFilteredStocks] = useState([]);
      
      useEffect(() => {
        const filtered = stocks.filter(stock => stock.change > 0);
        setFilteredStocks(filtered);
      }, [stocks]);
      
      return (
        <div>
          {filteredStocks.map(stock => (
            <div key={stock.symbol}>
              {stock.symbol}: ${stock.price} ({stock.change}%)
            </div>
          ))}
        </div>
      );
    }
    ```
    
    **Agent analysis**:
    ```
    Based on your financial application context where performance is critical, I've identified several optimization opportunities:
    
    1. Unnecessary re-rendering: The current approach filters stocks on every render cycle
    
    2. Missing memoization: For financial data that updates frequently, memoization would significantly improve performance
    
    3. Rendering optimization: The list rendering can be optimized for large datasets
    
    Recommended implementation:
    
    ```javascript
    function StockDisplay({ stocks }) {
      // Memoize the filtered stocks to prevent unnecessary recalculations
      const filteredStocks = useMemo(() => 
        stocks.filter(stock => stock.change > 0),
        [stocks]
      );
      
      // For financial applications, consider using a virtualized list for performance
      return (
        <div className="stock-list">
          {filteredStocks.map(stock => (
            <StockRow 
              key={stock.symbol} 
              symbol={stock.symbol}
              price={stock.price}
              change={stock.change}
            />
          ))}
        </div>
      );
    }
    
    // Separate component with memo for optimized re-rendering
    const StockRow = memo(({ symbol, price, change }) => (
      <div className="stock-row">
        <span className="symbol">{symbol}</span>
        <span className="price">${price}</span>
        <span className={change > 0 ? "positive-change" : "negative-change"}>
          ({change}%)
        </span>
      </div>
    ));
    ```
    
    This implementation:
    - Uses `useMemo` to prevent unnecessary recalculations
    - Creates a separate memoized component for list items
    - Improves performance for real-time financial data
    - Still maintains the same functionality
    ```
```

### Knowledge Integration Pattern

```yaml
pattern:
  name: "Multi-Domain Knowledge Integration"
  principles: [parsimony, coherence]
  context: "Complex AI agent problem-solving"
  application:
    - "Connect knowledge across domain boundaries"
    - "Apply consistent reasoning patterns across domains"
    - "Establish clear knowledge references and relationships"
    - "Balance domain specificity with cross-domain integration"
  example: |
    # Knowledge Integration: Full-Stack Application Development
    
    <knowledge_integration>
    primary_domains:
      - "frontend_development"
      - "backend_development"
      - "database_systems"
      - "deployment_infrastructure"
    
    integration_points:
      - domains: ["frontend_development", "backend_development"]
        connections:
          - "API contract design and implementation"
          - "Authentication and authorization flow"
          - "Data validation and error handling"
        canonical_references:
          - "api_design/contract_first_development.md"
          - "security/auth_implementation.md"
      
      - domains: ["backend_development", "database_systems"]
        connections:
          - "Data access patterns"
          - "Query optimization"
          - "Transaction management"
        canonical_references:
          - "data_access/repository_pattern.md"
          - "database/query_optimization.md"
      
      - domains: ["backend_development", "deployment_infrastructure"]
        connections:
          - "Configuration management"
          - "Environment-specific adaptations"
          - "Logging and monitoring"
        canonical_references:
          - "devops/configuration_management.md"
          - "operations/logging_best_practices.md"
      
      - domains: ["frontend_development", "deployment_infrastructure"]
        connections:
          - "Static asset optimization"
          - "Caching strategies"
          - "CDN integration"
        canonical_references:
          - "performance/frontend_optimization.md"
          - "deployment/cdn_strategies.md"
    
    reasoning_patterns:
      - name: "Full-Stack Problem Diagnosis"
        steps:
          - "Isolate issue to specific layer(s)"
          - "Examine integration points between layers"
          - "Trace data and control flow across boundaries"
          - "Consider cross-cutting concerns (security, performance)"
        
      - name: "Technology Stack Selection"
        steps:
          - "Evaluate requirements across all layers"
          - "Ensure technological compatibility"
          - "Consider team expertise and ecosystem maturity"
          - "Assess operational implications"
        
      - name: "Cross-Cutting Implementation"
        steps:
          - "Design consistent patterns across layers"
          - "Implement from contract boundaries inward"
          - "Validate complete flow across boundaries"
          - "Optimize critical cross-layer interactions"
    </knowledge_integration>
    
    ## Integration Application Example
    
    ### Problem Statement
    
    User reports slow application performance with increased load.
    
    ### Integrated Analysis Approach
    
    **1. Isolate Performance Issues**
    
    Examine performance across application layers to identify bottlenecks:
    
    - **Frontend Metrics**:
      - Page load time: 3.5s (exceeds 2s target)
      - First contentful paint: 1.8s
      - API response rendering time: 0.5s
    
    - **Backend Metrics**:
      - API endpoint response times: 800ms average (exceeds 300ms target)
      - Database query time: 650ms average
      - Business logic processing: 120ms
    
    - **Database Metrics**:
      - Query execution plan shows table scan operations
      - Index utilization below 60%
      - Connection pool utilization at 85%
    
    - **Infrastructure Metrics**:
      - CPU utilization: 65% (acceptable)
      - Memory utilization: 80% (high but not critical)
      - Network latency: normal
    
    **2. Cross-Domain Performance Improvement Strategy**
    
    Based on integrated analysis, the primary bottlenecks are in database query performance with cascading effects on API response times and overall application performance. The recommended cross-domain approach:
    
    **Database Layer**:
    - Optimize query performance by adding appropriate indexes
    - Implement query caching for frequently accessed data
    - Review and optimize DB connection management
    
    **Backend Layer**:
    - Implement response caching for expensive operations
    - Add pagination for large data sets
    - Consider async processing for non-critical operations
    
    **Frontend Layer**:
    - Implement progressive loading for large data sets
    - Add loading indicators for improved user experience
    - Consider client-side caching of static data
    
    **Infrastructure Layer**:
    - Review scaling policies for database resources
    - Consider read replicas for query distribution
    - Implement performance monitoring across all layers
    
    This integrated approach addresses the root cause while optimizing the entire application stack, demonstrating knowledge integration across all domains.
```

### Prompt Design Pattern

```yaml
pattern:
  name: "Contextual Prompt Engineering"
  principles: [clarity, adaptivity]
  context: "AI agent prompt development"
  application:
    - "Design prompts with clear structure and purpose"
    - "Include context-specific adaptations"
    - "Balance comprehensive instruction with conciseness"
    - "Provide effective examples for guidance"
  example: |
    # Prompt Design: Code Review Assistant
    
    <prompt_template>
    name: "Code Review Assistant"
    purpose: "Provide comprehensive code review with actionable feedback"
    structure:
      - section: "Context Setting"
        purpose: "Establish the technical context for appropriate review"
        components:
          - "Technological stack information"
          - "Project-specific standards reference"
          - "Review focus areas"
          - "Code context (file purpose, related components)"
      
      - section: "Review Guidance"
        purpose: "Provide specific guidance on review approach"
        components:
          - "Review depth instruction"
          - "Principle prioritization"
          - "Output format specification"
          - "Expected review categories"
      
      - section: "Examples and Standards"
        purpose: "Demonstrate expected review quality and approach"
        components:
          - "Example code snippets with reviews"
          - "Project-specific patterns to enforce"
          - "Common issues to identify"
      
      - section: "Response Formatting"
        purpose: "Ensure consistent, actionable review format"
        components:
          - "Summary section structure"
          - "Issue categorization format"
          - "Recommendation formatting"
          - "Code example formatting"
      
    context_adaptations:
      - context: "security_review"
        specialization:
          - "Emphasize security vulnerability detection"
          - "Include OWASP reference categories"
          - "Prioritize security over other concerns"
          - "Include severity ratings for security issues"
      
      - context: "performance_review"
        specialization:
          - "Focus on computational and memory efficiency"
          - "Include performance impact estimates"
          - "Recommend performance measurement approaches"
          - "Identify potential bottlenecks"
      
      - context: "maintainability_review"
        specialization:
          - "Emphasize readability and documentation"
          - "Focus on architectural patterns and consistency"
          - "Identify technical debt indicators"
          - "Suggest refactoring opportunities"
    </prompt_template>
    
    ## Implementation Example
    
    ### Standard Code Review Prompt
    
    ```
    # Code Review Request
    
    ## Context
    
    - **Language/Framework**: TypeScript with React
    - **Project Standards**: Following Airbnb style guide and project-specific patterns
    - **Review Focus**: General quality, maintainability, and adherence to best practices
    - **File Purpose**: User authentication component handling login, registration, and password reset
    
    ## Code for Review
    
    ```typescript
    import React, { useState } from 'react';
    import axios from 'axios';
    
    const Auth = (props) => {
      const [email, setEmail] = useState('');
      const [password, setPass] = useState('');
      const [error, setError] = useState('');
      
      async function handleSubmit(event) {
        event.preventDefault();
        try {
          const res = await axios.post('/api/login', { email: email, password: password });
          if(res.data.token) {
            localStorage.setItem('token', res.data.token);
            props.setLoggedIn(true);
          }
        } catch(e) {
          setError('Login failed');
          console.log(e);
        }
      }
      
      return (
        <div className="auth-form">
          <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            {error && <div className="error">{error}</div>}
            <div>
              <label>Email</label>
              <input 
                type="email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
                required
              />
            </div>
            <div>
              <label>Password</label>
              <input 
                type="password" 
                value={password} 
                onChange={(e) => setPass(e.target.value)} 
                required
              />
            </div>
            <button type="submit">Login</button>
          </form>
        </div>
      );
    }
    
    export default Auth;
    ```
    
    ## Review Guidance
    
    Please provide a comprehensive code review addressing:
    
    1. Code quality and best practices
    2. Type safety and TypeScript usage
    3. React patterns and component design
    4. Security considerations
    5. Error handling and user experience
    
    For each issue, provide:
    - A clear description of the issue
    - The potential impact or risk
    - A specific recommendation with code example
    
    ## Example Review Format
    
    ```
    # Code Review Summary
    
    ## Overview
    [1-2 paragraphs summarizing the overall assessment]
    
    ## Key Issues
    
    ### [Issue Category] - [Severity: High/Medium/Low]
    **Issue**: [Clear description]
    **Impact**: [Why this matters]
    **Recommendation**:
    ```code
    // Code example showing the fix
    ```
    
    ## Additional Recommendations
    - [Bulleted list of minor suggestions]
    
    ## Positive Aspects
    - [Bulleted list of things done well]
    ```
    
    Please be thorough but constructive, focusing on actionable improvements.
    ```
    
    ### Security-Focused Adaptation
    
    ```
    # Security-Focused Code Review Request
    
    ## Context
    
    - **Language/Framework**: TypeScript with React
    - **Project Standards**: Following Airbnb style guide and OWASP security best practices
    - **Review Focus**: Security vulnerabilities and secure coding practices
    - **File Purpose**: User authentication component handling login, registration, and password reset
    
    ## Code for Review
    
    [Same code as above]
    
    ## Review Guidance
    
    Please provide a security-focused code review addressing:
    
    1. Authentication vulnerabilities
    2. Sensitive data handling
    3. CSRF/XSS prevention
    4. Secure storage practices
    5. Input validation and sanitization
    
    For each security issue, provide:
    - A clear description of the vulnerability
    - The potential security impact with CVSS severity estimate
    - A specific remediation recommendation with code example
    - Reference to relevant OWASP category where applicable
    
    ## Example Review Format
    
    ```
    # Security Review Summary
    
    ## Overview
    [1-2 paragraphs summarizing the security assessment]
    
    ## Security Vulnerabilities
    
    ### [Vulnerability Type] - [Severity: Critical/High/Medium/Low]
    **Vulnerability**: [Clear description]
    **Impact**: [Security implications]
    **OWASP Reference**: [Relevant OWASP category]
    **Remediation**:
    ```code
    // Code example showing the security fix
    ```
    
    ## Additional Security Recommendations
    - [Bulleted list of security hardening suggestions]
    
    ## Secure Implementation Aspects
    - [Bulleted list of security measures already in place]
    ```
    
    Please follow a defense-in-depth approach and assume sophisticated attackers.
    ```
```

### Collaboration Model Pattern

```yaml
pattern:
  name: "Human-AI Collaboration Framework"
  principles: [tensegrity, modularity]
  context: "Collaboration between human and AI team members"
  application:
    - "Define clear role boundaries and responsibilities"
    - "Establish structured collaboration workflows"
    - "Create explicit handoff protocols"
    - "Balance strengths of human and AI contributors"
  example: |
    # Collaboration Model: Software Development Partnership
    
    <collaboration_model>
    name: "Software Development Partnership"
    purpose: "Optimize the collaboration between human developers and AI assistants during software development"
    
    role_definitions:
      - role: "Human Developer"
        primary_responsibilities:
          - "Define requirements and acceptance criteria"
          - "Make architectural decisions"
          - "Evaluate generated code quality and correctness"
          - "Handle business context and stakeholder communication"
          - "Make final implementation decisions"
        
        strengths_leveraged:
          - "Domain expertise and business context understanding"
          - "Creative problem-solving for novel challenges"
          - "Intuitive understanding of user experience"
          - "Contextual judgment for trade-offs"
          - "Responsibility for final outcomes"
      
      - role: "AI Assistant"
        primary_responsibilities:
          - "Generate implementation options based on requirements"
          - "Identify potential issues and edge cases"
          - "Ensure consistency with established patterns"
          - "Provide comprehensive documentation"
          - "Apply best practices systematically"
        
        strengths_leveraged:
          - "Pattern recognition across large codebases"
          - "Systematic application of best practices"
          - "Comprehensive knowledge of language features"
          - "Consistency in documentation and style"
          - "Rapid generation of implementation alternatives"
    
    collaboration_workflows:
      - workflow: "Requirements to Implementation"
        stages:
          - stage: "Requirement Clarification"
            human_role: "Define high-level requirements and constraints"
            ai_role: "Ask clarifying questions and restate requirements"
            output: "Clear, detailed requirements specification"
          
          - stage: "Solution Design"
            human_role: "Make key architectural decisions"
            ai_role: "Generate design alternatives with trade-offs"
            output: "Chosen design approach with implementation plan"
          
          - stage: "Implementation"
            human_role: "Guide implementation priorities"
            ai_role: "Generate code following established patterns"
            output: "Initial implementation meeting requirements"
          
          - stage: "Refinement"
            human_role: "Review and identify improvement areas"
            ai_role: "Refine implementation based on feedback"
            output: "Polished implementation meeting quality standards"
      
      - workflow: "Code Review and Enhancement"
        stages:
          - stage: "Code Analysis"
            human_role: "Provide code and improvement goals"
            ai_role: "Analyze code for issues and opportunities"
            output: "Comprehensive code review"
          
          - stage: "Recommendation Selection"
            human_role: "Select priority improvements"
            ai_role: "Explain implications of different approaches"
            output: "Prioritized enhancement plan"
          
          - stage: "Implementation Support"
            human_role: "Apply selected improvements"
            ai_role: "Generate specific code examples"
            output: "Improved code quality"
          
          - stage: "Knowledge Transfer"
            human_role: "Learn from explanations and patterns"
            ai_role: "Explain rationale and best practices"
            output: "Enhanced developer understanding"
    
    handoff_protocols:
      - transition: "Human to AI"
        protocol:
          - "Clearly state the objective or problem"
          - "Provide relevant context and constraints"
          - "Specify expected output format and detail level"
          - "Indicate any specific approaches to consider or avoid"
      
      - transition: "AI to Human"
        protocol:
          - "Summarize understanding of the request"
          - "Present output with clear structure"
          - "Highlight key decisions or assumptions made"
          - "Indicate areas where human judgment is particularly needed"
      
      - transition: "Iterative Handoffs"
        protocol:
          - "Reference specific aspects of previous exchanges"
          - "Clearly indicate what has changed or been refined"
          - "Maintain continuity of context and decisions"
          - "Track progress toward overall objective"
    
    adaptation_strategies:
      - context: "Novel Problem Domains"
        strategy:
          - "Increase human guidance on domain specifics"
          - "AI focuses on general patterns and best practices"
          - "More iterative cycles with smaller steps"
          - "Explicit verification of domain assumptions"
      
      - context: "Time-Critical Development"
        strategy:
          - "AI provides more complete initial implementations"
          - "Human focuses on critical decision points only"
          - "Reduced iteration cycles"
          - "Prioritize core functionality over refinement"
      
      - context: "Learning-Focused Collaboration"
        strategy:
          - "AI provides more detailed explanations"
          - "Step-by-step implementation with teaching focus"
          - "Multiple alternative approaches with trade-offs"
          - "Focus on knowledge transfer over implementation speed"
    </collaboration_model>
    
    ## Collaboration Examples
    
    ### Feature Implementation Workflow
    
    **Human Developer**: I need to implement a user profile update feature that allows users to change their name, email, and profile picture. The email change should require verification, and we need to ensure proper validation of all fields. We're using our standard React frontend with Express backend.
    
    **AI Assistant**: I understand you need a user profile update feature with email verification. Let me clarify a few details:
    
    1. Are there specific validation rules for names and emails?
    2. Should users be able to use the application while their new email is pending verification?
    3. What's the preferred approach for handling profile pictures (local storage vs cloud)?
    4. Are there any size or format restrictions for profile images?
    
    **Human Developer**: Good questions. Names should be 2-50 characters, emails should follow standard formats. Users should continue using their old email until verification is complete. We'll use S3 for image storage, and images should be limited to 5MB, jpg/png formats only.
    
    **AI Assistant**: Thanks for the clarification. Based on your requirements, here's a proposed implementation approach:
    
    **Frontend**:
    - Create a ProfileUpdateForm component with fields for name, email, and profile image
    - Implement client-side validation for all fields
    - Add email verification UI elements (pending state, resend verification)
    - Implement image preview, cropping, and size validation
    
    **Backend**:
    - Extend user API with profile update endpoint
    - Implement email verification flow with secure tokens
    - Create S3 integration for image upload with type and size validation
    - Add validation middleware for all inputs
    
    Would you like me to proceed with implementing any specific part of this first?
    
    **Human Developer**: Let's start with the backend API for profile updates and the email verification flow.
    
    **AI Assistant**: I'll implement the backend API for profile updates and email verification. Here's my implementation:
    
    [Detailed code implementation for the backend API]
    
    The implementation includes:
    - Input validation middleware
    - Profile update endpoint with conditional email verification
    - Secure verification token generation and storage
    - Email verification endpoints for confirming changes
    - S3 integration for profile image uploads
    
    Key considerations:
    - Verification tokens expire after 24 hours
    - Old email remains active until verification completes
    - All operations are transactional to prevent partial updates
    
    Would you like me to explain any particular part in more detail or make any adjustments?
    
    **Human Developer**: This looks good overall, but I noticed we're not handling the case where a user might try to change their email to one that's already in use by another account. Can you add that check?
    
    **AI Assistant**: You're absolutely right, that's an important check to add. Here's the updated implementation with email uniqueness validation:
    
    [Updated code implementation with uniqueness check]
    
    I've made these changes:
    1. Added a uniqueness check before initiating email change
    2. Added a specific error code for duplicate email attempts
    3. Ensured this check happens before sending verification emails
    4. Added a test case for this scenario
    
    This prevents users from attempting to verify an email that's already taken, improving both security and user experience.
    
    **Human Developer**: Perfect, that covers everything we need for the backend. Let's proceed with implementing the frontend components next.
```

## Context-Specific Agent Patterns

### Development Assistance Patterns

When designing agent capabilities for development support:

1. **Code Generation Pattern**:
   - Generate code that follows project-specific conventions
   - Provide multiple implementation alternatives
   - Include comprehensive documentation
   - Explain design decisions and trade-offs

2. **Code Review Pattern**:
   - Analyze code systematically against best practices
   - Identify potential bugs, security issues, and optimizations
   - Suggest specific improvements with rationale
   - Balance criticism with positive reinforcement

3. **Debugging Support Pattern**:
   - Guide systematic problem isolation
   - Generate hypotheses based on symptoms
   - Suggest specific diagnostic approaches
   - Provide concrete solutions with explanations

4. **Architecture Guidance Pattern**:
   - Apply architectural patterns appropriately for the context
   - Balance technical considerations with business needs
   - Provide concrete implementation strategies
   - Explain trade-offs for different approaches

5. **Documentation Generation Pattern**:
   - Create comprehensive documentation at appropriate level
   - Include concrete examples for complex concepts
   - Organize information logically and accessibly
   - Tailor documentation to target audience

### Creativity Support Patterns

When designing agent capabilities for creative work:

1. **Idea Generation Pattern**:
   - Provide diverse but relevant suggestions
   - Balance novelty with practicality
   - Adapt creativity level to context
   - Build upon established themes cohesively

2. **Refinement Pattern**:
   - Suggest targeted improvements to creative work
   - Preserve original intent and voice
   - Provide specific enhancement options
   - Balance critical feedback with encouragement

3. **Expansion Pattern**:
   - Elaborate on existing creative elements
   - Maintain consistent tone and style
   - Develop related ideas cohesively
   - Integrate new material seamlessly

4. **Adaptation Pattern**:
   - Transform concepts across mediums or contexts
   - Preserve core essence while adapting form
   - Suggest context-appropriate modifications
   - Balance fidelity with contextual needs

5. **Critical Assessment Pattern**:
   - Provide balanced and constructive criticism
   - Analyze against relevant standards
   - Highlight strengths alongside improvement areas
   - Suggest specific enhancement strategies

### Analytical Support Patterns

When designing agent capabilities for analytical work:

1. **Data Analysis Pattern**:
   - Structure analytical approach systematically
   - Identify relevant patterns and anomalies
   - Apply appropriate analytical methods
   - Explain findings with appropriate visualizations

2. **Research Synthesis Pattern**:
   - Organize information logically and hierarchically
   - Identify key themes and relationships
   - Highlight contradictions and knowledge gaps
   - Present balanced viewpoints with evidence

3. **Problem-Solving Pattern**:
   - Break complex problems into manageable components
   - Apply structured reasoning frameworks
   - Generate multiple solution approaches
   - Evaluate options against criteria

4. **Decision Support Pattern**:
   - Structure decision framework with clear criteria
   - Present options with comprehensive pros and cons
   - Highlight key trade-offs and dependencies
   - Support decision process without replacing judgment

5. **Trend Analysis Pattern**:
   - Identify patterns across time and contexts
   - Distinguish signal from noise in data
   - Connect trends to broader implications
   - Present actionable insights based on trends

## Meta-Systemic Application

### Parsimony
- Define capabilities in canonical locations
- Reference standard patterns rather than redefining
- Create reusable interaction templates
- Maintain single source of truth for agent knowledge

Example:
```
Instead of creating custom interaction patterns for each capability, adapt the canonical [pattern:context_sensitive_interaction] to specific contexts with appropriate modifications.

For knowledge integration, reference the canonical domains rather than recreating domain knowledge:

```typescript
import { authenticationDomain } from '../knowledge/security/authentication.js';
import { userManagementDomain } from '../knowledge/users/management.js';

// Use imported knowledge rather than redefining
```
```

### Tensegrity
- Balance responsibilities between human and AI
- Create bidirectional value exchange in collaboration
- Design mutually supportive capability relationships
- Establish resilient interaction mechanisms

Example:
```
## Balanced Collaboration Model

The code review capability demonstrates tensegrity through balanced responsibilities:

**AI Responsibilities**:
- Systematic pattern detection
- Comprehensive review coverage
- Reference to best practices
- Code example generation

**Human Responsibilities**:
- Context provision
- Priority determination
- Final decision making
- Domain-specific insights

This balanced relationship provides mutual value in both directions.
```

### Modularity
- Create clear capability boundaries
- Define explicit interfaces for interaction
- Separate knowledge domains with clean interfaces
- Design for independent capability evolution

Example:
```
## Modular Capability Design

Agent capabilities should be modular with clear interfaces:

```typescript
interface CodeAnalysisCapability {
  // Clear input/output contract
  analyzeCode(code: string, options: AnalysisOptions): Promise<AnalysisResult>;
  
  // Capability-specific types
  type AnalysisOptions = {
    language: string;
    focus?: 'security' | 'performance' | 'maintainability';
    depth: 'basic' | 'comprehensive';
  };
  
  type AnalysisResult = {
    issues: Issue[];
    recommendations: Recommendation[];
    summary: string;
  };
}
```

This modular design allows capabilities to evolve independently while maintaining clear integration points.
```

### Coherence
- Apply consistent patterns across capabilities
- Use standard terminology and structures
- Follow established interaction models
- Maintain consistent knowledge representation

Example:
```
## Coherent Pattern Application

All agent capabilities should follow consistent patterns:

1. **Input Processing**: 
   - Clear context establishment
   - Requirement clarification if needed
   - Explicit confirmation of understanding

2. **Processing Approach**:
   - Structured, transparent methodology
   - Application of relevant knowledge domains
   - Consistent problem-solving frameworks

3. **Output Formatting**:
   - Standardized response structure
   - Consistent terminology
   - Clear organization with appropriate headings
   - Examples in consistent format

This coherence enables predictable interactions and faster learning for human collaborators.
```

### Clarity
- Provide explicit capability descriptions and limitations
- Include concrete examples for all interaction patterns
- Document reasoning processes transparently
- Explain knowledge application clearly

Example:
```
## Clarity Through Examples

Each capability should include clear examples showing:

**Input Example**:
```
I need to implement an authentication system for a Node.js API using JWT.
```

**Processing Clarity**:
```
Analyzing request:
1. Domain: Authentication implementation
2. Technology context: Node.js API
3. Specific approach: JWT
4. Implied needs: User management, token handling, security considerations
```

**Output Example**:
```
Here's an implementation approach for JWT authentication in Node.js:

[Structured, specific implementation with explanatory comments]

Key considerations:
- Token expiration and refresh strategy
- Secure storage of secrets
- Protection against common vulnerabilities

Implementation alternatives:
1. Passport.js integration (pros/cons)
2. Custom middleware approach (pros/cons)
```

This clarity ensures shared understanding and appropriate capability application.
```

### Adaptivity
- Design capabilities for context-specific adaptation
- Provide mechanisms for capability evolution
- Balance standard patterns with contextual needs
- Document adaptation strategies explicitly

Example:
```
## Adaptive Capability Application

Agent capabilities should adapt to different contexts:

**Code Review Adaptation**:

```yaml
context_adaptations:
  - context: "Startup / MVP"
    adaptations:
      - Emphasize development speed and flexibility
      - Focus on critical security and performance issues only
      - Suggest pragmatic solutions over perfect implementations
      - Prioritize user-facing functionality
  
  - context: "Enterprise / Regulated"
    adaptations:
      - Emphasize compliance and security
      - Apply comprehensive best practice validation
      - Suggest thorough documentation approaches
      - Prioritize maintainability and stability
      
  - context: "Educational"
    adaptations:
      - Emphasize learning opportunities
      - Explain recommendations in greater detail
      - Suggest multiple alternative approaches
      - Connect recommendations to broader principles
```

This adaptivity ensures appropriate capability application across different contexts.
```

## Implementation Validation Checklist

Before finalizing agent patterns, verify that:

- [ ] Patterns have clear purpose and application guidance
- [ ] Each pattern includes concrete examples
- [ ] Patterns can be adapted to different contexts
- [ ] Knowledge domains have clear boundaries and relationships
- [ ] Interaction patterns include appropriate structure
- [ ] Capability definitions include evaluation criteria
- [ ] Collaboration models balance human and AI responsibilities
- [ ] Patterns apply meta-systemic principles consistently
- [ ] Context-specific adaptations are clearly defined
- [ ] Pattern documentation is comprehensive and clear

<important>
Agent patterns form the foundation for effective AI capabilities that embody meta-systemic principles. Focus on creating patterns that balance structure with adaptivity, clearly define knowledge domains and interactions, and optimize the collaboration between human and AI team members.
</important>