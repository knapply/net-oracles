---
title: "Coloring"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Coloring

Family: Graph theory and combinatorics. Identifier: `st_coloring`.

## Definition

Coloring.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_coloring` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `colours per node from greedy_color(G, 'largest_first'), (G, 'largest_first', interchange=True), (G, 'DSATUR'), equitable_color(G, D + 1), equitable_color(G, D + 3) on the simple undirected graph` |  |
| `st_coloring_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's colourings` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
