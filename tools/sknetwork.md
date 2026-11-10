---
title: "scikit-network"
layout: default
parent: Tools
---

{% raw %}

# scikit-network

| Field | Value |
|---|---|
| Identifier | `sknetwork` |
| Language | Python |
| Version tested | 0.33.0 |
| License | BSD-3-Clause |
| Homepage | <https://scikit-network.readthedocs.io> |
| Role | checked |
| Citation | [tool_sknetwork](../references.html#tool_sknetwork) |

## How it was run

Imported in CPython; algorithms called on sparse adjacency matrices.

Capabilities listed by introspection of scikit-network public classes and functions.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 2 |
| checked, differs by convention (≠) | 5 |
| reported in docs (·) | 37 |

## Measures

| Family | Subfamily | Concept | Measure (variant) | State | API names |
|---|---|---|---|---|---|
| Centrality | Betweenness, load and flow | [Betweenness](../measures/centrality/betweenness.html) | [Betweenness](../measures/centrality/betweenness.html#betweenness) | · reported in docs | `Betweenness` |
| Centrality | Distance-based | [Closeness](../measures/centrality/closeness.html) | [Closeness](../measures/centrality/closeness.html#closeness) | ≠ checked, differs by convention | `Closeness` |
| Centrality | Local and structural scores | [Diffusion centrality and diffusion degree](../measures/centrality/diffusion_centrality.html) | [Diffusion](../measures/centrality/diffusion_centrality.html#cat_diffusion) | · reported in docs | `Diffusion; diffusion` |
| Centrality | Spectral and walk-based | [HITS hubs and authorities](../measures/centrality/hits.html) | [Hits](../measures/centrality/hits.html#hits) | ≠ checked, differs by convention | `HITS` |
| Centrality | Spectral and walk-based | [Katz centrality](../measures/centrality/katz_centrality.html) | [Katz](../measures/centrality/katz_centrality.html#katz) | · reported in docs | `Katz` |
| Centrality | Spectral and walk-based | [PageRank](../measures/centrality/pagerank.html) | [Pagerank](../measures/centrality/pagerank.html#pagerank) | ≠ checked, differs by convention | `PageRank; get_pagerank` |
| Cohesion and subgroups | Cliques | [Maximal cliques](../measures/cohesion-and-subgroups/maximal_cliques.html) | [Max cliques](../measures/cohesion-and-subgroups/maximal_cliques.html#max_cliques) | · reported in docs | `count_cliques` |
| Cohesion and subgroups | Cores, trusses and cohesive blocks | [K-core decomposition](../measures/cohesion-and-subgroups/k_core.html) | [Coreness](../measures/cohesion-and-subgroups/k_core.html#coreness) | ≠ checked, differs by convention | `get_core_decomposition` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Leiden](../measures/communities/modularity_maximization.html#leiden) | · reported in docs | `Leiden` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain Hierarchy](../measures/communities/modularity_maximization.html#cat_hierarchy_louvain) | · reported in docs | `LouvainHierarchy` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain Iteration](../measures/communities/modularity_maximization.html#cat_iteration_louvain) | · reported in docs | `LouvainIteration` |
| Communities | Modularity-based detection | [Modularity maximization (Louvain, Leiden, greedy, spectral, exact)](../measures/communities/modularity_maximization.html) | [Louvain modularity](../measures/communities/modularity_maximization.html#louvain_modularity) | · reported in docs | `Louvain` |
| Communities | Other detection algorithms | [Dasgupta cost and score](../measures/communities/dasgupta_cost.html) | [Dasgupta cost](../measures/communities/dasgupta_cost.html#cat_cost_dasgupta) | · reported in docs | `dasgupta_cost` |
| Communities | Other detection algorithms | [Dasgupta cost and score](../measures/communities/dasgupta_cost.html) | [Dasgupta score](../measures/communities/dasgupta_cost.html#cat_dasgupta) | · reported in docs | `dasgupta_score` |
| Communities | Other detection algorithms | [Label propagation](../measures/communities/label_propagation.html) | [Label propagation](../measures/communities/label_propagation.html#label_propagation) | · reported in docs | `PropagationClustering` |
| Communities | Other detection algorithms | [Paris hierarchical clustering](../measures/communities/paris.html) | [Paris](../measures/communities/paris.html#cat_paris) | · reported in docs | `Paris` |
| Communities | Partition and cover quality | [Modularity](../measures/communities/modularity.html) | [Modularity](../measures/communities/modularity.html#modularity) | ≠ checked, differs by convention | `get_modularity` |
| Components and connectivity | Connected components | [Connected components](../measures/components-and-connectivity/connected_components.html) | [Components](../measures/components-and-connectivity/connected_components.html#components) | ✓ checked, agrees | `get_connected_components; get_largest_connected_component; is_connected` |
| Descriptive statistics | Clustering and transitivity | [Local clustering coefficient](../measures/descriptive-statistics/local_clustering.html) | [Clustering](../measures/descriptive-statistics/local_clustering.html#clustering) | · reported in docs | `get_clustering_coefficient` |
| Descriptive statistics | Clustering and transitivity | [Triangle count](../measures/descriptive-statistics/triangle_count.html) | [Triangles](../measures/descriptive-statistics/triangle_count.html#nxo_triangles) | · reported in docs | `count_triangles` |
| Graph theory and combinatorics | Coloring | [Bipartite coloring and test](../measures/graph-theory-and-combinatorics/bipartite_coloring.html) | [Bipartite color](../measures/graph-theory-and-combinatorics/bipartite_coloring.html#bipartite_color) | · reported in docs | `is_bipartite` |
| Graph theory and combinatorics | Cycles | [Feedback arc and vertex sets](../measures/graph-theory-and-combinatorics/feedback_sets.html) | [Break cycles](../measures/graph-theory-and-combinatorics/feedback_sets.html#cat_break_cycle) | · reported in docs | `break_cycles` |
| Graph theory and combinatorics | Cycles | [Find a cycle](../measures/graph-theory-and-combinatorics/find_cycle.html) | [Find cycle](../measures/graph-theory-and-combinatorics/find_cycle.html#find_cycle) | · reported in docs | `get_cycles` |
| Graph theory and combinatorics | Independent sets and approximation | [K-center and Gon heuristic](../measures/graph-theory-and-combinatorics/k_center.html) | [KCenters](../measures/graph-theory-and-combinatorics/k_center.html#cat_centers_k) | · reported in docs | `KCenters` |
| Graph theory and combinatorics | Isomorphism and subgraph matching | [Graph isomorphism](../measures/graph-theory-and-combinatorics/graph_isomorphism.html) | [Vf2pp](../measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) | · reported in docs | `are_isomorphic` |
| Graph theory and combinatorics | Isomorphism and subgraph matching | [Weisfeiler-Lehman graph and subgraph hash](../measures/graph-theory-and-combinatorics/isomorphism_hash.html) | [Wl hash](../measures/graph-theory-and-combinatorics/isomorphism_hash.html#wl_hash) | · reported in docs | `color_weisfeiler_lehman; weisfeiler_lehman_coloring` |
| Graph theory and combinatorics | Similarity and link prediction | [Link prediction scores](../measures/graph-theory-and-combinatorics/link_prediction.html) | [Link prediction](../measures/graph-theory-and-combinatorics/link_prediction.html#link_prediction) | · reported in docs | `NNLinker` |
| Layout | Embeddings | [Louvain embedding](../measures/layout/louvain_embedding.html) | [Louvain Embedding](../measures/layout/louvain_embedding.html#cat_embedding_louvain) | · reported in docs | `LouvainEmbedding` |
| Layout | Embeddings | [Spectral embedding and clustering](../measures/layout/spectral_embedding.html) | [Spectral](../measures/layout/spectral_embedding.html#cat_spectral) | · reported in docs | `Spectral` |
| Layout | Layout algorithms | [Force-directed layouts](../measures/layout/force_directed_layout.html) | [Fruchterman-Reingold layout](../measures/layout/force_directed_layout.html#layout_fruchterman_reingold) | · reported in docs | `ForceAtlas` |
| Layout | Layout algorithms | [Force-directed layouts](../measures/layout/force_directed_layout.html) | [Spring](../measures/layout/force_directed_layout.html#cat_spring) | · reported in docs | `Spring` |
| Matrices and spectra | Graph matrices | [Laplacian matrix](../measures/matrices-and-spectra/laplacian_matrix.html) | [Gm laplacian](../measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) | · reported in docs | `Laplacian` |
| Paths and distances | Shortest paths | [Geodesic distances](../measures/paths-and-distances/geodesic_distances.html) | [Distances](../measures/paths-and-distances/geodesic_distances.html#distances) | ✓ checked, agrees | `get_distances` |
| Paths and distances | Shortest paths | [Shortest paths (Dijkstra, Bellman-Ford, A\*, bidirectional)](../measures/paths-and-distances/shortest_paths.html) | [Paths sssp](../measures/paths-and-distances/shortest_paths.html#paths_sssp) | · reported in docs | `get_shortest_path` |
| Statistical fitting | Model fitting | [Dirichlet regression on graphs](../measures/statistical-fitting/dirichlet.html) | [Dirichlet](../measures/statistical-fitting/dirichlet.html#cat_dirichlet) | · reported in docs | `Dirichlet` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [Diffusion Classifier](../measures/statistical-fitting/node_classification.html#cat_classifier_diffusion) | · reported in docs | `DiffusionClassifier` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [GNNClassifier](../measures/statistical-fitting/node_classification.html#cat_classifier_gnn) | · reported in docs | `GNNClassifier` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [NNClassifier](../measures/statistical-fitting/node_classification.html#cat_classifier_nn) | · reported in docs | `NNClassifier` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [Page Rank Classifier](../measures/statistical-fitting/node_classification.html#cat_classifier_page_rank) | · reported in docs | `PageRankClassifier` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [Propagation](../measures/statistical-fitting/node_classification.html#cat_propagation) | · reported in docs | `Propagation` |
| Statistical fitting | Prediction and classification | [Node classification](../measures/statistical-fitting/node_classification.html) | [Rank Classifier](../measures/statistical-fitting/node_classification.html#cat_classifier_rank) | · reported in docs | `RankClassifier` |
| Traversal, trees and DAGs | DAGs and topological order | [DAG test](../measures/traversal-trees-and-dags/is_dag.html) | [Is dag](../measures/traversal-trees-and-dags/is_dag.html#is_dag) | · reported in docs | `is_acyclic` |
| Traversal, trees and DAGs | Traversal and orderings | [Breadth-first search](../measures/traversal-trees-and-dags/breadth_first_search.html) | [Bfs edges](../measures/traversal-trees-and-dags/breadth_first_search.html#trav_bfs_edges) | · reported in docs | `breadth_first_search` |
| Traversal, trees and DAGs | Tree structure and enumeration | [Tree sampling divergence](../measures/traversal-trees-and-dags/tree_sampling_divergence.html) | [Tree sampling divergence](../measures/traversal-trees-and-dags/tree_sampling_divergence.html#cat_divergence_sampling_tree) | · reported in docs | `tree_sampling_divergence` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F087](../findings.html#f087) | defect | PageRank restart vector departs from the definition |
{% endraw %}
