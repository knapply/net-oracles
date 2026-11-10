---
title: "Connectivity"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Connectivity

Family: Components and connectivity. Identifier: `connectivity`.

## Definition

Global edge connectivity: the fewest edges whose removal disconnects the network.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `average_node_connectivity; edge_connectivity; is_k_edge_connected; local_edge_connectivity; local_node_connectivity; node_connectivity` |  |
| [igraph (R)](../tools/igraph.html) | · reported in docs | `adhesion; cohesion; edge_connectivity; vertex_connectivity` | API listing |
| [igraph (Python)](../tools/pyigraph.html) | · reported in docs | `adhesion; cohesion` | API listing |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `edge_connectivity` | API listing |
| [UCINET](../tools/ucinet.html) | · reported in docs | `cohesion` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_edge` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.edge_connectivity(G)` |  |
| `conn_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.node_connectivity(G)` |  |

## References

[esfahanian1984computing](../references.html#esfahanian1984computing), [even1975algorithm](../references.html#even1975algorithm), [even1975network](../references.html#even1975network), [ford1956maximal](../references.html#ford1956maximal), [harary1969graph](../references.html#harary1969graph), [menger1927allgemeinen](../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../references.html#schnorr1979bottlenecks)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring), [siek2002boost](../references.html#siek2002boost)
{% endraw %}
