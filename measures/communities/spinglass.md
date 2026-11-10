---
title: "Spinglass"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Spinglass {#concept-top}

Family: [Communities](index.html). Subfamily: Modularity-based detection. Concept id: `spinglass`. 1 measure.

## Definition {#concept-definition}

Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

## References {#concept-references}

[reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

## Spinglass {#spinglass}

Measure id: `spinglass`. Original family: Communities.

**Definition.** Spinglass communities of a connected network by simulated annealing of a Potts Hamiltonian (Reichardt and Bornholdt).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cluster_spinglass` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-spinglass-pyigraph) | `community_spinglass` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-spinglass-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_spinglass.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `spinglass_quality` | igraph (R) | undirected | no-value-on-some-inputs | (no value) disconnected, (no value) edge\_case | defaults | abs 0.02, rel 0 | `mean over set.seed(1..10) of modularity(g, cluster_spinglass(g, weights = NA))` | both tools reject disconnected networks; igraph also rejects the trivial ones |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F038](../../findings.html#f038) | igraph (R) | convention | Spinglass reads the network as simple |

**References:** [reichardt2006statistical](../../references.html#reichardt2006statistical), [traag2009community](../../references.html#traag2009community)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
