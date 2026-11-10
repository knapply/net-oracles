---
title: "N clans"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# N clans

Family: Cohesion and subgroups. Identifier: `n_clans`.

## Definition

n-clans: the n-cliques whose induced subgraph also has diameter at most n.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `n_clans_2` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `2-cliques whose induced subgraph is connected with nx.diameter <= 2` |  |

## References

[alba1973graph](../references.html#alba1973graph), [luce1950connectivity](../references.html#luce1950connectivity), [mokken1979cliques](../references.html#mokken1979cliques)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
