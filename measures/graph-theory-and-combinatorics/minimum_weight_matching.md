---
title: "Minimum-weight matching"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Minimum-weight matching {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `minimum_weight_matching`. 2 measures.

## Definition {#concept-definition}

A matching of least total weight among the matchings of largest size, as input edge positions.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Min weight full matching](#min_weight_full_matching) | `min_weight_full_matching` | 1 |
| [Min weight matching](#min_weight_matching) | `min_weight_matching` | 1 |

## References {#concept-references}

[jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian), [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight full matching {#min_weight_full_matching}

Measure id: `min_weight_full_matching`. Original family: Two-mode and bipartite.

**Definition.** A full matching of least total cost of a bipartite graph, as each node's mate (-1 if unmatched).

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `minimum_weight_full_matching` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `min_weight_full_matching` | NetworkX | undirected | agrees |  |  | abs 1e-09, rel 1e-12 | `nx.bipartite.minimum_weight_full_matching(G, top, weight = c): (total cost, 1 if it covers the smaller side); -1 where it raises` |  |

**References:** [jonker1987shortest](../../references.html#jonker1987shortest), [kuhn1955hungarian](../../references.html#kuhn1955hungarian)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Min weight matching {#min_weight_matching}

Measure id: `min_weight_matching`. Original family: Graph theory and combinatorics.

**Definition.** A matching of least total weight among the matchings of largest size, as input edge positions.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `min_weight_matching` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_min_weight` | NetworkX | undirected | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.min_weight_matching(G, weight = 'weight')` |  |

**References:** [edmonds1965maximum](../../references.html#edmonds1965maximum), [edmonds1965paths](../../references.html#edmonds1965paths), [galil1986efficient](../../references.html#galil1986efficient), [hagberg2008exploring](../../references.html#hagberg2008exploring)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
