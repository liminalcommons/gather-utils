Feature: Portal Explorer Service
  As a developer
  I want to analyze portal structures across multiple maps
  So that I can understand the connections and navigation paths in a Gather.town space

  Background:
    Given I have a valid Gather.town API key
    And I have access to a Gather.town space with multiple maps and portals

  @REQ-2.1
  Scenario: Create PortalExplorer Class
    Given I need to analyze portal structures
    When I create a PortalExplorer class
    Then it should initialize with a client and output directory
    And it should have the basic structure for portal analysis

  @REQ-2.2
  Scenario: Analyze Portals in a Single Map
    Given I have a PortalExplorer instance
    When I call the analyze_map_portals method for a specific map
    Then it should extract all portals from the map
    And it should analyze the portal data
    And it should return structured portal information

  @REQ-2.3
  Scenario: Analyze Portals Across Multiple Maps
    Given I have a PortalExplorer instance
    When I call the analyze_all_maps method
    Then it should process all maps in the space
    And it should aggregate portal data across maps
    And it should return comprehensive portal information for the entire space

  @REQ-2.4
  Scenario: Analyze Portal Connections Between Maps
    Given I have portal data from multiple maps
    When I analyze the portal connections
    Then it should identify bidirectional portals
    And it should create a connection graph between maps
    And it should detect orphaned or one-way portals

  @REQ-2.5
  Scenario: Generate Structured Output for Analysis Results
    Given I have completed portal analysis
    When I save the results to JSON
    Then the output should have a structured format
    And it should include all portal information
    And it should be saved to the specified output directory 