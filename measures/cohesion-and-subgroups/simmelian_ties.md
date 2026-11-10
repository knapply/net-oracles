---
title: "Simmelian ties"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Simmelian ties {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Relaxed cliques and subgroups. Concept id: `simmelian_ties`. 1 measure.

## Definition {#concept-definition}

Simmelian ties. Entries grouped here: Simmelian ties.

*Definition not yet written.* Documented only (ergm, sna and UCINET Simmelian ties), never run; the sources give the name and the tool's function, not a formula, and no verified bibliography entry for the original definition is available.

## Simmelian ties {#simmelian}

Measure id: `simmelian`. Original family: Cohesion and subgroups.

**Definition.** Simmelian ties.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simmelian-sna">details</a></td><td><code>simmelian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ergm.html">ergm (statnet)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simmelian-ergm">details</a></td><td><code>simmelian</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-simmelian-ucinet">details</a></td><td><code>bowtie</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-simmelian-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: simmelian.
- <a id="why-simmelian-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: simmelian.
- <a id="why-simmelian-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [hunter2008ergm](../../references.html#hunter2008ergm)
{% endraw %}
