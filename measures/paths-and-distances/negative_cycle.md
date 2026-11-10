---
title: "Negative cycle detection"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Negative cycle detection {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Shortest paths. Concept id: `negative_cycle`. 1 measure.

## Definition {#concept-definition}

Negative cycle detection. Entries grouped here: Paths negative cycle.

## Paths negative cycle {#paths_negative_cycle}

Measure id: `paths_negative_cycle`. Original family: Paths and distances.

**Definition.** Paths negative cycle.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `find_negative_cycle; negative_edge_cycle` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `find_negative_cycle; negative_edge_cycle` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_negative_cycle_potential` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.negative_edge_cycle(G, weight = 'len')` |  |
| `paths_negative_cycle_shift` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.negative_edge_cycle(G, weight = 'len')` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
