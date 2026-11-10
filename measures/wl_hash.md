---
title: "Wl hash"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Wl hash

Family: Graph theory and combinatorics. Identifier: `wl_hash`.

## Definition

Wl hash.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `weisfeiler_lehman_graph_hash; weisfeiler_lehman_subgraph_hashes` |  |
| [scikit-network](../tools/sknetwork.html) | · reported in docs | `color_weisfeiler_lehman; weisfeiler_lehman_coloring` | API listing |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `ColorRefinementAlgorithm` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `wl_hash` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G)` |  |
| `wl_hash_both_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label', node_attr = 'label', digest_size = 32)` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_hash_edge_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, edge_attr = 'label')` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_hash_iter1` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, iterations = 1)` |  |
| `wl_hash_iter5_digest8` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, iterations = 5, digest_size = 8)` |  |
| `wl_hash_node_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_graph_hash(G, node_attr = 'label')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
