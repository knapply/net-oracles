---
title: "Chain decomposition"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Chain decomposition {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `chain_decomposition`. 2 measures.

## Definition {#concept-definition}

Chain decomposition. Entries grouped here: Chain count; Chain decomposition.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Chain count](#gb_chain_count) | `gb_chain_count` | 1 |
| [Chain decomposition](#cat_chain_decomposition) | `cat_chain_decomposition` | 1 |

## Chain count {#gb_chain_count}

Measure id: `gb_chain_count`. Original family: Traversal, trees and DAGs.

**Definition.** Chain count.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `chain_decomposition` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `gb_chain_count` | NetworkX | undirected | no-value-on-some-inputs | (no value) multi\_edges | multi\_edges | abs 0, rel 0 | `len(list(nx.chain_decomposition(M)))` | NetworkX's chain\_decomposition rejects multigraphs. |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Chain decomposition {#cat_chain_decomposition}

Measure id: `cat_chain_decomposition`. Original family: Roles and positions.

**Definition.** Chain decomposition.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `chain_decomposition` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
