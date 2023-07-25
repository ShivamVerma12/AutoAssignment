Feature: Flow Test
  Scenario: User creates a Flow
    Given User login with login credentials email "test@mailinator.com" and password "123456"
    When User creates a project "Project"
    And User creates a empty Dataset "dataset"
    And User clicks on flow
    When User creates a new flow
    And User clicks on new task and choose data task
    And Users click on save changes
    And User clicks on new task and choose custom task
    And User enters command "python3 experimentstop.py"
    And Users click on save changes
    And User link Dataset task output with task input
    And User click on run
    Then User verify status