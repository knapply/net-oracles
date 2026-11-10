---
title: "K-edge subgraphs"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-edge subgraphs {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_edge_subgraphs`. 1 measure.

## Definition {#concept-definition}

K-edge subgraphs. Entries grouped here: K edge subgraphs.

## K edge subgraphs {#gb_k_edge_subgraphs}

Measure id: `gb_k_edge_subgraphs`. Original family: Traversal, trees and DAGs.

**Definition.** K edge subgraphs.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `k_edge_subgraphs` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_k_edge_subgraphs` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `nx.k_edge_subgraphs(G, 2)` | NetworkX's k\_edge\_subgraphs rejects multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
