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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_attribute_matrix_mixing-networkx) | `attribute_mixing_matrix` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_attribute_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: attribute\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Degree mixing matrix {#cat_degree_matrix_mixing}

Measure id: `cat_degree_matrix_mixing`. Original family: Mixing and assortativity.

**Definition.** Degree mixing matrix.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_degree_matrix_mixing-networkx) | `degree_mixing_matrix` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_matrix_mixing-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: degree\_mixing\_matrix.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Mixing {#mixing}

Measure id: `mixing`. Original family: Mixing and assortativity.

**Definition.** Mixing.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `attribute_mixing_dict; degree_mixing_dict` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-mixing-ucinet) | `Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)` | published documentation |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-mixing-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

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
