@API
Feature: API Authentication
  This feature describes the authentication process for the API.
  
  As a API user
  I want to authenticate with the API
  So that I can access protected resources

  Background:
    Given the system is ready for authentication operations

  @API
  @AUTHENTICATION
  @REQ-API-101
  @REL-1
  Scenario: API Authentication - successful login
    Given the authentication system is configured
    When the user performs authentication with valid credentials
    Then the system responds with a valid authentication token

  @API
  @AUTHENTICATION
  @REQ-API-102
  @REL-1
  @PROC-VALIDATION
  Scenario: API Authentication - invalid credentials
    Given the authentication system is configured
    When the user performs authentication with invalid credentials
    Then the system responds with an authentication error

  @API
  @AUTHENTICATION
  @REQ-API-103
  @REL-1
  Scenario Outline: API Authentication - with multiple credential types
    Given the authentication system is configured with <auth_type>
    When the user performs authentication with <credential>
    Then the system responds with <expected>
    
    Examples:
      | auth_type    | credential        | expected            |
      | basic        | valid_basic       | valid_token         |
      | oauth        | valid_oauth       | valid_token         |
      | basic        | invalid_basic     | authentication_error |
      | oauth        | invalid_oauth     | authentication_error | 