---
title: "Panther"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Panther {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `panther`. 1 measure.

## Definition {#concept-definition}

The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

*Definition not yet written.*

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

## Panther {#panther}

Measure id: `panther`. Original family: Graph theory and combinatorics.

**Definition.** The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>panther_similarity; panther_vector_similarity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>panther</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0.015, rel 0</td><td><code>nx.panther_similarity(G, hub, k = (non-isolated nodes) - 1, eps = 0.01, seed = 1)</code></td><td>as for the definition oracle</td></tr></tbody></table></div>

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
