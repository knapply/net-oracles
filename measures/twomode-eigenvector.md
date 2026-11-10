---
title: "Twomode / eigenvector"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Twomode / eigenvector

Family: Two-mode and bipartite. Identifier: `twomode:eigenvector`.

## Definition

Eigenvector centrality of a two-mode network: the leading singular vectors of the incidence matrix, each mode of length 1.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [igraph (R)](../tools/igraph.html) | ✓ checked, agrees |  |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_eigenvector` | igraph (R) | any | differs | edgeless, (no value) onemode | defaults | abs 1e-14, rel 1e-12 | `igraph::eigen_centrality(simplify(as.undirected(g)))$vector, each mode rescaled to unit length` | Without edges the leading eigenvector is not defined; the reference reports undefined, igraph a vector of ones. one-mode fixture (no node types) |

## References

[borgatti1997network](../references.html#borgatti1997network), [borgatti2011analyzing](../references.html#borgatti2011analyzing), [breiger1974duality](../references.html#breiger1974duality), [everett2013dual](../references.html#everett2013dual), [newman2001scientific](../references.html#newman2001scientific), [wasserman1994social](../references.html#wasserman1994social)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [csardi2006igraph](../references.html#csardi2006igraph)
{% endraw %}
