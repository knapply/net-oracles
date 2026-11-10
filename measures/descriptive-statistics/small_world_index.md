---
title: "Small-world quotient"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Small-world quotient {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `small_world_index`. 2 measures.

## Definition {#concept-definition}

Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#small_world">Small world</a></td><td><code>small_world</code></td><td>1</td></tr><tr><td><a href="#small_world_observed">Small world observed</a></td><td><code>small_world_observed</code></td><td>2</td></tr></tbody></table></div>

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Small world {#small_world}

Measure id: `small_world`. Original family: Generators and rewiring.

**Definition.** Small-world coefficient omega of a connected undirected network against random and lattice references (Telesford et al.).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>omega; sigma</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>small_world_omega</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>defaults, normalization</td><td>abs 0.05, rel 0</td><td><code>mean of nx.omega(G, niter = 2, nrand = 10, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)</code></td><td>As for small_world_sigma; on path10 every clustering coefficient is 0, so NetworkX divides 0 by 0 and raises ZeroDivisionError, where the reference returns NaN.</td></tr><tr><td><code>small_world_sigma</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>ties</td><td>abs 0.15, rel 0</td><td><code>mean of nx.sigma(G, niter = 20, nrand = 20, seed = s) over s = 0..9; -1 where it raises (disconnected graphs)</code></td><td>The means over random graphs are compared on the small networks only, to keep the NetworkX oracle fast; on a star NetworkX's random_reference redraws forever (every draw is rejected), where the reference stops each round after 100 (m + 1) rejected draws.</td></tr></tbody></table></div>

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Small world observed {#small_world_observed}

Measure id: `small_world_observed`. Original family: Descriptive statistics.

**Definition.** Small world observed.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>small_world_observed</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>nx.transitivity and the mean of nx.shortest_path_length over connected pairs (simple undirected graph)</code></td><td></td></tr><tr><td><code>small_world_observed</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>igraph::transitivity(type = 'global') and mean_distance(unconnected = TRUE) on simplify(as_undirected(g))</code></td><td></td></tr><tr><td><code>small_world_observed_local</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>nx.average_clustering and the mean of nx.shortest_path_length over connected pairs</code></td><td></td></tr><tr><td><code>small_world_observed_local</code></td><td>igraph (R)</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-15, rel 1e-13</td><td><code>igraph::transitivity(type = 'average', isolates = 'zero') and mean_distance(unconnected = TRUE)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
