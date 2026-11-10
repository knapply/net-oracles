---
title: "Triangles"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Triangles

Family: Descriptive statistics. Identifier: `nxo_triangles`.

## Definition

Number of triangles at each node of the simple undirected reading of the network.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `all_triangles; triangles` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `count_triangles; triangles` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `list_triangles` | API listing |
| [ergm (statnet)](../tools/ergm.html) | · reported in docs | `triangle` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `count_triangles` | API listing |
| [GraphBLAS algorithms](../tools/graphblas.html) | ✓ checked, agrees |  |  |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_triangles` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.triangles(nx.Graph(G))` |  |
| `nxo_triangles` | GraphBLAS algorithms | undirected | agrees |  |  | abs 0, rel 0 | `nx.triangles(G simple without loops, backend = 'graphblas')` |  |
| `nxo_triangles_sorted` | Gephi toolkit | undirected | differs |  | multi\_edges, self\_loops | abs 0, rel 0 | `Gephi toolkit 0.11.3: ClusteringCoefficient.getTriangesReuslts() (setDirected(false)), sorted: the array is in an internal node order` | Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). |

## References

[chiba1985arboricity](../references.html#chiba1985arboricity)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [hunter2008ergm](../references.html#hunter2008ergm), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
