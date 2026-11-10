---
title: "Wl subgraph"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Wl subgraph

Family: Graph theory and combinatorics. Identifier: `wl_subgraph`.

## Definition

Wl subgraph.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `wl_subgraph` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G)` |  |
| `wl_subgraph_edge_labels` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, edge_attr = 'label')` | edge labels need a network without parallel edges (a NetworkX Graph has one label per pair) |
| `wl_subgraph_initial` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, iterations = 2, include_initial_labels = True)` |  |
| `wl_subgraph_node_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.weisfeiler_lehman_subgraph_hashes(G, node_attr = 'label', include_initial_labels = True)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
