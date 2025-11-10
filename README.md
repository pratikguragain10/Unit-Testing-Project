# IPL Data Analysis (Unit Testing Project)

This project demonstrates the use of **Unit Testing** and **Code Coverage** in Python.

## Steps to Run

1. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run any scripts:
   python3 logic-code/total_matches_per_year.py
   python3 logic-code/stacked_bar_chart.py

4. Run Unit Tests:
   python3 -m unittest discover tests

   - Usage Output:
   test_calculate_returns_dict (test_extra_runs.TestExtraRuns2016.test_calculate_returns_dict) ... ok
   test_execute_runs (test_extra_runs.TestExtraRuns2016.test_execute_runs) ... ok
   test_calculation_returns_dict (test_stacked_chart.TestStackedBarChart.test_calculation_returns_dict) ... ok
   test_execute_runs (test_stacked_chart.TestStackedBarChart.test_execute_runs) ... ok
   test_calculate_returns_dict (test_total_matches.TestTotalMatchesPerYear.test_calculate_returns_dict) ... ok
   test_execute_runs (test_total_matches.TestTotalMatchesPerYear.test_execute_runs)
   Ensure execute() runs without throwing exceptions. ... ok
   test_load_returns_list (test_total_matches.TestTotalMatchesPerYear.test_load_returns_list) ... ok
   Ran 7 tests in 10.602s
   OK

5. Measure Coverage:
   coverage run -m unittest discover tests
   coverage report -m

   - Usage Output:
   overage report -m
   .........
   Ran 9 tests in 3.905s
   OK
