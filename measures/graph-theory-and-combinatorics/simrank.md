---
title: "SimRank"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SimRank {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Similarity and link prediction. Concept id: `simrank`. 1 measure.

## Definition {#concept-definition}

SimRank similarity of every pair of nodes: two nodes are similar when their in-neighbors are (Jeh and Widom 2002).

*Definition not yet written.*

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

## Simrank {#simrank}

Measure id: `simrank`. Original family: Graph theory and combinatorics.

**Definition.** SimRank similarity of every pair of nodes: two nodes are similar when their in-neighbors are (Jeh and Widom 2002).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>simrank_similarity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>simrank</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.simrank_similarity(G) on the simple Graph or DiGraph, every pair</code></td><td></td></tr><tr><td><code>simrank_converged</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-11, rel 1e-09</td><td><code>nx.similarity._simrank_similarity_python(G, tolerance = 1e-13)</code></td><td></td></tr><tr><td><code>simrank_pairwise</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.similarity._simrank_similarity_python(G)</code></td><td></td></tr><tr><td><code>simrank_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-09</td><td><code>nx.simrank_similarity(M) on the weighted multigraph (to_numpy_array adds the weights of parallel edges)</code></td><td></td></tr></tbody></table></div>

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
