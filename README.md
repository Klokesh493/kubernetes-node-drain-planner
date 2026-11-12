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

## Business problem

A planned node drain can reduce replica availability or disrupt a critical workload. Operators need to see the blockers before scheduling maintenance.

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

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 drain_planner.py sample_nodes.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
