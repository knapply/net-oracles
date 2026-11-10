---
title: "Second order"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Second order

Family: Centrality. Identifier: `cx_second_order`.

## Definition

Second-order centrality of every node: the standard deviation of its return times in a random walk (Kermarrec et al. 2011).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `second_order_centrality` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_second_order` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.second_order_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_second_order_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.second_order_centrality(G, weight = 'weight')` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
