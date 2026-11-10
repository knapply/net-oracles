---
title: "Bipartite color"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bipartite color

Family: Two-mode and bipartite. Identifier: `bipartite_color`.

## Definition

Bipartite color.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `is_bipartite` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `bipartite_mapping; is_bipartite` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `is_bipartite` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `is_bipartite` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `digraph_is_bipartite; digraph_two_color; graph_is_bipartite; graph_two_color; is_bipartite; two_color` | API listing |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `is_bipartite` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `is_bipartite` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bipartite_color` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.bipartite.color(G) (-1 everywhere where it raises)` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
