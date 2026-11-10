---
title: "Trophic levels and incoherence"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Trophic levels and incoherence {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `trophic_levels`. 1 measure.

## Definition {#concept-definition}

Trophic incoherence parameter of a directed network: the standard deviation of the trophic differences (Johnson et al.).

## References {#concept-references}

[johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

## Trophic {#cx_trophic}

Measure id: `cx_trophic`. Original family: Centrality.

**Definition.** Trophic incoherence parameter of a directed network: the standard deviation of the trophic differences (Johnson et al.).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `trophic_differences; trophic_incoherence_parameter; trophic_levels` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_trophic_differences` | NetworkX | directed | no-value-on-some-inputs | (no value) multi\_edges | direction, multi\_edges | abs 1e-12, rel 1e-09 | `nx.trophic_differences(G)[(u, v)] for every edge` | NetworkX's trophic\_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs. |
| `cx_trophic_incoherence` | NetworkX | directed | no-value-on-some-inputs | (no value) multi\_edges | direction, multi\_edges | abs 1e-12, rel 1e-09 | `nx.trophic_incoherence_parameter(G)` | NetworkX's trophic\_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs. |
| `cx_trophic_incoherence_cannibalism` | NetworkX | directed | no-value-on-some-inputs | (no value) multi\_edges | direction, multi\_edges | abs 1e-12, rel 1e-09 | `nx.trophic_incoherence_parameter(G, cannibalism = True)` | NetworkX's trophic\_differences unpacks MultiDiGraph edges as pairs and fails on multigraphs. |
| `cx_trophic_levels` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.trophic_levels(G) (an error is undefined)` |  |
| `cx_trophic_levels_weighted` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.trophic_levels(G, weight = 'weight')` |  |

**References:** [johnson2014trophic](../../references.html#johnson2014trophic), [levine1980several](../../references.html#levine1980several), [mones2012hierarchy](../../references.html#mones2012hierarchy), [tarjan1972depth](../../references.html#tarjan1972depth)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
