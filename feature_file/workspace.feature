Feature: Test Workspace
  Scenario: User creates workspace
    Given  User login with login credentials email "test@mailinator.com" and password "123456"
    When User creates a project "Demo"
    And User create an workspace "MyWorkspace" in project "Demo"
    Then User verifies workspace "MyWorkspace" created or not in project "Demo"
