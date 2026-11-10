---
title: "Directed clustering"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Directed clustering

Family: Descriptive statistics. Identifier: `nxo_directed_clustering`.

## Definition

Directed clustering.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ≠ checked, differs by convention |  |  |
| [bctpy](../tools/bctpy.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_directed_clustering` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.clustering(nx.DiGraph(G))` |  |
| `nxo_directed_clustering` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-14, rel 1e-12 | `nx.clustering(DiGraph, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |
| `nxo_directed_clustering` | bctpy | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `bct.clustering_coef_bd(A binary, no diagonal)` |  |
| `nxo_directed_clustering_weighted` | NetworkX | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-12, rel 1e-10 | `nx.clustering(nx.DiGraph(G), weight = 'weight')` | nx.DiGraph(G) keeps the last of a pair's parallel arcs (and its weight); the reference keeps the first. |
| `nxo_directed_clustering_weighted` | GraphBLAS algorithms | directed | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-12, rel 1e-10 | `nx.clustering(DiGraph, weight = 'weight', backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |
| `nxo_directed_clustering_weighted` | bctpy | directed | agrees |  |  | abs 1e-12, rel 1e-10 | `bct.clustering_coef_wd(W / max(W))` |  |

Tools cited: [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex)
{% endraw %}
