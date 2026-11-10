---
title: "Cycle basis"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Cycle basis {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `cycle_basis`. 3 measures.

## Definition {#concept-definition}

Cycle basis. Entries grouped here: Cycle basis; Basis; Nxs cycle basis.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Cycle basis](#cycle_basis) | `cycle_basis` | 3 |
| [Basis](#basis) | `basis` | 1 |
| [Nxs cycle basis](#nxs_cycle_basis) | `nxs_cycle_basis` | 1 |

## Cycle basis {#cycle_basis}

Measure id: `cycle_basis`. Original family: Graph theory and combinatorics.

**Definition.** Cycle basis.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention | `cycle_basis` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `cycle_basis` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis` | NetworkX | undirected | differs | multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.cycle_basis(G), cycle for cycle, in order` | NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)

## Basis {#basis}

Measure id: `basis`. Original family: Graph theory and combinatorics.

**Definition.** Basis.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis_check` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 0, rel 0 | `the count and the cycle/independence tests of nx.cycle_basis(G)` | as for cyc\_basis |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nxs cycle basis {#nxs_cycle_basis}

Measure id: `nxs_cycle_basis`. Original family: Graph theory and combinatorics.

**Definition.** Nxs cycle basis.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_cycle_basis` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.cycle_basis(G) on the simple graph, in its order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
