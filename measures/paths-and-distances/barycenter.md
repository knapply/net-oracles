---
title: "Barycenter"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Barycenter {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `barycenter`. 1 measure.

## Definition {#concept-definition}

The nodes of smallest total distance to the others, and every node's total distance.

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Barycenter {#dm_barycenter}

Measure id: `dm_barycenter`. Original family: Paths and distances.

**Definition.** The nodes of smallest total distance to the others, and every node's total distance.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [centiserve](../../tools/centiserve.html) | · reported in docs | `barycenter` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_barycenter` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.barycenter(G) (empty on NetworkXNoPath)` |  |
| `dm_barycenter_weighted` | NetworkX | any | differs | fractional\_weights | ties, weights | abs 1e-12, rel 1e-12 | `nx.barycenter(G, weight = 'weight')` | tie: exact compares floating-point sums exactly, as NetworkX does, but the sums are added in a different order, so a tie that is exact in real arithmetic can hold in one tool and not the other. |

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
