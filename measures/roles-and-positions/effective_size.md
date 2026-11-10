---
title: "Effective size"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Effective size {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `effective_size`. 1 measure.

## Definition {#concept-definition}

Effective size. Entries grouped here: Effective size.

## Effective size {#effective_size}

Measure id: `effective_size`. Original family: Roles and positions.

**Definition.** Effective size.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (self-loops, ties and weights): NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. [details](#why-effective_size-networkx) | `effective_size` |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-effective_size-ucinet) | `structuralholes` | published documentation |
| [manynet](../../tools/manynet.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... *(reason incomplete)* [details](#why-effective_size-manynet) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-effective_size-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (self-loops, ties and weights) on inputs tagged loops. effective\_size: NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. This reference ignores loops. effective\_size\_weighted: Burt's effective size counts a node's neighbours; NetworkX's weighted formula also counts a neighbour's self-loop as redundancy (0.5 for node 0 of 1-0 plus a loop at 1, against 1). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 2 comparisons differ and 33 agree. Finding F025 (defect): effective\_size is wrong for weighted or directed graphs on its vectorized path. Findings: [F025](../../findings.html#f025).
- <a id="why-effective_size-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-effective_size-manynet"></a>**[manynet](../../tools/manynet.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> manynet 2.4.0 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, normalization, self-loops and ties) on inputs tagged directed, edge\_case, loops and multi\_edges. manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. Relation to the reference value: Directed input, multigraphs: the values differ from the reference value's on directed networks and on multigraphs with loops (half the reference value's on a directed cycle), cause not traced; simple undirected networks agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 8 comparisons differ and 20 agree. Finding F082 (defect): Effective size and efficiency differ on directed networks and multigraphs with loops. Findings: [F082](../../findings.html#f082). **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `effective_size` | NetworkX | any | differs | loops | self\_loops, ties | abs 1e-12, rel 1e-12 | `nx.effective_size(MultiGraph \| MultiDiGraph)` | NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. This reference ignores loops. |
| `effective_size` | manynet | any | differs | directed, edge\_case, loops, multi\_edges | defaults, direction, multi\_edges, normalization, self\_loops, ties | abs 1e-12, rel 1e-12 | `manynet::node_effsize(g) (node_by_effsize in newer versions)` | manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. |
| `effective_size_weighted` | NetworkX | any | differs | loops | self\_loops, weights | abs 1e-12, rel 1e-12 | `nx.effective_size(G, weight = 'weight')` | Burt's effective size counts a node's neighbours; NetworkX's weighted formula also counts a neighbour's self-loop as redundancy (0.5 for node 0 of 1-0 plus a loop at 1, against 1). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F025](../../findings.html#f025) | NetworkX | defect | effective\_size is wrong for weighted or directed graphs on its vectorized path |
| [F082](../../findings.html#f082) | manynet | defect | Effective size and efficiency differ on directed networks and multigraphs with loops |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
