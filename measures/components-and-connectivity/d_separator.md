---
title: "D-separators"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# D-separators {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Cuts and separators. Concept id: `d_separator`. 3 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G\)</td><td>directed acyclic graph</td></tr><tr><td>\(X,Y,Z\)</td><td>disjoint node sets</td></tr><tr><td>\(\mathrm{de}(w)\)</td><td>descendants of \(w\) (including \(w\))</td></tr></tbody></table></div>

## Definition {#concept-definition}

D-separators. Entries grouped here: D separated; Find minimal d separator; Is minimal d separator.

*Definition partly written:* cat\_d\_find\_minimal\_separator and cat\_d\_is\_minimal\_separator (NetworkX) are documented only and were never run; minimality and the search options are not recorded.

<div class="formula-block"><p class="formula-name"><strong>d-separation (Pearl 1988)</strong> <span class="applies">applies to: directed, acyclic</span></p><div class="formula">\[Z\text{ d-separates }X\text{ and }Y\iff\text{every path between them is blocked by }Z\]</div><p class="formula-where">A path is blocked by \(Z\) if it contains a chain \(a\to w\to b\) or fork \(a\leftarrow w\to b\) with \(w\in Z\), or a collider \(a\to w\leftarrow b\) with \(\mathrm{de}(w)\cap Z=\emptyset\). Defined for DAGs; the sets must be disjoint.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gb_d_separated">D separated</a></td><td><code>gb_d_separated</code></td><td>1</td><td>Whether a given set \(Z\) d-separates the node 0 from node \(n-1\) (the test).</td></tr><tr><td><a href="#cat_d_find_minimal_separator">Find minimal d separator</a></td><td><code>cat_d_find_minimal_separator</code></td><td>1</td><td>Documented for NetworkX as finding a minimal d-separator; not recorded in detail.</td></tr><tr><td><a href="#cat_d_is_minimal_separator">Is minimal d separator</a></td><td><code>cat_d_is_minimal_separator</code></td><td>1</td><td>Documented for NetworkX as testing minimality of a d-separator; not recorded in detail.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">Empty \(Z\): d-separated iff no path connects \(X\) and \(Y\) without colliders; sets that overlap are not valid input.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">Two adjacent nodes cannot be d-separated by any set.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (pair, single_node).">agrees</span></td></tr><tr><td title="A directed graph in which some node cannot reach another along edge directions although the graph may be weakly connected (not strongly connected)."><strong>Directed graph, unreachable pairs</strong></td><td class="def">Direction matters: blocking depends on the arrow pattern, not on reachability alone.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined for directed acyclic graphs; cycles are excluded.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Too few nodes for the formula</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (pair, single_node). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Directed graph, unreachable pairs</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (gnp_dir_sparse, weighted_dir, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details></div>

## D separated {#gb_d_separated}

Measure id: `gb_d_separated`. Original family: Traversal, trees and DAGs.

**Definition.** D separated.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>is_d_separator</code></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>gb_d_separated</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>nx.is_d_separator(M, 0, n - 1, {1})</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Find minimal d separator {#cat_d_find_minimal_separator}

Measure id: `cat_d_find_minimal_separator`. Original family: Components and connectivity.

**Definition.** Find minimal d separator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_d_find_minimal_separator-networkx">details</a></td><td><code>find_minimal_d_separator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_find_minimal_separator-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: find\_minimal\_d\_separator.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Is minimal d separator {#cat_d_is_minimal_separator}

Measure id: `cat_d_is_minimal_separator`. Original family: Components and connectivity.

**Definition.** Is minimal d separator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_d_is_minimal_separator-networkx">details</a></td><td><code>is_minimal_d_separator</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_d_is_minimal_separator-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_minimal\_d\_separator.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
