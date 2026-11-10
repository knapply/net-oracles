---
title: "Leiden seeded"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Leiden seeded

Family: Communities. Identifier: `cnx_leiden_seeded`.

## Definition

Leiden seeded.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_leiden_seeded` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `per node: community index under nx.community.leiden_communities(simple graph, seed=random.Random(7)) with metric 'cpm' and 'modularity' (NetworkX 3.7); -1 without edges` |  |
| `nx_leiden_seeded_valid` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's communities` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
