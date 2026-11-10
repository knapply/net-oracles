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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-eulerian-jgrapht) | `HierholzerEulerianCycle` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-eulerian-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: HierholzerEulerianCycle.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Euler {#nxs_euler}

Measure id: `nxs_euler`. Original family: Graph theory and combinatorics.

**Definition.** Euler.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_euler-networkx) | `eulerian_circuit; eulerian_path; eulerize; has_eulerian_path; is_eulerian; is_semieulerian` | API listing |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_euler-igraph) | `eulerian_cycle; eulerian_path; has_eulerian_cycle; has_eulerian_path` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_euler-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: eulerian\_circuit; eulerian\_path; eulerize; has\_eulerian\_path; is\_eulerian; is\_semieulerian.
- <a id="why-nxs_euler-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: eulerian\_cycle; eulerian\_path; has\_eulerian\_cycle; has\_eulerian\_path.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Euler circuit {#nxs_euler_circuit}

Measure id: `nxs_euler_circuit`. Original family: Graph theory and combinatorics.

**Definition.** Euler circuit.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_euler_circuit` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `list(nx.eulerian_circuit(G, source = 0, keys = True))` | NetworkX refuses a graph that is not connected (or has no node) |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is eulerian {#gb_is_eulerian}

Measure id: `gb_is_eulerian`. Original family: Traversal, trees and DAGs.

**Definition.** Is eulerian.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_is_eulerian` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_eulerian(M)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
