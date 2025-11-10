import unittest
from logic_code.ipl_analysis import load, calculate, execute


class TestTotalMatchesPerYear(unittest.TestCase):
    """Unit tests for total matches per year analysis."""

    def setUp(self):
        self.path = 'data/mock_matches.csv'

    def test_load_returns_list(self):
        data = load(self.path)
        self.assertIsInstance(data, list)
        self.assertTrue(all('season' in match for match in data))

    def test_calculate_returns_dict(self):
        data = load(self.path)
        result = calculate(data)
        self.assertIsInstance(result, dict)

    def test_execute_runs(self):
        """Ensure execute() runs without throwing exceptions."""
        try:
            execute(self.path)
        except Exception as e:
            self.fail(f"Execute raised {e}")

