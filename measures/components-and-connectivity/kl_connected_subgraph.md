---
title: "KL-connected subgraph"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# KL-connected subgraph {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Robustness and percolation. Concept id: `kl_connected_subgraph`. 1 measure.

## Definition {#concept-definition}

KL-connected subgraph. Entries grouped here: Kl.

## Kl {#st_kl}

Measure id: `st_kl`. Original family: Graph theory and combinatorics.

**Definition.** Kl.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `kl_connected_subgraph` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_kl` | NetworkX | any | no-value-on-some-inputs |  | direction | abs 0, rel 0 | `per edge: 1 if kept by nx.kl_connected_subgraph(G_sorted, 2, l), l = 2, 3` | NetworkX deep-copies the graph once per edge; the 784-arc fixture is skipped for time |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
