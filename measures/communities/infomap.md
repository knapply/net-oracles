---
title: "Infomap"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Infomap {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `infomap`. 1 measure.

## Definition {#concept-definition}

Infomap. Entries grouped here: Infomap.

## Infomap {#infomap}

Measure id: `infomap`. Original family: Communities.

**Definition.** Infomap.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `cluster_infomap` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-infomap-pyigraph) | `community_infomap` | API listing |
| [Infomap](../../tools/infomap.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-infomap-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: community\_infomap.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `infomap_native` | Infomap | undirected | no-value-on-some-inputs | (no value) loops | self\_loops | abs 1e-09, rel 1e-09 | `Infomap(two_level = True, directed = False, num_trials = 10, seed = 1) on the links without loops; its codelength` | Infomap leaves self-links out unless asked; the reference value's flow counts them |
| `infomap_native_weighted` | Infomap | undirected | no-value-on-some-inputs | (no value) loops | self\_loops | abs 1e-09, rel 1e-09 | `as infomap_native with link weights` | Infomap leaves self-links out unless asked; the reference value's flow counts them |
| `infomap_partition` | Infomap | any | agrees |  |  | abs 1e-09, rel 1e-09 | `map equation (definition oracle, tau = 0.15) of the partition Infomap(two_level = True, num_trials = 10, seed = 1) finds` |  |
| `infomap_partition_weighted` | Infomap | any | agrees |  |  | abs 1e-09, rel 1e-09 | `as infomap_partition with link weights` |  |
| `infomap_quality` | igraph (R) | undirected | differs | edge\_case | defaults, ties | abs 0.02, rel 0 | `mean over set.seed(1..5) of cluster_infomap(g, nb.trials = 10)$codelength` | a network without edges has no random walk; the reference reports -1 (undefined) where igraph may report a codelength of 0 |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [rosvall2008maps](../../references.html#rosvall2008maps)
{% endraw %}
