---
title: "Local bridges"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Local bridges {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `local_bridges`. 1 measure.

## Definition {#concept-definition}

Local bridges. Entries grouped here: Local bridges.

## Local bridges {#local_bridges}

Measure id: `local_bridges`. Original family: Components and connectivity.

**Definition.** Local bridges.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `conn_local_bridges` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.local_bridges(G, with_span = True), mapped to the fixture's edges` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
