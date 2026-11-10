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

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_kl_connected` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is locally k edge connected (connectivity) {#cat_connected_edge_is_k_locally-connectivity}

Measure id: `cat_connected_edge_is_k_locally@connectivity`. Original family: Components and connectivity.

**Definition.** Is locally k edge connected (connectivity).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `is_locally_k_edge_connected` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
