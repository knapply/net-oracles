---
title: "All minimum s-t cuts"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# All minimum s-t cuts {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `st_min_cuts`. 1 measure.

## Definition {#concept-definition}

All minimum s-t cuts. Entries grouped here: St Mincuts.

## St Mincuts {#cat_mincuts_st}

Measure id: `cat_mincuts_st`. Original family: Components and connectivity.

**Definition.** St Mincuts.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_mincuts_st-igraph) | `stMincuts` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_mincuts_st-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: stMincuts.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
