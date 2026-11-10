---
title: "Temporal degree"
layout: default
parent: "Temporal and events"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Temporal degree {#concept-top}

Family: [Temporal and events](index.html). Subfamily: Temporal descriptives. Concept id: `temporal_degree`. 2 measures.

## Definition {#concept-definition}

Temporal degree. Entries grouped here: Dynamic Degree; T Degree.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dynamic Degree](#cat_degree_dynamic) | `cat_degree_dynamic` | 1 |
| [T Degree](#cat_degree_t) | `cat_degree_t` | 1 |

## Dynamic Degree {#cat_degree_dynamic}

Measure id: `cat_degree_dynamic`. Original family: Temporal and events.

**Definition.** Dynamic Degree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [Gephi toolkit](../../tools/gephi.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_dynamic-gephi) | `DynamicDegree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_dynamic-gephi"></a>**[Gephi toolkit](../../tools/gephi.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Gephi toolkit 0.11.3 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Gephi toolkit 0.11.3 javadoc (published class list of org.gephi.statistics.plugin)); API names: DynamicDegree.

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi)

## T Degree {#cat_degree_t}

Measure id: `cat_degree_t`. Original family: Graph theory and combinatorics.

**Definition.** T Degree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [tsna / networkDynamic](../../tools/tsna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_t-tsna) | `tDegree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_t-tsna"></a>**[tsna / networkDynamic](../../tools/tsna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. tsna / networkDynamic 0.3.6 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package tsna: exported functions and help titles); API names: tDegree.

**Tools cited:** [handcock2008statnet](../../references.html#handcock2008statnet)
{% endraw %}
