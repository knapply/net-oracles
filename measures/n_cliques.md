---
title: "N cliques"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# N cliques

Family: Cohesion and subgroups. Identifier: `n_cliques`.

## Definition

n-cliques: maximal sets whose members are all within distance n of each other in the whole network.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `ncliques` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `n_cliques_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cliques on the graph joining nodes at distance <= 2 (single_source_shortest_path_length, cutoff 2)` |  |
| `n_cliques_3_min4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.find_cliques on the distance-3 power graph, keeping cliques of at least 4` |  |

## References

[alba1973graph](../references.html#alba1973graph), [luce1950connectivity](../references.html#luce1950connectivity), [mokken1979cliques](../references.html#mokken1979cliques)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
