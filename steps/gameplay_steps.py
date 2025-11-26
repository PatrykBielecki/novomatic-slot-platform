from behave import when, then
from domain.models import SpinResult

@when("the player makes a cash spin with bet {bet}")
def step_cash_spin(context, bet):
    context.last_spin = context.controller.make_cash_spin(
        context.player.id,
        float(bet)
    )

@then("the spin should be successful")
def step_spin_success(context):
    assert isinstance(context.last_spin, SpinResult)

@then("the player balance should be updated accordingly")
def step_balance_updated(context):
    refreshed = context.controller.get_player(context.player.id)
    assert refreshed.balance == context.last_spin.balance_after
