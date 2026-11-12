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
