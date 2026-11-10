---
title: "Fiedler value and vector"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Fiedler value and vector {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Spectra. Concept id: `fiedler`. 1 measure.

## Definition {#concept-definition}

Fiedler value and vector. Entries grouped here: Fiedler.

## Fiedler {#gm_fiedler}

Measure id: `gm_fiedler`. Original family: Matrices and spectra.

**Definition.** Fiedler.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `algebraic_connectivity; fiedler_vector; spectral_bisection` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_fiedler_value` | NetworkX | any | agrees |  |  | abs 1e-10, rel 1e-09 | `nx.algebraic_connectivity(G, tol = 1e-10, method = 'tracemin_lu') (directed graphs through NetworkX's _preprocess_graph, then weight = 'weight', as spectral_ordering reads them)` |  |
| `gm_fiedler_value_normalized_weighted` | NetworkX | any | agrees |  |  | abs 1e-10, rel 1e-09 | `nx.algebraic_connectivity(G, weight = 'weight', normalized = True, tol = 1e-10, method = 'tracemin_lu')` |  |
| `gm_fiedler_vector` | NetworkX | any | differs | two\_nodes | defaults | abs 1e-06, rel 1e-05 | `nx.fiedler_vector(G) (default method tracemin_pcg, tol 1e-8)` | For two nodes NetworkX returns \[1, -1\] without solving; the reference returns the unit vector with its first entry negative (the backend returns NetworkX's \[1, -1\]). |
| `gm_fiedler_vector_normalized` | NetworkX | any | differs | two\_nodes | defaults, normalization, ties | abs 1e-06, rel 1e-05 | `nx.fiedler_vector(G, normalized = True)` | For two nodes NetworkX returns \[1, -1\] without solving; the reference returns the unit vector with its first entry negative. NetworkX's tracemin\_pcg iteration for the normalized Laplacian does not converge on these graphs and, having no iteration cap, never returns. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
