---
title: "Bridges"
layout: default
parent: "Components and connectivity"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Bridges {#concept-top}

Family: [Components and connectivity](index.html). Subfamily: Articulation points, bridges and biconnected components. Concept id: `bridges`. 1 measure.

## Definition {#concept-definition}

Bridges. Entries grouped here: Bridges.

## Bridges {#bridges}

Measure id: `bridges`. Original family: Components and connectivity.

**Definition.** Bridges.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bridges; has_bridges; local_bridges` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bridges` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-bridges-pyigraph) | `bridges` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `bridges` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-bridges-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: bridges.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `bridges` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.bridges(nx.MultiGraph of the network)` |  |
| `bridges` | igraph (R) | any | no-value-on-some-inputs |  | direction, multi\_edges | abs 0, rel 0 | `igraph::ends(u, igraph::bridges(u)) with u = as_undirected(g, mode = 'each')` | The undirected reading of these networks has parallel edges (or arcs in both directions), and igraph's documentation does not say how bridges() treats them, so it is compared only where there are none. |
| `bridges` | rustworkx | any | differs | multi\_edges, (no value) directed | direction, multi\_edges | abs 0, rel 0 | `rx.bridges(G)` | Two parallel edges between the same nodes are never a bridge for the reference (removing one leaves the other); rx.bridges() reads the multigraph as a simple graph and reports the pair as a bridge. rx.bridges() accepts only an undirected PyGraph. |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
