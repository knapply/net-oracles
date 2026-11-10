---
title: "Group degree centrality"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Group degree centrality {#concept-top}

Family: [Centrality](index.html). Subfamily: Degree and strength. Concept id: `group_degree`. 2 measures.

## Notation {#concept-notation}

<div class="table-wrapper"><table class="notation"><thead><tr><th>Symbol</th><th>Meaning</th></tr></thead><tbody><tr><td>\(G=(V,E)\)</td><td>graph with node set \(V\) and edge set \(E\); every edge has a source and a target (the two ends of an undirected edge are interchangeable)</td></tr><tr><td>\(n=|V|\)</td><td>number of nodes</td></tr><tr><td>\(S\subset V\)</td><td>the group</td></tr><tr><td>\(N(S)\)</td><td>nodes outside \(S\) joined by an edge to at least one member of \(S\) (for a directed graph: reached by an edge from \(S\) for the out version)</td></tr></tbody></table></div>

## Definition {#concept-definition}

Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

<div class="formula-block"><p class="formula-name"><strong>Group degree (Everett and Borgatti 1999)</strong> <span class="applies">applies to: group, raw</span></p><div class="formula">\[C_D(S)=\bigl|N(S)\bigr|=\bigl|\{v\notin S:\ \exists u\in S,\ \{u,v\}\in E\}\bigr|\]</div><p class="formula-where">Number of non-members that are adjacent to the group. Members are not counted; each non-member counts once however many members it is adjacent to.</p></div>

<div class="formula-block"><p class="formula-name"><strong>Normalized group degree</strong> <span class="applies">applies to: group, normalized</span></p><div class="formula">\[C_D'(S)=\frac{C_D(S)}{n-|S|}\]</div><p class="formula-where">Share of the non-members reached; needs \(|S|&lt;n\).</p></div>

## Variants {#concept-variants}

<div class="table-wrapper"><table class="variants"><thead><tr><th>Variant</th><th>Measure id</th><th>Tools</th><th>What changes</th></tr></thead><tbody><tr><td><a href="#group-degree">Group / degree</a></td><td><code>group:degree</code></td><td>3</td><td>The formulas above for undirected or in-direction adjacency.</td></tr><tr><td><a href="#cat_degree_group_out">Group out degree centrality</a></td><td><code>cat_degree_group_out</code></td><td>1</td><td>The directed version that counts non-members reached by an edge from a group member (out-direction).</td></tr></tbody></table></div>

## Edge cases {#concept-edge-cases}

<div class="table-wrapper edge-wrap"><table class="edge-cases"><thead><tr><th>Case</th><th>The published definition gives</th><th><a href="../../tools/networkx.html">NetworkX</a></th><th><a href="../../tools/networkit.html">NetworKit</a></th><th><a href="../../tools/rustworkx.html">rustworkx</a></th></tr></thead><tbody><tr><td title="A group, source set, target set or sample that is empty, a single node, or the whole node set."><strong>Degenerate group or subset input</strong></td><td class="def">Empty group: value 0. Group equal to all nodes: no non-members, the normalized form is 0/0 and the raw value 0. A one-node network: the single node is the whole group, so there are no non-members.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="An edge whose source and target are the same node."><strong>Self-loops</strong></td><td class="def">A loop joins a member to itself, a member; it adds no non-member.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="Several edges with the same source and target (same endpoints, for undirected edges)."><strong>Parallel edges</strong></td><td class="def">Parallel edges do not change which non-members are adjacent; the count is of nodes.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="The same measure applied to an undirected graph (each edge usable both ways) and to a directed graph (edges usable from source to target only), including which degree or distance direction is scored."><strong>Undirected versus directed input</strong></td><td class="def">Out version: non-members reached from the group; in version: non-members that reach the group.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="At least one node has no edge to any other node (degree 0), in a graph that has other edges."><strong>Isolated nodes</strong></td><td class="def">An isolated non-member is never adjacent to the group and is not counted.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr><tr><td title="One centre joined to every other node and no other edges."><strong>Star</strong></td><td class="def">The centre alone: \(n-1\), normalized 1; one leaf alone: 1.</td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td><td><span class="nr" title="The sources do not record this tool&#x27;s behaviour on this input.">not recorded</span></td></tr></tbody></table></div>

**Behaviour by case.** What each tool does, as observed (run entries) or documented (documented entries), with the source of the statement.

<div class="edge-details"><details><summary>Degenerate group or subset input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Self-loops</summary><ul><li>No tool entries.</li></ul></details><details><summary>Parallel edges</summary><ul><li>No tool entries.</li></ul></details><details><summary>Undirected versus directed input</summary><ul><li>No tool entries.</li></ul></details><details><summary>Isolated nodes</summary><ul><li>No tool entries.</li></ul></details><details><summary>Star</summary><ul><li>No tool entries.</li></ul></details></div>

## References {#concept-references}

[borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

## Group / degree {#group-degree}

Measure id: `group:degree`. Original family: Centrality.

**Definition.** Group degree, closeness or betweenness of a set of nodes (Everett and Borgatti).

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>group_degree_centrality; group_in_degree_centrality</code></td><td></td></tr><tr><td><a href="../../tools/networkit.html">NetworKit</a></td><td><a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a></td><td></td><td><code>GroupDegree</code></td><td></td></tr><tr><td><a href="../../tools/rustworkx.html">rustworkx</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-group-degree-rustworkx">details</a></td><td><code>digraph_group_degree_centrality; graph_group_degree_centrality; group_degree_centrality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-group-degree-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: digraph\_group\_degree\_centrality; graph\_group\_degree\_centrality; group\_degree\_centrality.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

<div class="table-wrapper"><table><thead><tr><th>Variant</th><th>Tool</th><th>Scope</th><th>Outcome</th><th>Differs when</th><th>Conventions</th><th>Tolerance</th><th>Call</th><th>Note</th></tr></thead><tbody><tr><td><code>group_degree</code></td><td>NetworkX</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.group_degree_centrality(G, C) (out-neighbours in directed graphs: nx.group_out_degree_centrality)</code></td><td>The group is the only node, so there are no non-members (division by zero).</td></tr><tr><td><code>group_degree</code></td><td>NetworKit</td><td>any</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nk.centrality.GroupDegree(G, k = 3, countGroupNodes = False).scoreOfGroup(S) / (n - |S|)</code></td><td></td></tr><tr><td><code>group_degree_all</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.group_degree_centrality(G.to_undirected(), C)</code></td><td></td></tr><tr><td><code>group_degree_in</code></td><td>NetworkX</td><td>directed</td><td>agrees</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nx.group_in_degree_centrality(G, C)</code></td><td></td></tr><tr><td><code>group_degree_in</code></td><td>NetworKit</td><td>directed</td><td>no-value-on-some-inputs</td><td></td><td></td><td>abs 0, rel 1e-14</td><td><code>nk.centrality.GroupDegree(reversed G, k = 3, countGroupNodes = False).scoreOfGroup(S) / (n - |S|)</code></td><td></td></tr></tbody></table></div>

**References:** [borgatti2006identifying](../../references.html#borgatti2006identifying), [brandes2008variants](../../references.html#brandes2008variants), [dinic1970algorithm](../../references.html#dinic1970algorithm), [everett1999centrality](../../references.html#everett1999centrality), [everton2012disrupting](../../references.html#everton2012disrupting), [ford1956maximal](../../references.html#ford1956maximal), [freeman1991centrality](../../references.html#freeman1991centrality), [koschutzki2005centrality](../../references.html#koschutzki2005centrality)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Group out degree centrality {#cat_degree_group_out}

Measure id: `cat_degree_group_out`. Original family: Centrality.

**Definition.** Group out degree centrality.

**Implementations**

<div class="table-wrapper"><table><thead><tr><th>Tool</th><th>State</th><th>Why, if not agrees</th><th>API names</th><th>Source</th></tr></thead><tbody><tr><td><a href="../../tools/networkx.html">NetworkX</a></td><td><a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a></td><td>Not run: listed in the tool's public API listing; no comparison set up for this measure yet. <a href="#why-cat_degree_group_out-networkx">details</a></td><td><code>group_out_degree_centrality</code></td><td>API listing</td></tr></tbody></table></div>

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_degree_group_out-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworkX 3.7 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (networkx public API (algorithms, generators, linalg, readwrite)); API names: group\_out\_degree\_centrality.

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
