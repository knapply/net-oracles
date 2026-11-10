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

## Definition {#concept-definition}

Deterministic degree-sequence realization. Entries grouped here: Bipartite degree-sequence realization; Deterministic realisation of a degree sequence; Havel Hakimi Generator.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#gen_realize_bipartite">Bipartite degree-sequence realization</a></td><td><code>gen_realize_bipartite</code></td><td>2</td></tr><tr><td><a href="#gen_degree_realization">Deterministic realisation of a degree sequence</a></td><td><code>gen_degree_realization</code></td><td>3</td></tr><tr><td><a href="#cat_generator_hakimi_havel">Havel Hakimi Generator</a></td><td><code>cat_generator_hakimi_havel</code></td><td>1</td></tr></tbody></table></div>

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
