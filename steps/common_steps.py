from behave import given
from application.controllers import GameController
from tests.helpers import remember

@given("API client is initialized")
def step_init(context):
    if not hasattr(context, "controller") or context.controller is None:
        context.controller = GameController()
    context.memory = {}

@given("a player with balance at least {amount} exists")
def step_player_min(context, amount):
    context.player = context.controller.find_player_with_min_balance(float(amount))

@given("a player with balance lower than {amount} exists")
def step_player_low(context, amount):
    context.player = context.controller.find_player_with_balance_lower_than(float(amount))

@given('I remember the player balance as "{key}"')
def step_remember(context, key):
    remember(context, key, context.player.balance)
