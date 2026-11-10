---
title: "Minimum and maximum cycle ratio"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum and maximum cycle ratio {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Path enumeration and counting. Concept id: `cycle_ratio`. 1 measure.

## Definition {#concept-definition}

Minimum and maximum cycle ratio. Entries grouped here: Minimum/maximum cycle ratio and mean cycle.

## Minimum/maximum cycle ratio and mean cycle {#cycle_ratio}

Measure id: `cycle_ratio`. Original family: Paths and distances.

**Definition.** Minimum/maximum cycle ratio and mean cycle.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cycle_ratio-jgrapht) | `HowardMinimumMeanCycle` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cycle_ratio-boost) | `howard_cycle_ratio; maximum_cycle_ratio; minimum_cycle_ratio` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cycle_ratio-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: HowardMinimumMeanCycle.
- <a id="why-cycle_ratio-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: howard\_cycle\_ratio; maximum\_cycle\_ratio; minimum\_cycle\_ratio.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
