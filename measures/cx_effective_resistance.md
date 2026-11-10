---
title: "Effective resistance"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Effective resistance

Family: Descriptive statistics. Identifier: `cx_effective_resistance`.

## Definition

Effective graph resistance (Kirchhoff index): the sum of resistance distances over all node pairs (Ellens et al. 2011).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `effective_graph_resistance` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_effective_resistance` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.effective_graph_resistance(G)` |  |
| `cx_effective_resistance_weighted` | NetworkX | undirected | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.effective_graph_resistance(G, weight = 'weight')` |  |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
