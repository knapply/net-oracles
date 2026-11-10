---
title: "Approximate and b-matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Approximate and b-matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `approximate_matching`. 1 measure.

## Definition {#concept-definition}

Approximate and b-matching. Entries grouped here: Approximate and b-matching.

## Approximate and b-matching {#matching_approx}

Measure id: `matching_approx`. Original family: Graph theory and combinatorics.

**Definition.** Approximate and b-matching.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-matching_approx-networkit) | `BMatcher; BSuitorMatcher; DynamicBSuitorMatcher; PathGrowingMatcher; SuitorMatcher` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-matching_approx-jgrapht) | `PathGrowingWeightedMatching` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-matching_approx-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: BMatcher; BSuitorMatcher; DynamicBSuitorMatcher; PathGrowingMatcher; SuitorMatcher.
- <a id="why-matching_approx-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: PathGrowingWeightedMatching.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
