---
title: "NetworKit"
layout: default
parent: Tools
---

{% raw %}
# NetworKit

| Field | Value |
|---|---|
| Identifier | `networkit` |
| Language | C++ / Python |
| Version tested | 11.2.2 |
| License | MIT |
| Homepage | <https://networkit.github.io> |
| Role | checked |
| Citation | [staudt2016networkit](../references.html#staudt2016networkit) |

## How it was run

Imported in CPython; classes constructed and run on graphs with edges added one by one.

Capabilities listed by introspection of NetworKit public classes and functions.

## Coverage

| State | Measures |
|---|---|
| checked, agrees (✓) | 15 |
| checked, no value on some inputs (∅) | 9 |
| reported in docs (·) | 135 |

## Measures

| Family | Measure | State | API names |
|---|---|---|---|
| Centrality | [Approximate betweenness (sampling)](../measures/betweenness_approx.html) | · reported in docs | `ApproxBetweenness; ApproxGroupBetweenness; DynApproxBetweenness; EstimateBetweenness; KadabraBetweenness` |
| Centrality | [Approximate, top-k and group closeness](../measures/closeness_approx.html) | · reported in docs | `ApproxCloseness; DynTopHarmonicCloseness; GroupClosenessGrowShrink; GroupClosenessLocalSearch; GroupClosenessLocalSwaps; GroupHarmonicCloseness; TopCloseness` |
| Centrality | [Betweenness](../measures/betweenness.html) | ∅ checked, no value on some inputs | `Betweenness` |
| Centrality | [Closeness](../measures/closeness.html) | ✓ checked, agrees | `Closeness` |
| Centrality | [Cover Hub Dominance](../measures/cat_cover_dominance_hub.html) | · reported in docs | `CoverHubDominance` |
| Centrality | [Cx laplacian](../measures/cx_laplacian.html) | ✓ checked, agrees | `LaplacianCentrality` |
| Centrality | [Edge betweenness](../measures/edge_betweenness.html) | ✓ checked, agrees |  |
| Centrality | [Eigenvector](../measures/eigenvector.html) | · reported in docs | `EigenvectorCentrality` |
| Centrality | [Group / closeness](../measures/group-closeness.html) | ✓ checked, agrees | `GroupCloseness` |
| Centrality | [Group / degree](../measures/group-degree.html) | ✓ checked, agrees | `GroupDegree` |
| Centrality | [Harmonic](../measures/harmonic.html) | ✓ checked, agrees | `HarmonicCloseness; TopHarmonicCloseness` |
| Centrality | [Hub Dominance](../measures/cat_dominance_hub.html) | · reported in docs | `HubDominance` |
| Centrality | [Katz](../measures/katz.html) | · reported in docs | `KatzCentrality; KatzIndex` |
| Centrality | [KPath Centrality](../measures/cat_k_path.html) | · reported in docs | `KPathCentrality` |
| Centrality | [Local and approximate PageRank](../measures/local_pagerank.html) | · reported in docs | `ApproximatePageRank; PageRankMatrix; PageRankNibble` |
| Centrality | [Pagerank](../measures/pagerank.html) | ∅ checked, no value on some inputs | `PageRank` |
| Centrality | [Partition Hub Dominance](../measures/cat_dominance_hub_partition.html) | · reported in docs | `PartitionHubDominance` |
| Centrality | [Permanence Centrality](../measures/cat_permanence.html) | · reported in docs | `PermanenceCentrality` |
| Centrality | [Resistance-based and spectral edge/vertex scores](../measures/resistance_based.html) | · reported in docs | `AlgebraicDistance; ApproxElectricalCloseness; ApproxSpanningEdge; CommuteTimeDistance; ForestCentrality; SpanningEdgeCentrality` |
| Centrality | [Strength](../measures/strength.html) | ∅ checked, no value on some inputs |  |
| Cohesion and subgroups | [Clique Detect](../measures/cat_clique_detect.html) | · reported in docs | `CliqueDetect` |
| Cohesion and subgroups | [Clique number](../measures/clique_number.html) | ✓ checked, agrees |  |
| Cohesion and subgroups | [Coreness](../measures/coreness.html) | ∅ checked, no value on some inputs | `CoreDecomposition` |
| Cohesion and subgroups | [Cut quality (conductance, expansion, boundary)](../measures/cut_quality.html) | · reported in docs | `Volume` |
| Cohesion and subgroups | [Max cliques](../measures/max_cliques.html) | ∅ checked, no value on some inputs | `MaximalCliques` |
| Communities | [Compare partitions](../measures/compare_partitions.html) | · reported in docs | `AdjustedRandIndex; AdjustedRandMeasure; GraphStructuralRandMeasure; JaccardMeasure; NMIDistance; NodeStructuralRandMeasure; OverlappingNMIDistance; compareCommunities` |
| Communities | [Intrapartition Density](../measures/cat_density_intrapartition.html) | · reported in docs | `IntrapartitionDensity` |
| Communities | [Isolated Interpartition Conductance](../measures/cat_conductance_interpartition_isolated.html) | · reported in docs | `IsolatedInterpartitionConductance` |
| Communities | [Isolated Interpartition Expansion](../measures/cat_expansion_interpartition_isolated.html) | · reported in docs | `IsolatedInterpartitionExpansion` |
| Communities | [K Core Community Detection](../measures/cat_community_core_detection_k.html) | · reported in docs | `kCoreCommunityDetection` |
| Communities | [Label propagation](../measures/label_propagation.html) | · reported in docs | `LPDegreeOrdered; PLP` |
| Communities | [Leiden](../measures/leiden.html) | · reported in docs | `ParallelLeiden` |
| Communities | [Local Partition Coverage](../measures/cat_coverage_local_partition.html) | · reported in docs | `LocalPartitionCoverage` |
| Communities | [Louvain modularity](../measures/louvain_modularity.html) | · reported in docs | `LouvainMapEquation; PLM` |
| Communities | [Modularity](../measures/modularity.html) | ∅ checked, no value on some inputs | `Modularity` |
| Communities | [Partition Fragmentation](../measures/cat_fragmentation_partition.html) | · reported in docs | `PartitionFragmentation` |
| Communities | [Partition quality (coverage, performance)](../measures/partition_quality.html) | · reported in docs | `Coverage` |
| Communities | [Same Community Index](../measures/cat_community_same.html) | · reported in docs | `SameCommunityIndex` |
| Communities | [Set Conductance](../measures/cat_conductance_set.html) | · reported in docs | `SetConductance` |
| Communities | [Spectral Partitioner](../measures/cat_partitioner_spectral.html) | · reported in docs | `SpectralPartitioner` |
| Components and connectivity | [Bicomponents](../measures/bicomponents.html) | ∅ checked, no value on some inputs | `BiconnectedComponents` |
| Components and connectivity | [Edge cut](../measures/edge_cut.html) | · reported in docs | `EdgeCut` |
| Components and connectivity | [Max flow](../measures/max_flow.html) | · reported in docs | `EdmondsKarp` |
| Components and connectivity | [Parallel Connected Components](../measures/cat_component_connected_parallel.html) | · reported in docs | `ParallelConnectedComponents` |
| Data transforms | [Op difference](../measures/op_difference.html) | · reported in docs | `GraphDifference` |
| Descriptive statistics | [Average clustering](../measures/average_clustering.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Clustering](../measures/clustering.html) | ✓ checked, agrees | `ClusteringCoefficient; LocalClusteringCoefficient; clustering` |
| Descriptive statistics | [Components](../measures/components.html) | ✓ checked, agrees | `ConnectedComponents; StronglyConnectedComponents; WeaklyConnectedComponents` |
| Descriptive statistics | [Degree](../measures/degree.html) | ✓ checked, agrees | `DegreeCentrality; degreeDistribution` |
| Descriptive statistics | [Degree distribution and its summary statistics](../measures/degree_distribution.html) | · reported in docs | `clusteringPerDegree; gini` |
| Descriptive statistics | [Density](../measures/density.html) | ✓ checked, agrees |  |
| Descriptive statistics | [Transitivity](../measures/transitivity.html) | ✓ checked, agrees |  |
| Generators and rewiring | [Chung-Lu (expected degree) generator](../measures/gen_chung_lu.html) | · reported in docs | `ChungLuGenerator` |
| Generators and rewiring | [Clustering Generator](../measures/cat_clustering_generator.html) | · reported in docs | `ClusteringGenerator` |
| Generators and rewiring | [Cut Clustering](../measures/cat_clustering_cut.html) | · reported in docs | `CutClustering` |
| Generators and rewiring | [Dorogovtsev-Goltsev-Mendes graph](../measures/dorogovtsev_goltsev_mendes_graph.html) | · reported in docs | `DorogovtsevMendesGenerator; DynamicDorogovtsevMendesGenerator` |
| Generators and rewiring | [Dynamic Path Generator](../measures/cat_dynamic_generator_path.html) | · reported in docs | `DynamicPathGenerator` |
| Generators and rewiring | [Dynamic Pub Web Generator](../measures/cat_dynamic_generator_pub_web.html) | · reported in docs | `DynamicPubWebGenerator` |
| Generators and rewiring | [Forest fire generator](../measures/gen_forest_fire.html) | · reported in docs | `DynamicForestFireGenerator` |
| Generators and rewiring | [Forest Fire Sparsifier](../measures/cat_fire_forest_sparsifier.html) | · reported in docs | `ForestFireSparsifier` |
| Generators and rewiring | [G(n, p) random graph](../measures/gen_gnp.html) | · reported in docs | `ErdosRenyiGenerator` |
| Generators and rewiring | [Havel Hakimi Generator](../measures/cat_generator_hakimi_havel.html) | · reported in docs | `HavelHakimiGenerator` |
| Generators and rewiring | [Hyperbolic random graph generator](../measures/gen_hyperbolic.html) | · reported in docs | `DynamicHyperbolicGenerator; HyperbolicGenerator` |
| Generators and rewiring | [LFRGenerator](../measures/cat_generator_lfr.html) | · reported in docs | `LFRGenerator` |
| Generators and rewiring | [Local Square Clustering Coefficient](../measures/cat_clustering_coefficient_local_square.html) | · reported in docs | `LocalSquareClusteringCoefficient` |
| Generators and rewiring | [Mocnik Generator](../measures/cat_generator_mocnik.html) | · reported in docs | `MocnikGenerator` |
| Generators and rewiring | [Mocnik Generator Basic](../measures/cat_basic_generator_mocnik.html) | · reported in docs | `MocnikGeneratorBasic` |
| Generators and rewiring | [Powerlaw Degree Sequence](../measures/cat_degree_powerlaw_sequence.html) | · reported in docs | `PowerlawDegreeSequence` |
| Generators and rewiring | [Preferential attachment generator](../measures/gen_preferential.html) | · reported in docs | `BarabasiAlbertGenerator` |
| Generators and rewiring | [Pub Web Generator](../measures/cat_generator_pub_web.html) | · reported in docs | `PubWebGenerator` |
| Generators and rewiring | [R-MAT generator](../measures/gen_rmat.html) | · reported in docs | `RmatGenerator` |
| Generators and rewiring | [Regular Ring Lattice Generator](../measures/cat_generator_lattice_regular_ring.html) | · reported in docs | `RegularRingLatticeGenerator` |
| Generators and rewiring | [Small-world generator](../measures/gen_small_world.html) | · reported in docs | `WattsStrogatzGenerator` |
| Generators and rewiring | [Stochastic block model generator](../measures/gen_sbm.html) | · reported in docs | `ClusteredRandomGraphGenerator` |
| Generators and rewiring | [Swap contract](../measures/swap_contract.html) | · reported in docs | `Curveball; CurveballGlobalTradeGenerator; CurveballUniformTradeGenerator; DegreePreservingShuffle; EdgeSwitching; EdgeSwitchingInPlace; EdgeSwitchingMarkovChainGenerator; GlobalCurveball` |
| Graph theory and combinatorics | [Ap vertex cover](../measures/ap_vertex_cover.html) | · reported in docs | `Cover` |
| Graph theory and combinatorics | [Approximate and b-matching](../measures/matching_approx.html) | · reported in docs | `BMatcher; BSuitorMatcher; DynamicBSuitorMatcher; PathGrowingMatcher; SuitorMatcher` |
| Graph theory and combinatorics | [BTERReplicator](../measures/cat_bter_replicator.html) | · reported in docs | `BTERReplicator` |
| Graph theory and combinatorics | [Check matching](../measures/check_matching.html) | · reported in docs | `Matching` |
| Graph theory and combinatorics | [Combined SCD](../measures/cat_combined_scd.html) | · reported in docs | `CombinedSCD` |
| Graph theory and combinatorics | [Cover F1 Similarity](../measures/cat_cover_f1_similarity.html) | · reported in docs | `CoverF1Similarity` |
| Graph theory and combinatorics | [Degree Multiscale Sparsifier](../measures/cat_degree_multiscale_sparsifier.html) | · reported in docs | `DegreeMultiscaleSparsifier` |
| Graph theory and combinatorics | [Epidemic Simulation SEIR](../measures/cat_epidemic_seir_simulation.html) | · reported in docs | `EpidemicSimulationSEIR` |
| Graph theory and combinatorics | [GCE](../measures/cat_gce.html) | · reported in docs | `GCE` |
| Graph theory and combinatorics | [Global Threshold Filter](../measures/cat_filter_global_threshold.html) | · reported in docs | `GlobalThresholdFilter` |
| Graph theory and combinatorics | [Greedy color](../measures/greedy_color.html) | · reported in docs | `SpectralColoring` |
| Graph theory and combinatorics | [Jaccard Similarity Sparsifier](../measures/cat_jaccard_similarity_sparsifier.html) | · reported in docs | `JaccardSimilaritySparsifier` |
| Graph theory and combinatorics | [LFM](../measures/cat_lfm.html) | · reported in docs | `LFM` |
| Graph theory and combinatorics | [LFMLocal](../measures/cat_lfm_local.html) | · reported in docs | `LFMLocal` |
| Graph theory and combinatorics | [Link prediction](../measures/link_prediction.html) | · reported in docs | `AdamicAdarDistance; AdamicAdarIndex; AlgebraicDistanceIndex; CommonNeighborsIndex; JaccardDistance; JaccardIndex; LinkThresholder; MissingLinksFinder; NeighborhoodDistanceIndex; NeighborsMeasureIndex; PreferentialAttachmentIndex; ResourceAllocationIndex` |
| Graph theory and combinatorics | [Local Degree Sparsifier](../measures/cat_degree_local_sparsifier.html) | · reported in docs | `LocalDegreeSparsifier` |
| Graph theory and combinatorics | [Local Similarity Sparsifier](../measures/cat_local_similarity_sparsifier.html) | · reported in docs | `LocalSimilaritySparsifier` |
| Graph theory and combinatorics | [Local Tightness Expansion](../measures/cat_expansion_local_tightness.html) | · reported in docs | `LocalTightnessExpansion` |
| Graph theory and combinatorics | [Multiscale Sparsifier](../measures/cat_multiscale_sparsifier.html) | · reported in docs | `MultiscaleSparsifier` |
| Graph theory and combinatorics | [Pivot MDS](../measures/cat_mds_pivot.html) | · reported in docs | `PivotMDS` |
| Graph theory and combinatorics | [Pruned Landmark Labeling](../measures/cat_labeling_landmark_pruned.html) | · reported in docs | `PrunedLandmarkLabeling` |
| Graph theory and combinatorics | [Quadrilateral Simmelian Sparsifier](../measures/cat_quadrilateral_simmelian_sparsifier.html) | · reported in docs | `QuadrilateralSimmelianSparsifier` |
| Graph theory and combinatorics | [Random Edge Sparsifier](../measures/cat_edge_random_sparsifier.html) | · reported in docs | `RandomEdgeSparsifier; RandomNodeEdgeSparsifier` |
| Graph theory and combinatorics | [SCANSparsifier](../measures/cat_scan_sparsifier.html) | · reported in docs | `SCANSparsifier` |
| Graph theory and combinatorics | [SCDGround Truth Comparison](../measures/cat_comparison_ground_scd_truth.html) | · reported in docs | `SCDGroundTruthComparison` |
| Graph theory and combinatorics | [Sfigality](../measures/cat_sfigality.html) | · reported in docs | `Sfigality` |
| Graph theory and combinatorics | [Simmelian Multiscale Sparsifier](../measures/cat_multiscale_simmelian_sparsifier.html) | · reported in docs | `SimmelianMultiscaleSparsifier` |
| Graph theory and combinatorics | [Simmelian Sparsifier Non Parametric](../measures/cat_non_parametric_simmelian_sparsifier.html) | · reported in docs | `SimmelianSparsifierNonParametric` |
| Graph theory and combinatorics | [Simmelian Sparsifier Parametric](../measures/cat_parametric_simmelian_sparsifier.html) | · reported in docs | `SimmelianSparsifierParametric` |
| Graph theory and combinatorics | [SPSP](../measures/cat_spsp.html) | · reported in docs | `SPSP` |
| Graph theory and combinatorics | [TCE](../measures/cat_tce.html) | · reported in docs | `TCE` |
| Graph theory and combinatorics | [Total Neighbors Index](../measures/cat_neighbors_total.html) | · reported in docs | `TotalNeighborsIndex` |
| Graph theory and combinatorics | [Traveling salesman (exact and heuristic)](../measures/tsp.html) | · reported in docs | `STSP` |
| Graph theory and combinatorics | [Triangle Sparsifier](../measures/cat_sparsifier_triangle.html) | · reported in docs | `TriangleSparsifier` |
| Graph theory and combinatorics | [UDegree Index](../measures/cat_degree_u.html) | · reported in docs | `UDegreeIndex` |
| Graph theory and combinatorics | [VDegree Index](../measures/cat_degree_v.html) | · reported in docs | `VDegreeIndex` |
| Input and output | [BINARYEDGELISTPARTITION read and write](../measures/io_binaryedgelistpartition.html) | · reported in docs | `BinaryEdgeListPartitionReader; BinaryEdgeListPartitionWriter` |
| Input and output | [BINARYPARTITION read and write](../measures/io_binarypartition.html) | · reported in docs | `BinaryPartitionReader; BinaryPartitionWriter` |
| Input and output | [EDGELIST read and write](../measures/io_edgelist.html) | · reported in docs | `EdgeListReader; EdgeListWriter` |
| Input and output | [EDGELISTCOVER read and write](../measures/io_edgelistcover.html) | · reported in docs | `EdgeListCoverReader` |
| Input and output | [EDGELISTPARTITION read and write](../measures/io_edgelistpartition.html) | · reported in docs | `EdgeListPartitionReader` |
| Input and output | [GEXF read and write](../measures/io_gexf.html) | · reported in docs | `GEXFReader; GEXFWriter` |
| Input and output | [GML read and write](../measures/io_gml.html) | · reported in docs | `GMLGraphReader; GMLGraphWriter` |
| Input and output | [GraphML read and write](../measures/io_graphml.html) | · reported in docs | `GraphMLReader; GraphMLWriter` |
| Input and output | [GRAPHTOOLBINARY read and write](../measures/io_graphtoolbinary.html) | · reported in docs | `GraphToolBinaryReader; GraphToolBinaryWriter` |
| Input and output | [GRAPHVIZ read and write](../measures/io_graphviz.html) | · reported in docs | `DotGraphWriter` |
| Input and output | [KONECT read and write](../measures/io_konect.html) | · reported in docs | `KONECTGraphReader` |
| Input and output | [MATLAB read and write](../measures/io_matlab.html) | · reported in docs | `MatReader; MatWriter` |
| Input and output | [METIS read and write](../measures/io_metis.html) | · reported in docs | `METISGraphReader; METISGraphWriter` |
| Input and output | [MTX read and write](../measures/io_mtx.html) | · reported in docs | `MTXGraphReader` |
| Input and output | [NETWORKITBINARY read and write](../measures/io_networkitbinary.html) | · reported in docs | `NetworkitBinaryReader; NetworkitBinaryWriter` |
| Input and output | [RB read and write](../measures/io_rb.html) | · reported in docs | `RBGraphReader` |
| Input and output | [SNAP read and write](../measures/io_snap.html) | · reported in docs | `SNAPGraphReader; SNAPGraphWriter` |
| Input and output | [SNAPEDGELISTPARTITION read and write](../measures/io_snapedgelistpartition.html) | · reported in docs | `SNAPEdgeListPartitionReader` |
| Input and output | [THRILLGRAPHBINARY read and write](../measures/io_thrillgraphbinary.html) | · reported in docs | `ThrillGraphBinaryReader; ThrillGraphBinaryWriter` |
| Layout | [Maxent Stress](../measures/cat_maxent_stress.html) | · reported in docs | `MaxentStress` |
| Layout | [Node2 Vec](../measures/cat_node2_vec.html) | · reported in docs | `Node2Vec` |
| Matrices and spectra | [Adjacency](../measures/gm_adjacency.html) | · reported in docs | `adjacencyMatrix` |
| Matrices and spectra | [Eigenvectors of graph matrices](../measures/eigenvectors_matrix.html) | · reported in docs | `SpectralCentrality; adjacencyEigenvector; adjacencyEigenvectors; eigenvectors; laplacianEigenvector; laplacianEigenvectors; symmetricEigenvectors` |
| Matrices and spectra | [Gm laplacian](../measures/gm_laplacian.html) | · reported in docs | `laplacianMatrix` |
| Mixing and assortativity | [Assortativity values](../measures/assortativity_values.html) | · reported in docs | `Assortativity` |
| Paths and distances | [Algebraic Distance Sparsifier](../measures/cat_algebraic_distance_sparsifier.html) | · reported in docs | `AlgebraicDistanceSparsifier` |
| Paths and distances | [Complex Paths](../measures/cat_complex_path.html) | · reported in docs | `ComplexPaths` |
| Paths and distances | [Diameter](../measures/diameter.html) | ∅ checked, no value on some inputs | `Diameter; DiameterAlgo; EffectiveDiameter` |
| Paths and distances | [Distances](../measures/distances.html) | ✓ checked, agrees | `GraphDistance` |
| Paths and distances | [Eccentricity](../measures/eccentricity.html) | ∅ checked, no value on some inputs | `Eccentricity` |
| Paths and distances | [Ged Walk](../measures/cat_ged_walk.html) | · reported in docs | `GedWalk` |
| Paths and distances | [Neighborhood function, hop plot, effective diameter](../measures/neighborhood_function.html) | · reported in docs | `EffectiveDiameterApproximation; HopPlotApproximation; NeighborhoodFunction; NeighborhoodFunctionApproximation; NeighborhoodFunctionHeuristic; hopPlot` |
| Paths and distances | [Paths all pairs](../measures/paths_all_pairs.html) | · reported in docs | `APSP; DynAPSP` |
| Paths and distances | [Paths astar](../measures/paths_astar.html) | · reported in docs | `AStar` |
| Paths and distances | [Paths bidirectional](../measures/paths_bidirectional.html) | · reported in docs | `BidirectionalBFS` |
| Paths and distances | [Paths simple](../measures/paths_simple.html) | · reported in docs | `AllSimplePaths` |
| Paths and distances | [Paths sssp](../measures/paths_sssp.html) | · reported in docs | `BidirectionalDijkstra; Dijkstra; DynDijkstra; MultiTargetBFS; MultiTargetDijkstra; SSSP` |
| Paths and distances | [Random BFS](../measures/cat_bfs_random.html) | · reported in docs | `RandomBFS` |
| Paths and distances | [Reachable Nodes](../measures/cat_reachable.html) | · reported in docs | `ReachableNodes` |
| Paths and distances | [Reverse BFS](../measures/cat_bfs_reverse.html) | · reported in docs | `ReverseBFS` |
| Roles and positions | [Core Decomposition Sequence](../measures/cat_core_decomposition_sequence.html) | · reported in docs | `coreDecompositionSequence` |
| Temporal and events | [Incremental maintenance on a changing graph](../measures/dynamic_update.html) | · reported in docs | `DynBFS; DynBetweenness; DynBetweennessOneNode; DynConnectedComponents; DynKatzCentrality; DynPrunedLandmarkLabeling; DynWeaklyConnectedComponents` |
| Traversal, trees and DAGs | [Bfs edges](../measures/trav_bfs_edges.html) | · reported in docs | `BFS` |
| Traversal, trees and DAGs | [Random Maximum Spanning Forest](../measures/cat_forest_maximum_random_spanning.html) | · reported in docs | `RandomMaximumSpanningForest` |
| Traversal, trees and DAGs | [Spanning tree](../measures/spanning_tree.html) | · reported in docs | `KruskalMSF; PrimMSF; SpanningForest` |
| Traversal, trees and DAGs | [Spanning weight](../measures/spanning_weight.html) | ✓ checked, agrees |  |
| Traversal, trees and DAGs | [Union Maximum Spanning Forest](../measures/cat_forest_maximum_spanning_union.html) | · reported in docs | `UnionMaximumSpanningForest` |
| Traversal, trees and DAGs | [Walks](../measures/gb_walks.html) | · reported in docs | `walk` |

## Findings

| Id | Kind | Title |
|---|---|---|
| [F060](../findings.html#f060) | convention | Undirected betweenness scores both orderings of a pair |
| [F061](../findings.html#f061) | convention | Closeness returns (n-1)/sum of distances whatever normalized says |
| [F062](../findings.html#f062) | convention | edgeScores() follow NetworKit's own edge numbering |
| [F063](../findings.html#f063) | defect | Katz and degree assortativity differ by 2% to 40% |
| [F064](../findings.html#f064) | defect | Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs |
| [F065](../findings.html#f065) | convention | Loops, parallel edges and directed input are counted differently |
| [F066](../findings.html#f066) | convention | MaximalCliques omits a node without edges |
| [F067](../findings.html#f067) | defect | Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10% |
| [F068](../findings.html#f068) | convention | Rank at isolated nodes is spread differently |
| [F069](../findings.html#f069) | convention | weightedDegree counts out-edges only; a single node gets 0 |
{% endraw %}
