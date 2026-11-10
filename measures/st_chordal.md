---
title: "St chordal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# St chordal

Family: Graph theory and combinatorics. Identifier: `st_chordal`.

## Definition

St chordal.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `chordal_graph_cliques; chordal_graph_treewidth; complete_to_chordal_graph; is_chordal` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `is_chordal` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `chordal_completion; is_chordal` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_chordal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `[nx.is_chordal(G), nx.chordal_graph_treewidth(G)]` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
