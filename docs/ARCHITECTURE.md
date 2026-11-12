# Kubernetes Node Drain Planner architecture

Plans safe node drains by checking replicas, pod disruption budgets, and critical workloads.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Decision evidence

The evaluator emits the decision, replica counts, and each blocking reason.
The CLI renders the decision as concise text or JSON for a change review.
The planner evaluates an exported snapshot and never drains a live node.
