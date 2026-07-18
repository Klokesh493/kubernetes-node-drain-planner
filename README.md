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
