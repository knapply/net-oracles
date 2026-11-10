---
title: "Antichains and antichain width"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Antichains and antichain width {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `antichains`. 2 measures.

## Definition {#concept-definition}

The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#gb_antichain_width">Antichain width</a></td><td><code>gb_antichain_width</code></td><td>1</td></tr><tr><td><a href="#cat_antichains">Antichains</a></td><td><code>cat_antichains</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[dilworth1950decomposition](../../references.html#dilworth1950decomposition), [hopcroft1973n52](../../references.html#hopcroft1973n52)

## Antichain width {#gb_antichain_width}

Measure id: `gb_antichain_width`. Original family: Traversal, trees and DAGs.

**Definition.** The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_antichain_width</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.algorithms.dag.antichain_width(M)</code></td><td></td></tr></tbody></table></div>

**References:** [dilworth1950decomposition](../../references.html#dilworth1950decomposition), [hopcroft1973n52](../../references.html#hopcroft1973n52)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Antichains {#cat_antichains}

Measure id: `cat_antichains`. Original family: Graph theory and combinatorics.

**Definition.** Antichains.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_antichains-networkx">details</a></td><td><code>antichains</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_antichains-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: antichains.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
