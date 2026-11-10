---
title: "Gomory-Hu and equivalent-flow trees"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Gomory-Hu and equivalent-flow trees {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Flows and flow trees. Concept id: `gomory_hu_tree`. 3 measures.

## Definition {#concept-definition}

The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Gomory hu](#gomory_hu) | `gomory_hu` | 3 |
| [Gomory hu values](#gomory_hu_values) | `gomory_hu_values` | 1 |
| [Gusfield Equivalent Flow Tree](#cat_equivalent_flow_gusfield_tree) | `cat_equivalent_flow_gusfield_tree` | 1 |

## References {#concept-references}

[gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gomory hu {#gomory_hu}

Measure id: `gomory_hu`. Original family: Components and connectivity.

**Definition.** The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `gomory_hu_tree` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gomory_hu-pyigraph) | `gomory_hu_tree` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-gomory_hu-jgrapht) | `GusfieldGomoryHuCutTree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gomory_hu-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: gomory\_hu\_tree.
- <a id="why-gomory_hu-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GusfieldGomoryHuCutTree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_gomory_hu_tree` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.gomory_hu_tree(G, capacity = 'capacity').edges(data = 'weight'), as (u, v, weight) with u < v` |  |

**References:** [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht)

## Gomory hu values {#gomory_hu_values}

Measure id: `gomory_hu_values`. Original family: Components and connectivity.

**Definition.** The Gomory-Hu tree of an undirected network: each node's parent and the minimum cut value to it (Gusfield).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_gomory_hu_values` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.minimum_cut_value(G, u, v) for every pair u < v` |  |

**References:** [gomory1961multi](../../references.html#gomory1961multi), [gusfield1990very](../../references.html#gusfield1990very), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Gusfield Equivalent Flow Tree {#cat_equivalent_flow_gusfield_tree}

Measure id: `cat_equivalent_flow_gusfield_tree`. Original family: Components and connectivity.

**Definition.** Gusfield Equivalent Flow Tree.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_equivalent_flow_gusfield_tree-jgrapht) | `GusfieldEquivalentFlowTree` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_equivalent_flow_gusfield_tree-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: GusfieldEquivalentFlowTree.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
