---
title: "Node contraction"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Node contraction {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Spanners, contraction and reduction. Concept id: `contracted_nodes`. 1 measure.

## Definition {#concept-definition}

Node contraction. Entries grouped here: Contracted nodes.

## Contracted nodes {#nxs_contracted_nodes}

Measure id: `nxs_contracted_nodes`. Original family: Graph theory and combinatorics.

**Definition.** Contracted nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `contracted_edge; contracted_nodes; quotient_graph` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `contract` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `contract_vertices` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `local_complement` | API listing |
| [keyplayer](../../tools/keyplayer.html) | · reported in docs | `contract` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_contracted_loops_order` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.contracted_nodes(G, 0, n - 1, self_loops = True).edges()), in its order` |  |
| `nxs_contracted_loops_set` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.contracted_nodes(G, 0, n - 1, self_loops = True)` |  |
| `nxs_contracted_noloops_order` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.contracted_nodes(G, 0, n - 1, self_loops = False).edges()), in its order` |  |
| `nxs_contracted_noloops_set` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.contracted_nodes(G, 0, n - 1, self_loops = False)` |  |

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
