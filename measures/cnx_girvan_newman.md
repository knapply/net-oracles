---
title: "Cnx girvan newman"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Cnx girvan newman

Family: Communities. Identifier: `cnx_girvan_newman`.

## Definition

Cnx girvan newman.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_girvan_newman` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `itertools.islice(nx.community.girvan_newman(G), 3)` |  |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
