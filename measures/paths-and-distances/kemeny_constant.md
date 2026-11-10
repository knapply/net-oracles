---
title: "Kemeny constant"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Kemeny constant {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Resistance and spectral distances. Concept id: `kemeny_constant`. 1 measure.

## Definition {#concept-definition}

Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

*Definition not yet written.*

## References {#concept-references}

[brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

## Kemeny {#cx_kemeny}

Measure id: `cx_kemeny`. Original family: Descriptive statistics.

**Definition.** Kemeny's constant of the random walk: the expected steps to reach a stationary-distributed node, the same from every start.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>kemeny_constant</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cx_kemeny</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.kemeny_constant(G)</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr><tr><td><code>cx_kemeny_weighted</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected</td><td>defaults, normalization</td><td>abs 1e-14, rel 1e-12</td><td><code>nx.kemeny_constant(G, weight = 'weight')</code></td><td>NetworkX's resistance_distance and kemeny_constant raise an error on disconnected graphs; the reference gives infinite resistance between components and NaN for Kemeny's constant.</td></tr></tbody></table></div>

**References:** [brandes2005centrality](../../references.html#brandes2005centrality), [ellens2011effective](../../references.html#ellens2011effective), [hestenes1952methods](../../references.html#hestenes1952methods), [kermarrec2011second](../../references.html#kermarrec2011second), [klein1993resistance](../../references.html#klein1993resistance), [levene2002kemeny](../../references.html#levene2002kemeny), [newman2005measure](../../references.html#newman2005measure), [stephenson1989rethinking](../../references.html#stephenson1989rethinking)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
