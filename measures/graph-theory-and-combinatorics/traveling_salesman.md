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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `traveling_salesman_problem` |  |

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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `asadpour_atsp; christofides; greedy_tsp; simulated_annealing_tsp; threshold_accepting_tsp` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `STSP` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `ChristofidesThreeHalvesApproxMetricTSP; FarthestInsertionHeuristicTSP; GreedyHeuristicTSP; HeldKarpTSP; NearestInsertionHeuristicTSP; NearestNeighborHeuristicTSP; RandomTourTSP; TwoApproxMetricTSP; TwoOptHeuristicTSP` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `metric_tsp_approx` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit)

## Tsp tour {#cat_tour_tsp}

Measure id: `cat_tour_tsp`. Original family: Graph theory and combinatorics.

**Definition.** Tsp tour.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `tsp_tour` | API listing |

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
