---
title: "Paths all shortest"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths all shortest

Family: Paths and distances. Identifier: `paths_all_shortest`.

## Definition

Paths all shortest.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `all_shortest_paths` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `all_shortest_paths` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `get_all_shortest_paths` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `all_shortest_paths` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `all_shortest_paths; digraph_all_shortest_paths; digraph_num_shortest_paths_unweighted; graph_all_shortest_paths; graph_num_shortest_paths_unweighted; num_shortest_paths_unweighted` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_all_shortest_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.all_shortest_paths(G, 0, n - 1)) (none on NetworkXNoPath)` |  |
| `paths_all_shortest_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.all_shortest_paths(G, 0, n - 1, weight = 'weight'))` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
