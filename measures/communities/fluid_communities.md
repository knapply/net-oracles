---
title: "Fluid communities"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Fluid communities {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `fluid_communities`. 1 measure.

## Definition {#concept-definition}

Fluid communities of a connected undirected network: k groups found by density-propagating sweeps.

## References {#concept-references}

[pares2018fluid](../../references.html#pares2018fluid)

## Fluid communities {#fluid_communities}

Measure id: `fluid_communities`. Original family: Communities.

**Definition.** Fluid communities of a connected undirected network: k groups found by density-propagating sweeps.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `asyn_fluidc` |  |
| [igraph (R)](../../tools/igraph.html) | ✓ checked, agrees | `cluster_fluid_communities` |  |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `community_fluid_communities` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fluid_quality` | NetworkX | undirected | differs | directed, undirected | direction, ties | abs 0.05, rel 0 | `mean over seeds of modularity(G, asyn_fluidc(simple graph, 3, seed = s))` | Fluid communities are randomized and the two procedures draw from different generators; the mean modularity over 20 seeds agrees on the corpus but not on every graph (0.505 against 0.560 on a 60-node tree). The comparison is statistical, not per run. |
| `fluid_quality` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case | defaults | abs 0.05, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_fluid_communities(simplify(g), 3))` | both tools reject disconnected networks (the reference reports -1); igraph also rejects the trivial ones |

**References:** [pares2018fluid](../../references.html#pares2018fluid)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
