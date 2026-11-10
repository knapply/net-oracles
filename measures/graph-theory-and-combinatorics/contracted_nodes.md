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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `contracted_edge; contracted_nodes; quotient_graph` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_contracted_nodes-igraph) | `contract` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_contracted_nodes-pyigraph) | `contract_vertices` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_contracted_nodes-rustworkx) | `local_complement` | API listing |
| [keyplayer](../../tools/keyplayer.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-nxs_contracted_nodes-keyplayer) | `contract` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_contracted_nodes-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: contract.
- <a id="why-nxs_contracted_nodes-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: contract\_vertices.
- <a id="why-nxs_contracted_nodes-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: local\_complement.
- <a id="why-nxs_contracted_nodes-keyplayer"></a>**[keyplayer](../../tools/keyplayer.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. keyplayer 1.0.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package keyplayer: exported functions and help titles); API names: contract.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nxs_contracted_loops_order` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.contracted_nodes(G, 0, n - 1, self_loops = True).edges()), in its order` |  |
| `nxs_contracted_loops_set` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.contracted_nodes(G, 0, n - 1, self_loops = True)` |  |
| `nxs_contracted_noloops_order` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.contracted_nodes(G, 0, n - 1, self_loops = False).edges()), in its order` |  |
| `nxs_contracted_noloops_set` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted edges of nx.contracted_nodes(G, 0, n - 1, self_loops = False)` |  |

**Tools cited:** [an2016keyplayer](../../references.html#an2016keyplayer), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
