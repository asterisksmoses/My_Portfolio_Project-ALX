from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return jsonify(message="Welcome to the home of EPL stats.")

@app.route('/api/players', methods=['GET'])
def get_all_players():
    """This function returns a list of EPL players for a selected season."""
    season = request.args.get('season', '2023')
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/players?league=39&season={season}"

    try:
        response = requests.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        })

        response.raise_for_status()
        players_data = response.json()
        return jsonify(players_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500
@app.route('/api/teams', methods=['GET'])
def get_all_teams():
    """This function returns a list of all EPL teams for the selected season."""
    season = request.args.get('season', '2023')
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/teams?league=39&season={season}"

    try:
        response = requests.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        })

        response.raise_for_status()
        teams_data = response.json()
        return jsonify(teams_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/teams/<string:team_id>', methods=['GET'])
def get_team_details(team_id):
    """This function returns detailed information about a specific EPL team."""
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/teams?id={team_id}"

    try:
        response = request.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "v3.football.api-sports.io"
            })
        
        response.raise_for_status()
        team_details = response.json
        return jsonify(team_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches', methods=['GET'])
def get_all_matches():
    """This function returns a list of all EPL matches for the selected season."""
    season = request.args.get('season', '2023')
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season={season}"

    try:
        response = requests.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        })

        response.raise_for_status()
        matches_data = response.json()
        return jsonify(matches_data)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/api/matches/<string:match_id>', methods=['GET'])
def get_match_details(match_id):
    """This function returns detailed information for a specific EPL match."""
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?id={match_id}"

    try:
        response = requests.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        })

        response.raise_for_status()
        match_details = response.json()
        return jsonify(match_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

@app.route('/player/<string:player_id>', methods=['GET'])
def get_player_stats(player_id):
    """This function gets the stats of the EPL players."""
    api_url = f"https://api-football.com/players/{player_id}/stats/"

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
    api_url = f"https://api-football-v1.p.rapidapi.com/v3/players?id={player_id}&season=2023"

    try:
        response = requests.get(api_url, headers={
            'X-RapidAPI-Key': "XxXxXxXxXxXxXxXxXxXxXxXx",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        })
        
        response.raise_for_status()
        player_details = response.json()
        return jsonify(player_details)
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)