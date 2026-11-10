---
title: "Bethe Hessian"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bethe Hessian {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `bethe_hessian`. 1 measure.

## Definition {#concept-definition}

Bethe Hessian. Entries grouped here: Bethe hessian.

## Bethe hessian {#gm_bethe_hessian}

Measure id: `gm_bethe_hessian`. Original family: Matrices and spectra.

**Definition.** Bethe hessian.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `bethe_hessian_matrix` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_bethe_hessian` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.bethe_hessian_matrix(G).toarray() (graph built without weights)` | NetworkX does not implement the Bethe Hessian for multigraphs. |
| `gm_bethe_hessian_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.bethe_hessian_matrix(G).toarray() (it reads the attribute 'weight')` | NetworkX does not implement the Bethe Hessian for multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
