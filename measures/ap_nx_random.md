---
title: "Nx random"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Nx random

Family: Graph theory and combinatorics. Identifier: `ap_nx_random`.

## Definition

Nx random.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `random_graph` |  |
| [graph-tool](../tools/graphtool.html) | · reported in docs | `random_graph` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_random` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `with seed=7: maximal_independent_set, average_clustering(trials=200) closed pairs, diameter (-1 if disconnected), randomized_partitioning and one_exchange (cut size, then the sorted cut)` |  |
| `ap_nx_random_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's results` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [peixoto2014graphtool](../references.html#peixoto2014graphtool)
{% endraw %}
