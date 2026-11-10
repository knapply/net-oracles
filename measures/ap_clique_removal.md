---
title: "Clique removal"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Clique removal

Family: Graph theory and combinatorics. Identifier: `ap_clique_removal`.

## Definition

Ramsey-based clique removal: a large independent set and the disjoint cliques removed.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `clique_removal` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_clique_removal` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.approximation.clique_removal(G_sorted): (size of the independent set, number of cliques)` | NetworkX's ramsey\_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value's, which takes the first node in node order; any graph with a choice can differ. ap\_clique\_removal\_valid checks the reference value's sets, and the convention check ap\_clique\_removal\_\_networkx reproduces NetworkX through the reference value's set-order kernel. |

## References

[baryehuda1985local](../references.html#baryehuda1985local), [bodlaender2010treewidth](../references.html#bodlaender2010treewidth), [boob2020flowless](../references.html#boob2020flowless), [boppana1992approximating](../references.html#boppana1992approximating), [hagberg2008exploring](../references.html#hagberg2008exploring), [haynes1998fundamentals](../references.html#haynes1998fundamentals), [lekkerkerker1962representation](../references.html#lekkerkerker1962representation), [moon1968topics](../references.html#moon1968topics)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
