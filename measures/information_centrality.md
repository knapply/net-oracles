---
title: "Information centrality"
layout: default
parent: Measures
nav_exclude: true
---

{% raw %}
# Information centrality

Family: Centrality. Identifier: `information_centrality`.

## Definition

Stephenson and Zelen's information centrality of every node.

## Implementations

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../tools/networkx.html) | ✓ checked, agrees |  |  |
| [sna](../tools/sna.html) | ≠ checked, differs by convention | `infocent` |  |
| [UCINET](../tools/ucinet.html) | · reported in docs | `Information centrality (fails on singular input)` | published documentation |
| [netrankr](../tools/netrankr.html) | ✓ checked, agrees |  |  |

## Conventions and tolerances

Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `information_centrality` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 1e-14, rel 1e-12 | `n * nx.information_centrality(Graph) (NetworkX returns I_i / n)` | NetworkX refuses graphs that are not connected (an isolate disconnects them) and a one-node graph. |
| `information_centrality` | sna | any | differs | disconnected, loops, multi\_edges | defaults, multi\_edges, self\_loops, ties | abs 1e-14, rel 1e-12 | `sna::infocent(m, gmode, cmode = 'weak')` | On networks with more than one component sna's results differ from Stephenson and Zelen's formula as evaluated exactly by the definition oracle, which agrees with this reference. sna reads the network as an adjacency matrix, so parallel edges collapse to one tie, while this reference counts each edge. sna::infocent() fails on networks with no ties, and its linear solve is singular when the network has an isolate. |
| `information_centrality` | netrankr | any | no-value-on-some-inputs | (no value) directed, (no value) disconnected | defaults, direction, weights | abs 1e-14, rel 1e-12 | `aggregate_positions(indirect_relations(g, 'dist_resist'), 'invsum')` | netrankr reads the network as undirected, unweighted and simple and has no value for a single node; its resistance distance (type = "dist\_resist") is defined only for connected graphs and raises an error otherwise. |
| `information_centrality_weighted` | NetworkX | any | no-value-on-some-inputs | (no value) disconnected | defaults | abs 1e-14, rel 1e-12 | `n * nx.information_centrality(Graph, weight = 'weight') with summed weights` | NetworkX refuses graphs that are not connected. |
| `information_centrality_weighted` | sna | any | differs | directed, disconnected | defaults, direction, ties, weights | abs 1e-14, rel 1e-12 | `sna::infocent(valued matrix, gmode, cmode = 'weak')` | For valued directed networks sna symmetrizes the tie values differently from this reference, and on disconnected networks its matrix is singular (sna's known behaviour on singular inputs); on connected undirected valued networks the two agree, and the definition oracle agrees with this reference throughout. |

## Findings

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F041](../findings.html#f041) | sna | defect | Information centrality fails on singular inputs |
| [F080](../findings.html#f080) | netrankr | convention | dist\_resist with invsum is the standard value divided by n |

## References

[borgatti2006identifying](../references.html#borgatti2006identifying), [brandes2005centrality](../references.html#brandes2005centrality), [brandes2008variants](../references.html#brandes2008variants), [butts2008sna](../references.html#butts2008sna), [freeman1977set](../references.html#freeman1977set), [girvan2002community](../references.html#girvan2002community), [hwang2008bridging](../references.html#hwang2008bridging), [stephenson1989rethinking](../references.html#stephenson1989rethinking)

Tools cited: [borgatti2002ucinet](../references.html#borgatti2002ucinet), [butts2008sna](../references.html#butts2008sna), [hagberg2008exploring](../references.html#hagberg2008exploring), [schoch2018centrality](../references.html#schoch2018centrality)
{% endraw %}
