---
title: "Random edge addition and removal"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random edge addition and removal {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Rewiring and randomization. Concept id: `random_edge_edit`. 2 measures.

## Definition {#concept-definition}

Random edge addition and removal. Entries grouped here: Random edge addition and removal; Random k lift.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Random edge addition and removal](#random_edge_edit) | `random_edge_edit` | 1 |
| [Random k lift](#cat_k_lift_random) | `cat_k_lift_random` | 1 |

## Random edge addition and removal {#random_edge_edit}

Measure id: `random_edge_edit`. Original family: Generators and rewiring.

**Definition.** Random edge addition and removal.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-random_edge_edit-graphtool) | `add_random_edges; remove_random_edges` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-random_edge_edit-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: add\_random\_edges; remove\_random\_edges.

**Tools cited:** [peixoto2014graphtool](../../references.html#peixoto2014graphtool)

## Random k lift {#cat_k_lift_random}

Measure id: `cat_k_lift_random`. Original family: Graph theory and combinatorics.

**Definition.** Random k lift.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_k_lift_random-networkx) | `random_k_lift` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_k_lift_random-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: random\_k\_lift.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
