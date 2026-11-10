---
title: "Edge cover"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Edge cover {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `edge_cover`. 2 measures.

## Definition {#concept-definition}

Edge cover. Entries grouped here: Edge cover; St edge cover.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Edge cover](#edge_cover) | `edge_cover` | 1 |
| [St edge cover](#st_edge_cover) | `st_edge_cover` | 1 |

## Edge cover {#edge_cover}

Measure id: `edge_cover`. Original family: Graph theory and combinatorics.

**Definition.** Edge cover.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-edge_cover-networkx) | `is_cover; is_edge_cover; min_edge_cover` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-edge_cover-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_cover; is\_edge\_cover; min\_edge\_cover.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St edge cover {#st_edge_cover}

Measure id: `st_edge_cover`. Original family: Graph theory and combinatorics.

**Definition.** St edge cover.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_edge_cover` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.min_edge_cover(G)) counting each edge once, -1 with an isolated node` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
