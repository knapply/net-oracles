---
title: "Spinglass"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spinglass {#concept-top}

Family: [Communities](index.html). Subfamily: Modularity-based detection. Concept id: `spinglass`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\sigma_i\in\{1..q\}\)</td><td>spin (community) of node \(i\), \(q\) the maximum number of spins</td></tr><tr><td>\(A_{ij}\)</td><td>weight of the edges from \(i\) to \(j\) (the edge count for an unweighted graph, parallel edges added); for an undirected graph \(A\) is symmetric and a self-loop adds 2 to \(A_{ii}\)</td></tr><tr><td>\(p_{ij}\)</td><td>null-model weight, \(k_ik_j/2m\) for the configuration model</td></tr><tr><td>\(\gamma\)</td><td>resolution (coupling) parameter</td></tr></tbody></table></div>

## Definition {#concept-definition}

Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

<div class="formula-block"><p class="formula-name"><strong>Potts Hamiltonian (Reichardt and Bornholdt 2006)</strong> <span class="applies">applies to: connected, undirected</span></p><div class="formula">\[\mathcal H(\sigma)=-\sum_{i\ne j}\bigl(A_{ij}-\gamma p_{ij}\bigr)\delta(\sigma_i,\sigma_j)\]</div><p class="formula-where">Minimizing \(\mathcal H\) is maximizing modularity at \(\gamma=1\); minimized by simulated annealing, so the result is stochastic. Traag and Bruggeman 2009 add negative weights. Stated for connected networks.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#spinglass">Spinglass</a></td><td><code>spinglass</code></td><td>2</td><td>The communities of a connected network from simulated annealing of the Potts Hamiltonian; \(q\) bounds the number of communities.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">Not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Not defined (trivial network).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No coupling: every spin assignment has \(\mathcal H=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">The method is stated for connected networks; with several components the annealing is not determined.</td><td><span class="st st-w st-nov" title="both tools reject disconnected networks;">no value</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The sum is over \(i\ne j\): loops do not enter.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges add to \(A_{ij}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Weights enter \(A\) and the null model; negative weights are handled by Traag and Bruggeman 2009.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal energies: a stochastic search returns one minimizer.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\gamma\ge0\); \(q\) at least the number of communities wanted.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li><strong>igraph (R)</strong>: no value. both tools reject disconnected networks; <em>(conventions.json spinglass / spinglass_quality)</em></li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

## Spinglass {#spinglass}

Measure id: `spinglass`. Original family: Communities.

**Definition.** Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>cluster_spinglass</code></td><td></td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-spinglass-pyigraph">details</a></td><td><code>community_spinglass</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-spinglass-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_spinglass.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>spinglass_quality</code></td><td>igraph (R)</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) disconnected, (no value) edge_case</td><td>defaults</td><td>abs 0.02, rel 0</td><td><code>mean over set.seed(1..10) of modularity(g, cluster_spinglass(g, weights = NA))</code></td><td>both tools reject disconnected networks; igraph also rejects the trivial ones</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/communities.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/communities.yaml); [harness/golden/igraph/](https://github.com/knapply/net-oracles/tree/main/harness/golden/igraph/)

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f038">F038</a></td><td>igraph (R)</td><td>convention</td><td>Spinglass reads the network as simple</td></tr></tbody></table></div>

**References:** [reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
