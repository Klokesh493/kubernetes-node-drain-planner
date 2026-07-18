import unittest

from drain_planner import can_drain


class DrainPlannerTest(unittest.TestCase):
    def test_holds_when_min_available_would_break(self):
        row = {"node": "b", "available_replicas": "2", "min_available": "2", "has_critical_pod": "no"}
        self.assertFalse(can_drain(row))


if __name__ == "__main__":
    unittest.main()
