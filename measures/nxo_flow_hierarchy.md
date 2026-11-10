---
title: "Flow hierarchy"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Flow hierarchy

Family: Graph theory and combinatorics. Identifier: `nxo_flow_hierarchy`.

## Definition

Flow hierarchy.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `flow_hierarchy` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_flow_hierarchy` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.flow_hierarchy(G)` |  |
| `nxo_flow_hierarchy_weighted` | NetworkX | directed | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.flow_hierarchy(G, weight = 'weight')` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
