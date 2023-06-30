Feature: Test Experiment
  Scenario: User creates experiment and verifies its status
    Given  User login with login credentials email "test@mailinator.com" and password "123456"
    When User creates a project "MyProject"
    And User uploads a file "experiment.rb" in project "MyProject"
    And User create an experiment "Experiment" in project "MyProject"
    Then User verifies status code of experiment in project "MyProject"
