---
title: "Triad type classification"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Triad type classification {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Triads, motifs and local structure. Concept id: `triad_type`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\((m,a,n)\)</td><td>numbers of mutual, asymmetric and null dyads of a triple of nodes, with \(m+a+n=3\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Triad type classification. Entries grouped here: Triad type; Triads by type.

*Definition partly written:* Both measures are documented only (NetworkX) and were never run; the assignment of the orientation letters (D, U, C, T) is not detailed in the sources.

<div class="formula-block"><p class="formula-name"><strong>Triad type (Holland and Leinhardt 1976)</strong> <span class="applies">applies to: directed, simple</span></p><div class="formula">\[\text{type}(i,j,k)=m\,a\,n\ [\text{orientation letter}]\]</div><p class="formula-where">One of 16 classes (003, 012, 102, 021D, 021U, 021C, 111D, 111U, 030T, 030C, 201, 120D, 120U, 120C, 210, 300): the three digits are the counts of mutual, asymmetric and null dyads, the letter distinguishes orientations (Down, Up, Cyclic, Transitive) where more than one structure has the same counts.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_triad_type">Triad type</a></td><td><code>cat_triad_type</code></td><td>1</td><td>The type of a given triple of nodes among the 16 classes.</td></tr><tr><td><a href="#cat_triads_type">Triads by type</a></td><td><code>cat_triads_type</code></td><td>1</td><td>The triples of a graph grouped by type.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">A triad needs three distinct nodes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Loops are ignored in the dyad classification.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">A dyad is tied or not.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined for directed graphs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Triad type {#cat_triad_type}

Measure id: `cat_triad_type`. Original family: Cohesion and subgroups.

**Definition.** Triad type.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_triad_type-networkx">details</a></td><td><code>triad_type</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_triad_type-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: triad\_type.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Triads by type {#cat_triads_type}

Measure id: `cat_triads_type`. Original family: Cohesion and subgroups.

**Definition.** Triads by type.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_triads_type-networkx">details</a></td><td><code>triads_by_type</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_triads_type-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: triads\_by\_type.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
