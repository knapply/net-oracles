---
title: "Cut points (articulation points)"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Cut points (articulation points) {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `cut_points`. 1 measure.

## Definition {#concept-definition}

Cut points (articulation points). Entries grouped here: Cut points.

## Cut points {#cut_points}

Measure id: `cut_points`. Original family: Components and connectivity.

**Definition.** Cut points.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `articulation_points` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `articulation_points` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `articulation_points` |  |
| [sna](../../tools/sna.html) | ✓ checked, agrees | `cutpoints` |  |
| [rustworkx](../../tools/rustworkx.html) | ✓ checked, agrees | `articulation_points` |  |
| [Boost Graph Library](../../tools/boost.html) | ✓ checked, agrees | `articulation_points` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `cutpoints` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cut_points` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.articulation_points(nx.MultiGraph of the network)` |  |
| `cut_points` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::articulation_points(simplify(as_undirected(g))), which does not depend on parallel edges` |  |
| `cut_points` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: sorted(float(v) for v in su.articulation_points()),` |  |
| `cut_points` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::cutpoints(symmetrized m without its diagonal, mode = 'graph')` |  |
| `cut_points` | rustworkx | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `rx.articulation_points(G)` | rx.articulation\_points() accepts only an undirected PyGraph. |
| `cut_points` | Boost Graph Library | any | no-value-on-some-inputs | (no value) directed | direction | abs 0, rel 0 | `Boost Graph Library articulation_points` | BGL's articulation\_points is defined for undirected graphs only; the driver does not call it on directed input. |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
