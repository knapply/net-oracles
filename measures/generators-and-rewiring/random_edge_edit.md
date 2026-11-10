---
title: "Random edge addition and removal"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random edge addition and removal {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Rewiring and randomization. Concept id: `random_edge_edit`. 2 measures.

## Definition {#concept-definition}

Random edge addition and removal. Entries grouped here: Random edge addition and removal; Random k lift.

*Definition not yet written.* Documented by name only; the sources record the tool function and no definition, and no primary paper was checked.

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#random_edge_edit">Random edge addition and removal</a></td><td><code>random_edge_edit</code></td><td>1</td></tr><tr><td><a href="#cat_k_lift_random">Random k lift</a></td><td><code>cat_k_lift_random</code></td><td>1</td></tr></tbody></table></div>

## Random edge addition and removal {#random_edge_edit}

Measure id: `random_edge_edit`. Original family: Generators and rewiring.

**Definition.** Random edge addition and removal.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-random_edge_edit-graphtool">details</a></td><td><code>add_random_edges; remove_random_edges</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-random_edge_edit-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: add\_random\_edges; remove\_random\_edges.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Random k lift {#cat_k_lift_random}

Measure id: `cat_k_lift_random`. Original family: Graph theory and combinatorics.

**Definition.** Random k lift.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_k_lift_random-networkx">details</a></td><td><code>random_k_lift</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_k_lift_random-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: random\_k\_lift.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
