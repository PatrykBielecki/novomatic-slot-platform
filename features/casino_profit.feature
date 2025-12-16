Feature: Check Casino Profit after spins
    In order to ensure casino profitability
    As a casino operator
    I want to verify that the casino profit is calculated correctly after multiple spins
    
    Scenario: Verify casino profit after cash spin
        Given API client is initialized
        And a player with balance at least 1000 exists
        When the player makes 10 cash spins with bet 10 each
        Then the total casino profit should be calculated correctly