---
title: "St node cut"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# St node cut

Family: Components and connectivity. Identifier: `st_node_cut`.

## Definition

St node cut.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_st_node_cut` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[len(nx.connectivity.minimum_st_node_cut(G, 0, n - 1)), 1]; -1 if G.has_edge(0, n - 1)` |  |
| `conn_st_node_cut_networkx` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.connectivity.minimum_st_node_cut(G, 0, n - 1))` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
