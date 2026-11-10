---
title: "Longest path in a DAG"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Longest path in a DAG {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `dag_longest_path`. 7 measures.

## Definition {#concept-definition}

A longest path of a DAG and its length, by dynamic programming in topological order.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#cat_dag_longest_path">Dag longest path</a></td><td><code>cat_dag_longest_path</code></td><td>1</td></tr><tr><td><a href="#cat_dag_length_longest_path">Dag longest path length</a></td><td><code>cat_dag_length_longest_path</code></td><td>1</td></tr><tr><td><a href="#cat_dag_longest_path_weighted">Dag weighted longest path</a></td><td><code>cat_dag_longest_path_weighted</code></td><td>1</td></tr><tr><td><a href="#cat_dag_length_longest_path_weighted">Dag weighted longest path length</a></td><td><code>cat_dag_length_longest_path_weighted</code></td><td>1</td></tr><tr><td><a href="#longest_length">Longest length</a></td><td><code>longest_length</code></td><td>1</td></tr><tr><td><a href="#longest_path">Longest path</a></td><td><code>longest_path</code></td><td>1</td></tr><tr><td><a href="#gb_longest_path_len">Longest path len</a></td><td><code>gb_longest_path_len</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Dag longest path {#cat_dag_longest_path}

Measure id: `cat_dag_longest_path`. Original family: Paths and distances.

**Definition.** Dag longest path.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dag_longest_path-rustworkx">details</a></td><td><code>dag_longest_path</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dag_longest_path-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: dag\_longest\_path.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag longest path length {#cat_dag_length_longest_path}

Measure id: `cat_dag_length_longest_path`. Original family: Paths and distances.

**Definition.** Dag longest path length.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dag_length_longest_path-rustworkx">details</a></td><td><code>dag_longest_path_length</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dag_length_longest_path-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: dag\_longest\_path\_length.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag weighted longest path {#cat_dag_longest_path_weighted}

Measure id: `cat_dag_longest_path_weighted`. Original family: Paths and distances.

**Definition.** Dag weighted longest path.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dag_longest_path_weighted-rustworkx">details</a></td><td><code>dag_weighted_longest_path</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dag_longest_path_weighted-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: dag\_weighted\_longest\_path.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Dag weighted longest path length {#cat_dag_length_longest_path_weighted}

Measure id: `cat_dag_length_longest_path_weighted`. Original family: Paths and distances.

**Definition.** Dag weighted longest path length.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_dag_length_longest_path_weighted-rustworkx">details</a></td><td><code>dag_weighted_longest_path_length</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_dag_length_longest_path_weighted-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: dag\_weighted\_longest\_path\_length.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Longest length {#longest_length}

Measure id: `longest_length`. Original family: Traversal, trees and DAGs.

**Definition.** A longest path of a DAG and its length, by dynamic programming in topological order.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>dag_longest_path_length</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dag_longest_length</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.dag_longest_path_length(D)</code></td><td></td></tr><tr><td><code>dag_longest_length_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.dag_longest_path_length(D, weight = 'weight') on the multigraph D</code></td><td></td></tr></tbody></table></div>

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Longest path {#longest_path}

Measure id: `longest_path`. Original family: Traversal, trees and DAGs.

**Definition.** A longest path of a DAG and its length, by dynamic programming in topological order.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>dag_longest_path</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>dag_longest_path</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.dag_longest_path(D)</code></td><td></td></tr><tr><td><code>dag_longest_path_weighted</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.dag_longest_path(D, weight = 'weight') on the multigraph D</code></td><td></td></tr></tbody></table></div>

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Longest path len {#gb_longest_path_len}

Measure id: `gb_longest_path_len`. Original family: Traversal, trees and DAGs.

**Definition.** Longest path len.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_longest_path_len</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>len(nx.dag_longest_path(M, weight=None)) - 1</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
