# Example of a complex feature demonstrating advanced patterns
@PORTAL-COMPLEX-1
Feature: Portal Analysis and Management
  As a Space Administrator
  I want to analyze and manage portals in my space
  So that I can understand and optimize space connectivity

  Background:
    Given I have a valid API key
    And I have a valid space ID
    And I have loaded the test space configuration:
      | setting          | value                |
      | max_portals     | 100                  |
      | default_map     | default-test-map     |
      | portal_template | standard-portal.json |

  # Portal discovery and validation scenarios
  @REQ-PORTAL-1 @REL-2 @PORTAL @DISCOVERY
  Scenario: Discover and validate all portals in a map
    Given I have a map with the following portals:
      | portal_id | source_x | source_y | target_map    | target_x | target_y |
      | portal1   | 10      | 20      | target-map-1  | 15      | 25      |
      | portal2   | 30      | 40      | target-map-2  | 35      | 45      |
    When I run the portal discovery analysis
    Then the analysis should succeed
    And the following portals should be identified:
      | portal_id | status    | connectivity |
      | portal1   | valid     | bidirectional|
      | portal2   | valid     | bidirectional|
    And a portal map visualization should be generated
    And the portal connectivity report should be created

  # Portal configuration scenarios
  @REQ-PORTAL-2 @REL-2 @PORTAL @CONFIG
  Scenario Outline: Configure portal properties with validation
    Given I have a portal with id "<portal_id>"
    And the portal has the following initial configuration:
      | property     | value     |
      | type        | <type>    |
      | visibility  | <visible> |
    When I update the portal with these properties:
      | property     | new_value    |
      | type        | <new_type>   |
      | visibility  | <new_visible>|
    Then the update should <outcome>
    And the portal properties should be:
      | property    | expected_value |
      | type       | <final_type>   |
      | visibility | <final_visible>|
    And an audit log entry should be created with "<audit_message>"

    Examples:
      | portal_id | type    | visible | new_type | new_visible | outcome | final_type | final_visible | audit_message        |
      | test1     | normal  | true    | special  | true        | succeed | special    | true         | Updated type         |
      | test2     | normal  | true    | normal   | false       | succeed | normal     | false        | Updated visibility   |
      | test3     | special | true    | invalid  | true        | fail    | special    | true         | Invalid portal type  |

  # Complex portal operations
  @REQ-PORTAL-3 @REL-2 @PORTAL @OPERATIONS
  Scenario: Perform complex portal operations with dependencies
    Given I have the following maps with portals:
      | map_id    | portal_count | connected_to  |
      | map-1     | 3           | map-2         |
      | map-2     | 2           | map-3         |
      | map-3     | 4           | map-1         |
    And I have generated a portal dependency graph
    When I analyze the portal network for:
      | analysis_type   | parameters                  |
      | connectivity   | depth=3,bidirectional=true  |
      | optimization   | max_distance=100            |
      | validation     | check_orphans=true          |
    Then the analysis should identify:
      | result_type        | count |
      | circular_paths     | 1     |
      | orphaned_portals   | 0     |
      | optimization_hints | 2     |
    And the following optimizations should be suggested:
      | optimization_type | affected_portals | benefit_score |
      | consolidate      | portal1,portal2  | high          |
      | redistribute     | portal4,portal5  | medium        |
    And a detailed analysis report should be generated
    And the report should include network topology diagrams 