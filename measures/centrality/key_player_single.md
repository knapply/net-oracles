---
title: "Key player single-node scores (KPP)"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Key player single-node scores (KPP) {#concept-top}

Family: [Centrality](index.html). Subfamily: Key players. Concept id: `key_player_single`. 4 measures.

## Definition {#concept-definition}

Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Kpp\_single / distance\_fragmentation](#kpp_single-distance_fragmentation) | `kpp_single:distance_fragmentation` | 1 |
| [Kpp\_single / distance\_reach](#kpp_single-distance_reach) | `kpp_single:distance_reach` | 1 |
| [Kpp\_single / fragmentation](#kpp_single-fragmentation) | `kpp_single:fragmentation` | 1 |
| [Kpp\_single / m\_reach](#kpp_single-m_reach) | `kpp_single:m_reach` | 1 |

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Kpp\_single / distance\_fragmentation {#kpp_single-distance_fragmentation}

Measure id: `kpp_single:distance_fragmentation`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... *(reason incomplete)* [details](#why-kpp_single-distance_fragmentation-keyplayer) | `fragment` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-distance_fragmentation-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> keyplayer 1.0.4 was run and its value differs from the reference value by convention (defaults, direction and weights) on the fixtures real\_weights\_und, uniform\_weights. keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. The reference equals the definition oracle (exact shortest paths). Unresolved without reading the tool. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (kpp\_distance\_fragmentation\_single) on inputs tagged directed and edgeless and the fixtures single\_node, star8: keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node). 2 comparisons differ and 20 agree. **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_fragmentation_single` | keyplayer | any | no-value-on-some-inputs | (no value) directed, (no value) edgeless | defaults, direction, normalization, ties | abs 1e-14, rel 1e-12 | `keyplayer::fragment(adjacency, v, binary = TRUE) for each node v: 1 - sum_{j,k != v} 1/d_jk / (d (n - 1)(n - 2)), d the largest 1/d_jk (An and Liu 2016, eq. 7)` | keyplayer's fragmentation is not directional, so it is compared on undirected networks only. Its formula divides by the largest inverse distance in the residual network (1 on a binary network with any tie left, which makes it Borgatti's DF), so it is undefined when removing a node leaves no ties (the centre of star8) or no pairs (one node). |
| `kpp_distance_fragmentation_single_weighted` | keyplayer | any | differs | (no value) directed, (no value) edgeless | defaults, direction, weights | abs 1e-14, rel 1e-12 | `keyplayer::fragment(weighted adjacency, v, binary = FALSE) for each node v (edge values read as distances)` | keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths). |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_single / distance\_reach {#kpp_single-distance_reach}

Measure id: `kpp_single:distance_reach`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... *(reason incomplete)* [details](#why-kpp_single-distance_reach-keyplayer) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-distance_reach-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> keyplayer 1.0.4 was run and its value differs from the reference value by convention (defaults and weights) on the fixtures real\_weights\_dir, real\_weights\_und, uniform\_weights. keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. The reference equals the definition oracle (exact shortest paths). Unresolved without reading the tool. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-14, rel 1e-12 (0 means exact equality). No value (kpp\_distance\_reach\_single) on inputs tagged edgeless: keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. No value (kpp\_distance\_reach\_single\_in) on inputs tagged edgeless: keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. 3 comparisons differ and 38 agree. Finding F012 (defect): Weighted distances (binary = FALSE) are not shortest-path lengths. Findings: [F012](../../findings.html#f012). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_reach_single` | keyplayer | any | no-value-on-some-inputs | (no value) edgeless | defaults | abs 1e-14, rel 1e-12 | `(1 + (n - 1) * keyplayer::mreach.closeness(adjacency, v, M = Inf, binary = TRUE, cmode = 'outdegree')) / n; keyplayer divides the sum of 1/d by n - 1, Borgatti's DR by n` | keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. |
| `kpp_distance_reach_single_in` | keyplayer | directed | no-value-on-some-inputs | (no value) edgeless | defaults | abs 1e-14, rel 1e-12 | `as kpp_distance_reach_single with cmode = 'indegree'` | keyplayer returns -1 for a network without edges (and for one node), where Borgatti's measures are defined. |
| `kpp_distance_reach_single_weighted` | keyplayer | any | differs | (no value) edgeless | defaults, weights | abs 1e-14, rel 1e-12 | `as kpp_distance_reach_single on the weighted adjacency matrix with binary = FALSE (edge values read as distances)` | keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the value from igraph Dijkstra distances with edge values as lengths, and its weighted fragmentation 3 to 14 percent above. the reference equals the definition oracle (exact shortest paths). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F012](../../findings.html#f012) | keyplayer | defect | Weighted distances (binary = FALSE) are not shortest-path lengths |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_single / fragmentation {#kpp_single-fragmentation}

Measure id: `kpp_single:fragmentation`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-kpp_single-fragmentation-ucinet) | `Key player / group centrality; exhaustivekp` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_single-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Kpp\_single / m\_reach {#kpp_single-m_reach}

Measure id: `kpp_single:m_reach`. Original family: Centrality.

**Definition.** Key player criterion (fragmentation, distance-weighted fragmentation, m-reach or distance-weighted reach) of a given set of nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_m_reach_single` | keyplayer | any | agrees |  |  | abs 0, rel 0 | `keyplayer::mreach.degree(adjacency, v, M = 2, binary = TRUE, cmode = 'outdegree')` |  |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)
{% endraw %}
