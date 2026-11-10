---
title: "Stress centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Stress centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Betweenness, load and flow. Concept id: `stress_centrality`. 2 measures.

## Definition {#concept-definition}

Stress centrality. Entries grouped here: Stresscent; Subgraph centrality and stress centrality.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Stresscent](#cat_stresscent) | `cat_stresscent` | 1 |
| [Subgraph centrality and stress centrality](#subgraph_stress_centrality) | `subgraph_stress_centrality` | 1 |

## Stresscent {#cat_stresscent}

Measure id: `cat_stresscent`. Original family: Layout.

**Definition.** Stresscent.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [sna](../../tools/sna.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_stresscent-sna) | `stresscent` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_stresscent-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. sna 2.8 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package sna: exported functions and help titles); API names: stresscent.

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)

## Subgraph centrality and stress centrality {#subgraph_stress_centrality}

Measure id: `subgraph_stress_centrality`. Original family: Centrality.

**Definition.** Subgraph centrality and stress centrality.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's documentation; no comparison set up for this measure yet. [details](#why-subgraph_stress_centrality-networkx) |  | documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-subgraph_stress_centrality-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's documentation (networkx public API (algorithms, generators, linalg, readwrite)).

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
