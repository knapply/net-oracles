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

*Definition not yet written.*

## References {#concept-references}

[depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

## Simple cycles {#simple_cycles}

Measure id: `simple_cycles`. Original family: Graph theory and combinatorics.

**Definition.** Every simple cycle, by Johnson's search or a bounded depth-first search.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>minimum_cycle_basis; recursive_simple_cycles; simple_cycles</code></td><td></td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-igraph">details</a></td><td><code>simple_cycles</code></td><td>API listing</td></tr><tr><td><a href="../../tools/pyigraph.html">igraph (Python)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-pyigraph">details</a></td><td><code>fundamental_cycles; minimum_cycle_basis; simple_cycles</code></td><td>API listing</td></tr><tr><td><a href="../../tools/graphtool.html">graph-tool</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-graphtool">details</a></td><td><code>all_circuits</code></td><td>API listing</td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-rustworkx">details</a></td><td><code>simple_cycles</code></td><td>API listing</td></tr><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-jgrapht">details</a></td><td><code>DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles</code></td><td>API listing</td></tr><tr><td><a href="../../tools/boost.html">Boost Graph Library</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-simple_cycles-boost">details</a></td><td><code>find_odd_cycle; hawick_circuits; tiernan_all_cycles</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-simple_cycles-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: simple\_cycles.
- <a id="why-simple_cycles-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: fundamental\_cycles; minimum\_cycle\_basis; simple\_cycles.
- <a id="why-simple_cycles-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: all\_circuits.
- <a id="why-simple_cycles-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: simple\_cycles.
- <a id="why-simple_cycles-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles.
- <a id="why-simple_cycles-boost"></a>**[Boost Graph Library](../../tools/boost.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. Boost Graph Library 1.90 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (Boost Graph Library 1.90 documentation: table of contents (algorithms and random-graph tools) plus algorithm headers it omits); API names: find\_odd\_cycle; hawick\_circuits; tiernan\_all\_cycles.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>cyc_simple</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.simple_cycles(M), canonically rotated</code></td><td>these fixtures have more than 200 000 simple cycles, which neither side enumerates here; cyc_simple_bound4 covers them</td></tr><tr><td><code>cyc_simple_bound4</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.simple_cycles(M, length_bound = 4)</code></td><td></td></tr></tbody></table></div>

**References:** [depina1995applications](../../references.html#depina1995applications), [dias2013efficient](../../references.html#dias2013efficient), [gupta2021finding](../../references.html#gupta2021finding), [hagberg2008exploring](../../references.html#hagberg2008exploring), [itai1978finding](../../references.html#itai1978finding), [johnson1975finding](../../references.html#johnson1975finding), [kavitha2009cycle](../../references.html#kavitha2009cycle), [kirchhoff1847ueber](../../references.html#kirchhoff1847ueber)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
