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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `asyn_fluidc` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cluster_fluid_communities` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-fluid_communities-pyigraph) | `community_fluid_communities` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-fluid_communities-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_fluid\_communities.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `fluid_quality` | NetworkX | undirected | differs | directed, undirected | direction, ties | abs 0.05, rel 0 | `mean over seeds of modularity(G, asyn_fluidc(simple graph, 3, seed = s))` | Fluid communities are randomized and the two procedures draw from different generators; the mean modularity over 20 seeds agrees on the corpus but not on every graph (0.505 against 0.560 on a 60-node tree). The comparison is statistical, not per run. |
| `fluid_quality` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case | defaults | abs 0.05, rel 0 | `mean over set.seed(1..20) of modularity(g, cluster_fluid_communities(simplify(g), 3))` | both tools reject disconnected networks (the reference reports -1); igraph also rejects the trivial ones |

**References:** [pares2018fluid](../../references.html#pares2018fluid)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
