---
title: "Rank comparison and ordering"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Rank comparison and ordering {#concept-top}

Family: [Centrality](index.html). Subfamily: Partial rankings (netrankr). Concept id: `rank_comparison`. 7 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(P=(V,\preceq)\)</td><td>partial order</td></tr><tr><td>\(\ell\)</td><td>a total ranking</td></tr></tbody></table></div>

## Definition {#concept-definition}

Rank comparison and ordering. Entries grouped here: Comparable pairs; Compare ranks; Get rankings; Incomparable pairs; Index builder; Is preserved; and 1 more.

*Definition partly written:* The majorization gap and the compare\_ranks counting rule are not defined in the sources read.

<div class="formula-block"><p class="formula-name"><strong>Comparable and incomparable pairs</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\mathrm{comp}(P)=\bigl|\{\{u,v\}:\ u\preceq v\ \text{or}\ v\preceq u\}\bigr|,\qquad \mathrm{inc}(P)=\binom n2-\mathrm{comp}(P)\]</div><p class="formula-where">Pairs of nodes that every compatible ranking orders the same way, and pairs for which rankings may differ.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Compatibility of a ranking</strong> <span class="applies">applies to: any</span></p><div class="formula">\[\ell\ \text{preserves}\ P\ \Longleftrightarrow\ u\preceq v\Rightarrow r_\ell(u)\ge r_\ell(v)\]</div><p class="formula-where">A ranking is compatible with the partial order when it never reverses a dominance pair.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_comparable_pairs">Comparable pairs</a></td><td><code>cat_comparable_pairs</code></td><td>1</td><td>Number of comparable pairs.</td></tr><tr><td><a href="#cat_compare_ranks">Compare ranks</a></td><td><code>cat_compare_ranks</code></td><td>1</td><td>Counts, for every pair of nodes, how often each is ranked above the other across rankings.</td></tr><tr><td><a href="#cat_rankings">Get rankings</a></td><td><code>cat_rankings</code></td><td>1</td><td>Enumerates linear extensions (rankings) of a partial order.</td></tr><tr><td><a href="#cat_incomparable_pairs">Incomparable pairs</a></td><td><code>cat_incomparable_pairs</code></td><td>1</td><td>Number of incomparable pairs.</td></tr><tr><td><a href="#cat_builder">Index builder</a></td><td><code>cat_builder</code></td><td>1</td><td>Builds a centrality index from an indirect relation, a transformation and an aggregation (see walk and distance transformations).</td></tr><tr><td><a href="#cat_is_preserved">Is preserved</a></td><td><code>cat_is_preserved</code></td><td>1</td><td>Check that given rankings preserve the partial order.</td></tr><tr><td><a href="#cat_gap_majorization">Majorization gap</a></td><td><code>cat_gap_majorization</code></td><td>1</td><td>Majorization gap: its definition is not stated in the sources read.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/netrankr.html">netrankr</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">No pairs.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several shortest paths of equal length, equal scores, or equal eigenvalues, including ties that arise only in floating point (for example equal sums of reciprocals)."><strong>Ties and equal values</strong></td><td class="def">Mutually dominating nodes are comparable in both directions.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Every pair of distinct nodes is joined by an edge. All nodes are structurally equivalent."><strong>Complete graph</strong></td><td class="def">All pairs comparable (mutual dominance).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">Leaves are comparable to each other (mutual inclusion) and to the centre.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Ties and equal values</summary><ul><li>No tool entries.</li></ul></details><details><summary>Complete graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## Comparable pairs {#cat_comparable_pairs}

Measure id: `cat_comparable_pairs`. Original family: Graph theory and combinatorics.

**Definition.** Comparable pairs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_comparable_pairs-netrankr">details</a></td><td><code>comparable_pairs</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_comparable_pairs-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: comparable\_pairs.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Compare ranks {#cat_compare_ranks}

Measure id: `cat_compare_ranks`. Original family: Graph theory and combinatorics.

**Definition.** Compare ranks.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_compare_ranks-netrankr">details</a></td><td><code>compare_ranks</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_compare_ranks-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: compare\_ranks.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Get rankings {#cat_rankings}

Measure id: `cat_rankings`. Original family: Graph theory and combinatorics.

**Definition.** Get rankings.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_rankings-netrankr">details</a></td><td><code>get_rankings</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_rankings-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: get\_rankings.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Incomparable pairs {#cat_incomparable_pairs}

Measure id: `cat_incomparable_pairs`. Original family: Graph theory and combinatorics.

**Definition.** Incomparable pairs.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_incomparable_pairs-netrankr">details</a></td><td><code>incomparable_pairs</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_incomparable_pairs-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: incomparable\_pairs.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Index builder {#cat_builder}

Measure id: `cat_builder`. Original family: Graph theory and combinatorics.

**Definition.** Index builder.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_builder-netrankr">details</a></td><td><code>index_builder</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_builder-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: index\_builder.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Is preserved {#cat_is_preserved}

Measure id: `cat_is_preserved`. Original family: Graph theory and combinatorics.

**Definition.** Is preserved.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_is_preserved-netrankr">details</a></td><td><code>is_preserved</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_is_preserved-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: is\_preserved.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)

## Majorization gap {#cat_gap_majorization}

Measure id: `cat_gap_majorization`. Original family: Graph theory and combinatorics.

**Definition.** Majorization gap.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/netrankr.html">netrankr</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_gap_majorization-netrankr">details</a></td><td><code>majorization_gap</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_gap_majorization-netrankr"></a>**[netrankr](../../tools/netrankr.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. netrankr 2.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package netrankr: exported functions and help titles); API names: majorization\_gap.

**Tools cited:** [schoch2018centrality](../../references.html#schoch2018centrality)
{% endraw %}
