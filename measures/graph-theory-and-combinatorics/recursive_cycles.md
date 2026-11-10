---
title: "Recursive cycles"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Recursive cycles {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `recursive_cycles`. 1 measure.

## Definition {#concept-definition}

Recursive cycles. Entries grouped here: Recursive cycles.

## Recursive cycles {#nxs_recursive_cycles}

Measure id: `nxs_recursive_cycles`. Original family: Graph theory and combinatorics.

**Definition.** Recursive cycles.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_recursive_cycles` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `list(nx.recursive_simple_cycles(D)) on the simple digraph with loops, in its order and rotation` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
