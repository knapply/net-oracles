---
title: "Greedy routing and navigation"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Greedy routing and navigation {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Distance summaries. Concept id: `greedy_routing`. 3 measures.

## Definition {#concept-definition}

Greedy routing and navigation. Entries grouped here: Hyperbolic greedy routing; Hyperbolic greedy success rate; Navigation.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Hyperbolic greedy routing](#cat_greedy_hyperbolic_routing) | `cat_greedy_hyperbolic_routing` | 1 |
| [Hyperbolic greedy success rate](#cat_greedy_hyperbolic_rate_success) | `cat_greedy_hyperbolic_rate_success` | 1 |
| [Navigation](#cat_navigation) | `cat_navigation` | 1 |

## Hyperbolic greedy routing {#cat_greedy_hyperbolic_routing}

Measure id: `cat_greedy_hyperbolic_routing`. Original family: Generators and rewiring.

**Definition.** Hyperbolic greedy routing.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_greedy_hyperbolic_routing-rustworkx) | `hyperbolic_greedy_routing` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_hyperbolic_routing-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: hyperbolic\_greedy\_routing.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Hyperbolic greedy success rate {#cat_greedy_hyperbolic_rate_success}

Measure id: `cat_greedy_hyperbolic_rate_success`. Original family: Generators and rewiring.

**Definition.** Hyperbolic greedy success rate.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_greedy_hyperbolic_rate_success-rustworkx) | `hyperbolic_greedy_success_rate` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_greedy_hyperbolic_rate_success-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: hyperbolic\_greedy\_success\_rate.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Navigation {#cat_navigation}

Measure id: `cat_navigation`. Original family: Graph theory and combinatorics.

**Definition.** Navigation.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_navigation-bct) | `navigation_wu` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_navigation-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: navigation\_wu.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)
{% endraw %}
