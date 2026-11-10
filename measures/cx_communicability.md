---
title: "Communicability"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Communicability

Family: Centrality. Identifier: `cx_communicability`.

## Definition

Communicability of every pair of nodes: the matrix exponential of the adjacency matrix, per component (Estrada and Hatano 2008).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `communicability; communicability_exp; subgraph_centrality; subgraph_centrality_exp` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `subgraph_centrality` | API listing |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `subgraph_centrality` | API listing |
| [netrankr](../tools/netrankr.html) | ≠ checked, differs by convention | `indirect_relations` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_communicability` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-10, rel 1e-09 | `nx.communicability(G)` | NetworkX's communicability is not implemented for multigraphs. |
| `cx_communicability` | netrankr | undirected | differs | loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 1e-10, rel 1e-09 | `indirect_relations(g, 'walks', FUN = walks_exp)` | netrankr reads the simple graph (parallel edges collapsed, loops dropped); the reference value's adjacency matrix counts them. netrankr has no value for a single node. |

## References

[estrada2008communicability](../references.html#estrada2008communicability), [estrada2009communicability](../references.html#estrada2009communicability)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex), [schoch2018centrality](../references.html#schoch2018centrality)
{% endraw %}
