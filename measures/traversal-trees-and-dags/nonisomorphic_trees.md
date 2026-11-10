---
title: "Number of nonisomorphic trees"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Number of nonisomorphic trees {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `nonisomorphic_trees`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(t(n)\)</td><td>number of trees on \(n\) nodes, counted up to isomorphism</td></tr></tbody></table></div>

## Definition {#concept-definition}

Number of nonisomorphic trees. Entries grouped here: Number of nonisomorphic trees.

*Definition partly written:* The count is a known integer sequence given here from its standard definition and first values, without a cited primary source; the tool entry is documented only.

<div class="formula-block"><p class="formula-name"><strong>Number of nonisomorphic trees</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[t(0),\dots,t(10)=1,1,1,1,2,3,6,11,23,47,106\]</div><p class="formula-where">No closed form; the generating function satisfies a functional equation (Otter). For \(n=4\) the two trees are the path and the star.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_nonisomorphic_tree">Number of nonisomorphic trees</a></td><td><code>cat_nonisomorphic_tree</code></td><td>1</td><td>The number \(t(n)\) of nonisomorphic (unlabelled) trees on \(n\) nodes; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="A free parameter (attenuation, damping, decay, exponent, walk length) outside the range for which the series or fixed point is defined or convergent."><strong>Parameter outside its valid range</strong></td><td class="def">\(n\ge0\) integer; \(n=0\) is counted as 1 (the null tree) by the sequence above.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Parameter outside its valid range</summary><ul><li>No tool entries.</li></ul></details></div>

## Number of nonisomorphic trees {#cat_nonisomorphic_tree}

Measure id: `cat_nonisomorphic_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Number of nonisomorphic trees.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_nonisomorphic_tree-networkx">details</a></td><td><code>number_of_nonisomorphic_trees</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_nonisomorphic_tree-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: number\_of\_nonisomorphic\_trees.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
