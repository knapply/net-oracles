---
title: "Minimum cycle basis"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum cycle basis {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `minimum_cycle_basis`. 3 measures.

## Definition {#concept-definition}

A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Mcb weight](#gb_mcb_weight) | `gb_mcb_weight` | 1 |
| [Min basis](#min_basis) | `min_basis` | 1 |
| [Min basis weights](#min_basis_weights) | `min_basis_weights` | 1 |

## References {#concept-references}

[depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

## Mcb weight {#gb_mcb_weight}

Measure id: `gb_mcb_weight`. Original family: Traversal, trees and DAGs.

**Definition.** Mcb weight.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_mcb_weight` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `total weight of nx.minimum_cycle_basis(G, weight)` | NetworkX's minimum\_cycle\_basis rejects multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min basis {#min_basis}

Measure id: `min_basis`. Original family: Graph theory and combinatorics.

**Definition.** A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_min_basis_check` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 0, rel 0 | `the count and the cycle/independence tests of nx.minimum_cycle_basis(G)` | as for cyc\_basis |

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min basis weights {#min_basis_weights}

Measure id: `min_basis_weights`. Original family: Graph theory and combinatorics.

**Definition.** A minimum cycle basis of an undirected network and the weight of each cycle (de Pina).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ≠ checked, differs by convention |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_min_basis_weights` | NetworkX | undirected | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `weights of the cycles of nx.minimum_cycle_basis(G)` | as for cyc\_basis |
| `cyc_min_basis_weights_weighted` | NetworkX | undirected | differs | multi\_edges | multi\_edges, self\_loops, weights | abs 1e-12, rel 1e-12 | `weights of the cycles of nx.minimum_cycle_basis(G, weight = 'weight')` | Two parallel edges form a cycle of their total weight for the reference and the definition (two parallel loops, two cycles); NetworkX's simple graph keeps one edge per pair and has no such cycle. |

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
