---
title: "Maximum branching"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum branching {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Spanning trees and branchings. Concept id: `maximum_branching`. 4 measures.

## Definition {#concept-definition}

Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

*Definition not yet written.*

## Variants {#concept-variants}

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th></tr></thead><tbody><tr><td><a href="#branching">Branching</a></td><td><code>branching</code></td><td>1</td></tr><tr><td><a href="#gb_branching_weight">Branching weight</a></td><td><code>gb_branching_weight</code></td><td>1</td></tr><tr><td><a href="#cat_branching_dag_to">Dag to branching</a></td><td><code>cat_branching_dag_to</code></td><td>1</td></tr><tr><td><a href="#nxs_greedy_branching">Greedy branching</a></td><td><code>nxs_greedy_branching</code></td><td>1</td></tr></tbody></table></div>

## References {#concept-references}

[boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

## Branching {#branching}

Measure id: `branching`. Original family: Traversal, trees and DAGs.

**Definition.** Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>maximum_branching; maximum_spanning_arborescence; minimal_branching; minimum_branching; minimum_spanning_arborescence</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>tree_max_arborescence</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException</code></td><td></td></tr><tr><td><code>tree_max_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr><tr><td><code>tree_min_arborescence</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.minimum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException</code></td><td></td></tr><tr><td><code>tree_min_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.minimum_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr><tr><td><code>tree_minimal_branching</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.algorithms.tree.branchings.minimal_branching(M, attr = 'weight').size(weight = 'weight')</code></td><td></td></tr></tbody></table></div>

**References:** [boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Branching weight {#gb_branching_weight}

Measure id: `gb_branching_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Branching weight.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>branching_weight</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_branching_weight</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 1e-12, rel 1e-12</td><td><code>nx.maximum_branching(M, preserve_attrs=True)</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Dag to branching {#cat_branching_dag_to}

Measure id: `cat_branching_dag_to`. Original family: Traversal, trees and DAGs.

**Definition.** Dag to branching.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_branching_dag_to-networkx">details</a></td><td><code>dag_to_branching</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_branching_dag_to-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: dag\_to\_branching.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Greedy branching {#nxs_greedy_branching}

Measure id: `nxs_greedy_branching`. Original family: Graph theory and combinatorics.

**Definition.** Greedy branching.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>greedy_branching</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_greedy_branching_max</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sorted(greedy_branching(D, attr = 'weight', kind = 'max').edges())</code></td><td></td></tr><tr><td><code>nxs_greedy_branching_min</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>sorted(greedy_branching(D, attr = 'weight', kind = 'min').edges())</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
