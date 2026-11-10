---
title: "Seeded labels"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Seeded labels

Family: Communities. Identifier: `cnx_seeded_labels`.

## Definition

Seeded labels.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_seeded_labels` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under asyn_lpa_communities and fast_label_propagation_communities (simple graph), and asyn_fluidc(k = min(3, n)) on the simple undirected graph (-1 if not connected), each with seed=random.Random(7)` |  |
| `nx_seeded_labels_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
