---
title: "Degree sequence test"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Degree sequence test

Family: Graph theory and combinatorics. Identifier: `nxs_degree_sequence_test`.

## Definition

Degree sequence test.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_digraphical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_digraphical(in_seq, out_seq)` |  |
| `nxs_graphical_eg` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_graphical(seq, method = 'eg')` |  |
| `nxs_graphical_hh` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_graphical(seq, method = 'hh')` |  |
| `nxs_multigraphical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_multigraphical(seq)` |  |
| `nxs_pseudographical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_pseudographical(seq)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
