---
title: "Stochastic block model fit"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stochastic block model fit {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_fit`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(b_i\)</td><td>block of node \(i\); \(B\) blocks</td></tr><tr><td>\(A\)</td><td>multigraph adjacency, \(A_{ij}\) edges between \(i\) and \(j\)</td></tr><tr><td>\(e_{rs}\)</td><td>number of edges between blocks \(r\) and \(s\)</td></tr><tr><td>\(k_i\)</td><td>degree of node \(i\)</td></tr><tr><td>\(n_r\)</td><td>size of block \(r\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

*Definition partly written:* The objective is written; the search (agglomerative start, annealing, Markov chain refinement, restarts) is a heuristic whose result depends on the seed, and is not part of the definition.

<div class="formula-block"><p class="formula-name"><strong>Description length (Peixoto 2017; degree correction after Karrer and Newman 2011)</strong> <span class="applies">applies to: any, multigraph</span></p><div class="formula">\[\Sigma(A,b)=-\ln P(A\mid e,b)-\ln P(e)-\ln P(b)\quad\bigl[-\ln P(k\mid e,b)\ \text{added, with }P(A\mid k,e,b),\ \text{for the degree-corrected model}\bigr]\]</div><p class="formula-where">The negative log of the joint probability of the network, the block edge counts, the partition and (degree-corrected) the degrees, with the microcanonical Bayesian priors of the paper; it is in nats. The components are reported separately: adjacency, partition, edges, degrees. The closed forms of the components are in the paper and are not transcribed here.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Fit as minimization</strong> <span class="applies">applies to: any, multigraph</span></p><div class="formula">\[\hat b=\arg\min_{b}\ \Sigma(A,b)\]</div><p class="formula-where">The partition (and its number of blocks) with the shortest description length. The exact minimizer is found only by exhaustive search on tiny graphs; heuristics return a local minimum.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#sbm_fit">Sbm fit</a></td><td><code>sbm_fit</code></td><td>1</td><td>Blocks, their number and the description length of the best partition found over several restarts.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">With no edges the description length is smallest for a single block; the fit is trivial.</td><td><span class="st st-w st-nov" title="The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.">no value</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With fewer than two nodes there is one partition.</td><td><span class="st st-w st-nov" title="The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.">no value</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several partitions can share the minimal description length; which one is returned depends on the search and the seed.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>graph-tool</strong>: no value. The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. <em>(conventions.json sbm_fit)</em></li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>graph-tool</strong>: no value. The oracle script does not run graph-tool on a network with fewer than two nodes or without edges. <em>(conventions.json sbm_fit)</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## Sbm fit {#sbm_fit}

Measure id: `sbm_fit`. Original family: Statistical fitting.

**Definition.** Stochastic block model fit by minimum description length: agglomerative start, annealed and Markov chain refinement, best of several restarts; returns the blocks, their number and the description length with its parts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimize_blockmodel_dl</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>sbm_fit_dc_vs_graphtool</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.</td></tr><tr><td><code>sbm_fit_vs_graphtool</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network with fewer than two nodes or without edges.</td></tr></tbody></table></div>

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
