---
title: "All paths"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# All paths {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Path enumeration and counting. Concept id: `all_paths`. 3 measures.

## Definition {#concept-definition}

All paths. Entries grouped here: All Directed Paths; Allpaths; Paths simple.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [All Directed Paths](#cat_all_directed_path) | `cat_all_directed_path` | 1 |
| [Allpaths](#cat_allpaths) | `cat_allpaths` | 1 |
| [Paths simple](#paths_simple) | `paths_simple` | 6 |

## All Directed Paths {#cat_all_directed_path}

Measure id: `cat_all_directed_path`. Original family: Paths and distances.

**Definition.** All Directed Paths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_all_directed_path-jgrapht) | `AllDirectedPaths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_all_directed_path-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: AllDirectedPaths.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Allpaths {#cat_allpaths}

Measure id: `cat_allpaths`. Original family: Communities.

**Definition.** Allpaths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-cat_allpaths-ucinet) | `allpaths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_allpaths-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Paths simple {#paths_simple}

Measure id: `paths_simple`. Original family: Paths and distances.

**Definition.** Paths simple.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `all_simple_edge_paths; all_simple_paths` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_simple-igraph) | `all_simple_paths` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_simple-pyigraph) | `get_all_simple_paths` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_simple-graphtool) | `all_paths` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_simple-networkit) | `AllSimplePaths` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_simple-rustworkx) | `all_simple_paths; digraph_all_simple_paths; graph_all_simple_paths` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_simple-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: all\_simple\_paths.
- <a id="why-paths_simple-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: get\_all\_simple\_paths.
- <a id="why-paths_simple-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: all\_paths.
- <a id="why-paths_simple-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: AllSimplePaths.
- <a id="why-paths_simple-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: all\_simple\_paths; digraph\_all\_simple\_paths; graph\_all\_simple\_paths.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_simple_cutoff4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.all_simple_paths(G, 0, n - 1, cutoff = 4))` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
