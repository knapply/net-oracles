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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `directed_combinatorial_laplacian_matrix; directed_laplacian_matrix; laplacian_matrix; normalized_laplacian_matrix` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-igraph) | `laplacian_matrix` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-pyigraph) | `laplacian` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-graphtool) | `laplacian` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-networkit) | `laplacianMatrix` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-sknetwork) | `Laplacian` | API listing |
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gm_laplacian-centiserve) | `laplacian` | API listing |
| [graspologic](../../tools/graspologic.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction): For a directed graph graspologic's 'I-DAD' form is D\_in^-1/2 (D\_in - A) D\_in^-1/2 with in-degrees (graspologic/utils/utils.py, to\_laplacian), and a... [details](#why-gm_laplacian-graspologic) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gm_laplacian-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: laplacian\_matrix.
- <a id="why-gm_laplacian-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: laplacian.
- <a id="why-gm_laplacian-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: laplacian.
- <a id="why-gm_laplacian-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: laplacianMatrix.
- <a id="why-gm_laplacian-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Laplacian.
- <a id="why-gm_laplacian-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: laplacian.
- <a id="why-gm_laplacian-graspologic"></a>**[graspologic](../../tools/graspologic.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> graspologic 3.4.4 was run and its value differs from the reference value by convention (direction) on inputs tagged directed. For a directed graph graspologic's 'I-DAD' form is D\_in^-1/2 (D\_in - A) D\_in^-1/2 with in-degrees (graspologic/utils/utils.py, to\_laplacian), and a node without in-links gets 0 on the diagonal; the reference, like NetworkX's normalized\_laplacian\_matrix, normalizes by out-degrees. Undirected fixtures agree. Relation to the reference value: Degree used: the 'I-DAD' form normalizes by in-degrees and gives a node without in-links 0 on the diagonal; the reference value and NetworkX use out-degrees; undirected agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 8 comparisons differ and 27 agree. Finding F072 (convention): The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs. Findings: [F072](../../findings.html#f072).

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_laplacian_magnetic_matrix-networkx) | `magnetic_laplacian_matrix` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_laplacian_magnetic_matrix-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: magnetic\_laplacian\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
