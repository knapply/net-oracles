---
title: "Spanners"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Spanners {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `spanners`. 2 measures.

## Definition {#concept-definition}

Spanners. Entries grouped here: Greedy Multiplicative Spanner; Spanner ok.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Greedy Multiplicative Spanner](#cat_greedy_multiplicative_spanner) | `cat_greedy_multiplicative_spanner` | 1 |
| [Spanner ok](#gb_spanner_ok) | `gb_spanner_ok` | 1 |

## Greedy Multiplicative Spanner {#cat_greedy_multiplicative_spanner}

Measure id: `cat_greedy_multiplicative_spanner`. Original family: Graph theory and combinatorics.

**Definition.** Greedy Multiplicative Spanner.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GreedyMultiplicativeSpanner` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Spanner ok {#gb_spanner_ok}

Measure id: `gb_spanner_ok`. Original family: Traversal, trees and DAGs.

**Definition.** Spanner ok.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `spanner` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_spanner_ok` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `stretch check of nx.spanner(nx.Graph(M), 3, seed=1)` | NetworkX's spanner rejects multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
