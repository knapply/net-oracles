---
title: "Paths simple"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Paths simple

Family: Paths and distances. Identifier: `paths_simple`.

## Definition

Paths simple.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `all_simple_edge_paths; all_simple_paths` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `all_simple_paths` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `get_all_simple_paths` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `all_paths` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `AllSimplePaths` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `all_simple_paths; digraph_all_simple_paths; graph_all_simple_paths` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_simple_cutoff4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.all_simple_paths(G, 0, n - 1, cutoff = 4))` |  |

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
