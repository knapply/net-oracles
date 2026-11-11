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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target</td></tr><tr><td>\(a_{ij}\)</td><td>tie from \(i\) to \(j\) (0 or 1)</td></tr><tr><td>\(\equiv\)</td><td>an equivalence relation on \(V\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Regular equivalence (REGE, CATREGE). Entries grouped here: Regular equivalence; Automorphic (Max Sim) and regular equivalence (REGE, CATREGE).

*Definition partly written:* The UCINET REGE and CATREGE similarity iterations (Borgatti and Everett 1993) and Max Sim are documented only and never run; their update formulas are not recorded in the sources, so only the White-Reitz definition is written.

<div class="formula-block"><p class="formula-name"><strong>Regular equivalence (White and Reitz 1983)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[i\equiv j\Rightarrow\begin{cases}\forall k:\,a_{ik}=1\Rightarrow\exists l:\,a_{jl}=1,\ l\equiv k\\ \forall k:\,a_{ki}=1\Rightarrow\exists l:\,a_{lj}=1,\ l\equiv k\end{cases}\]</div><p class="formula-where">An equivalence relation is regular when equivalent nodes have ties to and from equivalent nodes. The relation is not unique: the coarsest (all nodes) is always regular, so a procedure fixes the one it reports (for example the maximal regular relation refining a seed partition, as the CATREGE iteration yields).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#regular_equivalence">Regular equivalence</a></td><td><code>regular_equivalence</code></td><td>3</td><td>The classes of the regular equivalence found by the tool (sna: classes at distance 0 of the CATREGE dissimilarity, optionally from a seed partition).</td></tr><tr><td><a href="#cat_automorphic_catrege_equivalence_max_rege_regular_sim">Automorphic (Max Sim) and regular equivalence (REGE, CATREGE)</a></td><td><code>cat_automorphic_catrege_equivalence_max_rege_regular_sim</code></td><td>1</td><td>Documented as the UCINET REGE and CATREGE regular-equivalence similarity procedures and Max Sim for automorphic equivalence; not recorded in detail.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/sna.html">sna</a></th><th><a href="../../tools/ucinet.html">UCINET</a></th><th><a href="../../tools/blockmodeling.html">blockmodeling</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No nodes: no relation.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">Every node has no ties: all nodes are regularly equivalent (one class).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One class of one node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop is a tie to a node equivalent to itself and is part of the profile.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Binary ties: multiplicity is ignored.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Both the out-condition and the in-condition apply; undirected ties satisfy them together.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">The relation found is one of several regular relations (the definition does not fix a unique one).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All nodes equivalent.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Centre and leaves form two classes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

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

**Harness files:** [harness/manifest/roles.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/roles.yaml); [harness/golden/sna/](https://github.com/knapply/net-oracles/tree/main/harness/golden/sna/)

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
