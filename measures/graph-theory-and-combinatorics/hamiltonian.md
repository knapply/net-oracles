---
title: "Hamiltonian paths and cycles"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Hamiltonian paths and cycles {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Eulerian paths, Hamiltonian paths and tours. Concept id: `hamiltonian`. 2 measures.

## Definition {#concept-definition}

Hamiltonian paths and cycles. Entries grouped here: Hampath; Palmer Hamiltonian Cycle.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Hampath](#st_hampath) | `st_hampath` | 1 |
| [Palmer Hamiltonian Cycle](#cat_cycle_hamiltonian_palmer) | `cat_cycle_hamiltonian_palmer` | 1 |

## Hampath {#st_hampath}

Measure id: `st_hampath`. Original family: Graph theory and combinatorics.

**Definition.** Hampath.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `hamiltonian_path` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_hampath` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.tournament.hamiltonian_path(G) on the simple digraph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Palmer Hamiltonian Cycle {#cat_cycle_hamiltonian_palmer}

Measure id: `cat_cycle_hamiltonian_palmer`. Original family: Traversal, trees and DAGs.

**Definition.** Palmer Hamiltonian Cycle.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `PalmerHamiltonianCycle` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
