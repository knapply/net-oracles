---
title: "Moral graph"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Moral graph {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `moral_graph`. 1 measure.

## Definition {#concept-definition}

Moral graph. Entries grouped here: Moral edges.

## Moral edges {#gb_moral_edges}

Measure id: `gb_moral_edges`. Original family: Traversal, trees and DAGs.

**Definition.** Moral edges.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `moral_graph` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_moral_edges` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `distinct pairs of nx.moral_graph(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
