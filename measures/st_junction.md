---
title: "Junction"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Junction

Family: Graph theory and combinatorics. Identifier: `st_junction`.

## Definition

Junction.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `junction_tree` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_junction` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.junction_tree(G): per node (0 clique / 1 sepset, members), then (-1, i, j) per edge, in NetworkX's order` |  |
| `st_junction_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on nx.junction_tree(G)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
