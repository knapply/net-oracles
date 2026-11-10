---
title: "Square clustering"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Square clustering

Family: Descriptive statistics. Identifier: `square_clustering`.

## Definition

Square clustering of every node: the share of possible squares through it that exist.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `square_clustering` |  |
| [GraphBLAS algorithms](../tools/graphblas.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `square_clustering` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.square_clustering(G)` |  |
| `square_clustering` | GraphBLAS algorithms | any | differs | multi\_edges, (no value) directed | direction, multi\_edges, weights | abs 1e-12, rel 1e-12 | `nx.square_clustering(G simple, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. graphblas-algorithms' square\_clustering fails on a DiGraph (KeyError 'degrees+'). |

## References

[hagberg2008exploring](../references.html#hagberg2008exploring), [lind2005cycles](../references.html#lind2005cycles), [zhang2008clustering](../references.html#zhang2008clustering), [zlatic2012networks](../references.html#zlatic2012networks)

Tools cited: [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
