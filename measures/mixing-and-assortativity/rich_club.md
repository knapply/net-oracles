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

## Definition {#concept-definition}

Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#rich_club">Rich club</a></td><td><code>rich_club</code></td><td>2</td></tr><tr><td><a href="#cat_richclub_weighted">Weighted richclub</a></td><td><code>cat_richclub_weighted</code></td><td>1</td></tr><tr><td><a href="#cat_local_richclub_weighted">Weighted richclub local</a></td><td><code>cat_local_richclub_weighted</code></td><td>1</td></tr></tbody></table></div>

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
