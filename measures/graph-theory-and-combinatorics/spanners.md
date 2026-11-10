---
title: "Spanners"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spanners {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `spanners`. 2 measures.

## Definition {#concept-definition}

Spanners. Entries grouped here: Greedy Multiplicative Spanner; Spanner ok.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_greedy_multiplicative_spanner">Greedy Multiplicative Spanner</a></td><td><code>cat_greedy_multiplicative_spanner</code></td><td>1</td></tr><tr><td><a href="#gb_spanner_ok">Spanner ok</a></td><td><code>gb_spanner_ok</code></td><td>1</td></tr></tbody></table></div>

## Greedy Multiplicative Spanner {#cat_greedy_multiplicative_spanner}

Measure id: `cat_greedy_multiplicative_spanner`. Original family: Graph theory and combinatorics.

**Definition.** Greedy Multiplicative Spanner.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_greedy_multiplicative_spanner-jgrapht">details</a></td><td><code>GreedyMultiplicativeSpanner</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_multiplicative_spanner-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GreedyMultiplicativeSpanner.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Spanner ok {#gb_spanner_ok}

Measure id: `gb_spanner_ok`. Original family: Traversal, trees and DAGs.

**Definition.** Spanner ok.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>spanner</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_spanner_ok</code></td><td>NetworkX</td><td>undirected</td><td>no-value-on-some-inputs</td><td>(no value) multi_edges</td><td>multi_edges</td><td>abs 0, rel 0</td><td><code>stretch check of nx.spanner(nx.Graph(M), 3, seed=1)</code></td><td>NetworkX's spanner rejects multigraphs.</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
