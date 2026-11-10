---
title: "RSiena"
layout: default
parent: Tools
---

{% raw %}
# RSiena

| Field | Value |
|---|---|
| Identifier | `rsiena` |
| Language | R |
| Version tested | 1.6.6 |
| License | GPL-2.0-or-later |
| Homepage | <https://cran.r-project.org/package=RSiena> |
| Role | checked |
| Citation | [ripley2026manual](../references.html#ripley2026manual) |

## How it was run

Called from R; effects and simulations evaluated on small panel data sets.

Capabilities listed by introspection of RSiena exported functions and help titles; effects from getEffects().

## Coverage

| State | Measures |
|---|---|
| checked, differs by convention (≠) | 1 |
| reported in docs (·) | 278 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | · reported in docs | `between` |
| Cohesion and subgroups | [Beh Dense Triads](../measures/cat_beh_dense_triads.html) | · reported in docs | `behDenseTriads` |
| Cohesion and subgroups | [Dense Triads](../measures/cat_dense_triads.html) | · reported in docs | `denseTriads` |
| Cohesion and subgroups | [Mixed Triad Census](../measures/cat_census_mixed_triad.html) | · reported in docs | `mixedTriadCensus` |
| Cohesion and subgroups | [Sim Dense Triads](../measures/cat_dense_sim_triads.html) | · reported in docs | `simDenseTriads` |
| Descriptive statistics | [Density](../measures/density.html) | · reported in docs | `density` |
| Descriptive statistics | [Triad census](../measures/triad_census.html) | · reported in docs | `TriadCensus` |
| Graph theory and combinatorics | [Abs Diff X](../measures/cat_abs_diff_x.html) | · reported in docs | `absDiffX` |
| Graph theory and combinatorics | [Agreetrans](../measures/cat_agreetrans.html) | · reported in docs | `agreetrans` |
| Graph theory and combinatorics | [Alt Dist2](../measures/cat_alt_dist2.html) | · reported in docs | `altDist2; altInDist2` |
| Graph theory and combinatorics | [Alt LThreshold X](../measures/cat_alt_l_threshold_x.html) | · reported in docs | `altLThresholdX` |
| Graph theory and combinatorics | [Alt RThreshold X](../measures/cat_alt_r_threshold_x.html) | · reported in docs | `altRThresholdX` |
| Graph theory and combinatorics | [Alt Sq X](../measures/cat_alt_sq_x.html) | · reported in docs | `altSqX` |
| Graph theory and combinatorics | [Alt X](../measures/cat_alt_x.html) | · reported in docs | `altX` |
| Graph theory and combinatorics | [Alt XOut Act](../measures/cat_act_alt_out_x.html) | · reported in docs | `altXOutAct` |
| Graph theory and combinatorics | [Anti In Iso](../measures/cat_anti_iso.html) | · reported in docs | `antiInIso; antiIso` |
| Graph theory and combinatorics | [Anti In Iso2](../measures/cat_anti_iso2.html) | · reported in docs | `antiInIso2` |
| Graph theory and combinatorics | [Any In Exposure Dist2](../measures/cat_any_dist2_exposure.html) | · reported in docs | `anyInExposureDist2` |
| Graph theory and combinatorics | [Av Alt](../measures/cat_alt_av.html) | · reported in docs | `avAlt; avInAlt` |
| Graph theory and combinatorics | [Av Alt Alt X](../measures/cat_alt_av_x.html) | · reported in docs | `avAltAltX; avXAlt; avXInAlt` |
| Graph theory and combinatorics | [Av Alt cc](../measures/cat_alt_av_cc.html) | · reported in docs | `avAlt_cc` |
| Graph theory and combinatorics | [Av Alt Dist2](../measures/cat_alt_av_dist2.html) | · reported in docs | `avAltDist2; avInAltDist2` |
| Graph theory and combinatorics | [Av Alt gmm](../measures/cat_alt_av_gmm.html) | · reported in docs | `avAlt_gmm` |
| Graph theory and combinatorics | [Av Alt Pop](../measures/cat_alt_av_pop.html) | · reported in docs | `avAltPop` |
| Graph theory and combinatorics | [Av Alt Same X](../measures/cat_alt_av_same_x.html) | · reported in docs | `avAltSameX; avSameXAlt; avSameXInAlt` |
| Graph theory and combinatorics | [Av Alt W](../measures/cat_alt_av_w.html) | · reported in docs | `avAltW; avInAltW; avWAlt; avWInAlt` |
| Graph theory and combinatorics | [Av Att Higher](../measures/cat_att_av_higher.html) | · reported in docs | `avAttHigher` |
| Graph theory and combinatorics | [Av Att Lower](../measures/cat_att_av_lower.html) | · reported in docs | `avAttLower` |
| Graph theory and combinatorics | [Av Deg](../measures/cat_av_deg.html) | · reported in docs | `avDeg` |
| Graph theory and combinatorics | [Av Exposure](../measures/cat_av_exposure.html) | · reported in docs | `avExposure` |
| Graph theory and combinatorics | [Av Group](../measures/cat_av_group.html) | · reported in docs | `avGroup` |
| Graph theory and combinatorics | [Av In Alt Dist2 nc](../measures/cat_alt_av_dist2_nc.html) | · reported in docs | `avInAltDist2_nc` |
| Graph theory and combinatorics | [Av In Sim](../measures/cat_av_sim.html) | · reported in docs | `avInSim; avSim` |
| Graph theory and combinatorics | [Av In Sim Dist2](../measures/cat_av_dist2_sim.html) | · reported in docs | `avInSimDist2` |
| Graph theory and combinatorics | [Av In Sim Pop Alt](../measures/cat_alt_av_pop_sim.html) | · reported in docs | `avInSimPopAlt; avSimPopAlt` |
| Graph theory and combinatorics | [Av Rec Alt](../measures/cat_alt_av_rec.html) | · reported in docs | `avRecAlt` |
| Graph theory and combinatorics | [Av Rec Alt Same X](../measures/cat_alt_av_rec_same_x.html) | · reported in docs | `avRecAltSameX; avSameXRecAlt` |
| Graph theory and combinatorics | [Av Sim Alt X](../measures/cat_alt_av_sim_x.html) | · reported in docs | `avSimAltX` |
| Graph theory and combinatorics | [Av Sim gmm](../measures/cat_av_gmm_sim.html) | · reported in docs | `avSim_gmm` |
| Graph theory and combinatorics | [Av Sim Rec Pop](../measures/cat_av_pop_rec_sim.html) | · reported in docs | `avSimRecPop` |
| Graph theory and combinatorics | [Av Sim Recip](../measures/cat_av_recip_sim.html) | · reported in docs | `avSimRecip` |
| Graph theory and combinatorics | [Av Sim Var Alt](../measures/cat_alt_av_sim_var.html) | · reported in docs | `avSimVarAlt` |
| Graph theory and combinatorics | [Av Sim W](../measures/cat_av_sim_w.html) | · reported in docs | `avSimW` |
| Graph theory and combinatorics | [Av TAlt Dist2](../measures/cat_alt_av_dist2_t.html) | · reported in docs | `avTAltDist2; avTInAltDist2` |
| Graph theory and combinatorics | [Av TIn Alt Dist2 nc](../measures/cat_alt_av_dist2_nc_t.html) | · reported in docs | `avTInAltDist2_nc` |
| Graph theory and combinatorics | [Av Tin Exposure Dist2](../measures/cat_av_dist2_exposure_tin.html) | · reported in docs | `avTinExposureDist2` |
| Graph theory and combinatorics | [Av TXAlt Dist2](../measures/cat_alt_av_dist2_tx.html) | · reported in docs | `avTXAltDist2; avTXInAltDist2` |
| Graph theory and combinatorics | [Av XAlt Dist2](../measures/cat_alt_av_dist2_x.html) | · reported in docs | `avXAltDist2; avXInAltDist2` |
| Graph theory and combinatorics | [Av XRec Alt](../measures/cat_alt_av_rec_x.html) | · reported in docs | `avXRecAlt` |
| Graph theory and combinatorics | [Beh Unsp Int](../measures/cat_beh_int_unsp.html) | · reported in docs | `behUnspInt` |
| Graph theory and combinatorics | [Cross XOut Act](../measures/cat_act_cross_out_x.html) | · reported in docs | `crossXOutAct` |
| Graph theory and combinatorics | [Cy WWX](../measures/cat_cy_wwx.html) | · reported in docs | `cyWWX` |
| Graph theory and combinatorics | [Cycle3](../measures/cat_cycle3.html) | · reported in docs | `cycle3` |
| Graph theory and combinatorics | [Cycle4](../measures/cat_cycle4.html) | · reported in docs | `cycle4` |
| Graph theory and combinatorics | [Deg Abs Contr X](../measures/cat_abs_contr_deg_x.html) | · reported in docs | `degAbsContrX` |
| Graph theory and combinatorics | [Deg Abs Diff X](../measures/cat_abs_deg_diff_x.html) | · reported in docs | `degAbsDiffX` |
| Graph theory and combinatorics | [Deg Neg Contr X](../measures/cat_contr_deg_neg_x.html) | · reported in docs | `degNegContrX` |
| Graph theory and combinatorics | [Deg Neg Diff X](../measures/cat_deg_diff_neg_x.html) | · reported in docs | `degNegDiffX` |
| Graph theory and combinatorics | [Deg Pos Contr X](../measures/cat_contr_deg_pos_x.html) | · reported in docs | `degPosContrX` |
| Graph theory and combinatorics | [Deg Pos Diff X](../measures/cat_deg_diff_pos_x.html) | · reported in docs | `degPosDiffX` |
| Graph theory and combinatorics | [Diff Sq X](../measures/cat_diff_sq_x.html) | · reported in docs | `diffSqX` |
| Graph theory and combinatorics | [Diff X](../measures/cat_diff_x.html) | · reported in docs | `diffX` |
| Graph theory and combinatorics | [Diff XIn Pop](../measures/cat_diff_pop_x.html) | · reported in docs | `diffXInPop` |
| Graph theory and combinatorics | [Diff XOut Act](../measures/cat_act_diff_out_x.html) | · reported in docs | `diffXOutAct` |
| Graph theory and combinatorics | [Diff XReci Act](../measures/cat_act_diff_reci_x.html) | · reported in docs | `diffXReciAct` |
| Graph theory and combinatorics | [Diff XTrans Rec Trip](../measures/cat_diff_rec_trans_trip_x.html) | · reported in docs | `diffXTransRecTrip` |
| Graph theory and combinatorics | [Diff XTrans Trip](../measures/cat_diff_trans_trip_x.html) | · reported in docs | `diffXTransTrip` |
| Graph theory and combinatorics | [Dyadic Cov](../measures/cat_cov_dyadic.html) | · reported in docs | `dyadicCov` |
| Graph theory and combinatorics | [Gwdsp FB](../measures/cat_fb_gwdsp.html) | · reported in docs | `gwdspFB` |
| Graph theory and combinatorics | [Gwdsp FF](../measures/cat_ff_gwdsp.html) | · reported in docs | `gwdspFF` |
| Graph theory and combinatorics | [Gwesp BB](../measures/cat_bb_gwesp.html) | · reported in docs | `gwespBB` |
| Graph theory and combinatorics | [Gwesp BF](../measures/cat_bf_gwesp.html) | · reported in docs | `gwespBF` |
| Graph theory and combinatorics | [Gwesp FB](../measures/cat_fb_gwesp.html) | · reported in docs | `gwespFB` |
| Graph theory and combinatorics | [Gwesp FF](../measures/cat_ff_gwesp.html) | · reported in docs | `gwespFF` |
| Graph theory and combinatorics | [Gwesp RR](../measures/cat_gwesp_rr.html) | · reported in docs | `gwespRR` |
| Graph theory and combinatorics | [Higher](../measures/cat_higher.html) | · reported in docs | `higher` |
| Graph theory and combinatorics | [Hom XOut Act](../measures/cat_act_hom_out_x.html) | · reported in docs | `homXOutAct` |
| Graph theory and combinatorics | [Hom XOut Act2](../measures/cat_act2_hom_out_x.html) | · reported in docs | `homXOutAct2` |
| Graph theory and combinatorics | [Hom XTrans Rec Trip](../measures/cat_hom_rec_trans_trip_x.html) | · reported in docs | `homXTransRecTrip` |
| Graph theory and combinatorics | [Hom XTrans Trip](../measures/cat_hom_trans_trip_x.html) | · reported in docs | `homXTransTrip` |
| Graph theory and combinatorics | [In Act](../measures/cat_act.html) | · reported in docs | `inAct` |
| Graph theory and combinatorics | [In Act c](../measures/cat_act_c.html) | · reported in docs | `inAct.c` |
| Graph theory and combinatorics | [In Act Sqrt](../measures/cat_act_sqrt.html) | · reported in docs | `inActSqrt` |
| Graph theory and combinatorics | [In Act X](../measures/cat_act_x.html) | · reported in docs | `inActX` |
| Graph theory and combinatorics | [In In Ass](../measures/cat_ass.html) | · reported in docs | `inInAss` |
| Graph theory and combinatorics | [In Is Degree](../measures/cat_degree_is.html) | · reported in docs | `inIsDegree` |
| Graph theory and combinatorics | [In Out Ass](../measures/cat_ass_out.html) | · reported in docs | `inOutAss; outInAss; outOutAss` |
| Graph theory and combinatorics | [In Pop](../measures/cat_pop.html) | · reported in docs | `inPop` |
| Graph theory and combinatorics | [In Pop c](../measures/cat_c_pop.html) | · reported in docs | `inPop.c` |
| Graph theory and combinatorics | [In Pop dya](../measures/cat_dya_pop.html) | · reported in docs | `inPop_dya` |
| Graph theory and combinatorics | [In Pop Sqrt](../measures/cat_pop_sqrt.html) | · reported in docs | `inPopSqrt` |
| Graph theory and combinatorics | [In Pop X](../measures/cat_pop_x.html) | · reported in docs | `inPopX` |
| Graph theory and combinatorics | [In Rate](../measures/cat_rate.html) | · reported in docs | `Rate; inRate` |
| Graph theory and combinatorics | [In Rate Inv](../measures/cat_inv_rate.html) | · reported in docs | `inRateInv` |
| Graph theory and combinatorics | [In Rate Log](../measures/cat_log_rate.html) | · reported in docs | `inRateLog` |
| Graph theory and combinatorics | [In Struct Eq](../measures/cat_eq_struct.html) | · reported in docs | `inStructEq` |
| Graph theory and combinatorics | [In WWX](../measures/cat_wwx.html) | · reported in docs | `InWWX; WWX` |
| Graph theory and combinatorics | [In2 Plus](../measures/cat_in2_plus.html) | · reported in docs | `in2Plus` |
| Graph theory and combinatorics | [In3 Plus](../measures/cat_in3_plus.html) | · reported in docs | `in3Plus` |
| Graph theory and combinatorics | [Indeg](../measures/cat_indeg.html) | · reported in docs | `indeg` |
| Graph theory and combinatorics | [Indeg Av Group](../measures/cat_av_group_indeg.html) | · reported in docs | `indegAvGroup` |
| Graph theory and combinatorics | [Indeg Tot Group](../measures/cat_group_indeg_tot.html) | · reported in docs | `indegTotGroup` |
| Graph theory and combinatorics | [Infect Covar](../measures/cat_covar_infect.html) | · reported in docs | `infectCovar` |
| Graph theory and combinatorics | [Infect In](../measures/cat_infect.html) | · reported in docs | `infectIn` |
| Graph theory and combinatorics | [Infect Out](../measures/cat_infect_out.html) | · reported in docs | `infectOut` |
| Graph theory and combinatorics | [Isolate](../measures/cat_isolate.html) | · reported in docs | `isolate` |
| Graph theory and combinatorics | [Isolate Net](../measures/cat_isolate_net.html) | · reported in docs | `isolateNet` |
| Graph theory and combinatorics | [Isolate Pop](../measures/cat_isolate_pop.html) | · reported in docs | `isolatePop` |
| Graph theory and combinatorics | [Jin](../measures/cat_jin.html) | · reported in docs | `Jin` |
| Graph theory and combinatorics | [Jout](../measures/cat_jout.html) | · reported in docs | `Jout` |
| Graph theory and combinatorics | [Jump XTrans Trip](../measures/cat_jump_trans_trip_x.html) | · reported in docs | `jumpXTransTrip` |
| Graph theory and combinatorics | [Max Alt](../measures/cat_alt_max.html) | · reported in docs | `maxAlt` |
| Graph theory and combinatorics | [Max Alt gmm](../measures/cat_alt_gmm_max.html) | · reported in docs | `maxAlt_gmm` |
| Graph theory and combinatorics | [Max XAlt](../measures/cat_alt_max_x.html) | · reported in docs | `maxXAlt` |
| Graph theory and combinatorics | [Min Alt](../measures/cat_alt_min.html) | · reported in docs | `minAlt` |
| Graph theory and combinatorics | [Min Alt gmm](../measures/cat_alt_gmm_min.html) | · reported in docs | `minAlt_gmm` |
| Graph theory and combinatorics | [Min XAlt](../measures/cat_alt_min_x.html) | · reported in docs | `minXAlt` |
| Graph theory and combinatorics | [Nbr Dist2](../measures/cat_dist2_nbr.html) | · reported in docs | `nbrDist2` |
| Graph theory and combinatorics | [Nbr Dist2twice](../measures/cat_dist2twice_nbr.html) | · reported in docs | `nbrDist2twice` |
| Graph theory and combinatorics | [Newrecip](../measures/cat_newrecip.html) | · reported in docs | `newrecip` |
| Graph theory and combinatorics | [Non PCompress](../measures/cat_compress_non_p.html) | · reported in docs | `nonPCompress` |
| Graph theory and combinatorics | [Out Act](../measures/cat_act_out.html) | · reported in docs | `outAct` |
| Graph theory and combinatorics | [Out Act c](../measures/cat_act_c_out.html) | · reported in docs | `outAct.c` |
| Graph theory and combinatorics | [Out Act Sqrt](../measures/cat_act_out_sqrt.html) | · reported in docs | `outActSqrt` |
| Graph theory and combinatorics | [Out Act X](../measures/cat_act_out_x.html) | · reported in docs | `outActX` |
| Graph theory and combinatorics | [Out Inv](../measures/cat_inv_out.html) | · reported in docs | `outInv` |
| Graph theory and combinatorics | [Out Iso](../measures/cat_iso_out.html) | · reported in docs | `outIso` |
| Graph theory and combinatorics | [Out Isolate](../measures/cat_isolate_out.html) | · reported in docs | `outIsolate` |
| Graph theory and combinatorics | [Out More](../measures/cat_more_out.html) | · reported in docs | `outMore` |
| Graph theory and combinatorics | [Out More2](../measures/cat_more2_out.html) | · reported in docs | `outMore2` |
| Graph theory and combinatorics | [Out More3](../measures/cat_more3_out.html) | · reported in docs | `outMore3` |
| Graph theory and combinatorics | [Out Pop](../measures/cat_out_pop.html) | · reported in docs | `outPop` |
| Graph theory and combinatorics | [Out Pop c](../measures/cat_c_out_pop.html) | · reported in docs | `outPop.c` |
| Graph theory and combinatorics | [Out Pop More](../measures/cat_more_out_pop.html) | · reported in docs | `outPopMore` |
| Graph theory and combinatorics | [Out Pop Sqrt](../measures/cat_out_pop_sqrt.html) | · reported in docs | `outPopSqrt` |
| Graph theory and combinatorics | [Out Pop Sqrt More](../measures/cat_more_out_pop_sqrt.html) | · reported in docs | `outPopSqrtMore` |
| Graph theory and combinatorics | [Out Pop Threshold](../measures/cat_out_pop_threshold.html) | · reported in docs | `outPopThreshold` |
| Graph theory and combinatorics | [Out Pop X](../measures/cat_out_pop_x.html) | · reported in docs | `outPopX` |
| Graph theory and combinatorics | [Out Rate](../measures/cat_out_rate.html) | · reported in docs | `outRate` |
| Graph theory and combinatorics | [Out Rate Inv](../measures/cat_inv_out_rate.html) | · reported in docs | `outRateInv` |
| Graph theory and combinatorics | [Out Rate Log](../measures/cat_log_out_rate.html) | · reported in docs | `outRateLog` |
| Graph theory and combinatorics | [Out Sq Inv](../measures/cat_inv_out_sq.html) | · reported in docs | `outSqInv` |
| Graph theory and combinatorics | [Out Threshold](../measures/cat_out_threshold.html) | · reported in docs | `outThreshold` |
| Graph theory and combinatorics | [Out Threshold2](../measures/cat_out_threshold2.html) | · reported in docs | `outThreshold2` |
| Graph theory and combinatorics | [Out Trunc](../measures/cat_out_trunc.html) | · reported in docs | `outTrunc` |
| Graph theory and combinatorics | [Out Trunc2](../measures/cat_out_trunc2.html) | · reported in docs | `outTrunc2` |
| Graph theory and combinatorics | [Out WWX](../measures/cat_out_wwx.html) | · reported in docs | `OutWWX` |
| Graph theory and combinatorics | [Out XMore](../measures/cat_more_out_x.html) | · reported in docs | `outXMore` |
| Graph theory and combinatorics | [Outdeg](../measures/cat_outdeg.html) | · reported in docs | `outdeg` |
| Graph theory and combinatorics | [Persistrecip](../measures/cat_persistrecip.html) | · reported in docs | `persistrecip` |
| Graph theory and combinatorics | [Pop Alt](../measures/cat_alt_pop.html) | · reported in docs | `popAlt` |
| Graph theory and combinatorics | [Prim Compress](../measures/cat_compress_prim.html) | · reported in docs | `primCompress` |
| Graph theory and combinatorics | [Prim Deg Act](../measures/cat_act_deg_prim.html) | · reported in docs | `primDegAct` |
| Graph theory and combinatorics | [Prim Deg Act Diff](../measures/cat_act_deg_diff_prim.html) | · reported in docs | `primDegActDiff` |
| Graph theory and combinatorics | [Prim Deg Act Diff Sqrt](../measures/cat_act_deg_diff_prim_sqrt.html) | · reported in docs | `primDegActDiffSqrt` |
| Graph theory and combinatorics | [Prim Deg Act Inv](../measures/cat_act_deg_inv_prim.html) | · reported in docs | `primDegActInv` |
| Graph theory and combinatorics | [Prim Deg Act Log](../measures/cat_act_deg_log_prim.html) | · reported in docs | `primDegActLog` |
| Graph theory and combinatorics | [Prim Deg Act Sqrt](../measures/cat_act_deg_prim_sqrt.html) | · reported in docs | `primDegActSqrt` |
| Graph theory and combinatorics | [Primary](../measures/cat_primary.html) | · reported in docs | `primary` |
| Graph theory and combinatorics | [Rate X](../measures/cat_rate_x.html) | · reported in docs | `RateX` |
| Graph theory and combinatorics | [Realrecip](../measures/cat_realrecip.html) | · reported in docs | `realrecip` |
| Graph theory and combinatorics | [Realtrans](../measures/cat_realtrans.html) | · reported in docs | `realtrans` |
| Graph theory and combinatorics | [Reci Act](../measures/cat_act_reci.html) | · reported in docs | `reciAct` |
| Graph theory and combinatorics | [Reci Pop](../measures/cat_pop_reci.html) | · reported in docs | `reciPop` |
| Graph theory and combinatorics | [Reci Pop Sqrt](../measures/cat_pop_reci_sqrt.html) | · reported in docs | `reciPopSqrt` |
| Graph theory and combinatorics | [Recip](../measures/cat_recip.html) | · reported in docs | `recip` |
| Graph theory and combinatorics | [Recip Deg](../measures/cat_deg_recip.html) | · reported in docs | `recipDeg` |
| Graph theory and combinatorics | [Recip Rate](../measures/cat_rate_recip.html) | · reported in docs | `recipRate` |
| Graph theory and combinatorics | [Recip Rate Inv](../measures/cat_inv_rate_recip.html) | · reported in docs | `recipRateInv` |
| Graph theory and combinatorics | [Recip Rate Log](../measures/cat_log_rate_recip.html) | · reported in docs | `recipRateLog` |
| Graph theory and combinatorics | [Same In XCycle4](../measures/cat_cycle4_same_x.html) | · reported in docs | `sameInXCycle4; sameXCycle4` |
| Graph theory and combinatorics | [Same X](../measures/cat_same_x.html) | · reported in docs | `sameX` |
| Graph theory and combinatorics | [Same XIn Pop](../measures/cat_pop_same_x.html) | · reported in docs | `sameXInPop` |
| Graph theory and combinatorics | [Same XOut Act](../measures/cat_act_out_same_x.html) | · reported in docs | `sameXOutAct` |
| Graph theory and combinatorics | [Same XReci Act](../measures/cat_act_reci_same_x.html) | · reported in docs | `sameXReciAct` |
| Graph theory and combinatorics | [Same XRecip](../measures/cat_recip_same_x.html) | · reported in docs | `sameXRecip` |
| Graph theory and combinatorics | [Same XTrans Rec Trip](../measures/cat_rec_same_trans_trip_x.html) | · reported in docs | `sameXTransRecTrip` |
| Graph theory and combinatorics | [Same XTrans Trip](../measures/cat_same_trans_trip_x.html) | · reported in docs | `sameXTransTrip` |
| Graph theory and combinatorics | [Shared Pop](../measures/cat_pop_shared.html) | · reported in docs | `sharedPop` |
| Graph theory and combinatorics | [Sim All Far](../measures/cat_all_far_sim.html) | · reported in docs | `simAllFar` |
| Graph theory and combinatorics | [Sim All Near](../measures/cat_all_near_sim.html) | · reported in docs | `simAllNear` |
| Graph theory and combinatorics | [Sim Dist2](../measures/cat_dist2_sim.html) | · reported in docs | `simDist2` |
| Graph theory and combinatorics | [Sim Recip X](../measures/cat_recip_sim_x.html) | · reported in docs | `simRecipX` |
| Graph theory and combinatorics | [Sim X](../measures/cat_sim_x.html) | · reported in docs | `simX` |
| Graph theory and combinatorics | [Sim X gmm](../measures/cat_gmm_sim_x.html) | · reported in docs | `simX_gmm` |
| Graph theory and combinatorics | [Sim XTrans Trip](../measures/cat_sim_trans_trip_x.html) | · reported in docs | `simXTransTrip` |
| Graph theory and combinatorics | [Suscept Av Covar](../measures/cat_av_covar_suscept.html) | · reported in docs | `susceptAvCovar` |
| Graph theory and combinatorics | [Suscept Av In](../measures/cat_av_suscept.html) | · reported in docs | `susceptAvIn` |
| Graph theory and combinatorics | [Threshold](../measures/cat_threshold.html) | · reported in docs | `threshold` |
| Graph theory and combinatorics | [Threshold2](../measures/cat_threshold2.html) | · reported in docs | `threshold2` |
| Graph theory and combinatorics | [Threshold3](../measures/cat_threshold3.html) | · reported in docs | `threshold3` |
| Graph theory and combinatorics | [Threshold4](../measures/cat_threshold4.html) | · reported in docs | `threshold4` |
| Graph theory and combinatorics | [Tot AAlt Dist2](../measures/cat_a_alt_dist2_tot.html) | · reported in docs | `totAAltDist2; totAInAltDist2` |
| Graph theory and combinatorics | [Tot AIn Alt Dist2 nc](../measures/cat_a_alt_dist2_nc_tot.html) | · reported in docs | `totAInAltDist2_nc` |
| Graph theory and combinatorics | [Tot AIn Exposure Dist2](../measures/cat_a_dist2_exposure_tot.html) | · reported in docs | `totAInExposureDist2` |
| Graph theory and combinatorics | [Tot Alt](../measures/cat_alt_tot.html) | · reported in docs | `totAlt; totInAlt` |
| Graph theory and combinatorics | [Tot Alt cc](../measures/cat_alt_cc_tot.html) | · reported in docs | `totAlt_cc` |
| Graph theory and combinatorics | [Tot Alt Dist2](../measures/cat_alt_dist2_tot.html) | · reported in docs | `totAltDist2; totInAltDist2` |
| Graph theory and combinatorics | [Tot Alt gmm](../measures/cat_alt_gmm_tot.html) | · reported in docs | `totAlt_gmm` |
| Graph theory and combinatorics | [Tot Alt Pop](../measures/cat_alt_pop_tot.html) | · reported in docs | `totAltPop; totPopAlt` |
| Graph theory and combinatorics | [Tot Alt Same X](../measures/cat_alt_same_tot_x.html) | · reported in docs | `totAltSameX; totSameXAlt; totSameXInAlt` |
| Graph theory and combinatorics | [Tot Alt W](../measures/cat_alt_tot_w.html) | · reported in docs | `totAltW; totInAltW; totWAlt; totWInAlt` |
| Graph theory and combinatorics | [Tot Att Higher](../measures/cat_att_higher_tot.html) | · reported in docs | `totAttHigher` |
| Graph theory and combinatorics | [Tot Att Lower](../measures/cat_att_lower_tot.html) | · reported in docs | `totAttLower` |
| Graph theory and combinatorics | [Tot AXAlt Dist2](../measures/cat_alt_ax_dist2_tot.html) | · reported in docs | `totAXAltDist2; totAXInAltDist2` |
| Graph theory and combinatorics | [Tot Dist2](../measures/cat_dist2_tot.html) | · reported in docs | `totDist2; totInDist2` |
| Graph theory and combinatorics | [Tot Exposure](../measures/cat_exposure_tot.html) | · reported in docs | `totExposure` |
| Graph theory and combinatorics | [Tot Group](../measures/cat_group_tot.html) | · reported in docs | `totGroup` |
| Graph theory and combinatorics | [Tot Gwdsp FBAlt](../measures/cat_alt_fb_gwdsp_tot.html) | · reported in docs | `totGwdspFBAlt` |
| Graph theory and combinatorics | [Tot Gwdsp FBAlt nc](../measures/cat_alt_fb_gwdsp_nc_tot.html) | · reported in docs | `totGwdspFBAlt_nc` |
| Graph theory and combinatorics | [Tot Gwdsp FFAlt](../measures/cat_alt_ff_gwdsp_tot.html) | · reported in docs | `totGwdspFFAlt` |
| Graph theory and combinatorics | [Tot Gwdsp FFAlt nc](../measures/cat_alt_ff_gwdsp_nc_tot.html) | · reported in docs | `totGwdspFFAlt_nc` |
| Graph theory and combinatorics | [Tot In Alt Dist2 nc](../measures/cat_alt_dist2_nc_tot.html) | · reported in docs | `totInAltDist2_nc` |
| Graph theory and combinatorics | [Tot In Exposure Dist2](../measures/cat_dist2_exposure_tot.html) | · reported in docs | `totInExposureDist2` |
| Graph theory and combinatorics | [Tot In Sim](../measures/cat_sim_tot.html) | · reported in docs | `totInSim; totSim` |
| Graph theory and combinatorics | [Tot In Sim Dist2](../measures/cat_dist2_sim_tot.html) | · reported in docs | `totInSimDist2` |
| Graph theory and combinatorics | [Tot In Sim Pop Alt](../measures/cat_alt_pop_sim_tot.html) | · reported in docs | `totInSimPopAlt; totSimPopAlt` |
| Graph theory and combinatorics | [Tot Rec Alt](../measures/cat_alt_rec_tot.html) | · reported in docs | `totRecAlt` |
| Graph theory and combinatorics | [Tot Rec Alt Same X](../measures/cat_alt_rec_same_tot_x.html) | · reported in docs | `totRecAltSameX; totSameXRecAlt` |
| Graph theory and combinatorics | [Tot Sim Alt X](../measures/cat_alt_sim_tot_x.html) | · reported in docs | `totSimAltX` |
| Graph theory and combinatorics | [Tot Sim Rec Pop](../measures/cat_pop_rec_sim_tot.html) | · reported in docs | `totSimRecPop` |
| Graph theory and combinatorics | [Tot Sim Recip](../measures/cat_recip_sim_tot.html) | · reported in docs | `totSimRecip` |
| Graph theory and combinatorics | [Tot Sim W](../measures/cat_sim_tot_w.html) | · reported in docs | `totSimW` |
| Graph theory and combinatorics | [Tot XAlt](../measures/cat_alt_tot_x.html) | · reported in docs | `totXAlt; totXInAlt` |
| Graph theory and combinatorics | [Tot XAlt Dist2](../measures/cat_alt_dist2_tot_x.html) | · reported in docs | `totXAltDist2; totXInAltDist2` |
| Graph theory and combinatorics | [Tot XRec Alt](../measures/cat_alt_rec_tot_x.html) | · reported in docs | `totXRecAlt` |
| Graph theory and combinatorics | [Trans Med Trip](../measures/cat_med_trans_trip.html) | · reported in docs | `transMedTrip` |
| Graph theory and combinatorics | [Trans Rec Trip](../measures/cat_rec_trans_trip.html) | · reported in docs | `transRecTrip` |
| Graph theory and combinatorics | [Trans Rec Trip2](../measures/cat_rec_trans_trip2.html) | · reported in docs | `transRecTrip2` |
| Graph theory and combinatorics | [Trans Ties](../measures/cat_ties_trans.html) | · reported in docs | `transTies` |
| Graph theory and combinatorics | [Trans Trip](../measures/cat_trans_trip.html) | · reported in docs | `transTrip` |
| Graph theory and combinatorics | [Trans Trip EE](../measures/cat_ee_trans_trip.html) | · reported in docs | `transTrip.EE` |
| Graph theory and combinatorics | [Trans Trip FE](../measures/cat_fe_trans_trip.html) | · reported in docs | `transTrip.FE` |
| Graph theory and combinatorics | [Trans Trip FR](../measures/cat_fr_trans_trip.html) | · reported in docs | `transTrip.FR` |
| Graph theory and combinatorics | [Trans Trip X](../measures/cat_trans_trip_x.html) | · reported in docs | `transTripX` |
| Graph theory and combinatorics | [Trans Trip1](../measures/cat_trans_trip1.html) | · reported in docs | `transTrip1` |
| Graph theory and combinatorics | [Trans Trip2](../measures/cat_trans_trip2.html) | · reported in docs | `transTrip2` |
| Graph theory and combinatorics | [Unequal X](../measures/cat_unequal_x.html) | · reported in docs | `unequalX` |
| Graph theory and combinatorics | [Unsp Int](../measures/cat_int_unsp.html) | · reported in docs | `unspInt` |
| Graph theory and combinatorics | [Var Alt](../measures/cat_alt_var.html) | · reported in docs | `varAlt` |
| Graph theory and combinatorics | [WXX](../measures/cat_wxx.html) | · reported in docs | `WXX` |
| Graph theory and combinatorics | [X](../measures/cat_x.html) | · reported in docs | `X` |
| Graph theory and combinatorics | [XRecip](../measures/cat_recip_x.html) | · reported in docs | `XRecip` |
| Graph theory and combinatorics | [XWX](../measures/cat_xwx.html) | · reported in docs | `XWX` |
| Graph theory and combinatorics | [XWX1](../measures/cat_xwx1.html) | · reported in docs | `XWX1` |
| Graph theory and combinatorics | [XWX2](../measures/cat_xwx2.html) | · reported in docs | `XWX2` |
| Graph theory and combinatorics | [XXW](../measures/cat_xxw.html) | · reported in docs | `XXW` |
| Roles and positions | [Alt Higher Ego X](../measures/cat_alt_ego_higher_x.html) | · reported in docs | `altHigherEgoX` |
| Roles and positions | [Av Alt Ego X](../measures/cat_alt_av_ego_x.html) | · reported in docs | `avAltEgoX` |
| Roles and positions | [Av Group Ego X](../measures/cat_av_ego_group_x.html) | · reported in docs | `avGroupEgoX` |
| Roles and positions | [Av Sim Ego X](../measures/cat_av_ego_sim_x.html) | · reported in docs | `avSimEgoX` |
| Roles and positions | [Av Sim Pop Ego](../measures/cat_av_ego_pop_sim.html) | · reported in docs | `avSimPopEgo` |
| Roles and positions | [Div In ego](../measures/cat_div_ego.html) | · reported in docs | `divIn_ego` |
| Roles and positions | [Div Out ego](../measures/cat_div_ego_out.html) | · reported in docs | `divOut_ego` |
| Roles and positions | [Ego Alter Combi](../measures/cat_alter_combi_ego.html) | · reported in docs | `egoAlterCombi` |
| Roles and positions | [Ego Alter Covar Comb](../measures/cat_alter_comb_covar_ego.html) | · reported in docs | `egoAlterCovarComb` |
| Roles and positions | [Ego Diff X](../measures/cat_diff_ego_x.html) | · reported in docs | `egoDiffX` |
| Roles and positions | [Ego LThreshold X](../measures/cat_ego_l_threshold_x.html) | · reported in docs | `egoLThresholdX` |
| Roles and positions | [Ego Plus Alt Sq X](../measures/cat_alt_ego_plus_sq_x.html) | · reported in docs | `egoPlusAltSqX` |
| Roles and positions | [Ego Plus Alt X](../measures/cat_alt_ego_plus_x.html) | · reported in docs | `egoPlusAltX` |
| Roles and positions | [Ego RThreshold X](../measures/cat_ego_r_threshold_x.html) | · reported in docs | `egoRThresholdX` |
| Roles and positions | [Ego Sq X](../measures/cat_ego_sq_x.html) | · reported in docs | `egoSqX` |
| Roles and positions | [Ego X](../measures/cat_ego_x.html) | · reported in docs | `egoX` |
| Roles and positions | [Ego X gmm](../measures/cat_ego_gmm_x.html) | · reported in docs | `egoX_gmm` |
| Roles and positions | [Ego Xalt X](../measures/cat_ego_x_xalt.html) | · reported in docs | `egoXaltX` |
| Roles and positions | [Ego Xalt XRecip](../measures/cat_ego_recip_x_xalt.html) | · reported in docs | `egoXaltXRecip` |
| Roles and positions | [In Act ego](../measures/cat_act_ego.html) | · reported in docs | `inAct_ego` |
| Roles and positions | [Out Act ego](../measures/cat_act_ego_out.html) | · reported in docs | `outAct_ego` |
| Roles and positions | [Out Act More ego](../measures/cat_act_ego_more_out.html) | · reported in docs | `outActMore_ego` |
| Roles and positions | [Out Act Sqrt More ego](../measures/cat_act_ego_more_out_sqrt.html) | · reported in docs | `outActSqrtMore_ego` |
| Roles and positions | [Out More ego](../measures/cat_ego_more_out.html) | · reported in docs | `outMore_ego` |
| Roles and positions | [Reci Act ego](../measures/cat_act_ego_reci.html) | · reported in docs | `reciAct_ego` |
| Roles and positions | [Same Ego Dist2](../measures/cat_dist2_ego_same.html) | · reported in docs | `sameEgoDist2; sameEgoInDist2` |
| Roles and positions | [Sim Ego Dist2](../measures/cat_dist2_ego_sim.html) | · reported in docs | `simEgoDist2; simEgoInDist2` |
| Roles and positions | [Tot Alt Ego X](../measures/cat_alt_ego_tot_x.html) | · reported in docs | `totAltEgoX` |
| Roles and positions | [Tot Group Ego X](../measures/cat_ego_group_tot_x.html) | · reported in docs | `totGroupEgoX` |
| Roles and positions | [Tot Sim Ego X](../measures/cat_ego_sim_tot_x.html) | · reported in docs | `totSimEgoX` |
| Signed and multilayer | [Balance](../measures/cat_balance.html) | · reported in docs | `balance` |
| Statistical fitting | [Saom sim mean](../measures/saom_sim_mean.html) | ≠ checked, differs by convention | `siena07` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F085](../findings.html#f085) | defect | From a complete first wave the mean tie count stays at 5.0 |
{% endraw %}
