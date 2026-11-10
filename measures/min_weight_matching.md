---
title: "Min weight matching"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Min weight matching

Family: Graph theory and combinatorics. Identifier: `min_weight_matching`.

## Definition

A matching of least total weight among the matchings of largest size, as input edge positions.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `min_weight_matching` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_min_weight` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.min_weight_matching(G, weight = 'weight')` |  |

## References

[edmonds1965maximum](../references.html#edmonds1965maximum), [edmonds1965paths](../references.html#edmonds1965paths), [galil1986efficient](../references.html#galil1986efficient), [hagberg2008exploring](../references.html#hagberg2008exploring)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
