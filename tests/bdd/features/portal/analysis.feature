@portal @analysis
Feature: Portal Analysis and Troubleshooting
  As a Space Designer
  I want to analyze portal properties and troubleshoot issues
  So that I can ensure consistency and fix problems

  Background:
    Given I have a valid Gather.town API key
    And I have a valid Gather.town space ID
    And my space has at least one map with portals

  # Properties analysis
  @REQ-2.1 @properties
  Scenario: Analyzing portal properties across all maps
    When I run the command "gather-manager explore --analyze-properties"
    Then I should see a property frequency analysis
    And I should see the percentage of portals with each property
    And I should see which properties appear to be directional
    And the results should be saved to a file

  @REQ-2.2 @properties @specific-map
  Scenario: Analyzing portal properties in a specific map
    Given I know the ID of a map in my space
    When I run the command "gather-manager explore --map-id <map_id> --analyze-properties"
    Then I should see a property frequency analysis for that map
    And I should see the percentage of portals with each property
    And I should see which properties appear to be directional
    And the results should be saved to a file

  # Configuration analysis
  @REQ-2.3 @configuration @unusual
  Scenario: Identifying unusual portal configurations
    When I run the command "gather-manager explore --analyze-properties"
    Then I should see properties that are present in less than 50% of portals
    And I should be able to identify portals with unusual configurations

  @REQ-2.4 @configuration @consistency
  Scenario: Analyzing portal property consistency
    When I run the command "gather-manager explore --analyze-properties"
    Then I should see which properties have consistent values
    And I should see which properties have variable values
    And I should be able to identify inconsistencies in portal configurations

  # Connection validation
  @REQ-2.5 @validation @connections
  Scenario: Validating portals across maps
    When I run the portal validation command
    Then I should see a list of valid and invalid portals
    And each portal should show its validation status
    And invalid portals should show the reason for invalidity

  @REQ-2.6 @validation @one-way
  Scenario: Identifying one-way portals
    When I run the command "gather-manager validate-portals --check-bidirectional"
    Then I should see a list of portal pairs where one direction is missing
    And I should see the source and target maps for each one-way portal
    And I should see suggestions for creating the missing portals

  # Portal export
  @REQ-2.7 @export @json
  Scenario: Exporting portal data to JSON
    When I run the portal export command with format "json"
    Then the portal data should be exported to a JSON file
    And the exported data should contain all portal information

  @REQ-2.8 @export @csv
  Scenario: Exporting portal data to CSV
    When I run the portal export command with format "csv"
    Then the portal data should be exported to a CSV file
    And the exported data should contain all portal information

  # Problem resolution
  @REQ-2.9 @troubleshooting @fix
  Scenario: Fixing portal issues automatically
    When I run the command "gather-manager fix-portals"
    Then I should see a list of issues that were fixed
    And I should see a list of issues that require manual intervention
    And the changes should be applied to my space

  @REQ-2.10 @troubleshooting @report
  Scenario: Generating a portal health report
    When I run the command "gather-manager validate-portals --report"
    Then I should see a summary of portal health across my space
    And I should see statistics on portal issues by type
    And I should see a list of maps with the most issues
    And the report should be saved to a file
