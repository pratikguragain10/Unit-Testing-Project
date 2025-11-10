import unittest
from logic_code.stacked_bar_chart import calculation, execute

class TestStackedBarChart(unittest.TestCase):
    def setUp(self):
        self.path = "data/mock_matches.csv"

    def test_calculation_returns_dict(self):
        data = calculation(self.path)
        self.assertIsInstance(data, dict)
        self.assertTrue(all(isinstance(v, dict) for v in data.values()))

    def test_execute_runs(self):
        try:
            execute(self.path)
        except Exception as e:
            self.fail(f"Execute raised {e}")

if __name__ == "__main__":
    unittest.main()
