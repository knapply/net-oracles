---
title: "Random tree"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Random tree {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Random trees and forests. Concept id: `random_tree`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(n\)</td><td>number of nodes</td></tr></tbody></table></div>

## Definition {#concept-definition}

Random tree. Entries grouped here: Random tree generator.

*Definition partly written:* The uniform labelled tree is written; the tool functions are named only and which sampler they use is not recorded.

<div class="formula-block"><p class="formula-name"><strong>Uniform random labelled tree (Prufer 1918)</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[\Pr(T)=n^{-(n-2)}\quad\text{for each of the }n^{n-2}\text{ labelled trees}\]</div><p class="formula-where">A Prufer sequence of \(n-2\) uniform labels corresponds one-to-one to a labelled tree. A generator returns a random sample, so a result is reproducible only for a fixed seed and random generator; tools use different generators.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#gen_random_tree">Random tree generator</a></td><td><code>gen_random_tree</code></td><td>2</td><td>A tree on \(n\) nodes; whether it is uniform among labelled trees is not recorded.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/igraph.html">igraph (R)</a></th></tr></thead><tbody><tr><td title="The graph has fewer nodes than a normalizing constant or a term of the formula needs (for example n &lt; 3 when dividing by (n-1)(n-2)), so a division by zero or an empty sum arises."><strong>Too few nodes for the formula</strong></td><td class="def">For \(n=1\) there is one tree (no edges); for \(n=2\) one tree; the Prufer sequence has length \(n-2\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">\(n=0\): no tree.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Too few nodes for the formula</summary><ul><li>No tool entries.</li></ul></details><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details></div>

## Random tree generator {#gen_random_tree}

Measure id: `gen_random_tree`. Original family: Generators and rewiring.

**Definition.** Random tree generator.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_random_tree-networkx">details</a></td><td><code>nonisomorphic_trees; random_labeled_rooted_tree; random_labeled_tree; random_unlabeled_rooted_tree; random_unlabeled_tree</code></td><td>API listing</td></tr><tr><td><a href="../../tools/igraph.html">igraph (R)</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-gen_random_tree-igraph">details</a></td><td><code>sample_tree</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-gen_random_tree-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: nonisomorphic\_trees; random\_labeled\_rooted\_tree; random\_labeled\_tree; random\_unlabeled\_rooted\_tree; random\_unlabeled\_tree.
- <a id="why-gen_random_tree-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: sample\_tree.

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
