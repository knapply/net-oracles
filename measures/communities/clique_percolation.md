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

| Tool | State | API names | Source |
|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `clique_communities` | API listing |

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## K clique {#cnx_k_clique}

Measure id: `cnx_k_clique`. Original family: Communities.

**Definition.** Clique percolation communities: unions of maximal cliques of at least k nodes that share k - 1 nodes.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `k_clique_communities` |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `nx_k_clique_communities` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.community.k_clique_communities(G, 3) on the simple undirected graph` |  |

**References:** [brandes2001faster](../../references.html#brandes2001faster), [chen2014extension](../../references.html#chen2014extension), [clauset2004finding](../../references.html#clauset2004finding), [cordasco2010community](../../references.html#cordasco2010community), [fortunato2010community](../../references.html#fortunato2010community), [girvan2002community](../../references.html#girvan2002community), [hagberg2008exploring](../../references.html#hagberg2008exploring), [kernighan1970efficient](../../references.html#kernighan1970efficient)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
