---
title: "Label propagation"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Label propagation {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `label_propagation`. 3 measures.

## Definition {#concept-definition}

Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Label propagation](#label_propagation) | `label_propagation` | 7 |
| [Cnx label propagation](#cnx_label_propagation) | `cnx_label_propagation` | 1 |
| [Seeded labels](#cnx_seeded_labels) | `cnx_seeded_labels` | 1 |

## References {#concept-references}

[cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

## Label propagation {#label_propagation}

Measure id: `label_propagation`. Original family: Communities.

**Definition.** Label propagation communities: every node repeatedly takes the dominant label among the nodes it reads.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, multi-edges and self-loops): NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity. [details](#why-label_propagation-networkx) | `asyn_lpa_communities; fast_label_propagation_communities; label_propagation_communities` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): the reference ignores self-loops (a node never reads its own label). [details](#why-label_propagation-igraph) | `cluster_label_prop` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-label_propagation-pyigraph) | `community_label_propagation` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-label_propagation-networkit) | `LPDegreeOrdered; PLP` | API listing |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-label_propagation-sknetwork) | `PropagationClustering` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-label_propagation-jgrapht) | `LabelPropagationClustering` | API listing |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-label_propagation-ucinet) | `labelprop` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-label_propagation-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults, multi-edges and self-loops) on inputs tagged edge\_case, loops and multi\_edges. label\_prop\_quality\_fast and label\_prop\_quality\_retention: NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0). label\_prop\_semisync: NetworkX runs on the simple graph here (parallel edges once, no loops); the reference counts parallel edges with their multiplicity. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0.05, rel 0 on all 2 comparisons where the difference occurs. Mapping: the reference value computed with the adjacency-matrix reading (parallel edges collapse into one tie, self-loops dropped) agrees with the tool within abs 0, rel 0 on all 1 comparison where the difference occurs. Tolerance before mapping: abs 0.05, rel 0; abs 0, rel 0 (0 means exact equality). 3 comparisons differ and 84 agree. Finding F029 (convention): Ties are broken by Python set or insertion order. Findings: [F029](../../findings.html#f029).
- <a id="why-label_propagation-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged loops. the reference ignores self-loops (a node never reads its own label); igraph documents no rule for loops, but its mean on multi\_loops\_und (0.258) is what a node that reads its own label once per loop gives (0.265 over 300 simulated runs, against 0.206 with loops ignored), as NetworkX does. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0.05, rel 0 (0 means exact equality). 1 comparisons differ and 29 agree.
- <a id="why-label_propagation-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_label\_propagation.
- <a id="why-label_propagation-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LPDegreeOrdered; PLP.
- <a id="why-label_propagation-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: PropagationClustering.
- <a id="why-label_propagation-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: LabelPropagationClustering.
- <a id="why-label_propagation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `label_prop_quality` | igraph (R) | undirected | differs | loops | multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over set.seed(1..100) of modularity(g, cluster_label_prop(g, weights = NA))` | the reference ignores self-loops (a node never reads its own label); igraph documents no rule for loops, but its mean on multi\_loops\_und (0.258) is what a node that reads its own label once per loop gives (0.265 over 300 simulated runs, against 0.206 with loops ignored), as NetworkX does |
| `label_prop_quality_fast` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over seeds of modularity(G, fast_label_propagation_communities(simple graph, seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `label_prop_quality_retention` | NetworkX | undirected | differs | edge\_case, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0.05, rel 0 | `mean over seeds of modularity(G, asyn_lpa_communities(simple graph, seed = s))` | NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity; without edges modularity is undefined (the reference reports -1, NetworkX 0) |
| `label_prop_semisync` | NetworkX | undirected | differs | loops, multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.community.label_propagation_communities(simple graph)` | NetworkX runs on the simple graph here (parallel edges once, no loops); the reference counts parallel edges with their multiplicity |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F029](../../findings.html#f029) | NetworkX | convention | Ties are broken by Python set or insertion order |

**References:** [cordasco2010community](../../references.html#cordasco2010community), [raghavan2007near](../../references.html#raghavan2007near), [traag2023large](../../references.html#traag2023large)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_sknetwork](../../references.html#tool_sknetwork)

## Cnx label propagation {#cnx_label_propagation}

Measure id: `cnx_label_propagation`. Original family: Communities.

**Definition.** Cnx label propagation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_label_propagation` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.label_propagation_communities(G) on the simple undirected graph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Seeded labels {#cnx_seeded_labels}

Measure id: `cnx_seeded_labels`. Original family: Communities.

**Definition.** Seeded labels.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_seeded_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under asyn_lpa_communities and fast_label_propagation_communities (simple graph), and asyn_fluidc(k = min(3, n)) on the simple undirected graph (-1 if not connected), each with seed=random.Random(7)` |  |
| `nx_seeded_labels_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
