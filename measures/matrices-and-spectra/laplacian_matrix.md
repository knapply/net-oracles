---
title: "Laplacian matrix"
layout: default
parent: "Matrices and spectra"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Laplacian matrix {#concept-top}

Family: [Matrices and spectra](index.html). Subfamily: Graph matrices. Concept id: `laplacian_matrix`. 2 measures.

## Definition {#concept-definition}

Laplacian matrix. Entries grouped here: Gm laplacian; Magnetic laplacian matrix.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Gm laplacian](#gm_laplacian) | `gm_laplacian` | 8 |
| [Magnetic laplacian matrix](#cat_laplacian_magnetic_matrix) | `cat_laplacian_magnetic_matrix` | 1 |

## Gm laplacian {#gm_laplacian}

Measure id: `gm_laplacian`. Original family: Matrices and spectra.

**Definition.** Gm laplacian.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `directed_combinatorial_laplacian_matrix; directed_laplacian_matrix; laplacian_matrix; normalized_laplacian_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `laplacian_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `laplacian` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `laplacian` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `laplacianMatrix` | API listing |
| [scikit-network](../../tools/sknetwork.html) | · reported in docs | `Laplacian` | API listing |
| [centiserve](../../tools/centiserve.html) | · reported in docs | `laplacian` | API listing |
| [graspologic](../../tools/graspologic.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gm_laplacian` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.laplacian_matrix(G, weight = None).toarray()` |  |
| `gm_laplacian_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.laplacian_matrix(G, weight = 'weight').toarray()` |  |
| `gm_normalized_laplacian` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.normalized_laplacian_matrix(G, weight = None).toarray()` |  |
| `gm_normalized_laplacian` | graspologic | any | differs | directed | direction | abs 1e-14, rel 1e-12 | `graspologic.utils.to_laplacian(A, form = 'I-DAD')` | Undirected fixtures agree. |
| `gm_normalized_laplacian_weighted` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.normalized_laplacian_matrix(G, weight = 'weight').toarray()` |  |
| `gm_normalized_laplacian_weighted` | graspologic | any | differs | directed | direction | abs 1e-14, rel 1e-12 | `graspologic.utils.to_laplacian(W, form = 'I-DAD')` | Undirected fixtures agree. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F072](../../findings.html#f072) | graspologic | convention | The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_graspologic](../../references.html#tool_graspologic), [tool_sknetwork](../../references.html#tool_sknetwork)

## Magnetic laplacian matrix {#cat_laplacian_magnetic_matrix}

Measure id: `cat_laplacian_magnetic_matrix`. Original family: Matrices and spectra.

**Definition.** Magnetic laplacian matrix.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `magnetic_laplacian_matrix` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
