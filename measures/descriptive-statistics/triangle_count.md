---
title: "Triangle count"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Triangle count {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Clustering and transitivity. Concept id: `triangle_count`. 1 measure.

## Definition {#concept-definition}

Number of triangles at each node of the simple undirected reading of the network.

## References {#concept-references}

[chiba1985arboricity](../../references.html#chiba1985arboricity)

## Triangles {#nxo_triangles}

Measure id: `nxo_triangles`. Original family: Descriptive statistics.

**Definition.** Number of triangles at each node of the simple undirected reading of the network.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `all_triangles; triangles` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxo_triangles-igraph) | `count_triangles; triangles` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxo_triangles-pyigraph) | `list_triangles` | API listing |
| [ergm (statnet)](../../tools/ergm.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxo_triangles-ergm) | `triangle` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxo_triangles-sknetwork) | `count_triangles` | API listing |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [details](#why-nxo_triangles-gephi) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxo_triangles-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: count\_triangles; triangles.
- <a id="why-nxo_triangles-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: list\_triangles.
- <a id="why-nxo_triangles-ergm"></a>**[ergm (statnet)](../../tools/ergm.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. ergm (statnet) 4.12.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms()); API names: triangle.
- <a id="why-nxo_triangles-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: count\_triangles.
- <a id="why-nxo_triangles-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (multi-edges and self-loops) on the fixtures multi\_loops\_und. Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). Relation to the reference value: Self-loops: a loop enters the neighbourhood; removing loops gives the simple-graph value. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_triangles` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.triangles(nx.Graph(G))` |  |
| `nxo_triangles` | GraphBLAS algorithms | undirected | agrees |  |  | abs 0, rel 0 | `nx.triangles(G simple without loops, backend = 'graphblas')` |  |
| `nxo_triangles_sorted` | Gephi toolkit | undirected | differs |  | multi\_edges, self\_loops | abs 0, rel 0 | `Gephi toolkit 0.11.3: ClusteringCoefficient.getTriangesReuslts() (setDirected(false)), sorted: the array is in an internal node order` | Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the simple-graph definition, which this reference and the definition oracle follow; parallel edges do not change them (checked on multi\_loops\_und and multi\_loops\_dir). |

**References:** [chiba1985arboricity](../../references.html#chiba1985arboricity)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
