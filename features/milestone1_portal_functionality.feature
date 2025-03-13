Feature: Portal Functionality
  As a developer
  I want to extract and analyze portal data from Gather.town spaces
  So that I can understand the connections between maps

  Background:
    Given I have a valid Gather.town API key
    And I have access to a Gather.town space with portals

  @REQ-1.1
  Scenario: Enhanced Object Model for Portals
    Given I have the space data model
    When I update the model to include portal-specific properties
    Then the model should validate portal objects correctly
    And the model should handle all required portal properties

  @REQ-1.2
  Scenario: Extract Portals from a Map
    Given I have a GatherClient instance
    When I call the get_portals method for a specific map
    Then it should return a list of portal objects
    And each portal should have the correct properties
    And portals should be filtered from other object types

  @REQ-1.3
  Scenario: Test Portal Extraction with Real Map Data
    Given I have a test script for portal extraction
    When I run the script against real map data
    Then it should correctly identify all portals
    And it should parse portal properties accurately
    And it should handle different portal configurations

  @REQ-1.4
  Scenario: Unit Tests for Portal Functionality
    Given I have unit tests for the portal object model
    And I have unit tests for portal extraction
    When I run the test suite
    Then all tests should pass
    And the tests should cover edge cases
    And the tests should verify portal property validation 