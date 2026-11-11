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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(R\)</td><td>number of sampled paths</td></tr><tr><td>\(T\)</td><td>path length</td></tr><tr><td>\(\mathcal P\)</td><td>random path of \(T\) steps</td></tr></tbody></table></div>

## Definition {#concept-definition}

The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

<div class="formula-block"><p class="formula-name"><strong>Panther similarity (Zhang et al. 2015)</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[s(u,v)=\Pr\bigl(u\in\mathcal P\ \wedge\ v\in\mathcal P\bigr)\approx\frac{\#\{\text{sampled paths containing both}\}}{R}\]</div><p class="formula-where">Probability that a random path (uniform start among non-isolated nodes, \(T\) uniform steps) visits both nodes; estimated from \(R\) sampled paths, so two runs differ by sampling error. The top-\(k\) nodes by \(s(u,\cdot)\) are the most similar to \(u\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#panther">Panther</a></td><td><code>panther</code></td><td>1</td><td>The \(k\) nodes most similar to a source, estimated by sampling, or the similarity vectors.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">Isolated nodes cannot start or continue a path: similarity 0, and they are excluded from the start distribution.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No path: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Nodes in different components are never on the same path: similarity 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal estimates and sampling noise make the top-\(k\) order unstable.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(k\) beyond the number of non-isolated nodes minus 1 asks for more nodes than exist.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

## Panther {#panther}

Measure id: `panther`. Original family: Graph theory and combinatorics.

**Definition.** The k nodes most similar to a source by Panther: how often random paths contain both (Zhang et al. 2015).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>panther_similarity; panther_vector_similarity</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>panther</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0.015, rel 0</td><td><code>nx.panther_similarity(G, hub, k = (non-isolated nodes) - 1, eps = 0.01, seed = 1)</code></td><td>as for the definition oracle</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/similarity.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/similarity.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**References:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [jeh2002simrank](../../references.html#jeh2002simrank), [zhang2015panther](../../references.html#zhang2015panther)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
