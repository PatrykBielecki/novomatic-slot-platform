Feature: Bonus spins do not consume real balance
  In order to use bonus feature
  As a player with bonus spins
  I want to win without reducing my real balance

  Scenario: Player makes a bonus spin
    Given API client is initialized
    And a player with balance at least 100 exists
    And I remember the player balance as "initial_balance"
    When the player makes a bonus spin with bet 10
    Then the spin should be successful
    And the player real balance should not be lower than "initial_balance"

