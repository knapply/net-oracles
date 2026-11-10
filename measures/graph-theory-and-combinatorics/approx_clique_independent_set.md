---
title: "Approximate clique and independent set (Ramsey, clique removal)"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Approximate clique and independent set (Ramsey, clique removal) {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `approx_clique_independent_set`. 3 measures.

## Definition {#concept-definition}

Ramsey-based clique removal: a large independent set and the disjoint cliques removed.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Clique removal](#ap_clique_removal) | `ap_clique_removal` | 1 |
| [Large clique size](#ap_large_clique_size) | `ap_large_clique_size` | 1 |
| [Nx ramsey](#ap_nx_ramsey) | `ap_nx_ramsey` | 1 |

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [haynes1998fundamentals](../../references.html#haynes1998fundamentals), [lekkerkerker1962representation](../../references.html#lekkerkerker1962representation), [moon1968topics](../../references.html#moon1968topics)

## Clique removal {#ap_clique_removal}

Measure id: `ap_clique_removal`. Original family: Graph theory and combinatorics.

**Definition.** Ramsey-based clique removal: a large independent set and the disjoint cliques removed.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `clique_removal` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_clique_removal` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.approximation.clique_removal(G_sorted): (size of the independent set, number of cliques)` | NetworkX's ramsey\_R2 recurses on subgraphs whose nodes come in Python set order, so its arbitrary node, and the cliques and independent sets it finds, differ from the reference value's, which takes the first node in node order; any graph with a choice can differ. ap\_clique\_removal\_valid checks the reference value's sets, and the convention check ap\_clique\_removal\_\_networkx reproduces NetworkX through the reference value's set-order kernel. |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [haynes1998fundamentals](../../references.html#haynes1998fundamentals), [lekkerkerker1962representation](../../references.html#lekkerkerker1962representation), [moon1968topics](../../references.html#moon1968topics)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Large clique size {#ap_large_clique_size}

Measure id: `ap_large_clique_size`. Original family: Graph theory and combinatorics.

**Definition.** Large clique size.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `large_clique_size` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_large_clique_size` | NetworkX | any | differs | directed, undirected | direction, ties | abs 0, rel 0 | `nx.approximation.large_clique_size(G_sorted)` | NetworkX picks the candidate of largest degree from a Python set, so ties go to a different node than the reference value's first in node order, on any graph with tied degrees. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx ramsey {#ap_nx_ramsey}

Measure id: `ap_nx_ramsey`. Original family: Graph theory and combinatorics.

**Definition.** Nx ramsey.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `ramsey_R2` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_ramsey` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `ramsey_R2, clique_removal, max_clique, maximum_independent_set, large_clique_size on G_sorted: each set sorted with its size first` |  |
| `ap_nx_ramsey_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's results` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
