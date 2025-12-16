from behave import when, then
from domain.models import SpinResult
import time

@when("the player makes a bonus spin with bet {bet}")
def step_bonus_spin(context, bet):
    context.last_spin = context.controller.make_bonus_spin(
        context.player.player_id,
        float(bet)
    )

@then('the player real balance should not be lower than "{key}"')
def step_balance_not_lower(context, key):
    refreshed = context.controller.get_player(context.player.player_id)
    before = context.memory[key]
    after = refreshed.balance

    assert after >= before, \
        f"Expected balance >= {before}, got {after}"

# wykonuje spiny dopoki nie wyczerpia sie srodki uzytkownika, ale max do 100 spinów
@when('the player makes cash spins until money is spent')
def step_bonus_spins_until_spend(context):
    max_spins = 100
    spins_played = 0
    bet_amount = 100.0   # ustalamy stały zakład na potrzeby testu

    player = context.controller.get_player(context.player.player_id)
    while player.balance >= bet_amount and spins_played < max_spins:
        context.last_spin = context.controller.make_cash_spin(
            context.player.player_id,
            bet_amount
        )

        time.sleep(0.2)  # Small delay to avoid overwhelming the system

        player = context.controller.get_player(context.player.player_id)
        spins_played += 1
        