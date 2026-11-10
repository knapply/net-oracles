---
title: "Fill"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Fill

Family: Graph theory and combinatorics. Identifier: `st_fill`.

## Definition

Fill.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_fill` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.complete_to_chordal_graph(G): [fill edges, alpha of each node]` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
