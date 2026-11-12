# Kubernetes Node Drain Planner walkthrough

## Business problem

A planned node drain can reduce replica availability or disrupt a critical workload. Operators need to see the blockers before scheduling maintenance.

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

## Explain a hold decision

Run `python3 drain_planner.py sample_nodes.csv --json`. In the bundled
sample, node-b is held because two available replicas equal the minimum of
two. The JSON includes both counts and a stable reason code. A regression
test covers a node with two simultaneous blockers and confirms that the
original text output remains stable.
