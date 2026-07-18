import csv
import sys


def can_drain(row):
    if int(row["available_replicas"]) <= int(row["min_available"]):
        return False
    if row["has_critical_pod"].lower() == "yes":
        return False
    return True


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['node']} {'drain' if can_drain(row) else 'hold'}")


if __name__ == "__main__":
    main(sys.argv[1])
