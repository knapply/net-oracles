---
title: "Circulant and ring graphs (ladder, chordal, Petersen, Harary)"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Circulant and ring graphs (ladder, chordal, Petersen, Harary) {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Named and deterministic graphs. Concept id: `circulant_ring_graphs`. 9 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(n\)</td><td>number of nodes</td></tr><tr><td>\(S\)</td><td>set of offsets</td></tr></tbody></table></div>

## Definition {#concept-definition}

Circulant and ring graphs (ladder, chordal, Petersen, Harary). Entries grouped here: Chordal cycle graph; Chordal ring generator; Circulant graph generator; Circular ladder graph; Generalized petersen graph; Generalized Petersen graph generator; and 3 more.

*Definition partly written:* No primary paper was checked for the circulant, chordal ring, Harary and generalized Petersen definitions; formulas are not written. NetworkX was run on small cases but the comparison records no counts, so no tool value is stated.

<div class="formula-block"><p class="formula-name"><strong>Circulant graph</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[i\sim j\iff (i-j)\bmod n\in S\cup(-S)\]</div><p class="formula-where">Nodes on a cycle, an edge joins nodes whose cyclic distance is in the offset set; \(S\subseteq\{1,\dots,\lfloor n/2\rfloor\}\). Standard definition; no primary paper was checked.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gen_circulant">Circulant graph generator</a></td><td><code>gen_circulant</code></td><td>2</td><td>The circulant graph with offset set \(S\) above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/rustworkx.html">rustworkx</a></th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="The graph has exactly two nodes."><strong>Two nodes</strong></td><td class="def">Cyclic offsets of a 2-cycle coincide; whether the single edge is doubled is not fixed by the definition.</td><td><span class="nr" title="NetworkX 3.7 was run on the pair fixture but the comparison records no counts, so the outcome is not stated.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Two nodes</summary><ul><li><strong>NetworkX</strong>: not recorded. NetworkX 3.7 was run on the pair fixture but the comparison records no counts, so the outcome is not stated. <em>(reasons.json circulant_ring_graphs)</em></li></ul></details></div>

## Chordal cycle graph {#cat_chordal_cycle}

Measure id: `cat_chordal_cycle`. Original family: Generators and rewiring.

**Definition.** Chordal cycle graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_chordal_cycle-networkx">details</a></td><td><code>chordal_cycle_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_chordal_cycle-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: chordal\_cycle\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Chordal ring generator {#gen_chordal_ring}

Measure id: `gen_chordal_ring`. Original family: Generators and rewiring.

**Definition.** Chordal ring generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_chordal_ring-igraph">details</a></td><td><code>chordal_ring; make_chordal_ring</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_chordal_ring-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: chordal\_ring; make\_chordal\_ring.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Circulant graph generator {#gen_circulant}

Measure id: `gen_circulant`. Original family: Generators and rewiring.

**Definition.** Circulant graph generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_circulant-networkx">details</a></td><td><code>circulant_graph</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_circulant-igraph">details</a></td><td><code>circulant; make_circulant</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_circulant-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: circulant\_graph.
- <a id="why-gen_circulant-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: circulant; make\_circulant.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Circular ladder graph {#cat_circular_ladder}

Measure id: `cat_circular_ladder`. Original family: Generators and rewiring.

**Definition.** Circular ladder graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_circular_ladder-networkx">details</a></td><td><code>circular_ladder_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_circular_ladder-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: circular\_ladder\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generalized petersen graph {#cat_generalized_petersen}

Measure id: `cat_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized petersen graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generalized_petersen-networkx">details</a></td><td><code>generalized_petersen_graph</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generalized_petersen-rustworkx">details</a></td><td><code>generalized_petersen_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generalized_petersen-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generalized\_petersen\_graph.
- <a id="why-cat_generalized_petersen-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: generalized\_petersen\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Generalized Petersen graph generator {#gen_generalized_petersen}

Measure id: `gen_generalized_petersen`. Original family: Generators and rewiring.

**Definition.** Generalized Petersen graph generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_generalized_petersen-jgrapht">details</a></td><td><code>GeneralizedPetersenGraphGenerator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_generalized_petersen-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GeneralizedPetersenGraphGenerator.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Hkn harary graph {#cat_harary_hkn}

Measure id: `cat_harary_hkn`. Original family: Generators and rewiring.

**Definition.** Hkn harary graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_harary_hkn-networkx">details</a></td><td><code>hkn_harary_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_harary_hkn-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: hkn\_harary\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Hnm harary graph {#cat_harary_hnm}

Measure id: `cat_harary_hnm`. Original family: Generators and rewiring.

**Definition.** Hnm harary graph.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_harary_hnm-networkx">details</a></td><td><code>hnm_harary_graph</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_harary_hnm-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: hnm\_harary\_graph.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Implicit family {#implicit_family}

Measure id: `implicit_family`. Original family: Graph theory and combinatorics.

**Definition.** Implicit family.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a></td><td>Checked, no comparison counts recorded for this entry. <em>(reason incomplete)</em> <a href="#why-implicit_family-networkx">details</a></td><td></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-implicit_family-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-nov" href="../../method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> NetworkX 3.7 was run for this measure, but the survey's comparison report records no comparison counts (neither agreeing nor differing) for the entry, so the inputs on which the tool gives no value, and why, cannot be stated from the sources. What the sources do say: the cases are fixed and do not use the fixture graph; one fixture carries them. The comparison is restricted to the fixture(s): pair. Findings: [F034](../../findings.html#f034). **Reason incomplete:** The sources record no comparison counts (agreeing or differing) for this entry, so the inputs on which the tool gives no value, and why, cannot be stated.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>implicit_circulant</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.circulant_graph(n, offsets)</code></td><td></td></tr><tr><td><code>implicit_complete_bipartite</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.complete_bipartite_graph(a, b)</code></td><td></td></tr><tr><td><code>implicit_complete_bipartite_dir</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.complete_bipartite_graph(a, b), oriented from the first part</code></td><td></td></tr><tr><td><code>implicit_complete_multipartite</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.complete_multipartite_graph(*sizes)</code></td><td></td></tr><tr><td><code>implicit_de_bruijn</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>iterated nx.line_graph of the complete digraph with loops</code></td><td></td></tr><tr><td><code>implicit_hypercube</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.hypercube_graph(d), tuple read as an integer</code></td><td></td></tr><tr><td><code>implicit_kautz</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>iterated nx.line_graph of the complete digraph</code></td><td></td></tr><tr><td><code>implicit_path</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.path_graph(n)</code></td><td></td></tr><tr><td><code>implicit_path_dir</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.path_graph(n, create_using=nx.DiGraph)</code></td><td></td></tr><tr><td><code>implicit_star</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.star_graph(n)</code></td><td></td></tr><tr><td><code>implicit_wheel</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.wheel_graph(n)</code></td><td></td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f034">F034</a></td><td>NetworkX</td><td>convention</td><td>hypercube_graph nodes are bit tuples; dimension 0 is the null graph</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
