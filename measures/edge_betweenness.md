---
title: "Edge betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Edge betweenness

Family: Centrality. Identifier: `edge_betweenness`.

## Definition

Shortest-path betweenness of every edge (Brandes 2001 accumulation, as used by Girvan and Newman).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `edge_betweenness_centrality` |  |
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees | `edge_betweenness` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `edge_betweenness` | API listing |
| [NetworKit](../tools/networkit.html) | ✓ checked, agrees |  |  |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `digraph_edge_betweenness_centrality; edge_betweenness_centrality; graph_edge_betweenness_centrality` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `EdgeBetweennessCentrality` | API listing |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `edge_betweenness_bin; edge_betweenness_wei` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `edge_betweenness` | NetworkX | any | differs | multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `nx.edge_betweenness_centrality(MultiGraph/MultiDiGraph, normalized = False)` | NetworkX counts shortest paths per neighbour, not per parallel edge, and then credits every parallel edge with the whole amount, so the values of parallel edges add up to more than the paths they carry. This reference (like the exact-arithmetic definition oracle) treats parallel edges as distinct shortest paths that share the credit. |
| `edge_betweenness` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::edge_betweenness(g, directed, weights = NA)` |  |
| `edge_betweenness` | NetworKit | any | no-value-on-some-inputs | (no value) loops, (no value) multi\_edges | multi\_edges, self\_loops, ties | abs 1e-09, rel 1e-09 | `nk.centrality.Betweenness(G, normalized = False, computeEdgeCentrality = True).edgeScores() looked up by edgeId(u, v), halved when undirected` | NetworKit numbers edges in its own adjacency order, so the oracle maps its scores back by endpoints, which parallel edges leave ambiguous; loops are not mapped either. |
| `edge_betweenness` | rustworkx | any | agrees |  |  | abs 1e-09, rel 1e-09 | `rx.edge_betweenness_centrality(G, normalized = False)` |  |
| `edge_betweenness_normalized` | NetworkX | any | differs | multi\_edges, (no value) one\_node | defaults, multi\_edges, normalization | abs 1e-12, rel 1e-09 | `nx.edge_betweenness_centrality(G, normalized = True)` | As for edge\_betweenness: NetworkX over-credits parallel edges. NetworkX leaves a one-node graph's values unscaled (0) where the reference reports NaN. |
| `edge_betweenness_weighted` | NetworkX | any | differs | multi\_edges | multi\_edges, normalization, weights | abs 1e-09, rel 1e-09 | `nx.edge_betweenness_centrality(G, weight = 'weight', normalized = False)` | NetworkX counts one shortest path per neighbour pair, so parallel edges of equal weight do not multiply the path count; the reference, igraph and NetworKit count each edge as a path (checked: 0-&gt;1 twice, 1-&gt;2, 0-&gt;3, 3-&gt;2, all weights 1, gives 2/3 and 1/3 for nodes 1 and 3 in the reference, 1/2 and 1/2 in NetworkX). |
| `edge_betweenness_weighted` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::edge_betweenness(g, directed, weights = E(g)$weight)` |  |
| `edge_betweenness_weighted_strength` | NetworkX | any | differs | integer\_weights | ties, weights | abs 1e-09, rel 1e-09 | `nx.edge_betweenness_centrality(G, weight = 'weight') with weight = 1/strength` | Reciprocals of whole-number weights often give path lengths that tie exactly (1/3 + 1/6 = 1/2) but differ in the last bit of floating point. NetworkX compares lengths exactly and drops one of the tied paths; this reference (like igraph) compares with a relative tolerance and agrees with the exact-arithmetic definition oracle. |
| `edge_betweenness_weighted_strength` | igraph (R) | any | agrees |  |  | abs 1e-09, rel 1e-09 | `igraph::edge_betweenness(g, directed, weights = 1 / E(g)$weight)` |  |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F062](../findings.html#f062) | NetworKit | convention | edgeScores() follow NetworKit's own edge numbering |

## References

[brandes2008variants](../references.html#brandes2008variants)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [rubinov2010complex](../references.html#rubinov2010complex), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
