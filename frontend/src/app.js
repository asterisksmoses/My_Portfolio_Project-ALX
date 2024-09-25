const playerList = document.getElementById('player-list');
const teamList = document.getElementById('team-list');
const matchList = document.getElementById('match-list');

// Function to show loading state
function showLoading() {
    const loadingDiv = document.createElement('div');
    loadingDiv.classList.add('loading');
    loadingDiv.textContent = 'Loading...';
    document.body.appendChild(loadingDiv);
}

// Function to hide loading state
function hideLoading() {
    const loadingDiv = document.querySelector('.loading');
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

// Function to display errors
function displayError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.classList.add('error');
    errorDiv.textContent = message;
    document.body.appendChild(errorDiv);
}

// Function to fetch and display players
async function fetchPlayers() {
    try {
        showLoading();
        const response = await fetch('/api/players');
        const data = await response.json();
        hideLoading();
        displayPlayers(data);
    } catch (error) {
        hideLoading();
        console.error('Error fetching players:', error);
        displayError('Failed to load player data.');
    }
}

function displayPlayers(players) {
    playerList.innerHTML = '';
    if (players.length === 0) {
        playerList.textContent = 'No players found.';
        return;
    }
    players.forEach(player => {
        const playerCard = document.createElement('div');
        playerCard.classList.add('card');
        playerCard.innerHTML = `
            <h3>${player.name}</h3>
            <p>Team: ${player.team}</p>
            <p>Goals: ${player.goals}</p>
            <p>Assists: ${player.assists}</p>
        `;
        playerList.appendChild(playerCard);
    });
}

// Fetch and display teams
async function fetchTeams() {
    try {
        showLoading();
        const response = await fetch('/api/teams');
        const data = await response.json();
        hideLoading();
        displayTeams(data);
    } catch (error) {
        hideLoading();
        console.error('Error fetching teams:', error);
        displayError('Failed to load team data.');
    }
}

function displayTeams(teams) {
    teamList.innerHTML = '';
    if (teams.length === 0) {
        teamList.textContent = 'No teams found.';
        return;
    }
    teams.forEach(team => {
        const teamCard = document.createElement('div');
        teamCard.classList.add('card');
        teamCard.innerHTML = `
            <h3>${team.name}</h3>
            <p>Wins: ${team.wins}</p>
            <p>Losses: ${team.losses}</p>
        `;
        teamList.appendChild(teamCard);
    });
}

// Fetch matches
async function fetchMatches() {
    try {
        showLoading();
        const response = await fetch('/api/matches');
        const data = await response.json();
        hideLoading();
        displayMatches(data);
    } catch (error) {
        hideLoading();
        console.error('Error fetching matches:', error);
        displayError('Failed to load match data.');
    }
}

function displayMatches(matches) {
    matchList.innerHTML = '';
    if (matches.length === 0) {
        matchList.textContent = 'No matches found.';
        return;
    }
    matches.forEach(match => {
        const matchCard = document.createElement('div');
        matchCard.classList.add('card');
        matchCard.innerHTML = `
            <h3>${match.homeTeam} vs ${match.awayTeam}</h3>
            <p>Score: ${match.homeScore} - ${match.awayScore}</p>
        `;
        matchList.appendChild(matchCard);
    });
}

// Call the functions to fetch and display data
fetchPlayers();
fetchTeams();
fetchMatches();