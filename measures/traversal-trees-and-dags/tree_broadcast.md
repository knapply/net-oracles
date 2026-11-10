---
title: "Tree broadcast time and center"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Tree broadcast time and center {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `tree_broadcast`. 2 measures.

## Definition {#concept-definition}

Tree broadcast time and center. Entries grouped here: Broadcast time; Tree broadcast center.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Broadcast time](#gb_broadcast_time) | `gb_broadcast_time` | 1 |
| [Tree broadcast center](#cat_broadcast_center_tree) | `cat_broadcast_center_tree` | 1 |

## Broadcast time {#gb_broadcast_time}

Measure id: `gb_broadcast_time`. Original family: Traversal, trees and DAGs.

**Definition.** Broadcast time.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `tree_broadcast_time` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_broadcast_time` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.tree_broadcast_time(nx.Graph(M))` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Tree broadcast center {#cat_broadcast_center_tree}

Measure id: `cat_broadcast_center_tree`. Original family: Traversal, trees and DAGs.

**Definition.** Tree broadcast center.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_broadcast_center_tree-networkx) | `tree_broadcast_center` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_broadcast_center_tree-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: tree\_broadcast\_center.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
