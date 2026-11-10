---
title: "Degree"
layout: default
parent: "Centrality"
grand_parent: Measures
nav_exclude: true
---

{% raw %}
# Degree {#concept-top}

Family: [Centrality](index.html). Subfamily: Degree and strength. Concept id: `degree`. 3 measures.

## Definition {#concept-definition}

Degree of every node: edge endpoints by direction, loops counted twice.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Degree](#degree) | `degree` | 12 |
| [Degree simple](#degree_simple) | `degree_simple` | 1 |
| [Twomode / degree](#twomode-degree) | `twomode:degree` | 3 |

## References {#concept-references}

[lanczos1950iteration](../../references.html#lanczos1950iteration), [newman2006modularity](../../references.html#newman2006modularity), [wu2000thick](../../references.html#wu2000thick)

## Degree {#degree}

Measure id: `degree`. Original family: Descriptive statistics.

**Definition.** Degree of every node: edge endpoints by direction, loops counted twice.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `degree_centrality; degrees; in_degree_centrality; out_degree_centrality` |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs | `degree; degree_distribution` |  |
| [igraph (Python)](../../tools/pyigraph.html) | ✓ checked, agrees | `degree; degree_distribution; mean_degree` |  |
| [sna](../../tools/sna.html) | ≠ checked, differs by convention | `degree` |  |
| [ergm (statnet)](../../tools/ergm.html) | · reported in docs | `degree` | API listing |
| [NetworKit](../../tools/networkit.html) | ✓ checked, agrees | `DegreeCentrality; degreeDistribution` |  |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `degree_centrality; digraph_degree_centrality; graph_degree_centrality; in_degree_centrality; out_degree_centrality` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `degree_centrality` | API listing |
| [BCT (Octave)](../../tools/bct.html) | ≠ checked, differs by convention | `degrees_dir; degrees_und; strengths_dir; strengths_und; strengths_und_sign` |  |
| [Gephi toolkit](../../tools/gephi.html) | ✓ checked, agrees | `Degree` |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `Degree (Freeman), in/out, normalized, centralization; degree; indeg; outdeg` | published documentation |
| [tnet](../../tools/tnet.html) | · reported in docs | `degree_tm; degree_w` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `degree_all` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `MultiGraph/MultiDiGraph G.degree()` |  |
| `degree_all` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::degree(g, mode = 'all', loops = TRUE)` |  |
| `degree_all` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: g.degree(mode="all", loops=True)` |  |
| `degree_all` | sna | any | differs | loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0, rel 0 | `sna::degree(m, gmode, cmode = 'freeman' \| 'indegree' for graphs)` | sna works on adjacency matrices, so parallel edges collapse to one, and it ignores the diagonal by default (diag = FALSE). |
| `degree_all` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `G.degree(v) (undirected) or G.degreeIn(v) + G.degreeOut(v), fixture edges added one by one` |  |
| `degree_all` | Gephi toolkit | any | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: Degree.execute(graphModel), node column 'degree'` |  |
| `degree_all_noloops` | igraph (R) | any | agrees |  |  | abs 0, rel 0 | `igraph::degree(g, mode = 'all', loops = FALSE)` |  |
| `degree_all_noloops` | igraph (Python) | any | agrees |  |  | abs 0, rel 0 | `python-igraph: g.degree(mode="all", loops=False)` |  |
| `degree_all_noloops` | sna | any | differs | multi\_edges | multi\_edges | abs 0, rel 0 | `sna::degree(m, gmode, diag = FALSE)` | sna works on adjacency matrices, so parallel edges collapse to one. |
| `degree_all_noloops` | NetworKit | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `G.removeSelfLoops(); G.degree(v) or G.degreeIn(v) + G.degreeOut(v)` |  |
| `degree_all_noloops` | BCT (Octave) | any | differs |  | direction, multi\_edges, self\_loops, ties | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: degrees_und / degrees_dir (in + out), on the binary adjacency matrix without loops or parallel edges` | A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. |
| `degree_documented` | UCINET | any | documented |  | multi\_edges, self\_loops | abs 0, rel 0 | `Documented behaviour (not run)` | Degree is read from the adjacency matrix: parallel edges collapse and the diagonal is ignored. |
| `degree_in` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `MultiDiGraph G.in_degree()` |  |
| `degree_in` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::degree(g, mode = 'in', loops = TRUE)` |  |
| `degree_in` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: g.degree(mode="in", loops=True)` |  |
| `degree_in` | sna | directed | differs | loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0, rel 0 | `sna::degree(m, cmode = 'indegree')` | sna collapses parallel edges and ignores the diagonal by default. |
| `degree_in` | NetworKit | directed | agrees |  |  | abs 0, rel 0 | `G.degreeIn(v)` |  |
| `degree_in` | BCT (Octave) | directed | differs |  | direction, multi\_edges, self\_loops, ties | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: degrees_dir, on the binary adjacency matrix without loops or parallel edges` | A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. |
| `degree_in` | Gephi toolkit | directed | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: Degree.execute(graphModel), node column 'indegree'` |  |
| `degree_out` | NetworkX | directed | agrees |  |  | abs 0, rel 0 | `MultiDiGraph G.out_degree()` |  |
| `degree_out` | igraph (R) | directed | agrees |  |  | abs 0, rel 0 | `igraph::degree(g, mode = 'out', loops = TRUE)` |  |
| `degree_out` | igraph (Python) | directed | agrees |  |  | abs 0, rel 0 | `python-igraph: g.degree(mode="out", loops=True)` |  |
| `degree_out` | sna | directed | differs | loops, multi\_edges | defaults, multi\_edges, self\_loops | abs 0, rel 0 | `sna::degree(m, cmode = 'outdegree')` | sna collapses parallel edges and ignores the diagonal by default. |
| `degree_out` | NetworKit | directed | agrees |  |  | abs 0, rel 0 | `G.degreeOut(v)` |  |
| `degree_out` | BCT (Octave) | directed | differs |  | direction, multi\_edges, self\_loops, ties | abs 0, rel 0 | `Brain Connectivity Toolbox 2019-03-03 in Octave: degrees_dir, on the binary adjacency matrix without loops or parallel edges` | A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops, while the reference counts every edge. |
| `degree_out` | Gephi toolkit | directed | agrees |  |  | abs 0, rel 0 | `Gephi toolkit 0.11.3: Degree.execute(graphModel), node column 'outdegree'` |  |

**Findings**

| Id | Tool | Kind | Title |
|---|---|---|---|
| [F020](../../findings.html#f020) | Gephi toolkit | convention | Degree counts a self-loop twice |
| [F042](../../findings.html#f042) | sna | convention | Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default |
| [F059](../../findings.html#f059) | BCT (Octave) | convention | Matrix-input calls carry no loops or parallel edges |
| [F065](../../findings.html#f065) | NetworKit | convention | Loops, parallel edges and directed input are counted differently |

**References:** [lanczos1950iteration](../../references.html#lanczos1950iteration), [newman2006modularity](../../references.html#newman2006modularity), [wu2000thick](../../references.html#wu2000thick)

**Tools cited:** [bastian2009gephi](../../references.html#bastian2009gephi), [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [butts2008sna](../../references.html#butts2008sna), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [hunter2008ergm](../../references.html#hunter2008ergm), [opsahl2010node](../../references.html#opsahl2010node), [rubinov2010complex](../../references.html#rubinov2010complex), [siek2002boost](../../references.html#siek2002boost), [staudt2016networkit](../../references.html#staudt2016networkit), [tool_rustworkx](../../references.html#tool_rustworkx)

## Degree simple {#degree_simple}

Measure id: `degree_simple`. Original family: Centrality.

**Definition.** Degree simple.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [sna](../../tools/sna.html) | ✓ checked, agrees |  |  |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `degree_sna` | sna | any | agrees |  |  | abs 0, rel 0 | `sna::degree(m, gmode, cmode = 'freeman' \| 'indegree')` |  |

**Tools cited:** [butts2008sna](../../references.html#butts2008sna)

## Twomode / degree {#twomode-degree}

Measure id: `twomode:degree`. Original family: Two-mode and bipartite.

**Definition.** Twomode / degree.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ∅ checked, no value on some inputs |  |  |
| [igraph (R)](../../tools/igraph.html) | ∅ checked, no value on some inputs |  |  |
| [UCINET](../../tools/ucinet.html) | · reported in docs | `2-mode centrality` | published documentation |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `twomode_degree` | NetworkX | any | no-value-on-some-inputs |  |  | abs 0, rel 1e-14 | `nx.bipartite.degree_centrality(G, first_mode_nodes)` | one-mode fixture (no node types) |
| `twomode_degree_raw` | igraph (R) | any | no-value-on-some-inputs |  |  | abs 0, rel 0 | `igraph::degree(simplify(g))` | one-mode fixture (no node types) |

**Tools cited:** [borgatti2002ucinet](../../references.html#borgatti2002ucinet), [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
