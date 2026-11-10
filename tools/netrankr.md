---
title: "netrankr"
layout: default
parent: Tools
---

{% raw %}

# netrankr

| Field | Value |
|---|---|
| Identifier | `netrankr` |
| Language | R |
| Version tested | 2.0.0 |
| License | MIT |
| Homepage | <https://cran.r-project.org/package=netrankr> |
| Role | checked |
| Citation | [schoch2018centrality](../references.html#schoch2018centrality) |

## How it was run

Called from R on igraph objects.

Capabilities listed by introspection of R package netrankr: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 5 |
| checked, differs by convention (≠) | 3 |
| reported in docs (·) | 34 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | ≠ checked, differs by convention | `aggregate_positions` |
| Centrality | Betweenness, load and flow | [Current-flow betweenness](../measures/centrality/current_flow_betweenness.html) | [Cx current flow](../measures/centrality/current_flow_betweenness.html#cx_current_flow) | ✓ checked, agrees |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | ≠ checked, differs by convention |  |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Swan closeness](../measures/centrality/closeness.html#cat_closeness_swan) | · reported in docs | `swan_closeness` |
| Centrality | Distance-based | [Harmonic centrality](../measures/centrality/harmonic_centrality.html) | [Harmonic](../measures/centrality/harmonic_centrality.html#harmonic) | ✓ checked, agrees |  |
| Centrality | Partial rankings (netrankr) | [Hyperbolic index](../measures/centrality/hyperbolic_index.html) | [Hyperbolic index](../measures/centrality/hyperbolic_index.html#cat_hyperbolic) | · reported in docs | `hyperbolic_index` |
| Centrality | Partial rankings (netrankr) | [Neighborhood inclusion](../measures/centrality/neighborhood_inclusion.html) | [Neighborhood inclusion](../measures/centrality/neighborhood_inclusion.html#cat_inclusion_neighborhood) | · reported in docs | `neighborhood_inclusion` |
| Centrality | Partial rankings (netrankr) | [Neighborhood inclusion](../measures/centrality/neighborhood_inclusion.html) | [Neighborhood inclusion, positional dominance, rank intervals](../measures/centrality/neighborhood_inclusion.html#partial_ranking) | · reported in docs |  |
| Centrality | Partial rankings (netrankr) | [Positional dominance](../measures/centrality/positional_dominance.html) | [Positional dominance](../measures/centrality/positional_dominance.html#cat_dominance_positional) | · reported in docs | `positional_dominance` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Comparable pairs](../measures/centrality/rank_comparison.html#cat_comparable_pairs) | · reported in docs | `comparable_pairs` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Compare ranks](../measures/centrality/rank_comparison.html#cat_compare_ranks) | · reported in docs | `compare_ranks` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Get rankings](../measures/centrality/rank_comparison.html#cat_rankings) | · reported in docs | `get_rankings` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Incomparable pairs](../measures/centrality/rank_comparison.html#cat_incomparable_pairs) | · reported in docs | `incomparable_pairs` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Index builder](../measures/centrality/rank_comparison.html#cat_builder) | · reported in docs | `index_builder` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Is preserved](../measures/centrality/rank_comparison.html#cat_is_preserved) | · reported in docs | `is_preserved` |
| Centrality | Partial rankings (netrankr) | [Rank comparison and ordering](../measures/centrality/rank_comparison.html) | [Majorization gap](../measures/centrality/rank_comparison.html#cat_gap_majorization) | · reported in docs | `majorization_gap` |
| Centrality | Partial rankings (netrankr) | [Rank intervals](../measures/centrality/rank_intervals.html) | [Rank intervals](../measures/centrality/rank_intervals.html#cat_intervals_rank) | · reported in docs | `rank_intervals` |
| Centrality | Partial rankings (netrankr) | [Rank probabilities and expected ranks](../measures/centrality/rank_probabilities.html) | [Approx rank expected](../measures/centrality/rank_probabilities.html#cat_approx_expected_rank) | · reported in docs | `approx_rank_expected` |
| Centrality | Partial rankings (netrankr) | [Rank probabilities and expected ranks](../measures/centrality/rank_probabilities.html) | [Approx rank relative](../measures/centrality/rank_probabilities.html#cat_approx_rank_relative) | · reported in docs | `approx_rank_relative` |
| Centrality | Partial rankings (netrankr) | [Rank probabilities and expected ranks](../measures/centrality/rank_probabilities.html) | [Exact rank prob](../measures/centrality/rank_probabilities.html#cat_exact_prob_rank) | · reported in docs | `exact_rank_prob` |
| Centrality | Partial rankings (netrankr) | [Rank probabilities and expected ranks](../measures/centrality/rank_probabilities.html) | [Mcmc rank prob](../measures/centrality/rank_probabilities.html#cat_mcmc_prob_rank) | · reported in docs | `mcmc_rank_prob` |
| Centrality | Resistance and information | [Information centrality (current-flow closeness)](../measures/centrality/information_centrality.html) | [Current flow closeness](../measures/centrality/information_centrality.html#cx_current_flow_closeness) | ✓ checked, agrees |  |
| Centrality | Resistance and information | [Information centrality (current-flow closeness)](../measures/centrality/information_centrality.html) | [Information centrality](../measures/centrality/information_centrality.html#information_centrality) | ✓ checked, agrees |  |
| Centrality | Spectral and walk-based | [Communicability](../measures/centrality/communicability.html) | [Communicability](../measures/centrality/communicability.html#cx_communicability) | ≠ checked, differs by convention | `indirect_relations` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Distance transformations for indices](../measures/centrality/distance_transform_indices.html) | [Dist 2pow](../measures/centrality/distance_transform_indices.html#cat_2pow_dist) | · reported in docs | `dist_2pow` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Distance transformations for indices](../measures/centrality/distance_transform_indices.html) | [Dist dpow](../measures/centrality/distance_transform_indices.html#cat_dist_dpow) | · reported in docs | `dist_dpow` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Distance transformations for indices](../measures/centrality/distance_transform_indices.html) | [Dist inv](../measures/centrality/distance_transform_indices.html#cat_dist_inv) | · reported in docs | `dist_inv` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Distance transformations for indices](../measures/centrality/distance_transform_indices.html) | [Dist powd](../measures/centrality/distance_transform_indices.html#cat_dist_powd) | · reported in docs | `dist_powd` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Distance transformations for indices](../measures/centrality/distance_transform_indices.html) | [Swan combinatory](../measures/centrality/distance_transform_indices.html#cat_combinatory_swan) | · reported in docs | `swan_combinatory` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks attenuated](../measures/centrality/walk_indices.html#cat_attenuated_walk) | · reported in docs | `walks_attenuated` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks exp](../measures/centrality/walk_indices.html#cat_exp_walk) | · reported in docs | `walks_exp` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks exp even](../measures/centrality/walk_indices.html#cat_even_exp_walk) | · reported in docs | `walks_exp_even` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks exp odd](../measures/centrality/walk_indices.html#cat_exp_odd_walk) | · reported in docs | `walks_exp_odd` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks limit prop](../measures/centrality/walk_indices.html#cat_limit_prop_walk) | · reported in docs | `walks_limit_prop` |
| Centrality | Walk-based and distance-based indices (netrankr) | [Walk-based index components](../measures/centrality/walk_indices.html) | [Walks uptok](../measures/centrality/walk_indices.html#cat_uptok_walk) | · reported in docs | `walks_uptok` |
| Components and connectivity | Connectivity numbers | [Swan connectivity](../measures/components-and-connectivity/connectivity_swan.html) | [Swan connectivity](../measures/components-and-connectivity/connectivity_swan.html#cat_connectivity_swan) | · reported in docs | `swan_connectivity` |
| Generators and rewiring | Named and deterministic graphs | [Dominance graph](../measures/generators-and-rewiring/dominance_graph.html) | [Dominance graph](../measures/generators-and-rewiring/dominance_graph.html#cat_dominance) | · reported in docs | `dominance_graph` |
| Graph theory and combinatorics | Chordal, perfect and special graph classes | [Threshold graphs](../measures/graph-theory-and-combinatorics/threshold_graph.html) | [Threshold graphs](../measures/graph-theory-and-combinatorics/threshold_graph.html#threshold_graph) | · reported in docs | `threshold_graph` |
| Matrices and spectra | Spectra | [Spectral gap](../measures/matrices-and-spectra/spectral_gap.html) | [Spectral gap](../measures/matrices-and-spectra/spectral_gap.html#cat_gap_spectral) | · reported in docs | `spectral_gap` |
| Paths and distances | Efficiency and reachability | [Global and local efficiency](../measures/paths-and-distances/global_efficiency.html) | [Swan efficiency](../measures/paths-and-distances/global_efficiency.html#cat_efficiency_swan) | · reported in docs | `swan_efficiency` |
| Paths and distances | Resistance and spectral distances | [Resistance distance and effective resistance](../measures/paths-and-distances/resistance_distance.html) | [Resistance](../measures/paths-and-distances/resistance_distance.html#cx_resistance) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | DAGs and topological order | [Transitive reduction](../measures/traversal-trees-and-dags/transitive_reduction.html) | [Reduction](../measures/traversal-trees-and-dags/transitive_reduction.html#reduction) | · reported in docs | `transitive_reduction` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F079](../findings.html#f079) | convention | depend\_sp and depend\_curflow count both orderings of an unordered pair |
| [F080](../findings.html#f080) | convention | dist\_resist with invsum is the standard value divided by n |
| [F081](../findings.html#f081) | convention | Empty distance sum inverts to 0 |
{% endraw %}
