---
title: "Clique percolation communities"
layout: default
parent: "Communities"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Clique percolation communities {#concept-top}

Family: [Communities](index.html). Subfamily: Other detection algorithms. Concept id: `clique_percolation`. 2 measures.

## Definition {#concept-definition}

Clique percolation communities: unions of maximal cliques of at least k nodes that share k - 1 nodes.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Clique communities](#cat_clique_community) | `cat_clique_community` | 1 |
| [K clique](#cnx_k_clique) | `cnx_k_clique` | 1 |

## References {#concept-references}

[brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [girvan2002community](../../references.html#girvan2002community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

## Clique communities {#cat_clique_community}

Measure id: `cat_clique_community`. Original family: Communities.

**Definition.** Clique communities.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-cat_clique_community-bct) | `clique_communities` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cat_clique_community-bct"></a>**[BCT (Octave)](../../tools/bct.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. BCT (Octave) 2019-03-03 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (bctpy public functions (the Python port of the Brain Connectivity Toolbox function set)); API names: clique\_communities.

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## K clique {#cnx_k_clique}

Measure id: `cnx_k_clique`. Original family: Communities.

**Definition.** Clique percolation communities: unions of maximal cliques of at least k nodes that share k - 1 nodes.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `k_clique_communities` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_k_clique_communities` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.k_clique_communities(G, 3) on the simple undirected graph` |  |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [girvan2002community](../../references.html#girvan2002community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
