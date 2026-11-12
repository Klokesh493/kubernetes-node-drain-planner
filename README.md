# Kubernetes Node Drain Planner

Plans safe node drains by checking replicas, pod disruption budgets, and critical workloads.

Focus: Telecom DevOps Kubernetes operations.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 drain_planner.py sample_nodes.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Node replica and critical pod CSV"]
    B["Evaluate replica minimum and critical pod checks"]
    C{"Any blocking reason?"}
    D["Hold with all reason codes"]
    E["Drain recommendation"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

Use `python3 drain_planner.py sample_nodes.csv --json` to see replica counts
and hold reasons alongside each decision.
