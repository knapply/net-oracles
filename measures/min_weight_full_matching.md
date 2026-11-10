---
title: "Min weight full matching"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Min weight full matching

Family: Two-mode and bipartite. Identifier: `min_weight_full_matching`.

## Definition

A full matching of least total cost of a bipartite graph, as each node's mate (-1 if unmatched).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `minimum_weight_full_matching` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `min_weight_full_matching` | NetworkX | undirected | agrees |  |  | abs 1e-09, rel 1e-12 | `nx.bipartite.minimum_weight_full_matching(G, top, weight = c): (total cost, 1 if it covers the smaller side); -1 where it raises` |  |

## References

[jonker1987shortest](../references.html#jonker1987shortest), [kuhn1955hungarian](../references.html#kuhn1955hungarian)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
