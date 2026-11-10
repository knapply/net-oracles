---
title: "Planarity test"
layout: default
parent: "Graph theory and combinatorics"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Planarity test {#concept-top}

Family: [Graph theory and combinatorics](index.html). Subfamily: Planarity. Concept id: `planarity_test`. 2 measures.

## Definition {#concept-definition}

Planarity test. Entries grouped here: Planar; Planarity testing, embedding and straight-line drawing.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Planar](#st_planar) | `st_planar` | 4 |
| [Planarity testing, embedding and straight-line drawing](#planarity) | `planarity` | 3 |

## Planar {#st_planar}

Measure id: `st_planar`. Original family: Graph theory and combinatorics.

**Definition.** Planar.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | ✓ checked, agrees | `PlanarEmbedding; check_planarity; is_planar` |  |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `is_planar` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `is_planar` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `boyer_myrvold_planarity_test` | API listing |

**Conventions and tolerances.** Tolerance is the bound used when comparing a tool's values with the reference value: `abs` and `rel` (0 means exact).

| Variant | Tool | Scope | Outcome | Differs when | Conventions | Tolerance | Call | Note |
|---|---|---|---|---|---|---|---|---|
| `st_planar` | NetworkX | any | agrees |  |  | abs 0, rel 0 | `nx.is_planar(G)` |  |

**Tools cited:** [hagberg2008exploring](../../references.html#hagberg2008exploring), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost), [tool_rustworkx](../../references.html#tool_rustworkx)

## Planarity testing, embedding and straight-line drawing {#planarity}

Measure id: `planarity`. Original family: Graph theory and combinatorics.

**Definition.** Planarity testing, embedding and straight-line drawing.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `make_maximal_planar` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `BoyerMyrvoldPlanarityInspector` | API listing |
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `chrobak_payne_straight_line_drawing; is_kuratowski_subgraph; is_straight_line_drawing; make_biconnected_planar; make_maximal_planar; planar_canonical_ordering; planar_face_traversal` | API listing |

**Tools cited:** [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [siek2002boost](../../references.html#siek2002boost)
{% endraw %}
