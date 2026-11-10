---
title: "Simple cycles"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Simple cycles {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Cycles. Concept id: `simple_cycles`. 1 measure.

## Definition {#concept-definition}

Every simple cycle, by Johnson's search or a bounded depth-first search.

## References {#concept-references}

[depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

## Simple cycles {#simple_cycles}

Measure id: `simple_cycles`. Original family: Graph theory and combinatorics.

**Definition.** Every simple cycle, by Johnson's search or a bounded depth-first search.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `minimum_cycle_basis; recursive_simple_cycles; simple_cycles` |  |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `simple_cycles` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `fundamental_cycles; minimum_cycle_basis; simple_cycles` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `all_circuits` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `simple_cycles` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `find_odd_cycle; hawick_circuits; tiernan_all_cycles` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_simple` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.simple_cycles(M), canonically rotated` | these fixtures have more than 200 000 simple cycles, which neither side enumerates here; cyc\_simple\_bound4 covers them |
| `cyc_simple_bound4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.simple_cycles(M, length_bound = 4)` |  |

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
