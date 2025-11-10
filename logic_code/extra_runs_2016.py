"""Analyze and plot the total extra runs conceded by each team in the 2016 IPL season."""

import csv
import matplotlib.pyplot as plt

# Constants for column names
MATCH_ID = "id"
SEASON = "season"
BOWLING_TEAM = "bowling_team"
EXTRA_RUNS = "extra_runs"


def calculate(matches_file, deliveries_file):
    """Calculate total extra runs conceded per team in the 2016 season.

    Args:
        matches_file (str): Path to the matches CSV file.
        deliveries_file (str): Path to the deliveries CSV file.

    Returns:
        dict: A dictionary mapping each bowling team to total extra runs conceded in 2016.
    """
    # Step 1: Find all match IDs for season 2016
    match_ids_2016 = set()
    with open(matches_file, "r", encoding="utf-8") as file:
        matches_reader = csv.DictReader(file)
        for match in matches_reader:
            if int(match[SEASON]) == 2016:
                match_ids_2016.add(match[MATCH_ID])

    # Step 2: Calculate total extra runs per team
    extra_runs_per_team = {}
    with open(deliveries_file, "r", encoding="utf-8") as file:
        deliveries_reader = csv.DictReader(file)
        for delivery in deliveries_reader:
            if delivery["match_id"] in match_ids_2016:
                team = delivery[BOWLING_TEAM].strip()
                extra = int(delivery[EXTRA_RUNS])
                extra_runs_per_team[team] = extra_runs_per_team.get(team, 0) + extra

    return extra_runs_per_team


def plot(data):
    """Plot a bar chart of extra runs conceded by each team.

    Args:
        data (dict): Mapping of teams to total extra runs.
    """
    teams = list(data.keys())
    extras = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(teams, extras, color="orange", edgecolor="black")
    plt.title("Extra Runs Conceded Per Team (2016)")
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("extra-runs-2016-plot.png")
    plt.close()  # close the plot to prevent resource locking


def execute(matches_file, deliveries_file):
    """Execute the full analysis and generate a plot."""
    data = calculate(matches_file, deliveries_file)
    plot(data)


if __name__ == "__main__":
    execute("../data/mock_matches.csv", "../data/mock_deliveries.csv")


