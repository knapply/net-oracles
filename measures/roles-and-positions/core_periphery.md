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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(a_{ij}\)</td><td>1 if there is a tie between \(i\) and \(j\), else 0</td></tr><tr><td>\(c_i\in\{0,1\}\)</td><td>core (1) or periphery (0) membership</td></tr><tr><td>\(\delta_{ij}=c_ic_j\)</td><td>ideal pattern: ties exactly between pairs of core nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Discrete core-periphery fit: the core membership that best matches the ideal pattern, by tabu search from random starts.

*Definition partly written:* core\_periphery\_en (the Estevez-Nordlund variant) is documented only (UCINET), never run, and its definition is not recorded in the sources.

<div class="formula-block"><p class="formula-name"><strong>Discrete core-periphery fit (Borgatti and Everett 1999)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\rho(c)=\mathrm{corr}\bigl((a_{ij})_{i&lt;j},(c_ic_j)_{i&lt;j}\bigr),\qquad c^\star=\arg\max_{c\in\{0,1\}^n}\rho(c)\]</div><p class="formula-where">The membership vector with the best match to the ideal pattern, found by a heuristic search (tabu search, Glover 1989, from random starts), so the optimum is not guaranteed and tied optima depend on the starts. The correlation is 0/0 when ties or pattern are constant.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#core_periphery">Core periphery</a></td><td><code>core_periphery</code></td><td>3</td><td>The discrete membership vector that best matches the ideal pattern, found by tabu search from random starts, together with its fit \(\rho\).</td></tr><tr><td><a href="#core_periphery_en">Estevez-Nordlund variant</a></td><td><code>core_periphery_en</code></td><td>1</td><td>Documented as the Estevez-Nordlund variant (UCINET); the definition is not recorded in the sources.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/bct.html">BCT (Octave)</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/cpnet.html">cpnet</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Constant ties: the correlation is 0/0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">With fewer than three nodes there are too few pairs to distinguish a core.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Constant ties: correlation 0/0; every node can be core.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Several memberships can attain the same fit, and a swap of the labels core and periphery changes the pattern; heuristic search returns one of them.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The number of starts and the stopping rule of the search are parameters of the procedure, not of the definition.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

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
