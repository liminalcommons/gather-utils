# Template for BDD feature files
# Replace placeholders in [BRACKETS] with actual values

@[DOMAIN]-[MODULE]-[NUMBER]
Feature: [Feature Name]
  As a [role/persona]
  I want [capability/action]
  So that [benefit/value]

  Background:
    Given [common precondition 1]
    And [common precondition 2]

  # [Group 1] scenarios
  @REQ-[MODULE]-[NUMBER] @REL-[NUMBER] @[COMPONENT]
  Scenario: [First scenario name]
    Given [specific precondition]
    When [action is performed]
    Then [expected outcome is verified]
    And [additional verification]

  # [Group 2] scenarios
  @REQ-[MODULE]-[NUMBER] @REL-[NUMBER] @[COMPONENT]
  Scenario Outline: [Parameterized scenario name]
    Given [precondition with <parameter>]
    When [action with <parameter> is performed]
    Then [outcome with <parameter> is verified]

    Examples:
      | parameter | expected_result |
      | value1    | result1        |
      | value2    | result2        | 