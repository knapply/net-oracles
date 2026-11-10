---
title: "Bethe hessian"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Bethe hessian

Family: Matrices and spectra. Identifier: `gm_bethe_hessian`.

## Definition

Bethe hessian.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `bethe_hessian_matrix` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_bethe_hessian` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.bethe_hessian_matrix(G).toarray() (graph built without weights)` | NetworkX does not implement the Bethe Hessian for multigraphs. |
| `gm_bethe_hessian_weighted` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `nx.bethe_hessian_matrix(G).toarray() (it reads the attribute 'weight')` | NetworkX does not implement the Bethe Hessian for multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
