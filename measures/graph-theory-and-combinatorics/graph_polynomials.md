---
title: "Chromatic and Tutte polynomials"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Chromatic and Tutte polynomials {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Coloring. Concept id: `graph_polynomials`. 2 measures.

## Definition {#concept-definition}

Chromatic and Tutte polynomials. Entries grouped here: Chromatic polynomial; Polynomials.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_chromatic_polynomial">Chromatic polynomial</a></td><td><code>cat_chromatic_polynomial</code></td><td>1</td></tr><tr><td><a href="#st_polynomials">Polynomials</a></td><td><code>st_polynomials</code></td><td>1</td></tr></tbody></table></div>

## Chromatic polynomial {#cat_chromatic_polynomial}

Measure id: `cat_chromatic_polynomial`. Original family: Graph theory and combinatorics.

**Definition.** Chromatic polynomial.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_chromatic_polynomial-networkx">details</a></td><td><code>chromatic_polynomial</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_chromatic_polynomial-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: chromatic\_polynomial.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Polynomials {#st_polynomials}

Measure id: `st_polynomials`. Original family: Graph theory and combinatorics.

**Definition.** Polynomials.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>tutte_polynomial</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>st_polynomials</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>coefficients of sympy.Poly(nx.chromatic_polynomial(G), x) and of nx.tutte_polynomial(G) in x, y</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
