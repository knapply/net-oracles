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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `hamiltonian_path` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_hampath` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.tournament.hamiltonian_path(G) on the simple digraph` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Palmer Hamiltonian Cycle {#cat_cycle_hamiltonian_palmer}

Measure id: `cat_cycle_hamiltonian_palmer`. Original family: Traversal, trees and DAGs.

**Definition.** Palmer Hamiltonian Cycle.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_cycle_hamiltonian_palmer-jgrapht) | `PalmerHamiltonianCycle` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_cycle_hamiltonian_palmer-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: PalmerHamiltonianCycle.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
