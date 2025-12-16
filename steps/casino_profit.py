from behave import then
from domain.game_rules import HOUSE_EDGE

# Sprawdzamy, czy system poprawnie nalicza prowizję (House Edge),
# czyli czy zysk kasyna wynosi dokładnie 10% sumy stawek zakładów

@then("the total casino profit should be calculated correctly")
def step_casino_profit_calculated(context): 
    total_bets = sum(spin.bet_amount for spin in context.spins)
    expected_profit = round(total_bets * HOUSE_EDGE, 2)  # HOUSE_EDGE = 0.10
    rounds_played = context.controller.round_repo.list_rounds_for_player(context.player.player_id)
    actual_total_profit = sum(r.casino_profit for r in rounds_played)
    actual_total_profit = round(actual_total_profit, 2)
    
    assert actual_total_profit == expected_profit, \
        f"Expected casino profit: {expected_profit} with total bets: {total_bets}, actual profit: {actual_total_profit}"