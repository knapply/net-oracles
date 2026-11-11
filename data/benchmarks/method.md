# Benchmark method

This file describes how the timing rows in `results.csv` were produced. Only the other tools' results are kept. Each row is one tool on one graph and one measure.

## Suites

- `size-ladder`: 24 graphs from about 1,000 to several hundred thousand nodes (road networks, citation graphs, generated random and scale-free graphs). Each tool ran in a fresh process per graph. The time is the median of 3 runs (1 run for betweenness and closeness, which are measured on a sample of sources, as the measure name states). Budget: 240 s per tool and graph. 21 threads were offered to each tool; tools that are single-threaded by design used one.
- `size-ladder-graph-tool`: the same 24 graphs for graph-tool, run in a container image with 5 CPUs and a budget of 600 s per tool and graph, because the tool is distributed as a container image.
- `gap-kernels`: the kernels of the GAP Benchmark Suite (breadth-first search, PageRank, connected components, betweenness on 4 sources) on two generated graphs with about 4.2 million nodes and 128 million edges, with 1 thread and with all offered threads. Budget: 20 s per kernel.
- `python-comparison` and `r-comparison`: a smaller set of measures (degree build, components, betweenness, closeness, harmonic closeness, k-cores, maximal cliques, Louvain communities, triad census, constraint, eigenvector centrality, QAP and MRQAP in R) against NetworkX, igraph, NetworKit and sna. Times are medians of runs of at least 0.2 s. NetworkX and igraph used 1 thread; NetworKit used all offered threads. The R rows come from the printed output of the run and are rounded to 0.1 ms.
- `networkx-backends`: NetworkX functions on sparse, medium and dense generated graphs from 1,000 to 10,000 nodes, with the nx-parallel backend and the graphblas-algorithms backend where they implement the function. Budget: 20 s per call; the time is the cold call, conversion into the backend excluded unless stated.

## Measurement

- Time: wall clock of the measure call after the graph is loaded in memory, unless the measure name says "build".
- Memory: peak resident memory of the process during the call, above the process's resident memory before the graph was read (`peak_megabytes`). For the `gap-kernels` suite the value is the whole-process peak.
- `status` is `over-budget` when the tool did not finish within the budget; `seconds` is then empty.
- `threads` is the number of threads offered to the tool (`all` means every CPU offered to the container).
- Each row records the version of the tool where it was recorded; the main versions are NetworkX 3.7, igraph 1.0.0 (Python) and 2.3.4 (R), NetworKit 11.2.2, graph-tool 3.9 and GAP Benchmark Suite revision 941462c7c42e.

## Hardware

A 24-core x86-64 desktop processor (8 performance cores and 16 efficiency cores) in a Linux container on a Windows host, 16.6 GB of memory for the main runs and 4.9 GB for the graph-tool run. Other workloads on the machine were paused during the main runs. Timings from a different machine will differ; ratios between tools are more portable than absolute times.

## Limits

Results are single runs of a fixed protocol on one machine, not a statistical sample. Default settings of each tool were used. Where two tools compute a measure with different conventions (see the measure pages), the measures are comparable in cost but not identical in output.

## Shared runner and hosted runs

The adapters and the runner in `bench/` (see `bench/README.md`) produce rows in the same format. One adapter per tool gives every tool the same command line, the same graphs (seeded generators and checked downloads, `bench/graphs.yaml`) and the same measure ids (`bench/measures.yaml`). Every (tool, graph, measure) runs in a fresh process; the time is the median of the repeats of the measure call after the graph is built, the memory is the peak resident memory above the process's resident memory before the graph was read, and a run that does not finish within the budget is killed and recorded as `over-budget`. The runner also records the wall time and the child's peak resident memory from the operating system, a short digest of each result (to notice a tool computing something different), and the environment (CPU, cores offered, memory, versions).

Two kinds of rows are kept apart and never combined in one table:

- Headline rows (`results.csv`): dedicated hardware, described in the section above, with other workloads paused.
- Hosted rows (`hosted.csv`, suite `hosted`): the `bench` workflow runs the small and mid suites of the shared runner on GitHub-hosted runners every week and on request. The runner hardware is shared and varies, so each tool and suite records its date, CPU, cores offered, memory and run id in `hosted-environments.json`. Compare tools within one run; absolute times are not comparable with the headline rows. `threads` is the number of threads the tool used (all CPUs offered unless the tool is single-threaded by design). Hosted rows with status `error` mean the tool failed on that graph and measure.

