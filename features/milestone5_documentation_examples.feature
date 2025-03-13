Feature: Documentation & Examples
  As a user or developer
  I want comprehensive documentation and examples
  So that I can effectively use and contribute to the Portal Explorer

  Background:
    Given I have the Portal Explorer codebase
    And all features are implemented and tested

  @REQ-5.1
  Scenario: Update README
    Given I need to document the Portal Explorer
    When I update the README.md file
    Then it should include comprehensive installation instructions
    And it should provide basic usage examples
    And it should explain the purpose and features of the tool

  @REQ-5.2
  Scenario: Create Example Scripts
    Given I need to demonstrate the Portal Explorer functionality
    When I implement example scripts
    Then they should demonstrate portal analysis
    And they should include detailed comments explaining the functionality
    And they should be runnable with minimal setup

  @REQ-5.3
  Scenario: Document CLI Usage
    Given I have implemented the CLI
    When I create CLI usage documentation
    Then it should include examples for all commands
    And it should explain all available options
    And it should provide real-world usage scenarios

  @REQ-5.4
  Scenario: Add Code Documentation
    Given I have implemented all components
    When I add code documentation
    Then all classes and methods should have docstrings
    And the codebase should have type hints throughout
    And the documentation should follow a consistent style

  @REQ-5.5
  Scenario: Create User Guide
    Given I need comprehensive user documentation
    When I create a user guide
    Then it should include detailed usage instructions
    And it should have a troubleshooting section
    And it should cover all features of the Portal Explorer

  @REQ-5.6
  Scenario: BDD Documentation Integration
    Given I have BDD scenarios for all features
    When I generate documentation from BDD scenarios
    Then the documentation should be comprehensive
    And it should show test coverage for each requirement
    And it should be accessible to both users and developers 