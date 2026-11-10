---
title: "Could be iso"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Could be iso

Family: Graph theory and combinatorics. Identifier: `could_be_iso`.

## Definition

Could be iso.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `could_be_iso_d_perturbed` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'd')` |  |
| `could_be_iso_d_rev` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'd')` |  |
| `could_be_iso_dt_perturbed` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'dt')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dt_rev` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'dt')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dtc_perturbed` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, perturbed(G), properties = 'dtc')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |
| `could_be_iso_dtc_rev` | NetworkX | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `nx.could_be_isomorphic(G, rev(G), properties = 'dtc')` | NetworkX counts triangles and maximal cliques of undirected graphs only (it raises NetworkXNotImplemented) |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
