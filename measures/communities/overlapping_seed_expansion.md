---
title: "Overlapping seed expansion (LFM, GCE)"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Overlapping seed expansion (LFM, GCE) {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `overlapping_seed_expansion`. 4 measures.

## Definition {#concept-definition}

Overlapping seed expansion (LFM, GCE). Entries grouped here: GCE; Greedy source expansion (community); LFM; LFMLocal.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [GCE](#cat_gce) | `cat_gce` | 1 |
| [Greedy source expansion (community)](#cat_expansion_greedy_source-community) | `cat_expansion_greedy_source@community` | 1 |
| [LFM](#cat_lfm) | `cat_lfm` | 1 |
| [LFMLocal](#cat_lfm_local) | `cat_lfm_local` | 1 |

## GCE {#cat_gce}

Measure id: `cat_gce`. Original family: Graph theory and combinatorics.

**Definition.** GCE.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_gce-networkit) | `GCE` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gce-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: GCE.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Greedy source expansion (community) {#cat_expansion_greedy_source-community}

Measure id: `cat_expansion_greedy_source@community`. Original family: Graph theory and combinatorics.

**Definition.** Greedy source expansion (community).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_expansion_greedy_source-community-networkx) | `greedy_source_expansion` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_expansion_greedy_source-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: greedy\_source\_expansion.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## LFM {#cat_lfm}

Measure id: `cat_lfm`. Original family: Graph theory and combinatorics.

**Definition.** LFM.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_lfm-networkit) | `LFM` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_lfm-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LFM.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## LFMLocal {#cat_lfm_local}

Measure id: `cat_lfm_local`. Original family: Graph theory and combinatorics.

**Definition.** LFMLocal.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_lfm_local-networkit) | `LFMLocal` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_lfm_local-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: LFMLocal.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
