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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_cover; is_edge_cover; min_edge_cover` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## St edge cover {#st_edge_cover}

Measure id: `st_edge_cover`. Original family: Graph theory and combinatorics.

**Definition.** St edge cover.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_edge_cover` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `len(nx.min_edge_cover(G)) counting each edge once, -1 with an isolated node` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
