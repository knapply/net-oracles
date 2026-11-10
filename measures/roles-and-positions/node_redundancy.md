---
title: "Node redundancy"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Node redundancy {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `node_redundancy`. 1 measure.

## Definition {#concept-definition}

Node redundancy. Entries grouped here: Node redundancy.

## Node redundancy {#node_redundancy}

Measure id: `node_redundancy`. Original family: Two-mode and bipartite.

**Definition.** Node redundancy.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `node_redundancy` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `node_redundancy` | NetworkX | any | agrees |  |  | abs 0, rel 1e-14 | `nx.bipartite.node_redundancy(G, nodes with at least two neighbours)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
