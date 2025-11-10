import csv
import matplotlib.pyplot as plt

SEASON = 'season'
WINNER = 'winner'

def calculation(file_path):
    matches_won = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for match in reader:
            season = int(match[SEASON])
            team = match[WINNER].strip()
            if not team:
                continue
            if season not in matches_won:
                matches_won[season] = {}
            matches_won[season][team] = matches_won[season].get(team, 0) + 1
    return matches_won


def plot(data):
    seasons = sorted(data.keys())
    teams = sorted({team for season in data.values() for team in season.keys()})
    team_count = {team: [] for team in teams}

    for season in seasons:
        for team in teams:
            team_count[team].append(data[season].get(team, 0))

    bottom = [0] * len(seasons)
    plt.figure(figsize=(10, 6))
    for team in teams:
        plt.bar(seasons, team_count[team], bottom=bottom, label=team)
        bottom = [bottom[i] + team_count[team][i] for i in range(len(bottom))]

    plt.title('Matches Won by IPL Teams per Season')
    plt.xlabel('Seasons')
    plt.ylabel('Matches Won')
    plt.xticks(seasons, rotation=45, ha='right')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('matches-won-by-team-plot.png')
    plt.show()


def execute(path):
    data = calculation(path)
    plot(data)


if __name__ == "__main__":
    execute('../data/mock_matches.csv')

