---
title: "sna"
layout: default
parent: Tools
---

{% raw %}
# sna

| Field | Value |
|---|---|
| Identifier | `sna` |
| Language | R |
| Version tested | 2.8 |
| License | GPL-2.0-or-later |
| Homepage | <https://cran.r-project.org/package=sna> |
| Role | checked |
| Citation | [butts2008sna](../references.html#butts2008sna) |

## How it was run

Called from R on adjacency matrices (the package works on matrices and edge arrays).

Capabilities listed by introspection of R package sna: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 12 |
| checked, differs by convention (≠) | 10 |
| reported in docs (·) | 48 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `betweenness` |
| Centrality | [Betweenness simple](../measures/betweenness_simple.html) | ✓ checked, agrees |  |
| Centrality | [Bonacich](../measures/bonacich.html) | ✓ checked, agrees | `bonpow` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `closeness` |
| Centrality | [Degree simple](../measures/degree_simple.html) | ✓ checked, agrees |  |
| Centrality | [Eigenvector](../measures/eigenvector.html) | ≠ checked, differs by convention | `evcent` |
| Centrality | [Flow betweenness](../measures/flow_betweenness.html) | ≠ checked, differs by convention | `flowbet` |
| Centrality | [Graphcent](../measures/cat_graphcent.html) | · reported in docs | `graphcent` |
| Centrality | [Harmonic](../measures/harmonic.html) | ≠ checked, differs by convention |  |
| Centrality | [Information centrality](../measures/information_centrality.html) | ≠ checked, differs by convention | `infocent` |
| Centrality | [Loadcent](../measures/cat_loadcent.html) | · reported in docs | `loadcent` |
| Centrality | [Reach](../measures/reach.html) | · reported in docs | `reachability` |
| Cohesion and subgroups | [Clique census](../measures/cat_census_clique.html) | · reported in docs | `clique.census` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | · reported in docs | `kcores` |
| Cohesion and subgroups | [Simmelian ties](../measures/simmelian.html) | · reported in docs | `simmelian` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `bicomponent.dist` |
| Components and connectivity | [Cut points](../measures/cut_points.html) | ✓ checked, agrees | `cutpoints` |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `maxflow` |
| Data transforms | [Full symmetrize method set and dichotomize by density](../measures/symmetrize_methods.html) | · reported in docs | `symmetrize` |
| Descriptive statistics | [Centralization / betweenness](../measures/centralization-betweenness.html) | ≠ checked, differs by convention | `centralization` |
| Descriptive statistics | [Centralization / closeness](../measures/centralization-closeness.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Centralization / degree](../measures/centralization-degree.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `component.dist; component.largest; component.size.byvertex; components; is.connected` |
| Descriptive statistics | [Degree](../measures/degree.html) | ≠ checked, differs by convention | `degree` |
| Descriptive statistics | [Density](../measures/density.html) | ≠ checked, differs by convention | `gden` |
| Descriptive statistics | [Dyad census (mutual, asymmetric, null)](../measures/dyad_census.html) | · reported in docs | `dyad.census` |
| Descriptive statistics | [Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)](../measures/krackhardt_dimensions.html) | · reported in docs | `connectedness; lubness` |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ≠ checked, differs by convention | `grecip; mutuality` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | · reported in docs | `gt; gtrans` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | ≠ checked, differs by convention | `triad.census; triad.classify` |
| Descriptive statistics | [Weak and strong transitivity; directed and weighted clustering conventions](../measures/sna_transitivity.html) | · reported in docs |  |
| Generators and rewiring | [G(n, m) random graph](../measures/gen_gnm.html) | · reported in docs | `rgnm` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `rgraph` |
| Generators and rewiring | [Interval graph](../measures/cat_interval.html) | · reported in docs | `interval.graph` |
| Generators and rewiring | [Rgnmix](../measures/cat_rgnmix.html) | · reported in docs | `rgnmix` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `rewire.ws; rgws` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `rewire.ud` |
| Graph theory and combinatorics | [Bbnam](../measures/cat_bbnam.html) | · reported in docs | `bbnam` |
| Graph theory and combinatorics | [Bbnam bf](../measures/cat_bbnam_bf.html) | · reported in docs | `bbnam.bf` |
| Graph theory and combinatorics | [Bn](../measures/cat_bn.html) | · reported in docs | `bn` |
| Graph theory and combinatorics | [Centralgraph](../measures/cat_centralgraph.html) | · reported in docs | `centralgraph` |
| Graph theory and combinatorics | [Equiv clust](../measures/cat_clust_equiv.html) | · reported in docs | `equiv.clust` |
| Graph theory and combinatorics | [Gilschmidt](../measures/cat_gilschmidt.html) | · reported in docs | `gilschmidt` |
| Graph theory and combinatorics | [Hdist](../measures/cat_hdist.html) | · reported in docs | `hdist` |
| Graph theory and combinatorics | [Kcycle census](../measures/cat_census_kcycle.html) | · reported in docs | `kcycle.census` |
| Graph theory and combinatorics | [Netcancor](../measures/cat_netcancor.html) | · reported in docs | `netcancor` |
| Graph theory and combinatorics | [Prestige](../measures/cat_prestige.html) | · reported in docs | `prestige` |
| Graph theory and combinatorics | [Pstar](../measures/cat_pstar.html) | · reported in docs | `pstar` |
| Graph theory and combinatorics | [Rgbn](../measures/cat_rgbn.html) | · reported in docs | `rgbn` |
| Graph theory and combinatorics | [Rguman](../measures/cat_rguman.html) | · reported in docs | `rguman` |
| Graph theory and combinatorics | [Sdmat](../measures/cat_sdmat.html) | · reported in docs | `sdmat` |
| Graph theory and combinatorics | [Structdist](../measures/cat_structdist.html) | · reported in docs | `structdist` |
| Graph theory and combinatorics | [Structure statistics](../measures/cat_statistics_structure.html) | · reported in docs | `structure.statistics` |
| Inference (QAP, null models) | [Conditional uniform graph tests and null models](../measures/cug_null_models.html) | · reported in docs | `cug.test; cugtest` |
| Inference (QAP, null models) | [Logistic MR-QAP](../measures/lr_qap.html) | · reported in docs | `netlogit` |
| Inference (QAP, null models) | [MR-QAP regression (Y-permutation, double semi-partialling)](../measures/qap_regression.html) | · reported in docs | `netlm` |
| Inference (QAP, null models) | [Network autocorrelation: lag/error model, Moran, Geary](../measures/network_autocorrelation.html) | · reported in docs | `lnam; nacf` |
| Inference (QAP, null models) | [QAP correlation (Y-permutation, exact and Monte Carlo)](../measures/qap_correlation.html) | · reported in docs | `gcor; gcov; gscor; gscov; qaptest` |
| Layout | [Stresscent](../measures/cat_stresscent.html) | · reported in docs | `stresscent` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `geodist` |
| Paths and distances | [Global and local efficiency](../measures/efficiency_global.html) | · reported in docs | `efficiency` |
| Paths and distances | [Kpath census](../measures/cat_census_kpath.html) | · reported in docs | `kpath.census` |
| Roles and positions | [Block density](../measures/block_density.html) | ✓ checked, agrees | `blockmodel` |
| Roles and positions | [Brokerage](../measures/brokerage.html) | ✓ checked, agrees | `brokerage` |
| Roles and positions | [Cognitive social structures with accuracy measures](../measures/css_accuracy.html) | · reported in docs | `consensus` |
| Roles and positions | [Hierarchy](../measures/hierarchy.html) | · reported in docs | `hierarchy` |
| Roles and positions | [Regular equivalence](../measures/regular_equivalence.html) | ✓ checked, agrees | `redist` |
| Roles and positions | [Structural equivalence](../measures/structural_equivalence.html) | ✓ checked, agrees | `sedist` |
| Traversal, trees and DAGs | [Isolates](../measures/gb_isolates.html) | · reported in docs | `isolates` |
| Two-mode and bipartite | [Ego members](../measures/ego_members.html) | · reported in docs | `ego.extract` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F041](../findings.html#f041) | defect | Information centrality fails on singular inputs |
| [F042](../findings.html#f042) | convention | Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default |
| [F043](../findings.html#f043) | convention | Closeness and centralization normalizations differ from other tools |
| [F044](../findings.html#f044) | convention | Reciprocity correlation is 0 on a single arc |
{% endraw %}
