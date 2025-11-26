from behave import when, then
from domain.models import SpinResult

@when("the player makes a bonus spin with bet {bet}")
def step_bonus_spin(context, bet):
    context.last_spin = context.controller.make_bonus_spin(
        context.player.id,
        float(bet)
    )

@then('the player real balance should not be lower than "{key}"')
def step_balance_not_lower(context, key):
    refreshed = context.controller.get_player(context.player.id)
    before = context.memory[key]
    after = refreshed.balance

    assert after >= before, \
        f"Expected balance >= {before}, got {after}"
