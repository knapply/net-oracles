---
title: "Approximate node connectivity"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Approximate node connectivity {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Connectivity numbers. Concept id: `node_connectivity`. 1 measure.

## Definition {#concept-definition}

Approximate node connectivity of the whole network by greedy node-disjoint shortest paths.

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Node connectivity {#ap_node_connectivity}

Measure id: `ap_node_connectivity`. Original family: Graph theory and combinatorics.

**Definition.** Approximate node connectivity of the whole network by greedy node-disjoint shortest paths.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_node_connectivity` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.approximation.node_connectivity(G_sorted)` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F031](../../findings.html#f031) | NetworkX | defect | approximation.node\_connectivity starts from a bound that can exceed the connectivity |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
