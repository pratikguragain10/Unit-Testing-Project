import csv
import matplotlib.pyplot as plt

SEASON = 'season'

def load(file_path):
    matches = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for match in reader:
            matches.append({SEASON: int(match[SEASON])})
    return matches


def calculate(matches):
    total_matches = {}
    for match in matches:
        season = match[SEASON]
        total_matches[season] = total_matches.get(season, 0) + 1
    return total_matches


def plot(data):
    seasons = sorted(data.keys())
    matches = [data[s] for s in seasons]

    plt.figure(figsize=(10, 5))
    plt.bar(seasons, matches, color='violet', edgecolor='black')
    plt.title('Total Matches Played Per Season')
    plt.xlabel('Season')
    plt.ylabel('Matches')
    plt.xticks(seasons, rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('total-matches-year-plot.png')
    plt.show()


def execute(path):
    matches = load(path)
    data = calculate(matches)
    plot(data)


if __name__ == "__main__":
    execute('../data/mock_matches.csv')

    
            