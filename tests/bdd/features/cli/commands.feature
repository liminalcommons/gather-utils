Feature: CLI Commands
  As a user
  I want to use intuitive CLI commands
  So that I can manage my Gather.town space effectively

  Background:
    Given the CLI tool is installed
    And I have valid credentials configured

  Scenario: List Available Commands
    When I run "gather-manager --help"
    Then I should see a list of available commands
    And the output should include
      | command    | description               |
      | list      | List portals or maps      |
      | validate  | Validate portal connections|
      | fix       | Fix broken connections    |

  Scenario: Execute Portal Discovery
    When I run "gather-manager list portals"
    Then the command should execute successfully
    And I should see a table of portals
    And each row should contain
      | column     |
      | ID        |
      | Map       |
      | Position  |
      | Target    |

  Scenario: Handle Invalid Commands
    When I run "gather-manager invalid-command"
    Then the command should fail
    And I should see an error message
    And the error should suggest valid commands

  Scenario: Show Command Help
    When I run "gather-manager list --help"
    Then I should see the command usage
    And I should see available options
    And I should see example commands 