---
title: "Regular equivalence (REGE, CATREGE)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Regular equivalence (REGE, CATREGE) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Equivalence and clustering. Concept id: `regular_equivalence`. 2 measures.

## Definition {#concept-definition}

Regular equivalence (REGE, CATREGE). Entries grouped here: Regular equivalence; Automorphic (Max Sim) and regular equivalence (REGE, CATREGE).

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#regular_equivalence">Regular equivalence</a></td><td><code>regular_equivalence</code></td><td>3</td></tr><tr><td><a href="#cat_automorphic_catrege_equivalence_max_rege_regular_sim">Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)</a></td><td><code>cat_automorphic_catrege_equivalence_max_rege_regular_sim</code></td><td>1</td></tr></tbody></table></div>

## Regular equivalence {#regular_equivalence}

Measure id: `regular_equivalence`. Original family: Roles and positions.

**Definition.** Regular equivalence.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>redist</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-regular_equivalence-ucinet">details</a></td><td></td><td>published documentation</td></tr><tr><td><a href="../../tools/blockmodeling.html">blockmodeling</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-regular_equivalence-blockmodeling">details</a></td><td><code>REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-regular_equivalence-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-regular_equivalence-blockmodeling"></a>**[blockmodeling](../../tools/blockmodeling.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. blockmodeling 1.1.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package blockmodeling: exported functions and help titles); API names: REGD.for; REGD.ne.for; REGD.ow.for; REGE; REGE.FC; REGE.FC.ow; REGE.for; REGE.ne.for; REGE.nm.diag.for; REGE.nm.for; REGE.nm.ne.for; REGE.ow.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>regular_equivalence</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>classes at distance 0 in sna::redist(m, method = 'catrege')</code></td><td>sna fails on a network with a single node.</td></tr><tr><td><code>regular_equivalence_seed</code></td><td>sna</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sna::redist(m, method = 'catrege', seed.partition = v %% 3), distance 0</code></td><td>sna fails on a network with a single node.</td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [ziberna2007generalized](../../references.html#ziberna2007generalized)

## Automorphic (Max Sim) and regular equivalence (REGE, CATREGE) {#cat_automorphic_catrege_equivalence_max_rege_regular_sim}

Measure id: `cat_automorphic_catrege_equivalence_max_rege_regular_sim`. Original family: Roles and positions.

**Definition.** Automorphic (Max Sim) and regular equivalence (REGE, CATREGE).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-cat_automorphic_catrege_equivalence_max_rege_regular_sim-ucinet">details</a></td><td><code>Automorphic (MaxSim) and regular equivalence (REGE, CATREGE)</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_automorphic_catrege_equivalence_max_rege_regular_sim-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
