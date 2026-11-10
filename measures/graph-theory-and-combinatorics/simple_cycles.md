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

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `minimum_cycle_basis; recursive_simple_cycles; simple_cycles` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-igraph) | `simple_cycles` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-pyigraph) | `fundamental_cycles; minimum_cycle_basis; simple_cycles` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-graphtool) | `all_circuits` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-rustworkx) | `simple_cycles` | API listing |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-jgrapht) | `DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles` | API listing |
| [Boost Graph Library](../../tools/boost.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-simple_cycles-boost) | `find_odd_cycle; hawick_circuits; tiernan_all_cycles` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-simple_cycles-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: simple\_cycles.
- <a id="why-simple_cycles-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: fundamental\_cycles; minimum\_cycle\_basis; simple\_cycles.
- <a id="why-simple_cycles-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: all\_circuits.
- <a id="why-simple_cycles-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: simple\_cycles.
- <a id="why-simple_cycles-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles.
- <a id="why-simple_cycles-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: find\_odd\_cycle; hawick\_circuits; tiernan\_all\_cycles.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cyc_simple` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `nx.simple_cycles(M), canonically rotated` | these fixtures have more than 200 000 simple cycles, which neither side enumerates here; cyc\_simple\_bound4 covers them |
| `cyc_simple_bound4` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.simple_cycles(M, length_bound = 4)` |  |

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
