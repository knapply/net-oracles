---
title: "Global and local efficiency"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Global and local efficiency {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Efficiency and reachability. Concept id: `global_efficiency`. 2 measures.

## Definition {#concept-definition}

Global and local efficiency. Entries grouped here: Global and local efficiency; Swan efficiency.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Global and local efficiency](#efficiency_global) | `efficiency_global` | 4 |
| [Swan efficiency](#cat_efficiency_swan) | `cat_efficiency_swan` | 1 |

## Global and local efficiency {#efficiency_global}

Measure id: `efficiency_global`. Original family: Paths and distances.

**Definition.** Global and local efficiency.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-efficiency_global-networkx) | `efficiency; global_efficiency; local_efficiency` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-efficiency_global-igraph) | `average_local_efficiency; global_efficiency; local_efficiency` | API listing |
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-efficiency_global-sna) | `efficiency` | API listing |
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-efficiency_global-bct) | `efficiency_bin; efficiency_wei` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-efficiency_global-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: efficiency; global\_efficiency; local\_efficiency.
- <a id="why-efficiency_global-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: average\_local\_efficiency; global\_efficiency; local\_efficiency.
- <a id="why-efficiency_global-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: efficiency.
- <a id="why-efficiency_global-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: efficiency\_bin; efficiency\_wei.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [rubinov2010complex](../../references.html#rubinov2010complex)

## Swan efficiency {#cat_efficiency_swan}

Measure id: `cat_efficiency_swan`. Original family: Descriptive statistics.

**Definition.** Swan efficiency.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [netrankr](../../tools/netrankr.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_efficiency_swan-netrankr) | `swan_efficiency` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_efficiency_swan-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: swan\_efficiency.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
