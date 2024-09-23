document.addEventListener("DOMContentLoaded", function () {
    // Fetch players
    fetchPlayers();

    // Fetch teams
    fetchTeams();

    // Fetch matches
    fetchMatches();

    // Search player functionality
    document.getElementById('search-player').addEventListener('keyup', searchPlayer);

    function fetchPlayers() {
        fetch('/api/players?season=2023')
            .then(response => response.json())
            .then(data => {
                displayPlayers(data.response);
            })
            .catch(error => console.error('Error fetching players:', error));
    }

    function fetchTeams() {
        fetch('/api/teams?season=2023')
            .then(response => response.json())
            .then(data => {
                displayTeams(data.response);
            })
            .catch(error => console.error('Error fetching teams:', error));
    }

    function fetchMatches() {
        fetch('/api/matches?season=2023')
            .then(response => response.json())
            .then(data => {
                displayMatches(data.response);
            })
            .catch(error => console.error('Error fetching matches:', error));
    }

    function displayPlayers(players) {
        const playersList = document.getElementById('players-list');
        playersList.innerHTML = '';
        players.forEach(player => {
            const playerCard = `
                <div class="player-card">
                    <h3>${player.player.name}</h3>
                    <p>Team: ${player.statistics[0].team.name}</p>
                    <p>Goals: ${player.statistics[0].goals.total}</p>
                </div>
            `;
            playersList.innerHTML += playerCard;
        });
    }

    function displayTeams(teams) {
        const teamsList = document.getElementById('teams-list');
        teamsList.innerHTML = '';
        teams.forEach(team => {
            const teamCard = `
                <div class="team-card">
                    <h3>${team.team.name}</h3>
                    <img src="${team.team.logo}" alt="${team.team.name}" width="50">
                </div>
            `;
            teamsList.innerHTML += teamCard;
        });
    }

    function displayMatches(matches) {
        const matchesList = document.getElementById('matches-list');
        matchesList.innerHTML = '';
        matches.forEach(match => {
            const matchCard = `
                <div class="match-card">
                    <h3>${match.teams.home.name} vs ${match.teams.away.name}</h3>
                    <p>Date: ${match.fixture.date}</p>
                    <p>Status: ${match.fixture.status.short}</p>
                </div>
            `;
            matchesList.innerHTML += matchCard;
        });
    }

    function searchPlayer() {
        const searchQuery = document.getElementById('search-player').value.toLowerCase();
        const playerCards = document.querySelectorAll('.player-card');
        playerCards.forEach(card => {
            const playerName = card.querySelector('h3').textContent.toLowerCase();
            if (playerName.includes(searchQuery)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }
});