from behave import when, then
from domain.models import SpinResult
import time 

@when("the player makes a cash spin with bet {bet}")
def step_cash_spin(context, bet):
    context.last_spin = context.controller.make_cash_spin(
        context.player.player_id,
        float(bet)
    )

@when("the player makes 10 cash spins with bet 10 each")
def step_multiple_cash_spins(context):
    spins_to_make = 10
    bet_amount = 10.0
    context.spins = []

    for _ in range(spins_to_make):
        spin_result = context.controller.make_cash_spin(
            context.player.player_id,
            bet_amount
        )
        context.spins.append(spin_result)

        time.sleep(0.1)  # Small delay to avoid overwhelming the system

@then("the spin should be successful")
def step_spin_success(context):
    assert isinstance(context.last_spin, SpinResult)

@then("the player balance should be updated accordingly")
def step_balance_updated(context):
    refreshed = context.controller.get_player(context.player.player_id)
    assert refreshed.balance == context.last_spin.balance_after

@then("the player balance is calculated correctly after the spin")
def step_balance_updated_correctly(context):
    refreshed = context.controller.get_player(context.player.player_id)
    bet_amount = context.last_spin.bet_amount
    win_amount = context.last_spin.win_amount  
    expected_balance = context.memory['initial_balance'] - bet_amount + win_amount
    actual_balance = refreshed.balance

    assert actual_balance == expected_balance, f"Expected balance: {expected_balance}, actual balance: {actual_balance}"

@then("the player real balance should not be lower than '{key}'")
def step_balance_not_lower(context, key):
    refreshed = context.controller.get_player(context.player.player_id)
    before = context.memory[key]
    after = refreshed.balance

    assert after >= before, f"Expected balance >= {before}, got {after}"