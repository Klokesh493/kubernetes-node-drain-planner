# Kubernetes Node Drain Planner walkthrough

## Business problem

Plans safe node drains by checking replicas, pod disruption budgets, and critical workloads.

## Reproduce the workflow

Run `python3 drain_planner.py sample_nodes.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
node-a drain
node-b hold
```

The sample supplies these fields. `node`, `available_replicas`, `min_available`, `has_critical_pod`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
