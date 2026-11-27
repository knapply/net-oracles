---
title: "Krackhardt graph-theoretic dimensions"
layout: default
parent: "Descriptive statistics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Krackhardt graph-theoretic dimensions {#concept-top}

Family: [Descriptive statistics](index.html). Subfamily: Efficiency, compactness and hierarchy. Concept id: `krackhardt_dimensions`. 1 measure.

## Definition {#concept-definition}

Krackhardt graph-theoretic dimensions. Entries grouped here: Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness).

*Definition not yet written.* Documented only (sna and UCINET Krackhardt graph-theoretic dimensions), never run; the sources give the name and the tool's function, not a formula, and no verified bibliography entry for the original definition is available.

## Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness) {#krackhardt_dimensions}

Measure id: `krackhardt_dimensions`. Original family: Descriptive statistics.

**Definition.** Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../tools/sna.html">sna</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (unreachable pairs): Three conventions differ. Hierarchy: sna documents it as the share of asymmetric dyads among the non-null dyads of the reachability graph (each mutual dyad counts... <a href="#why-krackhardt_dimensions-sna">details</a></td><td><code>connectedness; lubness</code></td><td></td></tr><tr><td><a href="../../tools/ucinet.html">UCINET</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: UCINET is proprietary Windows software, never run here; listed in its documentation. <a href="#why-krackhardt_dimensions-ucinet">details</a></td><td><code>Fragmentation, Krackhardt graph-theoretic dimensions (connectedness, hierarchy, efficiency, LUBness)</code></td><td>published documentation</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-krackhardt_dimensions-sna"></a>**[sna](../../tools/sna.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> sna 2.8 was run and its value differs from the reference value by convention (unreachable pairs) on inputs tagged disconnected, not\_strongly\_connected, one\_node and null\_graph. Three conventions differ. Hierarchy: sna documents it as the share of asymmetric dyads among the non-null dyads of the reachability graph (each mutual dyad counts once); the reference value counts reachable ordered pairs, so a mutually reachable dyad weighs twice (asymmetric / (asymmetric + 2 mutual) against sna's asymmetric / (asymmetric + mutual)); the two are equal when every dyad is asymmetric or none is, and a strongly connected network gives 0 in both. Efficiency: with more than one weak component (isolated nodes count as components) sna's value differs from the reference value's, which measures the arcs against the n - c an out-forest needs (sna returns NaN on the edgeless network and 0 on two triangles and an isolate, where the reference value gives 1 and 0.789). Connectedness of a single node: sna gives 1, the reference value NaN (no pair to be connected). The normalization, the weak-component sum and the NaN rule agree with sna on every digraph of 3 and 4 nodes and 1,500 random ones of 5 to 8. The difference is the least upper bound. sna's help page defines it as an upper bound lying on a path from every upper bound to both nodes, which is the upper bound every other one reaches (the reference value's rule). The values sna returns follow a different rule, the upper bound that reaches every other upper bound (the most distant one): on all 5,660 digraphs that were run its counts equal that rule exactly, and its counts differ from the documented rule on 341. Example: arcs 0 -&gt; 1, 2 -&gt; 0, 3 -&gt; 0 on 4 nodes: the pair (0, 1) has the upper bounds 0, 2 and 3 and 0 is the one all reach; the reference value counts 1 violation (score 2/3), sna 2 (score 1/3). Networks in which every node reaches every other (and every undirected network) are not affected. Tolerance: abs 1e-12, rel 1e-12 (0 means exact equality). 10 comparisons differ and 46 agree.
- <a id="why-krackhardt_dimensions-ucinet"></a>**[UCINET](../../tools/ucinet.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run. UCINET is proprietary, commercial software for Windows; it was never run in this survey (it cannot be run headless on the Linux test machines), so no value from it is compared with the reference value. Documentation source: published help pages and program documentation.

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
