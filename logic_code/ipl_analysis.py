"""Analyze and plot the total number of IPL matches played per season."""

import csv
import matplotlib.pyplot as plt

# Constant for the column name
SEASON = "season"


def load(file_path):
    """Load match data from a CSV file.

    Args:
        file_path (str): Path to the matches CSV file.

    Returns:
        list[dict]: A list of matches, each containing the season number.
    """
    matches = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for match in reader:
            # Keep only the season information
            matches.append({SEASON: int(match[SEASON])})
    return matches


def calculate(matches):
    """Calculate the total number of matches played per season.

    Args:
        matches (list[dict]): List of match data with season information.

    Returns:
        dict: Mapping of season to number of matches played.
    """
    total_matches = {}
    for match in matches:
        season = match[SEASON]
        total_matches[season] = total_matches.get(season, 0) + 1
    return total_matches


def plot(data):
    """Plot a bar chart showing total matches per season.

    Args:
        data (dict): Mapping of season to total matches.
    """
    seasons = sorted(data.keys())
    matches = [data[season] for season in seasons]

    plt.figure(figsize=(10, 5))
    plt.bar(seasons, matches, color="violet", edgecolor="black")
    plt.title("Total Matches Played Per Season")
    plt.xlabel("Season")
    plt.ylabel("Matches")
    plt.xticks(seasons, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("total-matches-year-plot.png")
    plt.close()  # close to avoid blocking during tests


def execute(file_path):
    """Execute the full workflow: load, calculate, and plot the data."""
    matches = load(file_path)
    data = calculate(matches)
    plot(data)


if __name__ == "__main__":
    execute("../data/mock_matches.csv")


    
            