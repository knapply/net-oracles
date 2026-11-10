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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `aggregate_positions` |
| Centrality | [Closeness](../measures/closeness.html) | ≠ checked, differs by convention |  |
| Centrality | [Communicability](../measures/cx_communicability.html) | ≠ checked, differs by convention | `indirect_relations` |
| Centrality | [Current flow closeness](../measures/cx_current_flow_closeness.html) | ✓ checked, agrees |  |
| Centrality | [Cx current flow](../measures/cx_current_flow.html) | ✓ checked, agrees |  |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees |  |
| Centrality | [Information centrality](../measures/information_centrality.html) | ✓ checked, agrees |  |
| Centrality | [Neighborhood inclusion, positional dominance, rank intervals](../measures/partial_ranking.html) | · reported in docs |  |
| Centrality | [Resistance](../measures/cx_resistance.html) | ✓ checked, agrees |  |
| Centrality | [Swan closeness](../measures/cat_closeness_swan.html) | · reported in docs | `swan_closeness` |
| Components and connectivity | [Swan connectivity](../measures/cat_connectivity_swan.html) | · reported in docs | `swan_connectivity` |
| Descriptive statistics | [Swan efficiency](../measures/cat_efficiency_swan.html) | · reported in docs | `swan_efficiency` |
| Generators and rewiring | [Dominance graph](../measures/cat_dominance.html) | · reported in docs | `dominance_graph` |
| Generators and rewiring | [Hyperbolic index](../measures/cat_hyperbolic.html) | · reported in docs | `hyperbolic_index` |
| Graph theory and combinatorics | [Approx rank expected](../measures/cat_approx_expected_rank.html) | · reported in docs | `approx_rank_expected` |
| Graph theory and combinatorics | [Approx rank relative](../measures/cat_approx_rank_relative.html) | · reported in docs | `approx_rank_relative` |
| Graph theory and combinatorics | [Comparable pairs](../measures/cat_comparable_pairs.html) | · reported in docs | `comparable_pairs` |
| Graph theory and combinatorics | [Compare ranks](../measures/cat_compare_ranks.html) | · reported in docs | `compare_ranks` |
| Graph theory and combinatorics | [Dist 2pow](../measures/cat_2pow_dist.html) | · reported in docs | `dist_2pow` |
| Graph theory and combinatorics | [Dist dpow](../measures/cat_dist_dpow.html) | · reported in docs | `dist_dpow` |
| Graph theory and combinatorics | [Dist inv](../measures/cat_dist_inv.html) | · reported in docs | `dist_inv` |
| Graph theory and combinatorics | [Dist powd](../measures/cat_dist_powd.html) | · reported in docs | `dist_powd` |
| Graph theory and combinatorics | [Exact rank prob](../measures/cat_exact_prob_rank.html) | · reported in docs | `exact_rank_prob` |
| Graph theory and combinatorics | [Get rankings](../measures/cat_rankings.html) | · reported in docs | `get_rankings` |
| Graph theory and combinatorics | [Incomparable pairs](../measures/cat_incomparable_pairs.html) | · reported in docs | `incomparable_pairs` |
| Graph theory and combinatorics | [Index builder](../measures/cat_builder.html) | · reported in docs | `index_builder` |
| Graph theory and combinatorics | [Is preserved](../measures/cat_is_preserved.html) | · reported in docs | `is_preserved` |
| Graph theory and combinatorics | [Majorization gap](../measures/cat_gap_majorization.html) | · reported in docs | `majorization_gap` |
| Graph theory and combinatorics | [Neighborhood inclusion](../measures/cat_inclusion_neighborhood.html) | · reported in docs | `neighborhood_inclusion` |
| Graph theory and combinatorics | [Rank intervals](../measures/cat_intervals_rank.html) | · reported in docs | `rank_intervals` |
| Graph theory and combinatorics | [Swan combinatory](../measures/cat_combinatory_swan.html) | · reported in docs | `swan_combinatory` |
| Graph theory and combinatorics | [Threshold graphs](../measures/threshold_graph.html) | · reported in docs | `threshold_graph` |
| Graph theory and combinatorics | [Walks attenuated](../measures/cat_attenuated_walk.html) | · reported in docs | `walks_attenuated` |
| Graph theory and combinatorics | [Walks exp](../measures/cat_exp_walk.html) | · reported in docs | `walks_exp` |
| Graph theory and combinatorics | [Walks exp even](../measures/cat_even_exp_walk.html) | · reported in docs | `walks_exp_even` |
| Graph theory and combinatorics | [Walks exp odd](../measures/cat_exp_odd_walk.html) | · reported in docs | `walks_exp_odd` |
| Graph theory and combinatorics | [Walks limit prop](../measures/cat_limit_prop_walk.html) | · reported in docs | `walks_limit_prop` |
| Graph theory and combinatorics | [Walks uptok](../measures/cat_uptok_walk.html) | · reported in docs | `walks_uptok` |
| Inference (QAP, null models) | [Mcmc rank prob](../measures/cat_mcmc_prob_rank.html) | · reported in docs | `mcmc_rank_prob` |
| Matrices and spectra | [Spectral gap](../measures/cat_gap_spectral.html) | · reported in docs | `spectral_gap` |
| Roles and positions | [Positional dominance](../measures/cat_dominance_positional.html) | · reported in docs | `positional_dominance` |
| Traversal, trees and DAGs | [Reduction](../measures/reduction.html) | · reported in docs | `transitive_reduction` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F079](../findings.html#f079) | convention | depend\_sp and depend\_curflow count both orderings of an unordered pair |
| [F080](../findings.html#f080) | convention | dist\_resist with invsum is the standard value divided by n |
| [F081](../findings.html#f081) | convention | Empty distance sum inverts to 0 |
{% endraw %}
