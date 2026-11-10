---
title: "DAG reachability"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# DAG reachability {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `dag_reachability`. 1 measure.

## Definition {#concept-definition}

DAG reachability. Entries grouped here: Dag reachability.

## Dag reachability {#nxs_dag_reachability}

Measure id: `nxs_dag_reachability`. Original family: Graph theory and combinatorics.

**Definition.** Dag reachability.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_dag_reachability` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `(u, v) for v in nx.descendants(DAG, u)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
