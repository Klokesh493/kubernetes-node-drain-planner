# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 drain_planner.py sample_nodes.csv
node-a drain
node-b hold
test_holds_when_min_available_would_break (test_drain_planner.DrainPlannerTest) ... ok
test_json_cli_exposes_reason_and_keeps_text_mode (test_explain.DrainEvidenceTest) ... ok
test_reports_both_hold_reasons (test_explain.DrainEvidenceTest) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.048s

OK
````
