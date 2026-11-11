---
title: "SBM description length"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SBM description length {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_description_length`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(b_i\)</td><td>block of node \(i\); \(B\) blocks</td></tr><tr><td>\(A\)</td><td>multigraph adjacency, \(A_{ij}\) edges between \(i\) and \(j\)</td></tr><tr><td>\(e_{rs}\)</td><td>number of edges between blocks \(r\) and \(s\)</td></tr><tr><td>\(k_i\)</td><td>degree of node \(i\)</td></tr><tr><td>\(n_r\)</td><td>size of block \(r\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

SBM description length. Entries grouped here: Sbm description length.

*Definition partly written:* The decomposition and the meaning of each term are given; the closed-form expressions of \\(P(A\\mid e,b)\\), \\(P(e)\\), \\(P(b)\\) and \\(P(k\\mid e,b)\\) were not checked against the paper text and are not written.

<div class="formula-block"><p class="formula-name"><strong>Description length (Peixoto 2017; degree correction after Karrer and Newman 2011)</strong> <span class="applies">applies to: any, multigraph</span></p><div class="formula">\[\Sigma(A,b)=-\ln P(A\mid e,b)-\ln P(e)-\ln P(b)\quad\bigl[-\ln P(k\mid e,b)\ \text{added, with }P(A\mid k,e,b),\ \text{for the degree-corrected model}\bigr]\]</div><p class="formula-where">The negative log of the joint probability of the network, the block edge counts, the partition and (degree-corrected) the degrees, with the microcanonical Bayesian priors of the paper; it is in nats. The components are reported separately: adjacency, partition, edges, degrees. The closed forms of the components are in the paper and are not transcribed here.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#sbm_description_length">Sbm description length</a></td><td><code>sbm_description_length</code></td><td>1</td><td>Total description length of a given partition and its four components, without or with degree correction; parallel edges are read with multiplicity, weights are ignored.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For one node the partition has one block; the formula is stated for any \(N\ge1\), the sources only record that graph-tool was not run on it.</td><td><span class="st st-w st-nov" title="The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).">no value</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The model is for multigraphs: parallel edges count with their multiplicity in \(A\) and \(e_{rs}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Loops are admitted in the multigraph model.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>graph-tool</strong>: no value. The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node). <em>(conventions.json sbm_description_length)</em></li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details></div>

## Sbm description length {#sbm_description_length}

Measure id: `sbm_description_length`. Original family: Statistical fitting.

**Definition.** Sbm description length.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>BlockState</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>sbm_dl_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_b2</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_b5</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_dc_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_dc_b2</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_dc_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_dl_dc_b5</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/sbm.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/sbm.yaml); [harness/golden/graphtool/](https://github.com/knapply/net-oracles/tree/main/harness/golden/graphtool/)

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
