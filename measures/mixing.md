---
title: "Mixing"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Mixing

Family: Mixing and assortativity. Identifier: `mixing`.

## Definition

Mixing.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `attribute_mixing_dict; degree_mixing_dict` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Homophily: categorical (categonethomophily), continuous attributes (own FAQ), PropSame (6.793), mixing matrices / tables (6.813, 6.837)` | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `mixing_attribute` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.attribute_mixing_dict(G, 'label')` |  |
| `mixing_attribute_subset` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.attribute_mixing_dict(G, 'label', nodes = even nodes)` |  |
| `mixing_degree` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G)` |  |
| `mixing_degree_in_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G, x = 'in', y = 'out')` |  |
| `mixing_degree_subset` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.degree_mixing_dict(G, nodes = even nodes)` |  |
| `mixing_degree_weighted` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `nx.degree_mixing_dict(G, weight = 'weight')` |  |

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
