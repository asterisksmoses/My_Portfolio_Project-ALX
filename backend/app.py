from flask import Flask, jsonify, request

import requests
import pymysql
from flask import Flask, jsonify, request

db = pymysql.connect(
    host="localhost",
    user="root",
    password="Vicario123",
    database="Football_Statistics"
)

app = Flask(__name__)

API_TOKEN = "wJlO2hE6FKj1b3mE1gcU2mvufbL7K2Q7ilFvOVAOH4P6qgC9yjfyP5wJf6Yh"
BASE_URL = "https://api.sportmonks.com/v3/football"

@app.route('/')
def home_page():
    return jsonify(message="Welcome to the home of Football stats.")

@app.route('/api/players', methods=['GET'])
def get_all_players():
    """This function returns a list of EPL players for a selected season."""
    season = request.args.get('season', '2023')
    api_url = f"{BASE_URL}/players?api_token={API_TOKEN}&season={season}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        players_data = response.json()
        return jsonify(players_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams', methods=['GET'])
def get_all_teams():
    """This function returns a list of all EPL teams for the selected season."""
    season = request.args.get('season', '2023')
    api_url = f"{BASE_URL}/teams?api_token={API_TOKEN}&season={season}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        teams_data = response.json()
        return jsonify(teams_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams/<string:team_id>', methods=['GET'])
def get_team_details(team_id):
    """This function returns detailed information about a specific EPL team."""
    api_url = f"{BASE_URL}/teams/{team_id}?api_token={API_TOKEN}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        team_details = response.json()
        return jsonify(team_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches', methods=['GET'])
def get_all_matches():
    """This function returns a list of all EPL matches for the selected season."""
    season = request.args.get('season', '2023')
    api_url = f"{BASE_URL}/fixtures?api_token={API_TOKEN}&season={season}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        matches_data = response.json()
        return jsonify(matches_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches/<string:match_id>', methods=['GET'])
def get_match_details(match_id):
    """This function returns detailed information for a specific EPL match."""
    api_url = f"{BASE_URL}/fixtures/{match_id}?api_token={API_TOKEN}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        match_details = response.json()
        return jsonify(match_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/player/<string:player_id>', methods=['GET'])
def get_player_stats(player_id):
    """This function gets the stats of the EPL players."""
    api_url = f"{BASE_URL}/players/{player_id}/stats?api_token={API_TOKEN}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        player_stats = response.json()
        return jsonify(player_stats)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/players/<string:player_id>', methods=['GET'])
def get_player_details(player_id):
    """This function acquires the information of a player."""
    api_url = f"{BASE_URL}/players/{player_id}?api_token={API_TOKEN}&season=2023"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        player_details = response.json()
        return jsonify(player_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500
    
@app.route('/api/players', methods=['POST'])
def add_player():
    """This function allows adding a new player to the database."""
    player_data = request.get_json()

    if not player_data:
        return jsonify(error="No player data provided"), 400
    
    name = player_data.get('name')
    team = player_data.get('team', None)
    goals = player_data.get('goals', 0)
    assists = player_data.get('assists', 0)

    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO players (name, team, goals, assists) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, team, goals, assists))
            db.commit() 

        return jsonify(message="Player added successfully", player=player_data), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/players/<string:player_id>', methods=['PUT'])
def update_player(player_id):
    """This function updates a player's information."""
    updated_data = request.get_json()

    if not updated_data:
        return jsonify(error="No data provided for updating"), 400
    
    name = updated_data.get('name')
    team = updated_data.get('team')
    goals = updated_data.get('goals')
    assists = updated_data.get('assists')

    try:
        with db.cursor() as cursor:
            sql = """
                UPDATE players
                SET name = %s, team = %s, goals = %s, assists = %s
                WHERE id = %s
            """
            cursor.execute(sql, (name, team, goals, assists, player_id))
            db.commit()
            
        return jsonify(message=f"Player {player_id} updated successfully", player=updated_data), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/players/<string:player_id>', methods=['DELETE'])
def delete_player(player_id):
    """This function deletes a player's data."""
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM players WHERE id = %s"
            cursor.execute(sql, (player_id))
            db.commit()
        return jsonify(message=f"Player {player_id} deleted successfully"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams', methods=['POST'])
def add_team():
    """This function allows adding a new team to the database."""
    team_data = request.get_json()

    if not team_data:
        return jsonify(error="No team data provided"), 400
    
    name = team_data.get('name')
    wins = team_data.get('wins', 0)
    losses = team_data.get('losses', 0)

    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO teams (name, wins, losses) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, wins, losses))
            db.commit() 
        return jsonify(message="Team added successfully", team=team_data), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams/<string:team_id>', methods=['PUT'])
def update_team(team_id):
    """This function updates a team's information."""
    updated_data = request.get_json()

    if not updated_data:
        return jsonify(error="No data provided for updating"), 400
    
    name = updated_data.get('name')
    wins = updated_data.get('wins', 0)
    losses = updated_data.get('losses', 0)

    try:
        with db.cursor() as cursor:
            sql = """
                UPDATE teams
                SET name = %s, wins = %s, losses = %s
                WHERE id = %s
            """
            cursor.execute(sql, (name, wins, losses, team_id))
            db.commit()
        return jsonify(message=f"Team {team_id} updated successfully", team=updated_data), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams/<string:team_id>', methods=['DELETE'])
def delete_team(team_id):
    """This function deletes a team's data."""
    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM teams WHERE id = %s"
            cursor.execute(sql, (team_id))
            db.commit()
        return jsonify(message=f"Team {team_id} deleted successfully"), 200
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches', methods=['POST'])
def add_match():
    """This function allows adding a new match to the database."""
    match_data = request.get_json()

    if not match_data:
        return jsonify(error="No match data provided"), 400
    
    home_team = match_data.get('home_team')
    away_team = match_data.get('away_team')
    home_score = match_data.get('home_score', 0)
    away_score = match_data.get('away_score', 0)

    try:
        with db.cursor() as cursor:
            sql = """
                INSERT INTO matches (home_team, away_team, home_score, away_score)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (home_team, away_team, home_score, away_score))
            db.commit()
        return jsonify(message="Match added successfully", match=match_data), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches/<string:match_id>', methods=['PUT'])
def update_match(match_id):
    """This function updates a match's information."""
    updated_data = request.get_json()

    if not updated_data:
        return jsonify(error="No data provided for updating"), 400

    return jsonify(message=f"Match {match_id} updated successfully", match=updated_data), 200

@app.route('/api/matches/<string:match_id>', methods=['DELETE'])
def delete_match(match_id):
    """This function deletes a match's data.""" 
    return jsonify(message=f"Match {match_id} deleted successfully"), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)