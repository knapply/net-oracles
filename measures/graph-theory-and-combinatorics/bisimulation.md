---
title: "Maximum bisimulation"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Maximum bisimulation {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Isomorphism and subgraph matching. Concept id: `bisimulation`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(m=|E|\)</td><td>number of edges</td></tr><tr><td>\(\approx\)</td><td>a bisimulation relation on \(V\)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Maximum bisimulation. Entries grouped here: Maximum bisimulation.

*Definition partly written:* Defined from the standard notion without a cited primary source (Paige and Tarjan 1987 is not among the checked bibliography); the documented entry is not specified further.

<div class="formula-block"><p class="formula-name"><strong>Maximum bisimulation</strong> <span class="applies">applies to: directed</span></p><div class="formula">\[u\approx v\Rightarrow\bigl(\forall (u,u')\in E\ \exists (v,v')\in E:\ u'\approx v'\bigr)\ \wedge\ \bigl(\forall (v,v')\in E\ \exists (u,u')\in E:\ u'\approx v'\bigr)\]</div><p class="formula-where">The largest such relation is an equivalence; the coarsest stable partition of the nodes. It can be refined from initial label classes.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cat_bisimulation_maximum">Maximum bisimulation</a></td><td><code>cat_bisimulation_maximum</code></td><td>1</td><td>Maximum bisimulation; documented only.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/rustworkx.html">rustworkx</a></th></tr></thead><tbody><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">All nodes (with equal labels) are bisimilar.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Defined by successors; the version with predecessors is a different relation.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Edgeless graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details></div>

## Maximum bisimulation {#cat_bisimulation_maximum}

Measure id: `cat_bisimulation_maximum`. Original family: Graph theory and combinatorics.

**Definition.** Maximum bisimulation.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_bisimulation_maximum-rustworkx">details</a></td><td><code>digraph_maximum_bisimulation</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_bisimulation_maximum-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_maximum\_bisimulation.

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
