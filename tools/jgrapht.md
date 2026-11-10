---
title: "JGraphT"
layout: default
parent: Tools
---

{% raw %}
# JGraphT

| Field | Value |
|---|---|
| Identifier | `jgrapht` |
| Language | Java |
| Version tested | 1.5.2 |
| License | LGPL-2.1-or-later OR EPL-2.0 |
| Homepage | <https://jgrapht.org> |
| Role | checked |
| Citation | [michail2020jgrapht](../references.html#michail2020jgrapht) |

## How it was run

Driver programs in Java run against the released jar.

Capabilities listed by documentation of JGraphT 1.5.2 javadoc: all classes and interfaces (org.jgrapht.\*).

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 8 |
| checked, differs by convention (≠) | 8 |
| reported in docs (·) | 99 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Approximate betweenness (sampling)](../measures/betweenness_approx.html) | · reported in docs | `ApBetweennessCentrality` |
| Centrality | [Betweenness](../measures/betweenness.html) | ≠ checked, differs by convention | `BetweennessCentrality` |
| Centrality | [Closeness](../measures/closeness.html) | ≠ checked, differs by convention | `ClosenessCentrality` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | · reported in docs | `EdgeBetweennessCentrality` |
| Centrality | [Eigenvector](../measures/eigenvector.html) | · reported in docs | `EigenvectorCentrality` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees | `HarmonicCentrality` |
| Centrality | [Katz](../measures/katz.html) | · reported in docs | `KatzCentrality` |
| Centrality | [Pagerank](../measures/pagerank.html) | ✓ checked, agrees | `PageRank` |
| Cohesion and subgroups | [Clique number](../measures/clique_number.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ✓ checked, agrees | `Coreness` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | ✓ checked, agrees | `BronKerboschCliqueFinder; DegeneracyBronKerboschCliqueFinder; PivotBronKerboschCliqueFinder` |
| Communities | [Bipartite Partitioning](../measures/cat_bipartite_partitioning.html) | · reported in docs | `BipartitePartitioning` |
| Communities | [Dag All Paths Counter](../measures/cat_all_counter_dag_path.html) | · reported in docs | `DagAllPathsCounter` |
| Communities | [Girvan newman](../measures/girvan_newman.html) | · reported in docs | `GirvanNewmanClustering` |
| Communities | [Greedy modularity](../measures/cnx_greedy_modularity.html) | · reported in docs | `GreedyModularityAlgorithm` |
| Communities | [Label propagation](../measures/label_propagation.html) | · reported in docs | `LabelPropagationClustering` |
| Communities | [Modularity](../measures/modularity.html) | · reported in docs | `NaiveGreedyModularityAlgorithm; UndirectedModularityMeasurer` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | · reported in docs | `BiconnectivityInspector; BlockCutpointGraph` |
| Components and connectivity | [Capacity Scaling Minimum Cost Flow](../measures/cat_capacity_cost_flow_minimum_scaling.html) | · reported in docs | `CapacityScalingMinimumCostFlow` |
| Components and connectivity | [Disjoint paths](../measures/disjoint_paths.html) | · reported in docs | `BhandariKDisjointShortestPaths; SuurballeKDisjointShortestPaths` |
| Components and connectivity | [Gomory hu](../measures/gomory_hu.html) | · reported in docs | `GusfieldGomoryHuCutTree` |
| Components and connectivity | [Gusfield Equivalent Flow Tree](../measures/cat_equivalent_flow_gusfield_tree.html) | · reported in docs | `GusfieldEquivalentFlowTree` |
| Components and connectivity | [KConnectivity Flow Algorithm](../measures/cat_connectivity_flow_k.html) | · reported in docs | `KConnectivityFlowAlgorithm` |
| Components and connectivity | [Min cut](../measures/min_cut.html) | · reported in docs | `StoerWagnerMinimumCut` |
| Components and connectivity | [Padberg Rao Odd Minimum Cutset](../measures/cat_cutset_minimum_odd_padberg_rao.html) | · reported in docs | `PadbergRaoOddMinimumCutset` |
| Components and connectivity | [Strong partition](../measures/strong_partition.html) | ✓ checked, agrees | `GabowStrongConnectivityInspector; KosarajuStrongConnectivityInspector` |
| Components and connectivity | [Tree Dynamic Connectivity](../measures/cat_connectivity_dynamic_tree.html) | · reported in docs | `TreeDynamicConnectivity` |
| Data transforms | [Graph complement](../measures/graph_complement.html) | · reported in docs | `ComplementGraphGenerator` |
| Data transforms | [Line graph](../measures/line_graph.html) | · reported in docs | `LineGraphConverter` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ≠ checked, differs by convention |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ≠ checked, differs by convention | `ClusteringCoefficient` |
| Descriptive statistics | [Components](../measures/components.html) | · reported in docs | `ConnectivityInspector` |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ≠ checked, differs by convention |  |
| Generators and rewiring | [Deterministic generators](../measures/deterministic_generators.html) | · reported in docs | `CompleteBipartiteGraphGenerator; CompleteGraphGenerator; EmptyGraphGenerator; HyperCubeGraphGenerator; LinearGraphGenerator; RingGraphGenerator; StarGraphGenerator; WheelGraphGenerator` |
| Generators and rewiring | [G(n, m) random graph](../measures/gen_gnm.html) | · reported in docs | `GnmRandomGraphGenerator` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `GnpRandomGraphGenerator` |
| Generators and rewiring | [Generalized Petersen graph generator](../measures/gen_generalized_petersen.html) | · reported in docs | `GeneralizedPetersenGraphGenerator` |
| Generators and rewiring | [KSpanning Tree Clustering](../measures/cat_clustering_k_spanning_tree.html) | · reported in docs | `KSpanningTreeClustering` |
| Generators and rewiring | [Lattice generator](../measures/gen_lattice.html) | · reported in docs | `GridGraphGenerator` |
| Generators and rewiring | [Linearized Chord Diagram Graph Generator](../measures/cat_chord_diagram_generator_linearized.html) | · reported in docs | `LinearizedChordDiagramGraphGenerator` |
| Generators and rewiring | [Navigable small-world generator](../measures/gen_navigable_small_world.html) | · reported in docs | `KleinbergSmallWorldGraphGenerator` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `BarabasiAlbertForestGenerator; BarabasiAlbertGraphGenerator; DirectedScaleFreeGraphGenerator; ScaleFreeGraphGenerator` |
| Generators and rewiring | [Random bipartite graph generator](../measures/gen_random_bipartite.html) | · reported in docs | `GnmRandomBipartiteGraphGenerator; GnpRandomBipartiteGraphGenerator` |
| Generators and rewiring | [Random regular graph generator](../measures/gen_regular.html) | · reported in docs | `RandomRegularGraphGenerator` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `WattsStrogatzGraphGenerator` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `PlantedPartitionGraphGenerator` |
| Generators and rewiring | [Windmill graph generator](../measures/gen_windmill.html) | · reported in docs | `WindmillGraphsGenerator` |
| Graph theory and combinatorics | [Ahuja Orlin Sharma Cyclic Exchange Local Augmentation](../measures/cat_ahuja_augmentation_cyclic_exchange_local_orlin_sharma.html) | · reported in docs | `AhujaOrlinSharmaCyclicExchangeLocalAugmentation` |
| Graph theory and combinatorics | [Approximate and b-matching](../measures/matching_approx.html) | · reported in docs | `PathGrowingWeightedMatching` |
| Graph theory and combinatorics | [Chinese Postman](../measures/cat_chinese_postman.html) | · reported in docs | `ChinesePostman` |
| Graph theory and combinatorics | [Chordal-graph tests and algorithms](../measures/chordal.html) | · reported in docs | `ChordalGraphIndependentSetFinder; ChordalGraphMaxCliqueFinder; ChordalGraphMinimalVertexSeparatorFinder; ChordalityInspector; CliqueMinimalSeparatorDecomposition; WeakChordalityInspector` |
| Graph theory and combinatorics | [Cycle basis](../measures/cycle_basis.html) | · reported in docs | `PatonCycleBase; QueueBFSFundamentalCycleBasis; StackBFSFundamentalCycleBasis` |
| Graph theory and combinatorics | [Find cycle](../measures/find_cycle.html) | · reported in docs | `CycleDetector` |
| Graph theory and combinatorics | [From prufer](../measures/nxs_from_prufer.html) | · reported in docs | `PruferTreeGenerator` |
| Graph theory and combinatorics | [Gon Heuristic](../measures/cat_gon_heuristic.html) | · reported in docs | `GonHeuristic` |
| Graph theory and combinatorics | [Graph edit distance](../measures/ged.html) | · reported in docs | `ZhangShashaTreeEditDistance` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `BrownBacktrackColoring; ChordalGraphColoring; GreedyColoring; LargestDegreeFirstColoring; RandomGreedyColoring; SaturationDegreeColoring; SmallestDegreeLastColoring` |
| Graph theory and combinatorics | [Greedy Multiplicative Spanner](../measures/cat_greedy_multiplicative_spanner.html) | · reported in docs | `GreedyMultiplicativeSpanner` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `AdamicAdarIndexLinkPrediction; CommonNeighborsLinkPrediction; HubDepressedIndexLinkPrediction; HubPromotedIndexLinkPrediction; JaccardCoefficientLinkPrediction; LeichtHolmeNewmanIndexLinkPrediction; PreferentialAttachmentLinkPrediction; ResourceAllocationIndexLinkPrediction; SaltonIndexLinkPrediction; SorensenIndexLinkPrediction; SørensenIndexLinkPrediction` |
| Graph theory and combinatorics | [Max weight matching](../measures/max_weight_matching.html) | · reported in docs | `DenseEdmondsMaximumCardinalityMatching; GreedyMaximumCardinalityMatching; GreedyWeightedMatching; KuhnMunkresMinimalWeightBipartitePerfectMatching; MaximumWeightBipartiteMatching; SparseEdmondsMaximumCardinalityMatching` |
| Graph theory and combinatorics | [Perfect-graph (Berge) tests](../measures/perfect_graph.html) | · reported in docs | `BergeGraphInspector` |
| Graph theory and combinatorics | [Planarity testing, embedding and straight-line drawing](../measures/planarity.html) | · reported in docs | `BoyerMyrvoldPlanarityInspector` |
| Graph theory and combinatorics | [Simple cycles](../measures/simple_cycles.html) | · reported in docs | `DirectedSimpleCycles; HawickJamesSimpleCycles; JohnsonSimpleCycles; SzwarcfiterLauerSimpleCycles; TarjanSimpleCycles; TiernanSimpleCycles` |
| Graph theory and combinatorics | [Topological sorts](../measures/nxs_topological_sorts.html) | · reported in docs | `TopologicalOrderIterator` |
| Graph theory and combinatorics | [Traveling salesman (exact and heuristic)](../measures/tsp.html) | · reported in docs | `ChristofidesThreeHalvesApproxMetricTSP; FarthestInsertionHeuristicTSP; GreedyHeuristicTSP; HeldKarpTSP; NearestInsertionHeuristicTSP; NearestNeighborHeuristicTSP; RandomTourTSP; TwoApproxMetricTSP; TwoOptHeuristicTSP` |
| Graph theory and combinatorics | [Vf2pp](../measures/vf2pp.html) | · reported in docs | `AHUForestIsomorphismInspector; AHURootedTreeIsomorphismInspector; AHUUnrootedTreeIsomorphismInspector; ColorRefinementIsomorphismInspector; IsomorphicGraphMapping; IsomorphismInspector; VF2GraphIsomorphismInspector; VF2SubgraphIsomorphismInspector` |
| Graph theory and combinatorics | [Wl hash](../measures/wl_hash.html) | · reported in docs | `ColorRefinementAlgorithm` |
| Inference (QAP, null models) | [Goldberg Maximum Density Subgraph Algorithm](../measures/cat_density_goldberg_maximum_subgraph.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithm` |
| Inference (QAP, null models) | [Goldberg Maximum Density Subgraph Algorithm Base](../measures/cat_base_density_goldberg_maximum_subgraph.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmBase` |
| Inference (QAP, null models) | [Goldberg Maximum Density Subgraph Algorithm Node Weight Per Edge Weight](../measures/cat_density_edge_goldberg_maximum_per_subgraph_weight.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmNodeWeightPerEdgeWeight` |
| Inference (QAP, null models) | [Goldberg Maximum Density Subgraph Algorithm Node Weights](../measures/cat_density_goldberg_maximum_subgraph_weights.html) | · reported in docs | `GoldbergMaximumDensitySubgraphAlgorithmNodeWeights` |
| Input and output | [CSV read and write](../measures/io_csv.html) | · reported in docs | `CSVEventDrivenImporter; CSVExporter; CSVImporter; VisioExporter` |
| Input and output | [DIMACS read and write](../measures/io_dimacs.html) | · reported in docs | `DIMACSEventDrivenImporter; DIMACSExporter; DIMACSImporter` |
| Input and output | [GEXF read and write](../measures/io_gexf.html) | · reported in docs | `GEXFExporter; SimpleGEXFEventDrivenImporter; SimpleGEXFImporter` |
| Input and output | [GML read and write](../measures/io_gml.html) | · reported in docs | `GmlEventDrivenImporter; GmlExporter; GmlImporter` |
| Input and output | [GRAPH6 read and write](../measures/io_graph6.html) | · reported in docs | `Graph6Sparse6EventDrivenImporter; Graph6Sparse6Exporter; Graph6Sparse6Importer` |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | · reported in docs | `GraphMLEventDrivenImporter; GraphMLExporter; GraphMLImporter; SimpleGraphMLEdgeListImporter; SimpleGraphMLEventDrivenImporter; SimpleGraphMLImporter` |
| Input and output | [GRAPHVIZ read and write](../measures/io_graphviz.html) | · reported in docs | `DOTEventDrivenImporter; DOTExporter; DOTImporter` |
| Input and output | [LEMON read and write](../measures/io_lemon.html) | · reported in docs | `LemonExporter` |
| Input and output | [MATRIX read and write](../measures/io_matrix.html) | · reported in docs | `MatrixExporter` |
| Input and output | [Node-link JSON read and write](../measures/io_json.html) | · reported in docs | `JSONEventDrivenImporter; JSONExporter; JSONImporter` |
| Input and output | [TSPLIB read and write](../measures/io_tsplib.html) | · reported in docs | `TSPLIBImporter` |
| Layout | [Barycenter Greedy Two Layered Bipartite Layout2 D](../measures/cat_barycenter_bipartite_d_greedy_layered_layout2_two.html) | · reported in docs | `BarycenterGreedyTwoLayeredBipartiteLayout2D` |
| Layout | [Median Greedy Two Layered Bipartite Layout2 D](../measures/cat_bipartite_d_greedy_layered_layout2_median_two.html) | · reported in docs | `MedianGreedyTwoLayeredBipartiteLayout2D` |
| Layout | [Two Layered Bipartite Layout2 D](../measures/cat_bipartite_d_layered_layout2_two.html) | · reported in docs | `TwoLayeredBipartiteLayout2D` |
| Paths and distances | [All Directed Paths](../measures/cat_all_directed_path.html) | · reported in docs | `AllDirectedPaths` |
| Paths and distances | [Diameter](../measures/diameter.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees |  |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ≠ checked, differs by convention |  |
| Paths and distances | [Heavy Path Decomposition](../measures/cat_decomposition_heavy_path.html) | · reported in docs | `HeavyPathDecomposition` |
| Paths and distances | [Many-to-many and hierarchy-based shortest paths](../measures/paths_hierarchy.html) | · reported in docs | `CHManyToManyShortestPaths; ContractionHierarchyPrecomputation; DefaultManyToManyShortestPaths; TransitNodeRoutingShortestPath` |
| Paths and distances | [Minimum/maximum cycle ratio and mean cycle](../measures/cycle_ratio.html) | · reported in docs | `HowardMinimumMeanCycle` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `AStarShortestPath; BidirectionalAStarShortestPath` |
| Paths and distances | [Paths floyd warshall](../measures/paths_floyd_warshall.html) | · reported in docs | `FloydWarshallShortestPaths` |
| Paths and distances | [Paths johnson](../measures/paths_johnson.html) | · reported in docs | `JohnsonShortestPaths` |
| Paths and distances | [Paths k shortest](../measures/paths_k_shortest.html) | · reported in docs | `EppsteinKShortestPath; EppsteinShortestPathIterator; YenKShortestPath; YenShortestPathIterator` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `BFSShortestPath; BidirectionalDijkstraShortestPath; ClosestFirstIterator; ContractionHierarchyBidirectionalDijkstra; DeltaSteppingShortestPath; DijkstraManyToManyShortestPaths; DijkstraShortestPath; IntVertexDijkstraShortestPath; MartinShortestPath` |
| Paths and distances | [Radius](../measures/radius.html) | ≠ checked, differs by convention |  |
| Roles and positions | [Dulmage Mendelsohn Decomposition](../measures/cat_decomposition_dulmage_mendelsohn.html) | · reported in docs | `DulmageMendelsohnDecomposition` |
| Traversal, trees and DAGs | [Ahuja Orlin Sharma Capacitated Minimum Spanning Tree](../measures/cat_ahuja_capacitated_minimum_orlin_sharma_spanning_tree.html) | · reported in docs | `AhujaOrlinSharmaCapacitatedMinimumSpanningTree` |
| Traversal, trees and DAGs | [Bellman ford](../measures/ord_bellman_ford.html) | · reported in docs | `BellmanFordShortestPath` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `BreadthFirstIterator; LexBreadthFirstIterator` |
| Traversal, trees and DAGs | [Closure](../measures/closure.html) | · reported in docs | `TransitiveClosure` |
| Traversal, trees and DAGs | [Dfs events](../measures/trav_dfs_events.html) | · reported in docs | `DepthFirstIterator` |
| Traversal, trees and DAGs | [Esau Williams Capacitated Minimum Spanning Tree](../measures/cat_capacitated_esau_minimum_spanning_tree_williams.html) | · reported in docs | `EsauWilliamsCapacitatedMinimumSpanningTree` |
| Traversal, trees and DAGs | [Eulerian circuits and paths](../measures/eulerian.html) | · reported in docs | `HierholzerEulerianCycle` |
| Traversal, trees and DAGs | [Palmer Hamiltonian Cycle](../measures/cat_cycle_hamiltonian_palmer.html) | · reported in docs | `PalmerHamiltonianCycle` |
| Traversal, trees and DAGs | [Random walk generation and sampling](../measures/random_walk_sampling.html) | · reported in docs | `RandomWalkVertexIterator` |
| Traversal, trees and DAGs | [Reduction](../measures/reduction.html) | · reported in docs | `TransitiveReduction` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `BoruvkaMinimumSpanningTree; KruskalMinimumSpanningTree; PrimMinimumSpanningTree` |
| Traversal, trees and DAGs | [Spanning weight](../measures/spanning_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Steiner tree](../measures/steiner_tree.html) | · reported in docs | `KouMarkowskyBermanAlgorithm` |
| Traversal, trees and DAGs | [Tree lca](../measures/tree_lca.html) | · reported in docs | `BinaryLiftingLCAFinder; EulerTourRMQLCAFinder; HeavyPathLCAFinder; NaiveLCAFinder; TarjanLCAFinder` |
| Traversal, trees and DAGs | [Vertex orderings (max cardinality, degeneracy)](../measures/vertex_orderings.html) | · reported in docs | `DegeneracyOrderingIterator; MaximumCardinalityIterator` |
| Two-mode and bipartite | [Hopcroft karp](../measures/hopcroft_karp.html) | · reported in docs | `HopcroftKarpMaximumCardinalityBipartiteMatching` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F009](../findings.html#f009) | convention | Undirected self-loop is one arc |
| [F045](../findings.html#f045) | convention | Normalized betweenness divides by (n-1)(n-2) in undirected graphs |
| [F047](../findings.html#f047) | convention | Closeness is 0 for a node that cannot reach every other node |
| [F049](../findings.html#f049) | convention | Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable |
| [F051](../findings.html#f051) | convention | Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs |
| [F053](../findings.html#f053) | limitation | Transitivity refuses directed input |
| [F054](../findings.html#f054) | limitation | Coreness and clique finders refuse non-simple input |
{% endraw %}
