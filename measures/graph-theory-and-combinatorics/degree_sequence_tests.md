---
title: "Graphical and bigraphical degree-sequence tests"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Graphical and bigraphical degree-sequence tests {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Degree sequences and predicates. Concept id: `degree_sequence_tests`. 4 measures.

## Definition {#concept-definition}

Graphical and bigraphical degree-sequence tests. Entries grouped here: Degree sequence test; Is bigraphical; Is degseq; Is graphical.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Degree sequence test](#nxs_degree_sequence_test) | `nxs_degree_sequence_test` | 1 |
| [Is bigraphical](#cat_bigraphical_is) | `cat_bigraphical_is` | 1 |
| [Is degseq](#cat_degseq_is) | `cat_degseq_is` | 1 |
| [Is graphical](#cat_graphical_is) | `cat_graphical_is` | 2 |

## Degree sequence test {#nxs_degree_sequence_test}

Measure id: `nxs_degree_sequence_test`. Original family: Graph theory and combinatorics.

**Definition.** Degree sequence test.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_digraphical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_digraphical(in_seq, out_seq)` |  |
| `nxs_graphical_eg` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_graphical(seq, method = 'eg')` |  |
| `nxs_graphical_hh` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_graphical(seq, method = 'hh')` |  |
| `nxs_multigraphical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_multigraphical(seq)` |  |
| `nxs_pseudographical` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_pseudographical(seq)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is bigraphical {#cat_bigraphical_is}

Measure id: `cat_bigraphical_is`. Original family: Graph theory and combinatorics.

**Definition.** Is bigraphical.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `is_bigraphical` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Is degseq {#cat_degseq_is}

Measure id: `cat_degseq_is`. Original family: Graph theory and combinatorics.

**Definition.** Is degseq.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_degseq` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)

## Is graphical {#cat_graphical_is}

Measure id: `cat_graphical_is`. Original family: Graph theory and combinatorics.

**Definition.** Is graphical.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_graphical` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `is_graphical` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph)
{% endraw %}
