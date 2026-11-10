---
title: "St tsp"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# St tsp

Family: Graph theory and combinatorics. Identifier: `st_tsp`.

## Definition

St tsp.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `traveling_salesman_problem` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_tsp` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `traveling_salesman_problem(G) (Christofides), (G, method=greedy_tsp), (G, cycle=False), each with its length first; [-1] if G is disconnected or has fewer than two nodes` |  |
| `st_tsp_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's walks` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
