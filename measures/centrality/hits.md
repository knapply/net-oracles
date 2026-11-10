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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `hits` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and ties): Without ties the scores are undefined (reference NaN, igraph fills in values). [details](#why-hits-igraph) | `authority_score; hits_scores; hub_score` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and ties): Without ties the scores are undefined (reference NaN, igraph fills in values). [details](#why-hits-pyigraph) | `authority_score; hub_score` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-hits-graphtool) | `hits` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and ties): When the leading singular value of A is repeated (bipartite or disconnected networks, symmetric ones such as the directed cycle) hub and authority... [details](#why-hits-rustworkx) | `hits` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults): Repeated leading singular value on these fixtures: scikit-network takes the leading singular vectors from a sparse SVD solver and clips their... [details](#why-hits-sknetwork) | `HITS` |  |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges and weights): graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins). [details](#why-hits-graphblas) |  |  |
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, normalization and self-loops): Gephi scales the hub and authority vectors to unit Euclidean length. [details](#why-hits-gephi) | `Hits` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-hits-ucinet) | `Hubs and authorities, SVD (two-mode fixes 6.748)` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-hits-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (R) 2.3.4 was run and its value differs from the reference value by convention (defaults and ties) on inputs tagged bipartite, disconnected, edge\_case and symmetric\_nodes. Without ties the scores are undefined (reference NaN, igraph fills in values). When several blocks of the hub-authority graph share the largest singular value (bipartite or disconnected networks, and symmetric ones such as the directed cycle, where A^T A = I), the leading eigenvector is not unique and depends on the start; the reference returns the limit of Kleinberg's iteration from h = 1, as NetworkX's hits() does. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 2e-12, rel 5e-11 (0 means exact equality). 22 comparisons differ and 66 agree. Finding F040 (convention): HITS returns 1 for an edgeless network. Findings: [F040](../../findings.html#f040).
- <a id="why-hits-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> igraph (Python) 1.0.0 was run and its value differs from the reference value by convention (defaults and ties) on inputs tagged bipartite, disconnected, edge\_case and symmetric\_nodes. Without ties the scores are undefined (reference NaN, igraph fills in values). When several blocks of the hub-authority graph share the largest singular value (bipartite or disconnected networks, and symmetric ones such as the directed cycle, where A^T A = I), the leading eigenvector is not unique and depends on the start; the reference returns the limit of Kleinberg's iteration from h = 1, as NetworkX's hits() does. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 2e-12, rel 5e-11 (0 means exact equality). 20 comparisons differ and 86 agree.
- <a id="why-hits-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: hits.
- <a id="why-hits-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> rustworkx 0.18.1 was run and its value differs from the reference value by convention (defaults, direction and ties) on inputs tagged bipartite, disconnected and symmetric\_nodes. When the leading singular value of A is repeated (bipartite or disconnected networks, symmetric ones such as the directed cycle) hub and authority vectors are not unique. rustworkx iterates A^T A from uniform authorities; the reference, like NetworkX, takes the limit from h = 1, so the two land on different vectors of the same eigenspace. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 5e-14, rel 2e-11 (0 means exact equality). 12 comparisons differ and 84 agree.
- <a id="why-hits-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> scikit-network 0.33.0 was run and its value differs from the reference value by convention (defaults) on the fixtures cycle7\_dir, davis\_twomode, path10, southern\_women, star8, two\_triangles\_isolate, twomode\_random, twomode\_weighted. Repeated leading singular value on these fixtures: scikit-network takes the leading singular vectors from a sparse SVD solver and clips their negative entries (ranking/hits.py), which picks another vector of the eigenspace. The definition oracle declares these fixtures undefined. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 5e-14, rel 2e-11 (0 means exact equality). 16 comparisons differ and 36 agree.
- <a id="why-hits-graphblas"></a>**[GraphBLAS algorithms](../../tools/graphblas.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> GraphBLAS algorithms graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) was run and its value differs from the reference value by convention (defaults, direction, multi-edges and weights) on inputs tagged multi\_edges and the fixtures empty, single\_node. graphblas-algorithms accepts only Graph and DiGraph, so parallel edges collapse into one (the last weight wins); the reference counts each edge. Without edges it returns 0 for every node, where hubs and authorities are undefined (0/0). Mapping: the reference value computed with NetworkX's Graph/DiGraph reading (parallel edges collapse, one self-loop per node kept) agrees with the tool within abs 5e-14, rel 2e-11 on all 4 comparisons where the difference occurs. Tolerance before mapping: abs 5e-14, rel 2e-11 (0 means exact equality). 8 comparisons differ and 48 agree.
- <a id="why-hits-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Gephi toolkit 0.11.3 was run and its value differs from the reference value by convention (defaults, direction, normalization and self-loops) on inputs tagged directed and undirected. Gephi scales the hub and authority vectors to unit Euclidean length; the reference scales to maximum 1 (scale: unit reproduces it), and Gephi ignores self-loops (loops: ignore). With no edges Gephi returns 0 where the reference value's value is undefined. A convention check holds on every fixture with edges. Relation to the reference value: Scale, loops: unit Euclidean length, self-loops ignored; 0 on an edgeless network. Mapping: the reference value computed with the tool's convention (unit Euclidean length) and (Gephi's HITS ignores self-loops) agrees with the tool within abs 2e-12, rel 5e-11 on all 52 comparisons where the difference occurs. Tolerance before mapping: abs 2e-12, rel 5e-11 (0 means exact equality). 54 comparisons differ and 2 agree. Finding F019 (convention): HITS uses unit Euclidean scaling and ignores self-loops. Findings: [F019](../../findings.html#f019).
- <a id="why-hits-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_hits` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G) (power iteration; graph read without weights)` |  |
| `nxp_hits_raw_weighted` | NetworkX | any | agrees |  |  | abs 1e-13, rel 1e-10 | `nx.hits(G, normalized = False)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
