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

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(i^*\)</td><td>focal paper; \(\mathrm{refs}(i^*)\) its references; arcs run from the citing to the cited paper</td></tr><tr><td>\(f_i\)</td><td>1 if citer \(i\) cites \(i^*\), else 0</td></tr><tr><td>\(b_i\)</td><td>1 if citer \(i\) cites at least one paper in \(\mathrm{refs}(i^*)\), else 0</td></tr><tr><td>\(n_t\)</td><td>number of papers published in the window that cite \(i^*\) or a paper in \(\mathrm{refs}(i^*)\)</td></tr><tr><td>\(\delta\)</td><td>length of the window after the focal paper's date (time delta)</td></tr></tbody></table></div>

## Definition {#concept-definition}

CD index. Entries grouped here: CD index.

<div class="formula-block"><p class="formula-name"><strong>CD index (Funk and Owen-Smith 2017)</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[CD_{\delta}=\frac1{n_t}\sum_{i=1}^{n_t}\bigl(-2f_ib_i+f_i\bigr)=\frac{n_i-n_j}{n_i+n_j+n_k}\]</div><p class="formula-where">Only papers published after the focal paper and at most \(\delta\) after it are counted. \(n_i\) cite the focal paper only, \(n_j\) cite it and its references, \(n_k\) cite its references only. The value lies in \([-1,1]\): \(+1\) disruptive, \(-1\) consolidating. The weighted form divides each term by the weight of the citing paper.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#nxs_cd_index">CD index</a></td><td><code>nxs_cd_index</code></td><td>1</td><td>The index in the window of length delta (delta 0, 1, 3, ...), unweighted or with each term divided by the citer's weight; the window in the definition covers only papers published after the focal paper.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">\(n_t=0\): no citer in the window, \(0/0\): not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A paper with no citers and none citing its references has \(n_t=0\): not defined.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Citation arcs are directed from the citing to the cited paper; the formula reads citers as in-neighbours of the focal node. A tool that counts citers published before the focal paper, or all citers of a reference whatever their date, computes a different number.</td><td><a class="st st-w st-conv" href="../../findings.html#f032" title="NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value&#x27;s default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX&#x27;s rounding of the index to two decimals.">differs</a></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: differs. NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. <em>(conventions.json nxs_cd_index / nxs_cd_index_delta0)</em></li></ul></details></div>

## CD index {#nxs_cd_index}

Measure id: `nxs_cd_index`. Original family: Graph theory and combinatorics.

**Definition.** CD index.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a></td><td>Differs by convention (defaults and direction): NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n... <a href="#why-nxs_cd_index-networkx">details</a></td><td><code>cd_index</code></td><td></td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-nxs_cd_index-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (defaults and direction) on inputs tagged directed. NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. Reproduced by the reference value computed with NetworkX's citation window, which matches NetworkX on every fixture. Publication times are a fixed function of the node id (derived/nx\_shims.py), so any arc can bring in a citer outside the window: declared for every directed network (a two-node network with the arc 0 -&gt; 1 already differs: NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals. Mapping: the reference value computed with the tool's convention (citers up to the end of the window, earlier ones included; every citer of a reference in the pool) agrees with the tool within abs 0.0050001, rel 0 on all 24 comparisons where the difference occurs. Tolerance before mapping: abs 0.0050001, rel 0 (0 means exact equality). 24 comparisons differ and 3 agree. Finding F032 (convention): cd\_index pools every citer of the references, whatever its time. Findings: [F032](../../findings.html#f032).

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nxs_cd_index_delta0</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 0, time = 'time')</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr><tr><td><code>nxs_cd_index_delta1</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 1, time = 'time'), -999 if it raises</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr><tr><td><code>nxs_cd_index_delta3_weighted</code></td><td>NetworkX</td><td>directed</td><td>differs</td><td>directed</td><td>defaults, direction</td><td>abs 0.0050001, rel 0</td><td><code>nx.cd_index(G, v, time_delta = 3, time = 'time', weight = 'w')</code></td><td>NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n every citer of a reference whatever its time; Funk and Owen-Smith (and the reference value's default) count only the papers published after the focal paper and at most delta after it. NetworkX 1, reference undefined, since the only citer predates the focal paper). The tolerance is NetworkX's rounding of the index to two decimals.</td></tr></tbody></table></div>

**Harness files:** [harness/manifest/nx_shims.yaml](https://github.com/knapply/net-oracles/tree/main/harness/manifest/nx_shims.yaml); [harness/golden/networkx/](https://github.com/knapply/net-oracles/tree/main/harness/golden/networkx/)

**Findings**

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Kind</th><th>Title</th></tr></thead><tbody><tr><td><a href="../../findings.html#f032">F032</a></td><td>NetworkX</td><td>convention</td><td>cd_index pools every citer of the references, whatever its time</td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
