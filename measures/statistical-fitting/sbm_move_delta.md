---
title: "SBM move delta"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# SBM move delta {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `sbm_move_delta`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(b_i\)</td><td>block of node \(i\); \(B\) blocks</td></tr><tr><td>\(A\)</td><td>multigraph adjacency, \(A_{ij}\) edges between \(i\) and \(j\)</td></tr><tr><td>\(e_{rs}\)</td><td>number of edges between blocks \(r\) and \(s\)</td></tr><tr><td>\(k_i\)</td><td>degree of node \(i\)</td></tr><tr><td>\(n_r\)</td><td>size of block \(r\)</td></tr><tr><td>\(b'\)</td><td>the partition after moving one node to another block</td></tr></tbody></table></div>

## Definition {#concept-definition}

SBM move delta. Entries grouped here: Sbm move delta.

*Definition partly written:* Depends on the description length, whose closed forms are not written here (see sbm\_description\_length).

<div class="formula-block"><p class="formula-name"><strong>Description length (Peixoto 2017; degree correction after Karrer and Newman 2011)</strong> <span class="applies">applies to: any, multigraph</span></p><div class="formula">\[\Sigma(A,b)=-\ln P(A\mid e,b)-\ln P(e)-\ln P(b)\quad\bigl[-\ln P(k\mid e,b)\ \text{added, with }P(A\mid k,e,b),\ \text{for the degree-corrected model}\bigr]\]</div><p class="formula-where">The negative log of the joint probability of the network, the block edge counts, the partition and (degree-corrected) the degrees, with the microcanonical Bayesian priors of the paper; it is in nats. The components are reported separately: adjacency, partition, edges, degrees. The closed forms of the components are in the paper and are not transcribed here.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Move delta</strong> <span class="applies">applies to: any, multigraph</span></p><div class="formula">\[\Delta=\Sigma(A,b')-\Sigma(A,b)\]</div><p class="formula-where">The change of the description length when one node moves to another block (or to a new block); it can be evaluated from the counts that change, but equals this difference by definition. A negative value favours the move.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#sbm_move_delta">Sbm move delta</a></td><td><code>sbm_move_delta</code></td><td>1</td><td>Description length after the move minus before it.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/graphtool.html">graph-tool</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">No node can move in a network of fewer than two nodes.</td><td><span class="st st-w st-nov" title="The oracle script does not run graph-tool on a network of fewer than two nodes.">no value</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li><strong>graph-tool</strong>: no value. The oracle script does not run graph-tool on a network of fewer than two nodes. <em>(conventions.json sbm_move_delta)</em></li></ul></details></div>

## Sbm move delta {#sbm_move_delta}

Measure id: `sbm_move_delta`. Original family: Statistical fitting.

**Definition.** Sbm move delta.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>sbm_move_delta_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_dc_b1</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr><tr><td><code>sbm_move_delta_dc_b3</code></td><td>graph-tool</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>graph-tool entropy of the partition after the move minus before</code></td><td>The oracle script does not run graph-tool on a network of fewer than two nodes (no node to move, a one-block partition of one node).</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/sbm.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/sbm.yaml); [harness/golden/graphtool/](https://github.com/knapply/net-oracles/tree/main/harness/golden/graphtool/)

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
