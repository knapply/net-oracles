---
title: "All shortest paths"
layout: default
parent: "Paths and distances"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# All shortest paths {#concept-top}

Family: [Paths and distances](index.html). Subfamily: Shortest paths. Concept id: `all_shortest_paths`. 1 measure.

## Definition {#concept-definition}

All shortest paths. Entries grouped here: Paths all shortest.

## Paths all shortest {#paths_all_shortest}

Measure id: `paths_all_shortest`. Original family: Paths and distances.

**Definition.** Paths all shortest.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `all_shortest_paths` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_shortest-igraph) | `all_shortest_paths` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_shortest-pyigraph) | `get_all_shortest_paths` | API listing |
| [graph-tool](../../tools/graphtool.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_shortest-graphtool) | `all_shortest_paths` | API listing |
| [rustworkx](../../tools/rustworkx.html) | <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> | Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [details](#why-paths_all_shortest-rustworkx) | `all_shortest_paths; digraph_all_shortest_paths; digraph_num_shortest_paths_unweighted; graph_all_shortest_paths; graph_num_shortest_paths_unweighted; num_shortest_paths_unweighted` | API listing |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-paths_all_shortest-igraph"></a>**[igraph (R)](../../tools/igraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (R) 2.3.4 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (R package igraph: exported functions and help titles); API names: all\_shortest\_paths.
- <a id="why-paths_all_shortest-pyigraph"></a>**[igraph (Python)](../../tools/pyigraph.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. igraph (Python) 1.0.0 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (python-igraph Graph methods and module functions); API names: get\_all\_shortest\_paths.
- <a id="why-paths_all_shortest-graphtool"></a>**[graph-tool](../../tools/graphtool.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. graph-tool 3.9 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (graph-tool public classes and functions); API names: all\_shortest\_paths.
- <a id="why-paths_all_shortest-rustworkx"></a>**[rustworkx](../../tools/rustworkx.html)** <a class="st st-t st-docs" href="../../method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run for this measure. rustworkx 0.18.1 was run in this survey on other measures, but no comparison against the reference value has been set up for this one yet (not yet wired up). Documentation source: the tool's public API listing (rustworkx public functions and generators); API names: all\_shortest\_paths; digraph\_all\_shortest\_paths; digraph\_num\_shortest\_paths\_unweighted; graph\_all\_shortest\_paths; graph\_num\_shortest\_paths\_unweighted; num\_shortest\_paths\_unweighted.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `paths_all_shortest_unweighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.all_shortest_paths(G, 0, n - 1)) (none on NetworkXNoPath)` |  |
| `paths_all_shortest_weighted` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `list(nx.all_shortest_paths(G, 0, n - 1, weight = 'weight'))` |  |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [tool_rustworkx](../../references.html#tool_rustworkx)
{% endraw %}
