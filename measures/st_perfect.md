---
title: "Perfect"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Perfect

Family: Graph theory and combinatorics. Identifier: `st_perfect`.

## Definition

Perfect.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_perfect_graph` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_perfect` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.is_perfect_graph(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
