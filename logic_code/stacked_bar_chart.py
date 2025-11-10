"""Plot a stacked bar chart of matches won by each IPL team per season."""

import csv
import matplotlib.pyplot as plt

# Constants for CSV column names
SEASON = "season"
WINNER = "winner"


def calculation(file_path):
    """Read match data and calculate matches won by each team per season.

    Args:
        file_path (str): Path to the matches CSV file.

    Returns:
        dict: Nested dictionary mapping {season: {team: matches_won}}
    """
    matches_won = {}

    # Read the CSV file
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for match in reader:
            season = int(match[SEASON])
            team = match[WINNER].strip()

            # Skip empty team names
            if not team:
                continue

            # Initialize season dictionary if not present
            if season not in matches_won:
                matches_won[season] = {}

            # Increment the count for that team
            matches_won[season][team] = matches_won[season].get(team, 0) + 1

    return matches_won


def plot(data):
    """Plot a stacked bar chart of matches won per team per season.

    Args:
        data (dict): Nested dictionary {season: {team: matches_won}}
    """
    seasons = sorted(data.keys())

    # Find all unique teams across all seasons
    teams = sorted({team for season_data in data.values() for team in season_data.keys()})

    # Prepare a list of match counts per team per season
    team_counts = {team: [] for team in teams}
    for season in seasons:
        for team in teams:
            team_counts[team].append(data[season].get(team, 0))

    # Build stacked bars
    bottom = [0] * len(seasons)
    plt.figure(figsize=(10, 6))

    for team in teams:
        plt.bar(seasons, team_counts[team], bottom=bottom, label=team)
        bottom = [bottom[i] + team_counts[team][i] for i in range(len(bottom))]

    # Add chart details
    plt.title("Matches Won by IPL Teams per Season")
    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.xticks(seasons, rotation=45, ha="right")
    plt.legend(title="Teams", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("matches-won-by-team-plot.png")
    plt.close()  # close to prevent blocking in tests


def execute(path):
    """Execute the full analysis workflow."""
    data = calculation(path)
    plot(data)


if __name__ == "__main__":
    execute("../data/mock_matches.csv")


