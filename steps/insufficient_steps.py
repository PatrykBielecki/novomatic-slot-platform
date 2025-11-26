from behave import when, then

@when("the player tries to make a cash spin with bet {bet}")
def step_try_cash_spin(context, bet):
    context.error = None
    try:
        context.controller.make_cash_spin(context.player.id, float(bet))
    except Exception as e:
        context.error = e

@then("an error about insufficient funds should be raised")
def step_error_insufficient(context):
    assert context.error is not None
    assert "Insufficient funds" in str(context.error)
