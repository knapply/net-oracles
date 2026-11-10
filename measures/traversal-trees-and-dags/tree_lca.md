---
title: "Lowest common ancestor in trees"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lowest common ancestor in trees {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `tree_lca`. 2 measures.

## Definition {#concept-definition}

Lowest common ancestor in trees. Entries grouped here: Tree lca; Nxs tree lca.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Tree lca](#tree_lca) | `tree_lca` | 2 |
| [Nxs tree lca](#nxs_tree_lca) | `nxs_tree_lca` | 1 |

## Tree lca {#tree_lca}

Measure id: `tree_lca`. Original family: Traversal, trees and DAGs.

**Definition.** Tree lca.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-tree_lca-jgrapht) | `BinaryLiftingLCAFinder; EulerTourRMQLCAFinder; HeavyPathLCAFinder; NaiveLCAFinder; TarjanLCAFinder` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-tree_lca-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: BinaryLiftingLCAFinder; EulerTourRMQLCAFinder; HeavyPathLCAFinder; NaiveLCAFinder; TarjanLCAFinder.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `dag_tree_lca` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.tree_all_pairs_lowest_common_ancestor(T, root = 0, pairs)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Nxs tree lca {#nxs_tree_lca}

Measure id: `nxs_tree_lca`. Original family: Graph theory and combinatorics.

**Definition.** Nxs tree lca.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_tree_lca` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[(u, v, a) for (u, v), a in nx.tree_all_pairs_lowest_common_ancestor(T, root = 0)], in its order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
