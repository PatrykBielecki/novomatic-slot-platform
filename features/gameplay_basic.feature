Feature: Basic gameplay with cash balance
  In order to play the slot game
  As a player with sufficient balance
  I want my balance to change correctly after a spin

  Scenario: Player makes a cash spin
    Given API client is initialized
    And a player with balance at least 100 exists
    When the player makes a cash spin with bet 10
    Then the spin should be successful
    And the player balance should be updated accordingly
