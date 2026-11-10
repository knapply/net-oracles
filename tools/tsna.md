---
title: "tsna / networkDynamic"
layout: default
parent: Tools
---

{% raw %}

# tsna / networkDynamic

| Field | Value |
|---|---|
| Identifier | `tsna` |
| Language | R |
| Version tested | 0.3.6 |
| License | GPL-3.0-only |
| Homepage | <https://cran.r-project.org/package=tsna> |
| Role | checked |
| Citation | [handcock2008statnet](../references.html#handcock2008statnet) |

## How it was run

Called from R on networkDynamic objects.

Capabilities listed by introspection of R package tsna: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 2 |
| reported in docs (·) | 11 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Temporal and events | Temporal descriptives | [Edge formation and dissolution](../measures/temporal-and-events/edge_formation_dissolution.html) | [T Edge Dissolution](../measures/temporal-and-events/edge_formation_dissolution.html#cat_dissolution_edge_t) | · reported in docs | `tEdgeDissolution` |
| Temporal and events | Temporal descriptives | [Edge formation and dissolution](../measures/temporal-and-events/edge_formation_dissolution.html) | [T Edge Formation](../measures/temporal-and-events/edge_formation_dissolution.html#cat_edge_formation_t) | · reported in docs | `tEdgeFormation` |
| Temporal and events | Temporal descriptives | [P-shift count](../measures/temporal-and-events/p_shift_count.html) | [P Shift Count](../measures/temporal-and-events/p_shift_count.html#cat_count_p_shift) | · reported in docs | `pShiftCount` |
| Temporal and events | Temporal descriptives | [Statistics over time (ergm, sna)](../measures/temporal-and-events/temporal_statistic_series.html) | [T Ergm Stats](../measures/temporal-and-events/temporal_statistic_series.html#cat_ergm_stats_t) | · reported in docs | `tErgmStats` |
| Temporal and events | Temporal descriptives | [Statistics over time (ergm, sna)](../measures/temporal-and-events/temporal_statistic_series.html) | [T Sna Stats](../measures/temporal-and-events/temporal_statistic_series.html#cat_sna_stats_t) | · reported in docs | `tSnaStats` |
| Temporal and events | Temporal descriptives | [Temporal degree](../measures/temporal-and-events/temporal_degree.html) | [T Degree](../measures/temporal-and-events/temporal_degree.html#cat_degree_t) | · reported in docs | `tDegree` |
| Temporal and events | Temporal descriptives | [Temporal edge density](../measures/temporal-and-events/temporal_edge_density.html) | [T Edge Density](../measures/temporal-and-events/temporal_edge_density.html#cat_density_edge_t) | · reported in docs | `tEdgeDensity` |
| Temporal and events | Temporal descriptives | [Temporal paths](../measures/temporal-and-events/temporal_paths.html) | [Temporal paths](../measures/temporal-and-events/temporal_paths.html#temporal_paths) | ✓ checked, agrees | `tPath` |
| Temporal and events | Temporal descriptives | [Temporal reach](../measures/temporal-and-events/temporal_reach.html) | [Temporal reach](../measures/temporal-and-events/temporal_reach.html#temporal_reach) | ✓ checked, agrees | `forward.reachable; tReach` |
| Temporal and events | Temporal descriptives | [Time-projected network](../measures/temporal-and-events/time_projected_network.html) | [Time Projected Network](../measures/temporal-and-events/time_projected_network.html#cat_projected_time) | · reported in docs | `timeProjectedNetwork` |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Edge Duration](../measures/temporal-and-events/activity_duration.html#cat_duration_edge) | · reported in docs | `edgeDuration` |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Tied Duration](../measures/temporal-and-events/activity_duration.html#cat_duration_tied) | · reported in docs | `tiedDuration` |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Vertex Duration](../measures/temporal-and-events/activity_duration.html#cat_duration) | · reported in docs | `vertexDuration` |
{% endraw %}
