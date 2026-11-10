---
title: "Graph center"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Graph center {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `graph_center`. 1 measure.

## Definition {#concept-definition}

Nodes of smallest eccentricity; empty unless the network is (strongly) connected, as in NetworkX.

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Center {#dm_center}

Measure id: `dm_center`. Original family: Paths and distances.

**Definition.** Nodes of smallest eccentricity; empty unless the network is (strongly) connected, as in NetworkX.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `center` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-dm_center-igraph) | `graph_center` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_center-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: graph\_center.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dm_center` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.center(G) (empty when NetworkX raises on a disconnected network)` |  |
| `dm_center_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.center(G, weight = 'weight')` |  |

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
