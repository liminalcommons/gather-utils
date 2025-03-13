Feature: Command Line Interface
  As a user
  I want to interact with the Portal Explorer through a command-line interface
  So that I can easily analyze and visualize portal structures

  Background:
    Given I have the Portal Explorer CLI installed
    And I have configured my API key and space ID

  @REQ-3.1
  Scenario: Set Up CLI Framework
    Given I need a command-line interface for the Portal Explorer
    When I set up the CLI framework with typer
    Then it should have a basic structure
    And it should be ready for implementing commands

  @REQ-3.2
  Scenario: List Maps in a Space
    Given I have access to a Gather.town space
    When I run the command "gather-explorer list-maps"
    Then it should display a list of all maps in the space
    And the output should be formatted with rich tables
    And it should include map IDs and names

  @REQ-3.3
  Scenario: Explore Portals in a Single Map
    Given I have access to a Gather.town space with portals
    When I run the command "gather-explorer explore --map-id <map_id>"
    Then it should analyze portals in the specified map
    And it should display the portal information
    And it should show connections to other maps

  @REQ-3.3.1
  Scenario: Explore Portals Across All Maps
    Given I have access to a Gather.town space with multiple maps
    When I run the command "gather-explorer explore --all-maps"
    Then it should analyze portals across all maps
    And it should display comprehensive portal information
    And it should show the connection graph between maps

  @REQ-3.4
  Scenario: Rich Output Formatting
    Given I am using the Portal Explorer CLI
    When I run any command
    Then the output should be formatted with rich tables and styling
    And long-running operations should show progress indicators
    And the information should be presented in a user-friendly way

  @REQ-3.5
  Scenario: Handle API Errors Gracefully
    Given I have incorrect API credentials
    When I run any command that requires API access
    Then it should display a user-friendly error message
    And it should provide guidance on how to fix the issue
    And it should exit with an appropriate error code

  @REQ-3.6
  Scenario: CLI Entry Point Registration
    Given I have installed the package
    When I run the command "gather-explorer" without arguments
    Then it should display help information
    And all available commands should be listed
    And the CLI should be accessible as a system command 