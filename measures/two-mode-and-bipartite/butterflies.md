---
title: "Butterflies"
layout: default
parent: "Two-mode and bipartite"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Butterflies {#concept-top}

Family: [Two-mode and bipartite](index.html). Subfamily: Bipartite structure. Concept id: `butterflies`. 1 measure.

## Definition {#concept-definition}

Butterflies (4-cycles) at each node, counted over wedges of the lower-ranked endpoint.

## References {#concept-references}

[barber2007modularity](../../references.html#barber2007modularity), [estrada2005spectral](../../references.html#estrada2005spectral), [hagberg2008exploring](../../references.html#hagberg2008exploring), [he2017birank](../../references.html#he2017birank), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [lakhal1998polynomial](../../references.html#lakhal1998polynomial), [latapy2008basic](../../references.html#latapy2008basic)

## Butterflies {#butterflies}

Measure id: `butterflies`. Original family: Two-mode and bipartite.

**Definition.** Butterflies (4-cycles) at each node, counted over wedges of the lower-ranked endpoint.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `butterflies` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `butterflies` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.butterflies(G)` |  |

**References:** [barber2007modularity](../../references.html#barber2007modularity), [estrada2005spectral](../../references.html#estrada2005spectral), [hagberg2008exploring](../../references.html#hagberg2008exploring), [he2017birank](../../references.html#he2017birank), [hopcroft1973algorithm](../../references.html#hopcroft1973algorithm), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [lakhal1998polynomial](../../references.html#lakhal1998polynomial), [latapy2008basic](../../references.html#latapy2008basic)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
