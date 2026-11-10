---
title: "Dag reachability"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Dag reachability

Family: Graph theory and combinatorics. Identifier: `nxs_dag_reachability`.

## Definition

Dag reachability.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_dag_reachability` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `(u, v) for v in nx.descendants(DAG, u)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
