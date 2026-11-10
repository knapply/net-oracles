---
title: "Prominent group"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Prominent group {#concept-top}

Family: [Centrality](index.html). Subfamily: Group centrality. Concept id: `group_prominence`. 1 measure.

## Definition {#concept-definition}

Prominent group. Entries grouped here: Prominent group.

## Prominent group {#nxo_prominent}

Measure id: `nxo_prominent`. Original family: Graph theory and combinatorics.

**Definition.** Prominent group.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `prominent_group` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxo_prominent_greedy` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.prominent_group(G, 3, greedy = True)` |  |
| `nxo_prominent_group` | NetworkX | any | differs | disconnected | defaults, direction | abs 0, rel 0 | `nx.prominent_group(G, 2), value then group` | the reference searches the value without endpoints; the definition oracle checks it. |
| `nxo_prominent_group_options` | NetworkX | any | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges, weights | abs 0, rel 0 | `nx.prominent_group(G, 3, weight = 'weight', endpoints = True, normalized = False)` | NetworkX takes the smallest weight of parallel edges; the reference reads the first (the backend leaves multigraphs to NetworkX). |
| `nxo_prominent_value` | NetworkX | any | differs | disconnected | defaults, direction | abs 0, rel 0 | `nx.prominent_group(G, 2)[0]` | the reference searches the value without endpoints; the definition oracle checks it. |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F002](../../findings.html#f002) | NetworkX | defect | prominent\_group misses the best group on disconnected graphs |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
