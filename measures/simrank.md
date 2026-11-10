---
title: "Simrank"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Simrank

Family: Graph theory and combinatorics. Identifier: `simrank`.

## Definition

SimRank similarity of every pair of nodes: two nodes are similar when their in-neighbors are (Jeh and Widom 2002).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `simrank_similarity` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `simrank` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.simrank_similarity(G) on the simple Graph or DiGraph, every pair` |  |
| `simrank_converged` | NetworkX | any | agrees |  |  | abs 1e-11, rel 1e-09 | `nx.similarity._simrank_similarity_python(G, tolerance = 1e-13)` |  |
| `simrank_pairwise` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.similarity._simrank_similarity_python(G)` |  |
| `simrank_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.simrank_similarity(M) on the weighted multigraph (to_numpy_array adds the weights of parallel edges)` |  |

## References

[hagberg2008exploring](../references.html#hagberg2008exploring), [jeh2002simrank](../references.html#jeh2002simrank), [zhang2015panther](../references.html#zhang2015panther)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
