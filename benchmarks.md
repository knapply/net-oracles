---
title: Benchmarks
layout: default
nav_order: 6
---

{% raw %}

# Benchmarks

Timings and memory of other tools only. Raw rows: `data/benchmarks/results.csv`. Method:


This file describes how the timing rows in `results.csv` were produced. Only the other tools' results are kept. Each row is one tool on one graph and one measure.

### Suites

- `size-ladder`: 24 graphs from about 1,000 to several hundred thousand nodes (road networks, citation graphs, generated random and scale-free graphs). Each tool ran in a fresh process per graph. The time is the median of 3 runs (1 run for betweenness and closeness, which are measured on a sample of sources, as the measure name states). Budget: 240 s per tool and graph. 21 threads were offered to each tool; tools that are single-threaded by design used one.
- `size-ladder-graph-tool`: the same 24 graphs for graph-tool, run in a container image with 5 CPUs and a budget of 600 s per tool and graph, because the tool is distributed as a container image.
- `gap-kernels`: the kernels of the GAP Benchmark Suite (breadth-first search, PageRank, connected components, betweenness on 4 sources) on two generated graphs with about 4.2 million nodes and 128 million edges, with 1 thread and with all offered threads. Budget: 20 s per kernel.
- `python-comparison` and `r-comparison`: a smaller set of measures (degree build, components, betweenness, closeness, harmonic closeness, k-cores, maximal cliques, Louvain communities, triad census, constraint, eigenvector centrality, QAP and MRQAP in R) against NetworkX, igraph, NetworKit and sna. Times are medians of runs of at least 0.2 s. NetworkX and igraph used 1 thread; NetworKit used all offered threads. The R rows come from the printed output of the run and are rounded to 0.1 ms.
- `networkx-backends`: NetworkX functions on sparse, medium and dense generated graphs from 1,000 to 10,000 nodes, with the nx-parallel backend and the graphblas-algorithms backend where they implement the function. Budget: 20 s per call; the time is the cold call, conversion into the backend excluded unless stated.

### Measurement

- Time: wall clock of the measure call after the graph is loaded in memory, unless the measure name says "build".
- Memory: peak resident memory of the process during the call, above the process's resident memory before the graph was read (`peak_megabytes`). For the `gap-kernels` suite the value is the whole-process peak.
- `status` is `over-budget` when the tool did not finish within the budget; `seconds` is then empty.
- `threads` is the number of threads offered to the tool (`all` means every CPU offered to the container).
- Each row records the version of the tool where it was recorded; the main versions are NetworkX 3.7, igraph 1.0.0 (Python) and 2.3.4 (R), NetworKit 11.2.2, graph-tool 3.9 and GAP Benchmark Suite revision 941462c7c42e.

### Hardware

A 24-core x86-64 desktop processor (8 performance cores and 16 efficiency cores) in a Linux container on a Windows host, 16.6 GB of memory for the main runs and 4.9 GB for the graph-tool run. Other workloads on the machine were paused during the main runs. Timings from a different machine will differ; ratios between tools are more portable than absolute times.

### Limits

Results are single runs of a fixed protocol on one machine, not a statistical sample. Default settings of each tool were used. Where two tools compute a measure with different conventions (see the measure pages), the measures are comparable in cost but not identical in output.

## Summary by suite

| Suite | Tool | Rows | Graphs | Measures | Over budget |
|---|---|---|---|---|---|
| gap-kernels | GAP Benchmark Suite | 24 | 4 | 6 | 0 |
| networkx-backends | GraphBLAS algorithms | 60 | 7 | 10 | 0 |
| networkx-backends | NetworkX | 347 | 14 | 57 | 52 |
| networkx-backends | nx-parallel | 64 | 7 | 12 | 14 |
| python-comparison | NetworKit | 8 | 3 | 7 | 0 |
| python-comparison | NetworkX | 25 | 8 | 10 | 0 |
| python-comparison | igraph (Python) | 19 | 8 | 9 | 0 |
| r-comparison | igraph (R) | 25 | 7 | 10 | 0 |
| r-comparison | sna | 6 | 2 | 6 | 0 |
| size-ladder | GAP Benchmark Suite | 114 | 24 | 5 | 0 |
| size-ladder | igraph (R) | 156 | 24 | 7 | 0 |
| size-ladder | NetworKit | 155 | 24 | 7 | 0 |
| size-ladder | NetworkX | 64 | 10 | 7 | 0 |
| size-ladder-graph-tool | graph-tool | 161 | 24 | 7 | 0 |

## Median time per measure: gap-kernels

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| betweenness (4 sources) | GAP Benchmark Suite | 4 | 4 | 4.421 | 629.5 |
| bfs | GAP Benchmark Suite | 4 | 4 | 0.05286 | 568 |
| [components](measures/components-and-connectivity/connected_components.html#components) | GAP Benchmark Suite | 4 | 4 | 0.09574 | 568.5 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | GAP Benchmark Suite | 4 | 4 | 0.9395 | 569 |
| sssp | GAP Benchmark Suite | 4 | 4 | 0.5963 | 1141 |
| triangle count | GAP Benchmark Suite | 4 | 4 | 8.89 | 877.5 |

## Median time per measure: networkx-backends

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| adjacency\_matrix (weighted) | NetworkX | 7 | 7 | 0.0427 |  |
| all\_pairs\_dijkstra\_path\_length (weighted) | NetworkX | 3 | 2 | 2.495 |  |
| all\_pairs\_dijkstra\_path\_length (weighted) | nx-parallel | 3 | 2 | 2.5 |  |
| all\_pairs\_shortest\_path\_length | GraphBLAS algorithms | 4 | 4 | 0.0389 |  |
| all\_pairs\_shortest\_path\_length | NetworkX | 4 | 4 | 0.178 |  |
| all\_pairs\_shortest\_path\_length | nx-parallel | 4 | 4 | 0.186 |  |
| average\_neighbor\_degree | NetworkX | 7 | 7 | 0.00849 |  |
| average\_neighbor\_degree | nx-parallel | 7 | 7 | 0.327 |  |
| average\_shortest\_path\_length | NetworkX | 7 | 4 | 0.186 |  |
| betweenness\_centrality | NetworkX | 6 | 3 | 1.95 |  |
| betweenness\_centrality | nx-parallel | 6 | 3 | 0.424 |  |
| betweenness\_centrality (weighted) | NetworkX | 6 | 2 | 4.245 |  |
| betweenness\_centrality (weighted) | nx-parallel | 6 | 3 | 1.2 |  |
| betweenness\_centrality\_subset | NetworkX | 6 | 6 | 1.377 |  |
| bfs\_edges | NetworkX | 7 | 7 | 0.00123 |  |
| biconnected\_components | NetworkX | 7 | 7 | 0.0369 |  |
| closeness\_centrality | NetworkX | 7 | 4 | 0.1745 |  |
| [clustering](measures/descriptive-statistics/local_clustering.html#clustering) | GraphBLAS algorithms | 7 | 7 | 0.00667 |  |
| [clustering](measures/descriptive-statistics/local_clustering.html#clustering) | NetworkX | 7 | 6 | 0.4515 |  |
| [clustering](measures/descriptive-statistics/local_clustering.html#clustering) | nx-parallel | 7 | 7 | 0.661 |  |
| clustering (weighted) | GraphBLAS algorithms | 7 | 7 | 0.00819 |  |
| clustering (weighted) | NetworkX | 7 | 6 | 0.798 |  |
| clustering (weighted) | nx-parallel | 7 | 6 | 0.475 |  |
| [condensation](measures/components-and-connectivity/condensation.html#condensation) | NetworkX | 7 | 7 | 0.0131 |  |
| conductance | GraphBLAS algorithms | 7 | 7 | 0.0018 |  |
| conductance | NetworkX | 7 | 7 | 0.0125 |  |
| connected\_components | NetworkX | 7 | 7 | 0.000525 |  |
| [constraint](measures/roles-and-positions/burt_constraint.html#constraint) | NetworkX | 7 | 7 | 0.116 |  |
| core\_number | NetworkX | 7 | 7 | 0.0182 |  |
| current\_flow\_betweenness\_centrality | NetworkX | 3 | 2 | 7.23 |  |
| [cycle\_basis](measures/graph-theory-and-combinatorics/cycle_basis.html#cycle_basis) | NetworkX | 6 | 6 | 0.2318 |  |
| degree\_assortativity\_coefficient | NetworkX | 7 | 7 | 0.0611 |  |
| [diameter](measures/paths-and-distances/diameter.html#diameter) | NetworkX | 7 | 4 | 0.195 |  |
| edge\_betweenness\_centrality | NetworkX | 6 | 2 | 3.015 |  |
| edge\_betweenness\_centrality | nx-parallel | 6 | 3 | 0.988 |  |
| edge\_connectivity | NetworkX | 4 | 4 | 0.4295 |  |
| edge\_dfs | NetworkX | 7 | 7 | 0.573 |  |
| edge\_disjoint\_paths | NetworkX | 7 | 7 | 0.301 |  |
| edmonds\_karp (weighted) | NetworkX | 7 | 7 | 0.298 |  |
| eigenvector\_centrality\_numpy | NetworkX | 7 | 7 | 0.0561 |  |
| find\_cliques | NetworkX | 5 | 5 | 0.289 |  |
| floyd\_warshall (weighted) | GraphBLAS algorithms | 3 | 3 | 3.26 |  |
| floyd\_warshall (weighted) | NetworkX | 3 | 0 |  |  |
| global\_efficiency | NetworkX | 7 | 4 | 0.1975 |  |
| [greedy\_color](measures/graph-theory-and-combinatorics/vertex_coloring.html#greedy_color) | NetworkX | 7 | 7 | 0.00796 |  |
| harmonic\_centrality | NetworkX | 7 | 4 | 0.256 |  |
| harmonic\_centrality | nx-parallel | 7 | 6 | 3.776 |  |
| [hits](measures/centrality/hits.html#hits) | NetworkX | 7 | 7 | 0.0695 |  |
| hyper\_wiener\_index | NetworkX | 6 | 4 | 0.1915 |  |
| jaccard\_coefficient | NetworkX | 4 | 3 | 2.18 |  |
| jaccard\_coefficient | nx-parallel | 4 | 3 | 0.406 |  |
| [k\_truss](measures/cohesion-and-subgroups/k_truss.html#k_truss) | GraphBLAS algorithms | 7 | 7 | 0.0083 |  |
| [k\_truss](measures/cohesion-and-subgroups/k_truss.html#k_truss) | NetworkX | 7 | 6 | 0.3405 |  |
| load\_centrality | NetworkX | 6 | 3 | 2.9 |  |
| local\_efficiency | NetworkX | 3 | 2 | 0.4225 |  |
| local\_efficiency | nx-parallel | 3 | 3 | 0.168 |  |
| louvain\_communities | NetworkX | 7 | 7 | 0.997 |  |
| maximum\_branching (weighted) | NetworkX | 4 | 1 | 11.1 |  |
| minimum\_spanning\_tree (weighted) | NetworkX | 7 | 7 | 0.497 |  |
| number\_of\_walks (length 3) | NetworkX | 3 | 3 | 6.07 |  |
| onion\_layers | NetworkX | 7 | 7 | 0.0377 |  |
| [pagerank](measures/centrality/pagerank.html#pagerank) | GraphBLAS algorithms | 7 | 7 | 0.0031 |  |
| [pagerank](measures/centrality/pagerank.html#pagerank) | NetworkX | 7 | 7 | 0.0446 |  |
| second\_order\_centrality | NetworkX | 3 | 3 | 7.07 |  |
| shortest\_simple\_paths (20 paths) | NetworkX | 6 | 6 | 0.00226 |  |
| single\_source\_bellman\_ford\_path\_length (weighted) | GraphBLAS algorithms | 7 | 7 | 0.00299 |  |
| single\_source\_bellman\_ford\_path\_length (weighted) | NetworkX | 7 | 7 | 0.0476 |  |
| single\_source\_dijkstra (weighted) | NetworkX | 7 | 7 | 0.0305 |  |
| [square\_clustering](measures/descriptive-statistics/square_clustering.html#square_clustering) | GraphBLAS algorithms | 4 | 4 | 0.008435 |  |
| [square\_clustering](measures/descriptive-statistics/square_clustering.html#square_clustering) | NetworkX | 4 | 3 | 0.32 |  |
| [square\_clustering](measures/descriptive-statistics/square_clustering.html#square_clustering) | nx-parallel | 4 | 3 | 0.0681 |  |
| strongly\_connected\_components | NetworkX | 7 | 7 | 0.00266 |  |
| topological\_sort (DAG) | NetworkX | 7 | 7 | 0.0129 |  |
| transitive\_reduction (DAG) | NetworkX | 4 | 4 | 0.005435 |  |
| [transitivity](measures/descriptive-statistics/global_transitivity.html#transitivity) | GraphBLAS algorithms | 7 | 7 | 0.00403 |  |
| [transitivity](measures/descriptive-statistics/global_transitivity.html#transitivity) | NetworkX | 7 | 6 | 0.604 |  |
| triadic\_census | NetworkX | 7 | 3 | 3.65 |  |
| vf2pp\_is\_isomorphic | NetworkX | 7 | 5 | 0.31 |  |
| weisfeiler\_lehman\_graph\_hash | NetworkX | 7 | 7 | 0.0472 |  |

## Median time per measure: python-comparison

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| [betweenness](measures/centrality/betweenness.html#betweenness) | NetworKit | 2 | 2 | 0.2638 |  |
| [betweenness](measures/centrality/betweenness.html#betweenness) | NetworkX | 6 | 6 | 14.62 |  |
| [betweenness](measures/centrality/betweenness.html#betweenness) | igraph (Python) | 6 | 6 | 0.4909 |  |
| [closeness](measures/centrality/closeness.html#closeness) | NetworkX | 6 | 6 | 5.667 |  |
| [components](measures/components-and-connectivity/connected_components.html#components) | NetworKit | 1 | 1 | 0.003536 |  |
| [components](measures/components-and-connectivity/connected_components.html#components) | NetworkX | 1 | 1 | 0.05599 |  |
| [components](measures/components-and-connectivity/connected_components.html#components) | igraph (Python) | 1 | 1 | 0.001698 |  |
| [constraint](measures/roles-and-positions/burt_constraint.html#constraint) | NetworkX | 1 | 1 | 0.01158 |  |
| [constraint](measures/roles-and-positions/burt_constraint.html#constraint) | igraph (Python) | 1 | 1 | 0.001109 |  |
| eigenvector centrality | NetworKit | 1 | 1 | 0.02026 |  |
| eigenvector centrality | NetworkX | 1 | 1 | 0.5315 |  |
| eigenvector centrality | igraph (Python) | 1 | 1 | 0.2807 |  |
| harmonic centrality | NetworKit | 1 | 1 | 0.2209 |  |
| harmonic centrality | NetworkX | 6 | 6 | 7.065 |  |
| harmonic centrality | igraph (Python) | 6 | 6 | 0.3796 |  |
| k-cores | NetworKit | 1 | 1 | 0.002369 |  |
| k-cores | NetworkX | 1 | 1 | 0.4322 |  |
| k-cores | igraph (Python) | 1 | 1 | 0.005781 |  |
| Louvain communities | NetworKit | 1 | 1 | 0.1101 |  |
| Louvain communities | NetworkX | 1 | 1 | 151.8 |  |
| Louvain communities | igraph (Python) | 1 | 1 | 11.34 |  |
| maximal cliques | NetworKit | 1 | 1 | 0.08979 |  |
| maximal cliques | NetworkX | 1 | 1 | 1.133 |  |
| maximal cliques | igraph (Python) | 1 | 1 | 1.045 |  |
| triad census | NetworkX | 1 | 1 | 0.7426 |  |
| triad census | igraph (Python) | 1 | 1 | 0.01508 |  |

## Median time per measure: r-comparison

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| [betweenness](measures/centrality/betweenness.html#betweenness) | igraph (R) | 6 | 6 | 4.486 |  |
| [betweenness](measures/centrality/betweenness.html#betweenness) | sna | 1 | 1 | 1.615 |  |
| [brokerage](measures/roles-and-positions/brokerage.html#brokerage) | sna | 1 | 1 | 0.1033 |  |
| [closeness](measures/centrality/closeness.html#closeness) | igraph (R) | 6 | 6 | 2.664 |  |
| [components](measures/components-and-connectivity/connected_components.html#components) | igraph (R) | 1 | 1 | 0.0003 |  |
| [constraint](measures/roles-and-positions/burt_constraint.html#constraint) | igraph (R) | 1 | 1 | 0.0067 |  |
| eigenvector centrality | igraph (R) | 1 | 1 | 0.197 |  |
| harmonic centrality | igraph (R) | 6 | 6 | 2.623 |  |
| k-cores | igraph (R) | 1 | 1 | 0.007 |  |
| Louvain communities | igraph (R) | 1 | 1 | 15.67 |  |
| maximal cliques | igraph (R) | 1 | 1 | 3.486 |  |
| MRQAP (DSP) | sna | 1 | 1 | 21.67 |  |
| QAP correlation | sna | 1 | 1 | 0.618 |  |
| structural equivalence | sna | 1 | 1 | 121.8 |  |
| triad census | igraph (R) | 1 | 1 | 0.0352 |  |
| triad census | sna | 1 | 1 | 140.8 |  |

## Median time per measure: size-ladder

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| betweenness (16 sources) | GAP Benchmark Suite | 24 | 24 | 0.01828 | 7.3 |
| betweenness (16 sources) | igraph (R) | 24 | 24 | 0.03139 | 28.65 |
| betweenness (16 sources) | NetworKit | 24 | 24 | 0.03223 | 99.75 |
| betweenness (16 sources) | NetworkX | 10 | 10 | 0.2733 | 32.6 |
| bfs | GAP Benchmark Suite | 24 | 24 | 0.0002 | 6.5 |
| bfs | igraph (R) | 24 | 24 | 0.001472 | 26.25 |
| bfs | NetworKit | 24 | 24 | 0.0008986 | 15.25 |
| bfs | NetworkX | 10 | 10 | 0.002831 | 15.6 |
| [closeness](measures/centrality/closeness.html#closeness) | igraph (R) | 12 | 12 | 5.72 | 8.4 |
| [closeness](measures/centrality/closeness.html#closeness) | NetworKit | 17 | 17 | 0.4045 | 50 |
| [closeness](measures/centrality/closeness.html#closeness) | NetworkX | 4 | 4 | 5.703 | 25.75 |
| [components](measures/components-and-connectivity/connected_components.html#components) | GAP Benchmark Suite | 24 | 24 | 0.00072 | 6.45 |
| [components](measures/components-and-connectivity/connected_components.html#components) | igraph (R) | 24 | 24 | 0.001454 | 26.3 |
| [components](measures/components-and-connectivity/connected_components.html#components) | NetworKit | 24 | 24 | 0.002213 | 15.4 |
| [components](measures/components-and-connectivity/connected_components.html#components) | NetworkX | 10 | 10 | 0.003709 | 15.45 |
| load (read and build; memory = resident graph) | igraph (R) | 24 | 24 | 0.04654 | 26.21 |
| load (read and build; memory = resident graph) | NetworKit | 24 | 24 | 0.01752 | 15.01 |
| load (read and build; memory = resident graph) | NetworkX | 10 | 10 | 0.02982 | 15.2 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | GAP Benchmark Suite | 24 | 24 | 0.004435 | 6.65 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | igraph (R) | 24 | 24 | 0.0133 | 28.55 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | NetworKit | 24 | 24 | 0.002163 | 15.85 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | NetworkX | 10 | 10 | 0.03558 | 34.1 |
| triangles | GAP Benchmark Suite | 18 | 18 | 0.00102 | 7.1 |
| triangles | igraph (R) | 24 | 24 | 0.01993 | 28.65 |
| triangles | NetworKit | 18 | 18 | 0.003354 | 9.65 |
| triangles | NetworkX | 10 | 10 | 0.03577 | 31.25 |

## Median time per measure: size-ladder-graph-tool

Median over the graphs on which the tool finished within the budget; threads as in the data file.

| Measure | Tool | Graphs | Finished | Median seconds | Median peak MB |
|---|---|---|---|---|---|
| betweenness (16 sources) | graph-tool | 24 | 24 | 0.0294 | 38.8 |
| bfs | graph-tool | 24 | 24 | 0.001123 | 3.55 |
| [closeness](measures/centrality/closeness.html#closeness) | graph-tool | 17 | 17 | 3.258 | 21.4 |
| [components](measures/components-and-connectivity/connected_components.html#components) | graph-tool | 24 | 24 | 0.002662 | 3.7 |
| load (read and build; memory = resident graph) | graph-tool | 24 | 24 | 0.03632 | 1.469 |
| [pagerank](measures/centrality/pagerank.html#pagerank) | graph-tool | 24 | 24 | 0.01643 | 4.6 |
| triangles | graph-tool | 24 | 24 | 0.01899 | 6.75 |
{% endraw %}
