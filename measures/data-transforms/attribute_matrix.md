---
title: "Attribute-to-matrix construction"
layout: default
parent: "Data transforms"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Attribute-to-matrix construction {#concept-top}

Family: [Data transforms](index.html). Subfamily: Matrix and tie transformations. Concept id: `attribute_matrix`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(x_u\)</td><td>value of a node attribute at \(u\)</td></tr><tr><td>\(M=(m_{uv})\)</td><td>matrix built from the attribute</td></tr></tbody></table></div>

## Definition {#concept-definition}

Attribute-to-matrix construction. Entries grouped here: Attribute to matrix (same, difference, sender, receiver).

*Definition partly written:* The four forms are written from the names in the documented entry; whether 'difference' is signed or absolute, and what the diagonal holds, are not recorded in the sources, and no primary source is cited.

<div class="formula-block"><p class="formula-name"><strong>Same</strong> <span class="applies">applies to: any</span></p><div class="formula">\[m_{uv}=\mathbb 1[x_u=x_v]\]</div><p class="formula-where">1 when both nodes have the same attribute value.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Difference</strong> <span class="applies">applies to: any</span></p><div class="formula">\[m_{uv}=|x_u-x_v|\]</div><p class="formula-where">Absolute (or signed \(x_u-x_v\)) difference of numeric values.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Sender</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[m_{uv}=x_u\]</div><p class="formula-where">The attribute of the node in the row.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Receiver</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[m_{uv}=x_v\]</div><p class="formula-where">The attribute of the node in the column.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#attribute_matrix">Attribute to matrix (same, difference, sender, receiver)</a></td><td><code>attribute_matrix</code></td><td>1</td><td>Collective entry for the four constructions; each is a different matrix from the same attribute vector.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/ucinet.html">UCINET</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">With no nodes the matrix is 0\(\times\)0.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">A single node gives the 1\(\times\)1 matrix of the diagonal entry (1 for 'same', 0 for 'difference').</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details></div>

## Attribute to matrix (same, difference, sender, receiver) {#attribute_matrix}

Measure id: `attribute_matrix`. Original family: Data transforms.

**Definition.** Attribute to matrix (same, difference, sender, receiver).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-attribute_matrix-ucinet">details</a></td><td><code>Node attribute editor, attribute to matrix (att2mat: same, difference, etc.)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-attribute_matrix-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)
{% endraw %}
