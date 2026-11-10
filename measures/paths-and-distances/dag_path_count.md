---
title: "Path counting in DAGs"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Path counting in DAGs {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Path enumeration and counting. Concept id: `dag_path_count`. 1 measure.

## Definition {#concept-definition}

Path counting in DAGs. Entries grouped here: Dag All Paths Counter.

## Dag All Paths Counter {#cat_all_counter_dag_path}

Measure id: `cat_all_counter_dag_path`. Original family: Communities.

**Definition.** Dag All Paths Counter.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_all_counter_dag_path-jgrapht) | `DagAllPathsCounter` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_all_counter_dag_path-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: DagAllPathsCounter.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
