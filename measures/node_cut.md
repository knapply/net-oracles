---
title: "Node cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Node cut

Family: Components and connectivity. Identifier: `node_cut`.

## Definition

A smallest set of nodes whose removal disconnects the network.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `minimum_edge_cut; minimum_node_cut; minimum_st_edge_cut; minimum_st_node_cut` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `is_min_separator; is_separator; min_separators; min_st_separators; stCuts; st_cuts; st_min_cuts` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `all_minimal_st_separators; all_st_cuts; all_st_mincuts; is_minimal_separator; is_separator; minimum_size_separators` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_node_cut` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 0, rel 0 | `[len(nx.minimum_node_cut(G)), 1]` | NetworkX raises an error for a network that is not connected; the reference returns the empty cut. |
| `conn_node_cut_networkx` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 0, rel 0 | `[len(nx.minimum_node_cut(G)), 1]` | as for conn\_node\_cut |

## References

[esfahanian1984computing](../references.html#esfahanian1984computing), [even1975algorithm](../references.html#even1975algorithm), [even1975network](../references.html#even1975network), [ford1956maximal](../references.html#ford1956maximal), [hagberg2008exploring](../references.html#hagberg2008exploring), [menger1927allgemeinen](../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../references.html#schnorr1979bottlenecks)

Tools cited: [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
