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

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Branching](#branching) | `branching` | 1 |
| [Branching weight](#gb_branching_weight) | `gb_branching_weight` | 1 |
| [Dag to branching](#cat_branching_dag_to) | `cat_branching_dag_to` | 1 |
| [Greedy branching](#nxs_greedy_branching) | `nxs_greedy_branching` | 1 |

## References {#concept-references}

[boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

## Branching {#branching}

Measure id: `branching`. Original family: Traversal, trees and DAGs.

**Definition.** Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `maximum_branching; maximum_spanning_arborescence; minimal_branching; minimum_branching; minimum_spanning_arborescence` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_max_arborescence` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException` |  |
| `tree_max_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_branching(M, attr = 'weight').size(weight = 'weight')` |  |
| `tree_min_arborescence` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException` |  |
| `tree_min_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_branching(M, attr = 'weight').size(weight = 'weight')` |  |
| `tree_minimal_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.algorithms.tree.branchings.minimal_branching(M, attr = 'weight').size(weight = 'weight')` |  |

**References:** [boruvka1926jistem](../../references.html#boruvka1926jistem), [camerini1979note](../../references.html#camerini1979note), [chu1965shortest](../../references.html#chu1965shortest), [edmonds1967optimum](../../references.html#edmonds1967optimum), [gabow1986efficient](../../references.html#gabow1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kruskal1956shortest](../../references.html#kruskal1956shortest), [prim1957shortest](../../references.html#prim1957shortest)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Branching weight {#gb_branching_weight}

Measure id: `gb_branching_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Branching weight.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `branching_weight` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_branching_weight` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_branching(M, preserve_attrs=True)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Dag to branching {#cat_branching_dag_to}

Measure id: `cat_branching_dag_to`. Original family: Traversal, trees and DAGs.

**Definition.** Dag to branching.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_branching_dag_to-networkx) | `dag_to_branching` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_branching_dag_to-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: dag\_to\_branching.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Greedy branching {#nxs_greedy_branching}

Measure id: `nxs_greedy_branching`. Original family: Graph theory and combinatorics.

**Definition.** Greedy branching.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `greedy_branching` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_greedy_branching_max` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(greedy_branching(D, attr = 'weight', kind = 'max').edges())` |  |
| `nxs_greedy_branching_min` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(greedy_branching(D, attr = 'weight', kind = 'min').edges())` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
