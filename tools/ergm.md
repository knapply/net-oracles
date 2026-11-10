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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Tripercent](../measures/cat_tripercent.html) | · reported in docs | `tripercent` |
| Cohesion and subgroups | [Opentriad](../measures/cat_opentriad.html) | · reported in docs | `opentriad` |
| Cohesion and subgroups | [Simmelian ties](../measures/simmelian.html) | · reported in docs | `simmelian` |
| Data transforms | [Full symmetrize method set and dichotomize by density](../measures/symmetrize_methods.html) | · reported in docs | `Symmetrize` |
| Descriptive statistics | [Degree](../measures/degree.html) | · reported in docs | `degree` |
| Descriptive statistics | [Density](../measures/density.html) | ≠ checked, differs by convention | `density` |
| Descriptive statistics | [Intransitive](../measures/cat_intransitive.html) | · reported in docs | `intransitive` |
| Descriptive statistics | [Reciprocity](../measures/reciprocity.html) | ✓ checked, agrees | `mutual` |
| Descriptive statistics | [Transitive](../measures/cat_transitive.html) | · reported in docs | `transitive` |
| Descriptive statistics | [Transitiveties](../measures/cat_transitiveties.html) | · reported in docs | `transitiveties` |
| Descriptive statistics | [Transitiveweights](../measures/cat_transitiveweights.html) | · reported in docs | `transitiveweights` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees | `kstar` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | ✓ checked, agrees | `triadcensus` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | · reported in docs | `triangle` |
| Graph theory and combinatorics | [Absdiff](../measures/cat_absdiff.html) | · reported in docs | `absdiff` |
| Graph theory and combinatorics | [Absdiffcat](../measures/cat_absdiffcat.html) | · reported in docs | `absdiffcat` |
| Graph theory and combinatorics | [Altkstar](../measures/cat_altkstar.html) | · reported in docs | `altkstar` |
| Graph theory and combinatorics | [Attrcov](../measures/cat_attrcov.html) | · reported in docs | `attrcov` |
| Graph theory and combinatorics | [B1concurrent](../measures/cat_b1concurrent.html) | · reported in docs | `b1concurrent` |
| Graph theory and combinatorics | [B1cov](../measures/cat_b1cov.html) | · reported in docs | `b1cov` |
| Graph theory and combinatorics | [B1degrange](../measures/cat_b1degrange.html) | · reported in docs | `b1degrange` |
| Graph theory and combinatorics | [B1degree](../measures/cat_b1degree.html) | · reported in docs | `b1degree` |
| Graph theory and combinatorics | [B1dsp](../measures/cat_b1dsp.html) | · reported in docs | `b1dsp` |
| Graph theory and combinatorics | [B1dsp L](../measures/cat_b1dsp_l.html) | · reported in docs | `b1dspL` |
| Graph theory and combinatorics | [B1factor](../measures/cat_b1factor.html) | · reported in docs | `b1factor` |
| Graph theory and combinatorics | [B1factordistinct](../measures/cat_b1factordistinct.html) | · reported in docs | `b1factordistinct` |
| Graph theory and combinatorics | [B1mindegree](../measures/cat_b1mindegree.html) | · reported in docs | `b1mindegree` |
| Graph theory and combinatorics | [B1nodematch](../measures/cat_b1nodematch.html) | · reported in docs | `b1nodematch` |
| Graph theory and combinatorics | [B1sociality](../measures/cat_b1sociality.html) | · reported in docs | `b1sociality` |
| Graph theory and combinatorics | [B1star](../measures/cat_b1star.html) | · reported in docs | `b1star` |
| Graph theory and combinatorics | [B1starmix](../measures/cat_b1starmix.html) | · reported in docs | `b1starmix` |
| Graph theory and combinatorics | [B1twostar](../measures/cat_b1twostar.html) | · reported in docs | `b1twostar` |
| Graph theory and combinatorics | [B2concurrent](../measures/cat_b2concurrent.html) | · reported in docs | `b2concurrent` |
| Graph theory and combinatorics | [B2cov](../measures/cat_b2cov.html) | · reported in docs | `b2cov` |
| Graph theory and combinatorics | [B2degrange](../measures/cat_b2degrange.html) | · reported in docs | `b2degrange` |
| Graph theory and combinatorics | [B2degree](../measures/cat_b2degree.html) | · reported in docs | `b2degree` |
| Graph theory and combinatorics | [B2dsp](../measures/cat_b2dsp.html) | · reported in docs | `b2dsp` |
| Graph theory and combinatorics | [B2dsp L](../measures/cat_b2dsp_l.html) | · reported in docs | `b2dspL` |
| Graph theory and combinatorics | [B2factor](../measures/cat_b2factor.html) | · reported in docs | `b2factor` |
| Graph theory and combinatorics | [B2factordistinct](../measures/cat_b2factordistinct.html) | · reported in docs | `b2factordistinct` |
| Graph theory and combinatorics | [B2mindegree](../measures/cat_b2mindegree.html) | · reported in docs | `b2mindegree` |
| Graph theory and combinatorics | [B2nodematch](../measures/cat_b2nodematch.html) | · reported in docs | `b2nodematch` |
| Graph theory and combinatorics | [B2sociality](../measures/cat_b2sociality.html) | · reported in docs | `b2sociality` |
| Graph theory and combinatorics | [B2star](../measures/cat_b2star.html) | · reported in docs | `b2star` |
| Graph theory and combinatorics | [B2starmix](../measures/cat_b2starmix.html) | · reported in docs | `b2starmix` |
| Graph theory and combinatorics | [B2twostar](../measures/cat_b2twostar.html) | · reported in docs | `b2twostar` |
| Graph theory and combinatorics | [Concurrent](../measures/cat_concurrent.html) | · reported in docs | `concurrent` |
| Graph theory and combinatorics | [Concurrentties](../measures/cat_concurrentties.html) | · reported in docs | `concurrentties` |
| Graph theory and combinatorics | [Ctriple](../measures/cat_ctriple.html) | · reported in docs | `ctriple` |
| Graph theory and combinatorics | [Cyclicalties](../measures/cat_cyclicalties.html) | · reported in docs | `cyclicalties` |
| Graph theory and combinatorics | [Cyclicalweights](../measures/cat_cyclicalweights.html) | · reported in docs | `cyclicalweights` |
| Graph theory and combinatorics | [Ddsp](../measures/cat_ddsp.html) | · reported in docs | `ddsp` |
| Graph theory and combinatorics | [Ddsp L](../measures/cat_ddsp_l.html) | · reported in docs | `ddspL` |
| Graph theory and combinatorics | [Degcor](../measures/cat_degcor.html) | · reported in docs | `degcor` |
| Graph theory and combinatorics | [Degcrossprod](../measures/cat_degcrossprod.html) | · reported in docs | `degcrossprod` |
| Graph theory and combinatorics | [Degrange](../measures/cat_degrange.html) | · reported in docs | `degrange` |
| Graph theory and combinatorics | [Degrange mean age](../measures/cat_age_degrange_mean.html) | · reported in docs | `degrange.mean.age` |
| Graph theory and combinatorics | [Degree mean age](../measures/cat_age_degree_mean.html) | · reported in docs | `degree.mean.age` |
| Graph theory and combinatorics | [Degree1 5](../measures/cat_5_degree1.html) | · reported in docs | `degree1.5` |
| Graph theory and combinatorics | [Degreedist](../measures/cat_degreedist.html) | · reported in docs | `degreedist` |
| Graph theory and combinatorics | [Desp](../measures/cat_desp.html) | · reported in docs | `desp` |
| Graph theory and combinatorics | [Desp L](../measures/cat_desp_l.html) | · reported in docs | `despL` |
| Graph theory and combinatorics | [Dgwdsp](../measures/cat_dgwdsp.html) | · reported in docs | `dgwdsp` |
| Graph theory and combinatorics | [Dgwdsp L](../measures/cat_dgwdsp_l.html) | · reported in docs | `dgwdspL` |
| Graph theory and combinatorics | [Dgwesp](../measures/cat_dgwesp.html) | · reported in docs | `dgwesp` |
| Graph theory and combinatorics | [Dgwesp L](../measures/cat_dgwesp_l.html) | · reported in docs | `dgwespL` |
| Graph theory and combinatorics | [Dgwnsp](../measures/cat_dgwnsp.html) | · reported in docs | `dgwnsp` |
| Graph theory and combinatorics | [Dgwnsp L](../measures/cat_dgwnsp_l.html) | · reported in docs | `dgwnspL` |
| Graph theory and combinatorics | [Dnsp](../measures/cat_dnsp.html) | · reported in docs | `dnsp` |
| Graph theory and combinatorics | [Dnsp L](../measures/cat_dnsp_l.html) | · reported in docs | `dnspL` |
| Graph theory and combinatorics | [Dyadcov](../measures/cat_dyadcov.html) | · reported in docs | `dyadcov` |
| Graph theory and combinatorics | [Edge ages](../measures/cat_ages_edge.html) | · reported in docs | `edge.ages` |
| Graph theory and combinatorics | [Edgecov](../measures/cat_edgecov.html) | · reported in docs | `edgecov` |
| Graph theory and combinatorics | [Edgecov ages](../measures/cat_ages_edgecov.html) | · reported in docs | `edgecov.ages` |
| Graph theory and combinatorics | [Edgecov mean age](../measures/cat_age_edgecov_mean.html) | · reported in docs | `edgecov.mean.age` |
| Graph theory and combinatorics | [Edges](../measures/cat_edge.html) | · reported in docs | `edges` |
| Graph theory and combinatorics | [Edges ageinterval](../measures/cat_ageinterval_edge.html) | · reported in docs | `edges.ageinterval` |
| Graph theory and combinatorics | [Gwb1degree](../measures/cat_gwb1degree.html) | · reported in docs | `gwb1degree` |
| Graph theory and combinatorics | [Gwb1dsp](../measures/cat_gwb1dsp.html) | · reported in docs | `gwb1dsp` |
| Graph theory and combinatorics | [Gwb1dsp L](../measures/cat_gwb1dsp_l.html) | · reported in docs | `gwb1dspL` |
| Graph theory and combinatorics | [Gwb2degree](../measures/cat_gwb2degree.html) | · reported in docs | `gwb2degree` |
| Graph theory and combinatorics | [Gwb2dsp](../measures/cat_gwb2dsp.html) | · reported in docs | `gwb2dsp` |
| Graph theory and combinatorics | [Gwb2dsp L](../measures/cat_gwb2dsp_l.html) | · reported in docs | `gwb2dspL` |
| Graph theory and combinatorics | [Hamming](../measures/cat_hamming.html) | · reported in docs | `hamming` |
| Graph theory and combinatorics | [Idegrange](../measures/cat_idegrange.html) | · reported in docs | `idegrange` |
| Graph theory and combinatorics | [Idegree](../measures/cat_idegree.html) | · reported in docs | `idegree` |
| Graph theory and combinatorics | [Idegree1 5](../measures/cat_5_idegree1.html) | · reported in docs | `idegree1.5` |
| Graph theory and combinatorics | [Isolatededges](../measures/cat_isolatededges.html) | · reported in docs | `isolatededges` |
| Graph theory and combinatorics | [Localtriangle](../measures/cat_localtriangle.html) | · reported in docs | `localtriangle` |
| Graph theory and combinatorics | [M2star](../measures/cat_m2star.html) | · reported in docs | `m2star` |
| Graph theory and combinatorics | [Mean age](../measures/cat_age_mean.html) | · reported in docs | `mean.age` |
| Graph theory and combinatorics | [Meandeg](../measures/cat_meandeg.html) | · reported in docs | `meandeg` |
| Graph theory and combinatorics | [Mm](../measures/cat_mm.html) | · reported in docs | `mm` |
| Graph theory and combinatorics | [Mutual L](../measures/cat_l_mutual.html) | · reported in docs | `mutualL` |
| Graph theory and combinatorics | [Nearsimmelian](../measures/cat_nearsimmelian.html) | · reported in docs | `nearsimmelian` |
| Graph theory and combinatorics | [Nodecovar](../measures/cat_nodecovar.html) | · reported in docs | `nodecovar` |
| Graph theory and combinatorics | [Nodecovrange](../measures/cat_nodecovrange.html) | · reported in docs | `nodecovrange` |
| Graph theory and combinatorics | [Nodefactor mean age](../measures/cat_age_mean_nodefactor.html) | · reported in docs | `nodefactor.mean.age` |
| Graph theory and combinatorics | [Nodefactordistinct](../measures/cat_nodefactordistinct.html) | · reported in docs | `nodefactordistinct` |
| Graph theory and combinatorics | [Nodeicov](../measures/cat_nodeicov.html) | · reported in docs | `nodeicov` |
| Graph theory and combinatorics | [Nodeicovar](../measures/cat_nodeicovar.html) | · reported in docs | `nodeicovar` |
| Graph theory and combinatorics | [Nodeicovrange](../measures/cat_nodeicovrange.html) | · reported in docs | `nodeicovrange` |
| Graph theory and combinatorics | [Nodeifactor](../measures/cat_nodeifactor.html) | · reported in docs | `nodeifactor` |
| Graph theory and combinatorics | [Nodeifactordistinct](../measures/cat_nodeifactordistinct.html) | · reported in docs | `nodeifactordistinct` |
| Graph theory and combinatorics | [Nodemix](../measures/cat_nodemix.html) | · reported in docs | `nodemix` |
| Graph theory and combinatorics | [Nodemix mean age](../measures/cat_age_mean_nodemix.html) | · reported in docs | `nodemix.mean.age` |
| Graph theory and combinatorics | [Nodeocov](../measures/cat_nodeocov.html) | · reported in docs | `nodeocov` |
| Graph theory and combinatorics | [Nodeocovar](../measures/cat_nodeocovar.html) | · reported in docs | `nodeocovar` |
| Graph theory and combinatorics | [Nodeocovrange](../measures/cat_nodeocovrange.html) | · reported in docs | `nodeocovrange` |
| Graph theory and combinatorics | [Nodeofactor](../measures/cat_nodeofactor.html) | · reported in docs | `nodeofactor` |
| Graph theory and combinatorics | [Nodeofactordistinct](../measures/cat_nodeofactordistinct.html) | · reported in docs | `nodeofactordistinct` |
| Graph theory and combinatorics | [Odegrange](../measures/cat_odegrange.html) | · reported in docs | `odegrange` |
| Graph theory and combinatorics | [Odegree](../measures/cat_odegree.html) | · reported in docs | `odegree` |
| Graph theory and combinatorics | [Odegree1 5](../measures/cat_5_odegree1.html) | · reported in docs | `odegree1.5` |
| Graph theory and combinatorics | [Receiver](../measures/cat_receiver.html) | · reported in docs | `receiver` |
| Graph theory and combinatorics | [Rlebdm](../measures/cat_rlebdm.html) | · reported in docs | `rlebdm` |
| Graph theory and combinatorics | [Sender](../measures/cat_sender.html) | · reported in docs | `sender` |
| Graph theory and combinatorics | [Simmelianties](../measures/cat_simmelianties.html) | · reported in docs | `simmelianties` |
| Graph theory and combinatorics | [Smalldiff](../measures/cat_smalldiff.html) | · reported in docs | `smalldiff` |
| Graph theory and combinatorics | [Sociality](../measures/cat_sociality.html) | · reported in docs | `sociality` |
| Graph theory and combinatorics | [Threetrail](../measures/cat_threetrail.html) | · reported in docs | `threetrail` |
| Graph theory and combinatorics | [Ttriple](../measures/cat_ttriple.html) | · reported in docs | `ttriple` |
| Graph theory and combinatorics | [Twostar L](../measures/cat_l_twostar.html) | · reported in docs | `twostarL` |
| Paths and distances | [Twopath](../measures/cat_twopath.html) | · reported in docs | `twopath` |
| Signed and multilayer | [Balance](../measures/cat_balance.html) | · reported in docs | `balance` |
| Statistical fitting | [Ergm change sums](../measures/ergm_change_sums.html) | ✓ checked, agrees |  |
| Statistical fitting | [Ergm mcmle](../measures/ergm_mcmle.html) | ✓ checked, agrees | `ergm` |
| Statistical fitting | [Ergm mple](../measures/ergm_mple.html) | ✓ checked, agrees | `ergmMPLE` |
| Statistical fitting | [Ergm sim mean](../measures/ergm_sim_mean.html) | ✓ checked, agrees | `gwdegree; nodematch` |
| Statistical fitting | [Ergm statistics](../measures/ergm_statistics.html) | ✓ checked, agrees | `gwidegree; gwodegree; istar; nodecov; nodefactor; ostar` |
| Traversal, trees and DAGs | [Cycle count](../measures/gb_cycle_count.html) | ✓ checked, agrees | `cycle; sum` |
| Traversal, trees and DAGs | [Isolates](../measures/gb_isolates.html) | · reported in docs | `isolates` |
| Two-mode and bipartite | [Coincidence](../measures/cat_coincidence.html) | · reported in docs | `coincidence` |
| Two-mode and bipartite | [Project](../measures/project.html) | · reported in docs | `Project` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F070](../findings.html#f070) | convention | A network object holds each tie once and no loops |
{% endraw %}
