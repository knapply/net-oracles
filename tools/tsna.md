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

| Family | Measure | State | API names |
|---|---|---|---|
| Descriptive statistics | [T Edge Density](../measures/cat_density_edge_t.html) | · reported in docs | `tEdgeDensity` |
| Generators and rewiring | [T Edge Formation](../measures/cat_edge_formation_t.html) | · reported in docs | `tEdgeFormation` |
| Graph theory and combinatorics | [Edge Duration](../measures/cat_duration_edge.html) | · reported in docs | `edgeDuration` |
| Graph theory and combinatorics | [P Shift Count](../measures/cat_count_p_shift.html) | · reported in docs | `pShiftCount` |
| Graph theory and combinatorics | [T Degree](../measures/cat_degree_t.html) | · reported in docs | `tDegree` |
| Graph theory and combinatorics | [T Edge Dissolution](../measures/cat_dissolution_edge_t.html) | · reported in docs | `tEdgeDissolution` |
| Graph theory and combinatorics | [Tied Duration](../measures/cat_duration_tied.html) | · reported in docs | `tiedDuration` |
| Graph theory and combinatorics | [Vertex Duration](../measures/cat_duration.html) | · reported in docs | `vertexDuration` |
| Temporal and events | [T Ergm Stats](../measures/cat_ergm_stats_t.html) | · reported in docs | `tErgmStats` |
| Temporal and events | [T Sna Stats](../measures/cat_sna_stats_t.html) | · reported in docs | `tSnaStats` |
| Temporal and events | [Temporal paths](../measures/temporal_paths.html) | ✓ checked, agrees | `tPath` |
| Temporal and events | [Temporal reach](../measures/temporal_reach.html) | ✓ checked, agrees | `forward.reachable; tReach` |
| Temporal and events | [Time Projected Network](../measures/cat_projected_time.html) | · reported in docs | `timeProjectedNetwork` |
{% endraw %}
