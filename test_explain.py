import json
import subprocess
import sys
import unittest

from drain_planner import explain


class DrainEvidenceTest(unittest.TestCase):
    def test_reports_both_hold_reasons(self):
        result = explain({"node": "node-x", "available_replicas": "2",
                          "min_available": "2", "has_critical_pod": "yes"})
        self.assertEqual(result["decision"], "hold")
        self.assertEqual(result["reasons"], [
            "replicas_at_or_below_minimum", "critical_pod_present"
        ])

    def test_json_cli_exposes_reason_and_keeps_text_mode(self):
        command = [sys.executable, "drain_planner.py", "sample_nodes.csv"]
        self.assertEqual(subprocess.check_output(command, text=True).splitlines(),
                         ["node-a drain", "node-b hold"])
        result = json.loads(subprocess.check_output(command + ["--json"], text=True))
        self.assertEqual(result[0]["reasons"], [])
        self.assertEqual(result[1]["reasons"], ["replicas_at_or_below_minimum"])
