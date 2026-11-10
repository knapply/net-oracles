---
title: "Fast greedy"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Fast greedy

Family: Communities. Identifier: `fast_greedy`.

## Definition

Greedy modularity communities by repeated best mergers (Clauset, Newman and Moore); returns the best level, its modularity and the mergers.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs | `greedy_modularity_communities; naive_greedy_modularity_communities` |  |
| [igraph (R)](../tools/igraph.html) | ≠ checked, differs by convention | `cluster_fast_greedy` |  |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `community_fastgreedy` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Community detection (6.7xx): FastGreedy, LabelProp, LocalGreedy (6.809), Louvain-type, Moca, Girvan-Newman, factor-analysis clustering, polish partitions, Initi; FastGreedy` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fast_greedy` | NetworkX | undirected | no-value-on-some-inputs |  | ties | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(multigraph)` | NetworkX breaks ties between equally good mergers by the order of its floating-point heap, the reference by node order; on these fixtures the oracle verified in exact arithmetic that every merger NetworkX made was a best merger, so the two partitions differ only by tie-breaking |
| `fast_greedy` | igraph (R) | undirected | differs | directed, undirected, (no value) loops | direction, multi\_edges, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_fast_greedy(simplify(g, edge.attr.comb = 'sum'), weights = multiplicity)` | Exactly tied mergers on the greedy path are common (modularity gains are sums of small fractions): igraph breaks them by its own order and may reach a different dendrogram and best level. On networks without community structure (complete6, star8, two nodes and one edge) every merger along the reference value's path raises modularity and the path ends in one group (modularity 0), while igraph reports a partition of negative modularity. The definition oracle checks the reference. cluster\_fast\_greedy() needs a graph without multiple edges, so parallel edges are collapsed into weights, and the self-loops dropped with them count toward degree and modularity in the reference (as in NetworkX) but not in the simplified igraph graph; the listed fixtures have tied mergers on the greedy path (verified in exact arithmetic), which igraph breaks by its own order and so reaches a different partition. On complete6 and star8, which have no community structure, every merger along the reference value's path raises modularity and the path ends in one group (modularity 0), while igraph reports a partition of negative modularity (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `fast_greedy_membership` | NetworkX | undirected | differs | directed, undirected | direction, ties | abs 0, rel 0 | `membership of nx.community.greedy_modularity_communities(multigraph)` | Exactly tied mergers: NetworkX's greedy\_modularity\_communities breaks ties by its heap and dict order, the reference by group number. as for fast\_greedy (the oracle script skips these fixtures; on other graphs the tag declarations apply) |
| `fast_greedy_resolution` | NetworkX | undirected | no-value-on-some-inputs |  | ties | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(G, resolution = 0.5)` | tie-breaking between equally good mergers, verified in exact arithmetic as for fast\_greedy |
| `fast_greedy_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `modularity of nx.community.greedy_modularity_communities(G, weight = 'weight')` |  |
| `fast_greedy_weighted` | igraph (R) | undirected | differs | directed, undirected | direction, self\_loops, ties, weights | abs 1e-14, rel 1e-12 | `modularity of igraph::cluster_fast_greedy(g, weights = E(g)$weight)` | Tied mergers as for fast\_greedy; and self-loops, which igraph drops (one node with a loop: igraph -1, the reference 0). the weighted greedy path has tied mergers on these fixtures (verified in exact arithmetic), which igraph breaks by its own order (the oracle script skips these fixtures; on other graphs the tag declarations apply) |

## References

[clauset2004finding](../references.html#clauset2004finding)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
