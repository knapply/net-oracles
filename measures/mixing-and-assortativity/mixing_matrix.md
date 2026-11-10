---
title: "Mixing matrices"
layout: default
parent: "Mixing and assortativity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Mixing matrices {#concept-top}

Family: [Mixing and assortativity](index.html). Subfamily: Mixing matrices. Concept id: `mixing_matrix`. 3 measures.

## Definition {#concept-definition}

Mixing matrices. Entries grouped here: Attribute mixing matrix; Degree mixing matrix; Mixing.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Attribute mixing matrix](#cat_attribute_matrix_mixing) | `cat_attribute_matrix_mixing` | 1 |
| [Degree mixing matrix](#cat_degree_matrix_mixing) | `cat_degree_matrix_mixing` | 1 |
| [Mixing](#mixing) | `mixing` | 2 |

## Attribute mixing matrix {#cat_attribute_matrix_mixing}

Measure id: `cat_attribute_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Attribute mixing matrix.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `attribute_mixing_matrix` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degree mixing matrix {#cat_degree_matrix_mixing}

Measure id: `cat_degree_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Degree mixing matrix.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `degree_mixing_matrix` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mixing {#mixing}

Measure id: `mixing`. Original family: Mixing and assortativity.

**Definition.** Mixing.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `attribute_mixing_dict; degree_mixing_dict` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `mixing_attribute` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.attribute_mixing_dict(G, 'label')` |  |
| `mixing_attribute_subset` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.attribute_mixing_dict(G, 'label', nodes = even nodes)` |  |
| `mixing_degree` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G)` |  |
| `mixing_degree_in_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G, x = 'in', y = 'out')` |  |
| `mixing_degree_subset` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G, nodes = even nodes)` |  |
| `mixing_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.degree_mixing_dict(G, weight = 'weight')` |  |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
