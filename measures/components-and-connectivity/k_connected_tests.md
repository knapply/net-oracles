---
title: "K-connectivity tests"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# K-connectivity tests {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connected components. Concept id: `k_connected_tests`. 2 measures.

## Definition {#concept-definition}

K-connectivity tests. Entries grouped here: Is kl connected; Is locally k edge connected (connectivity).

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Is kl connected](#cat_connected_is_kl) | `cat_connected_is_kl` | 1 |
| [Is locally k edge connected (connectivity)](#cat_connected_edge_is_k_locally-connectivity) | `cat_connected_edge_is_k_locally@connectivity` | 1 |

## Is kl connected {#cat_connected_is_kl}

Measure id: `cat_connected_is_kl`. Original family: Components and connectivity.

**Definition.** Is kl connected.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_connected_is_kl-networkx) | `is_kl_connected` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_connected_is_kl-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_kl\_connected.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is locally k edge connected (connectivity) {#cat_connected_edge_is_k_locally-connectivity}

Measure id: `cat_connected_edge_is_k_locally@connectivity`. Original family: Components and connectivity.

**Definition.** Is locally k edge connected (connectivity).

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_connected_edge_is_k_locally-connectivity-networkx) | `is_locally_k_edge_connected` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_connected_edge_is_k_locally-connectivity-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_locally\_k\_edge\_connected.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
