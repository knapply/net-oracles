---
title: "Eigenvector"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Eigenvector

Family: Centrality. Identifier: `eigenvector`.

## Definition

Eigenvector centrality of every node, with the principal eigenvalue and a connectedness flag.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs | `eigenvector_centrality; eigenvector_centrality_numpy` |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs | `eigen_centrality; evcent` |  |
| [igraph (Python)](../tools/pyigraph.html) | ≠ checked, differs by convention | `eigenvector_centrality` |  |
| [sna](../tools/sna.html) | ≠ checked, differs by convention | `evcent` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `eigenvector` | API listing |
| [NetworKit](../tools/networkit.html) | · reported in docs | `EigenvectorCentrality` | API listing |
| [rustworkx](../tools/rustworkx.html) | ✓ checked, agrees | `digraph_eigenvector_centrality; eigenvector_centrality; graph_eigenvector_centrality` |  |
| [JGraphT](../tools/jgrapht.html) | · reported in docs | `EigenvectorCentrality` | API listing |
| [GraphBLAS algorithms](../tools/graphblas.html) | ≠ checked, differs by convention |  |  |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `eigenvector_centrality_und` | API listing |
| [Gephi toolkit](../tools/gephi.html) | ≠ checked, differs by convention | `EigenvectorCentrality` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Eigenvector; symmetrized by max for directed; lambda-squared scores for several components (6.831 handles disconnected networks)` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `eigenvector` | igraph (R) | any | differs | disconnected, not\_strongly\_connected | defaults, direction | abs 2e-11, rel 2e-10 | `igraph::eigen_centrality(g, directed = TRUE, weights = NA)$vector` | When several components (strong components of a digraph) share the largest eigenvalue the principal eigenvector is not unique, and the split between them depends on the starting vector (all ones here, degree-based in igraph's ARPACK call), or the reference declines. Graphs where the leading eigenvalue is simple must match. |
| `eigenvector` | igraph (Python) | any | differs | disconnected, not\_strongly\_connected | defaults, direction | abs 2e-11, rel 2e-10 | `python-igraph: g.eigenvector_centrality(directed=True, weights=None)` | When several components (strong components of a digraph) share the largest eigenvalue the principal eigenvector is not unique, and the split between them depends on the starting vector (all ones here, degree-based in igraph's ARPACK call), or the reference declines. Graphs where the leading eigenvalue is simple must match. |
| `eigenvector` | Gephi toolkit | any | differs | edgeless | defaults, direction, multi\_edges, normalization, self\_loops | abs 0.02, rel 0 | `Gephi toolkit 0.11.3: EigenvectorCentrality (setNumRuns(1000000)), node column 'eigencentrality'` | On a network without edges Gephi returns 0 where the reference returns the all-ones vector (any vector is an eigenvector of the zero matrix). Gephi counts an undirected self-loop once in the adjacency matrix; the reference value's default counts it twice (loops: once reproduces Gephi to 1.3e-3 on multi\_loops\_und). |
| `eigenvector_documented` | UCINET | any | documented |  | direction | abs 0, rel 0 | `Documented behaviour (not run)` | Eigenvector centrality symmetrizes directed ties by taking the maximum before the eigen-decomposition. |
| `eigenvector_networkx` | NetworkX | any | no-value-on-some-inputs |  | defaults, ties | abs 5e-10, rel 5e-09 | `nx.eigenvector_centrality_numpy(G); it refuses graphs that are not (strongly) connected, which are then not run` | NetworkX raises an error: its power iteration does not converge on these networks (disconnected, or without a unique leading eigenvector). |
| `eigenvector_networkx` | rustworkx | any | no-value-on-some-inputs |  |  | abs 5e-10, rel 5e-09 | `rx.eigenvector_centrality(G, max_iter = 100000, tol = 1e-14)` |  |
| `eigenvector_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | direction, multi\_edges, ties, weights | abs 5e-10, rel 5e-09 | `nx.eigenvector_centrality(G simple, tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. On the single arc A is nilpotent and the power iteration converges only like 1/k; PowerIterationFailedConvergence at tol 1e-14. |
| `eigenvector_sna` | sna | any | differs | disconnected, edge\_case | defaults, direction, ties | abs 1e-10, rel 1e-09 | `sna::evcent(m, gmode = 'digraph', diag = FALSE) for directed networks; sna::evcent(m, gmode = 'graph', diag = FALSE, use.eigen = TRUE) for undirected ones, with the sign chosen so the scores sum to a positive number (sna leaves the sign of the eigenvector arbitrary)` | sna's default iteration is plain power iteration on A, which does not converge on periodic graphs (it alternates on bipartite ones, hence use.eigen = TRUE for undirected networks), and returns NaN for a graph without cycles. When several components share the largest eigenvalue the eigenvector is not unique. sna returns missing values when the leading eigenvector is undefined. |
| `eigenvector_undirected` | igraph (R) | directed | differs | disconnected | defaults | abs 1e-13, rel 5e-12 | `igraph::eigen_centrality(g, directed = FALSE, weights = NA)$vector (the R default)` | Not unique when components share the largest eigenvalue (see eigenvector). |
| `eigenvector_undirected` | Gephi toolkit | directed | differs | edgeless | defaults, direction, multi\_edges, self\_loops, ties | abs 0.02, rel 0 | `Gephi toolkit 0.11.3: EigenvectorCentrality (setNumRuns(1000000), setDirected(false)), node column 'eigencentrality'` | Gephi's undirected view of a directed network merges a pair of opposite arcs into one edge; the reference value's undirected reading counts each arc (the symmetric reading reproduces Gephi, a convention check, except on multi\_loops\_dir, where Gephi also counts the loops once). The iteration is not converged (see eigenvector), so values are compared to 0.02; on a network without edges Gephi returns 0, the reference the all-ones vector. |
| `eigenvector_weighted` | igraph (R) | any | differs | disconnected, not\_strongly\_connected | defaults, direction | abs 5e-13, rel 5e-12 | `igraph::eigen_centrality(g, directed = TRUE, weights = E(g)$weight)$vector` | When several components (strong components of a digraph) share the largest eigenvalue the principal eigenvector is not unique, and the split between them depends on the starting vector (all ones here, degree-based in igraph's ARPACK call), or the reference declines. Graphs where the leading eigenvalue is simple must match. |
| `eigenvector_weighted` | igraph (Python) | any | differs | disconnected, not\_strongly\_connected | defaults, direction | abs 5e-13, rel 5e-12 | `python-igraph: g.eigenvector_centrality(directed=True, weights=w)` | When several components (strong components of a digraph) share the largest eigenvalue the principal eigenvector is not unique, and the split between them depends on the starting vector (all ones here, degree-based in igraph's ARPACK call), or the reference declines. Graphs where the leading eigenvalue is simple must match. |
| `eigenvector_weighted` | Gephi toolkit | any | differs | weighted | weights | abs 0.02, rel 0 | `Gephi toolkit 0.11.3: EigenvectorCentrality (setNumRuns(1000000)) on the weighted network, node column 'eigencentrality'` | EigenvectorCentrality has no weighted mode: its values on the weighted network equal its values on the unweighted network, so it ignores edge weights. |
| `eigenvector_weighted_networkx` | NetworkX | any | no-value-on-some-inputs |  | ties | abs 1e-10, rel 1e-09 | `nx.eigenvector_centrality_numpy(G, weight = 'weight')` | NetworkX's power iteration does not converge on this network. |
| `eigenvector_weighted_networkx` | rustworkx | any | agrees |  |  | abs 1e-10, rel 1e-09 | `rx.eigenvector_centrality(G, weight_fn = float, max_iter = 100000, tol = 1e-14)` |  |
| `eigenvector_weighted_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | direction, multi\_edges, weights | abs 1e-10, rel 1e-09 | `nx.eigenvector_centrality(G simple, weight = 'weight', tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F014](../findings.html#f014) | Gephi toolkit | defect | Eigenvector centrality is not converged |
| [F064](../findings.html#f064) | NetworKit | defect | Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs |

## References

[bonacich1972factoring](../references.html#bonacich1972factoring), [bonacich1987power](../references.html#bonacich1987power), [collatz1942einschliessungssatz](../references.html#collatz1942einschliessungssatz), [daniel1976reorthogonalization](../references.html#daniel1976reorthogonalization), [lanczos1950iteration](../references.html#lanczos1950iteration), [mises1929praktische](../references.html#mises1929praktische), [stewart2002krylov](../references.html#stewart2002krylov), [wu2000thick](../references.html#wu2000thick)

Tools cited: [bastian2009gephi](../references.html#bastian2009gephi), [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [csardi2006igraph](../references.html#csardi2006igraph), [davis2019algorithm](../references.html#davis2019algorithm), [hagberg2008exploring](../references.html#hagberg2008exploring), [michail2020jgrapht](../references.html#michail2020jgrapht), [peixoto2014graphtool](../references.html#peixoto2014graphtool), [rubinov2010complex](../references.html#rubinov2010complex), [staudt2016networkit](../references.html#staudt2016networkit), [tool_rustworkx](../references.html#tool_rustworkx)
{% endraw %}
