@bdd @integration
Feature: BDD Integration
  As a development team
  I want to integrate BDD into our development workflow
  So that we can ensure requirements are met and maintain high-quality code

  Background:
    Given I have a project with BDD features and scenarios
    And I have the necessary BDD tools installed

  # BDD framework
  @REQ-8.1 @framework
  Scenario: Set Up BDD Framework
    Given I need to implement BDD testing
    When I set up the BDD framework
    Then it should have the correct directory structure
    And it should include necessary configuration files
    And it should support both behave and pytest-bdd

  # Step definitions
  @REQ-8.2 @step-definitions
  Scenario: Implement Step Definitions
    Given I have BDD scenarios
    When I implement step definitions for all scenarios
    Then each step should be mapped to a Python function
    And the step definitions should be organized by feature
    And the step definitions should be reusable across scenarios

  # CI integration
  @REQ-8.3 @ci-integration
  Scenario: Integrate BDD with CI Pipeline
    Given I have a CI pipeline
    When I integrate BDD tests into the pipeline
    Then BDD tests should run automatically on each commit
    And test results should be reported in the CI dashboard
    And failed BDD tests should block merges

  # Documentation generation
  @REQ-8.4 @documentation
  Scenario: Generate Documentation from BDD
    Given I have BDD scenarios with step definitions
    When I generate documentation from BDD scenarios
    Then it should create human-readable documentation
    And it should show the relationship between requirements and tests
    And it should include test status for each scenario

  # Coverage tracking
  @REQ-8.5 @coverage
  Scenario: Track BDD Test Coverage
    Given I have BDD scenarios mapped to requirements
    When I run the BDD test coverage report
    Then it should show which requirements are covered by tests
    And it should identify requirements without test coverage
    And it should calculate the overall test coverage percentage

  # Test generation
  @REQ-8.6 @test-generation
  Scenario: Automate BDD Test Generation
    Given I have new requirements in the project plan
    When I use the BDD generator tool
    Then it should create skeleton BDD scenarios for new requirements
    And it should suggest step definitions based on existing ones
    And it should integrate with the existing BDD framework
