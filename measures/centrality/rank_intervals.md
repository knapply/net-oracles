---
title: "Rank intervals"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Rank intervals {#concept-top}

Family: [Centrality](index.html). Subfamily: Partial rankings (netrankr). Concept id: `rank_intervals`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(P=(V,\preceq)\)</td><td>partial order of the nodes</td></tr><tr><td>\(\mathrm{up}(v),\,\mathrm{down}(v)\)</td><td>nodes strictly above \(v\), and strictly below \(v\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Rank intervals. Entries grouped here: Rank intervals.

<div class="formula-block"><p class="formula-name"><strong>Rank interval (Schoch and Brandes 2016)</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\bigl[\,|\mathrm{up}(v)|+1,\ \ n-|\mathrm{down}(v)|\,\bigr]\]</div><p class="formula-where">The best and worst rank (counted from the top) that \(v\) can take in any linear ranking compatible with the partial order.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_intervals_rank">Rank intervals</a></td><td><code>cat_intervals_rank</code></td><td>1</td><td>The interval above for every node of a given partial order.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has exactly one node (n = 1), with or without a self-loop."><strong>Single node</strong></td><td class="def">Interval \([1,1]\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Equivalent nodes (mutually dominating) have the same interval; strictness of \(\mathrm{up}\) and \(\mathrm{down}\) needs a stated tie rule.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All nodes are mutually dominating: every interval is \([1,n]\) or one tied rank, depending on the tie rule.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Centre \([1,1]\); leaves \([2,n]\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Single node</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## Rank intervals {#cat_intervals_rank}

Measure id: `cat_intervals_rank`. Original family: Graph theory and combinatorics.

**Definition.** Rank intervals.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_intervals_rank-netrankr">details</a></td><td><code>rank_intervals</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_intervals_rank-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: rank\_intervals.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
