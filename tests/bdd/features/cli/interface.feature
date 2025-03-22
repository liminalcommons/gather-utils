@cli @interface
Feature: Command Line Interface
  As a Space Administrator
  I want to interact with the Portal Explorer through a command-line interface
  So that I can easily analyze and visualize portal structures

  Background:
    Given I have the Portal Explorer CLI installed
    And I have configured my API key and space ID

  # Basic commands
  @REQ-3.1 @maps
  Scenario: List Maps in a Space
    Given I have access to a Gather.town space
    When I run the command "gather-manager list-maps"
    Then I should display a list of all maps in the space
    And the output should be formatted as a table
    And it should include map IDs and names

  @REQ-3.2 @exploration @specific-map
  Scenario: Explore Portals in a Single Map
    Given I have access to a Gather.town space with portals
    When I run the command "gather-manager explore --map-id <map_id>"
    Then I should see a list of portals in that map
    And I should see details about each portal
    And the results should be saved to a file

  @REQ-3.3 @exploration @all-maps
  Scenario: Explore Portals Across All Maps
    Given I have access to a Gather.town space with multiple maps
    When I run the command "gather-manager explore"
    Then I should see a summary of portals across all maps
    And I should see the total number of portals found
    And the results should be saved to a file

  @REQ-3.4 @properties
  Scenario: Analyze Portal Properties
    Given I have access to a Gather.town space with portals
    When I run the command "gather-manager explore --analyze-properties"
    Then I should see a property frequency analysis
    And I should see the percentage of portals with each property
    And I should see which properties appear to be directional

  # UI/UX
  @REQ-3.5 @formatting
  Scenario: Rich Output Formatting
    Given I am using the Portal Explorer CLI
    When I run any command
    Then the output should be formatted with rich tables and styling
    And long-running operations should show progress indicators
    And the information should be presented in a user-friendly way

  # Error handling
  @REQ-3.6 @error-handling
  Scenario: Handle API Errors Gracefully
    Given I have incorrect API credentials
    When I run any command that requires API access
    Then I should see a user-friendly error message
    And I should receive guidance on how to fix the issue
    And the program should exit gracefully

  # Help and documentation
  @REQ-3.7 @help
  Scenario: CLI Help Information
    Given I have installed the package
    When I run the command "gather-manager" without arguments
    Then I should see help information
    And all available commands should be listed
    And the CLI should be accessible as a system command
