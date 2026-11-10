---
title: "Pagerank"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Pagerank

Family: Centrality. Identifier: `pagerank`.

## Definition

PageRank of every node by power iteration (Brin and Page 1998), with a GAP-suite preset.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention | `pagerank` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `page_rank` |  |
| [igraph (Python)](../tools/pyigraph.html) | ✓ checked, agrees | `pagerank; personalized_pagerank` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `pagerank` | API listing |
| [NetworKit](../tools/networkit.html) | ∅ checked, no value on some inputs | `PageRank` |  |
| [rustworkx](../tools/rustworkx.html) | ≠ checked, differs by convention | `pagerank` |  |
| [scikit-network](../tools/sknetwork.html) | ≠ checked, differs by convention | `PageRank; get_pagerank` |  |
| [JGraphT](../tools/jgrapht.html) | ✓ checked, agrees | `PageRank` |  |
| [Boost Graph Library](../tools/boost.html) | · reported in docs | `page_rank` | API listing |
| [GraphBLAS algorithms](../tools/graphblas.html) | ≠ checked, differs by convention |  |  |
| [Gephi toolkit](../tools/gephi.html) | ✗ checked, defect | `PageRank` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `PageRank` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

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

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F005](../findings.html#f005) | NetworkX | convention | PageRank stops on an L1 change below n \* tol |
| [F006](../findings.html#f006) | rustworkx | convention | PageRank stops on an L1 change below n \* tol |
| [F007](../findings.html#f007) | NetworkX | convention | Undirected self-loop is one arc |
| [F008](../findings.html#f008) | rustworkx | convention | Undirected self-loop is one arc |
| [F009](../findings.html#f009) | JGraphT | convention | Undirected self-loop is one arc |
| [F017](../findings.html#f017) | Gephi toolkit | defect | PageRank loses probability mass at self-loops |
| [F068](../findings.html#f068) | NetworKit | convention | Rank at isolated nodes is spread differently |
| [F087](../findings.html#f087) | scikit-network | defect | PageRank restart vector departs from the definition |
| [F088](../findings.html#f088) | GAP Benchmark Suite | convention | Rank held by dangling vertices is not passed on |

## References

[bonacich1972factoring](../references.html#bonacich1972factoring), [bonacich1987power](../references.html#bonacich1987power), [bonacich2001eigenvector](../references.html#bonacich2001eigenvector), [brin1998anatomy](../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../references.html#hagberg2008exploring), [katz1953new](../references.html#katz1953new), [kleinberg1999authoritative](../references.html#kleinberg1999authoritative)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [siek2002boost](../references.html#siek2002boost), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx), [tool_sknetwork](../references.html#tool_sknetwork)
{% endraw %}
