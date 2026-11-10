---
title: "Community-based centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Community-based centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `community_centrality`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(\mathcal C(v)\)</td><td>communities that contain \(v\) (overlapping link communities)</td></tr><tr><td>\(J(a,b)\)</td><td>Jaccard coefficient of the node sets of communities \(a\) and \(b\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Community-based centrality. Entries grouped here: Communitycent.

*Definition partly written:* The documentation describes the two scores in words; the exact formulas, the community-detection step they depend on and the normalization are not stated in the sources read.

<div class="formula-block"><p class="formula-name"><strong>Community weight score</strong> <span class="applies">applies to: undirected</span></p><div class="formula">\[\mathrm{commweight}(v)=\sum_{a\in\mathcal C(v)}\ \frac{1}{\sum_{b\in\mathcal C(v)}J(a,b)}\ (\text{as described in the documentation})\]</div><p class="formula-where">Each community of \(v\) is weighted by its similarity to the other communities of \(v\); described in words in the tool's documentation, the exact expression is not stated there.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_communitycent">Communitycent</a></td><td><code>cat_communitycent</code></td><td>1</td><td>Two scores selected by a type argument: community-membership weighting by Jaccard similarity, and community connectivity weighting by edges leaving versus inside communities (the inverse of modularity).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/centiserve.html">centiserve</a></th></tr></thead><tbody><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">A node in no community has no score from these definitions.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details></div>

## Communitycent {#cat_communitycent}

Measure id: `cat_communitycent`. Original family: Centrality.

**Definition.** Communitycent.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/centiserve.html">centiserve</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_communitycent-centiserve">details</a></td><td><code>communitycent</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_communitycent-centiserve"></a>**[centiserve](../../tools/centiserve.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. centiserve 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package centiserve: exported functions and help titles); API names: communitycent.

**Tools cited:** [jalili2015centiserver](../../references.html#jalili2015centiserver)
{% endraw %}
