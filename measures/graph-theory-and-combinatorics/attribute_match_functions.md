---
title: "Node and edge attribute match functions"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Node and edge attribute match functions {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `attribute_match_functions`. 9 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(a(v),\ a(w)\)</td><td>attribute values of two nodes or edges</td></tr><tr><td>\(m(v,w)\)</td><td>match predicate used by an isomorphism search</td></tr></tbody></table></div>

## Definition {#concept-definition}

Node and edge attribute match functions. Entries grouped here: Categorical edge match; Categorical multiedge match; Categorical node match; Generic edge match; Generic multiedge match; Generic node match; and 3 more.

*Definition partly written:* The functions are described by their names (categorical equality, numerical closeness, user-defined); the exact comparison rules and tolerances of each documented entry are not recorded, and no primary source applies.

<div class="formula-block"><p class="formula-name"><strong>Categorical match</strong> <span class="applies">applies to: any</span></p><div class="formula">\[m(v,w)=\mathbb 1\bigl[a(v)=a(w)\bigr]\]</div><p class="formula-where">True when the attribute values are equal.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Numerical match</strong> <span class="applies">applies to: any</span></p><div class="formula">\[m(v,w)=\mathbb 1\bigl[|a(v)-a(w)|\le\tau\bigr]\]</div><p class="formula-where">True when the values are within a tolerance \(\tau\); the definition of \(\tau\) (absolute or relative) is not fixed here.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Generic match</strong> <span class="applies">applies to: any</span></p><div class="formula">\[m(v,w)=f\bigl(a(v),a(w)\bigr)\]</div><p class="formula-where">Any user function returning true or false.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_categorical_edge_match">Categorical edge match</a></td><td><code>cat_categorical_edge_match</code></td><td>1</td><td>Categorical edge match.</td></tr><tr><td><a href="#cat_categorical_match_multiedge">Categorical multiedge match</a></td><td><code>cat_categorical_match_multiedge</code></td><td>1</td><td>Categorical match on multi-edge sets: the sets of attributes of the parallel edges are compared.</td></tr><tr><td><a href="#cat_categorical_match">Categorical node match</a></td><td><code>cat_categorical_match</code></td><td>1</td><td>Categorical node match.</td></tr><tr><td><a href="#cat_edge_generic_match">Generic edge match</a></td><td><code>cat_edge_generic_match</code></td><td>1</td><td>Generic edge match.</td></tr><tr><td><a href="#cat_generic_match_multiedge">Generic multiedge match</a></td><td><code>cat_generic_match_multiedge</code></td><td>1</td><td>Generic match on multi-edge sets.</td></tr><tr><td><a href="#cat_generic_match">Generic node match</a></td><td><code>cat_generic_match</code></td><td>1</td><td>Generic node match.</td></tr><tr><td><a href="#cat_edge_match_numerical">Numerical edge match</a></td><td><code>cat_edge_match_numerical</code></td><td>1</td><td>Numerical edge match.</td></tr><tr><td><a href="#cat_match_multiedge_numerical">Numerical multiedge match</a></td><td><code>cat_match_multiedge_numerical</code></td><td>1</td><td>Numerical match on multi-edge sets.</td></tr><tr><td><a href="#cat_match_numerical">Numerical node match</a></td><td><code>cat_match_numerical</code></td><td>1</td><td>Numerical node match.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">For parallel edges the match compares the whole set (multiset) of attribute values, not one edge.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">The tolerance \(\tau\) of the numerical match must be non-negative.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Categorical edge match {#cat_categorical_edge_match}

Measure id: `cat_categorical_edge_match`. Original family: Roles and positions.

**Definition.** Categorical edge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_categorical_edge_match-networkx">details</a></td><td><code>categorical_edge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_categorical_edge_match-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: categorical\_edge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Categorical multiedge match {#cat_categorical_match_multiedge}

Measure id: `cat_categorical_match_multiedge`. Original family: Roles and positions.

**Definition.** Categorical multiedge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_categorical_match_multiedge-networkx">details</a></td><td><code>categorical_multiedge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_categorical_match_multiedge-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: categorical\_multiedge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Categorical node match {#cat_categorical_match}

Measure id: `cat_categorical_match`. Original family: Roles and positions.

**Definition.** Categorical node match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_categorical_match-networkx">details</a></td><td><code>categorical_node_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_categorical_match-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: categorical\_node\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generic edge match {#cat_edge_generic_match}

Measure id: `cat_edge_generic_match`. Original family: Graph theory and combinatorics.

**Definition.** Generic edge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_edge_generic_match-networkx">details</a></td><td><code>generic_edge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge_generic_match-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generic\_edge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generic multiedge match {#cat_generic_match_multiedge}

Measure id: `cat_generic_match_multiedge`. Original family: Graph theory and combinatorics.

**Definition.** Generic multiedge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generic_match_multiedge-networkx">details</a></td><td><code>generic_multiedge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generic_match_multiedge-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generic\_multiedge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Generic node match {#cat_generic_match}

Measure id: `cat_generic_match`. Original family: Graph theory and combinatorics.

**Definition.** Generic node match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_generic_match-networkx">details</a></td><td><code>generic_node_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_generic_match-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: generic\_node\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Numerical edge match {#cat_edge_match_numerical}

Measure id: `cat_edge_match_numerical`. Original family: Graph theory and combinatorics.

**Definition.** Numerical edge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_edge_match_numerical-networkx">details</a></td><td><code>numerical_edge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_edge_match_numerical-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: numerical\_edge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Numerical multiedge match {#cat_match_multiedge_numerical}

Measure id: `cat_match_multiedge_numerical`. Original family: Graph theory and combinatorics.

**Definition.** Numerical multiedge match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_match_multiedge_numerical-networkx">details</a></td><td><code>numerical_multiedge_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_match_multiedge_numerical-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: numerical\_multiedge\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Numerical node match {#cat_match_numerical}

Measure id: `cat_match_numerical`. Original family: Graph theory and combinatorics.

**Definition.** Numerical node match.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_match_numerical-networkx">details</a></td><td><code>numerical_node_match</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_match_numerical-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: numerical\_node\_match.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
