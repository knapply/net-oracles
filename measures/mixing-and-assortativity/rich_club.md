---
title: "Rich club"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Rich club {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Rich club. Concept id: `rich_club`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(k_i\)</td><td>degree of node \(i\)</td></tr><tr><td>\(V_{&gt;k}=\{i:k_i&gt;k\}\)</td><td>the nodes richer than \(k\)</td></tr><tr><td>\(N_{&gt;k}=|V_{&gt;k}|\)</td><td>their number</td></tr><tr><td>\(E_{&gt;k}\)</td><td>number of edges among the nodes of \(V_{&gt;k}\)</td></tr><tr><td>\(\phi_{\mathrm{rand}}(k)\)</td><td>average rich-club coefficient of degree-preserving randomizations of the graph (Maslov and Sneppen 2002 rewiring)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

*Definition partly written:* The two weighted variants are documented only (tnet), with no formula in the sources checked.

<div class="formula-block"><p class="formula-name"><strong>Rich-club coefficient (Zhou and Mondragon 2004)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\phi(k)=\frac{2E_{&gt;k}}{N_{&gt;k}(N_{&gt;k}-1)}\]</div><p class="formula-where">Density of the subgraph induced by nodes of degree greater than \(k\). Defined only when \(N_{&gt;k}\ge2\); undirected simple graphs.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Normalized rich-club coefficient (Colizza et al. 2006)</strong> <span class="applies">applies to: undirected, simple, normalized</span></p><div class="formula">\[\rho(k)=\frac{\phi(k)}{\phi_{\mathrm{rand}}(k)}\]</div><p class="formula-where">Ratio to the value in a null model with the same degrees; \(\rho&gt;1\) indicates rich-club ordering. Depends on the randomization (number of rewired graphs and the random draws).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#rich_club">Rich club</a></td><td><code>rich_club</code></td><td>2</td><td>The coefficient \(\phi(k)\) for every degree \(k\), optionally normalized to \(\rho(k)\) by averaging randomizations (the normalized form is stochastic).</td></tr><tr><td><a href="#cat_richclub_weighted">Weighted richclub</a></td><td><code>cat_richclub_weighted</code></td><td>1</td><td>Weighted rich-club coefficient as documented for tnet (not run); the weighted definition is not recorded in the sources.</td></tr><tr><td><a href="#cat_local_richclub_weighted">Weighted richclub local</a></td><td><code>cat_local_richclub_weighted</code></td><td>1</td><td>Weighted local rich-club coefficient as documented for the R package tnet (not run); its definition is not recorded in the sources.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/bct.html">BCT (Octave)</a></th><th><a href="../../tools/tnet.html">tnet</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For \(k\) such that fewer than two nodes have degree above \(k\), the denominator is 0: not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">No node has degree above 0: \(N_{&gt;k}=0\) for every \(k\ge0\): not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The definition is for simple graphs; loops are not edges between two distinct rich nodes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">The definition is for simple graphs; parallel edges are not part of \(E_{&gt;k}\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">\(\phi(k)=1\) whenever \(N_{&gt;k}\ge2\); for the complete graph \(N_{&gt;k}=0\) for \(k\ge n-1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Many nodes share a degree; \(V_{&gt;k}\) is a strict inequality, so ties at the threshold fall outside the club.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The normalized form needs a null-model ensemble; with too few randomizations or an unrewirable graph \(\phi_{\mathrm{rand}}\) can be 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Rich club {#rich_club}

Measure id: `rich_club`. Original family: Generators and rewiring.

**Definition.** Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>rich_club_coefficient</code></td><td></td></tr><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-rich_club-bct">details</a></td><td><code>rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-rich_club-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: rich\_club\_bd; rich\_club\_bu; rich\_club\_wd; rich\_club\_wu.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>rich_club</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.rich_club_coefficient(G, normalized = False); -1 where it raises (self-loops)</code></td><td></td></tr><tr><td><code>rich_club_normalized</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td></td><td>normalization</td><td>abs 0.02, rel 0.1</td><td><code>nx.rich_club_coefficient(G, normalized = True, Q = 20, n_samples = 200, seed = 7); -1 where it raises</code></td><td>as for small_world_sigma (the normalization averages 200 rewired graphs)</td></tr></tbody></table></div>

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Weighted richclub {#cat_richclub_weighted}

Measure id: `cat_richclub_weighted`. Original family: Graph theory and combinatorics.

**Definition.** Weighted richclub.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_richclub_weighted-tnet">details</a></td><td><code>weighted_richclub_tm; weighted_richclub_w</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_richclub_weighted-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: weighted\_richclub\_tm; weighted\_richclub\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Weighted richclub local {#cat_local_richclub_weighted}

Measure id: `cat_local_richclub_weighted`. Original family: Graph theory and combinatorics.

**Definition.** Weighted richclub local.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_local_richclub_weighted-tnet">details</a></td><td><code>weighted_richclub_local_w</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_local_richclub_weighted-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: weighted\_richclub\_local\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
