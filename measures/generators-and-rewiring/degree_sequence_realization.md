---
title: "Deterministic degree-sequence realization"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Deterministic degree-sequence realization {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Degree-sequence models. Concept id: `degree_sequence_realization`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(d_1\ge\dots\ge d_n\)</td><td>a non-increasing degree sequence</td></tr></tbody></table></div>

## Definition {#concept-definition}

Deterministic degree-sequence realization. Entries grouped here: Bipartite degree-sequence realization; Deterministic realisation of a degree sequence; Havel Hakimi Generator.

*Definition partly written:* Havel-Hakimi and the Erdos-Gallai test are written. The bipartite realization (a Gale-Ryser type condition) and the igraph method options are named only.

<div class="formula-block"><p class="formula-name"><strong>Graphical test (Erdos and Gallai 1960)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\sum_{i=1}^{k}d_i\le k(k-1)+\sum_{i=k+1}^{n}\min(d_i,k)\ \ (k=1..n),\qquad \sum_id_i\ \text{even}\]</div><p class="formula-where">A sequence is the degree sequence of a simple graph exactly when it satisfies this.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Havel-Hakimi step (Havel 1955; Hakimi 1962)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[(d_1,\dots,d_n)\ \text{graphical}\iff(d_2-1,\dots,d_{d_1+1}-1,d_{d_1+2},\dots,d_n)\ \text{graphical}\]</div><p class="formula-where">Connect the node of largest degree to the next \(d_1\) largest and recurse; the realization is deterministic once the tie order among equal degrees is fixed.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gen_degree_realization">Deterministic realisation of a degree sequence</a></td><td><code>gen_degree_realization</code></td><td>3</td><td>Realization of a degree sequence; the choice of which node to connect first (the tool's method option) changes the graph and is not recorded here.</td></tr><tr><td><a href="#cat_generator_hakimi_havel">Havel Hakimi Generator</a></td><td><code>cat_generator_hakimi_havel</code></td><td>1</td><td>Realization by the Havel-Hakimi recursion above.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/igraph.html">igraph (R)</a></th><th><a href="../../tools/pyigraph.html">igraph (Python)</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th></tr></thead><tbody><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">Not defined (no simple graph) for a sequence that violates the Erdos-Gallai condition or has odd sum.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Among equal degrees the realized graph depends on the order used by the algorithm.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details></div>

## Bipartite degree-sequence realization {#gen_realize_bipartite}

Measure id: `gen_realize_bipartite`. Original family: Generators and rewiring.

**Definition.** Bipartite degree-sequence realization.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_realize_bipartite-igraph">details</a></td><td><code>realize_bipartite_degseq</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_realize_bipartite-pyigraph">details</a></td><td><code>Realize_Bipartite_Degree_Sequence</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_realize_bipartite-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: realize\_bipartite\_degseq.
- <a id="why-gen_realize_bipartite-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Realize\_Bipartite\_Degree\_Sequence.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Deterministic realisation of a degree sequence {#gen_degree_realization}

Measure id: `gen_degree_realization`. Original family: Generators and rewiring.

**Definition.** Deterministic realisation of a degree sequence.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_degree_realization-networkx">details</a></td><td><code>alternating_havel_hakimi_graph; directed_havel_hakimi_graph; havel_hakimi_graph; reverse_havel_hakimi_graph</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_degree_realization-igraph">details</a></td><td><code>realize_degseq</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_degree_realization-pyigraph">details</a></td><td><code>Realize_Degree_Sequence</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_degree_realization-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: alternating\_havel\_hakimi\_graph; directed\_havel\_hakimi\_graph; havel\_hakimi\_graph; reverse\_havel\_hakimi\_graph.
- <a id="why-gen_degree_realization-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: realize\_degseq.
- <a id="why-gen_degree_realization-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: Realize\_Degree\_Sequence.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Havel Hakimi Generator {#cat_generator_hakimi_havel}

Measure id: `cat_generator_hakimi_havel`. Original family: Generators and rewiring.

**Definition.** Havel Hakimi Generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generator_hakimi_havel-networkit">details</a></td><td><code>HavelHakimiGenerator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generator_hakimi_havel-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: HavelHakimiGenerator.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
