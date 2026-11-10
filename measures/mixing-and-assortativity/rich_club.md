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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `rich_club_coefficient` |  |
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu` | API listing |

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

| Tool | State | API names | Source |
|---|---|---|---|
| [tnet](../../tools/tnet.html) | · reported in docs | `weighted_richclub_tm; weighted_richclub_w` | API listing |

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)

## Weighted richclub local {#cat_local_richclub_weighted}

Measure id: `cat_local_richclub_weighted`. Original family: Graph theory and combinatorics.

**Definition.** Weighted richclub local.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [tnet](../../tools/tnet.html) | · reported in docs | `weighted_richclub_local_w` | API listing |

**Tools cited:** [opsahl2010node](../../references.html#opsahl2010node)
{% endraw %}
