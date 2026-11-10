---
title: "Matching and perfect-matching tests"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Matching and perfect-matching tests {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Matching. Concept id: `matching_tests`. 1 measure.

## Definition {#concept-definition}

Matching and perfect-matching tests. Entries grouped here: Check matching.

## Check matching {#check_matching}

Measure id: `check_matching`. Original family: Graph theory and combinatorics.

**Definition.** Check matching.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `is_matching; is_maximal_matching; is_perfect_matching` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `is_matching; is_max_matching` | API listing |
| [NetworKit](../../tools/networkit.html) | · reported in docs | `Matching` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `is_matching; is_maximal_matching` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `matching_check_candidate` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_matching, nx.is_maximal_matching, nx.is_perfect_matching of the candidate pairs` |  |
| `matching_check_maximal` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `the tests on nx.maximal_matching(G)` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
