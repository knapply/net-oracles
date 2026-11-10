---
title: "Traversal, trees and DAGs"
layout: default
parent: Measures
has_children: true
nav_order: 20
permalink: /measures/traversal-trees-and-dags/
---

{% raw %}

# Traversal, trees and DAGs

82 measures in 46 concepts and 4 subfamilies. Each concept page has a section per measure (variant); the anchor of a section is the measure id (characters other than letters, digits, underscore, dot and hyphen become hyphens).

## DAGs and topological order

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [All topological orders](all_topological_orders.html) | 2 | 2 | Every topological order of a DAG, in the sequence of Knuth and Szwarcfiter's algorithm. |
| [Antichains and antichain width](antichains.html) | 2 | 1 | The width of a DAG: the size of a largest antichain (Dilworth), by a maximum matching on the reachability pairs. |
| [Aperiodicity](aperiodic.html) | 2 | 1 | Aperiodicity. Entries grouped here: Gb aperiodic; Gm aperiodic. |
| [CD index](cd_index.html) | 1 | 1 | CD index. Entries grouped here: CD index. |
| [Chain decomposition](chain_decomposition.html) | 2 | 2 | Chain decomposition. Entries grouped here: Chain count; Chain decomposition. |
| [Colliders](colliders.html) | 1 | 1 | Colliders. Entries grouped here: Colliders. |
| [DAG reachability](dag_reachability.html) | 1 | 1 | DAG reachability. Entries grouped here: Dag reachability. |
| [DAG test](is_dag.html) | 1 | 6 | DAG test. Entries grouped here: Is dag. |
| [Lexicographic topological sort](lexicographic_topological_sort.html) | 2 | 1 | Lexicographic topological sort. Entries grouped here: Lex topo; Lexicographic. |
| [Longest path in a DAG](dag_longest_path.html) | 7 | 2 | A longest path of a DAG and its length, by dynamic programming in topological order. |
| [Lowest common ancestor in DAGs](dag_lca.html) | 1 | 1 | Lowest common ancestor of each node pair in a DAG; pairs with no common ancestor get the none mark u32::MAX. |
| [Moral graph](moral_graph.html) | 1 | 1 | Moral graph. Entries grouped here: Moral edges. |
| [Topological generations](topological_generations.html) | 2 | 1 | Topological generations of a DAG: the roots, then the nodes all of whose parents are in earlier generations. |
| [Topological sort](topological_sort.html) | 1 | 6 | Topological sort. Entries grouped here: Topological sort. |
| [Transitive closure](transitive_closure.html) | 1 | 5 | The pairs (u, v) of the transitive closure, sorted by source then target. |
| [Transitive reduction](transitive_reduction.html) | 1 | 5 | The arcs of the transitive reduction of a DAG, sorted by source then target. |

## Spanning trees and branchings

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Capacitated minimum spanning tree](capacitated_spanning_tree.html) | 2 | 1 | Capacitated minimum spanning tree. Entries grouped here: Ahuja Orlin Sharma Capacitated Minimum Spanning Tree; Esau Williams Capacitated Minimum Spanning Tree. |
| [Common spanning trees of two graphs](common_spanning_trees.html) | 1 | 1 | Common spanning trees of two graphs. Entries grouped here: Two graphs common spanning trees. |
| [Maximum branching](maximum_branching.html) | 4 | 1 | Optimum branching or spanning arborescence of a directed network (Edmonds), as input edge positions and total weight. |
| [Minimum spanning tree](minimum_spanning_tree.html) | 3 | 8 | Minimum or maximum spanning forest of an undirected network, as input edge positions and total weight. |
| [Number of spanning trees](spanning_tree_count.html) | 1 | 1 | Number of spanning trees (arborescences rooted at the root for a directed network) by the matrix-tree theorem. |
| [Partition spanning tree](partition_spanning_tree.html) | 1 | 1 | Partition spanning tree. Entries grouped here: Partition spanning tree. |
| [Random spanning tree](random_spanning_tree.html) | 3 | 5 | A random spanning tree of a connected undirected network by Wilson's algorithm, as input edge positions. |
| [Steiner tree](steiner_tree.html) | 1 | 3 | Steiner tree. Entries grouped here: Steiner tree. |
| [Union maximum spanning forest](maximum_spanning_forest.html) | 1 | 1 | Union maximum spanning forest. Entries grouped here: Union Maximum Spanning Forest. |

## Traversal and orderings

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Breadth-first search](breadth_first_search.html) | 8 | 9 | Levels, parents and counts of a breadth-first search from one node (direction-optimizing). |
| [Depth-first search](depth_first_search.html) | 3 | 7 | Depth-first search. Entries grouped here: Dfs events; Dfs iterator; Edge dfs. |
| [Random walks](random_walks.html) | 2 | 6 | Random walks. Entries grouped here: Random walk generation and sampling; Random walks. |
| [Vertex orderings (max cardinality, degeneracy)](vertex_orderings.html) | 2 | 3 | Vertex orderings (max cardinality, degeneracy). Entries grouped here: Vertex orderings (max cardinality, degeneracy); Maximum cardinality search. |
| [Walk counts](walk_counts.html) | 1 | 2 | Walk counts. Entries grouped here: Walks. |

## Tree structure and enumeration

| Concept | Measures | Tools | Definition |
|---|---|---|---|
| [Binomial tree](binomial_tree.html) | 1 | 2 | Binomial tree. Entries grouped here: Binomial tree. |
| [Consensus tree](consensus_tree.html) | 1 | 1 | Consensus tree. Entries grouped here: Consensus tree. |
| [Heavy path decomposition](heavy_path_decomposition.html) | 1 | 1 | Heavy path decomposition. Entries grouped here: Heavy Path Decomposition. |
| [Hierarchy tree](hierarchy_tree.html) | 1 | 1 | Hierarchy tree. Entries grouped here: Get hierarchy tree. |
| [Join trees](join_trees.html) | 1 | 1 | Join trees. Entries grouped here: Join trees. |
| [Lowest common ancestor in trees](tree_lca.html) | 2 | 2 | Lowest common ancestor in trees. Entries grouped here: Tree lca; Nxs tree lca. |
| [Number of nonisomorphic trees](nonisomorphic_trees.html) | 1 | 1 | Number of nonisomorphic trees. Entries grouped here: Number of nonisomorphic trees. |
| [Predecessor tree](predecessor_tree.html) | 1 | 1 | Predecessor tree. Entries grouped here: Predecessor tree. |
| [Prufer sequences](prufer_sequence.html) | 2 | 4 | Prufer sequences. Entries grouped here: From prufer; Prufer. |
| [Random power-law trees](random_powerlaw_tree.html) | 2 | 1 | Random power-law trees. Entries grouped here: Random powerlaw tree; Random powerlaw tree sequence. |
| [Random rooted forests](random_rooted_forest.html) | 2 | 1 | Random rooted forests. Entries grouped here: Random labeled rooted forest; Random unlabeled rooted forest. |
| [Tree broadcast time and center](tree_broadcast.html) | 2 | 1 | Tree broadcast time and center. Entries grouped here: Broadcast time; Tree broadcast center. |
| [Tree centroid](tree_centroid.html) | 1 | 1 | Tree centroid. Entries grouped here: Tree centroid. |
| [Tree sampling divergence](tree_sampling_divergence.html) | 1 | 1 | Tree sampling divergence. Entries grouped here: Tree sampling divergence. |
| [Tree, forest and arborescence tests](forest_tests.html) | 1 | 3 | Tree, forest and arborescence tests. Entries grouped here: Forest flags. |
| [Unfold tree](tree_unfold.html) | 1 | 2 | Unfold tree. Entries grouped here: Unfold tree. |
{% endraw %}
