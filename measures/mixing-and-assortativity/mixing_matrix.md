---
title: "Mixing matrices"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Mixing matrices {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Mixing matrices. Concept id: `mixing_matrix`. 3 measures.

## Definition {#concept-definition}

Mixing matrices. Entries grouped here: Attribute mixing matrix; Degree mixing matrix; Mixing.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_attribute_matrix_mixing">Attribute mixing matrix</a></td><td><code>cat_attribute_matrix_mixing</code></td><td>1</td></tr><tr><td><a href="#cat_degree_matrix_mixing">Degree mixing matrix</a></td><td><code>cat_degree_matrix_mixing</code></td><td>1</td></tr><tr><td><a href="#mixing">Mixing</a></td><td><code>mixing</code></td><td>2</td></tr></tbody></table></div>

## Attribute mixing matrix {#cat_attribute_matrix_mixing}

Measure id: `cat_attribute_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Attribute mixing matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_attribute_matrix_mixing-networkx">details</a></td><td><code>attribute_mixing_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attribute_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: attribute\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degree mixing matrix {#cat_degree_matrix_mixing}

Measure id: `cat_degree_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Degree mixing matrix.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_matrix_mixing-networkx">details</a></td><td><code>degree_mixing_matrix</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: degree\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mixing {#mixing}

Measure id: `mixing`. Original family: Mixing and assortativity.

**Definition.** Mixing.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>attribute_mixing_dict; degree_mixing_dict</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-mixing-ucinet">details</a></td><td><code>Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mixing-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>mixing_attribute</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attribute_mixing_dict(G, 'label')</code></td><td></td></tr><tr><td><code>mixing_attribute_subset</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.attribute_mixing_dict(G, 'label', nodes = even nodes)</code></td><td></td></tr><tr><td><code>mixing_degree</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G)</code></td><td></td></tr><tr><td><code>mixing_degree_in_out</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G, x = 'in', y = 'out')</code></td><td></td></tr><tr><td><code>mixing_degree_subset</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.degree_mixing_dict(G, nodes = even nodes)</code></td><td></td></tr><tr><td><code>mixing_degree_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.degree_mixing_dict(G, weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
