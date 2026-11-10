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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges and self-loops): NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the... [details](#why-cycle_basis-networkx) | `cycle_basis` |  |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cycle_basis-rustworkx) | `cycle_basis` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cycle_basis-jgrapht) | `PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cycle_basis-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges and self-loops) on inputs tagged multi\_edges. NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.
- <a id="why-cycle_basis-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: cycle\_basis.
- <a id="why-cycle_basis-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis` | NetworkX | undirected | differs | multi\_edges | multi\_edges, self\_loops | abs 0, rel 0 | `nx.cycle_basis(G), cycle for cycle, in order` | NetworkX's simple graph merges parallel edges and repeated loops, whose cycles the reference lists after NetworkX's basis (the basis of the multigraph has m - n + c cycles). |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [tool_rustworkx](../../references.html#tool_rustworkx)

## Basis {#basis}

Measure id: `basis`. Original family: Graph theory and combinatorics.

**Definition.** Basis.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (multi-edges): as for cyc\_basis. [details](#why-basis-networkx) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-basis-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (multi-edges) on inputs tagged multi\_edges. as for cyc\_basis. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 0, rel 0 (0 means exact equality). 1 comparisons differ and 18 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_basis_check` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 0, rel 0 | `the count and the cycle/independence tests of nx.cycle_basis(G)` | as for cyc\_basis |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Nxs cycle basis {#nxs_cycle_basis}

Measure id: `nxs_cycle_basis`. Original family: Graph theory and combinatorics.

**Definition.** Nxs cycle basis.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_cycle_basis` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.cycle_basis(G) on the simple graph, in its order` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
