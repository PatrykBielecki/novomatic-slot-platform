Feature: Player cannot spin with insufficient funds

  Scenario: Spin is rejected when balance is too low
    Given API client is initialized
    And a player with balance lower than 5 exists
    When the player tries to make a cash spin with bet 10
    Then an error about insufficient funds should be raised

  Scenario: Bonus spins until money is spent or max spins reached
    Given API client is initialized
    And Player with id 3 have a balance 100
    When the player makes cash spins until money is spent
    Then the player's balance should be zero or less than the minimum bet after spins