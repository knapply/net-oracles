---
title: "Partition test"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Partition test {#concept-top}

Family: [Communities](index.html). Subfamily: Partition comparison and operations. Concept id: `is_partition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\{S_1..S_k\}\)</td><td>a collection of node sets</td></tr></tbody></table></div>

## Definition {#concept-definition}

Partition test. Entries grouped here: Is partition (community).

*Definition partly written:* Documented only (NetworkX), never run; the condition is stated from its definition, with no primary paper.

<div class="formula-block"><p class="formula-name"><strong>Partition test</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\{S_i\}\text{ is a partition of }V\iff\bigcup_iS_i=V\ \text{and}\ S_i\cap S_j=\emptyset\ (i\ne j)\ \text{and}\ S_i\ne\emptyset\]</div><p class="formula-where">The sets cover all nodes, no node is in two sets (a cover that allows overlap is not a partition); empty sets are normally excluded.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_is_partition-community">Is partition (community)</a></td><td><code>cat_is_partition@community</code></td><td>1</td><td>True when the collection of node sets is a partition of the node set.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">The empty collection partitions the empty node set.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">Overlapping sets or missing nodes make it false.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Is partition (community) {#cat_is_partition-community}

Measure id: `cat_is_partition@community`. Original family: Communities.

**Definition.** Is partition (community).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_is_partition-community-networkx">details</a></td><td><code>is_partition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_is_partition-community-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: is\_partition.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
