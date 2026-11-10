---
title: "Strength (weighted degree)"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Strength (weighted degree) {#concept-top}

Family: [Centrality](index.html). Subfamily: Degree and strength. Concept id: `strength`. 1 measure.

## Definition {#concept-definition}

Strength (weighted degree). Entries grouped here: Strength.

## Strength {#strength}

Measure id: `strength`. Original family: Centrality.

**Definition.** Strength.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees |  |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `strength` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `strength` |  |
| [NetworKit](../../tools/networkit.html) | ∅ checked, no value on some inputs |  |  |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees | `WeightedDegree` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs |  | published documentation |
| [tnet](../../tools/tnet.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `strength_all` | NetworkX | any | agrees |  |  | abs 1e-12, rel 1e-12 | `G.degree(weight = 'weight')` |  |
| `strength_all` | igraph (R) | any | agrees |  |  | abs 1e-12, rel 1e-12 | `igraph::strength(g, mode = 'all', loops = TRUE)` |  |
| `strength_all` | igraph (Python) | any | agrees |  |  | abs 1e-12, rel 1e-12 | `python-igraph: g.strength(mode="all", loops=True, weights=w)` |  |
| `strength_all` | NetworKit | any | no-value-on-some-inputs |  |  | abs 1e-12, rel 1e-12 | `G.weightedDegree(v, countSelfLoopsTwice = True)` |  |
| `strength_all` | Gephi toolkit | any | agrees |  |  | abs 1e-12, rel 1e-12 | `Gephi toolkit 0.11.3: WeightedDegree.execute(graphModel), node column 'weighted degree'` |  |
| `strength_all` | tnet | any | differs | isolates, loops, zero\_weights | defaults, direction, self\_loops, ties, weights | abs 1e-12, rel 1e-12 | `tnet::degree_w(net, measure = 'output') (out + in when directed), loops dropped, parallel edges summed` | tnet drops self-loops from the strength (two nodes, one edge and a loop at a node, all of weight 1: tnet 1, where the reference counts an undirected loop at both ends, 3), and reports NaN for a node without ties (the reference 0), which includes a node whose only ties have weight 0 (tnet drops zero-weight ties, so the node has none left). |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F069](../../findings.html#f069) | NetworKit | convention | weightedDegree counts out-edges only; a single node gets 0 |

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [opsahl2010node](../../references.html#opsahl2010node), [staudt2016networkit](../../references.html#staudt2016networkit)
{% endraw %}
