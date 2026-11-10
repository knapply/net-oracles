---
title: "Adjacency matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Adjacency matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `adjacency_matrix`. 1 measure.

## Definition {#concept-definition}

Adjacency matrix. Entries grouped here: Adjacency.

## Adjacency {#gm_adjacency}

Measure id: `gm_adjacency`. Original family: Matrices and spectra.

**Definition.** Adjacency.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `adjacency_graph; adjacency_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `as_adjacency_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `get_adjacency; get_adjacency_sparse` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `adjacency` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `adjacencyMatrix` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `adjacency_matrix; digraph_adjacency_matrix; graph_adjacency_matrix` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_adjacency` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.adjacency_matrix(G, weight = None).toarray()` |  |
| `gm_adjacency_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.adjacency_matrix(G, weight = 'weight').toarray()` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
