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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 2 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 11 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Temporal and events | Temporal descriptives | [Edge formation and dissolution](../measures/temporal-and-events/edge_formation_dissolution.html) | [T Edge Dissolution](../measures/temporal-and-events/edge_formation_dissolution.html#cat_dissolution_edge_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tEdgeDissolution` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/edge_formation_dissolution.html#why-cat_dissolution_edge_t-tsna) |
| Temporal and events | Temporal descriptives | [Edge formation and dissolution](../measures/temporal-and-events/edge_formation_dissolution.html) | [T Edge Formation](../measures/temporal-and-events/edge_formation_dissolution.html#cat_edge_formation_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tEdgeFormation` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/edge_formation_dissolution.html#why-cat_edge_formation_t-tsna) |
| Temporal and events | Temporal descriptives | [P-shift count](../measures/temporal-and-events/p_shift_count.html) | [P Shift Count](../measures/temporal-and-events/p_shift_count.html#cat_count_p_shift) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `pShiftCount` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/p_shift_count.html#why-cat_count_p_shift-tsna) |
| Temporal and events | Temporal descriptives | [Statistics over time (ergm, sna)](../measures/temporal-and-events/temporal_statistic_series.html) | [T Ergm Stats](../measures/temporal-and-events/temporal_statistic_series.html#cat_ergm_stats_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tErgmStats` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/temporal_statistic_series.html#why-cat_ergm_stats_t-tsna) |
| Temporal and events | Temporal descriptives | [Statistics over time (ergm, sna)](../measures/temporal-and-events/temporal_statistic_series.html) | [T Sna Stats](../measures/temporal-and-events/temporal_statistic_series.html#cat_sna_stats_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tSnaStats` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/temporal_statistic_series.html#why-cat_sna_stats_t-tsna) |
| Temporal and events | Temporal descriptives | [Temporal degree](../measures/temporal-and-events/temporal_degree.html) | [T Degree](../measures/temporal-and-events/temporal_degree.html#cat_degree_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tDegree` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/temporal_degree.html#why-cat_degree_t-tsna) |
| Temporal and events | Temporal descriptives | [Temporal edge density](../measures/temporal-and-events/temporal_edge_density.html) | [T Edge Density](../measures/temporal-and-events/temporal_edge_density.html#cat_density_edge_t) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tEdgeDensity` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/temporal_edge_density.html#why-cat_density_edge_t-tsna) |
| Temporal and events | Temporal descriptives | [Temporal paths](../measures/temporal-and-events/temporal_paths.html) | [Temporal paths](../measures/temporal-and-events/temporal_paths.html#temporal_paths) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `tPath` |  |
| Temporal and events | Temporal descriptives | [Temporal reach](../measures/temporal-and-events/temporal_reach.html) | [Temporal reach](../measures/temporal-and-events/temporal_reach.html#temporal_reach) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `forward.reachable; tReach` |  |
| Temporal and events | Temporal descriptives | [Time-projected network](../measures/temporal-and-events/time_projected_network.html) | [Time Projected Network](../measures/temporal-and-events/time_projected_network.html#cat_projected_time) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `timeProjectedNetwork` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/time_projected_network.html#why-cat_projected_time-tsna) |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Edge Duration](../measures/temporal-and-events/activity_duration.html#cat_duration_edge) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `edgeDuration` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/activity_duration.html#why-cat_duration_edge-tsna) |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Tied Duration](../measures/temporal-and-events/activity_duration.html#cat_duration_tied) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `tiedDuration` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/activity_duration.html#why-cat_duration_tied-tsna) |
| Temporal and events | Temporal descriptives | [Vertex, edge and tie duration](../measures/temporal-and-events/activity_duration.html) | [Vertex Duration](../measures/temporal-and-events/activity_duration.html#cat_duration) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `vertexDuration` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/temporal-and-events/activity_duration.html#why-cat_duration-tsna) |
{% endraw %}
