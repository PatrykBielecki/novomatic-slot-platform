Feature: Player cannot spin with insufficient funds

  Scenario: Spin is rejected when balance is too low
    Given API client is initialized
    And a player with balance lower than 5 exists
    When the player tries to make a cash spin with bet 10
    Then an error about insufficient funds should be raised
