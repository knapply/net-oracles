---
title: "Dispersion"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Dispersion {#concept-top}

Family: [Centrality](index.html). Subfamily: Local and structural scores. Concept id: `dispersion`. 1 measure.

## Definition {#concept-definition}

Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair.

## References {#concept-references}

[qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

## Dispersion {#cx_dispersion}

Measure id: `cx_dispersion`. Original family: Centrality.

**Definition.** Dispersion of the tie between each given pair of nodes (Backstrom and Kleinberg), one value per pair.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> | Differs by convention (direction, self-loops and ties): On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair... [details](#why-cx_dispersion-networkx) | `dispersion` |  |

**Why these entries are not checked, agrees.** States are defined on [How entries are labelled](../../method.html).

- <a id="why-cx_dispersion-networkx"></a>**[NetworkX](../../tools/networkx.html)** <a class="st st-t st-conv" href="../../method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> NetworkX 3.7 was run and its value differs from the reference value by convention (direction, self-loops and ties) on inputs tagged directed and loops. On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. No mapping that reproduces the tool's value is recorded, so the entry was not compared after mapping. Tolerance before mapping: abs 1e-12, rel 1e-09 (0 means exact equality). 15 comparisons differ and 69 agree.

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `cx_dispersion` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G)[u][v] for every ordered pair of adjacent nodes` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |
| `cx_dispersion_params` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G, alpha = 2, b = 1, c = 0.5)` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |
| `cx_dispersion_raw` | NetworkX | any | differs | directed, loops | direction, self\_loops, ties | abs 1e-12, rel 1e-09 | `nx.dispersion(G, normalized = False)` | On directed networks, and at nodes with self-loops, NetworkX's pair test is not symmetric in the two common neighbors, and NetworkX takes each pair in the iteration order of a Python set of node labels; the reference takes the pair with the smaller node index first. On undirected networks without self-loops the test is symmetric and the values agree. |

**References:** [qi2012laplacian](../../references.html#qi2012laplacian), [zhang2016identifying](../../references.html#zhang2016identifying)

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
