---
title: "Key player set (KPP)"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Key player set (KPP) {#concept-top}

Family: [Centrality](index.html). Subfamily: Key players. Concept id: `key_player_set`. 5 measures.

## Definition {#concept-definition}

The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Kpp\_optimum / distance\_fragmentation](#kpp_optimum-distance_fragmentation) | `kpp_optimum:distance_fragmentation` | 1 |
| [Kpp\_optimum / distance\_reach](#kpp_optimum-distance_reach) | `kpp_optimum:distance_reach` | 1 |
| [Kpp\_optimum / fragmentation](#kpp_optimum-fragmentation) | `kpp_optimum:fragmentation` | 1 |
| [Kpp\_optimum / m\_reach](#kpp_optimum-m_reach) | `kpp_optimum:m_reach` | 1 |
| [Kpset](#cat_kpset) | `cat_kpset` | 1 |

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Kpp\_optimum / distance\_fragmentation {#kpp_optimum-distance_fragmentation}

Measure id: `kpp_optimum:distance_fragmentation`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_fragmentation_optimum_k2` | keyplayer | any | no-value-on-some-inputs | (no value) directed | direction | abs 1e-14, rel 1e-12 | `maximum over every pair S of keyplayer::fragment(adjacency, S, binary = TRUE)` | single\_node has fewer nodes than the set size, so there is no set to score; keyplayer's fragmentation is not directional, so it is compared on undirected networks only. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_optimum / distance\_reach {#kpp_optimum-distance_reach}

Measure id: `kpp_optimum:distance_reach`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_distance_reach_optimum_k2` | keyplayer | any | no-value-on-some-inputs |  |  | abs 1e-14, rel 1e-12 | `maximum over every pair S of (\|S\| + (n - \|S\|) kpcent(adjacency, S, 'mreach.closeness', M = Inf, method = 'min', binary = TRUE, cmode = 'outdegree')) / n` | no set of two nodes leaves anything to reach (single node), and keyplayer::kpcent fails on a two-node network. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpp\_optimum / fragmentation {#kpp_optimum-fragmentation}

Measure id: `kpp_optimum:fragmentation`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-kpp_optimum-fragmentation-ucinet) |  | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-kpp_optimum-fragmentation-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet)

## Kpp\_optimum / m\_reach {#kpp_optimum-m_reach}

Measure id: `kpp_optimum:m_reach`. Original family: Centrality.

**Definition.** The set of k key players that best satisfies a key player criterion (Borgatti's greedy swap search or exact enumeration), with its score.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `kpcent` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `kpp_m_reach_optimum_k3` | keyplayer | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `maximum over every set S of three nodes of keyplayer::kpcent(adjacency, S, 'mreach.degree', M = 1, method = 'min', binary = TRUE, cmode = 'outdegree')` | fewer nodes than the set size, so there is no set to score. |

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)

## Kpset {#cat_kpset}

Measure id: `cat_kpset`. Original family: Graph theory and combinatorics.

**Definition.** Kpset.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_kpset-keyplayer) | `kpset` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_kpset-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: kpset.

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer)
{% endraw %}
