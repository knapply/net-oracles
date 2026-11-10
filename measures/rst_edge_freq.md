---
title: "Rst edge freq"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Rst edge freq

Family: Traversal, trees and DAGs. Identifier: `rst_edge_freq`.

## Definition

A random spanning tree of a connected undirected network by Wilson's algorithm, as input edge positions.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rst_edge_freq_nx` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = None, seed = k) containing each edge` |  |
| `rst_edge_freq_nx_weighted` | NetworkX | undirected | agrees |  |  | abs 0.06, rel 0 | `fraction of 2000 draws of nx.random_spanning_tree(G, weight = 'weight', seed = k) containing each edge` |  |

## References

[wilson1996generating](../references.html#wilson1996generating)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
