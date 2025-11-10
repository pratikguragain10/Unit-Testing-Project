"""Unit tests for the stacked_bar_chart module."""

import unittest
from logic_code.stacked_bar_chart import calculation, execute


class TestStackedBarChart(unittest.TestCase):
    """Tests the functions in the stacked_bar_chart module."""

    def setUp(self):
        """Set up mock data file path for testing."""
        self.path = "data/mock_matches.csv"

    def test_calculation_returns_dict(self):
        """Check that calculation() returns a properly structured dictionary."""
        data = calculation(self.path)

        # Ensure the result is a dictionary
        self.assertIsInstance(data, dict)

        # Ensure each value inside the dictionary is also a dictionary
        self.assertTrue(all(isinstance(v, dict) for v in data.values()))

    def test_execute_runs(self):
        """Ensure execute() runs successfully without raising exceptions."""
        try:
            execute(self.path)
        except Exception as error:
            self.fail(f"execute() raised an unexpected exception: {error}")


if __name__ == "__main__":
    unittest.main()

