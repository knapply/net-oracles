---
title: "Eulerian circuits and paths"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Eulerian circuits and paths {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Eulerian paths, Hamiltonian paths and tours. Concept id: `eulerian`. 4 measures.

## Definition {#concept-definition}

Eulerian circuits and paths. Entries grouped here: Eulerian circuits and paths; Euler; Euler circuit; Is eulerian.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Eulerian circuits and paths](#eulerian) | `eulerian` | 1 |
| [Euler](#nxs_euler) | `nxs_euler` | 2 |
| [Euler circuit](#nxs_euler_circuit) | `nxs_euler_circuit` | 1 |
| [Is eulerian](#gb_is_eulerian) | `gb_is_eulerian` | 1 |

## Eulerian circuits and paths {#eulerian}

Measure id: `eulerian`. Original family: Traversal, trees and DAGs.

**Definition.** Eulerian circuits and paths.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `HierholzerEulerianCycle` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Euler {#nxs_euler}

Measure id: `nxs_euler`. Original family: Graph theory and combinatorics.

**Definition.** Euler.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `eulerian_circuit; eulerian_path; eulerize; has_eulerian_path; is_eulerian; is_semieulerian` | API listing |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `eulerian_cycle; eulerian_path; has_eulerian_cycle; has_eulerian_path` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Euler circuit {#nxs_euler_circuit}

Measure id: `nxs_euler_circuit`. Original family: Graph theory and combinatorics.

**Definition.** Euler circuit.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_euler_circuit` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `list(nx.eulerian_circuit(G, source = 0, keys = True))` | NetworkX refuses a graph that is not connected (or has no node) |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is eulerian {#gb_is_eulerian}

Measure id: `gb_is_eulerian`. Original family: Traversal, trees and DAGs.

**Definition.** Is eulerian.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_is_eulerian` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_eulerian(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
