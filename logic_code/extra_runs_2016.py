import csv
import matplotlib.pyplot as plt

MATCH_ID = 'id'
SEASON = 'season'
BOWLING_TEAM = 'bowling_team'
EXTRA_RUNS = 'extra_runs'

def calculate(matches_file, deliveries_file):
    # Step 1: Find all match IDs for season 2016
    match_ids_2016 = set()
    with open(matches_file, 'r', encoding='utf-8') as f:
        matches_reader = csv.DictReader(f)
        for match in matches_reader:
            if int(match[SEASON]) == 2016:
                match_ids_2016.add(match[MATCH_ID])

    # Step 2: Calculate total extra runs conceded per team
    extra_runs_per_team = {}
    with open(deliveries_file, 'r', encoding='utf-8') as f:
        deliveries_reader = csv.DictReader(f)
        for delivery in deliveries_reader:
            if delivery['match_id'] in match_ids_2016:
                team = delivery[BOWLING_TEAM].strip()
                extra = int(delivery[EXTRA_RUNS])
                extra_runs_per_team[team] = extra_runs_per_team.get(team, 0) + extra

    return extra_runs_per_team


def plot(data):
    teams = list(data.keys())
    extras = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(teams, extras, color='orange', edgecolor='black')
    plt.title('Extra Runs Conceded Per Team (2016)')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('extra-runs-2016-plot.png')
    plt.close()  # close to prevent blocking


def execute(matches_file, deliveries_file):
    data = calculate(matches_file, deliveries_file)
    plot(data)


if __name__ == "__main__":
    matches_path = '../data/mock_matches.csv'
    deliveries_path = '../data/mock_deliveries.csv'
    execute(matches_path, deliveries_path)

