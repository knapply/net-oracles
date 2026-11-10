---
title: "Rich club"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Rich club

Family: Generators and rewiring. Identifier: `rich_club`.

## Definition

Rich-club coefficient of an undirected network for every degree, optionally normalized by degree-preserving randomizations.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `rich_club_coefficient` |  |
| [BCT (Octave)](../tools/bct.html) | · reported in docs | `rich_club_bd; rich_club_bu; rich_club_wd; rich_club_wu` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `rich_club` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.rich_club_coefficient(G, normalized = False); -1 where it raises (self-loops)` |  |
| `rich_club_normalized` | NetworkX | undirected | no-value-on-some-inputs |  | normalization | abs 0.02, rel 0.1 | `nx.rich_club_coefficient(G, normalized = True, Q = 20, n_samples = 200, seed = 7); -1 where it raises` | as for small\_world\_sigma (the normalization averages 200 rewired graphs) |

## References

[colizza2006detecting](../references.html#colizza2006detecting), [erdos2010simple](../references.html#erdos2010simple), [hagberg2008exploring](../references.html#hagberg2008exploring), [humphries2008network](../references.html#humphries2008network), [maslov2002specificity](../references.html#maslov2002specificity), [sporns2004small](../references.html#sporns2004small), [telesford2011ubiquity](../references.html#telesford2011ubiquity), [zhou2004rich](../references.html#zhou2004rich)

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex)
{% endraw %}
