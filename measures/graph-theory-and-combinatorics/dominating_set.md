---
title: "Dominating set"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dominating set {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `dominating_set`. 3 measures.

## Definition {#concept-definition}

Greedy dominating set of least node weight (weight per newly covered node), as node ids in the order chosen.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Dominating sets](#dominating_set) | `dominating_set` | 1 |
| [Ap dominating set](#ap_dominating_set) | `ap_dominating_set` | 1 |
| [Dominating](#st_dominating) | `st_dominating` | 1 |

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Dominating sets {#dominating_set}

Measure id: `dominating_set`. Original family: Graph theory and combinatorics.

**Definition.** Dominating sets.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `connected_dominating_set; dominating_set; is_connected_dominating_set; is_dominating_set; min_edge_dominating_set; min_weighted_dominating_set` | API listing |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ap dominating set {#ap_dominating_set}

Measure id: `ap_dominating_set`. Original family: Graph theory and combinatorics.

**Definition.** Greedy dominating set of least node weight (weight per newly covered node), as node ids in the order chosen.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_dominating_set` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.approximation.min_weighted_dominating_set(G_sorted, weight = 'w')) with w(v) = v mod 3` |  |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Dominating {#st_dominating}

Measure id: `st_dominating`. Original family: Graph theory and combinatorics.

**Definition.** Dominating.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_dominating` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `[nx.is_dominating_set(G, even nodes), nx.is_dominating_set(G, [0])]` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
