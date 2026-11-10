---
title: "Edge cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Edge cut

Family: Components and connectivity. Identifier: `edge_cut`.

## Definition

A smallest set of edges whose removal disconnects the network.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [NetworKit](../tools/networkit.html) | · reported in docs | `EdgeCut` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_edge_cut` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 0, rel 0 | `[len(nx.minimum_edge_cut(G)), 1]` | as for conn\_node\_cut |

## References

[esfahanian1984computing](../references.html#esfahanian1984computing), [even1975algorithm](../references.html#even1975algorithm), [even1975network](../references.html#even1975network), [ford1956maximal](../references.html#ford1956maximal), [hagberg2008exploring](../references.html#hagberg2008exploring), [menger1927allgemeinen](../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../references.html#schnorr1979bottlenecks)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [staudt2016networkit](../references.html#staudt2016networkit)
{% endraw %}
