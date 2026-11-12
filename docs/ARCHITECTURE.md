# Kubernetes Node Drain Planner architecture

Plans safe node drains by checking replicas, pod disruption budgets, and critical workloads.

```mermaid
flowchart LR
    N0["sample_nodes.csv"]
    N1["drain_planner.py"]
    N2["can drain"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Decision evidence

The evaluator emits the decision, replica counts, and each blocking reason.
The CLI renders the decision as concise text or JSON for a change review.
The planner evaluates an exported snapshot and never drains a live node.
