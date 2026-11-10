---
title: "Closeness vitality"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Closeness vitality

Family: Paths and distances. Identifier: `dm_closeness_vitality`.

## Definition

Wiener index of the network minus that of the network without the node, for every node.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `closeness_vitality` |  |
| [centiserve](../tools/centiserve.html) | · reported in docs | `closeness.vitality` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_closeness_vitality` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.closeness_vitality(G) (an error is undefined)` |  |
| `dm_closeness_vitality_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.closeness_vitality(G, weight = 'weight')` |  |

## References

[gutman1994selected](../references.html#gutman1994selected), [hage1995eccentricity](../references.html#hage1995eccentricity), [klein1995hyper](../references.html#klein1995hyper), [koschutzki2005centrality](../references.html#koschutzki2005centrality), [latora2001efficient](../references.html#latora2001efficient), [marchiori2000harmony](../references.html#marchiori2000harmony), [randic1993novel](../references.html#randic1993novel), [schultz1989topological](../references.html#schultz1989topological)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [jalili2015centiserver](../references.html#jalili2015centiserver)
{% endraw %}
