---
title: "Flow betweenness"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Flow betweenness

Family: Centrality. Identifier: `flow_betweenness`.

## Definition

Flow betweenness of every node: the share of maximum flow between other pairs that cannot avoid it. The ucinet convention uses the normalized scale; UCINET's documentation does not define its normalization precisely, so the all\_pairs and max scales are offered as other readings.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../tools/sna.html) | ≠ checked, differs by convention | `flowbet` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs |  | published documentation |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `flow_betweenness` | sna | any | differs | multi\_edges | multi\_edges, ties | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode = 'digraph' \| 'graph', cmode = 'rawflow', ignore.eval = TRUE)` | sna reads an adjacency matrix, so parallel edges collapse into one tie of capacity 1; the reference adds their capacities. sna's flow routines need at least two nodes. |
| `flow_betweenness_capacity` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-09, rel 1e-09 | `sna::flowbet(m, gmode, cmode = 'rawflow') with the weights in the matrix` | sna keeps one value per pair of nodes. |
| `flow_betweenness_fractional` | sna | any | differs | multi\_edges | multi\_edges | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode, cmode = 'fracflow', ignore.eval = TRUE)` | sna collapses parallel edges. sna's flow routines need at least two nodes. |
| `flow_betweenness_normalized` | sna | any | differs | multi\_edges | defaults, multi\_edges, normalization | abs 1e-12, rel 1e-12 | `sna::flowbet(m, gmode, cmode = 'normflow', ignore.eval = TRUE)` | sna collapses parallel edges. No flow passes between pairs of other nodes, so the normalized score is 0/0; the reference reports NaN. |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2008variants](../references.html#brandes2008variants), [dinic1970algorithm](../references.html#dinic1970algorithm), [everett1999centrality](../references.html#everett1999centrality), [everton2012disrupting](../references.html#everton2012disrupting), [ford1956maximal](../references.html#ford1956maximal), [freeman1991centrality](../references.html#freeman1991centrality), [koschutzki2005centrality](../references.html#koschutzki2005centrality)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna)
{% endraw %}
