---
title: "Lowest common ancestor in DAGs"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lowest common ancestor in DAGs {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `dag_lca`. 1 measure.

## Definition {#concept-definition}

Lowest common ancestor of each node pair in a DAG; pairs with no common ancestor get the none mark u32::MAX.

## References {#concept-references}

[aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

## Dag lca {#dag_lca}

Measure id: `dag_lca`. Original family: Traversal, trees and DAGs.

**Definition.** Lowest common ancestor of each node pair in a DAG; pairs with no common ancestor get the none mark u32::MAX.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `lowest_common_ancestor; tree_all_pairs_lowest_common_ancestor` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_lca` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `dict(nx.all_pairs_lowest_common_ancestor(D, pairs)) for every pair u <= v, -1 if absent` | When a pair has several lowest common ancestors NetworkX starts its walk from the first common ancestor in Python's set order and the reference from the one of smallest index, so they can return different, equally valid ancestors (checked pair by pair on the corpus: every differing answer of both is a lowest common ancestor). dag\_lca\_check confirms every reference answer. |
| `dag_lca_check` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[number of pairs nx.all_pairs_lowest_common_ancestor(D, pairs) answers, 1]` |  |

**References:** [aho1972transitive](../../references.html#aho1972transitive), [aho1976finding](../../references.html#aho1976finding), [bender2005lowest](../../references.html#bender2005lowest), [cooper2001simple](../../references.html#cooper2001simple), [cytron1991efficiently](../../references.html#cytron1991efficiently), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kahn1962topological](../../references.html#kahn1962topological), [knuth1974structured](../../references.html#knuth1974structured)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
