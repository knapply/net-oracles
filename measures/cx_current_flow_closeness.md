---
title: "Current flow closeness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Current flow closeness

Family: Centrality. Identifier: `cx_current_flow_closeness`.

## Definition

Current-flow closeness of every node: the inverse of its mean resistance distance to the others (information centrality, Brandes and Fleischer 2005).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `current_flow_closeness_centrality` |  |
| [netrankr](../tools/netrankr.html) | ✓ checked, agrees |  |  |
| [centiserve](../tools/centiserve.html) | · reported in docs | `closeness.currentflow` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_cfc` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.current_flow_closeness_centrality(G)` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |
| `cx_cfc` | netrankr | undirected | differs | loops, multi\_edges, (no value) directed, (no value) disconnected | defaults, direction, multi\_edges, self\_loops, weights | abs 1e-14, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'dist_resist'), 'invsum')` | netrankr reads the network as undirected, unweighted and simple, so parallel edges count once and self-loops not at all; networks without them agree. netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist", "depend\_curflow") is defined only for connected graphs and raises an error otherwise. |
| `cx_cfc_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) multi\_edges | defaults, multi\_edges, normalization, ties | abs 1e-14, rel 1e-12 | `nx.current_flow_closeness_centrality(G, weight = 'weight')` | NetworkX defines these measures for connected simple graphs and raises an error otherwise (the reference returns NaN on disconnected networks); on a single node NetworkX divides by (n - 1)(n - 2) = 0 or forms a random walk without steps. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F077](../findings.html#f077) | centiserve | convention | Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks |

## References

[brandes2005centrality](../references.html#brandes2005centrality), [ellens2011effective](../references.html#ellens2011effective), [hestenes1952methods](../references.html#hestenes1952methods), [kermarrec2011second](../references.html#kermarrec2011second), [klein1993resistance](../references.html#klein1993resistance), [levene2002kemeny](../references.html#levene2002kemeny), [newman2005measure](../references.html#newman2005measure), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [jalili2015centiserver](../references.html#jalili2015centiserver), [schoch2018centrality](../references.html#schoch2018centrality)
{% endraw %}
