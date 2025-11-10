import unittest
import csv
from logic_code import extra_runs_2016

class TestExtraRuns2016(unittest.TestCase):

    def setUp(self):
        with open("mock_matches.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "season"])
            writer.writerow(["1", "2016"])
            writer.writerow(["2", "2015"])

        with open("mock_deliveries.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["match_id", "bowling_team", "extra_runs"])
            writer.writerow(["1", "Mumbai Indians", "5"])
            writer.writerow(["1", "Mumbai Indians", "2"])
            writer.writerow(["2", "CSK", "10"])

        self.matches = "mock_matches.csv"
        self.deliveries = "mock_deliveries.csv"

    def test_calculate_returns_dict(self):
        result = extra_runs_2016.calculate(self.matches, self.deliveries)

        self.assertIsInstance(result, dict)

        self.assertEqual(result["Mumbai Indians"], 7)

    def test_execute_runs(self):
        extra_runs_2016.execute(self.matches, self.deliveries)


if __name__ == "__main__":
    unittest.main()


