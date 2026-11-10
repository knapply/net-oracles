---
title: "ergm (statnet)"
layout: default
parent: Tools
---

{% raw %}

# ergm (statnet)

| Field | Value |
|---|---|
| Identifier | `ergm` |
| Language | R |
| Version tested | 4.12.0 |
| License | GPL-3.0-only |
| Homepage | <https://cran.r-project.org/package=ergm> |
| Role | checked |
| Citation | [hunter2008ergm](../references.html#hunter2008ergm) |

## How it was run

Called from R; summary statistics evaluated on network objects (network package).

Capabilities listed by introspection of network, ergm and tergm exported functions and help titles; ergm term list from search.ergmTerms().

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 9 |
| checked, differs by convention (≠) | 1 |
| reported in docs (·) | 124 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Degree and strength | [Degree](../measures/centrality/degree.html) | [Degree](../measures/centrality/degree.html#degree) | · reported in docs | `degree` |
| Cohesion and subgroups | Relaxed cliques and subgroups | [Simmelian ties](../measures/cohesion-and-subgroups/simmelian_ties.html) | [Simmelian ties](../measures/cohesion-and-subgroups/simmelian_ties.html#simmelian) | · reported in docs | `simmelian` |
| Data transforms | Matrix and tie transformations | [Symmetrize](../measures/data-transforms/symmetrize.html) | [Full symmetrize method set and dichotomize by density](../measures/data-transforms/symmetrize.html#symmetrize_methods) | · reported in docs | `Symmetrize` |
| Descriptive statistics | Clustering and transitivity | [Global transitivity](../measures/descriptive-statistics/global_transitivity.html) | [Transitivity](../measures/descriptive-statistics/global_transitivity.html#transitivity) | ✓ checked, agrees | `kstar` |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | · reported in docs | `triangle` |
| Descriptive statistics | Density and degree distribution | [Density](../measures/descriptive-statistics/density.html) | [Density](../measures/descriptive-statistics/density.html#density) | ≠ checked, differs by convention | `density` |
| Descriptive statistics | Reciprocity, dyad and triad census | [Reciprocity](../measures/descriptive-statistics/reciprocity.html) | [Reciprocity](../measures/descriptive-statistics/reciprocity.html#reciprocity) | ✓ checked, agrees | `mutual` |
| Descriptive statistics | Reciprocity, dyad and triad census | [Triad census](../measures/descriptive-statistics/triad_census.html) | [Triad census](../measures/descriptive-statistics/triad_census.html#triad_census) | ✓ checked, agrees | `triadcensus` |
| Graph theory and combinatorics | Cycles | [Cycle census and count](../measures/graph-theory-and-combinatorics/cycle_census.html) | [Cycle count](../measures/graph-theory-and-combinatorics/cycle_census.html#gb_cycle_count) | ✓ checked, agrees | `cycle; sum` |
| Graph theory and combinatorics | Degree sequences and predicates | [Isolates](../measures/graph-theory-and-combinatorics/isolates.html) | [Isolates](../measures/graph-theory-and-combinatorics/isolates.html#gb_isolates) | · reported in docs | `isolates` |
| Statistical fitting | ERGM terms | [Balance term](../measures/statistical-fitting/ergm_balance.html) | [Balance](../measures/statistical-fitting/ergm_balance.html#cat_balance) | · reported in docs | `balance` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1concurrent](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1concurrent) | · reported in docs | `b1concurrent` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1cov](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1cov) | · reported in docs | `b1cov` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1degrange](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1degrange) | · reported in docs | `b1degrange` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1degree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1degree) | · reported in docs | `b1degree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1dsp](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1dsp) | · reported in docs | `b1dsp` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1dsp L](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1dsp_l) | · reported in docs | `b1dspL` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1factor](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1factor) | · reported in docs | `b1factor` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1factordistinct](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1factordistinct) | · reported in docs | `b1factordistinct` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1mindegree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1mindegree) | · reported in docs | `b1mindegree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1nodematch](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1nodematch) | · reported in docs | `b1nodematch` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1sociality](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1sociality) | · reported in docs | `b1sociality` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1star](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1star) | · reported in docs | `b1star` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1starmix](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1starmix) | · reported in docs | `b1starmix` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B1twostar](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b1twostar) | · reported in docs | `b1twostar` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2concurrent](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2concurrent) | · reported in docs | `b2concurrent` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2cov](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2cov) | · reported in docs | `b2cov` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2degrange](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2degrange) | · reported in docs | `b2degrange` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2degree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2degree) | · reported in docs | `b2degree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2dsp](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2dsp) | · reported in docs | `b2dsp` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2dsp L](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2dsp_l) | · reported in docs | `b2dspL` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2factor](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2factor) | · reported in docs | `b2factor` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2factordistinct](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2factordistinct) | · reported in docs | `b2factordistinct` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2mindegree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2mindegree) | · reported in docs | `b2mindegree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2nodematch](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2nodematch) | · reported in docs | `b2nodematch` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2sociality](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2sociality) | · reported in docs | `b2sociality` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2star](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2star) | · reported in docs | `b2star` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2starmix](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2starmix) | · reported in docs | `b2starmix` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [B2twostar](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_b2twostar) | · reported in docs | `b2twostar` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Coincidence](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_coincidence) | · reported in docs | `coincidence` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb1degree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1degree) | · reported in docs | `gwb1degree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb1dsp](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1dsp) | · reported in docs | `gwb1dsp` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb1dsp L](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb1dsp_l) | · reported in docs | `gwb1dspL` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb2degree](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2degree) | · reported in docs | `gwb2degree` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb2dsp](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2dsp) | · reported in docs | `gwb2dsp` |
| Statistical fitting | ERGM terms | [Bipartite terms](../measures/statistical-fitting/ergm_bipartite_terms.html) | [Gwb2dsp L](../measures/statistical-fitting/ergm_bipartite_terms.html#cat_gwb2dsp_l) | · reported in docs | `gwb2dspL` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Concurrent](../measures/statistical-fitting/ergm_degree_terms.html#cat_concurrent) | · reported in docs | `concurrent` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Concurrentties](../measures/statistical-fitting/ergm_degree_terms.html#cat_concurrentties) | · reported in docs | `concurrentties` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Degcor](../measures/statistical-fitting/ergm_degree_terms.html#cat_degcor) | · reported in docs | `degcor` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Degcrossprod](../measures/statistical-fitting/ergm_degree_terms.html#cat_degcrossprod) | · reported in docs | `degcrossprod` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Degrange](../measures/statistical-fitting/ergm_degree_terms.html#cat_degrange) | · reported in docs | `degrange` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Degree1 5](../measures/statistical-fitting/ergm_degree_terms.html#cat_5_degree1) | · reported in docs | `degree1.5` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Degreedist](../measures/statistical-fitting/ergm_degree_terms.html#cat_degreedist) | · reported in docs | `degreedist` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Idegrange](../measures/statistical-fitting/ergm_degree_terms.html#cat_idegrange) | · reported in docs | `idegrange` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Idegree](../measures/statistical-fitting/ergm_degree_terms.html#cat_idegree) | · reported in docs | `idegree` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Idegree1 5](../measures/statistical-fitting/ergm_degree_terms.html#cat_5_idegree1) | · reported in docs | `idegree1.5` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Odegrange](../measures/statistical-fitting/ergm_degree_terms.html#cat_odegrange) | · reported in docs | `odegrange` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Odegree](../measures/statistical-fitting/ergm_degree_terms.html#cat_odegree) | · reported in docs | `odegree` |
| Statistical fitting | ERGM terms | [Degree terms](../measures/statistical-fitting/ergm_degree_terms.html) | [Odegree1 5](../measures/statistical-fitting/ergm_degree_terms.html#cat_5_odegree1) | · reported in docs | `odegree1.5` |
| Statistical fitting | ERGM terms | [Distance and difference terms](../measures/statistical-fitting/ergm_distance_terms.html) | [Hamming](../measures/statistical-fitting/ergm_distance_terms.html#cat_hamming) | · reported in docs | `hamming` |
| Statistical fitting | ERGM terms | [Distance and difference terms](../measures/statistical-fitting/ergm_distance_terms.html) | [Mm](../measures/statistical-fitting/ergm_distance_terms.html#cat_mm) | · reported in docs | `mm` |
| Statistical fitting | ERGM terms | [Distance and difference terms](../measures/statistical-fitting/ergm_distance_terms.html) | [Rlebdm](../measures/statistical-fitting/ergm_distance_terms.html#cat_rlebdm) | · reported in docs | `rlebdm` |
| Statistical fitting | ERGM terms | [Edge count and density terms](../measures/statistical-fitting/ergm_edge_terms.html) | [Edges](../measures/statistical-fitting/ergm_edge_terms.html#cat_edge) | · reported in docs | `edges` |
| Statistical fitting | ERGM terms | [Edge count and density terms](../measures/statistical-fitting/ergm_edge_terms.html) | [Isolatededges](../measures/statistical-fitting/ergm_edge_terms.html#cat_isolatededges) | · reported in docs | `isolatededges` |
| Statistical fitting | ERGM terms | [Edge count and density terms](../measures/statistical-fitting/ergm_edge_terms.html) | [Meandeg](../measures/statistical-fitting/ergm_edge_terms.html#cat_meandeg) | · reported in docs | `meandeg` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Degrange mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_degrange_mean) | · reported in docs | `degrange.mean.age` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Degree mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_degree_mean) | · reported in docs | `degree.mean.age` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Edge ages](../measures/statistical-fitting/ergm_duration_terms.html#cat_ages_edge) | · reported in docs | `edge.ages` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Edgecov ages](../measures/statistical-fitting/ergm_duration_terms.html#cat_ages_edgecov) | · reported in docs | `edgecov.ages` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Edgecov mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_edgecov_mean) | · reported in docs | `edgecov.mean.age` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Edges ageinterval](../measures/statistical-fitting/ergm_duration_terms.html#cat_ageinterval_edge) | · reported in docs | `edges.ageinterval` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean) | · reported in docs | `mean.age` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Nodefactor mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean_nodefactor) | · reported in docs | `nodefactor.mean.age` |
| Statistical fitting | ERGM terms | [Edge-age terms](../measures/statistical-fitting/ergm_duration_terms.html) | [Nodemix mean age](../measures/statistical-fitting/ergm_duration_terms.html#cat_age_mean_nodemix) | · reported in docs | `nodemix.mean.age` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Absdiff](../measures/statistical-fitting/ergm_covariate_terms.html#cat_absdiff) | · reported in docs | `absdiff` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Absdiffcat](../measures/statistical-fitting/ergm_covariate_terms.html#cat_absdiffcat) | · reported in docs | `absdiffcat` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Attrcov](../measures/statistical-fitting/ergm_covariate_terms.html#cat_attrcov) | · reported in docs | `attrcov` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Dyadcov](../measures/statistical-fitting/ergm_covariate_terms.html#cat_dyadcov) | · reported in docs | `dyadcov` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Edgecov](../measures/statistical-fitting/ergm_covariate_terms.html#cat_edgecov) | · reported in docs | `edgecov` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodecovar](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodecovar) | · reported in docs | `nodecovar` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodecovrange](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodecovrange) | · reported in docs | `nodecovrange` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodefactordistinct](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodefactordistinct) | · reported in docs | `nodefactordistinct` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeicov](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicov) | · reported in docs | `nodeicov` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeicovar](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicovar) | · reported in docs | `nodeicovar` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeicovrange](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeicovrange) | · reported in docs | `nodeicovrange` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeifactor](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeifactor) | · reported in docs | `nodeifactor` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeifactordistinct](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeifactordistinct) | · reported in docs | `nodeifactordistinct` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodemix](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodemix) | · reported in docs | `nodemix` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeocov](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocov) | · reported in docs | `nodeocov` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeocovar](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocovar) | · reported in docs | `nodeocovar` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeocovrange](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeocovrange) | · reported in docs | `nodeocovrange` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeofactor](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeofactor) | · reported in docs | `nodeofactor` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Nodeofactordistinct](../measures/statistical-fitting/ergm_covariate_terms.html#cat_nodeofactordistinct) | · reported in docs | `nodeofactordistinct` |
| Statistical fitting | ERGM terms | [Nodal and dyadic covariate terms](../measures/statistical-fitting/ergm_covariate_terms.html) | [Smalldiff](../measures/statistical-fitting/ergm_covariate_terms.html#cat_smalldiff) | · reported in docs | `smalldiff` |
| Statistical fitting | ERGM terms | [Open triad term](../measures/statistical-fitting/ergm_open_triad.html) | [Opentriad](../measures/statistical-fitting/ergm_open_triad.html#cat_opentriad) | · reported in docs | `opentriad` |
| Statistical fitting | ERGM terms | [Sender, receiver and sociality terms](../measures/statistical-fitting/ergm_sender_receiver_terms.html) | [Receiver](../measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_receiver) | · reported in docs | `receiver` |
| Statistical fitting | ERGM terms | [Sender, receiver and sociality terms](../measures/statistical-fitting/ergm_sender_receiver_terms.html) | [Sender](../measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_sender) | · reported in docs | `sender` |
| Statistical fitting | ERGM terms | [Sender, receiver and sociality terms](../measures/statistical-fitting/ergm_sender_receiver_terms.html) | [Sociality](../measures/statistical-fitting/ergm_sender_receiver_terms.html#cat_sociality) | · reported in docs | `sociality` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Ddsp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_ddsp) | · reported in docs | `ddsp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Ddsp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_ddsp_l) | · reported in docs | `ddspL` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Desp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_desp) | · reported in docs | `desp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Desp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_desp_l) | · reported in docs | `despL` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwdsp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwdsp) | · reported in docs | `dgwdsp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwdsp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwdsp_l) | · reported in docs | `dgwdspL` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwesp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwesp) | · reported in docs | `dgwesp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwesp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwesp_l) | · reported in docs | `dgwespL` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwnsp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwnsp) | · reported in docs | `dgwnsp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dgwnsp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dgwnsp_l) | · reported in docs | `dgwnspL` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dnsp](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dnsp) | · reported in docs | `dnsp` |
| Statistical fitting | ERGM terms | [Shared-partner terms](../measures/statistical-fitting/ergm_shared_partner_terms.html) | [Dnsp L](../measures/statistical-fitting/ergm_shared_partner_terms.html#cat_dnsp_l) | · reported in docs | `dnspL` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [Altkstar](../measures/statistical-fitting/ergm_star_path_terms.html#cat_altkstar) | · reported in docs | `altkstar` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [M2star](../measures/statistical-fitting/ergm_star_path_terms.html#cat_m2star) | · reported in docs | `m2star` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [Mutual L](../measures/statistical-fitting/ergm_star_path_terms.html#cat_l_mutual) | · reported in docs | `mutualL` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [Threetrail](../measures/statistical-fitting/ergm_star_path_terms.html#cat_threetrail) | · reported in docs | `threetrail` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [Twopath](../measures/statistical-fitting/ergm_star_path_terms.html#cat_twopath) | · reported in docs | `twopath` |
| Statistical fitting | ERGM terms | [Star and path terms](../measures/statistical-fitting/ergm_star_path_terms.html) | [Twostar L](../measures/statistical-fitting/ergm_star_path_terms.html#cat_l_twostar) | · reported in docs | `twostarL` |
| Statistical fitting | ERGM terms | [Transitive and intransitive triple terms](../measures/statistical-fitting/ergm_transitive.html) | [Intransitive](../measures/statistical-fitting/ergm_transitive.html#cat_intransitive) | · reported in docs | `intransitive` |
| Statistical fitting | ERGM terms | [Transitive and intransitive triple terms](../measures/statistical-fitting/ergm_transitive.html) | [Transitive](../measures/statistical-fitting/ergm_transitive.html#cat_transitive) | · reported in docs | `transitive` |
| Statistical fitting | ERGM terms | [Transitive and intransitive triple terms](../measures/statistical-fitting/ergm_transitive.html) | [Transitiveties](../measures/statistical-fitting/ergm_transitive.html#cat_transitiveties) | · reported in docs | `transitiveties` |
| Statistical fitting | ERGM terms | [Transitive and intransitive triple terms](../measures/statistical-fitting/ergm_transitive.html) | [Transitiveweights](../measures/statistical-fitting/ergm_transitive.html#cat_transitiveweights) | · reported in docs | `transitiveweights` |
| Statistical fitting | ERGM terms | [Triad percentage term](../measures/statistical-fitting/ergm_triad_percent.html) | [Tripercent](../measures/statistical-fitting/ergm_triad_percent.html#cat_tripercent) | · reported in docs | `tripercent` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Ctriple](../measures/statistical-fitting/ergm_triple_terms.html#cat_ctriple) | · reported in docs | `ctriple` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Cyclicalties](../measures/statistical-fitting/ergm_triple_terms.html#cat_cyclicalties) | · reported in docs | `cyclicalties` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Cyclicalweights](../measures/statistical-fitting/ergm_triple_terms.html#cat_cyclicalweights) | · reported in docs | `cyclicalweights` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Localtriangle](../measures/statistical-fitting/ergm_triple_terms.html#cat_localtriangle) | · reported in docs | `localtriangle` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Nearsimmelian](../measures/statistical-fitting/ergm_triple_terms.html#cat_nearsimmelian) | · reported in docs | `nearsimmelian` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Simmelianties](../measures/statistical-fitting/ergm_triple_terms.html#cat_simmelianties) | · reported in docs | `simmelianties` |
| Statistical fitting | ERGM terms | [Triple, cycle and Simmelian terms](../measures/statistical-fitting/ergm_triple_terms.html) | [Ttriple](../measures/statistical-fitting/ergm_triple_terms.html#cat_ttriple) | · reported in docs | `ttriple` |
| Statistical fitting | Model fitting | [ERGM change statistics](../measures/statistical-fitting/ergm_change_sums.html) | [Ergm change sums](../measures/statistical-fitting/ergm_change_sums.html#ergm_change_sums) | ✓ checked, agrees |  |
| Statistical fitting | Model fitting | [ERGM Monte Carlo maximum likelihood](../measures/statistical-fitting/ergm_mcmle.html) | [Ergm mcmle](../measures/statistical-fitting/ergm_mcmle.html#ergm_mcmle) | ✓ checked, agrees | `ergm` |
| Statistical fitting | Model fitting | [ERGM pseudolikelihood estimation](../measures/statistical-fitting/ergm_mple.html) | [Ergm mple](../measures/statistical-fitting/ergm_mple.html#ergm_mple) | ✓ checked, agrees | `ergmMPLE` |
| Statistical fitting | Model fitting | [ERGM simulated mean statistics](../measures/statistical-fitting/ergm_sim_mean.html) | [Ergm sim mean](../measures/statistical-fitting/ergm_sim_mean.html#ergm_sim_mean) | ✓ checked, agrees | `gwdegree; nodematch` |
| Statistical fitting | Model fitting | [ERGM statistics](../measures/statistical-fitting/ergm_statistics.html) | [Ergm statistics](../measures/statistical-fitting/ergm_statistics.html#ergm_statistics) | ✓ checked, agrees | `gwidegree; gwodegree; istar; nodecov; nodefactor; ostar` |
| Two-mode and bipartite | Projection | [Bipartite projection](../measures/two-mode-and-bipartite/bipartite_projection.html) | [Project](../measures/two-mode-and-bipartite/bipartite_projection.html#project) | · reported in docs | `Project` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F070](../findings.html#f070) | convention | A network object holds each tie once and no loops |
{% endraw %}
