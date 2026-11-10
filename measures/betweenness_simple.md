---
title: "Betweenness simple"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Betweenness simple

Family: Centrality. Identifier: `betweenness_simple`.

## Definition

Betweenness simple.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [sna](../tools/sna.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `betweenness_networkx` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(MultiGraph/MultiDiGraph, normalized = False)` |  |
| `betweenness_networkx` | sna | any | agrees |  |  | abs 1e-09, rel 1e-09 | `sna::betweenness(m, gmode, cmode = 'directed' \| 'undirected')` |  |
| `betweenness_networkx_weighted` | NetworkX | any | agrees |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(MultiGraph/MultiDiGraph, weight = 'weight', normalized = False), which uses the lightest parallel edge` |  |

Tools cited: [butts2008sna](../references.html#butts2008sna), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
