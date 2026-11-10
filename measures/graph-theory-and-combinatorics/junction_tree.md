---
title: "Junction tree"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Junction tree {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `junction_tree`. 1 measure.

## Definition {#concept-definition}

Junction tree. Entries grouped here: Junction.

## Junction {#st_junction}

Measure id: `st_junction`. Original family: Graph theory and combinatorics.

**Definition.** Junction.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `junction_tree` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_junction` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.junction_tree(G): per node (0 clique / 1 sepset, members), then (-1, i, j) per edge, in NetworkX's order` |  |
| `st_junction_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the same checks on nx.junction_tree(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
