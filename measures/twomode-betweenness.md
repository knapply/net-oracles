---
title: "Twomode / betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Twomode / betweenness

Family: Two-mode and bipartite. Identifier: `twomode:betweenness`.

## Definition

Betweenness of every node in a two-mode network, optionally divided by the largest possible value (Borgatti and Everett 1997).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_betweenness` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-09 | `nx.bipartite.betweenness_centrality(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `twomode_betweenness_raw` | NetworkX | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `nx.betweenness_centrality(G, normalized = False)` | one-mode fixture (no node types) |
| `twomode_betweenness_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 1e-09, rel 1e-09 | `igraph::betweenness(simplify(as.undirected(g)))` | one-mode fixture (no node types) |

## References

[borgatti1997network](../references.html#borgatti1997network), [borgatti2011analyzing](../references.html#borgatti2011analyzing), [breiger1974duality](../references.html#breiger1974duality), [everett2013dual](../references.html#everett2013dual), [newman2001scientific](../references.html#newman2001scientific), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
