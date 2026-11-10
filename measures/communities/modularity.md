---
title: "Modularity"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Modularity {#concept-top}

Family: [Communities](index.html). Subfamily: Partition and cover quality. Concept id: `modularity`. 3 measures.

## Definition {#concept-definition}

Modularity. Entries grouped here: Modularity; Modularity nx; Modularity State.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Modularity](#modularity) | `modularity` | 11 |
| [Modularity nx](#cnx_modularity_nx) | `cnx_modularity_nx` | 1 |
| [Modularity State](#cat_modularity_state) | `cat_modularity_state` | 1 |

## Modularity {#modularity}

Measure id: `modularity`. Original family: Communities.

**Definition.** Modularity.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): NetworkX returns 0 for a network without edges. [details](#why-modularity-networkx) | `modularity` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `modularity` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `modularity` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-modularity-graphtool) | `modularity` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `Modularity` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, normalization and self-loops): scikit-network reads the adjacency matrix, where an undirected self-loop is 1 on the diagonal and adds 1 to the degree. [details](#why-modularity-sknetwork) | `get_modularity` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-modularity-jgrapht) | `NaiveGreedyModularityAlgorithm; UndirectedModularityMeasurer` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-modularity-bct) | `modularity_dir; modularity_und; modularity_und_sign` | API listing |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-modularity-gephi) | `Modularity` | API listing |
| [cdlib](../../tools/cdlib.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges and self-loops): cdlib's newman\_girvan\_modularity counts the parallel edges inside a community once while the edge total and the degrees count every copy (a triangle... [details](#why-modularity-cdlib) |  |  |
| [graspologic](../../tools/graspologic.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, multi-edges, normalization, self-loops and weights): graspologic-native adds an undirected self-loop's weight once to the community's internal weight but twice to the node's degree (exact rational... [details](#why-modularity-graspologic) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-modularity-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults) on inputs tagged edge\_case and edgeless. modularity and modularity\_resolution: NetworkX returns 0 for a network without edges; this reference and igraph return NaN. modularity\_weighted: Without edges modularity is 0 / 0; NetworkX returns 0, the reference NaN. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 4 comparisons differ and 95 agree. Finding F035 (convention): Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input. Findings: [F035](../../findings.html#f035).
- <a id="why-modularity-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: modularity.
- <a id="why-modularity-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> scikit-network 0.33.0 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, normalization and self-loops) on inputs tagged loops. modularity: scikit-network reads the adjacency matrix, where an undirected self-loop is 1 on the diagonal and adds 1 to the degree; the reference, like igraph and NetworkX, counts it twice in both (exact rational evaluation of both conventions reproduces each tool's value on multi\_loops\_und). modularity\_resolution and modularity\_weighted: An undirected self-loop counts once on the diagonal and in the degree in scikit-network, twice in the reference (see modularity). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 2 comparisons differ and 57 agree.
- <a id="why-modularity-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: NaiveGreedyModularityAlgorithm; UndirectedModularityMeasurer.
- <a id="why-modularity-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: modularity\_dir; modularity\_und; modularity\_und\_sign.
- <a id="why-modularity-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Gephi toolkit 0.11.3 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Gephi toolkit 0.11.3 javadoc (published class list of org.gephi.statistics.plugin)); API names: Modularity.
- <a id="why-modularity-cdlib"></a>**[cdlib](../../tools/cdlib.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> cdlib 0.4.1 was run and its value differs from the reference value by convention (direction, multi-edges and self-loops) on inputs tagged multi\_edges. cdlib's newman\_girvan\_modularity counts the parallel edges inside a community once while the edge total and the degrees count every copy (a triangle with one doubled edge, communities {0, 1} and {2}: cdlib -0.375, NetworkX and the reference -0.125); with loops but no parallel edges it agrees. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 1 comparisons differ and 17 agree.
- <a id="why-modularity-graspologic"></a>**[graspologic](../../tools/graspologic.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> graspologic 3.4.4 was run and its value differs from the reference value by convention (direction, multi-edges, normalization, self-loops and weights) on inputs tagged loops. modularity: graspologic-native adds an undirected self-loop's weight once to the community's internal weight but twice to the node's degree (exact rational evaluation of that convention reproduces -0.090567 on multi\_loops\_und); the reference, igraph and NetworkX count it twice in both. modularity\_resolution and modularity\_weighted: A self-loop counts once in the internal weight and twice in the degree in graspologic-native (see modularity). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). 2 comparisons differ and 39 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `modularity` | NetworkX | any | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, blocks, weight = None) on the multigraph` | NetworkX returns 0 for a network without edges; this reference and igraph return NaN. |
| `modularity` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::modularity(g, blocks, weights = rep(1, m), directed = TRUE)` |  |
| `modularity` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: [g.modularity(blocks, weights=None, resolution=1.0, directed=True)]` |  |
| `modularity` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.community.Modularity().getQuality(blocks3 partition, G)` |  |
| `modularity` | scikit-network | any | differs | loops | defaults, direction, multi\_edges, normalization, self\_loops | abs 1e-14, rel 1e-12 | `sknetwork.clustering.get_modularity(A, blocks3 labels)` | scikit-network reads the adjacency matrix, where an undirected self-loop is 1 on the diagonal and adds 1 to the degree; the reference, like igraph and NetworkX, counts it twice in both (exact rational evaluation of both conventions reproduces each tool's value on multi\_loops\_und). scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `modularity` | cdlib | any | differs | multi\_edges, (no value) directed | direction, multi\_edges, self\_loops | abs 1e-14, rel 1e-12 | `cdlib.evaluation.newman_girvan_modularity(MultiGraph, blocks3)` | cdlib's newman\_girvan\_modularity counts the parallel edges inside a community once while the edge total and the degrees count every copy (a triangle with one doubled edge, communities {0, 1} and {2}: cdlib -0.375, NetworkX and the reference -0.125); with loops but no parallel edges it agrees. newman\_girvan\_modularity is the undirected measure; directed fixtures are not passed. |
| `modularity` | graspologic | any | differs | loops, (no value) directed | direction, multi\_edges, normalization, self\_loops, weights | abs 1e-14, rel 1e-12 | `graspologic.partition.modularity(G summed, blocks3, weight_attribute = 'weight')` | graspologic-native adds an undirected self-loop's weight once to the community's internal weight but twice to the node's degree (exact rational evaluation of that convention reproduces -0.090567 on multi\_loops\_und); the reference, igraph and NetworkX count it twice in both. graspologic's modularity is for undirected graphs. |
| `modularity_resolution` | NetworkX | any | differs | edge\_case | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, blocks, weight = None, resolution = 0.5)` | NetworkX returns 0 for a network without edges; this reference and igraph return NaN. |
| `modularity_resolution` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::modularity(g, blocks, weights = rep(1, m), resolution = 0.5)` |  |
| `modularity_resolution` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: [g.modularity(blocks, weights=None, resolution=0.5, directed=True)]` |  |
| `modularity_resolution` | scikit-network | any | differs | loops | defaults, direction, normalization, self\_loops | abs 1e-14, rel 1e-12 | `sknetwork.clustering.get_modularity(A, blocks3 labels, resolution = 0.5)` | An undirected self-loop counts once on the diagonal and in the degree in scikit-network, twice in the reference (see modularity). scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `modularity_resolution` | graspologic | any | differs | loops, (no value) directed | direction, normalization, self\_loops, weights | abs 1e-14, rel 1e-12 | `graspologic.partition.modularity(G summed, blocks3, resolution = 0.5)` | A self-loop counts once in the internal weight and twice in the degree in graspologic-native (see modularity). graspologic's modularity is for undirected graphs. |
| `modularity_weighted` | NetworkX | any | differs | edgeless | defaults | abs 1e-14, rel 1e-12 | `nx.community.modularity(G, blocks, weight = 'weight')` | Without edges modularity is 0 / 0; NetworkX returns 0, the reference NaN. |
| `modularity_weighted` | igraph (R) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `igraph::modularity(g, blocks, weights = E(g)$weight)` |  |
| `modularity_weighted` | igraph (Python) | any | agrees |  |  | abs 1e-14, rel 1e-12 | `python-igraph: [g.modularity(blocks, weights=w, resolution=1.0, directed=True)],` |  |
| `modularity_weighted` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `nk.community.Modularity().getQuality(blocks3 partition, G_weighted)` |  |
| `modularity_weighted` | scikit-network | any | differs | loops | direction, normalization, self\_loops | abs 1e-14, rel 1e-12 | `sknetwork.clustering.get_modularity(W, blocks3 labels)` | An undirected self-loop counts once on the diagonal and in the degree in scikit-network, twice in the reference (see modularity). |
| `modularity_weighted` | graspologic | any | differs | loops, (no value) directed | direction, normalization, self\_loops, weights | abs 1e-14, rel 1e-12 | `graspologic.partition.modularity(G summed weights, blocks3, weight_attribute = 'weight')` | A self-loop counts once in the internal weight and twice in the degree in graspologic-native (see modularity). graspologic's modularity is for undirected graphs. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F035](../../findings.html#f035) | NetworkX | convention | Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [rubinov2010complex](../../references.html#rubinov2010complex), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_cdlib](../../references.html#tool_cdlib), [tool_graspologic](../../references.html#tool_graspologic), [tool_sknetwork](../../references.html#tool_sknetwork)

## Modularity nx {#cnx_modularity_nx}

Measure id: `cnx_modularity_nx`. Original family: Communities.

**Definition.** Modularity nx.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_modularity_nx` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.community.modularity(G_natural, blocks, weight = 'weight' if weighted)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Modularity State {#cat_modularity_state}

Measure id: `cat_modularity_state`. Original family: Communities.

**Definition.** Modularity State.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_modularity_state-graphtool) | `ModularityState` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_modularity_state-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: ModularityState.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
