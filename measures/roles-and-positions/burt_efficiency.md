---
title: "Burt efficiency"
layout: default
parent: "Roles and positions"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Burt efficiency {#concept-top}

Family: [Roles and positions](index.html). Subfamily: Structural holes and brokerage. Concept id: `burt_efficiency`. 1 measure.

## Definition {#concept-definition}

Burt efficiency. Entries grouped here: Efficiency.

## Efficiency {#efficiency}

Measure id: `efficiency`. Original family: Roles and positions.

**Definition.** Efficiency.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (self-loops): NetworkX keeps self-loops in the effective size (see effective\_size). [details](#why-efficiency-networkx) |  |  |
| [UCINET](../../tools/ucinet.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. [details](#why-efficiency-ucinet) |  | published documentation |
| [manynet](../../tools/manynet.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... *(reason incomplete)* [details](#why-efficiency-manynet) |  |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-efficiency-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (self-loops) on inputs tagged loops. NetworkX keeps self-loops in the effective size (see effective\_size). No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 2 comparisons differ and 26 agree.
- <a id="why-efficiency-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.
- <a id="why-efficiency-manynet"></a>**[manynet](../../tools/manynet.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> manynet 2.4.0 was run and its value differs from the reference value by convention (defaults, direction, multi-edges, normalization, self-loops and ties) on inputs tagged directed, edge\_case, loops and multi\_edges. manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. Relation to the reference value: Directed input, multigraphs: the values differ from the reference value's on directed networks and on multigraphs with loops (half the reference value's on a directed cycle), cause not traced; simple undirected networks agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-12 (0 means exact equality). 9 comparisons differ and 19 agree. **Reason incomplete:** the cause of the difference is stated in the sources as not identified.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `efficiency` | NetworkX | any | differs | loops | self\_loops | abs 1e-12, rel 1e-12 | `nx.effective_size(G) / number of distinct neighbours other than the node` | NetworkX keeps self-loops in the effective size (see effective\_size). |
| `efficiency` | manynet | any | differs | directed, edge\_case, loops, multi\_edges | defaults, direction, multi\_edges, normalization, self\_loops, ties | abs 1e-12, rel 1e-12 | `manynet::node_efficiency(g) (node_by_efficiency in newer versions)` | manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about half the reference value's on a directed cycle and on directed random graphs); the cause was not traced. Simple undirected networks agree. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_manynet](../../references.html#tool_manynet)
{% endraw %}
