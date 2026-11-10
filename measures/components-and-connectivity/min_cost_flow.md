---
title: "Minimum-cost flow"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum-cost flow {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `min_cost_flow`. 4 measures.

## Definition {#concept-definition}

A maximum flow of least cost between two nodes, with its value.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Ahuja Orlin Sharma Cyclic Exchange Local Augmentation](#cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma) | `cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma` | 1 |
| [Capacity Scaling Minimum Cost Flow](#cat_capacity_cost_flow_minimum_scaling) | `cat_capacity_cost_flow_minimum_scaling` | 1 |
| [Max flow min cost](#max_flow_min_cost) | `max_flow_min_cost` | 2 |
| [Mincost](#gb_mincost) | `gb_mincost` | 1 |

## References {#concept-references}

[ahuja1993network](../../references.html#ahuja1993network), [cunningham1976network](../../references.html#cunningham1976network), [dantzig1951application](../../references.html#dantzig1951application), [grigoriadis1986efficient](../../references.html#grigoriadis1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ahuja Orlin Sharma Cyclic Exchange Local Augmentation {#cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma}

Measure id: `cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma`. Original family: Graph theory and combinatorics.

**Definition.** Ahuja Orlin Sharma Cyclic Exchange Local Augmentation.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `AhujaOrlinSharmaCyclicExchangeLocalAugmentation` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Capacity Scaling Minimum Cost Flow {#cat_capacity_cost_flow_minimum_scaling}

Measure id: `cat_capacity_cost_flow_minimum_scaling`. Original family: Components and connectivity.

**Definition.** Capacity Scaling Minimum Cost Flow.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `CapacityScalingMinimumCostFlow` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Max flow min cost {#max_flow_min_cost}

Measure id: `max_flow_min_cost`. Original family: Components and connectivity.

**Definition.** A maximum flow of least cost between two nodes, with its value.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `cost_of_flow; max_flow_min_cost; min_cost_flow; min_cost_flow_cost; network_simplex` |  |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `cycle_canceling; successive_shortest_path_nonnegative_weights` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_max_flow_min_cost` | NetworkX | directed | no-value-on-some-inputs |  | weights | abs 1e-09, rel 1e-09 | `F = nx.maximum_flow_value(G, 0, n - 1); nx.min_cost_flow_cost(M) on the multigraph M with demand -F at 0 and F at n - 1` | NetworkX's network simplex reports this real-valued problem infeasible (NetworkXUnfeasible): its documentation warns that it may fail on floating-point capacities and suggests integers. The linear program of the definition oracle confirms the reference value's value and cost. |

**References:** [ahuja1993network](../../references.html#ahuja1993network), [cunningham1976network](../../references.html#cunningham1976network), [dantzig1951application](../../references.html#dantzig1951application), [grigoriadis1986efficient](../../references.html#grigoriadis1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost)

## Mincost {#gb_mincost}

Measure id: `gb_mincost`. Original family: Traversal, trees and DAGs.

**Definition.** Mincost.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mincost` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.network_simplex(M) with demand -1 at 0 and 1 at n - 1` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
