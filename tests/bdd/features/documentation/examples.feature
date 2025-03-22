@documentation @examples
Feature: Documentation and Examples
  As a Developer
  I want comprehensive documentation and examples
  So that I can quickly understand and use the Portal Explorer

  Background:
    Given I have installed the Portal Explorer package

  # Core documentation
  @REQ-6.1 @readme
  Scenario: README Documentation
    Given I am viewing the README file
    Then I should see an overview of the project
    And I should see installation instructions
    And I should see basic usage examples
    And I should see information about API key configuration

  @REQ-6.2 @cli-docs
  Scenario: Command Line Interface Documentation
    Given I am viewing the CLI documentation
    Then I should see a list of all available commands
    And I should see examples for each command
    And I should see explanations of command options
    And I should see expected output formats

  @REQ-6.3 @api-docs
  Scenario: API Documentation
    Given I am viewing the API documentation
    Then I should see documentation for all public classes and methods
    And I should see parameter descriptions
    And I should see return value descriptions
    And I should see usage examples for each method

  # Example code
  @REQ-6.4 @example-scripts
  Scenario: Example Scripts
    Given I am viewing the examples directory
    Then I should see example scripts for common use cases
    And each example should be well-commented
    And each example should be runnable with minimal configuration
    And the examples should demonstrate key features of the package

  @REQ-6.5 @notebooks
  Scenario: Jupyter Notebook Examples
    Given I am viewing the notebook examples
    Then I should see interactive examples of portal analysis
    And I should see visualizations of portal connections
    And I should see explanations of the code
    And the notebooks should be runnable with minimal configuration

  # Troubleshooting
  @REQ-6.6 @troubleshooting
  Scenario: Error Handling Documentation
    Given I am viewing the error handling documentation
    Then I should see common error scenarios
    And I should see troubleshooting steps for each error
    And I should see examples of error messages
    And I should see how to resolve API authentication issues

  # API capabilities
  @REQ-6.7 @api-capabilities @space-info
  Scenario: Retrieving space information
    When I use the GatherClient to get space information
    Then I should receive the space details
    And the space details should include the space ID and name

  @REQ-6.8 @api-capabilities @maps-info
  Scenario: Retrieving maps in a space
    When I use the GatherClient to get maps in a space
    Then I should receive a list of maps
    And each map should have an ID and name

  @REQ-6.9 @api-capabilities @objects-info
  Scenario: Retrieving objects in a map
    Given I know the ID of a map in my space
    When I use the GatherClient to get objects in the map
    Then I should receive a list of objects
    And each object should have a type, x, and y coordinates

  @REQ-6.10 @api-capabilities @portals-info
  Scenario: Retrieving portals in a map
    Given I know the ID of a map in my space
    When I use the GatherClient to get portals in the map
    Then I should receive a list of portal objects
    And each portal should have a targetMap, targetX, and targetY
