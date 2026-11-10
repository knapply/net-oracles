---
title: "Asteroidal triples and AT-free graphs"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Asteroidal triples and AT-free graphs {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Chordal, perfect and special graph classes. Concept id: `asteroidal_triples`. 2 measures.

## Definition {#concept-definition}

Asteroidal triples and AT-free graphs. Entries grouped here: Asteroidal; At free.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Asteroidal](#st_asteroidal) | `st_asteroidal` | 1 |
| [At free](#st_at_free) | `st_at_free` | 1 |

## Asteroidal {#st_asteroidal}

Measure id: `st_asteroidal`. Original family: Graph theory and combinatorics.

**Definition.** Asteroidal.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `find_asteroidal_triple` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_asteroidal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.find_asteroidal_triple(G): the triple, or [-1]` |  |
| `st_asteroidal_valid` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `1 if nx.find_asteroidal_triple(G) returns a triple, else -1` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## At free {#st_at_free}

Measure id: `st_at_free`. Original family: Graph theory and combinatorics.

**Definition.** At free.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `is_at_free` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_at_free` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.is_at_free(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
