---
title: "Twomode / closeness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Twomode / closeness

Family: Two-mode and bipartite. Identifier: `twomode:closeness`.

## Definition

Closeness of every node in a two-mode network, normalized by the bounds of Borgatti and Everett (1997).

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ≠ checked, differs by convention |  |  |
| [igraph (R)](../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_closeness` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `nx.bipartite.closeness_centrality(G, first_mode_nodes, normalized = True)` | one-mode fixture (no node types) |
| `twomode_closeness_ignore` | NetworkX | any | differs | isolates, one\_node, (no value) onemode | defaults | abs 0, rel 1e-12 | `nx.bipartite.closeness_centrality(G, first_mode_nodes, normalized = False)` | One node, or a node that reaches nobody: no other node to be close to; the reference reports undefined, NetworkX 0. one-mode fixture (no node types) |
| `twomode_closeness_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-12 | `igraph::closeness(simplify(as.undirected(g)), normalized = FALSE)` | one-mode fixture (no node types) |

## References

[borgatti1997network](../references.html#borgatti1997network), [borgatti2011analyzing](../references.html#borgatti2011analyzing), [breiger1974duality](../references.html#breiger1974duality), [everett2013dual](../references.html#everett2013dual), [newman2001scientific](../references.html#newman2001scientific), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph), [hagberg2008exploring](../references.html#hagberg2008exploring)
{% endraw %}
