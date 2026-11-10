---
title: "Heavy path decomposition"
layout: default
parent: "Traversal, trees and DAGs"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Heavy path decomposition {#concept-top}

Family: [Traversal, trees and DAGs](index.html). Subfamily: Tree structure and enumeration. Concept id: `heavy_path_decomposition`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\mathrm{size}(v)\)</td><td>number of nodes in the subtree of \(v\) in the rooted tree</td></tr><tr><td>\(\mathrm{heavy}(v)\)</td><td>the child of \(v\) with the largest subtree</td></tr></tbody></table></div>

## Definition {#concept-definition}

Heavy path decomposition. Entries grouped here: Heavy Path Decomposition.

*Definition partly written:* Defined from the standard construction without a cited primary source; the tool entry is documented only and not specified further.

<div class="formula-block"><p class="formula-name"><strong>Heavy path decomposition</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[\mathrm{heavy}(v)=\arg\max_{c\in\mathrm{ch}(v)}\mathrm{size}(c),\qquad \text{heavy edges }v\mathrm{heavy}(v)\text{ form paths; every other edge is light}\]</div><p class="formula-where">In a rooted tree every root-to-node path meets at most \(\log_2 n\) light edges. Ties between children of equal size are broken by a convention not fixed here.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_decomposition_heavy_path">Heavy Path Decomposition</a></td><td><code>cat_decomposition_heavy_path</code></td><td>1</td><td>Heavy path decomposition of a rooted tree; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/jgrapht.html">JGraphT</a></th></tr></thead><tbody><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equal subtree sizes: the heavy child is not unique, so the decomposition is not unique.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">One path of one node.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details></div>

## Heavy Path Decomposition {#cat_decomposition_heavy_path}

Measure id: `cat_decomposition_heavy_path`. Original family: Paths and distances.

**Definition.** Heavy Path Decomposition.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/jgrapht.html">JGraphT</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_decomposition_heavy_path-jgrapht">details</a></td><td><code>HeavyPathDecomposition</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_decomposition_heavy_path-jgrapht"></a>**[JGraphT](../../tools/jgrapht.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. JGraphT 1.5.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*)); API names: HeavyPathDecomposition.

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht)
{% endraw %}
