Feature: Login functionality

  Scenario: Login to system  
    Given I visit login page
    When I enter user in the account field
    And I enter 123456 in the password field
    And I press the login button
    Then I should see the hello