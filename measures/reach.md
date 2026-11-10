---
title: "Reach"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Reach

Family: Centrality. Identifier: `reach`.

## Definition

Number (or share) of other nodes within distance k of every node.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `ancestors; descendants; descendants_at_distance` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `count_reachable` |  |
| [sna](../tools/sna.html) | · reported in docs | `reachability` | API listing |
| [rustworkx](../tools/rustworkx.html) | · reported in docs | `ancestors; descendants` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `reach_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.single_source_shortest_path_length(G, v, cutoff = 2)) - 1` |  |
| `reach_2` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'out') - 1` |  |
| `reach_2_all` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `single_source_shortest_path_length on G.to_undirected(), cutoff = 2` |  |
| `reach_2_all` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'all') - 1` |  |
| `reach_2_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `single_source_shortest_path_length on G.reverse(), cutoff = 2` |  |
| `reach_2_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = 2, mode = 'in') - 1` |  |
| `reach_2_normalized` | igraph (R) | any | agrees |  |  | abs 0, rel 1e-14 | `(igraph::ego_size(g, order = 2, mode = 'out') - 1) / (n - 1); undefined for one node` |  |
| `reach_inf` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.single_source_shortest_path_length(G, v)) - 1` |  |
| `reach_inf` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::ego_size(g, order = vcount(g), mode = 'out') - 1` |  |
| `reach_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.single_source_dijkstra_path_length(G, v, weight = 'weight'), lengths <= 3` |  |
| `reach_weighted_strength` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `Dijkstra lengths with edge length 1/weight, <= 1.5` |  |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2005centrality](../references.html#brandes2005centrality), [brandes2008variants](../references.html#brandes2008variants), [butts2008sna](../references.html#butts2008sna), [freeman1977set](../references.html#freeman1977set), [girvan2002community](../references.html#girvan2002community), [hwang2008bridging](../references.html#hwang2008bridging), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
