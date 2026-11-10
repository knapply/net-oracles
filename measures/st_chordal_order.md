---
title: "Chordal order"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Chordal order

Family: Graph theory and combinatorics. Identifier: `st_chordal_order`.

## Definition

Chordal order.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_chordal_order` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.chordal_graph_cliques(nx.complete_to_chordal_graph(G)[0]): each clique sorted, in NetworkX's order` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
