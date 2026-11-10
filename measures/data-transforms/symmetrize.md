---
title: "Symmetrize"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Symmetrize {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `symmetrize`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X=(x_{uv})\)</td><td>square matrix, possibly asymmetric</td></tr><tr><td>\(Y=(y_{uv})\)</td><td>symmetrized matrix, \(y_{uv}=y_{vu}\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Symmetrize. Entries grouped here: Full symmetrize method set and dichotomize by density; Symmetrise.

*Definition partly written:* Methods are written from the names in the documented entries without a cited source; which methods each tool offers, and the default, are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Maximum (union, 'or')</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y_{uv}=\max(x_{uv},x_{vu})\]</div><p class="formula-where">Keeps a tie if present in either direction.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Minimum (intersection, 'and', strong)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y_{uv}=\min(x_{uv},x_{vu})\]</div><p class="formula-where">Keeps a tie only if reciprocated.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Sum</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y_{uv}=x_{uv}+x_{vu}\]</div><p class="formula-where">Adds the two directions.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Mean</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y_{uv}=\tfrac12(x_{uv}+x_{vu})\]</div><p class="formula-where">Averages the two directions.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Upper or lower triangle</strong> <span class="applies">applies to: any</span></p><div class="formula">\[y_{uv}=x_{\min(u,v),\max(u,v)}\ \text{or}\ x_{\max(u,v),\min(u,v)}\]</div><p class="formula-where">Copies one triangle onto the other; depends on the node order.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#symmetrize_methods">Full symmetrize method set and dichotomize by density</a></td><td><code>symmetrize_methods</code></td><td>3</td><td>Collective entry for the full method set of a documented tool, with dichotomization by density.</td></tr><tr><td><a href="#cat_symmetrise">Symmetrise</a></td><td><code>cat_symmetrise</code></td><td>1</td><td>Symmetrization as listed by another documented tool; method not specified in the sources.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ergm.html">ergm (statnet)</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/tnet.html">tnet</a></th></tr></thead><tbody><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">The diagonal satisfies \(y_{uu}=x_{uu}\) for max, min and mean, and \(2x_{uu}\) for the sum.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="How edge weights enter: as lengths (costs) in path measures, as strengths (capacities, tie intensities) in degree, flow and spectral measures, or ignored."><strong>Edge weights</strong></td><td class="def">Max, min, sum and mean differ on valued data; on 0/1 data max is 'or' and min is 'and'.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Only asymmetric input is changed; a symmetric matrix is unchanged by max, min and mean.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edge weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Full symmetrize method set and dichotomize by density {#symmetrize_methods}

Measure id: `symmetrize_methods`. Original family: Data transforms.

**Definition.** Full symmetrize method set and dichotomize by density.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-symmetrize_methods-sna">details</a></td><td><code>symmetrize</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-symmetrize_methods-ergm">details</a></td><td><code>Symmetrize</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-symmetrize_methods-ucinet">details</a></td><td><code>Symmetrize</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-symmetrize_methods-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: symmetrize.
- <a id="why-symmetrize_methods-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: Symmetrize.
- <a id="why-symmetrize_methods-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [hunter2008ergm](../../references.html#hunter2008ergm)

## Symmetrise {#cat_symmetrise}

Measure id: `cat_symmetrise`. Original family: Graph theory and combinatorics.

**Definition.** Symmetrise.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_symmetrise-tnet">details</a></td><td><code>symmetrise_w</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_symmetrise-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: symmetrise\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
