---
title: "Epidemic simulation (SIR, SEIR)"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Epidemic simulation (SIR, SEIR) {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Diffusion simulation. Concept id: `epidemic_simulation`. 2 measures.

## Definition {#concept-definition}

Epidemic simulation (SIR, SEIR). Entries grouped here: Epidemic Simulation SEIR; Sir.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Epidemic Simulation SEIR](#cat_epidemic_seir_simulation) | `cat_epidemic_seir_simulation` | 1 |
| [Sir](#cat_sir) | `cat_sir` | 1 |

## Epidemic Simulation SEIR {#cat_epidemic_seir_simulation}

Measure id: `cat_epidemic_seir_simulation`. Original family: Graph theory and combinatorics.

**Definition.** Epidemic Simulation SEIR.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_epidemic_seir_simulation-networkit) | `EpidemicSimulationSEIR` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_epidemic_seir_simulation-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: EpidemicSimulationSEIR.

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Sir {#cat_sir}

Measure id: `cat_sir`. Original family: Graph theory and combinatorics.

**Definition.** Sir.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_sir-igraph) | `sir` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_sir-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sir.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
