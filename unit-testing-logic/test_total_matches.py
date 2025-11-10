"""Unit tests for the total matches per year analysis module."""

import unittest
from logic_code.ipl_analysis import load, calculate, execute


class TestTotalMatchesPerYear(unittest.TestCase):
    """Tests for IPL total matches per year logic."""

    def setUp(self):
        """Set up the mock data file path."""
        self.path = "data/mock_matches.csv"

    def test_load_returns_list(self):
        """Ensure load() returns a list of match dictionaries."""
        data = load(self.path)
        self.assertIsInstance(data, list)
        self.assertTrue(all("season" in match for match in data))

    def test_calculate_returns_dict(self):
        """Ensure calculate() returns a dictionary."""
        data = load(self.path)
        result = calculate(data)
        self.assertIsInstance(result, dict)

    def test_execute_runs(self):
        """Ensure execute() runs without raising exceptions."""
        try:
            execute(self.path)
        except Exception as error:
            self.fail(f"execute() raised an unexpected exception: {error}")


if __name__ == "__main__":
    unittest.main()


