from behave import when, then

@when("the player tries to make a cash spin with bet {bet}")
def step_try_cash_spin(context, bet):
    context.error = None
    try:
        context.controller.make_cash_spin(context.player.player_id, float(bet))
    except Exception as e:
        context.error = e

@then("an error about insufficient funds should be raised")
def step_error_insufficient(context):
    assert context.error is not None
    assert "Insufficient funds" in str(context.error)

@then("the player's balance should be zero or less than the minimum bet after spins")
def step_balance_zero_after_spins(context):
    refreshed = context.controller.get_player(context.player.player_id)
    assert refreshed.balance <= 0, f"Expected balance to be zero or less than minimum bet, got {refreshed.balance}"
