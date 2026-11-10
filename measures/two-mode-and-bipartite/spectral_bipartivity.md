---
title: "Spectral bipartivity"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Spectral bipartivity {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `spectral_bipartivity`. 1 measure.

## Definition {#concept-definition}

Spectral bipartivity. Entries grouped here: Spectral bipartivity.

## Spectral bipartivity {#spectral_bipartivity}

Measure id: `spectral_bipartivity`. Original family: Two-mode and bipartite.

**Definition.** Spectral bipartivity.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `spectral_bipartivity` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `spectral_bipartivity` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.bipartite.spectral_bipartivity(G, nodes = list(G)) and nx.bipartite.spectral_bipartivity(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
