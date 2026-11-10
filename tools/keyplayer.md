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
| <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | 4 |
| <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | 2 |
| <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | 5 |

Every state other than checked, agrees has a reason, shown in the last column and in full on the measure's page. The states are defined on [How entries are labelled](../method.html).

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names | Why, if not agrees |
|---|---|---|---|---|---|---|
| Centrality | Distance-based | [Reach and m-reach](../measures/centrality/reach_centrality.html) | [Mreach closeness](../measures/centrality/reach_centrality.html#cat_closeness_mreach) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `mreach.closeness` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/reach_centrality.html#why-cat_closeness_mreach-keyplayer) |
| Centrality | Distance-based | [Reach and m-reach](../measures/centrality/reach_centrality.html) | [Mreach degree](../measures/centrality/reach_centrality.html#cat_degree_mreach) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `mreach.degree` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/reach_centrality.html#why-cat_degree_mreach-keyplayer) |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / distance\_fragmentation](../measures/centrality/key_player_set.html#kpp_optimum-distance_fragmentation) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / distance\_reach](../measures/centrality/key_player_set.html#kpp_optimum-distance_reach) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpp\_optimum / m\_reach](../measures/centrality/key_player_set.html#kpp_optimum-m_reach) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> | `kpcent` |  |
| Centrality | Key players | [Key player set (KPP)](../measures/centrality/key_player_set.html) | [Kpset](../measures/centrality/key_player_set.html#cat_kpset) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `kpset` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/key_player_set.html#why-cat_kpset-keyplayer) |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / distance\_fragmentation](../measures/centrality/key_player_single.html#kpp_single-distance_fragmentation) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | `fragment` | Differs by convention (defaults, direction and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... *(reason incomplete)* [details](../measures/centrality/key_player_single.html#why-kpp_single-distance_fragmentation-keyplayer) |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / distance\_reach](../measures/centrality/key_player_single.html#kpp_single-distance_reach) | <a class="st st-t st-conv" href="../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> |  | Differs by convention (defaults and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... *(reason incomplete)* [details](../measures/centrality/key_player_single.html#why-kpp_single-distance_reach-keyplayer) |
| Centrality | Key players | [Key player single-node scores (KPP)](../measures/centrality/key_player_single.html) | [Kpp\_single / m\_reach](../measures/centrality/key_player_single.html#kpp_single-m_reach) | <a class="st st-t st-ok" href="../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |
| Centrality | Local and structural scores | [Diffusion centrality and diffusion degree](../measures/centrality/diffusion_centrality.html) | [Diffusion](../measures/centrality/diffusion_centrality.html#cat_diffusion) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `diffusion` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/centrality/diffusion_centrality.html#why-cat_diffusion-keyplayer) |
| Graph theory and combinatorics | Spanners, contraction and reduction | [Node contraction](../measures/graph-theory-and-combinatorics/contracted_nodes.html) | [Contracted nodes](../measures/graph-theory-and-combinatorics/contracted_nodes.html#nxs_contracted_nodes) | <a class="st st-t st-docs" href="../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | `contract` | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](../measures/graph-theory-and-combinatorics/contracted_nodes.html#why-nxs_contracted_nodes-keyplayer) |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F012](../findings.html#f012) | defect | Weighted distances (binary = FALSE) are not shortest-path lengths |
{% endraw %}
