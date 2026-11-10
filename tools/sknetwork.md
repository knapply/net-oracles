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

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Betweenness](../measures/betweenness.html) | · reported in docs | `Betweenness` |
| Centrality | [Closeness](../measures/closeness.html) | ≠ checked, differs by convention | `Closeness` |
| Centrality | [Diffusion](../measures/cat_diffusion.html) | · reported in docs | `Diffusion; diffusion` |
| Centrality | [Diffusion Classifier](../measures/cat_classifier_diffusion.html) | · reported in docs | `DiffusionClassifier` |
| Centrality | [Hits](../measures/hits.html) | ≠ checked, differs by convention | `HITS` |
| Centrality | [Katz](../measures/katz.html) | · reported in docs | `Katz` |
| Centrality | [Page Rank Classifier](../measures/cat_classifier_page_rank.html) | · reported in docs | `PageRankClassifier` |
| Centrality | [Pagerank](../measures/pagerank.html) | ≠ checked, differs by convention | `PageRank; get_pagerank` |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ≠ checked, differs by convention | `get_core_decomposition` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | · reported in docs | `count_cliques` |
| Communities | [Label propagation](../measures/label_propagation.html) | · reported in docs | `PropagationClustering` |
| Communities | [Leiden](../measures/leiden.html) | · reported in docs | `Leiden` |
| Communities | [Louvain Hierarchy](../measures/cat_hierarchy_louvain.html) | · reported in docs | `LouvainHierarchy` |
| Communities | [Louvain Iteration](../measures/cat_iteration_louvain.html) | · reported in docs | `LouvainIteration` |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs | `Louvain` |
| Communities | [Modularity](../measures/modularity.html) | ≠ checked, differs by convention | `get_modularity` |
| Descriptive statistics | [Clustering](../measures/clustering.html) | · reported in docs | `get_clustering_coefficient` |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `get_connected_components; get_largest_connected_component; is_connected` |
| Descriptive statistics | [Triangles](../measures/nxo_triangles.html) | · reported in docs | `count_triangles` |
| Graph theory and combinatorics | [Break cycles](../measures/cat_break_cycle.html) | · reported in docs | `break_cycles` |
| Graph theory and combinatorics | [Dasgupta cost](../measures/cat_cost_dasgupta.html) | · reported in docs | `dasgupta_cost` |
| Graph theory and combinatorics | [Dasgupta score](../measures/cat_dasgupta.html) | · reported in docs | `dasgupta_score` |
| Graph theory and combinatorics | [Dirichlet](../measures/cat_dirichlet.html) | · reported in docs | `Dirichlet` |
| Graph theory and combinatorics | [Find cycle](../measures/find_cycle.html) | · reported in docs | `get_cycles` |
| Graph theory and combinatorics | [KCenters](../measures/cat_centers_k.html) | · reported in docs | `KCenters` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `NNLinker` |
| Graph theory and combinatorics | [Paris](../measures/cat_paris.html) | · reported in docs | `Paris` |
| Graph theory and combinatorics | [Propagation](../measures/cat_propagation.html) | · reported in docs | `Propagation` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `are_isomorphic` |
| Graph theory and combinatorics | [Wl hash](../measures/wl_hash.html) | · reported in docs | `color_weisfeiler_lehman; weisfeiler_lehman_coloring` |
| Layout | [Fruchterman-Reingold layout](../measures/layout_fruchterman_reingold.html) | · reported in docs | `ForceAtlas` |
| Layout | [Louvain Embedding](../measures/cat_embedding_louvain.html) | · reported in docs | `LouvainEmbedding` |
| Layout | [Spring](../measures/cat_spring.html) | · reported in docs | `Spring` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `Laplacian` |
| Matrices and spectra | [Spectral](../measures/cat_spectral.html) | · reported in docs | `Spectral` |
| Mixing and assortativity | [GNNClassifier](../measures/cat_classifier_gnn.html) | · reported in docs | `GNNClassifier` |
| Mixing and assortativity | [NNClassifier](../measures/cat_classifier_nn.html) | · reported in docs | `NNClassifier` |
| Mixing and assortativity | [Rank Classifier](../measures/cat_classifier_rank.html) | · reported in docs | `RankClassifier` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `get_distances` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `get_shortest_path` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `breadth_first_search` |
| Traversal, trees and DAGs | [Is dag](../measures/is_dag.html) | · reported in docs | `is_acyclic` |
| Traversal, trees and DAGs | [Tree sampling divergence](../measures/cat_divergence_sampling_tree.html) | · reported in docs | `tree_sampling_divergence` |
| Two-mode and bipartite | [Bipartite color](../measures/bipartite_color.html) | · reported in docs | `is_bipartite` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F087](../findings.html#f087) | defect | PageRank restart vector departs from the definition |
{% endraw %}
