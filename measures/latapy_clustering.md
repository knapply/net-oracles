---
title: "Latapy clustering"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Latapy clustering

Family: Two-mode and bipartite. Identifier: `latapy_clustering`.

## Definition

Latapy clustering.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `latapy_clustering` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `latapy_clustering_dot` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'dot')` |  |
| `latapy_clustering_max` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'max')` |  |
| `latapy_clustering_min` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.bipartite.latapy_clustering(G, mode = 'min')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
