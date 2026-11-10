---
title: "Partition counts"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Partition counts {#concept-top}

Family: [Communities](index.html). Subfamily: Graph bisection and partitioning. Concept id: `partition_counts`. 1 measure.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\), \(n=|V|\); every edge has a source and a target (the ends of an undirected edge are interchangeable)</td></tr><tr><td>\(c_i\)</td><td>community (group) of node \(i\) in a partition \(\mathcal P\) of \(V\); \(\delta(c_i,c_j)=1\) when \(i,j\) are in the same community</td></tr></tbody></table></div>

## Definition {#concept-definition}

Partition counts. Entries grouped here: Partition counts.

*Definition partly written:* Defined by the NetworkX documentation (intra-community edges, inter-community edges, inter-community non-edges); no original paper is cited in the sources.

<div class="formula-block"><p class="formula-name"><strong>Partition counts</strong> <span class="applies">applies to: undirected, simple</span></p><div class="formula">\[I=\bigl|\{\{u,v\}\in E:c_u=c_v\}\bigr|,\quad X=\bigl|\{\{u,v\}\in E:c_u\ne c_v\}\bigr|,\quad Z=\bigl|\{\{u,v\}\notin E,u\ne v:c_u\ne c_v\}\bigr|\]</div><p class="formula-where">Counts of intra-community edges, inter-community edges and inter-community non-edges; defined for any partition.</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#cnx_partition_counts">Partition counts</a></td><td><code>cnx_partition_counts</code></td><td>1</td><td>The triple \((I,X,Z)\) of a partition.</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th></tr></thead><tbody><tr><td title="The graph has no nodes (n = 0)."><strong>Empty graph</strong></td><td class="def">All zero.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The graph has nodes but no edges (m = 0)."><strong>Edgeless graph</strong></td><td class="def">\(I=X=0\); \(Z\) counts all inter-community pairs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (empty).">agrees</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">Not edges between distinct nodes: excluded.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Merged in the simple reading.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir).">agrees</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Undirected pairs.</td><td><span class="st st-w st-ok" title="No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense).">agrees</span></td></tr><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">A single community: \(X=Z=0\); singletons: \(I=0\).</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Empty graph</summary><ul><li>No tool entries.</li></ul></details><details><summary>Edgeless graph</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (empty). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Self-loops</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Parallel edges</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (multi_loops_und, multi_loops_dir). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Undirected versus directed input</summary><ul><li><strong>NetworkX</strong>: agrees. No difference from the reference value recorded on the compared inputs of this kind (karate, gnp_dir_dense). <em>(capabilities.csv and conventions.json (outcome agrees))</em></li></ul></details><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details></div>

## Partition counts {#cnx_partition_counts}

Measure id: `cnx_partition_counts`. Original family: Communities.

**Definition.** Partition counts.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td></td><td></td></tr></tbody></table></div>

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>nx_partition_counts</code></td><td>NetworkX</td><td>any</td><td>agrees</td><td></td><td></td><td>abs 0, rel 0</td><td><code>(quality.intra_community_edges, quality.inter_community_edges, quality.inter_community_non_edges) of blocks on G_natural</code></td><td></td></tr></tbody></table></div>

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
