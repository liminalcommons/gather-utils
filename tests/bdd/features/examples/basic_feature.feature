# Example of a basic feature following best practices
@CLI-BASIC-1
Feature: Basic CLI Command Execution
  As a Gather.town space administrator
  I want to run basic CLI commands
  So that I can manage my space efficiently

  Background:
    Given I have a valid API key
    And I have a valid space ID

  # Basic command execution scenarios
  @REQ-CLI-1 @REL-1 @CLI
  Scenario: Execute a simple space info command
    Given I am in the CLI directory
    When I run the command "gather-manager info --space-id {space_id}"
    Then the command should succeed
    And the output should contain space information
    And the space name should be displayed

  # Parameter validation scenarios
  @REQ-CLI-2 @REL-1 @CLI
  Scenario Outline: Validate command parameters
    Given I am in the CLI directory
    When I run the command "gather-manager <command> --<parameter> <value>"
    Then the command should <outcome>
    And the output should contain "<message>"

    Examples:
      | command | parameter | value     | outcome  | message           |
      | info    | space-id | valid-id  | succeed  | Space found      |
      | info    | space-id | invalid   | fail     | Invalid space ID |
      | info    | api-key  | invalid   | fail     | Invalid API key  |

  # Error handling scenarios
  @REQ-CLI-3 @REL-1 @CLI
  Scenario: Handle network errors gracefully
    Given I am in the CLI directory
    And the network connection is down
    When I run the command "gather-manager info --space-id {space_id}"
    Then the command should fail
    And the error message should mention "network connectivity"
    And a detailed error log should be created
