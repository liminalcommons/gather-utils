---
description: 
globs: **/*.md,**/*.mdx,**/*.rst,**/*.txt,**/*.adoc,**/*.html
alwaysApply: false
---
---
description: "Documentation patterns for applying meta-systemic principles to all documentation types"
globs: "**/*.md,**/*.mdx,**/*.rst,**/*.txt,**/*.adoc,**/*.html"
priority: 2
alwaysApply: false
type: "Auto-Attached"
---

# Documentation Patterns

<critical>
Apply these documentation patterns when creating or updating any documentation to ensure clarity, consistency, and proper application of meta-systemic principles across all system contexts.
</critical>

## Pattern Application Process

When working with documentation, follow this process:

1. **IDENTIFY** the documentation type and purpose
2. **SELECT** the appropriate patterns for that context
3. **APPLY** the patterns consistently across the documentation
4. **VALIDATE** that the documentation effectively meets its purpose

## Core Documentation Patterns

### Document Structure Pattern

```yaml
pattern:
  name: "Hierarchical Document Structure"
  principles: [clarity, modularity]
  context: "All documentation types"
  application:
    - "Organize content in a clear hierarchy with logical sections"
    - "Use consistent heading levels to establish structure"
    - "Provide navigation aids like table of contents"
    - "Ensure each section has a clear purpose"
  example: |
    # Document Title
    
    ## 1. Introduction
    Brief overview of the document purpose and content.
    
    ## 2. Section One
    Main content for the first major topic.
    
    ### 2.1 Sub-section
    More detailed information on a specific aspect.
    
    #### 2.1.1 Further Detail
    Specific details about a narrow topic.
    
    ### 2.2 Another Sub-section
    Additional content related to the first major topic.
    
    ## 3. Section Two
    Main content for the second major topic.
```

### Knowledge Reference Pattern

```yaml
pattern:
  name: "Knowledge Reference System"
  principles: [parsimony, tensegrity]
  context: "All documentation types"
  application:
    - "Reference canonical sources instead of duplicating information"
    - "Use consistent reference formats for different content types"
    - "Establish bidirectional references between related content"
    - "Maintain reference integrity when content changes"
  example: |
    ## Authentication Process
    
    The user authentication process follows the [standard authentication flow](mdc:../security/authentication.md) with these specific adaptations for the admin interface:
    
    - Enhanced MFA requirements as specified in the [Admin Security Policy](mdc:../policies/admin-security.md)
    - Session timeout settings defined in the [Session Management Guidelines](mdc:../operations/session-management.md)
    
    For implementation Service API](../api/auth-service.md).
    
    ## Related Documentation
    - [User Authentication Guide](mdc:../user-guides/authentication.md)
    - [Security Incident Response](mdc:../security/incident-response.md)
    - [Complients](mdc:.ce.md#authentication)
```

### ClaritPattern  name: "Clarity Through Examples"
  principles: [clarity, "All documentation types"
  application:
    - "Provide concrete examples for complex concepts"
    - "Include code samples for technical documentation"
    - "Use visual elements to clarify relationships and flows"
    - "Demonstrate both common and edge cases"
  example: |
    ## Query Parameter Filtering
    
    The API supports filtering results using query parameters.
    
    ### Basic Filtering
    
    To filter by a single field, use the field name as a query parameter:
    
    ```
    GET /api/users?status=active
    ```
    
    ### Multiple Filters
    
    To apply multiple filters, include additional query parameters:
    
    ```
    GET /api/users?status=active&role=admin
    ```
    
    ### Advanced Filtering
    
    For more complex filtering, use the filter query parameter with JSON syntax:
    
    ```
    GET /api/users?filter={"created_at":{"$gt":"2023-01-01"}}
    ```
    
    ### Filter Operator Reference
    
    | Operator | Description | Example |
    |----------|-------------|---------|
    | $eq | Equal to | {"status":{"$eq":"active"}} |
    | $gt | Greater than | {"age":{"$gt":21}} |
    | $lt | Less than | {"priority":{"$lt":3}} |
    | $in | In array | {"status":{"$in":["active","pending"]}} |
```

### Metadata Pattern

```yaml
pattern:
  name: "Comprehensive Document Metadata"
  principles: [clarity, coherence]
  context: "All documentation types"
  application:
    - "Include consistent metadata at the document start"
    - "Specify document lifecycle information"
    - "Identify ownership and audience"
    - "Track document version and history"
  example: |
    ---
    title: "Authentication Service API Documentation"
    version: "2.3.0"
    created: "2023-05-15"
    last_updated: "2023-10-22"
    status: "Active"
    owner: "Security Team"
    audience: "Developers, System Integrators"
    lifecycle:
      created: "Documentation for v2 Authentication API"
      active: "Current reference for Auth API integration"
      obsolescence_criteria:
        - "When replaced by v3 Authentication API"
        - "When authentication model changes significantly"
    last_validated: "2023-10-15"
    ---
    
    # Authentication Service API
    
    This document provides comprehensive documentation for the Authentication Service API.
```

### Traceability Pattern

```yaml
pattern:
  name: "Requirement Traceability"
  principles: [tensegrity, coherence]
  context: "Technical and specification documents"
  application:
    - "Link documentation to specific requirements"
    - "Establish clear connections between related documents"
    - "Maintain forward and backward traceability"
    - "Identify impacts of changes"
  example: |
    ## Password Reset Feature
    
    **Requirement**: [REQ-AUTH-105](mdc:../requirements/authentication.md#REQ-AUTH-105)
    
    This feature implements the password reset functionality as specified in REQ-AUTH-105. The implementation includes:
    
    - Self-service password reset via email
    - Admin-initiated password reset
    - Secure reset token generation and validation
    
    **Implemented By**: [PasswordResetService](mdc:../code/auth/password-reset-service.ts)
    
    **Validated By**: [Password Reset Tests](mdc:../tests/auth/password-reset.test.ts)
    
    **Related Features**:
    - [User Authentication](mdc:user-authentication.md)
    - [Account Recovery](mdc:account-recovery.md)
    
    **Impact Analysis**:
    Changes to this feature may affect:
    - Email notification system
    - Authentication flow
    - Security audit logging
```

### Version Control Pattern

```yaml
pattern:
  name: "Version History Documentation"
  principles: [clarity, coherence]
  context: "All documentation types"
  application:
    - "Maintain explicit version history"
    - "Document significant changes with rationale"
    - "Track backwards compatibility information"
    - "Support parallel documentation versions when needed"
  example: |
    ## Version History
    
    | Version | Date | Author | Changes | Rationale |
    |---------|------|--------|---------|-----------|
    | 2.3.0 | 2023-10-22 | A. Garcia | Added OAuth2 authentication floty integrations |
    | 2.2.0 | 2023-08-15 FA options | Regulatory compliance 2023-07-02 | L. Chen | Fixed incorrect le | Bug fix for implementation error |
    | 2.1.0 | 2023-06-10 | A. Garcia | Added session management details | Support for new session controls |
    | 2.0.0 | 2023-05-15 | M. Johnson | Initial v2 API documentation | Major authentication model redesign |
    
    ### Compatibility Notes
    
    - 2.3.0: Fully backward compatible with 2.2.0
    - 2.2.0: Requires client updates for MFA support
    - 2.1.0: Fully backward compatible with 2.0.0
```

## Documentation Types and Specific Patterns

### API Documentation Patterns

When documenting APIs:

```yaml
api_documentation:
  purpose: "Document interfaces for developers integrating with the system"
  sections:
    - "Overview and authentication"
    - "Endpoint reference with request/response details"
    - "Error handling and status codes"
    - "Examples for common operations"
    - "Integration guidance"
  specific_patterns:
    - name: "Endpoint Documentation"
      example: |
        ## User Management API
        
        ### Get User
        
        Retrieves a user by their unique identifier.
        
        #### Request
        
        ```
        GET /api/users/{id}
        ```
        
        **Path Parameters**
        
        | Parameter | Type | Required | Description |
        |-----------|------|----------|-------------|
        | id | string | Yes | Unique identifier of the user |
        
        **Headers**
        
        | Header | Required | Description |
        |--------|---        | Authorization | Yes | Bearer token for authentication |
        | Accept | No | Response format (default: application/json) |
        
        #### Response
        
        **200 OK**
        
        ```json
        {
          "id": "user-123",
          "name": "Jane Smitexample.com",
          "role": "admin",
          "created_at": "2023-01-15T10:30:00Z",
          "updated_at": "2023-10-01T14:25:30Z"
        }
        ```
        
        **404 Not Found**
        
        ```json
        {
          "error": "user_not_found",
          "message": "User with ID user-123 not found",
          "request_id": "req-abc-123"
        }
        ```
        
        #### Example
        
        ```bash
        curl -X GET \
          https://api.example.com/api/users/user-123 \
          -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ```
```

### Technical Documentation Patterns

When creating technical documentation:

```yaml
technical_documentation:
  purpose: "Document system architecture, components, and implementation details"
  sections:
    - "System overview and architecture"
    - "Component diagrams and relationships"
    - "Implementation details and patterns"
    - "Configuration and deployment"
    - "Monitoring and troubleshooting"
  specific_patterns:
    - name: "Architecture Documentation"
      example: |
        # Authentication Subsystem
        
        ## Architecture Overview
        
        The authentication subsystem implements a token-based authentication model with support for various authentication methods and multi-factor authentication.
        
        ![Authentication Architecture](mdc:../diagrams/auth-architecture.png)
        
        ## Components
        
        | Component | Responsibility | Dependencies |
        |-----------|----------------|--------------|
        | Authentication Service | Handle authentication requests | User Store, Token Service |
        | Token Service | Generate and validate tokens | Encryption Service |
        | MFA Provider | Manage MFA challenges | Notification Service |
        | User Store | Store user credentials | Database |
        
        ## Communication Flows
        
        1. **Authentication Flow**
           - Client submits credentials to Authentication Service
           - Auth Service validates credentials with User Store
           - If valid and MFA required, MFA challenge is initiated
           - Upon successful authentication, Token Service generates tokens
           - Tokens returned to client
        
        2. **Verification Flow**
           - Client submits token with request
           - Token Service validates token
           - If valid, user context is established
           - Request proceeds with authenticated context
        
        ## Configuration
        
        Key configuration parameters:
        
        ```yaml
        auth:
          token:
            lifetime: 3600  # Token lifetime in seconds
            refresh: 604800  # Refresh token lifetime in seconds
            algorithm: RS256  # Signing algorithm
          mfa:
            enabled: true  # Enable MFA
            methods:  # Supported MFA methods
              - totp
              - email
              - sms
        ```
```

### User Documentation Patterns

When creating user-facing documentation:

```yaml
user_documentation:
  purpose: "Guide users in effectively using the system"
  sections:
    - "Getting started"
    - "Feature guides"
    - "Common tasks and workflows"
    - "Troubleshooting"
    - "FAQ and reference"
  specific_patterns:
    - name: "Task-Based Documentation"
      example: |
        # Document Management
        
        ## Creating a New Document
        
        This guide walks through the process of creating and saving a new document.
        
        ### Prerequisites
        
        - You must be logged in to your account
        - You need 'Create' permission in at least one workspace
        
        ### Steps
        
        1. **Navigate to the Workspace**
           From the dashboard, click on the workspace where you want to create the document.
           
           ![Workspace Navigation](mdc:../images/workspace-nav.png)
        
        2. **Create New Document**
           Click the '+ New' button in the top right corner and select 'Document' from the dropdown.
           
           ![New Document](mdc:../images/new-document.png)
        
        3. **Add Document Content**
           Enter a title in the title field and add your content to the document body.
           
           - Use the formatting toolbar to style your text
           - Add images by clicking the image icon or dragging and dropping
           - Insert tables using the table menu
        
        4. **Save the Document**
           Click the 'Save' button in the top right corner. The document will be saved to the current workspace.
        
        ### Result
        
        Your new document will appear in the workspace document list and be available to all workspace members with appropriate permissions.
        
        ### Troubleshooting
        
        **Document Doesn't Save**
        - Check your internet connection
        - Ensure you have sufficient permissions in the workspace
        - Try refreshing the page if the editor becomes unresponsive
        
        **Content Formatting Issues**
        - Use the 'Clear Formatting' button to remove problematic formatting
        - Try copying content to a plain text editor first, then back to the document
```

### Process Documentation Patterns

When documenting processes:

```yaml
process_documentation:
  purpose: "Define and explain organizational processes and workflows"
  sections:
    - "Process overview and purpose"
    - "Roles and responsibilities"
    - "Process steps and workflow"
    - "Inputs and outputs"
    - "Quality controls and metrics"
  specific_patterns:
    - name: "Process Flow Documentation"
      example: |
        # Release Deployment Process
        
        ## Process Overview
        
        This document outlines the standard process for deploying software releases to production environments. It ensures consistent, reliable deployments with appropriate controls and validations.
        
        ## Roles and Responsibilities
        
        | Role | Responsibilities | Participants |
        |------|------------------|--------------|
        | Release Manager | Overall process coordination, go/no-go decision | [Name/Team] |
        | Development Team | Preparation of release artifacts, deployment support | [Name/Team] |
        | QA Team | Pre and post-deployment validation | [Name/Team] |
        | Operations | Executing deployment, environment preparation | [Name/Team] |
        
        ## Process Flow
        
        ```mermaid
        flowchart TD
            A[Deployment Request] --> B{Pre-Deployment Checklist}
            B -->|Passed| C[Schedule Deployment]
            B -->|Failed| Z[Address Issues]
            Z --> B
            C --> D[Environment Preparation]
            D --> E[Deployment Execution]
            E --> F[Post-Deployment Verification]
            F -->|Passed| G[Release Completion]
            F -->|Failed| H{Severity Assessment}
            H -->|Critical| I[Rollback]
            H -->|Non-Critical| J[Issue Tracking]
            I --> K[Post-Rollback Verification]
            J --> G
            K --> G
        ```
        
        ## Process Steps
        
        ### 1. Deployment Request
        
        **Inputs**:
        - Completed Validation Report
        - Release Artifacts
        - Deployment Plan
        
        **Activities**:
        - Submit deployment request via deployment portal
        - Attach required documentation
        - Assign release manager
        
        **Outputs**:
        - Deployment ticket
        
        **Controls**:
        - Automated validation of required artifacts
        - Approval workflow for high-risk deployments
        
        ### 2. Pre-Deployment Checklist
        
        **Inputs**:
        - Deployment ticket
        - Release artifacts
        
        **Activities**:
        - Validate all artifacts are present and correct
        - Verify environment availability
        - Confirm all approvals are in place
        - Review deployment plan
        
        **Outputs**:
        - Completed pre-deployment checklist
        
        **Controls**:
        - Standardized checklist
        - Multi-party verification for critical items
        
        [Additional steps continue...]
```

## Context-Specific Documentation Guidance

### Code System Documentation

When documenting code systems, emphasize:

1. **Technical Accuracy**
   - Ensure all details are technically correct and current
   - Include version information for all referenced components
   - Verify code examples actually work
   - Include compatibility information

2. **Progressive Disclosure**
   - Start with high-level overview, then provide details
   - Create layered documentation from concepts to implementation details
   - Allow readers to drill down to the level of detail they need
   - Use collapsible sections for advanced or detailed content

3. **Interface Focus**
   - Clearly document all public interfaces
   - Distinguish between public and internal interfaces
   - Include contract information (pre/post conditions)
   - Document error handling and edge cases

4. **Implementation Guidance**
   - Provide best practices for implementation
   - Include anti-patterns to avoid
   - Document performance considerations
   - Offer security guidance where relevant

### Release System Documentation

When documenting release processes, emphasize:

1. **Process Clarity**
   - Document clear steps with entry/exit criteria
   - Define roles and responsibilities explicitly
   - Include decision points and approval requirements
   - Provide templates for required artifacts

2. **Consistency and Standards**
   - Use consistent terminology throughout
   - Apply standard structures to similar processes
   - Reference governing policies and principles
   - Highlight meta-systemic principle application

3. **Adaptability Guidance**
   - Document how processes adapt to different contexts
   - Include guidance for different release scopes
   - Explain when and how to customize processes
   - Provide decision frameworks for adaptations

4. **Measurement and Improvement**
   - Document key process metrics
   - Include validation criteria for process execution
   - Provide improvement mechanisms
   - Track process evolution over time

### Agent System Documentation

When documenting agent capabilities, emphasize:

1. **Capability Clarity**
   - Clearly define agent capabilities and limitations
   - Provide concrete examples of effective use
   - Document context sensitivity in capabilities
   - Include edge case handling

2. **Interaction Patterns**
   - Document effective collaboration models
   - Provide examples of successful interactions
   - Include guidance for different interaction types
   - Demonstrate escalation and handoff patterns

3. **Knowledge Representation**
   - Document knowledge domain structures
   - Explain reference mechanisms
   - Show knowledge application examples
   - Demonstrate knowledge evolution

4. **Adaptation Guidance**
   - Explain context-sensitive behavior
   - Document capability adaptation mechanisms
   - Provide guidance for teaching new capabilities
   - Include examples of adaptive responses

## Meta-Systemic Principle Application

### Parsimony
- Define concepts once in canonical locations
- Reference rather than duplicate information
- Link to existing documentation for common concepts
- Use shared templates and structures

Example:
```markdown
## Authentication Methods

The system supports the standard [authentication methods](mdc:../security/authentication-methods.md) defined in our security model, with these specific adaptations for the admin interface:

- Enhanced MFA requirements
- Shorter session timeouts
- IP-based access restrictions

See the [Security Configuration Guide](mdc:../configuration/security-config.md) for implementation details.
```

### Tensegrity
- Create bidirectional references between related documents
- Establish clear relationships between documents and code
- Maintain consistent cross-references
- Support content reuse while preserving context

Example:
```markdown
## User Management API

This API provides user management capabilities for the system.

**Implements**: [User Management Requirements](mdc:../requirements/user-management.md)

**Used By**: 
- [Admin Dashboard](mdc:../components/admin-dashboard.md)
- [User Registration Flow](mdc:../flows/user-registration.md)
- [Account Management](mdc:../features/account-management.md)

**Depends On**:
- [Authentication Service](mdc:authentication-service.md)
- [Notification Service](mdc:notification-service.md)
```

### Modularity
- Organize documentation into logical, self-contained sections
- Create clear boundaries between document types
- Design documentation to be consumed independently
- Support composition of documentation from modules

Example:
```markdown
# Authentication Service

This document is part of the Authentication Module documentation:

1. [Authentication Overview](mdc:auth-overview.md) - Concepts and architecture
2. [Authentication Service](mdc:auth-service.md) - This document
3. [Token Management](mdc:token-management.md) - Token handling details
4. [MFA Implementation](mdc:mfa-implementation.md) - Multi-factor authentication
5. [Authentication Configuration](mdc:auth-configuration.md) - Configuration guide

Each document can be read independently, but they form a complete understanding of the authentication system when read together.
```

### Coherence
- Use consistent terminology throughout documentation
- Apply standard document structures
- Follow established naming conventions
- Maintain consistent formatting and style

Example:
```markdown
## API Conventions

All APIs in the system follow these conventions:

- RESTful design with resource-based URLs
- JSON request and response bodies
- OAuth2 authentication with JWT tokens
- Standard error format with error codes
- Pagination using limit/offset parameters
- Versioning through URL path (/v1/, /v2/)

For details, see the [API Standards Guide](mdc:../standards/api-standards.md).
```

### Clarity
- Provide concrete examples for all concepts
- Use visuals to clarify complex ideas
- Structure content for easy comprehension
- Define terminology explicitly

Example:
```markdown
## Query Language

The search API supports a simple query language for advanced searches.

### Syntax

Queries use a simple syntax with operators and field specifiers:

```
field:value AND (other:value OR another:value)
```

### Examples

**Basic field search**:
```
status:active
```
Finds items where the status field equals "active"

**Combined search**:
```
status:active AND created:>2023-01-01
```
Finds active items created after January 1, 2023

**Complex filtering**:
```
status:(active OR pending) AND NOT assigned:null
```
Finds items with status either active or pending that have an assigned value

### Operator Reference

| Operator | Description | Example |
|----------|-------------|---------|
| AND | Logical AND | status:active AND priority:high |
| OR | Logical OR | status:active OR status:pending |
| NOT | Logical NOT | NOT status:inactive |
| : | Field specifier | field:value |
| > | Greater than | created:>2023-01-01 |
| < | Less than | priority:<3 |
```

### Adaptivity
- Design documentation for different audience needs
- Provide context-specific guidance
- Allow for appropriate levels of detail
- Support different consumption patterns

Example:
```markdown
# Authentication Guide

This guide is available in multiple formats for different audiences:

- [Developer Guide](mdc:auth-developer.md) - Technical implementation details
- [Administrator Guide](mdc:auth-admin.md) - Configuration and management
- [User Guide](mdc:auth-user.md) - End-user instructions
- [Security Guide](mdc:auth-security.md) - Security implications and best practices

The content is adapted to each audience while maintaining consistent information.

## Context-Specific Configuration

Authentication can be configured differently based on environment:

| Environment | Configuration Approach | Document Reference |
|-------------|------------------------|---------------------|
| Development | Simplified auth for rapid iteration | [Dev Config](mdc:auth-dev-config.md) |
| Testing | Mock authentication services | [Test Config](mdc:auth-test-config.md) |
| Production | Full security with all protections | [Prod Config](mdc:auth-prod-config.md) |
```

## Documentation Validation Checklist

Before finalizing documentation, verify that:

- [ ] The purpose of the document is clear
- [ ] The intended audience is identified
- [ ] The document follows a logical structure
- [ ] Content is technically accurate and current
- [ ] Examples are provided for complex concepts
- [ ] References to other documents are valid
- [ ] Metadata is complete and accurate
- [ ] The document follows established patterns
- [ ] Language is clear and appropriate for the audience
- [ ] Meta-systemic principles are properly applied

<important>
Documentation is essential for maintaining system knowledge and enabling effective use of the system. Apply these patterns consistently to create clear, comprehensive, and maintainable documentation that effectively serves its intended purpose.
</important>