---
title: "MCMC annealing and equilibration"
layout: default
parent: "Statistical fitting"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# MCMC annealing and equilibration {#concept-top}

Family: [Statistical fitting](index.html). Subfamily: Model fitting. Concept id: `mcmc_anneal_equilibrate`. 2 measures.

## Definition {#concept-definition}

MCMC annealing and equilibration. Entries grouped here: Mcmc anneal; Mcmc equilibrate.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Mcmc anneal](#cat_anneal_mcmc) | `cat_anneal_mcmc` | 1 |
| [Mcmc equilibrate](#cat_equilibrate_mcmc) | `cat_equilibrate_mcmc` | 1 |

## Mcmc anneal {#cat_anneal_mcmc}

Measure id: `cat_anneal_mcmc`. Original family: Inference (QAP, null models).

**Definition.** Mcmc anneal.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_anneal_mcmc-graphtool) | `mcmc_anneal` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_anneal_mcmc-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: mcmc\_anneal.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Mcmc equilibrate {#cat_equilibrate_mcmc}

Measure id: `cat_equilibrate_mcmc`. Original family: Inference (QAP, null models).

**Definition.** Mcmc equilibrate.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_equilibrate_mcmc-graphtool) | `mcmc_equilibrate` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_equilibrate_mcmc-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: mcmc\_equilibrate.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
