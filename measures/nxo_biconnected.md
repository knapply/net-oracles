---
title: "Biconnected"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Biconnected

Family: Components and connectivity. Identifier: `nxo_biconnected`.

## Definition

Biconnected.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_biconnected` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges, ties | abs 0, rel 0 | `nx.biconnected_component_edges(G), components in order, (parent, child) edges` | The backend leaves multigraphs to NetworkX (their adjacency order is not the edge order). |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
