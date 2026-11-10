---
title: "Average node"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Average node

Family: Components and connectivity. Identifier: `average_node`.

## Definition

Local node connectivity of every ordered pair, as an n-by-n matrix.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `vertex_average` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_average_node` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.average_node_connectivity(G)` |  |

## References

[esfahanian1984computing](../references.html#esfahanian1984computing), [even1975algorithm](../references.html#even1975algorithm), [even1975network](../references.html#even1975network), [ford1956maximal](../references.html#ford1956maximal), [harary1969graph](../references.html#harary1969graph), [menger1927allgemeinen](../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../references.html#schnorr1979bottlenecks)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
