---
title: "keyplayer"
layout: default
parent: Tools
---

{% raw %}
# keyplayer

| Field | Value |
|---|---|
| Identifier | `keyplayer` |
| Language | R |
| Version tested | 1.0.4 |
| License | see package DESCRIPTION |
| Homepage | <https://cran.r-project.org/package=keyplayer> |
| Role | checked |
| Citation | [an2016keyplayer](../references.html#an2016keyplayer) |

## How it was run

Called from R on adjacency matrices.

Capabilities listed by introspection of R package keyplayer: exported functions and help titles.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 4 |
| checked, differs by convention (≠) | 2 |
| reported in docs (·) | 5 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Diffusion](../measures/cat_diffusion.html) | · reported in docs | `diffusion` |
| Centrality | [Kpp\_optimum / distance\_fragmentation](../measures/kpp_optimum-distance_fragmentation.html) | ✓ checked, agrees |  |
| Centrality | [Kpp\_optimum / distance\_reach](../measures/kpp_optimum-distance_reach.html) | ✓ checked, agrees |  |
| Centrality | [Kpp\_optimum / m\_reach](../measures/kpp_optimum-m_reach.html) | ✓ checked, agrees | `kpcent` |
| Centrality | [Kpp\_single / distance\_fragmentation](../measures/kpp_single-distance_fragmentation.html) | ≠ checked, differs by convention | `fragment` |
| Centrality | [Kpp\_single / distance\_reach](../measures/kpp_single-distance_reach.html) | ≠ checked, differs by convention |  |
| Centrality | [Kpp\_single / m\_reach](../measures/kpp_single-m_reach.html) | ✓ checked, agrees |  |
| Centrality | [Mreach closeness](../measures/cat_closeness_mreach.html) | · reported in docs | `mreach.closeness` |
| Graph theory and combinatorics | [Contracted nodes](../measures/nxs_contracted_nodes.html) | · reported in docs | `contract` |
| Graph theory and combinatorics | [Kpset](../measures/cat_kpset.html) | · reported in docs | `kpset` |
| Paths and distances | [Mreach degree](../measures/cat_degree_mreach.html) | · reported in docs | `mreach.degree` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F012](../findings.html#f012) | defect | Weighted distances (binary = FALSE) are not shortest-path lengths |
{% endraw %}
