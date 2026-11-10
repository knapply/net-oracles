---
title: "CD index"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# CD index {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: DAGs and topological order. Concept id: `cd_index`. 1 measure.

## Definition {#concept-definition}

CD index. Entries grouped here: CD index.

*Definition not yet written.*

## CD index {#nxs_cd_index}

Measure id: `nxs_cd_index`. Original family: Graph theory and combinatorics.

**Definition.** CD index.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults and direction): NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n... <a href="#why-nxs_cd_index-networkx">details</a></td><td><code>cd_index</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_cd_index-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults and direction) on inputs tagged directed. NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. Reproduced by the reference value computed with NetworkX's citation window, which matches NetworkX on every fixture. Publication times are a fixed function of the node id (derived/nx\_shims.py), so any arc can bring in a citer outside the window: declared for every directed network (a two-node network with the arc 0 -&gt; 1 already differs: NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. Mapping: the reference value computed with the tool's convention (citers up to the end of the window, earlier ones included; every citer of a reference in the pool) agrees with the tool within abs 0.0050001, rel 0 on all 24 comparisons where the difference occurs. Tolerance before mapping: abs 0.0050001, rel 0 (0 means exact equality). 24 comparisons differ and 3 agree. Finding F032 (convention): cd\_index pools every citer of the references, whatever its time. Findings: [F032](../../findings.html#f032).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_cd_index_delta0</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 0, time = 'time')</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr><tr><td><code>nxs_cd_index_delta1</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 1, time = 'time'), -999 if it raises</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr><tr><td><code>nxs_cd_index_delta3_weighted</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 3, time = 'time', weight = 'w')</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr></tbody></table></div>

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f032">F032</a></td><td>NetworkX</td><td>convention</td><td>cd_index pools every citer of the references, whatever its time</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
