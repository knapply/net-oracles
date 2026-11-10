---
title: "Louvain seeded"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Louvain seeded

Family: Communities. Identifier: `cnx_louvain_seeded`.

## Definition

Louvain seeded.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_louvain_seeded` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under nx.community.louvain_communities(simple graph, seed=random.Random(7)); -1 for a graph without edges` |  |
| `nx_louvain_seeded_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
