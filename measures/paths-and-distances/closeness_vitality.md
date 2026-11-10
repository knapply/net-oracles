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

*Definition not yet written.*

## References {#concept-references}

[gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

## Closeness vitality {#dm_closeness_vitality}

Measure id: `dm_closeness_vitality`. Original family: Paths and distances.

**Definition.** Wiener index of the network minus that of the network without the node, for every node.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>closeness_vitality</code></td><td></td></tr><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-dm_closeness_vitality-centiserve">details</a></td><td><code>closeness.vitality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-dm_closeness_vitality-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: closeness.vitality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dm_closeness_vitality</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.closeness_vitality(G) (an error is undefined)</code></td><td></td></tr><tr><td><code>dm_closeness_vitality_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.closeness_vitality(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [gutman1994selected](../../references.html#gutman1994selected), [hage1995eccentricity](../../references.html#hage1995eccentricity), [klein1995hyper](../../references.html#klein1995hyper), [koschutzki2005centrality](../../references.html#koschutzki2005centrality), [latora2001efficient](../../references.html#latora2001efficient), [marchiori2000harmony](../../references.html#marchiori2000harmony), [randic1993novel](../../references.html#randic1993novel), [schultz1989topological](../../references.html#schultz1989topological)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
