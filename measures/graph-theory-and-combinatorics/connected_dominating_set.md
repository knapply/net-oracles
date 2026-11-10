---
title: "Connected dominating set"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Connected dominating set {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `connected_dominating_set`. 1 measure.

## Definition {#concept-definition}

Connected dominating set. Entries grouped here: Cds.

## Cds {#st_cds}

Measure id: `st_cds`. Original family: Graph theory and combinatorics.

**Definition.** Cds.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_cds` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `sorted(nx.connected_dominating_set(G_sorted)) (-1 if disconnected)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
