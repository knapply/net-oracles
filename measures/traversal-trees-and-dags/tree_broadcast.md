---
title: "Tree broadcast time and center"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tree broadcast time and center {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `tree_broadcast`. 2 measures.

## Definition {#concept-definition}

Tree broadcast time and center. Entries grouped here: Broadcast time; Tree broadcast center.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#gb_broadcast_time">Broadcast time</a></td><td><code>gb_broadcast_time</code></td><td>1</td></tr><tr><td><a href="#cat_broadcast_center_tree">Tree broadcast center</a></td><td><code>cat_broadcast_center_tree</code></td><td>1</td></tr></tbody></table></div>

## Broadcast time {#gb_broadcast_time}

Measure id: `gb_broadcast_time`. Original family: Traversal, trees and DAGs.

**Definition.** Broadcast time.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>tree_broadcast_time</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_broadcast_time</code></td><td>NetworkX</td><td>undirected</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.tree_broadcast_time(nx.Graph(M))</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Tree broadcast center {#cat_broadcast_center_tree}

Measure id: `cat_broadcast_center_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Tree broadcast center.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_broadcast_center_tree-networkx">details</a></td><td><code>tree_broadcast_center</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_broadcast_center_tree-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: tree\_broadcast\_center.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
