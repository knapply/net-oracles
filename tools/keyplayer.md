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

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Distance-based | [Reach and m-reach](../measures/centrality/reach_centrality.html) | [Mreach closeness](../measures/centrality/reach_centrality.html#cat_closeness_mreach) | · reported in docs | `mreach.closeness` |
| Centrality | Distance-based | [Reach and m-reach](../measures/centrality/reach_centrality.html) | [Mreach degree](../measures/centrality/reach_centrality.html#cat_degree_mreach) | · reported in docs | `mreach.degree` |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / distance\_fragmentation](../measures/centrality/key_player_set.html#kpp_optimum-distance_fragmentation) | ✓ checked, agrees |  |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / distance\_reach](../measures/centrality/key_player_set.html#kpp_optimum-distance_reach) | ✓ checked, agrees |  |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / m\_reach](../measures/centrality/key_player_set.html#kpp_optimum-m_reach) | ✓ checked, agrees | `kpcent` |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpset](../measures/centrality/key_player_set.html#cat_kpset) | · reported in docs | `kpset` |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / distance\_fragmentation](../measures/centrality/key_player_single.html#kpp_single-distance_fragmentation) | ≠ checked, differs by convention | `fragment` |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / distance\_reach](../measures/centrality/key_player_single.html#kpp_single-distance_reach) | ≠ checked, differs by convention |  |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / m\_reach](../measures/centrality/key_player_single.html#kpp_single-m_reach) | ✓ checked, agrees |  |
| Centrality | Local and structural scores | [Diffusion centrality and diffusion degree](../measures/centrality/diffusion_centrality.html) | [Diffusion](../measures/centrality/diffusion_centrality.html#cat_diffusion) | · reported in docs | `diffusion` |
| Graph theory and combinatorics | Spanners, contraction and reduction | [Node contraction](../measures/graph-theory-and-combinatorics/contracted_nodes.html) | [Contracted nodes](../measures/graph-theory-and-combinatorics/contracted_nodes.html#nxs_contracted_nodes) | · reported in docs | `contract` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F012](../findings.html#f012) | defect | Weighted distances (binary = FALSE) are not shortest-path lengths |
{% endraw %}
