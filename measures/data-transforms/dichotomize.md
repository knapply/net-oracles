---
title: "Dichotomize"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dichotomize {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `dichotomize`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(X=(x_{uv})\)</td><td>valued relation</td></tr><tr><td>\(B=(b_{uv})\)</td><td>binary relation</td></tr><tr><td>\(c\)</td><td>cutoff</td></tr><tr><td>\(\mathrm{op}\)</td><td>comparison: \(\ge,&gt;,\le,&lt;,=\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Dichotomize. Entries grouped here: Dichotomise; Dichotomize.

*Definition partly written:* The tool entries are documented only; the default cutoff and comparison of each tool are not recorded.

<div class="formula-block"><p class="formula-name"><strong>Dichotomization of a valued relation (Wasserman and Faust 1994)</strong> <span class="applies">applies to: weighted</span></p><div class="formula">\[b_{uv}=\begin{cases}1&amp;x_{uv}\ \mathrm{op}\ c\\0&amp;\text{otherwise}\end{cases}\]</div><p class="formula-where">A valued tie is kept as a 1 when it passes the cutoff and dropped otherwise; the choice of \(c\) and of \(\mathrm{op}\) changes the network and is a modelling decision.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_dichotomise">Dichotomise</a></td><td><code>cat_dichotomise</code></td><td>1</td><td>Threshold rule \(b_{uv}=\mathbb 1[x_{uv}\ \mathrm{op}\ c]\) applied entry by entry; the comparison and the cutoff \(c\) are parameters. This is the British spelling of the procedure in a documented tool.</td></tr><tr><td><a href="#cat_dichotomize">Dichotomize</a></td><td><code>cat_dichotomize</code></td><td>1</td><td>Threshold rule \(b_{uv}=\mathbb 1[x_{uv}\ \mathrm{op}\ c]\) applied entry by entry; the comparison and the cutoff \(c\) are parameters. This is the American spelling of the procedure in a documented tool.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/tnet.html">tnet</a></th></tr></thead><tbody><tr><td title="Edges with weight 0."><strong>Zero weights</strong></td><td class="def">A zero value passes the cutoff only when \(c\) and \(\mathrm{op}\) allow it, such as \(x\ge0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Edges with a negative weight."><strong>Negative weights</strong></td><td class="def">Negative values pass \(x\le c\) or \(x&lt;c\) but not \(x&gt;0\); the rule has no special case.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Any real \(c\) is allowed; a \(c\) beyond the range of the data gives an empty or a complete relation.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Zero weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Negative weights</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Dichotomise {#cat_dichotomise}

Measure id: `cat_dichotomise`. Original family: Data transforms.

**Definition.** Dichotomise.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/tnet.html">tnet</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dichotomise-tnet">details</a></td><td><code>dichotomise_tm; dichotomise_w</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomise-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: dichotomise\_tm; dichotomise\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Dichotomize {#cat_dichotomize}

Measure id: `cat_dichotomize`. Original family: Data transforms.

**Definition.** Dichotomize.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_dichotomize-ucinet">details</a></td><td><code>Dichotomize</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dichotomize-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
