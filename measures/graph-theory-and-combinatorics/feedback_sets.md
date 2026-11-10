---
title: "Feedback arc and vertex sets"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Feedback arc and vertex sets {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `feedback_sets`. 2 measures.

## Definition {#concept-definition}

Feedback arc and vertex sets. Entries grouped here: Feedback arc and vertex sets; Break cycles.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Feedback arc and vertex sets](#feedback_sets) | `feedback_sets` | 2 |
| [Break cycles](#cat_break_cycle) | `cat_break_cycle` | 1 |

## Feedback arc and vertex sets {#feedback_sets}

Measure id: `feedback_sets`. Original family: Graph theory and combinatorics.

**Definition.** Feedback arc and vertex sets.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-feedback_sets-igraph) | `feedback_arc_set; feedback_vertex_set` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-feedback_sets-pyigraph) | `feedback_arc_set; feedback_vertex_set` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-feedback_sets-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: feedback\_arc\_set; feedback\_vertex\_set.
- <a id="why-feedback_sets-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: feedback\_arc\_set; feedback\_vertex\_set.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Break cycles {#cat_break_cycle}

Measure id: `cat_break_cycle`. Original family: Graph theory and combinatorics.

**Definition.** Break cycles.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [scikit-network](../../tools/sknetwork.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_break_cycle-sknetwork) | `break_cycles` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_break_cycle-sknetwork"></a>**[scikit-network](../../tools/sknetwork.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. scikit-network 0.33.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (scikit-network public classes and functions); API names: break\_cycles.

**Tools cited:** [tool_sknetwork](../../references.html#tool_sknetwork)
{% endraw %}
