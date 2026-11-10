---
title: "Core-periphery (discrete)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Core-periphery (discrete) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Core-periphery. Concept id: `core_periphery`. 2 measures.

## Definition {#concept-definition}

Discrete core-periphery fit: the core membership that best matches the ideal pattern, by tabu search from random starts.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#core_periphery">Core periphery</a></td><td><code>core_periphery</code></td><td>3</td></tr><tr><td><a href="#core_periphery_en">Estevez-Nordlund variant</a></td><td><code>core_periphery_en</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [glover1989tabu](../../references.html#glover1989tabu)

## Core periphery {#core_periphery}

Measure id: `core_periphery`. Original family: Roles and positions.

**Definition.** Discrete core-periphery fit: the core membership that best matches the ideal pattern, by tabu search from random starts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/bct.html">BCT (Octave)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-core_periphery-bct">details</a></td><td><code>core_periphery_dir</code></td><td>API listing</td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-core_periphery-ucinet">details</a></td><td><code>Core/periphery: categorical (Borgatti-Everett), continuous coreness, Estevez-Nordlund variant (6.833); catcp</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/cpnet.html">cpnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: core\_periphery\_dir.
- <a id="why-core_periphery-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>core_periphery_ones_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>correlation, core-periphery pairs expected tied, of the core set of cpnet.BE().detect(G)</code></td><td></td></tr><tr><td><code>core_periphery_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>correlation, links 'missing', of the core set of cpnet.BE().detect(G) (undirected, unweighted, no loops)</code></td><td></td></tr><tr><td><code>core_periphery_weighted_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>correlation with weighted values of the core set of cpnet.BE().detect(G) (unweighted)</code></td><td></td></tr><tr><td><code>core_periphery_zeros_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>correlation, core-periphery pairs expected untied, of the core set of cpnet.BE().detect(G)</code></td><td></td></tr></tbody></table></div>

**References:** [borgatti1999models](../../references.html#borgatti1999models), [glover1989tabu](../../references.html#glover1989tabu)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [rubinov2010complex](../../references.html#rubinov2010complex), [tool_cpnet](../../references.html#tool_cpnet)

## Estevez-Nordlund variant {#core_periphery_en}

Measure id: `core_periphery_en`. Original family: Roles and positions.

**Definition.** Estevez-Nordlund variant.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-core_periphery_en-ucinet">details</a></td><td><code>enordcp</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery_en-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
