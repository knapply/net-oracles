---
title: "Closeness vitality"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Closeness vitality {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `closeness_vitality`. 1 measure.

## Definition {#concept-definition}

Wiener index of the network minus that of the network without the node, for every node.

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Closeness vitality {#dm_closeness_vitality}

Measure id: `dm_closeness_vitality`. Original family: Paths and distances.

**Definition.** Wiener index of the network minus that of the network without the node, for every node.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `closeness_vitality` |  |
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-dm_closeness_vitality-centiserve) | `closeness.vitality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_closeness_vitality-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.vitality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_closeness_vitality` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.closeness_vitality(G) (an error is undefined)` |  |
| `dm_closeness_vitality_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.closeness_vitality(G, weight = 'weight')` |  |

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
