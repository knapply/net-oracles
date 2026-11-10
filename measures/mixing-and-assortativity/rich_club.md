---
title: "Rich club"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Rich club {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Rich club. Concept id: `rich_club`. 3 measures.

## Definition {#concept-definition}

Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Rich club](#rich_club) | `rich_club` | 2 |
| [Weighted richclub](#cat_richclub_weighted) | `cat_richclub_weighted` | 1 |
| [Weighted richclub local](#cat_local_richclub_weighted) | `cat_local_richclub_weighted` | 1 |

## References {#concept-references}

[colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

## Rich club {#rich_club}

Measure id: `rich_club`. Original family: Generators and rewiring.

**Definition.** Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `rich_club_coefficient` |  |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-rich_club-bct) | `rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-rich_club-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: rich\_club\_bd; rich\_club\_bu; rich\_club\_wd; rich\_club\_wu.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rich_club` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.rich_club_coefficient(G, normalized = False); -1 where it raises (self-loops)` |  |
| `rich_club_normalized` | NetworkX | undirected | no-value-on-some-inputs |  | normalization | abs 0.02, rel 0.1 | `nx.rich_club_coefficient(G, normalized = True, Q = 20, n_samples = 200, seed = 7); -1 where it raises` | as for small\_world\_sigma (the normalization averages 200 rewired graphs) |

**References:** [colizza2006detecting](../../references.html#colizza2006detecting), [erdos2010simple](../../references.html#erdos2010simple), [hagberg2008exploring](../../references.html#hagberg2008exploring), [humphries2008network](../../references.html#humphries2008network), [maslov2002specificity](../../references.html#maslov2002specificity), [sporns2004small](../../references.html#sporns2004small), [telesford2011ubiquity](../../references.html#telesford2011ubiquity), [zhou2004rich](../../references.html#zhou2004rich)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Weighted richclub {#cat_richclub_weighted}

Measure id: `cat_richclub_weighted`. Original family: Graph theory and combinatorics.

**Definition.** Weighted richclub.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_richclub_weighted-tnet) | `weighted_richclub_tm; weighted_richclub_w` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_richclub_weighted-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: weighted\_richclub\_tm; weighted\_richclub\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Weighted richclub local {#cat_local_richclub_weighted}

Measure id: `cat_local_richclub_weighted`. Original family: Graph theory and combinatorics.

**Definition.** Weighted richclub local.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [tnet](../../tools/tnet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_local_richclub_weighted-tnet) | `weighted_richclub_local_w` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_local_richclub_weighted-tnet"></a>**[tnet](../../tools/tnet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tnet 3.0.16 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tnet: exported functions and help titles); API names: weighted\_richclub\_local\_w.

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
