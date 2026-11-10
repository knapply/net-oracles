---
title: "Katz centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Katz centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Spectral and walk-based. Concept id: `katz_centrality`. 2 measures.

## Definition {#concept-definition}

Katz centrality of every node by fixed-point iteration (Katz 1953).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Katz](#katz) | `katz` | 10 |
| [Nxp katz](#nxp_katz) | `nxp_katz` | 1 |

## References {#concept-references}

[bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative)

## Katz {#katz}

Measure id: `katz`. Original family: Centrality.

**Definition.** Katz centrality of every node by fixed-point iteration (Katz 1953).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `katz_centrality; katz_centrality_numpy` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `alpha_centrality` |  |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-katz-graphtool) | `katz` | API listing |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-katz-networkit) | `KatzCentrality; KatzIndex` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `digraph_katz_centrality; graph_katz_centrality; katz_centrality` |  |
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-katz-sknetwork) | `Katz` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-katz-jgrapht) | `KatzCentrality` | API listing |
| [GraphBLAS algorithms](../../tools/graphblas.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction and multi-edges): graphblas-algorithms' katz\_centrality drops the beta term for nodes that have no in-links (they get no entry in the sparse result, read as 0), so... [details](#why-katz-graphblas) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-katz-ucinet) | `Katz family (replaced Katz-Hubbell, 6.771)` | published documentation |
| [centiserve](../../tools/centiserve.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `katzcent` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-katz-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: katz.
- <a id="why-katz-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: KatzCentrality; KatzIndex.
- <a id="why-katz-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: Katz.
- <a id="why-katz-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: KatzCentrality.
- <a id="why-katz-graphblas"></a>**[GraphBLAS algorithms](../../tools/graphblas.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> GraphBLAS algorithms graphblas-algorithms 2023.10.0 (python-graphblas 2025.2.0, SuiteSparse:GraphBLAS 9.4.5.0) was run and its value differs from the reference value by convention (direction and multi-edges) on inputs tagged multi\_edges and the fixtures empty, gnp\_dir\_sparse, gnp\_und\_sparse, multi\_loops\_dir, multi\_loops\_und, pair, single\_node, two\_triangles\_isolate. katz: graphblas-algorithms' katz\_centrality drops the beta term for nodes that have no in-links (they get no entry in the sparse result, read as 0), so those nodes, and nodes reached only from them, score 0 instead of beta; Katz's definition gives every node at least beta. On every fixture where all nodes have in-links it agrees with the definition oracle. Parallel edges also collapse (Graph/DiGraph only). katz\_weighted: graphblas-algorithms' katz\_centrality drops the beta term for nodes without in-links (see katz). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-11, rel 1e-09 (0 means exact equality). 8 comparisons differ and 27 agree. Finding F086 (defect): Katz loses beta at nodes without in-links. Findings: [F086](../../findings.html#f086).
- <a id="why-katz-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `katz` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-11, rel 1e-09 | `nx.katz_centrality_numpy(G, alpha, beta = 1) on the summed adjacency matrix` | katz\_centrality\_numpy fails on a network with one node. |
| `katz` | rustworkx | any | agrees |  |  | abs 1e-11, rel 1e-09 | `rx.katz_centrality(G, alpha = 0.5 / lambda_max, beta = 1, max_iter = 100000, tol = 1e-14)` |  |
| `katz` | GraphBLAS algorithms | any | differs | multi\_edges | direction, multi\_edges | abs 1e-11, rel 1e-09 | `nx.katz_centrality(G simple, alpha = 0.5 / lambda_max, beta = 1, tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms' katz\_centrality drops the beta term for nodes that have no in-links (they get no entry in the sparse result, read as 0), so those nodes, and nodes reached only from them, score 0 instead of beta; Katz's definition gives every node at least beta. On every fixture where all nodes have in-links it agrees with the definition oracle. Parallel edges also collapse (Graph/DiGraph only). |
| `katz_alpha_010` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-11, rel 1e-09 | `nx.katz_centrality_numpy(G, alpha = 0.1 / lambda_max, beta = 1) on the summed adjacency matrix` | katz\_centrality\_numpy fails on a network with one node. |
| `katz_alpha_080_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `nx.katz_centrality_numpy(G, alpha = 0.8 / lambda_max, weight = 'weight')` | Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `katz_exogenous` | igraph (R) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `igraph::alpha_centrality(simplify(g, remove.multiple = FALSE), alpha, exo = (0:(n - 1)) %% 3 + 1, weights = NA)` |  |
| `katz_igraph` | igraph (R) | any | agrees |  |  | abs 1e-11, rel 1e-09 | `igraph::alpha_centrality(simplify(g, remove.multiple = FALSE), alpha, exo = 1, weights = NA)` |  |
| `katz_igraph` | centiserve | any | no-value-on-some-inputs |  |  | abs 1e-11, rel 1e-09 | `centiserve::katzcent(g without loops, alpha = 0.5 / lambda_max)` | centiserve::katz needs a decay below the reciprocal of the largest eigenvalue; it rejects the call's alpha on these inputs (valid range 0.0 to 0.2) or fails on a complex comparison. |
| `katz_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) negative\_weights | defaults, weights | abs 1e-11, rel 1e-09 | `nx.katz_centrality_numpy(G, alpha, weight = 'weight')` | Negative weights are outside the measure's domain (lengths, transition probabilities, attenuated walks): the reference declines (no value) where the oracle computes numbers from them. |
| `katz_weighted` | rustworkx | any | agrees |  |  | abs 1e-11, rel 1e-09 | `rx.katz_centrality(G, alpha = 0.5 / lambda_max, beta = 1, weight_fn = float, max_iter = 100000, tol = 1e-14)` |  |
| `katz_weighted` | GraphBLAS algorithms | any | differs |  |  | abs 1e-11, rel 1e-09 | `nx.katz_centrality(G simple, alpha = 0.5 / lambda_max, weight = 'weight', tol = 1e-14, backend = 'graphblas')` | graphblas-algorithms' katz\_centrality drops the beta term for nodes without in-links (see katz). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F063](../../findings.html#f063) | NetworKit | defect | Katz and degree assortativity differ by 2% to 40% |
| [F075](../../findings.html#f075) | igraph (Python) | limitation | Alpha and power centrality exist only in the R binding |
| [F086](../../findings.html#f086) | GraphBLAS algorithms | defect | Katz loses beta at nodes without in-links |

**References:** [bonacich1972factoring](../../references.html#bonacich1972factoring), [bonacich1987power](../../references.html#bonacich1987power), [bonacich2001eigenvector](../../references.html#bonacich2001eigenvector), [brin1998anatomy](../../references.html#brin1998anatomy), [collatz1942einschliessungssatz](../../references.html#collatz1942einschliessungssatz), [hagberg2008exploring](../../references.html#hagberg2008exploring), [katz1953new](../../references.html#katz1953new), [kleinberg1999authoritative](../../references.html#kleinberg1999authoritative)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [davis2019algorithm](../../references.html#davis2019algorithm), [hagberg2008exploring](../../references.html#hagberg2008exploring), [jalili2015centiserver](../../references.html#jalili2015centiserver), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx), [tool_sknetwork](../../references.html#tool_sknetwork)

## Nxp katz {#nxp_katz}

Measure id: `nxp_katz`. Original family: Centrality.

**Definition.** NetworkX's Katz centrality iteration, reproduced step for step; reports when it does not converge.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxp_katz` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.katz_centrality(G, alpha = 0.05)` | NetworkX does not implement katz\_centrality for multigraphs. |
| `nxp_katz_weighted_raw` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-12, rel 1e-10 | `nx.katz_centrality(G, alpha = 0.02, normalized = False, weight = 'weight')` | NetworkX does not implement katz\_centrality for multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
