---
title: "Min node cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Min node cut

Family: Components and connectivity. Identifier: `min_node_cut`.

## Definition

Min node cut.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_min_node_cut` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)) on the simple graph; -1 if G.has_edge(0, n - 1)` |  |
| `flow_min_node_cut_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.minimum_cut_value(H, '0B', '(n-1)A') on the split digraph H: arcs vA -> vB of capacity (v mod 3) + 1 and uB -> vA for each arc u -> v without a capacity (infinite)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
