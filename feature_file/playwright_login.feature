Feature: Playwright Login
  Scenario: User Login in IRCTC
    Given User open IRCTC url in browser
    When User click on Login, enter credentials username "Shivam" password "TFT@123"
    And User click on login & booking with otp
    And User confirms to book ticket
    And User click on Signin
    Then User verify