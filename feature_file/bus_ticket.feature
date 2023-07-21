Feature: Test bus booking
  Scenario: User books 2 bus ticket from Delhi to Manali
    Given User open IRCTC website
    When User clicks on buses
    And User select departure from as "Delhi"
    And User select going to "Manali"
    And User select Departure date after 15 days
    And Click on search bus
    And User select first search result
    And User select 2 seats
    And User select departure and arrival time and click on process to book
    And User login as guest user
    And User login with credential "shivam123@gmail.com" mobile number "8743991454"
    And User personal details "8743991454" "Udyog Vihar" "India"
    And User click on checkbox, continue to book
    Then Verify OTP sent