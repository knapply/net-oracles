---
title: "Distance transformations for indices"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Distance transformations for indices {#concept-top}

Family: [Centrality](index.html). Subfamily: Walk-based and distance-based indices (netrankr). Concept id: `distance_transform_indices`. 5 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(x\)</td><td>a relation value such as a distance \(d(u,v)\)</td></tr><tr><td>\(\alpha\)</td><td>tuning parameter</td></tr></tbody></table></div>

## Definition {#concept-definition}

Distance transformations for indices. Entries grouped here: Dist 2pow; Dist dpow; Dist inv; Dist powd; Swan combinatory.

*Definition partly written:* Swan's combinatory transformation is described by name only.

<div class="formula-block"><p class="formula-name"><strong>Transformations of a distance relation</strong> <span class="applies">applies to: any</span></p><div class="formula">\[f_{2^{-x}}(x)=2^{-x},\quad f_{\mathrm{inv}}(x)=\frac1x,\quad f_{\mathrm{dpow}}(x)=x^{-\alpha},\quad f_{\mathrm{powd}}(x)=\alpha^{x}\]</div><p class="formula-where">Applied entry by entry to a distance matrix; the index of a node is then the row sum of the transformed relation (aggregation). The documentation gives \(\alpha&gt;0\) for the power of the distance and \(0&lt;\alpha&lt;1\) for the power with the distance as exponent; \(1/x\) gives harmonic centrality and \(2^{-x}\) residual closeness.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_2pow_dist">Dist 2pow</a></td><td><code>cat_2pow_dist</code></td><td>1</td><td>\(2^{-x}\).</td></tr><tr><td><a href="#cat_dist_dpow">Dist dpow</a></td><td><code>cat_dist_dpow</code></td><td>1</td><td>\(x^{-\alpha}\) (default \(\alpha=1\)).</td></tr><tr><td><a href="#cat_dist_inv">Dist inv</a></td><td><code>cat_dist_inv</code></td><td>1</td><td>\(1/x\).</td></tr><tr><td><a href="#cat_dist_powd">Dist powd</a></td><td><code>cat_dist_powd</code></td><td>1</td><td>\(\alpha^{x}\) (default \(\alpha=0.5\)).</td></tr><tr><td><a href="#cat_combinatory_swan">Swan combinatory</a></td><td><code>cat_combinatory_swan</code></td><td>1</td><td>Swan's combinatory transformation: the formula is not stated in the sources read.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">\(1/x\) and \(x^{-\alpha}\) are undefined at \(x=0\): the diagonal and zero distances need a rule.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Infinite distances map to 0 under all four transformations, which is why they stay defined on disconnected graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha&gt;0\) for \(x^{-\alpha}\); \(0&lt;\alpha&lt;1\) for \(\alpha^x\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Dist 2pow {#cat_2pow_dist}

Measure id: `cat_2pow_dist`. Original family: Graph theory and combinatorics.

**Definition.** Dist 2pow.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_2pow_dist-netrankr">details</a></td><td><code>dist_2pow</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_2pow_dist-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: dist\_2pow.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Dist dpow {#cat_dist_dpow}

Measure id: `cat_dist_dpow`. Original family: Graph theory and combinatorics.

**Definition.** Dist dpow.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dist_dpow-netrankr">details</a></td><td><code>dist_dpow</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dist_dpow-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: dist\_dpow.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Dist inv {#cat_dist_inv}

Measure id: `cat_dist_inv`. Original family: Graph theory and combinatorics.

**Definition.** Dist inv.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dist_inv-netrankr">details</a></td><td><code>dist_inv</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dist_inv-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: dist\_inv.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Dist powd {#cat_dist_powd}

Measure id: `cat_dist_powd`. Original family: Graph theory and combinatorics.

**Definition.** Dist powd.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dist_powd-netrankr">details</a></td><td><code>dist_powd</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dist_powd-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: dist\_powd.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Swan combinatory {#cat_combinatory_swan}

Measure id: `cat_combinatory_swan`. Original family: Graph theory and combinatorics.

**Definition.** Swan combinatory.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_combinatory_swan-netrankr">details</a></td><td><code>swan_combinatory</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_combinatory_swan-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: swan\_combinatory.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
