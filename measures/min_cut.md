---
title: "Min cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Min cut

Family: Components and connectivity. Identifier: `min_cut`.

## Definition

Minimum cut between a set of sources and a set of sinks: its capacity, the source side and the crossing edges.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `minimum_cut; minimum_cut_value; stoer_wagner` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `min_cut` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `mincut; mincut_value; st_mincut` | API listing |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `min_cut; min_st_cut` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `stoer_wagner_min_cut` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `StoerWagnerMinimumCut` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `stoer_wagner_min_cut` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_min_cut_largest` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut(G, 0, n - 1)[1][0] as 1/0 flags` |  |
| `flow_min_cut_largest_multi` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut(H, 'S', 'T')[1][0] without S, as 1/0 flags` |  |
| `flow_min_cut_smallest` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nodes reachable from 0 over arcs with flow < capacity in nx.flow.edmonds_karp(G, 0, n - 1)` |  |

## References

[dinic1970algorithm](../references.html#dinic1970algorithm), [ford1956maximal](../references.html#ford1956maximal), [ford1962flows](../references.html#ford1962flows), [hagberg2008exploring](../references.html#hagberg2008exploring)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
