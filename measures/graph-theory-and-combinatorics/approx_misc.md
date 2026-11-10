---
title: "Approximation heuristics (annealing, random)"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Approximation heuristics (annealing, random) {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Independent sets and approximation. Concept id: `approx_misc`. 2 measures.

## Definition {#concept-definition}

Approximation heuristics (annealing, random). Entries grouped here: Nx anneal; Nx random.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Nx anneal](#ap_nx_anneal) | `ap_nx_anneal` | 1 |
| [Nx random](#ap_nx_random) | `ap_nx_random` | 2 |

## Nx anneal {#ap_nx_anneal}

Measure id: `ap_nx_anneal`. Original family: Graph theory and combinatorics.

**Definition.** Nx anneal.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_anneal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `simulated_annealing_tsp and threshold_accepting_tsp(K, 'greedy', move='1-1' and '1-0', seed=7), each tour with its length first; [-1] if disconnected or under three nodes` |  |
| `ap_nx_anneal_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's tours` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nx random {#ap_nx_random}

Measure id: `ap_nx_random`. Original family: Graph theory and combinatorics.

**Definition.** Nx random.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `random_graph` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `random_graph` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_nx_random` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `with seed=7: maximal_independent_set, average_clustering(trials=200) closed pairs, diameter (-1 if disconnected), randomized_partitioning and one_exchange (cut size, then the sorted cut)` |  |
| `ap_nx_random_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on NetworkX's results` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool)
{% endraw %}
