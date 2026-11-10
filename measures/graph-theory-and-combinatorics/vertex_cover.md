---
title: "Vertex cover"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Vertex cover {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Covers and dominating sets. Concept id: `vertex_cover`. 2 measures.

## Definition {#concept-definition}

Local-ratio vertex cover of least node cost (2-approximation), as node ids.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Vertex cover](#vertex_cover) | `vertex_cover` | 1 |
| [Ap vertex cover](#ap_vertex_cover) | `ap_vertex_cover` | 2 |

## References {#concept-references}

[baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

## Vertex cover {#vertex_cover}

Measure id: `vertex_cover`. Original family: Two-mode and bipartite.

**Definition.** Vertex cover.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `min_weighted_vertex_cover; to_vertex_cover` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `vertex_cover` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.bipartite.to_vertex_cover(G, nx.bipartite.hopcroft_karp_matching(G, top), top_nodes = top): (size, 1 if it covers every edge)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)

## Ap vertex cover {#ap_vertex_cover}

Measure id: `ap_vertex_cover`. Original family: Graph theory and combinatorics.

**Definition.** Local-ratio vertex cover of least node cost (2-approximation), as node ids.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-ap_vertex_cover-networkit) | `Cover` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-ap_vertex_cover-networkit"></a>**[NetworKit](../../tools/networkit.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. NetworKit 11.2.2 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (NetworKit public classes and functions); API names: Cover.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `ap_vertex_cover` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `sorted(nx.approximation.min_weighted_vertex_cover(G_sorted, weight = 'w')) with w(v) = v mod 4 + 1` |  |

**References:** [baryehuda1985local](../../references.html#baryehuda1985local), [bodlaender2010treewidth](../../references.html#bodlaender2010treewidth), [boob2020flowless](../../references.html#boob2020flowless), [boppana1992approximating](../../references.html#boppana1992approximating), [hagberg2008exploring](../../references.html#hagberg2008exploring), [vazirani2001approximation](../../references.html#vazirani2001approximation), [white2001fast](../../references.html#white2001fast)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
