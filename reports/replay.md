# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
node-a drain
node-b hold
````

## Hold evidence

Result: **PASS**

````text
[
  {
    "node": "node-a",
    "decision": "drain",
    "reasons": [],
    "available_replicas": 5,
    "min_available": 3
  },
  {
    "node": "node-b",
    "decision": "hold",
    "reasons": [
      "replicas_at_or_below_minimum"
    ],
    "available_replicas": 2,
    "min_available": 2
  }
]
````
