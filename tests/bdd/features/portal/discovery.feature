@portal @discovery
Feature: Portal Discovery and Structure
  As a Space Administrator
  I want to discover portals and their structure in my Gather.town space
  So that I can understand the connections between different areas

  Background:
    Given I have a valid Gather.town API key
    And I have a valid Gather.town space ID

  # Map listing
  @REQ-1.1 @CLI @listing
  Scenario: Listing all maps in a space
    When I run the command "gather-manager list-maps"
    Then I should see a list of maps in the space
    And each map should have an ID and name
    And the output should be formatted as a table

  # Single map exploration
  @REQ-1.2 @CLI @exploration
  Scenario: Exploring portals in a specific map
    Given I know the ID of a map in my space
    When I run the command "gather-manager explore --map-id <map_id>"
    Then I should see a list of portals in that map
    And I should see details about each portal
    And the results should be saved to a file

  # Multi-map exploration
  @REQ-1.3 @CLI @exploration
  Scenario: Exploring portals across all maps
    When I run the command "gather-manager explore"
    Then I should see a summary of portals across all maps
    And I should see the total number of portals found
    And the results should be saved to a file

  # Output options
  @REQ-1.4 @CLI @output
  Scenario: Specifying a custom output directory
    When I run the command "gather-manager explore --output-dir my_analysis"
    Then the results should be saved to the "my_analysis" directory
    And I should see a confirmation message with the output location

  # Object analysis
  @REQ-1.5 @debugging @analysis
  Scenario: Analyzing object types in a map
    Given I know the ID of a map in my space
    When I run the command "python debug_map_objects.py <map_id>"
    Then I should see a distribution of object types in the map
    And I should see the count and percentage of each object type
    And the results should be saved to a file

  # Portal candidates
  @REQ-1.6 @debugging @identification
  Scenario: Identifying potential portal objects
    Given I know the ID of a map in my space
    When I run the command "python debug_map_objects.py <map_id>"
    Then I should see a list of objects with targetMap properties
    And I should see sample portal candidates
    And I should see common properties among portal candidates

  # Edge cases
  @REQ-1.7 @debugging @edge-case
  Scenario: Handling maps with no portals
    Given I have a map with no portals
    When I run the command "python debug_map_objects.py <map_id>"
    Then I should see a message indicating no portal candidates were found
    And I should still see the distribution of object types
    And the results should be saved to a file

  @REQ-1.8 @debugging @error-handling
  Scenario: Handling API errors during discovery
    Given I have an invalid API key
    When I run the command "python debug_map_objects.py <map_id>"
    Then I should see an error message
    And the program should exit gracefully
