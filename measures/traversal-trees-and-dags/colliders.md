---
title: "Colliders"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Colliders {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `colliders`. 1 measure.

## Definition {#concept-definition}

Colliders. Entries grouped here: Colliders.

## Colliders {#nxs_colliders}

Measure id: `nxs_colliders`. Original family: Graph theory and combinatorics.

**Definition.** Colliders.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_colliders_order` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.dag.colliders(D)), in its order` |  |
| `nxs_v_structures_order` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.dag.v_structures(D)), in its order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
