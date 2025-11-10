import csv
import matplotlib.pyplot as plt

MATCH_ID = 'id'
SEASON = 'season'
BOWLER = 'bowler'
TOTAL_RUNS = 'total_runs'
IS_SUPER_OVER = 'is_super_over'

def calculate(matches_file, deliveries_file):
    # Step 1: Find match IDs for 2015
    match_ids_2015 = set()
    with open(matches_file, 'r', encoding='utf-8') as f:
        matches_reader = csv.DictReader(f)
        for match in matches_reader:
            if int(match[SEASON]) == 2015:
                match_ids_2015.add(match[MATCH_ID])

    # Step 2: Count total runs and balls for each bowler
    runs_by_bowler = {}
    balls_by_bowler = {}

    with open(deliveries_file, 'r', encoding='utf-8') as f:
        deliveries_reader = csv.DictReader(f)
        for delivery in deliveries_reader:
            if delivery['match_id'] not in match_ids_2015:
                continue

            if delivery[IS_SUPER_OVER] == '1':
                continue  # ignore super overs

            bowler = delivery[BOWLER].strip()
            runs = int(delivery[TOTAL_RUNS])

            runs_by_bowler[bowler] = runs_by_bowler.get(bowler, 0) + runs
            balls_by_bowler[bowler] = balls_by_bowler.get(bowler, 0) + 1

    # Step 3: Calculate economy rate
    economy = {}
    for bowler in runs_by_bowler:
        overs = balls_by_bowler[bowler] / 6
        economy[bowler] = round(runs_by_bowler[bowler] / overs, 2) if overs > 0 else 0

    return economy


def plot(data):
    # Sort by economy rate (ascending)
    sorted_bowlers = sorted(data.items(), key=lambda x: x[1])[:5]
    bowlers = [b[0] for b in sorted_bowlers]
    economies = [b[1] for b in sorted_bowlers]

    plt.figure(figsize=(10, 5))
    plt.bar(bowlers, economies, color='teal', edgecolor='black')
    plt.title('Top Economical Bowlers (2015)')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy Rate')
    plt.tight_layout()
    plt.savefig('top-economical-bowlers-2015.png')
    plt.close()


def execute(matches_file, deliveries_file):
    data = calculate(matches_file, deliveries_file)
    plot(data)


if __name__ == "__main__":
    matches_path = '../data/mock_matches.csv'
    deliveries_path = '../data/mock_deliveries.csv'
    execute(matches_path, deliveries_path)

