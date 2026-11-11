---
title: "Core-periphery (continuous)"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Core-periphery (continuous) {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Core-periphery. Concept id: `core_periphery_continuous`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(a_{ij}\)</td><td>1 if there is a tie between \(i\) and \(j\), else 0 (symmetric)</td></tr><tr><td>\(c_i\in[0,1]\)</td><td>coreness of node \(i\)</td></tr><tr><td>\(\delta_{ij}=c_ic_j\)</td><td>the ideal tie pattern for the coreness vector</td></tr></tbody></table></div>

## Definition {#concept-definition}

Continuous core-periphery fit: a coreness score per node by MINRES or by correlation with the pattern c\_i c\_j.

<div class="formula-block"><p class="formula-name"><strong>Continuous core-periphery fit (Borgatti and Everett 1999)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\rho(c)=\mathrm{corr}\bigl((a_{ij})_{i&lt;j},(c_ic_j)_{i&lt;j}\bigr),\qquad c^\star=\arg\max_{c}\rho(c)\]</div><p class="formula-where">Coreness is chosen to maximize the Pearson correlation between observed ties and the pattern \(c_ic_j\) over distinct pairs. The correlation is 0/0 when the ties or the pattern are constant (an empty or complete graph, or constant \(c\)).</p></div>

<div class="formula-block"><p class="formula-name"><strong>MINRES coreness (Comrey 1962; Boyd, Fitzgerald and Beck 2010)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[c^\star=\arg\min_{c}\sum_{i&lt;j}\bigl(a_{ij}-c_ic_j\bigr)^2\]</div><p class="formula-where">Least-squares fit of the rank-one pattern to the off-diagonal adjacency entries; unique up to sign, with the sign fixed by non-negativity.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#core_periphery_continuous">Core periphery continuous</a></td><td><code>core_periphery_continuous</code></td><td>2</td><td>A coreness score per node, by the MINRES fit or by maximum correlation with the pattern \(c_ic_j\); the score is up to the scaling of \(c\) fixed by the solver.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/cpnet.html">cpnet</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Constant ties: the correlation is 0/0 and MINRES gives \(c=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Fewer than three nodes: fewer than three pairs to fit.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">Constant ties: correlation 0/0; the least-squares solution is \(c_i=1\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir).">agrees</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal coreness values are possible; the optimum is not unique when the matrix has a repeated leading eigenvalue (symmetric structures).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Complete graph</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (complete6, complete5_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Ties and equal values</summary><ul><li><strong>cpnet</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, kite, les_miserables). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## References {#concept-references}

[borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

## Core periphery continuous {#core_periphery_continuous}

Measure id: `core_periphery_continuous`. Original family: Roles and positions.

**Definition.** Continuous core-periphery fit: a coreness score per node by MINRES or by correlation with the pattern c\_i c\_j.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-core_periphery_continuous-ucinet">details</a></td><td><code>contcp</code></td><td>published documentation</td></tr><tr><td><a href="../../tools/cpnet.html">cpnet</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-core_periphery_continuous-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>core_periphery_minres_vs_cpnet</code></td><td>cpnet</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-09, rel 1e-09</td><td><code>smallest residual sum of squares sum (a_ij - c_i c_j)^2 over the coreness vectors of cpnet.MINRES, Rombach and Rossa (those installed)</code></td><td></td></tr></tbody></table></div>

**Harness files:** [harness/manifest/groups.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/groups.yaml); [harness/golden/cpnet/](https://github.com/knapply/net-oracles/tree/main/harness/golden/cpnet/)

**References:** [borgatti1999models](../../references.html#borgatti1999models), [boyd2010computing](../../references.html#boyd2010computing), [comrey1962minimum](../../references.html#comrey1962minimum), [nocedal2006numerical](../../references.html#nocedal2006numerical)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [tool_cpnet](../../references.html#tool_cpnet)
{% endraw %}
