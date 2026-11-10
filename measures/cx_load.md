---
title: "Load"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Load

Family: Centrality. Identifier: `cx_load`.

## Definition

Load centrality of every node: flow split equally among predecessors (Goh, Kahng and Kim 2001).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `newman_betweenness_centrality` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `Load` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_load` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False)` |  |
| `cx_load_cutoff` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False, cutoff = 2)` |  |
| `cx_load_normalized` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G)` |  |
| `cx_load_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.load_centrality(G, normalized = False, weight = 'weight')` |  |

## References

[brandes2001faster](../references.html#brandes2001faster), [brandes2007centrality](../references.html#brandes2007centrality), [brandes2008variants](../references.html#brandes2008variants), [goh2001universal](../references.html#goh2001universal), [piraveenan2013percolation](../references.html#piraveenan2013percolation)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
