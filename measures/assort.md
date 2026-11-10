---
title: "Assort"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Assort

Family: Mixing and assortativity. Identifier: `assort`.

## Definition

Assort.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `degree_pearson_correlation_coefficient` |  |
| [bctpy](../tools/bctpy.html) | ≠ checked, differs by convention |  |  |
| [netseg](../tools/netseg.html) | · reported in docs | `assort` | API listing |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `assort_attribute` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.attribute_assortativity_coefficient(G, 'label')` |  |
| `assort_attribute_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.attribute_assortativity_coefficient(G, 'label', nodes = even nodes)` |  |
| `assort_degree` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G)` |  |
| `assort_degree` | bctpy | any | differs | multi\_edges, (no value) directed | direction, multi\_edges | abs 1e-12, rel 1e-09 | `bct.assortativity_bin(A binary, flag = 0)` | BCT works on the binary matrix, so parallel edges collapse and degrees count distinct neighbours; NetworkX and the reference count every edge. assortativity\_bin(flag = 0) is the undirected coefficient; directed fixtures are left to the definition and NetworkX oracles. |
| `assort_degree_in_in` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, x = 'in', y = 'in')` |  |
| `assort_degree_out_out` | NetworkX | directed | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, x = 'out', y = 'out')` |  |
| `assort_degree_pearson` | NetworkX | any | agrees |  |  | abs 1e-14, rel 1e-12 | `nx.degree_pearson_correlation_coefficient(G)` |  |
| `assort_degree_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, nodes = even nodes)` |  |
| `assort_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-08 | `nx.degree_assortativity_coefficient(G, weight = 'weight')` |  |
| `assort_degree_weighted` | bctpy | any | no-value-on-some-inputs | (no value) directed | direction | abs 1e-12, rel 1e-09 | `bct.assortativity_wei(W summed, flag = 0)` | assortativity\_wei(flag = 0) is the undirected coefficient; directed fixtures are not passed to it. |
| `assort_numeric` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.numeric_assortativity_coefficient(G, 'value')` |  |
| `assort_numeric_subset` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-09 | `nx.numeric_assortativity_coefficient(G, 'value', nodes = even nodes)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring), [rubinov2010complex](../references.html#rubinov2010complex), [tool_netseg](../references.html#tool_netseg)
{% endraw %}
