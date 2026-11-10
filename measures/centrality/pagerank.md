---
title: "PageRank"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# PageRank {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `pagerank`. 5 measures.

## Definition {#concept-definition}

PageRank of every node by power iteration (Brin and Page 1998), with a GAP-suite preset.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Pagerank](#pagerank) | `pagerank` | 12 |
| [Google](#nxp_google) | `nxp_google` | 1 |
| [Local and approximate PageRank](#local_pagerank) | `local_pagerank` | 1 |
| [Nxp pagerank](#nxp_pagerank) | `nxp_pagerank` | 2 |
| [Walks ppr](#walks_ppr) | `walks_ppr` | 1 |

## References {#concept-references}

[bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative), [andersen2006local](../../references.html#andersen2006local), [grover2016node2vec](../../references.html#grover2016node2vec), [tong2006fast](../../references.html#tong2006fast), [vose1991linear](../../references.html#vose1991linear), [walker1977new](../../references.html#walker1977new)

## Pagerank {#pagerank}

Measure id: `pagerank`. Original family: Centrality.

**Definition.** PageRank of every node by power iteration (Brin and Page 1998), with a GAP-suite preset.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and weights): The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. [details](#why-pagerank-networkx) | `pagerank` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `page_rank` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `pagerank; personalized_pagerank` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-pagerank-graphtool) | `pagerank` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `PageRank` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, normalization, self-loops and weights): rx.pagerank() takes a directed graph. [details](#why-pagerank-rustworkx) | `pagerank` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): scikit-network's random-surfer operator weights the restart vector by each node's own out-degree status, b\_i = (1 - d \[i has out-links\]) y\_i... [details](#why-pagerank-sknetwork) | `PageRank; get_pagerank` |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `PageRank` |  |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-pagerank-boost) | `page_rank` | API listing |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](#why-pagerank-graphblas) |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-defect" href="../../method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> | Defect: PageRank loses probability mass at self-loops; scores do not sum to 1 (finding F017). [details](#why-pagerank-gephi) | `PageRank` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-pagerank-ucinet) | `PageRank` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-pagerank-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults and weights) on the fixtures mid\_messy\_dir\_int\_2000, mid\_plc\_dir\_4000. The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-11, rel 1e-09 (0 means exact equality). No value (pagerank\_weighted\_networkx\_damping\_060) on inputs tagged negative\_weights: Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. 6 comparisons differ and 280 agree. Finding F005 (convention): PageRank stops on an L1 change below n \* tol. Finding F007 (convention): Undirected self-loop is one arc. Findings: [F005](../../findings.html#f005), [F007](../../findings.html#f007).
- <a id="why-pagerank-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: pagerank.
- <a id="why-pagerank-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> rustworkx 0.18.1 was run and its value differs from the reference value by convention (defaults, direction, normalization, self-loops and weights) on inputs tagged loops and the fixtures mid\_messy\_dir\_int\_2000, mid\_plc\_dir\_4000. pagerank: rx.pagerank() takes a directed graph; an undirected fixture enters as two arcs per edge and one arc per self-loop, so a loop counts once (NetworkX's convention, pagerank\_networkx), not twice (igraph's, this variant). pagerank\_networkx, pagerank\_personalized\_networkx and pagerank\_uniform\_dangling: The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). pagerank\_personalized: A self-loop enters rx.pagerank() as one arc, so it counts once, not twice as in this variant (see pagerank). pagerank\_weighted: The entry counts an undirected self-loop twice (loops: twice); rustworkx counts it once. Relation to the reference value: Undirected self-loop: the loop is one arc (adjacency diagonal 1), so it adds 1 to the node's out-degree; igraph and the reference value's default put 2 on the diagonal (two edge ends). Graph and MultiGraph agree. Path graph 0-1-2 with a loop at 1: NetworkX 0.5745 at node 1, loop counted twice 0.6316. Mapping: the reference value computed with the tool's convention (an undirected self-loop is one arc) agrees with the tool within abs 5e-11, rel 5e-08 on all 2 comparisons where the difference occurs. Tolerance before mapping: abs 5e-11, rel 5e-08 (0 means exact equality). 7 comparisons differ and 274 agree. Finding F006 (convention): PageRank stops on an L1 change below n \* tol. Finding F008 (convention): Undirected self-loop is one arc. Findings: [F006](../../findings.html#f006), [F008](../../findings.html#f008).
- <a id="why-pagerank-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> scikit-network 0.33.0 was run and its value differs from the reference value by convention (defaults) on the fixtures gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_und, pair, two\_triangles\_isolate, weighted\_dir. scikit-network's random-surfer operator weights the restart vector by each node's own out-degree status, b\_i = (1 - d \[i has out-links\]) y\_i (sknetwork/linalg/ppr\_solver.py), instead of spreading the rank of dangling nodes over y, so on fixtures with dangling nodes (sinks or isolates) its scores are not the stationary distribution of the Google matrix the reference value and NetworkX use. Elsewhere the two agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-11, rel 1e-09 (0 means exact equality). 25 comparisons differ and 86 agree. Finding F087 (defect): PageRank restart vector departs from the definition. Findings: [F087](../../findings.html#f087).
- <a id="why-pagerank-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: page\_rank.
- <a id="why-pagerank-graphblas"></a>**[GraphBLAS algorithms](../../tools/graphblas.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> GraphBLAS algorithms graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) was run and its value differs from the reference value by convention (defaults, direction, multi-edges and weights) on inputs tagged multi\_edges and the fixtures empty, single\_node. graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference value and NetworkX return. Mapping: the reference value computed with NetworkX's Graph/DiGraph reading (parallel edges collapse, one self-loop per node kept) agrees with the tool within abs 1e-11, rel 1e-09 on all 10 comparisons where the difference occurs. Tolerance before mapping: abs 1e-11, rel 1e-09 (0 means exact equality). 20 comparisons differ and 127 agree.
- <a id="why-pagerank-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-defect" href="../../method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> Gephi toolkit 0.11.3 gives a wrong value under the published definition of PageRank: it loses probability mass at self-loops, so the scores no longer sum to 1. Inputs: any network with self-loops; in the comparison corpus multi\_loops\_dir (scores sum to 0.545) and multi\_loops\_und (0.496); without self-loops the tool agrees. Observed: undirected edges 0-0, 0-1, 1-2, damping 0.85: scores 0.1375, 0.2058, 0.1375 (sum 0.4807); directed arcs 0&gt;0, 0&gt;1, 1&gt;0: 0.5, 0.2875 (sum 0.7875). Expected: scores that sum to 1 (they do without the loop). Separately, its undirected reading of a directed network merges a pair of opposite arcs into one edge, where the reference value counts each arc (a convention, reproduced by reading the network as symmetric). Tool version 0.11.3. 7 comparisons differ and 37 agree. Finding F017. Findings: [F017](../../findings.html#f017).
- <a id="why-pagerank-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `pagerank` | igraph (R) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `igraph::page_rank(g, damping = 0.85, weights = NA)$vector` |  |
| `pagerank` | igraph (Python) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `python-igraph: g.pagerank(damping=0.85, weights=None)` |  |
| `pagerank` | NetworKit | any | differs | disconnected, edge\_case, isolates, loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 1e-11, rel 1e-09 | `nk.centrality.PageRank(G, damp = 0.85, tol = 1e-15, distributeSinks = SinkHandling.DISTRIBUTE_SINKS)` |  |
| `pagerank` | rustworkx | any | differs | loops | direction, normalization, self\_loops | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, tol = 1e-14, max_iter = 100000)` | rx.pagerank() takes a directed graph; an undirected fixture enters as two arcs per edge and one arc per self-loop, so a loop counts once (NetworkX's convention, pagerank\_networkx), not twice (igraph's, this variant). |
| `pagerank` | scikit-network | any | differs |  | defaults | abs 1e-11, rel 1e-09 | `sknetwork.ranking.PageRank(damping_factor = 0.85, solver = 'piteration', n_iter = 100000, tol = 1e-15).fit_predict(A)` | Elsewhere the two agree. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `pagerank` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, alpha = 0.85, tol = 1e-14, max_iter = 100000, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank` | Gephi toolkit | any | differs |  | self\_loops | abs 1e-11, rel 1e-09 | `Gephi toolkit 0.11.3: PageRank (setProbability(0.85), setEpsilon(1e-14), setUseEdgeWeight(false)), node column 'pageranks'` | Without loops it matches. |
| `pagerank_networkx` | NetworkX | any | differs |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(MultiGraph/MultiDiGraph, alpha = 0.85, weight = None, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_networkx` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-11, rel 1e-09 | `nk.centrality.PageRank(G, damp = 0.85, tol = 1e-15, distributeSinks = SinkHandling.DISTRIBUTE_SINKS)` |  |
| `pagerank_networkx` | rustworkx | any | differs |  |  | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, tol = 1e-14, max_iter = 100000)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_networkx` | scikit-network | any | differs |  | defaults | abs 1e-11, rel 1e-09 | `sknetwork.ranking.PageRank(damping_factor = 0.85, solver = 'piteration', n_iter = 100000, tol = 1e-15).fit_predict(A)` | Elsewhere the two agree. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `pagerank_networkx` | JGraphT | any | agrees |  |  | abs 1e-11, rel 1e-09 | `JGraphT 1.5.2: new PageRank<>(g, 0.85, 10000, 1e-14) on a pseudograph` |  |
| `pagerank_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, alpha = 0.85, tol = 1e-14, max_iter = 100000, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank_networkx_damping_050` | NetworkX | any | agrees |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(MultiGraph/MultiDiGraph, alpha = 0.5, weight = None, tol = 1e-14)` |  |
| `pagerank_networkx_damping_095` | NetworkX | any | differs |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(MultiGraph/MultiDiGraph, alpha = 0.95, weight = None, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_personalized` | igraph (R) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `igraph::page_rank(g, personalized = (0:(n - 1)) %% 3 + 1, weights = NA)$vector` |  |
| `pagerank_personalized` | igraph (Python) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `python-igraph: g.personalized_pagerank( damping=0.85, weights=None, reset=node_rule("mod3plus1", n))` |  |
| `pagerank_personalized` | rustworkx | any | differs | loops | direction, normalization, self\_loops | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, personalization = {v: v % 3 + 1}, tol = 1e-14)` | A self-loop enters rx.pagerank() as one arc, so it counts once, not twice as in this variant (see pagerank). |
| `pagerank_personalized` | scikit-network | any | differs |  | defaults | abs 1e-11, rel 1e-09 | `sknetwork.ranking.PageRank(...).fit_predict(A, weights = (v % 3 + 1) / sum)` | Elsewhere the two agree. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `pagerank_personalized` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, personalization = {v: v % 3 + 1}, tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank_personalized_networkx` | NetworkX | any | differs |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(G, personalization = {v: v % 3 + 1}, weight = None, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_personalized_networkx` | rustworkx | any | differs |  |  | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, personalization = {v: v % 3 + 1}, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_personalized_networkx` | scikit-network | any | differs |  | defaults | abs 1e-11, rel 1e-09 | `sknetwork.ranking.PageRank(...).fit_predict(A, weights = (v % 3 + 1) / sum)` | Elsewhere the two agree. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `pagerank_personalized_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, personalization = {v: v % 3 + 1}, tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank_personalized_networkx_damping_030` | NetworkX | any | agrees |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(MultiGraph/MultiDiGraph, alpha = 0.3, personalization = mod3plus1, tol = 1e-14)` |  |
| `pagerank_undirected` | igraph (R) | directed | agrees |  |  | abs 1e-11, rel 1e-09 | `igraph::page_rank(g, directed = FALSE, weights = NA)$vector` |  |
| `pagerank_undirected` | igraph (Python) | directed | agrees |  |  | abs 1e-11, rel 1e-09 | `python-igraph: g.pagerank(damping=0.85, directed=False, weights=None)` |  |
| `pagerank_undirected` | Gephi toolkit | directed | differs |  | direction, multi\_edges, self\_loops | abs 1e-11, rel 1e-09 | `Gephi toolkit 0.11.3: PageRank (setProbability(0.85), setEpsilon(1e-14), setDirected(false)), node column 'pageranks'` | Gephi's undirected view of a directed network merges a pair of opposite arcs into one edge (PageRank on the union graph reproduces it to 1e-16); the reference value's undirected reading counts each arc. The symmetric reading reproduces Gephi (convention check) except on multi\_loops\_dir, which also has the loop defect of pagerank. |
| `pagerank_uniform_dangling` | NetworkX | any | differs |  |  | abs 1e-11, rel 1e-09 | `nx.pagerank(G, personalization = {v: v % 3 + 1}, dangling = {v: 1}, weight = None, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_uniform_dangling` | rustworkx | any | differs |  |  | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, personalization = {v: v % 3 + 1}, dangling = {v: 1}, tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). |
| `pagerank_uniform_dangling` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, personalization = {v: v % 3 + 1}, dangling = {v: 1}, tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank_weighted` | NetworkX | any | differs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G, weight = 'weight', tol = 1e-14)` | The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. Against the exact solution of the linear system (numpy.linalg.solve) on mid\_messy\_dir\_int\_2000 NetworkX is off by 3.4e-11 absolute (4.2e-9 relative), the reference by 1.8e-12 (2.1e-10). Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `pagerank_weighted` | igraph (R) | any | no-value-on-some-inputs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `igraph::page_rank(g, damping = 0.85, weights = E(g)$weight)$vector` | Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `pagerank_weighted` | igraph (Python) | any | no-value-on-some-inputs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `python-igraph: g.pagerank(damping=0.85, weights=w)` | Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `pagerank_weighted` | NetworKit | any | differs | loops, (no value) negative\_weights, (no value) zero\_weights | defaults, direction, normalization, self\_loops, weights | abs 1e-11, rel 1e-09 | `nk.centrality.PageRank(G_weighted, damp = 0.85, tol = 1e-15, distributeSinks = SinkHandling.DISTRIBUTE_SINKS)` | The entry counts an undirected self-loop twice; NetworKit counts it once. NetworKit returns no value when an edge weight is zero or negative. |
| `pagerank_weighted` | rustworkx | any | differs | loops, (no value) negative\_weights | defaults, direction, normalization, self\_loops, weights | abs 5e-11, rel 5e-08 | `rx.pagerank(G as arcs, alpha = 0.85, weight_fn = float, tol = 1e-14, max_iter = 100000)` | The entry counts an undirected self-loop twice; rustworkx counts it once. Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `pagerank_weighted` | scikit-network | any | differs |  |  | abs 1e-11, rel 1e-09 | `sknetwork.ranking.PageRank(damping_factor = 0.85, solver = 'piteration', n_iter = 100000, tol = 1e-15).fit_predict(W)` | Elsewhere the two agree. |
| `pagerank_weighted` | JGraphT | any | agrees |  |  | abs 1e-11, rel 1e-09 | `JGraphT 1.5.2: new PageRank<>(g_weighted, 0.85, 10000, 1e-14) on a pseudograph` |  |
| `pagerank_weighted` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(G simple, weight = 'weight', tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On a graph without edges graphblas-algorithms returns 0 for every node; the PageRank of an edgeless graph is uniform (every node dangles), as the reference and NetworkX return. |
| `pagerank_weighted` | Gephi toolkit | any | agrees |  |  | abs 1e-11, rel 1e-09 | `Gephi toolkit 0.11.3: PageRank (setProbability(0.85), setEpsilon(1e-14), setUseEdgeWeight(true)), node column 'pageranks'` |  |
| `pagerank_weighted_networkx_damping_060` | NetworkX | any | no-value-on-some-inputs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `nx.pagerank(MultiGraph/MultiDiGraph, alpha = 0.6, weight = 'weight', tol = 1e-14)` | Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F005](../../findings.html#f005) | NetworkX | convention | PageRank stops on an L1 change below n \* tol |
| [F006](../../findings.html#f006) | rustworkx | convention | PageRank stops on an L1 change below n \* tol |
| [F007](../../findings.html#f007) | NetworkX | convention | Undirected self-loop is one arc |
| [F008](../../findings.html#f008) | rustworkx | convention | Undirected self-loop is one arc |
| [F009](../../findings.html#f009) | JGraphT | convention | Undirected self-loop is one arc |
| [F017](../../findings.html#f017) | Gephi toolkit | defect | PageRank loses probability mass at self-loops |
| [F068](../../findings.html#f068) | NetworKit | convention | Rank at isolated nodes is spread differently |
| [F087](../../findings.html#f087) | scikit-network | defect | PageRank restart vector departs from the definition |
| [F088](../../findings.html#f088) | GAP Benchmark Suite | convention | Rank held by dangling vertices is not passed on |

**References:** [bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Google {#nxp_google}

Measure id: `nxp_google`. Original family: Centrality.

**Definition.** Google.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `google_matrix` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_google` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.google_matrix(G, weight = None)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Local and approximate PageRank {#local_pagerank}

Measure id: `local_pagerank`. Original family: Centrality.

**Definition.** Local and approximate PageRank.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-local_pagerank-networkit) | `ApproximatePageRank; PageRankMatrix; PageRankNibble` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-local_pagerank-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: ApproximatePageRank; PageRankMatrix; PageRankNibble.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Nxp pagerank {#nxp_pagerank}

Measure id: `nxp_pagerank`. Original family: Centrality.

**Definition.** NetworkX's PageRank iteration, reproduced step for step; reports when it does not converge.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxp_pagerank-bct) | `pagerank_centrality` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxp_pagerank-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: pagerank\_centrality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_pagerank` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.pagerank(G, weight = None)` |  |
| `nxp_pagerank_personalized_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) one\_node | defaults, weights | abs 1e-13, rel 1e-10 | `nx.pagerank(G, alpha = 0.7, personalization = {v: v % 3}, weight = 'weight')` | The personalization v % 3 gives node 0 weight 0, so on one node it sums to zero; the reference rejects it. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Walks ppr {#walks_ppr}

Measure id: `walks_ppr`. Original family: Centrality.

**Definition.** Personalized PageRank by the local push of Andersen, Chung and Lang: estimates below the exact value by at most the residual.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `walks_ppr_exact` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 2e-13, rel 1e-10 | `nx.pagerank(G, alpha = 0.85, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = None)` | NetworkX counts an undirected self-loop once, the reference twice. |
| `walks_ppr_push` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 5e-13, rel 5e-10 | `nx.pagerank(G, alpha = 0.85, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = None)` | NetworkX counts an undirected self-loop once, the reference twice. |
| `walks_ppr_push_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) loops | direction, normalization, self\_loops | abs 5e-12, rel 2e-09 | `nx.pagerank(G, alpha = 0.7, personalization = {0: 2, n - 1: 1}, tol = 1e-14, max_iter = 100000, weight = 'weight')` | NetworkX counts an undirected self-loop once, the reference twice. |

**References:** [andersen2006local](../../references.html#andersen2006local), [brin1998anatomy](../../references.html#brin1998anatomy), [grover2016node2vec](../../references.html#grover2016node2vec), [tong2006fast](../../references.html#tong2006fast), [vose1991linear](../../references.html#vose1991linear), [walker1977new](../../references.html#walker1977new)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
