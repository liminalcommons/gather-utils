@portal @discovery
Feature: Portal Discovery
  As a space administrator
  I want to discover all portals in my space
  So that I can understand the connections between maps

  Background:
    Given I have a valid Gather API key
    And I have a valid space ID

  Scenario: List All Portals in Space
    When I request to list all portals
    Then I should receive a list of all portals
    And each portal should have valid properties
      | property    |
      | id         |
      | mapId      |
      | x          |
      | y          |
      | targetMapId|

  Scenario: Find Portals in Specific Map
    Given I have a specific map ID
    When I request to list portals for that map
    Then I should receive only portals from that map
    And the portal list should not be empty

  Scenario: Detect Broken Portal Connections
    Given there are portals in the space
    When I validate portal connections
    Then I should receive a list of broken connections
    And each broken connection should indicate
      | detail           |
      | source portal    |
      | target map      |
      | error type      |
