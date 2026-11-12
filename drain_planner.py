import argparse
import csv
import json


def explain(row):
    available = int(row["available_replicas"])
    minimum = int(row["min_available"])
    critical = (row["has_critical_pod"] or "").strip().lower()
    if available < 0 or minimum < 0 or critical not in {"yes", "no"}:
        raise ValueError("replica counts must be nonnegative and has_critical_pod must be yes or no")
    reasons = []
    if available <= minimum:
        reasons.append("replicas_at_or_below_minimum")
    if critical == "yes":
        reasons.append("critical_pod_present")
    return {
        "node": row["node"],
        "decision": "hold" if reasons else "drain",
        "reasons": reasons,
        "available_replicas": available,
        "min_available": minimum,
    }


def can_drain(row):
    return explain({**row, "node": row.get("node", "")})["decision"] == "drain"


def main(path, as_json=False):
    with open(path, newline="", encoding="utf-8") as handle:
        plan = [explain(row) for row in csv.DictReader(handle)]
    if as_json:
        print(json.dumps(plan, indent=2))
    else:
        for item in plan:
            print(f"{item['node']} {item['decision']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Review synthetic node drain inputs.")
    parser.add_argument("path")
    parser.add_argument("--json", action="store_true", help="include decision reasons and replica evidence")
    args = parser.parse_args()
    try:
        main(args.path, args.json)
    except (OSError, ValueError, TypeError, KeyError, csv.Error) as error:
        parser.error(str(error))
