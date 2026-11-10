---
title: "Traveling salesman"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Traveling salesman {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Eulerian paths, Hamiltonian paths and tours. Concept id: `traveling_salesman`. 3 measures.

## Definition {#concept-definition}

Traveling salesman. Entries grouped here: St tsp; Traveling salesman (exact and heuristic); Tsp tour.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [St tsp](#st_tsp) | `st_tsp` | 1 |
| [Traveling salesman (exact and heuristic)](#tsp) | `tsp` | 4 |
| [Tsp tour](#cat_tour_tsp) | `cat_tour_tsp` | 1 |

## St tsp {#st_tsp}

Measure id: `st_tsp`. Original family: Graph theory and combinatorics.

**Definition.** St tsp.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `traveling_salesman_problem` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_tsp` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `traveling_salesman_problem(G) (Christofides), (G, method=greedy_tsp), (G, cycle=False), each with its length first; [-1] if G is disconnected or has fewer than two nodes` |  |
| `st_tsp_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's walks` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Traveling salesman (exact and heuristic) {#tsp}

Measure id: `tsp`. Original family: Graph theory and combinatorics.

**Definition.** Traveling salesman (exact and heuristic).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-tsp-networkx) | `asadpour_atsp; christofides; greedy_tsp; simulated_annealing_tsp; threshold_accepting_tsp` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-tsp-networkit) | `STSP` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-tsp-jgrapht) | `ChristofidesThreeHalvesApproxMetricTSP; FarthestInsertionHeuristicTSP; GreedyHeuristicTSP; HeldKarpTSP; NearestInsertionHeuristicTSP; NearestNeighborHeuristicTSP; RandomTourTSP; TwoApproxMetricTSP; TwoOptHeuristicTSP` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-tsp-boost) | `metric_tsp_approx` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-tsp-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: asadpour\_atsp; christofides; greedy\_tsp; simulated\_annealing\_tsp; threshold\_accepting\_tsp.
- <a id="why-tsp-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: STSP.
- <a id="why-tsp-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: ChristofidesThreeHalvesApproxMetricTSP; FarthestInsertionHeuristicTSP; GreedyHeuristicTSP; HeldKarpTSP; NearestInsertionHeuristicTSP; NearestNeighborHeuristicTSP; RandomTourTSP; TwoApproxMetricTSP; TwoOptHeuristicTSP.
- <a id="why-tsp-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: metric\_tsp\_approx.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Tsp tour {#cat_tour_tsp}

Measure id: `cat_tour_tsp`. Original family: Graph theory and combinatorics.

**Definition.** Tsp tour.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_tour_tsp-graphtool) | `tsp_tour` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_tour_tsp-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: tsp\_tour.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
