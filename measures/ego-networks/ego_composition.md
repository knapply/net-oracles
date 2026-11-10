---
title: "Ego composition and heterogeneity"
layout: default
parent: "Ego networks"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Ego composition and heterogeneity {#concept-top}

Family: [Ego networks](index.html). Subfamily: Ego measures. Concept id: `ego_composition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(A_v\)</td><td>set of alters of ego \(v\), with \(|A_v|=s\)</td></tr><tr><td>\(p_c\)</td><td>share of alters in category \(c\) of a categorical attribute: \(|\{u\in A_v: x_u=c\}|/s\)</td></tr><tr><td>\(K\)</td><td>number of categories</td></tr></tbody></table></div>

## Definition {#concept-definition}

Ego composition and heterogeneity. Entries grouped here: Ego composition: alter shares, Blau and Shannon heterogeneity, IQV.

*Definition partly written:* Documented only (egor, UCINET), never run. Formulas for alter shares, the Blau index and Shannon entropy are the standard definitions; the measure's own variants (index of qualitative variation normalisation, handling of missing attribute values) are not recorded in the sources.

<div class="formula-block"><p class="formula-name"><strong>Blau heterogeneity</strong> <span class="applies">applies to: any</span></p><div class="formula">\[H_{\mathrm{Blau}}=1-\sum_{c=1}^{K}p_c^2\]</div><p class="formula-where">Probability that two randomly drawn alters (with replacement) are in different categories; needs \(s\ge1\).</p></div>

<div class="formula-block"><p class="formula-name"><strong>Shannon heterogeneity</strong> <span class="applies">applies to: any</span></p><div class="formula">\[H_{\mathrm{Shannon}}=-\sum_{c:\,p_c&gt;0}p_c\ln p_c\]</div><p class="formula-where">Entropy of the alter composition; 0 for a single category.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Index of qualitative variation</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{IQV}=\frac{1-\sum_c p_c^2}{1-1/K}\]</div><p class="formula-where">Blau index divided by its maximum \(1-1/K\); needs \(K\ge2\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#ego_composition">Ego composition: alter shares, Blau and Shannon heterogeneity, IQV</a></td><td><code>ego_composition</code></td><td>2</td><td>The alter category shares \(p_c\) and the three heterogeneity indices above, computed for one categorical attribute of the alters.</td></tr></tbody></table></div>

## Ego composition: alter shares, Blau and Shannon heterogeneity, IQV {#ego_composition}

Measure id: `ego_composition`. Original family: Ego networks.

**Definition.** Ego composition: alter shares, Blau and Shannon heterogeneity, IQV.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-ego_composition-ucinet">details</a></td><td></td><td>published documentation</td></tr><tr><td><a href="../../tools/egor.html">egor</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's documentation; no comparison set up for this measure yet. <a href="#why-ego_composition-egor">details</a></td><td></td><td>documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ego_composition-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-ego_composition-egor"></a>**[egor](../../tools/egor.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. egor 1.25.10 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_egor](../../references.html#tool_egor)
{% endraw %}
