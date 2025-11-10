"""Unit tests for extra_runs_2016 module."""

import unittest
import csv
from logic_code import extra_runs_2016


class TestExtraRuns2016(unittest.TestCase):
    """Tests the calculation and execution functions in extra_runs_2016."""

    def setUp(self):
        """Set up mock CSV data for testing."""
        with open("mock_matches.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "season"])
            writer.writerow(["1", "2016"])
            writer.writerow(["2", "2015"])

        with open("mock_deliveries.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["match_id", "bowling_team", "extra_runs"])
            writer.writerow(["1", "Mumbai Indians", "5"])
            writer.writerow(["1", "Mumbai Indians", "2"])
            writer.writerow(["2", "CSK", "10"])

        self.matches = "mock_matches.csv"
        self.deliveries = "mock_deliveries.csv"

    def test_calculate_returns_dict(self):
        """Check that calculate() returns a dictionary with correct totals."""
        result = extra_runs_2016.calculate(self.matches, self.deliveries)

        # Ensure output type
        self.assertIsInstance(result, dict)

        # Ensure correct calculation for Mumbai Indians (5 + 2 = 7)
        self.assertEqual(result["Mumbai Indians"], 7)

    def test_execute_runs(self):
        """Ensure execute() runs without any exceptions."""
        extra_runs_2016.execute(self.matches, self.deliveries)


if __name__ == "__main__":
    unittest.main()



