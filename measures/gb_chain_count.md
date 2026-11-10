---
title: "Chain count"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Chain count

Family: Traversal, trees and DAGs. Identifier: `gb_chain_count`.

## Definition

Chain count.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees | `chain_decomposition` |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_chain_count` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `len(list(nx.chain_decomposition(M)))` | NetworkX's chain\_decomposition rejects multigraphs. |

Tools cited: [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
