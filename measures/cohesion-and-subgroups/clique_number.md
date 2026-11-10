---
title: "Clique number"
layout: default
parent: "Cohesion and subgroups"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Clique number {#concept-top}

Family: [Cohesion and subgroups](index.html). Subfamily: Cliques. Concept id: `clique_number`. 2 measures.

## Definition {#concept-definition}

Size of the largest clique.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Clique number](#clique_number) | `clique_number` | 5 |
| [Node clique number](#node_clique_number) | `node_clique_number` | 1 |

## References {#concept-references}

[bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

## Clique number {#clique_number}

Measure id: `clique_number`. Original family: Cohesion and subgroups.

**Definition.** Size of the largest clique.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `max_clique; max_weight_clique; node_clique_number; number_of_cliques` |  |
| [igraph (R)](../../tools/igraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `clique_num; weighted_clique_num` |  |
| [igraph (Python)](../../tools/pyigraph.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  | `clique_number` |  |
| [NetworKit](../../tools/networkit.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |
| [JGraphT](../../tools/jgrapht.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `clique_number` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `max(len(c) for c in nx.find_cliques(nx.Graph(G)))` |  |
| `clique_number` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::clique_num(g)` |  |
| `clique_number` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: [g.clique_number()]` |  |
| `clique_number` | NetworKit | any | agrees |  |  | abs 0, rel 0 | `max size in nk.clique.MaximalCliques(G simple undirected).getCliques()` |  |
| `clique_number` | JGraphT | any | no-value-on-some-inputs | (no value) directed, (no value) loops, (no value) multi\_edges | direction, multi\_edges, self\_loops | abs 0, rel 0 | `JGraphT 1.5.2: size of the largest BronKerboschCliqueFinder clique on a pseudograph` | BronKerboschCliqueFinder throws 'Graph must be simple' on loops or parallel edges; on directed input it does not error but returns a collection that is not the maximal cliques of the underlying graph (pair 0-&gt;1 gives two singletons, cycle7\_dir six cliques instead of seven edges), so it is not compared. |

**References:** [bron1973algorithm](../../references.html#bron1973algorithm), [eppstein2010listing](../../references.html#eppstein2010listing), [matula1983smallest](../../references.html#matula1983smallest), [tomita2006worst](../../references.html#tomita2006worst)

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [staudt2016networkit](../../references.html#staudt2016networkit)

## Node clique number {#node_clique_number}

Measure id: `node_clique_number`. Original family: Cohesion and subgroups.

**Definition.** Node clique number.

**Implementations**

| Tool | State | Why, if not agrees | API names | Source |
|---|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | <a class="st st-t st-ok" href="../../method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> |  |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `node_clique_number` | NetworkX | undirected | agrees |  |  | abs 0, rel 0 | `nx.node_clique_number(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
