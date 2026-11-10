---
title: "HITS hubs and authorities"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# HITS hubs and authorities {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `hits`. 2 measures.

## Definition {#concept-definition}

Hub and authority scores of every node (Kleinberg 1999), with the leading singular value.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Hits](#hits) | `hits` | 9 |
| [Nxp hits](#nxp_hits) | `nxp_hits` | 1 |

## References {#concept-references}

[bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative)

## Hits {#hits}

Measure id: `hits`. Original family: Centrality.

**Definition.** Hub and authority scores of every node (Kleinberg 1999), with the leading singular value.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `hits` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `authority_score; hits_scores; hub_score` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ≠ checked, differs by convention | `authority_score; hub_score` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `hits` | API listing |
| [rustworkx](../../tools/rustworkx.html) | ∅ checked, no value on some inputs | `hits` |  |
| [scikit-network](../../tools/sknetwork.html) | ≠ checked, differs by convention | `HITS` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | ≠ checked, differs by convention |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ≠ checked, differs by convention | `Hits` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Hubs and authorities, SVD (two-mode fixes 6.748)` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `hits_authorities` | igraph (R) | any | differs | bipartite, disconnected, edge\_case, symmetric\_nodes | defaults, ties | abs 2e-12, rel 5e-11 | `igraph::authority_score(g, weights = NA)$vector` |  |
| `hits_authorities` | igraph (Python) | any | differs | bipartite, disconnected, edge\_case, symmetric\_nodes | defaults, ties | abs 2e-12, rel 5e-11 | `python-igraph: gu.authority_score(scale=True)` |  |
| `hits_authorities` | Gephi toolkit | any | differs | directed, undirected | defaults, direction, normalization, self\_loops | abs 2e-12, rel 5e-11 | `Gephi toolkit 0.11.3: Hits (setEpsilon(1e-14)), node column 'authority'` | Gephi scales the hub and authority vectors to unit Euclidean length; the reference scales to maximum 1 (scale: unit reproduces it), and Gephi ignores self-loops. With no edges Gephi returns 0 where the reference value's value is undefined. A convention check holds on every fixture with edges. |
| `hits_authorities_networkx` | NetworkX | any | no-value-on-some-inputs |  | normalization, ties | abs 1e-12, rel 2e-11 | `nx.hits(G, normalized = True)[1] on the summed adjacency matrix` | Without edges NetworkX's iteration divides 0 by 0 and fails to converge. |
| `hits_authorities_networkx` | rustworkx | any | differs | bipartite, disconnected, symmetric\_nodes, (no value) edgeless | defaults, direction, ties | abs 5e-14, rel 2e-11 | `rx.hits(G as arcs, max_iter = 1000000, tol = 1e-13)[1]` | When the leading singular value of A is repeated (bipartite or disconnected networks, symmetric ones such as the directed cycle) hub and authority vectors are not unique. rustworkx iterates A^T A from uniform authorities; the reference, like NetworkX, takes the limit from h = 1, so the two land on different vectors of the same eigenspace. Without edges rx.hits() raises FailedToConverge. |
| `hits_authorities_networkx` | scikit-network | any | differs |  | defaults | abs 5e-14, rel 2e-11 | `sknetwork.ranking.HITS().fit(A).scores_col_, scaled to sum 1` | The definition oracle declares these fixtures undefined. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `hits_authorities_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 5e-14, rel 2e-11 | `nx.hits(G simple, tol = 1e-13, backend = 'graphblas')[1]` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. Without edges it returns 0 for every node, where hubs and authorities are undefined (0/0). |
| `hits_hubs` | igraph (R) | any | differs | bipartite, disconnected, edge\_case, symmetric\_nodes | defaults, ties | abs 2e-12, rel 5e-11 | `igraph::hub_score(g, weights = NA)$vector` |  |
| `hits_hubs` | igraph (Python) | any | differs | bipartite, disconnected, edge\_case, symmetric\_nodes | defaults, ties | abs 2e-12, rel 5e-11 | `python-igraph: gu.hub_score(scale=True)` |  |
| `hits_hubs` | Gephi toolkit | any | differs | directed, undirected | defaults, direction, normalization, self\_loops | abs 2e-12, rel 5e-11 | `Gephi toolkit 0.11.3: Hits (setEpsilon(1e-14)), node column 'hub'` | Gephi scales the hub and authority vectors to unit Euclidean length; the reference scales to maximum 1 (scale: unit reproduces it), and Gephi ignores self-loops. With no edges Gephi returns 0 where the reference value's value is undefined. A convention check holds on every fixture with edges. |
| `hits_hubs_networkx` | NetworkX | any | no-value-on-some-inputs |  | normalization, ties | abs 1e-12, rel 2e-11 | `nx.hits(G, normalized = True)[0] on the summed adjacency matrix` | Without edges NetworkX's iteration divides 0 by 0 and fails to converge. |
| `hits_hubs_networkx` | rustworkx | any | differs | bipartite, disconnected, symmetric\_nodes, (no value) edgeless | defaults, direction, ties | abs 5e-14, rel 2e-11 | `rx.hits(G as arcs, max_iter = 1000000, tol = 1e-13)[0]` | When the leading singular value of A is repeated (bipartite or disconnected networks, symmetric ones such as the directed cycle) hub and authority vectors are not unique. rustworkx iterates A^T A from uniform authorities; the reference, like NetworkX, takes the limit from h = 1, so the two land on different vectors of the same eigenspace. Without edges rx.hits() raises FailedToConverge. |
| `hits_hubs_networkx` | scikit-network | any | differs |  | defaults | abs 5e-14, rel 2e-11 | `sknetwork.ranking.HITS().fit(A).scores_row_, scaled to sum 1` | The definition oracle declares these fixtures undefined. scikit-network rejects an adjacency matrix without entries ('The input matrix is empty'). |
| `hits_hubs_networkx` | GraphBLAS algorithms | any | differs | multi\_edges | defaults, direction, multi\_edges, weights | abs 5e-14, rel 2e-11 | `nx.hits(G simple, tol = 1e-13, backend = 'graphblas')[0]` | graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. Without edges it returns 0 for every node, where hubs and authorities are undefined (0/0). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F019](../../findings.html#f019) | Gephi toolkit | convention | HITS uses unit Euclidean scaling and ignores self-loops |
| [F040](../../findings.html#f040) | igraph (R) | convention | HITS returns 1 for an edgeless network |

**References:** [bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Nxp hits {#nxp_hits}

Measure id: `nxp_hits`. Original family: Centrality.

**Definition.** NetworkX's hubs and authorities iteration, reproduced step for step; reports when it does not converge.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_hits` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G) (power iteration; graph read without weights)` |  |
| `nxp_hits_raw_weighted` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G, normalized = False)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
