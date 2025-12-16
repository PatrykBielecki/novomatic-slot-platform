from behave import when, then, step  


@when("I call GET {endpoint}")
def step_call_get_endpoint(context, endpoint):
    client = context.controller.user_repo.client
    context.response = client.get(endpoint)

@then("the response status code should be {status_code}")
def step_check_status_code(context, status_code):
    expected_code = int(status_code)
    actual_code = context.response.status_code
    assert actual_code == expected_code, f"Expected status code {expected_code}, got {actual_code}"

@step("the response should contain a player with id {player_id}")
def step_check_player_in_response(context, player_id):
    data = context.response.json()
    if not isinstance(data, list):
        raise AssertionError(f"Response is not a JSON list. Got: {type(data)}")
    player_ids = [str(player["player_id"]) for player in data]
    assert player_id in player_ids, f"Player ID {player_id} not found in response"