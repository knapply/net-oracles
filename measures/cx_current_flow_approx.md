---
title: "Current flow approx"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Current flow approx

Family: Centrality. Identifier: `cx_current_flow_approx`.

## Definition

Current-flow betweenness approximated from sampled pairs of nodes (random pairs or given ones).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `approximate_current_flow_betweenness_centrality` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfb_approx` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.approximate_current_flow_betweenness_centrality(G, epsilon = 0.5, seed = 1), the runner passing the same pairs` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
