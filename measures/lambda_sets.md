---
title: "Lambda sets"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Lambda sets

Family: Cohesion and subgroups. Identifier: `lambda_sets`.

## Definition

Gusfield's equivalent flow tree: each node's parent and the edge connectivity to it (n - 1 maximum flows).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `lambda_sets` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `classes of nx.edge_connectivity >= k with at least two members, for every k >= 1` |  |

## References

[borgatti1990ls](../references.html#borgatti1990ls), [edmonds1972theoretical](../references.html#edmonds1972theoretical), [ford1956maximal](../references.html#ford1956maximal), [gomory1961multi](../references.html#gomory1961multi), [gusfield1990very](../references.html#gusfield1990very)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
