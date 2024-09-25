import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the home of Football stats." in response.data

def test_get_all_players(client):
    response = client.get('/api/players?season=2023')
    assert response.status_code == 200
    assert isinstance(response.json, dict)  # Check if response is a dictionary

def test_get_player_details(client):
    player_id = '1'  # Replace with a valid player ID
    response = client.get(f'/api/players/{player_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_add_player(client):
    player_data = {
        'name': 'John Doe',
        'team': 'Team A',
        'goals': 10,
        'assists': 5
    }
    response = client.post('/api/players', data=json.dumps(player_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == "Player added successfully"

def test_update_player(client):
    player_id = '1'  # Replace with a valid player ID
    updated_data = {
        'name': 'Jane Doe',
        'team': 'Team B',
        'goals': 12,
        'assists': 7
    }
    response = client.put(f'/api/players/{player_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == f"Player {player_id} updated successfully"

def test_delete_player(client):
    player_id = '1'  # Replace with a valid player ID
    response = client.delete(f'/api/players/{player_id}')
    assert response.status_code == 200
    assert response.json['message'] == f"Player {player_id} deleted successfully"

def test_get_all_teams(client):
    response = client.get('/api/teams?season=2023')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_get_team_details(client):
    team_id = '1'  # Replace with a valid team ID
    response = client.get(f'/api/teams/{team_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_add_team(client):
    team_data = {
        'name': 'Team A',
        'wins': 10,
        'losses': 5
    }
    response = client.post('/api/teams', data=json.dumps(team_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == "Team added successfully"

def test_update_team(client):
    team_id = '1'  # Replace with a valid team ID
    updated_data = {
        'name': 'Team B',
        'wins': 12,
        'losses': 3
    }
    response = client.put(f'/api/teams/{team_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == f"Team {team_id} updated successfully"

def test_delete_team(client):
    team_id = '1'  # Replace with a valid team ID
    response = client.delete(f'/api/teams/{team_id}')
    assert response.status_code == 200
    assert response.json['message'] == f"Team {team_id} deleted successfully"

def test_get_all_matches(client):
    response = client.get('/api/matches?season=2023')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_get_match_details(client):
    match_id = '1'  # Replace with a valid match ID
    response = client.get(f'/api/matches/{match_id}')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_add_match(client):
    match_data = {
        'home_team': 'Team A',
        'away_team': 'Team B',
        'home_score': 2,
        'away_score': 1
    }
    response = client.post('/api/matches', data=json.dumps(match_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == "Match added successfully"

def test_update_match(client):
    match_id = '1'  # Replace with a valid match ID
    updated_data = {
        'home_team': 'Team C',
        'away_team': 'Team D',
        'home_score': 3,
        'away_score': 2
    }
    response = client.put(f'/api/matches/{match_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == f"Match {match_id} updated successfully"

def test_delete_match(client):
    match_id = '1'  # Replace with a valid match ID
    response = client.delete(f'/api/matches/{match_id}')
    assert response.status_code == 200
    assert response.json['message'] == f"Match {match_id} deleted successfully"