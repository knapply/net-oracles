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

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `AllDirectedPaths` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Allpaths {#cat_allpaths}

Measure id: `cat_allpaths`. Original family: Communities.

**Definition.** Allpaths.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | · reported in docs | `allpaths` | API listing |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Paths simple {#paths_simple}

Measure id: `paths_simple`. Original family: Paths and distances.

**Definition.** Paths simple.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `all_simple_edge_paths; all_simple_paths` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `all_simple_paths` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `get_all_simple_paths` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `all_paths` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `AllSimplePaths` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `all_simple_paths; digraph_all_simple_paths; graph_all_simple_paths` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_simple_cutoff4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.all_simple_paths(G, 0, n - 1, cutoff = 4))` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
