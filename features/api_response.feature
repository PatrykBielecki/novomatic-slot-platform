Feature: API Connectivity Check
  In order to ensure the backend is reachable
  As a developer
  I want to verify that API endpoints respond correctly

  Scenario: Verify Users Endpoint
    Given API client is initialized
    When I call GET /users
    Then the response status code should be 200
    And the response should contain a player with id 1

  Scenario: Verify Specific User Endpoint
    Given API client is initialized
    When I call GET /users/1
    Then the response status code should be 200