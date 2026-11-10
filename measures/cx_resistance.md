---
title: "Resistance"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Resistance

Family: Centrality. Identifier: `cx_resistance`.

## Definition

Resistance distance between every pair of nodes, infinite across components (Klein and Randic 1993).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `resistance_distance` |  |
| [netrankr](../tools/netrankr.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_resistance` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.resistance_distance(G)` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |
| `cx_resistance` | netrankr | undirected | differs | loops, multi\_edges, (no value) directed, (no value) disconnected | defaults, direction, multi\_edges, self\_loops, weights | abs 1e-14, rel 1e-12 | `indirect_relations(g, 'dist_resist')` | netrankr reads the network as undirected, unweighted and simple, so parallel edges count once and self-loops not at all; networks without them agree. netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist", "depend\_curflow") is defined only for connected graphs and raises an error otherwise. |
| `cx_resistance_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected | defaults, normalization | abs 1e-14, rel 1e-12 | `nx.resistance_distance(G, weight = 'weight', invert_weight = True)` | NetworkX's resistance\_distance and kemeny\_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant. |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [schoch2018centrality](../references.html#schoch2018centrality)
{% endraw %}
