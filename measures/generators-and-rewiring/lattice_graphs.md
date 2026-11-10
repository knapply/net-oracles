---
title: "Lattice graphs"
layout: default
parent: "Generators and rewiring"
grand_parent: Measures
nav_exclude: true
---

{% raw %}

# Lattice graphs {#concept-top}

Family: [Generators and rewiring](index.html). Subfamily: Small-world, lattice and geometric models. Concept id: `lattice_graphs`. 9 measures.

## Definition {#concept-definition}

Lattice graphs. Entries grouped here: Heavy hex graph; Heavy square graph; Hexagonal lattice graph; Lattice generator; Makeringlattice CIJ; Mesh graph; and 3 more.

## Variants {#concept-variants}

| Variant | Measure id | Tools |
|---|---|---|
| [Heavy hex graph](#cat_heavy_hex) | `cat_heavy_hex` | 1 |
| [Heavy square graph](#cat_heavy_square) | `cat_heavy_square` | 1 |
| [Hexagonal lattice graph](#cat_hexagonal_lattice) | `cat_hexagonal_lattice` | 3 |
| [Lattice generator](#gen_lattice) | `gen_lattice` | 6 |
| [Makeringlattice CIJ](#cat_cij_makeringlattice) | `cat_cij_makeringlattice` | 1 |
| [Mesh graph](#cat_mesh) | `cat_mesh` | 1 |
| [Mesh graph generator](#cat_generator_mesh) | `cat_generator_mesh` | 1 |
| [Regular Ring Lattice Generator](#cat_generator_lattice_regular_ring) | `cat_generator_lattice_regular_ring` | 1 |
| [Triangular lattice graph](#cat_lattice_triangular) | `cat_lattice_triangular` | 2 |

## Heavy hex graph {#cat_heavy_hex}

Measure id: `cat_heavy_hex`. Original family: Generators and rewiring.

**Definition.** Heavy hex graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_heavy_hex_graph; heavy_hex_graph` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Heavy square graph {#cat_heavy_square}

Measure id: `cat_heavy_square`. Original family: Generators and rewiring.

**Definition.** Heavy square graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_heavy_square_graph; heavy_square_graph` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Hexagonal lattice graph {#cat_hexagonal_lattice}

Measure id: `cat_hexagonal_lattice`. Original family: Generators and rewiring.

**Definition.** Hexagonal lattice graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `hexagonal_lattice_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Hexagonal_Lattice` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_hexagonal_lattice_graph; hexagonal_lattice_graph` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [tool_rustworkx](../../references.html#tool_rustworkx)

## Lattice generator {#gen_lattice}

Measure id: `gen_lattice`. Original family: Generators and rewiring.

**Definition.** Lattice generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `grid_2d_graph; grid_graph; lattice_reference` | documentation |
| [igraph (R)](../../tools/igraph.html) | · reported in docs | `lattice; make_lattice` | documentation |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Lattice` | API listing |
| [graph-tool](../../tools/graphtool.html) | · reported in docs | `lattice` | API listing |
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_grid_graph; grid_graph` | API listing |
| [JGraphT](../../tools/jgrapht.html) | · reported in docs | `GridGraphGenerator` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring), [michail2020jgrapht](../../references.html#michail2020jgrapht), [peixoto2014graphtool](../../references.html#peixoto2014graphtool), [tool_rustworkx](../../references.html#tool_rustworkx)

## Makeringlattice CIJ {#cat_cij_makeringlattice}

Measure id: `cat_cij_makeringlattice`. Original family: Generators and rewiring.

**Definition.** Makeringlattice CIJ.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [BCT (Octave)](../../tools/bct.html) | · reported in docs | `makeringlatticeCIJ` | API listing |

**Tools cited:** [rubinov2010complex](../../references.html#rubinov2010complex)

## Mesh graph {#cat_mesh}

Measure id: `cat_mesh`. Original family: Generators and rewiring.

**Definition.** Mesh graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [rustworkx](../../tools/rustworkx.html) | · reported in docs | `directed_mesh_graph; mesh_graph` | API listing |

**Tools cited:** [tool_rustworkx](../../references.html#tool_rustworkx)

## Mesh graph generator {#cat_generator_mesh}

Measure id: `cat_generator_mesh`. Original family: Generators and rewiring.

**Definition.** Mesh graph generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [Boost Graph Library](../../tools/boost.html) | · reported in docs | `mesh_graph_generator` | API listing |

**Tools cited:** [siek2002boost](../../references.html#siek2002boost)

## Regular Ring Lattice Generator {#cat_generator_lattice_regular_ring}

Measure id: `cat_generator_lattice_regular_ring`. Original family: Generators and rewiring.

**Definition.** Regular Ring Lattice Generator.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworKit](../../tools/networkit.html) | · reported in docs | `RegularRingLatticeGenerator` | API listing |

**Tools cited:** [staudt2016networkit](../../references.html#staudt2016networkit)

## Triangular lattice graph {#cat_lattice_triangular}

Measure id: `cat_lattice_triangular`. Original family: Generators and rewiring.

**Definition.** Triangular lattice graph.

**Implementations**

| Tool | State | API names | Source |
|---|---|---|---|
| [NetworkX](../../tools/networkx.html) | · reported in docs | `triangular_lattice_graph` | API listing |
| [igraph (Python)](../../tools/pyigraph.html) | · reported in docs | `Triangular_Lattice` | API listing |

**Tools cited:** [csardi2006igraph](../../references.html#csardi2006igraph), [hagberg2008exploring](../../references.html#hagberg2008exploring)
{% endraw %}
