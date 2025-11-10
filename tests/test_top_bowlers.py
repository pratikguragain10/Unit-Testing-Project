import unittest
import csv
from logic_code import top_bowlers_2015

class TestTopBowlers2015(unittest.TestCase):

    def setUp(self):
        # Create simple mock CSVs for matches and deliveries
        with open("mock_matches.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "season"])
            writer.writerow(["1", "2015"])
            writer.writerow(["2", "2014"])

        with open("mock_deliveries.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["match_id", "bowler", "total_runs", "is_super_over"])
            writer.writerow(["1", "Bumrah", "6", "0"])
            writer.writerow(["1", "Bumrah", "0", "0"])
            writer.writerow(["1", "Chahal", "4", "0"])
            writer.writerow(["2", "OldBowler", "100", "0"])

        self.matches = "mock_matches.csv"
        self.deliveries = "mock_deliveries.csv"

    def test_calculate_returns_dict(self):
        result = top_bowlers_2015.calculate(self.matches, self.deliveries)
        self.assertIsInstance(result, dict)
        self.assertIn("Bumrah", result)

    def test_execute_runs(self):
        # Just check if the execute function works without any errors
        top_bowlers_2015.execute(self.matches, self.deliveries)


if __name__ == "__main__":
    unittest.main()


