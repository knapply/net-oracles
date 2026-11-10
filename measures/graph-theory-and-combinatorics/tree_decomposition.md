---
title: "Tree decomposition and treewidth"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Tree decomposition and treewidth {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Tree decomposition. Concept id: `tree_decomposition`. 2 measures.

## Definition {#concept-definition}

Tree decomposition of a simple undirected network by an elimination heuristic: the bags, the edges between bags and the width.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Treewidth](#ap_treewidth) | `ap_treewidth` | 1 |
| [Tw min degree](#ap_tw_min_degree) | `ap_tw_min_degree` | 1 |

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Treewidth {#ap_treewidth}

Measure id: `ap_treewidth`. Original family: Graph theory and combinatorics.

**Definition.** Tree decomposition of a simple undirected network by an elimination heuristic: the bags, the edges between bags and the width.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `treewidth_min_fill_in` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_treewidth` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `(width, bags) of nx.approximation.treewidth_min_fill_in(G_sorted)` |  |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Tw min degree {#ap_tw_min_degree}

Measure id: `ap_tw_min_degree`. Original family: Graph theory and combinatorics.

**Definition.** Tree decomposition of a simple undirected network by an elimination heuristic: the bags, the edges between bags and the width.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `treewidth_min_degree` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_tw_min_degree` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.approximation.treewidth_min_degree(G_sorted): the width, the bags in decomposition order (sorted), then (-1, i, j) per edge` |  |
| `ap_tw_min_degree_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's decomposition` |  |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
