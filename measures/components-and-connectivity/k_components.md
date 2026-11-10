---
title: "K-components"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-components {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_components`. 1 measure.

## Definition {#concept-definition}

K-components. Entries grouped here: K components.

## K components {#k_components}

Measure id: `k_components`. Original family: Components and connectivity.

**Definition.** K components.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `k_components` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_k_components` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.k_components(G), each component of k as k * 1000 + node` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
