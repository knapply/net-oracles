---
title: "All pairs node"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# All pairs node

Family: Components and connectivity. Identifier: `all_pairs_node`.

## Definition

Local node connectivity of every ordered pair, as an n-by-n matrix.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_all_pairs_node` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.all_pairs_node_connectivity(G), with 0 on the diagonal` |  |

## References

[esfahanian1984computing](../references.html#esfahanian1984computing), [even1975algorithm](../references.html#even1975algorithm), [even1975network](../references.html#even1975network), [ford1956maximal](../references.html#ford1956maximal), [harary1969graph](../references.html#harary1969graph), [menger1927allgemeinen](../references.html#menger1927allgemeinen), [schnorr1979bottlenecks](../references.html#schnorr1979bottlenecks)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
