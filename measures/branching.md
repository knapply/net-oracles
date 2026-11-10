---
title: "Branching"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Branching

Family: Traversal, trees and DAGs. Identifier: `branching`.

## Definition

Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `maximum_branching; maximum_spanning_arborescence; minimal_branching; minimum_branching; minimum_spanning_arborescence` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `tree_max_arborescence` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException` |  |
| `tree_max_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.maximum_branching(M, attr = 'weight').size(weight = 'weight')` |  |
| `tree_min_arborescence` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_spanning_arborescence(M, attr = 'weight').size(weight = 'weight'); -1 on NetworkXException` |  |
| `tree_min_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_branching(M, attr = 'weight').size(weight = 'weight')` |  |
| `tree_minimal_branching` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.algorithms.tree.branchings.minimal_branching(M, attr = 'weight').size(weight = 'weight')` |  |

## References

[boruvka1926jistem](../references.html#boruvka1926jistem), [camerini1979note](../references.html#camerini1979note), [chu1965shortest](../references.html#chu1965shortest), [edmonds1967optimum](../references.html#edmonds1967optimum), [gabow1986efficient](../references.html#gabow1986efficient), [hagberg2008exploring](../references.html#hagberg2008exploring), [kruskal1956shortest](../references.html#kruskal1956shortest), [prim1957shortest](../references.html#prim1957shortest)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
