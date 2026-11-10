---
title: "Successor transitivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Successor transitivity

Family: Descriptive statistics. Identifier: `nxo_successor_transitivity`.

## Definition

Successor transitivity.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_successor_transitivity` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.transitivity(nx.DiGraph(G)) (triangles over successors)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
