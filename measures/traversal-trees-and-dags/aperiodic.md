---
title: "Aperiodicity"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Aperiodicity {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `aperiodic`. 2 measures.

## Definition {#concept-definition}

Aperiodicity. Entries grouped here: Gb aperiodic; Gm aperiodic.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Gb aperiodic](#gb_aperiodic) | `gb_aperiodic` | 1 |
| [Gm aperiodic](#gm_aperiodic) | `gm_aperiodic` | 1 |

## Gb aperiodic {#gb_aperiodic}

Measure id: `gb_aperiodic`. Original family: Traversal, trees and DAGs.

**Definition.** Gb aperiodic.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_aperiodic` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_aperiodic` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_aperiodic(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gm aperiodic {#gm_aperiodic}

Measure id: `gm_aperiodic`. Original family: Matrices and spectra.

**Definition.** Gm aperiodic.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_aperiodic` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.is_aperiodic(G) on strongly connected graphs` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
