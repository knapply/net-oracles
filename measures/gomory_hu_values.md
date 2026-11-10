---
title: "Gomory hu values"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Gomory hu values

Family: Components and connectivity. Identifier: `gomory_hu_values`.

## Definition

The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_gomory_hu_values` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_cut_value(G, u, v) for every pair u < v` |  |

## References

[gomory1961multi](../references.html#gomory1961multi), [gusfield1990very](../references.html#gusfield1990very), [hagberg2008exploring](../references.html#hagberg2008exploring)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
