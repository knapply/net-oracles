---
title: "Walk-based index components"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Walk-based index components {#concept-top}

Family: [Centrality](index.html). Subfamily: Walk-based and distance-based indices (netrankr). Concept id: `walk_indices`. 6 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(A\)</td><td>adjacency matrix: \(A_{uv}\) is the number (or total weight) of edges from \(u\) to \(v\)</td></tr><tr><td>\(\alpha\)</td><td>weighting factor</td></tr><tr><td>\(k\)</td><td>maximum walk length</td></tr></tbody></table></div>

## Definition {#concept-definition}

Walk-based index components. Entries grouped here: Walks attenuated; Walks exp; Walks exp even; Walks exp odd; Walks limit prop; Walks uptok.

*Definition partly written:* The limit-proportion transformation is described by its documentation sentence only.

<div class="formula-block"><p class="formula-name"><strong>Walk-based relations</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\sum_{k\ge0}\frac{(\alpha A)^k}{k!},\qquad \sum_{k\ge0}\frac{(\alpha A)^{2k}}{(2k)!},\qquad \sum_{k\ge0}\frac{(\alpha A)^{2k+1}}{(2k+1)!}\]</div><p class="formula-where">Exponential, even and odd exponential walk sums (communicability and its even and odd parts); computed from the eigendecomposition \(f(A)=Xf(\Lambda)X^{\mathsf T}\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Attenuated and truncated walks</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\sum_{k\ge0}\alpha^kA^k=(I-\alpha A)^{-1},\qquad \sum_{j=0}^{k}\alpha^jA^j\]</div><p class="formula-where">All-length attenuated walks (Katz-type; needs \(\alpha&lt;1/\lambda_1\), documented default \(0.99/\max A\)) and walks up to length \(k\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_attenuated_walk">Walks attenuated</a></td><td><code>cat_attenuated_walk</code></td><td>1</td><td>Attenuated walks \((I-\alpha A)^{-1}\).</td></tr><tr><td><a href="#cat_exp_walk">Walks exp</a></td><td><code>cat_exp_walk</code></td><td>1</td><td>Exponential walk sum.</td></tr><tr><td><a href="#cat_even_exp_walk">Walks exp even</a></td><td><code>cat_even_exp_walk</code></td><td>1</td><td>Even-length exponential walk sum.</td></tr><tr><td><a href="#cat_exp_odd_walk">Walks exp odd</a></td><td><code>cat_exp_odd_walk</code></td><td>1</td><td>Odd-length exponential walk sum.</td></tr><tr><td><a href="#cat_limit_prop_walk">Walks limit prop</a></td><td><code>cat_limit_prop_walk</code></td><td>1</td><td>Limit proportion of walks between pairs; the documentation gives no formula and states that its row sums give the principal eigenvector.</td></tr><tr><td><a href="#cat_uptok_walk">Walks uptok</a></td><td><code>cat_uptok_walk</code></td><td>1</td><td>Walks up to length \(k\).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All relations reduce to the identity (or zero off the diagonal).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The diagonal of \(A\) enters all walk sums.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">\(A\) counts parallel edges as larger entries.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An undirected graph with more than one connected component, or a directed graph that is not weakly connected: some pairs of nodes have no path."><strong>Disconnected graph</strong></td><td class="def">Entries between components are 0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(\alpha\ge1/\lambda_1\) makes the attenuated sum diverge.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Disconnected graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Walks attenuated {#cat_attenuated_walk}

Measure id: `cat_attenuated_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks attenuated.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_attenuated_walk-netrankr">details</a></td><td><code>walks_attenuated</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attenuated_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_attenuated.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Walks exp {#cat_exp_walk}

Measure id: `cat_exp_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks exp.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_exp_walk-netrankr">details</a></td><td><code>walks_exp</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_exp_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_exp.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Walks exp even {#cat_even_exp_walk}

Measure id: `cat_even_exp_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks exp even.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_even_exp_walk-netrankr">details</a></td><td><code>walks_exp_even</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_even_exp_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_exp\_even.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Walks exp odd {#cat_exp_odd_walk}

Measure id: `cat_exp_odd_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks exp odd.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_exp_odd_walk-netrankr">details</a></td><td><code>walks_exp_odd</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_exp_odd_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_exp\_odd.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Walks limit prop {#cat_limit_prop_walk}

Measure id: `cat_limit_prop_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks limit prop.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_limit_prop_walk-netrankr">details</a></td><td><code>walks_limit_prop</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_limit_prop_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_limit\_prop.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Walks uptok {#cat_uptok_walk}

Measure id: `cat_uptok_walk`. Original family: Graph theory and combinatorics.

**Definition.** Walks uptok.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_uptok_walk-netrankr">details</a></td><td><code>walks_uptok</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_uptok_walk-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: walks\_uptok.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
