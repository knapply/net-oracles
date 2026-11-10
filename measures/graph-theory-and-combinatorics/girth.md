---
title: "Girth"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Girth {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `girth`. 1 measure.

## Definition {#concept-definition}

Girth. Entries grouped here: Girth.

## Girth {#girth}

Measure id: `girth`. Original family: Graph theory and combinatorics.

**Definition.** Girth.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `girth` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `girth` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `girth` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_girth` | NetworkX | any | differs | multi\_edges, (no value) directed | direction, multi\_edges | abs 0, rel 0 | `nx.girth(G); -2 for infinity` | Parallel edges form a cycle of length 2 in the reference value's multigraph; NetworkX's simple graph merges them. NetworkX's girth is not implemented for directed graphs. |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
