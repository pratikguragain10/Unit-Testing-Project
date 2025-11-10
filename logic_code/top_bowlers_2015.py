"""Analyze IPL 2015 season to find the top economical bowlers."""

import csv
import matplotlib.pyplot as plt

MATCH_ID = 'id'
SEASON = 'season'
BOWLER = 'bowler'
TOTAL_RUNS = 'total_runs'
IS_SUPER_OVER = 'is_super_over'


def calculate(matches_file, deliveries_file):
    """Calculate the economy rate for each bowler in IPL 2015.

    Args:
        matches_file (str): Path to the matches CSV file.
        deliveries_file (str): Path to the deliveries CSV file.

    Returns:
        dict: A dictionary mapping bowlers to their economy rate.
    """
    match_ids_2015 = set()

    # Step 1: Collect all match IDs for season 2015
    with open(matches_file, 'r', encoding='utf-8') as matches:
        reader = csv.DictReader(matches)
        for match in reader:
            if int(match[SEASON]) == 2015:
                match_ids_2015.add(match[MATCH_ID])

    # Step 2: Accumulate total runs and balls per bowler
    runs_by_bowler = {}
    balls_by_bowler = {}

    with open(deliveries_file, 'r', encoding='utf-8') as deliveries:
        reader = csv.DictReader(deliveries)
        for delivery in reader:
            if delivery['match_id'] not in match_ids_2015:
                continue
            if delivery[IS_SUPER_OVER] == '1':
                continue  # Ignore super overs

            bowler = delivery[BOWLER].strip()
            runs = int(delivery[TOTAL_RUNS])

            runs_by_bowler[bowler] = runs_by_bowler.get(bowler, 0) + runs
            balls_by_bowler[bowler] = balls_by_bowler.get(bowler, 0) + 1

    # Step 3: Compute economy rate for each bowler
    economy = {}
    for bowler in runs_by_bowler:
        overs = balls_by_bowler[bowler] / 6
        economy[bowler] = round(runs_by_bowler[bowler] / overs, 2) if overs > 0 else 0

    return economy


def plot(data):
    """Generate and save a bar chart of the top 5 economical bowlers.

    Args:
        data (dict): Mapping of bowlers to their economy rate.
    """
    # Sort by economy rate in ascending order and select top 5
    sorted_bowlers = sorted(data.items(), key=lambda x: x[1])[:5]
    bowlers = [item[0] for item in sorted_bowlers]
    economies = [item[1] for item in sorted_bowlers]

    plt.figure(figsize=(10, 5))
    plt.bar(bowlers, economies, color='teal', edgecolor='black')
    plt.title('Top Economical Bowlers (2015)')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy Rate')
    plt.tight_layout()
    plt.savefig('../plotting-images/top-economical-bowlers-2015.png')
    plt.close()


def execute(matches_file, deliveries_file):
    """Run the full pipeline: calculate and plot top economical bowlers."""
    data = calculate(matches_file, deliveries_file)
    plot(data)


if __name__ == "__main__":
    MATCHES_PATH = '../data/mock_matches.csv'
    DELIVERIES_PATH = '../data/mock_deliveries.csv'
    execute(MATCHES_PATH, DELIVERIES_PATH)


