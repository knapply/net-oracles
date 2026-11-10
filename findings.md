---
title: Findings
layout: default
nav_order: 6
---

{% raw %}

# Findings

Bugs, disagreements and limitations observed in other tools. `kind` is *defect* (wrong under the published definition), *convention* (differs by a convention) or *limitation* (refuses or cannot represent the input). `status` is *reproduced* (minimal reproduction recorded), *observed* (seen on a shared corpus of test graphs) or *reported* (public discussion, not re-measured). Versions are those tested; a finding may not hold in later versions.

<div class="table-wrapper"><table><thead><tr><th>Id</th><th>Tool</th><th>Version</th><th>Measure</th><th>Kind</th><th>Status</th><th>Title</th></tr></thead><tbody><tr><td><a href="#f001">F001</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/group_betweenness.html#group-betweenness">Group / betweenness</a></td><td>defect</td><td>reproduced</td><td>group_betweenness_centrality compares float path lengths exactly</td></tr><tr><td><a href="#f002">F002</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/group_prominence.html#nxo_prominent">Prominent group</a></td><td>defect</td><td>reproduced</td><td>prominent_group misses the best group on disconnected graphs</td></tr><tr><td><a href="#f003">F003</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/graph-theory-and-combinatorics/graph_edit_distance.html#ged">Graph edit distance</a></td><td>defect</td><td>reproduced</td><td>graph_edit_distance substitutes a self-loop for an ordinary edge at no cost</td></tr><tr><td><a href="#f004">F004</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/paths-and-distances/shortest_paths.html#ord_bellman_ford">Bellman ford</a></td><td>defect</td><td>observed</td><td>goldberg_radzik raises NetworkXUnbounded for any negative self-loop</td></tr><tr><td><a href="#f005">F005</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>PageRank stops on an L1 change below n * tol</td></tr><tr><td><a href="#f006">F006</a></td><td>rustworkx</td><td>0.18.1</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>PageRank stops on an L1 change below n * tol</td></tr><tr><td><a href="#f007">F007</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>Undirected self-loop is one arc</td></tr><tr><td><a href="#f008">F008</a></td><td>rustworkx</td><td>0.18.1</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>Undirected self-loop is one arc</td></tr><tr><td><a href="#f009">F009</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>Undirected self-loop is one arc</td></tr><tr><td><a href="#f010">F010</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/communities/walktrap.html#walktrap">Walktrap</a></td><td>defect</td><td>observed</td><td>Walktrap skips minimal merge pairs on mid-size random networks</td></tr><tr><td><a href="#f011">F011</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/communities/modularity_maximization.html#leading_eigen">Leading eigen</a></td><td>convention</td><td>observed</td><td>Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance</td></tr><tr><td><a href="#f012">F012</a></td><td>keyplayer</td><td>1.0.4</td><td><a href="measures/centrality/key_player_single.html#kpp_single-distance_reach">Kpp_single / distance_reach</a></td><td>defect</td><td>observed</td><td>Weighted distances (binary = FALSE) are not shortest-path lengths</td></tr><tr><td><a href="#f013">F013</a></td><td>centiserve</td><td>1.0.0</td><td><a href="measures/centrality/communicability_betweenness.html#cx_communicability_betweenness">Communicability betweenness</a></td><td>defect</td><td>reproduced</td><td>communibet() cannot find an installed expm</td></tr><tr><td><a href="#f014">F014</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/centrality/eigenvector_centrality.html#eigenvector">Eigenvector</a></td><td>defect</td><td>reproduced</td><td>Eigenvector centrality is not converged</td></tr><tr><td><a href="#f015">F015</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/communities/modularity_maximization.html#louvain_quality">Louvain quality</a></td><td>defect</td><td>reproduced</td><td>Louvain with setRandom(false) is not reproducible</td></tr><tr><td><a href="#f016">F016</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/communities/modularity_maximization.html#louvain_quality">Louvain quality</a></td><td>defect</td><td>reproduced</td><td>Louvain sometimes does not return</td></tr><tr><td><a href="#f017">F017</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>defect</td><td>reproduced</td><td>PageRank loses probability mass at self-loops</td></tr><tr><td><a href="#f018">F018</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Closeness is reached/sum of distances; 0 for a node reaching nobody</td></tr><tr><td><a href="#f019">F019</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/centrality/hits.html#hits">Hits</a></td><td>convention</td><td>observed</td><td>HITS uses unit Euclidean scaling and ignores self-loops</td></tr><tr><td><a href="#f020">F020</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/centrality/degree.html#degree">Degree</a></td><td>convention</td><td>observed</td><td>Degree counts a self-loop twice</td></tr><tr><td><a href="#f021">F021</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/descriptive-statistics/local_clustering.html#average_clustering">Average clustering</a></td><td>convention</td><td>observed</td><td>Average clustering leaves out nodes of degree below 2</td></tr><tr><td><a href="#f022">F022</a></td><td>Gephi toolkit</td><td>0.11.3</td><td><a href="measures/communities/modularity_maximization.html#louvain_quality">Louvain quality</a></td><td>convention</td><td>observed</td><td>Louvain resolution acts as the reciprocal of gamma</td></tr><tr><td><a href="#f023">F023</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/paths-and-distances/wiener_index.html#dm_index">Index</a></td><td>defect</td><td>observed</td><td>hyper_wiener_index is twice the published value</td></tr><tr><td><a href="#f024">F024</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/betweenness.html#cx_betweenness_subset">Betweenness subset</a></td><td>defect</td><td>observed</td><td>edge_betweenness_centrality_subset deviates from its documented formula</td></tr><tr><td><a href="#f025">F025</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/roles-and-positions/effective_size.html#effective_size">Effective size</a></td><td>defect</td><td>observed</td><td>effective_size is wrong for weighted or directed graphs on its vectorized path</td></tr><tr><td><a href="#f026">F026</a></td><td>NetworkX</td><td>3.7</td><td></td><td>defect</td><td>observed</td><td>Network simplex can misreport feasibility with float weights</td></tr><tr><td><a href="#f027">F027</a></td><td>NetworkX</td><td>3.7</td><td></td><td>defect</td><td>observed</td><td>maximum_spanning_arborescence occasionally misses the maximum</td></tr><tr><td><a href="#f028">F028</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/components-and-connectivity/k_edge_components.html#k_edge_components">K edge components</a></td><td>limitation</td><td>observed</td><td>k_edge_components hits the recursion limit near n = 1000</td></tr><tr><td><a href="#f029">F029</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/communities/label_propagation.html#label_propagation">Label propagation</a></td><td>convention</td><td>observed</td><td>Ties are broken by Python set or insertion order</td></tr><tr><td><a href="#f030">F030</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/group_betweenness.html#group-betweenness">Group / betweenness</a></td><td>defect</td><td>observed</td><td>group_betweenness_centrality can vary with PYTHONHASHSEED</td></tr><tr><td><a href="#f031">F031</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/components-and-connectivity/node_connectivity.html#ap_node_connectivity">Node connectivity</a></td><td>defect</td><td>reproduced</td><td>approximation.node_connectivity starts from a bound that can exceed the connectivity</td></tr><tr><td><a href="#f032">F032</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/traversal-trees-and-dags/cd_index.html#nxs_cd_index">CD index</a></td><td>convention</td><td>observed</td><td>cd_index pools every citer of the references, whatever its time</td></tr><tr><td><a href="#f033">F033</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>Weighted betweenness counts one shortest path per neighbour pair with parallel edges</td></tr><tr><td><a href="#f034">F034</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/generators-and-rewiring/circulant_ring_graphs.html#implicit_family">Implicit family</a></td><td>convention</td><td>observed</td><td>hypercube_graph nodes are bit tuples; dimension 0 is the null graph</td></tr><tr><td><a href="#f035">F035</a></td><td>NetworkX</td><td>3.7</td><td><a href="measures/communities/modularity.html#modularity">Modularity</a></td><td>convention</td><td>observed</td><td>Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input</td></tr><tr><td><a href="#f036">F036</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/communities/compare_partitions.html#compare_partitions">Compare partitions</a></td><td>convention</td><td>observed</td><td>Adjusted Rand index is NaN on all-singleton partitions</td></tr><tr><td><a href="#f037">F037</a></td><td>cdlib</td><td>0.4.1</td><td><a href="measures/communities/compare_partitions.html#compare_partitions">Compare partitions</a></td><td>convention</td><td>observed</td><td>Adjusted Rand index is 1 on degenerate partitions</td></tr><tr><td><a href="#f038">F038</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/communities/spinglass.html#spinglass">Spinglass</a></td><td>convention</td><td>observed</td><td>Spinglass reads the network as simple</td></tr><tr><td><a href="#f039">F039</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/descriptive-statistics/triad_census.html#triad_census">Triad census</a></td><td>defect</td><td>observed</td><td>Triad census on multigraphs differs from the definition</td></tr><tr><td><a href="#f040">F040</a></td><td>igraph (R)</td><td>2.3.4</td><td><a href="measures/centrality/hits.html#hits">Hits</a></td><td>convention</td><td>observed</td><td>HITS returns 1 for an edgeless network</td></tr><tr><td><a href="#f041">F041</a></td><td>sna</td><td>2.8</td><td><a href="measures/centrality/information_centrality.html#information_centrality">Information centrality</a></td><td>defect</td><td>observed</td><td>Information centrality fails on singular inputs</td></tr><tr><td><a href="#f042">F042</a></td><td>sna</td><td>2.8</td><td><a href="measures/centrality/degree.html#degree">Degree</a></td><td>convention</td><td>observed</td><td>Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default</td></tr><tr><td><a href="#f043">F043</a></td><td>sna</td><td>2.8</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Closeness and centralization normalizations differ from other tools</td></tr><tr><td><a href="#f044">F044</a></td><td>sna</td><td>2.8</td><td><a href="measures/descriptive-statistics/reciprocity.html#reciprocity">Reciprocity</a></td><td>convention</td><td>observed</td><td>Reciprocity correlation is 0 on a single arc</td></tr><tr><td><a href="#f045">F045</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>Normalized betweenness divides by (n-1)(n-2) in undirected graphs</td></tr><tr><td><a href="#f046">F046</a></td><td>Boost Graph Library</td><td>1.90</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>relative_betweenness_centrality is twice the standard value on directed graphs</td></tr><tr><td><a href="#f047">F047</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Closeness is 0 for a node that cannot reach every other node</td></tr><tr><td><a href="#f048">F048</a></td><td>Boost Graph Library</td><td>1.90</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Closeness is 1 / sum of distances, with DBL_MAX for an unreachable pair</td></tr><tr><td><a href="#f049">F049</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/paths-and-distances/eccentricity.html#eccentricity">Eccentricity</a></td><td>convention</td><td>observed</td><td>Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable</td></tr><tr><td><a href="#f050">F050</a></td><td>Boost Graph Library</td><td>1.90</td><td><a href="measures/paths-and-distances/eccentricity.html#eccentricity">Eccentricity</a></td><td>convention</td><td>observed</td><td>Eccentricity, radius and diameter return DBL_MAX when a node is unreachable</td></tr><tr><td><a href="#f051">F051</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/descriptive-statistics/local_clustering.html#clustering">Clustering</a></td><td>convention</td><td>observed</td><td>Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs</td></tr><tr><td><a href="#f052">F052</a></td><td>Boost Graph Library</td><td>1.90</td><td><a href="measures/descriptive-statistics/local_clustering.html#clustering">Clustering</a></td><td>convention</td><td>observed</td><td>Clustering counts loops and parallel edges as extra neighbours</td></tr><tr><td><a href="#f053">F053</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/descriptive-statistics/global_transitivity.html#transitivity">Transitivity</a></td><td>limitation</td><td>observed</td><td>Transitivity refuses directed input</td></tr><tr><td><a href="#f054">F054</a></td><td>JGraphT</td><td>1.5.2</td><td><a href="measures/cohesion-and-subgroups/k_core.html#coreness">Coreness</a></td><td>limitation</td><td>observed</td><td>Coreness and clique finders refuse non-simple input</td></tr><tr><td><a href="#f055">F055</a></td><td>BCT (Octave)</td><td>2019-03-03</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>Betweenness counts ordered pairs on undirected networks</td></tr><tr><td><a href="#f056">F056</a></td><td>BCT (Octave)</td><td>2019-03-03</td><td><a href="measures/descriptive-statistics/local_clustering.html#clustering">Clustering</a></td><td>convention</td><td>observed</td><td>clustering_coef_bd and transitivity_bd are Fagiolo's directed coefficients</td></tr><tr><td><a href="#f057">F057</a></td><td>BCT (Octave)</td><td>2019-03-03</td><td><a href="measures/paths-and-distances/eccentricity.html#eccentricity">Eccentricity</a></td><td>convention</td><td>observed</td><td>charpath takes the longest finite distance; NaN for a node reaching nobody</td></tr><tr><td><a href="#f058">F058</a></td><td>BCT (Octave)</td><td>2019-03-03</td><td><a href="measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_degree">Assortativity degree</a></td><td>convention</td><td>observed</td><td>Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target</td></tr><tr><td><a href="#f059">F059</a></td><td>BCT (Octave)</td><td>2019-03-03</td><td><a href="measures/centrality/degree.html#degree">Degree</a></td><td>convention</td><td>observed</td><td>Matrix-input calls carry no loops or parallel edges</td></tr><tr><td><a href="#f060">F060</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>Undirected betweenness scores both orderings of a pair</td></tr><tr><td><a href="#f061">F061</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Closeness returns (n-1)/sum of distances whatever normalized says</td></tr><tr><td><a href="#f062">F062</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/edge_betweenness.html#edge_betweenness">Edge betweenness</a></td><td>convention</td><td>observed</td><td>edgeScores() follow NetworKit's own edge numbering</td></tr><tr><td><a href="#f063">F063</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/katz_centrality.html#katz">Katz</a></td><td>defect</td><td>observed</td><td>Katz and degree assortativity differ by 2% to 40%</td></tr><tr><td><a href="#f064">F064</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/eigenvector_centrality.html#eigenvector">Eigenvector</a></td><td>defect</td><td>observed</td><td>Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs</td></tr><tr><td><a href="#f065">F065</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/degree.html#degree">Degree</a></td><td>convention</td><td>observed</td><td>Loops, parallel edges and directed input are counted differently</td></tr><tr><td><a href="#f066">F066</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/cohesion-and-subgroups/maximal_cliques.html#max_cliques">Max cliques</a></td><td>convention</td><td>observed</td><td>MaximalCliques omits a node without edges</td></tr><tr><td><a href="#f067">F067</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/paths-and-distances/diameter.html#diameter">Diameter</a></td><td>defect</td><td>observed</td><td>Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10%</td></tr><tr><td><a href="#f068">F068</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>Rank at isolated nodes is spread differently</td></tr><tr><td><a href="#f069">F069</a></td><td>NetworKit</td><td>11.2.2</td><td><a href="measures/centrality/strength.html#strength">Strength</a></td><td>convention</td><td>observed</td><td>weightedDegree counts out-edges only; a single node gets 0</td></tr><tr><td><a href="#f070">F070</a></td><td>ergm (statnet)</td><td>4.12.0</td><td><a href="measures/descriptive-statistics/density.html#density">Density</a></td><td>convention</td><td>observed</td><td>A network object holds each tie once and no loops</td></tr><tr><td><a href="#f071">F071</a></td><td>nauty</td><td>2.8.8</td><td><a href="measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp">Vf2pp</a></td><td>limitation</td><td>observed</td><td>Parallel edges are not representable</td></tr><tr><td><a href="#f072">F072</a></td><td>graspologic</td><td>3.4.4</td><td><a href="measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian">Gm laplacian</a></td><td>convention</td><td>observed</td><td>The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs</td></tr><tr><td><a href="#f073">F073</a></td><td>egor</td><td>1.25.10</td><td><a href="measures/mixing-and-assortativity/ei_index.html#ei_index">Ei index</a></td><td>convention</td><td>observed</td><td>comp_ei counts each neighbour once</td></tr><tr><td><a href="#f074">F074</a></td><td>igraph (Python)</td><td>1.0.0</td><td><a href="measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_nominal">Assortativity nominal</a></td><td>limitation</td><td>observed</td><td>assortativity_nominal(normalized=False) raises SystemError; eigenvector_centrality(directed=False) on a directed graph raises Invalid mode</td></tr><tr><td><a href="#f075">F075</a></td><td>igraph (Python)</td><td>1.0.0</td><td><a href="measures/centrality/katz_centrality.html#katz">Katz</a></td><td>limitation</td><td>observed</td><td>Alpha and power centrality exist only in the R binding</td></tr><tr><td><a href="#f076">F076</a></td><td>influenceR</td><td>0.1.5</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>influenceR betweenness counts both orderings of an undirected pair and reads directed graphs as undirected</td></tr><tr><td><a href="#f077">F077</a></td><td>centiserve</td><td>1.0.0</td><td><a href="measures/centrality/information_centrality.html#cx_current_flow_closeness">Current flow closeness</a></td><td>convention</td><td>observed</td><td>Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks</td></tr><tr><td><a href="#f078">F078</a></td><td>tnet</td><td>3.0.16</td><td><a href="measures/paths-and-distances/geodesic_distances.html#distances">Distances</a></td><td>defect</td><td>observed</td><td>Weighted distance and closeness with the alpha exponent differ from the definition</td></tr><tr><td><a href="#f079">F079</a></td><td>netrankr</td><td>2.0.0</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>depend_sp and depend_curflow count both orderings of an unordered pair</td></tr><tr><td><a href="#f080">F080</a></td><td>netrankr</td><td>2.0.0</td><td><a href="measures/centrality/information_centrality.html#information_centrality">Information centrality</a></td><td>convention</td><td>observed</td><td>dist_resist with invsum is the standard value divided by n</td></tr><tr><td><a href="#f081">F081</a></td><td>netrankr</td><td>2.0.0</td><td><a href="measures/centrality/closeness.html#closeness">Closeness</a></td><td>convention</td><td>observed</td><td>Empty distance sum inverts to 0</td></tr><tr><td><a href="#f082">F082</a></td><td>manynet</td><td>2.4.0</td><td><a href="measures/roles-and-positions/effective_size.html#effective_size">Effective size</a></td><td>defect</td><td>observed</td><td>Effective size and efficiency differ on directed networks and multigraphs with loops</td></tr><tr><td><a href="#f083">F083</a></td><td>manynet</td><td>2.4.0</td><td><a href="measures/roles-and-positions/hierarchy_krackhardt.html#hierarchy">Hierarchy</a></td><td>defect</td><td>observed</td><td>hierarchy differs from the definition on all 25 fixtures</td></tr><tr><td><a href="#f084">F084</a></td><td>blockmodeling</td><td>1.1.8</td><td><a href="measures/roles-and-positions/structural_equivalence.html#structural_equivalence">Structural equivalence</a></td><td>convention</td><td>observed</td><td>Profiles keep the entries for the two nodes themselves on asymmetric matrices</td></tr><tr><td><a href="#f085">F085</a></td><td>RSiena</td><td>1.6.6</td><td><a href="measures/statistical-fitting/saom_simulated_mean.html#saom_sim_mean">Saom sim mean</a></td><td>defect</td><td>observed</td><td>From a complete first wave the mean tie count stays at 5.0</td></tr><tr><td><a href="#f086">F086</a></td><td>GraphBLAS algorithms</td><td>2023.10.0</td><td><a href="measures/centrality/katz_centrality.html#katz">Katz</a></td><td>defect</td><td>observed</td><td>Katz loses beta at nodes without in-links</td></tr><tr><td><a href="#f087">F087</a></td><td>scikit-network</td><td>0.33.0</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>defect</td><td>observed</td><td>PageRank restart vector departs from the definition</td></tr><tr><td><a href="#f088">F088</a></td><td>GAP Benchmark Suite</td><td>941462c7c42e</td><td><a href="measures/centrality/pagerank.html#pagerank">Pagerank</a></td><td>convention</td><td>observed</td><td>Rank held by dangling vertices is not passed on</td></tr><tr><td><a href="#f089">F089</a></td><td>GAP Benchmark Suite</td><td>941462c7c42e</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>observed</td><td>The BC verifier uses a float-epsilon tolerance against its own float accumulation</td></tr><tr><td><a href="#f090">F090</a></td><td>graph-tool</td><td>3.9</td><td><a href="measures/centrality/betweenness.html#betweenness">Betweenness</a></td><td>convention</td><td>reported</td><td>Betweenness normalization can differ by a factor 2 from the Freeman convention</td></tr></tbody></table></div>

## F001 group\_betweenness\_centrality compares float path lengths exactly {#f001}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

**Entry:** [Group / betweenness](measures/centrality/group_betweenness.html#group-betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and weights): NetworkX counts parallel edges as one path. [Full reason](measures/centrality/group_betweenness.html#why-group-betweenness-networkx).

**Observed:** 7.0 on the directed 8-node graph in the reproduction; the 12-cycle with random weights gave 16 where the exact count is 14

**Expected:** 6.0 (pairs outside {0,1,2} with a shortest path through the group: (5,3),(5,4),(5,6),(7,3),(7,4),(7,6), one path each)

**Reproduction:**

```
import networkx as nx
G = nx.DiGraph(); G.add_nodes_from(range(8))
for (a, b), w in zip([(1,3),(3,6),(4,2),(5,7),(6,4),(7,1)], [4.498309,1.502522,1.633862,2.801985,4.238676,3.760802]):
    G.add_edge(a, b, weight=w)
nx.group_betweenness_centrality(G, [0,1,2], normalized=False, weight='weight')  # 7.0
for a, b, d in G.edges(data=True):
    d['weight'] = round(d['weight'] * 10**6)
nx.group_betweenness_centrality(G, [0,1,2], normalized=False, weight='weight')  # 6.0
```

**Notes:** Rounding of floating-point path lengths adds or drops shortest paths; scaling weights to integers gives the exact count.

## F002 prominent\_group misses the best group on disconnected graphs {#f002}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

**Entry:** [Prominent group](measures/centrality/group_prominence.html#nxo_prominent) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** prominent\_group(G, 2) returns (0.0, \[3, 0\])

**Expected:** group\_betweenness\_centrality(G, \[0, 2\]) is 1.0, so a better group exists

**Reproduction:**

```
import networkx as nx
G = nx.Graph(); G.add_nodes_from(range(4)); G.add_edges_from([(1,0),(3,0)])
nx.prominent_group(G, 2)  # (0.0, [3, 0])
nx.group_betweenness_centrality(G, [0, 2])  # 1.0
```

**Notes:** The exact search maximizes the value with endpoints included and subtracts the endpoint terms afterwards.

## F003 graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost {#f003}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

**Entry:** [Graph edit distance](measures/graph-theory-and-combinatorics/graph_edit_distance.html#ged) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** 0

**Expected:** 2 (G1: nodes 0, 1 and the loop (1,1); G2: the edge (0,1))

**Reproduction:**

```
import networkx as nx
G1 = nx.Graph([(1,1)]); G1.add_node(0)
G2 = nx.Graph([(0,1)])
nx.graph_edit_distance(G1, G2)  # 0
```

**Notes:** Observed on a loop-bearing graph pair of the shared fixture corpus.

## F004 goldberg\_radzik raises NetworkXUnbounded for any negative self-loop {#f004}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Entry:** [Bellman ford](measures/paths-and-distances/shortest_paths.html#ord_bellman_ford) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** NetworkXUnbounded, even when the loop is unreachable from the source

**Expected:** a negative self-loop that is unreachable from the source should not make the problem unbounded

**Notes:** bellman\_ford\_predecessor\_and\_distance was also checked and behaves the same way.

## F005 PageRank stops on an L1 change below n \* tol {#f005}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and weights): The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. [Full reason](measures/centrality/pagerank.html#why-pagerank-networkx).

**Observed:** absolute error 3.4e-11 (relative 4.2e-9) against the exact solution on a 2000-node directed graph, damping 0.85

**Expected:** a tighter error is available from the same iteration; rustworkx shows the same stopping rule

**Notes:** The stopping rule scales the tolerance with the number of nodes.

## F006 PageRank stops on an L1 change below n \* tol {#f006}

Tool: [rustworkx](tools/rustworkx.html) 0.18.1. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, normalization, self-loops and weights): rx.pagerank() takes a directed graph. [Full reason](measures/centrality/pagerank.html#why-pagerank-rustworkx).

**Observed:** same stopping rule as NetworkX

**Expected:** exact solution

**Notes:** Compared with an exact linear solve on a 2000-node directed graph.

## F007 Undirected self-loop is one arc {#f007}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and weights): The tool stops when the L1 change of the iterate falls below n \* tol, which leaves an error of a few 1e-9 relative on networks of thousands of nodes. [Full reason](measures/centrality/pagerank.html#why-pagerank-networkx).

**Observed:** path graph 0-1-2 with a loop at node 1: 0.5745 at node 1

**Expected:** 0.6316 when the loop counts as two edge ends (igraph convention)

**Reproduction:**

```
import networkx as nx
G = nx.Graph([(0,1),(1,2),(1,1)])
nx.pagerank(G)[1]  # 0.5745
```

**Notes:** rustworkx and JGraphT follow the one-arc reading; Graph and MultiGraph agree in NetworkX.

## F008 Undirected self-loop is one arc {#f008}

Tool: [rustworkx](tools/rustworkx.html) 0.18.1. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, normalization, self-loops and weights): rx.pagerank() takes a directed graph. [Full reason](measures/centrality/pagerank.html#why-pagerank-rustworkx).

**Observed:** same as NetworkX: the loop adds 1 to the node's out-degree

**Expected:** two edge ends on the diagonal (igraph)

**Notes:** See the NetworkX entry.

## F009 Undirected self-loop is one arc {#f009}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** same as NetworkX

**Expected:** two edge ends on the diagonal (igraph)

**Notes:** See the NetworkX entry.

## F010 Walktrap skips minimal merge pairs on mid-size random networks {#f010}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: defect. Status: observed.

**Entry:** [Walktrap](measures/communities/walktrap.html#walktrap) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, multi-edges, self-loops, ties and weights): exact ties between pairs of groups occur during the merges, which the reference breaks by group names and igraph by an undocumented rule. [Full reason](measures/communities/walktrap.html#why-walktrap-igraph).

**Observed:** igraph merges a pair above the minimum (by more than a relative 1e-9) in 179 of 1999 merges (2000-node G(n,m)), 23 of 2498, 557 of 999 (dense, 1000 nodes) and 771 of 3999 (4000-node block model); the skipped pair joins a node to the group created by the preceding merge

**Expected:** merge the pair with the minimum delta sigma = \|C1\|\|C2\|/(\|C1\|+\|C2\|) r^2 / n (Pons and Latapy 2006)

**Notes:** Found by replaying igraph's merge sequence and evaluating the definition. Greedy-minimum sequence best level modularity 0.21065583 against igraph 0.21138759 on the 2000-node case; the direction of the difference varies. Mechanism unknown (the tool was used as a black box).

References: [pons2006computing](references.html#pons2006computing)

## F011 Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance {#f011}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Entry:** [Leading eigen](measures/communities/modularity_maximization.html#leading_eigen) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, multi-edges, self-loops and ties): On a disconnected network the leading eigenvector of a division's modularity matrix can be degenerate (components with equal eigenvalues, zero... [Full reason](measures/communities/modularity_maximization.html#why-leading_eigen-igraph).

**Observed:** 0.5404499 on Les Miserables (weighted)

**Expected:** 0.5404514 from the exact eigenvector

**Notes:** Attributed to ARPACK's tolerance on a near-zero eigenvector entry.

## F012 Weighted distances (binary = FALSE) are not shortest-path lengths {#f012}

Tool: [keyplayer](tools/keyplayer.html) 1.0.4. Kind: defect. Status: observed.

**Entry:** [Kpp\_single / distance\_reach](measures/centrality/key_player_single.html#kpp_single-distance_reach) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and weights): keyplayer's weighted distances are not the Dijkstra shortest-path lengths: on a probe graph its closeness-based reach lies 2 to 5 percent below the... [Full reason](measures/centrality/key_player_single.html#why-kpp_single-distance_reach-keyplayer).

**Observed:** reach 0.4485 on an 8-node probe

**Expected:** 0.4655 with exact shortest paths and edge values as lengths

**Notes:** The tool was used as a black box; the cause is unknown.

## F013 communibet() cannot find an installed expm {#f013}

Tool: [centiserve](tools/centiserve.html) 1.0.0. Kind: defect. Status: reproduced.

**Entry:** [Communicability betweenness](measures/centrality/communicability_betweenness.html#cx_communicability_betweenness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** error from requireNamespace

**Expected:** a value; a patched copy gives matching values on connected networks and NaN on disconnected ones

**Notes:** The function passes library() arguments to requireNamespace, which rejects them.

## F014 Eigenvector centrality is not converged {#f014}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: defect. Status: reproduced.

**Entry:** [Eigenvector](measures/centrality/eigenvector_centrality.html#eigenvector) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, normalization, self-loops, ties and weights): Gephi runs a fixed number of power-iteration steps (setNumRuns, here 10^6) without a convergence test, and its result is not the converged... [Full reason](measures/centrality/eigenvector_centrality.html#why-eigenvector-gephi).

**Observed:** karate, node 0: k=1: 0.941; k=100: 0.957540; k=1000: 0.953256; k=10^5: 0.952067; k=10^6: 0.952061; k=10^8: 0.952103

**Expected:** 0.952132

**Reproduction:**

```
Call setNumRuns(k) on the eigenvector statistic; the number of runs is a power-iteration step count with no stopping test.
```

**Notes:** Error of order 1e-3 to 1e-5 that shrinks very slowly; disconnected networks fare worse (Les Miserables 1.3e-2).

References: [bonacich1987power](references.html#bonacich1987power)

## F015 Louvain with setRandom(false) is not reproducible {#f015}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: defect. Status: reproduced.

**Entry:** [Louvain quality](measures/communities/modularity_maximization.html#louvain_quality) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and self-loops): With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept). [Full reason](measures/communities/modularity_maximization.html#why-louvain_quality-gephi).

**Observed:** karate modularity 0.3950, 0.4156, 0.4033, ... on repeated runs in one JVM

**Expected:** identical results for identical input

**Reproduction:**

```
Repeat the statistic on the same graph in one JVM with setRandom(false).
```

**Notes:** Results follow the identity hash order of objects the statistic creates, so a fresh JVM's main thread repeats; pooled threads or earlier work do not. Means of 20 runs ranged 0.3522 to 0.3632 on a weighted graph.

References: [blondel2008fast](references.html#blondel2008fast)

## F016 Louvain sometimes does not return {#f016}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: defect. Status: reproduced.

**Entry:** [Louvain quality](measures/communities/modularity_maximization.html#louvain_quality) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and self-loops): With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept). [Full reason](measures/communities/modularity_maximization.html#why-louvain_quality-gephi).

**Observed:** on a triangle, 2 of 100 repetitions did not return within 3 s (8 of 100 on a triangle plus an isolated node)

**Expected:** a result on every run

**Reproduction:**

```
On a fresh graph with edges 0-1, 1-2, 0-2: new Modularity(); setRandom(false); setResolution(1.0); execute(graphModel); repeat 100 times.
```

**Notes:** 0 of 100 on a single edge, two edges, or two nodes without edges.

References: [blondel2008fast](references.html#blondel2008fast)

## F017 PageRank loses probability mass at self-loops {#f017}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: defect. Status: reproduced.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-defect" href="method.html#state-checked-defect"><span class="g" aria-hidden="true">✗</span>checked, defect</a> Defect: PageRank loses probability mass at self-loops; scores do not sum to 1 (finding F017). [Full reason](measures/centrality/pagerank.html#why-pagerank-gephi).

**Observed:** undirected edges 0-0, 0-1, 1-2, damping 0.85: scores 0.1375, 0.2058, 0.1375 (sum 0.4807); directed arcs 0&gt;0, 0&gt;1, 1&gt;0: 0.5, 0.2875 (sum 0.7875)

**Expected:** scores that sum to 1 (they do without the loop)

**Reproduction:**

```
Run PageRank with epsilon 1e-14 on the graphs above.
```

**Notes:** Two larger fixtures with loops sum to 0.545 and 0.496.

## F018 Closeness is reached/sum of distances; 0 for a node reaching nobody {#f018}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction and normalization): Gephi gives 0 to a node that reaches no other node. [Full reason](measures/centrality/closeness.html#why-closeness-gephi).

**Observed:** (nodes reached)/(sum of distances); setNormalized has no effect on closeness

**Expected:** (n-1)/(sum of distances) with undefined for nodes that reach nobody

**Notes:** Harmonic closeness is sum(1/d)/(nodes reached).

References: [freeman1978centrality](references.html#freeman1978centrality)

## F019 HITS uses unit Euclidean scaling and ignores self-loops {#f019}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Entry:** [Hits](measures/centrality/hits.html#hits) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, normalization and self-loops): Gephi scales the hub and authority vectors to unit Euclidean length. [Full reason](measures/centrality/hits.html#why-hits-gephi).

**Observed:** unit-length vectors; 0 on an edgeless network

**Expected:** tool-specific scaling

References: [kleinberg1999authoritative](references.html#kleinberg1999authoritative)

## F020 Degree counts a self-loop twice {#f020}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Entry:** [Degree](measures/centrality/degree.html#degree) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** loop adds 2

**Notes:** Betweenness, eccentricity, radius, diameter, density and components agree with the definition.

## F021 Average clustering leaves out nodes of degree below 2 {#f021}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Entry:** [Average clustering](measures/descriptive-statistics/local_clustering.html#average_clustering) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and self-loops): Gephi counts a self-loop in a node's neighbourhood: with the loops removed (parallel edges kept) its coefficients and triangle counts equal the... [Full reason](measures/descriptive-statistics/local_clustering.html#why-average_clustering-gephi).

**Observed:** nodes of degree 0 or 1 are excluded from the average (their local value is 0)

**Expected:** average over all nodes with local value 0 for those nodes

## F022 Louvain resolution acts as the reciprocal of gamma {#f022}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Entry:** [Louvain quality](measures/communities/modularity_maximization.html#louvain_quality) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and self-loops): With self-loops Gephi's modularity changes (mean of 20 runs 0.249 with the loops, 0.321 with the loops removed and parallel edges kept). [Full reason](measures/communities/modularity_maximization.html#why-louvain_quality-gephi).

**Observed:** getModularity() always returns the gamma = 1 modularity

**Expected:** modularity at the requested resolution

**Notes:** No resolution value other than 1 can be compared.

References: [blondel2008fast](references.html#blondel2008fast)

## F023 hyper\_wiener\_index is twice the published value {#f023}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Entry:** [Index](measures/paths-and-distances/wiener_index.html#dm_index) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** twice the value of the defining formula (Randic 1993)

**Expected:** published value

**Notes:** Also affects schultz\_index and gutman\_index conventions noted in their documentation.

References: [randic1993novel](references.html#randic1993novel)

## F024 edge\_betweenness\_centrality\_subset deviates from its documented formula {#f024}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Entry:** [Betweenness subset](measures/centrality/betweenness.html#cx_betweenness_subset) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges): NetworkX counts a pair of adjacent nodes once however many parallel edges join them. [Full reason](measures/centrality/betweenness.html#why-cx_betweenness_subset-networkx).

**Observed:** values differ from the documented subset definition

**Expected:** documented formula

**Notes:** Observed on the shared fixture corpus.

## F025 effective\_size is wrong for weighted or directed graphs on its vectorized path {#f025}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Entry:** [Effective size](measures/roles-and-positions/effective_size.html#effective_size) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (self-loops, ties and weights): NetworkX keeps self-loops in the adjacency matrix, so a loop adds to the node's tie volume and can be its strongest tie. [Full reason](measures/roles-and-positions/effective_size.html#why-effective_size-networkx).

**Observed:** values differ from Burt's definition

**Expected:** Burt's effective size

References: [burt1992structural](references.html#burt1992structural)

## F026 Network simplex can misreport feasibility with float weights {#f026}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Observed:** infeasible reported for a feasible instance

**Expected:** feasible

## F027 maximum\_spanning\_arborescence occasionally misses the maximum {#f027}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Observed:** a lighter arborescence than the optimum on some inputs

**Expected:** maximum-weight arborescence

## F028 k\_edge\_components hits the recursion limit near n = 1000 {#f028}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: limitation. Status: observed.

**Entry:** [K edge components](measures/components-and-connectivity/k_edge_components.html#k_edge_components) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** RecursionError

**Expected:** a result

## F029 Ties are broken by Python set or insertion order {#f029}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Label propagation](measures/communities/label_propagation.html#label_propagation) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, multi-edges and self-loops): NetworkX runs on the simple graph here, while the reference counts parallel edges with their multiplicity. [Full reason](measures/communities/label_propagation.html#why-label_propagation-networkx).

**Observed:** results depend on iteration order

**Expected:** tie rule not specified by the published algorithm

**Notes:** Same for greedy modularity, lowest common ancestors, dispersion, shortest-path choice and minimum cuts.

## F030 group\_betweenness\_centrality can vary with PYTHONHASHSEED {#f030}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Entry:** [Group / betweenness](measures/centrality/group_betweenness.html#group-betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and weights): NetworkX counts parallel edges as one path. [Full reason](measures/centrality/group_betweenness.html#why-group-betweenness-networkx).

**Observed:** results vary with the hash seed on some inputs

**Expected:** one value

**Notes:** Reported separately from the weighted float-comparison finding above.

## F031 approximation.node\_connectivity starts from a bound that can exceed the connectivity {#f031}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

**Entry:** [Node connectivity](measures/components-and-connectivity/node_connectivity.html#ap_node_connectivity) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** 2 for one node with a self-loop (6 for the complete digraph on 4 nodes)

**Expected:** 0 for one node with a loop (3 for the complete digraph on 4 nodes)

**Reproduction:**

```
import networkx as nx
G = nx.Graph(); G.add_edge(0,0)
nx.approximation.node_connectivity(G)  # 2
```

**Notes:** The starting bound counts a self-loop twice and uses out- plus in-degree in a digraph.

## F032 cd\_index pools every citer of the references, whatever its time {#f032}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [CD index](measures/traversal-trees-and-dags/cd_index.html#nxs_cd_index) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and direction): NetworkX sums over every citer published up to the end of the window, including citers published before the focal node, and counts in the pool n... [Full reason](measures/traversal-trees-and-dags/cd_index.html#why-nxs_cd_index-networkx).

**Observed:** on nodes 0, 1 with the arc 0 -&gt; 1 NetworkX gives 1

**Expected:** undefined in the published definition (Funk and Owen-Smith 2017), whose window excludes earlier citers

**Notes:** Publication times were a fixed function of the node id.

References: [funk2017dynamic](references.html#funk2017dynamic)

## F033 Weighted betweenness counts one shortest path per neighbour pair with parallel edges {#f033}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges, normalization, ties and weights): NetworkX traverses neighbor sets, so parallel edges count as a single shortest path. [Full reason](measures/centrality/betweenness.html#why-betweenness-networkx).

**Observed:** node 1 gets 1/2 on arcs 0-&gt;1 twice, 1-&gt;2, 0-&gt;3, 3-&gt;2

**Expected:** 2/3 when each parallel edge is a distinct path (igraph, NetworKit)

References: [brandes2001faster](references.html#brandes2001faster)

## F034 hypercube\_graph nodes are bit tuples; dimension 0 is the null graph {#f034}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Implicit family](measures/generators-and-rewiring/circulant_ring_graphs.html#implicit_family) <a class="st st-t st-nov" href="method.html#state-checked-no-value"><span class="g" aria-hidden="true">∅</span>checked, no value on some inputs</a> Checked, no comparison counts recorded for this entry. [Full reason](measures/generators-and-rewiring/circulant_ring_graphs.html#why-implicit_family-networkx).

**Observed:** tuple labels

**Expected:** integer labels from reading the tuple as a number

## F035 Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input {#f035}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Entry:** [Modularity](measures/communities/modularity.html#modularity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): NetworkX returns 0 for a network without edges. [Full reason](measures/communities/modularity.html#why-modularity-networkx).

**Observed:** 0

**Expected:** undefined (0/0)

## F036 Adjusted Rand index is NaN on all-singleton partitions {#f036}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Entry:** [Compare partitions](measures/communities/compare_partitions.html#compare_partitions) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): on two nodes both fixed partitions are all singletons, so the two are identical and Hubert and Arabie's formula is 0/0. [Full reason](measures/communities/compare_partitions.html#why-compare_partitions-igraph).

**Observed:** NaN

**Expected:** 0/0 in the definition of Hubert and Arabie (1985); scikit-learn returns 1

References: [hubert1985comparing](references.html#hubert1985comparing)

## F037 Adjusted Rand index is 1 on degenerate partitions {#f037}

Tool: [cdlib](tools/cdlib.html) 0.4.1. Kind: convention. Status: observed.

**Entry:** [Compare partitions](measures/communities/compare_partitions.html#compare_partitions) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): For partitions of one element cdlib (through scikit-learn) returns 1.0. [Full reason](measures/communities/compare_partitions.html#why-compare_partitions-cdlib).

**Observed:** 1

**Expected:** 0/0 in the definition

References: [hubert1985comparing](references.html#hubert1985comparing)

## F038 Spinglass reads the network as simple {#f038}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Entry:** [Spinglass](measures/communities/spinglass.html#spinglass) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** two parallel edges on two nodes give -0.5

**Expected:** -1 for the multigraph Hamiltonian

## F039 Triad census on multigraphs differs from the definition {#f039}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: defect. Status: observed.

**Entry:** [Triad census](measures/descriptive-statistics/triad_census.html#triad_census) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges and ties): igraph's triad census does not support multigraphs: parallel edges change its counts. [Full reason](measures/descriptive-statistics/triad_census.html#why-triad_census-igraph).

**Observed:** values differ when parallel edges exist

**Expected:** triad census of the underlying simple digraph or a documented rule

## F040 HITS returns 1 for an edgeless network {#f040}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Entry:** [Hits](measures/centrality/hits.html#hits) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and ties): Without ties the scores are undefined (reference NaN, igraph fills in values). [Full reason](measures/centrality/hits.html#why-hits-igraph).

**Observed:** 1

**Expected:** undefined

References: [kleinberg1999authoritative](references.html#kleinberg1999authoritative)

## F041 Information centrality fails on singular inputs {#f041}

Tool: [sna](tools/sna.html) 2.8. Kind: defect. Status: observed.

**Entry:** [Information centrality](measures/centrality/information_centrality.html#information_centrality) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, self-loops, ties and weights): On networks with more than one component sna's results differ from Stephenson and Zelen's formula as evaluated exactly by the definition oracle,... [Full reason](measures/centrality/information_centrality.html#why-information_centrality-sna).

**Observed:** error or invalid values on disconnected or valued directed networks

**Expected:** a documented rule for singular matrices

## F042 Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default {#f042}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Entry:** [Degree](measures/centrality/degree.html#degree) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, multi-edges and self-loops): sna works on adjacency matrices, so parallel edges collapse to one, and it ignores the diagonal by default (diag = FALSE). [Full reason](measures/centrality/degree.html#why-degree-sna).

**Observed:** parallel edges count once; loops ignored (diag = FALSE)

**Expected:** edge-list degree counts every edge end

**Notes:** Applies to in-degree, out-degree and density.

## F043 Closeness and centralization normalizations differ from other tools {#f043}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** tool-specific normalizing constants

**Notes:** Also differs from UCINET's documented normalizations.

References: [freeman1978centrality](references.html#freeman1978centrality)

## F044 Reciprocity correlation is 0 on a single arc {#f044}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Entry:** [Reciprocity](measures/descriptive-statistics/reciprocity.html#reciprocity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction and ties): On a two-node network with one arc the two ordered pairs give the perfectly anticorrelated values (1, 0) and (0, 1), so the correlation is -1, as... [Full reason](measures/descriptive-statistics/reciprocity.html#why-reciprocity-sna).

**Observed:** 0

**Expected:** -1 (the correlation)

## F045 Normalized betweenness divides by (n-1)(n-2) in undirected graphs {#f045}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction and normalization): JGraphT normalizes the undirected betweenness by (n-1)(n-2) rather than (n-1)(n-2)/2: every nonzero value on all 16 undirected networks with at... [Full reason](measures/centrality/betweenness.html#why-betweenness-jgrapht).

**Observed:** exactly half the standard value on 16 undirected fixtures with n &gt;= 3 (raw betweenness agrees)

**Expected:** raw / ((n-1)(n-2)/2)

References: [brandes2001faster](references.html#brandes2001faster)

## F046 relative\_betweenness\_centrality is twice the standard value on directed graphs {#f046}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction and normalization): relative\_betweenness\_centrality gives exactly twice the reference value's normalized value on every directed network (checked on all six directed... [Full reason](measures/centrality/betweenness.html#why-betweenness-boost).

**Observed:** ratio 2 on 6 directed fixtures with n &gt;= 3 (undirected agrees); 0/0 = NaN below 3 nodes

**Expected:** standard value; 0 below 3 nodes in NetworkX

References: [brandes2001faster](references.html#brandes2001faster)

## F047 Closeness is 0 for a node that cannot reach every other node {#f047}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): JGraphT's closeness is exactly 0 for a node that does not reach every other node, and Infinity for the lone node of a one-node network (checked on... [Full reason](measures/centrality/closeness.html#why-closeness-jgrapht).

**Observed:** 0 for any node not reaching all; Infinity for the single node of a one-node network

**Expected:** reachable-only sum

References: [freeman1978centrality](references.html#freeman1978centrality)

## F048 Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair {#f048}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): BGL's closeness is 1 / (sum of distances) with DBL\_MAX standing in for an unreachable distance, so a node that cannot reach every other node gets... [Full reason](measures/centrality/closeness.html#why-closeness-boost).

**Observed:** about 5.6e-309 for unreachable cases; Infinity on one node; equals the unnormalized closeness on connected networks

**Expected:** normalized (n-1)/sum

References: [freeman1978centrality](references.html#freeman1978centrality)

## F049 Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable {#f049}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Entry:** [Eccentricity](measures/paths-and-distances/eccentricity.html#eccentricity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction): JGraphT's GraphMeasurer follows edge direction and returns Infinity for a node that cannot reach every other node. [Full reason](measures/paths-and-distances/eccentricity.html#why-eccentricity-jgrapht).

**Observed:** Infinity

**Expected:** longest finite shortest path

## F050 Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable {#f050}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Entry:** [Eccentricity](measures/paths-and-distances/eccentricity.html#eccentricity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction): BGL's all\_eccentricities and radius\_and\_diameter follow edge direction and give DBL\_MAX for a node that cannot reach every other node. [Full reason](measures/paths-and-distances/eccentricity.html#why-eccentricity-boost).

**Observed:** DBL\_MAX

**Expected:** longest finite shortest path

## F051 Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs {#f051}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Entry:** [Clustering](measures/descriptive-statistics/local_clustering.html#clustering) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction, multi-edges, self-loops and ties): JGraphT's local clustering on a directed graph counts ordered pairs of neighbours (denominator k(k-1) per arc direction), while the reference, like... [Full reason](measures/descriptive-statistics/local_clustering.html#why-clustering-jgrapht).

**Observed:** half the undirected-neighbourhood value on directed input

**Notes:** Agrees on fully reciprocated and simple undirected networks.

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F052 Clustering counts loops and parallel edges as extra neighbours {#f052}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Entry:** [Clustering](measures/descriptive-statistics/local_clustering.html#clustering) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction, multi-edges and self-loops): BGL's clustering\_coefficient counts parallel edges and loops as extra neighbours. [Full reason](measures/descriptive-statistics/local_clustering.html#why-clustering-boost).

**Observed:** extra neighbours

**Expected:** simple-graph value

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F053 Transitivity refuses directed input {#f053}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: limitation. Status: observed.

**Entry:** [Transitivity](measures/descriptive-statistics/global_transitivity.html#transitivity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction, multi-edges and self-loops): JGraphT counts loops and parallel edges as extra neighbours/triangles in a pseudograph. [Full reason](measures/descriptive-statistics/global_transitivity.html#why-transitivity-jgrapht).

**Observed:** "Graph must be undirected"; NaN when there is no connected triple

## F054 Coreness and clique finders refuse non-simple input {#f054}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: limitation. Status: observed.

**Entry:** [Coreness](measures/cohesion-and-subgroups/k_core.html#coreness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** "Graph must be simple"; coreness refuses directed input; the clique finder accepts directed input but does not return the maximal cliques of the underlying graph

## F055 Betweenness counts ordered pairs on undirected networks {#f055}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction, multi-edges, normalization, self-loops, ties and weights): BCT's betweenness\_bin counts ordered pairs, so an undirected network's value is exactly twice the reference value's (checked on every undirected... [Full reason](measures/centrality/betweenness.html#why-betweenness-bct).

**Observed:** exactly twice the standard value

**Expected:** each unordered pair once

References: [brandes2001faster](references.html#brandes2001faster)

## F056 clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients {#f056}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Entry:** [Clustering](measures/descriptive-statistics/local_clustering.html#clustering) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction): BCT's directed variants (clustering\_coef\_bd, transitivity\_bd) are Fagiolo's directed coefficients, which weigh the in/out/cycle/middleman triangle... [Full reason](measures/descriptive-statistics/local_clustering.html#why-clustering-bct).

**Observed:** values differ from the undirected-neighbourhood value on 5 directed fixtures

**Notes:** Undirected simple networks agree.

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F057 charpath takes the longest finite distance; NaN for a node reaching nobody {#f057}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Entry:** [Eccentricity](measures/paths-and-distances/eccentricity.html#eccentricity) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults and direction): charpath(distance\_bin(A), 0, 0) takes the longest finite distance and gives NaN to a node that reaches nobody. [Full reason](measures/paths-and-distances/eccentricity.html#why-eccentricity-bct).

**Observed:** NaN diameter for an edgeless network; radius ignores nodes reaching nobody

## F058 Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target {#f058}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Entry:** [Assortativity degree](measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_degree) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, self-loops, ties and weights): BCT returns NaN where the degree variance is zero (regular networks, a single node). [Full reason](measures/mixing-and-assortativity/assortativity_coefficient.html#why-assortativity_degree-bct).

**Observed:** differences of 0.1% to 14% on 4 directed fixtures

**Expected:** Pearson correlation

**Notes:** Cause not identified.

References: [newman2002assortative](references.html#newman2002assortative)

## F059 Matrix-input calls carry no loops or parallel edges {#f059}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Entry:** [Degree](measures/centrality/degree.html#degree) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction, multi-edges, self-loops and ties): A bct call takes a binary adjacency matrix, which cannot carry loops or parallel edges: the driver keeps one arc per ordered pair and drops loops,... [Full reason](measures/centrality/degree.html#why-degree-bct).

**Observed:** degree, coreness and local efficiency differ on multigraph inputs

## F060 Undirected betweenness scores both orderings of a pair {#f060}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** twice the standard value

**Expected:** each unordered pair once

References: [brandes2001faster](references.html#brandes2001faster)

## F061 Closeness returns (n-1)/sum of distances whatever normalized says {#f061}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** 1.0 on every node of K6 with normalized = False; ratio exactly n-1 on karate

**Expected:** unnormalized 1/sum of distances

References: [freeman1978centrality](references.html#freeman1978centrality)

## F062 edgeScores() follow NetworKit's own edge numbering {#f062}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Edge betweenness](measures/centrality/edge_betweenness.html#edge_betweenness) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** not the input edge order

**Notes:** Scores agree to 1e-14 after mapping by endpoints.

## F063 Katz and degree assortativity differ by 2% to 40% {#f063}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Entry:** [Katz](measures/centrality/katz_centrality.html#katz) <a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [Full reason](measures/centrality/katz_centrality.html#why-katz-networkit).

**Observed:** differences on 7 to 11 fixtures each

**Expected:** definition

**Notes:** Cause not identified.

References: [katz1953new](references.html#katz1953new)

## F064 Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs {#f064}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Entry:** [Eigenvector](measures/centrality/eigenvector_centrality.html#eigenvector) <a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [Full reason](measures/centrality/eigenvector_centrality.html#why-eigenvector-networkit).

**Observed:** differences of 6% to 90% on 7 to 11 fixtures

**Expected:** converged eigenvector

References: [bonacich1987power](references.html#bonacich1987power)

## F065 Loops, parallel edges and directed input are counted differently {#f065}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Degree](measures/centrality/degree.html#degree) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** k-core on a directed graph ignores direction; degenerate inputs (no edges, two nodes) return sentinel values

## F066 MaximalCliques omits a node without edges {#f066}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Max cliques](measures/cohesion-and-subgroups/maximal_cliques.html#max_cliques) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** isolates missing

**Expected:** a clique of one node

## F067 Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10% {#f067}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Entry:** [Diameter](measures/paths-and-distances/diameter.html#diameter) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** 12.0 against 12.5

**Expected:** 12.5

**Notes:** Cause not identified.

## F068 Rank at isolated nodes is spread differently {#f068}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** a 5% difference on a sparse random graph

## F069 weightedDegree counts out-edges only; a single node gets 0 {#f069}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Entry:** [Strength](measures/centrality/strength.html#strength) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Expected:** in plus out for directed input; undefined for one node

## F070 A network object holds each tie once and no loops {#f070}

Tool: [ergm (statnet)](tools/ergm.html) 4.12.0. Kind: convention. Status: observed.

**Entry:** [Density](measures/descriptive-statistics/density.html#density) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (multi-edges, self-loops and ties): A network object holds each tie once and no loops (multiple = FALSE, loops = FALSE), so the edge count drops parallel edges and loops that this... [Full reason](measures/descriptive-statistics/density.html#why-density-ergm).

**Observed:** edge count lower than a multigraph's

**Expected:** edge count including parallel edges

## F071 Parallel edges are not representable {#f071}

Tool: [nauty](tools/nauty.html) 2.8.8. Kind: limitation. Status: observed.

**Entry:** [Vf2pp](measures/graph-theory-and-combinatorics/graph_isomorphism.html#vf2pp) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** undefined on networks with parallel edges

## F072 The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs {#f072}

Tool: [graspologic](tools/graspologic.html) 3.4.4. Kind: convention. Status: observed.

**Entry:** [Gm laplacian](measures/matrices-and-spectra/laplacian_matrix.html#gm_laplacian) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction): For a directed graph graspologic's 'I-DAD' form is D\_in^-1/2 (D\_in - A) D\_in^-1/2 with in-degrees (graspologic/utils/utils.py, to\_laplacian), and a... [Full reason](measures/matrices-and-spectra/laplacian_matrix.html#why-gm_laplacian-graspologic).

**Observed:** a node without in-links gets 0 on the diagonal

**Expected:** out-degree normalization (NetworkX)

**Notes:** Undirected agree.

## F073 comp\_ei counts each neighbour once {#f073}

Tool: [egor](tools/egor.html) 1.25.10. Kind: convention. Status: observed.

**Entry:** [Ei index](measures/mixing-and-assortativity/ei_index.html#ei_index) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, self-loops and ties): egor's comp\_ei() counts alters, each neighbour once whatever the number or direction of the ties to it, and no self-loop. [Full reason](measures/mixing-and-assortativity/ei_index.html#why-ei_index-egor).

**Observed:** one count per neighbour whatever the number or direction of ties

**Expected:** count of ties

**Notes:** Directed and multi-edge fixtures differ.

## F074 assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode {#f074}

Tool: [igraph (Python)](tools/pyigraph.html) 1.0.0. Kind: limitation. Status: observed.

**Entry:** [Assortativity nominal](measures/mixing-and-assortativity/assortativity_coefficient.html#assortativity_nominal) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** error on every fixture

**Expected:** a value

## F075 Alpha and power centrality exist only in the R binding {#f075}

Tool: [igraph (Python)](tools/pyigraph.html) 1.0.0. Kind: limitation. Status: observed.

**Observed:** no Python function

References: [katz1953new](references.html#katz1953new)

## F076 influenceR betweenness counts both orderings of an undirected pair and reads directed graphs as undirected {#f076}

Tool: [influenceR](tools/influencer.html) 0.1.5. Kind: convention. Status: observed.

**Observed:** twice the standard value; bridging, Burt constraint and effective size differ on simple undirected networks (constraint by 1% to 2%, bridging by orders of magnitude)

**Expected:** definition

References: [brandes2001faster](references.html#brandes2001faster)

## F077 Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks {#f077}

Tool: [centiserve](tools/centiserve.html) 1.0.0. Kind: convention. Status: observed.

**Entry:** [Current flow closeness](measures/centrality/information_centrality.html#cx_current_flow_closeness) <a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [Full reason](measures/centrality/information_centrality.html#why-cx_current_flow_closeness-centiserve).

**Observed:** ratio 31 on a two-mode fixture; ratio 2.0 on a dense random graph

**Notes:** The raw Laplacian also differs on a fixture with loops.

## F078 Weighted distance and closeness with the alpha exponent differ from the definition {#f078}

Tool: [tnet](tools/tnet.html) 3.0.16. Kind: defect. Status: observed.

**Entry:** [Distances](measures/paths-and-distances/geodesic_distances.html#distances) <a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [Full reason](measures/paths-and-distances/geodesic_distances.html#why-distances-tnet).

**Observed:** differences on 7 weighted fixtures each

**Notes:** Cause not identified.

## F079 depend\_sp and depend\_curflow count both orderings of an unordered pair {#f079}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, self-loops, ties and weights): netrankr reads the simple undirected graph (parallel edges collapsed, loops dropped), while the reference counts parallel edges as distinct shortest... [Full reason](measures/centrality/betweenness.html#why-betweenness-netrankr).

**Observed:** twice the standard value; parallel edges and loops dropped

References: [brandes2001faster](references.html#brandes2001faster)

## F080 dist\_resist with invsum is the standard value divided by n {#f080}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Entry:** [Information centrality](measures/centrality/information_centrality.html#information_centrality) <a class="st st-t st-ok" href="method.html#state-checked-agrees"><span class="g" aria-hidden="true">✓</span>checked, agrees</a> Agrees with the reference value on every compared input.

**Observed:** ratio n on all connected fixtures

## F081 Empty distance sum inverts to 0 {#f081}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Entry:** [Closeness](measures/centrality/closeness.html#closeness) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction and weights): netrankr takes 1 over the sum of the finite and infinite distances, so a node that does not reach every other node gets 0 (an isolated node too). [Full reason](measures/centrality/closeness.html#why-closeness-netrankr).

**Observed:** 0 for nodes without reachable nodes

**Expected:** NaN (igraph)

References: [freeman1978centrality](references.html#freeman1978centrality)

## F082 Effective size and efficiency differ on directed networks and multigraphs with loops {#f082}

Tool: [manynet](tools/manynet.html) 2.4.0. Kind: defect. Status: observed.

**Entry:** [Effective size](measures/roles-and-positions/effective_size.html#effective_size) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults, direction, multi-edges, normalization, self-loops and ties): manynet (netrics) returns a different value from the reference on directed networks, on multigraphs with loops, and on the two-node network (about... [Full reason](measures/roles-and-positions/effective_size.html#why-effective_size-manynet).

**Observed:** half the standard value on a directed cycle

**Notes:** Simple undirected networks agree; cause not traced.

References: [burt1992structural](references.html#burt1992structural)

## F083 hierarchy differs from the definition on all 25 fixtures {#f083}

Tool: [manynet](tools/manynet.html) 2.4.0. Kind: defect. Status: observed.

**Observed:** 0.0285 against 0.0875 on karate; 0 where no value exists

## F084 Profiles keep the entries for the two nodes themselves on asymmetric matrices {#f084}

Tool: [blockmodeling](tools/blockmodeling.html) 1.1.8. Kind: convention. Status: observed.

**Entry:** [Structural equivalence](measures/roles-and-positions/structural_equivalence.html#structural_equivalence) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction): On a symmetric matrix (every undirected fixture and complete5\_dir) blockmodeling::sedist agrees with the reference. [Full reason](measures/roles-and-positions/structural_equivalence.html#why-structural_equivalence-blockmodeling).

**Observed:** 7 directed fixtures differ; 20 others agree

## F085 From a complete first wave the mean tie count stays at 5.0 {#f085}

Tool: [RSiena](tools/rsiena.html) 1.6.6. Kind: defect. Status: observed.

**Entry:** [Saom sim mean](measures/statistical-fitting/saom_simulated_mean.html#saom_sim_mean) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (ties): From a complete starting network RSiena returns a mean tie count of about 5.0 (the stationary value of the model, 5.4), where the reference value... [Full reason](measures/statistical-fitting/saom_simulated_mean.html#why-saom_sim_mean-rsiena).

**Observed:** 5.0 on the 5-node complete digraph

**Expected:** relaxes to 9.3 (one tie removed agrees)

**Notes:** Cause not identified.

## F086 Katz loses beta at nodes without in-links {#f086}

Tool: [GraphBLAS algorithms](tools/graphblas.html) 2023.10.0. Kind: defect. Status: observed.

**Entry:** [Katz](measures/centrality/katz_centrality.html#katz) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (direction and multi-edges): graphblas-algorithms' katz\_centrality drops the beta term for nodes that have no in-links (they get no entry in the sparse result, read as 0), so... [Full reason](measures/centrality/katz_centrality.html#why-katz-graphblas).

**Expected:** definition

**Notes:** Beta lost at nodes without in-links; also 0 for PageRank, HITS, Katz on edgeless input.

References: [katz1953new](references.html#katz1953new)

## F087 PageRank restart vector departs from the definition {#f087}

Tool: [scikit-network](tools/sknetwork.html) 0.33.0. Kind: defect. Status: observed.

**Entry:** [Pagerank](measures/centrality/pagerank.html#pagerank) <a class="st st-t st-conv" href="method.html#state-checked-convention"><span class="g" aria-hidden="true">≠</span>checked, differs by convention</a> Differs by convention (defaults): scikit-network's random-surfer operator weights the restart vector by each node's own out-degree status, b\_i = (1 - d \[i has out-links\]) y\_i... [Full reason](measures/centrality/pagerank.html#why-pagerank-sknetwork).

**Expected:** definition

## F088 Rank held by dangling vertices is not passed on {#f088}

Tool: [GAP Benchmark Suite](tools/gapbs.html) 941462c7c42e. Kind: convention. Status: observed.

**Observed:** scores sum to less than 1 on graphs with sinks (0.85, 0.34 and 0.18 on three benchmark graphs)

**Expected:** scores summing to 1

**Notes:** Reproduced bit for bit on one thread by a convention that drops the dangling mass.

References: [beamer2015gap](references.html#beamer2015gap)

## F089 The BC verifier uses a float-epsilon tolerance against its own float accumulation {#f089}

Tool: [GAP Benchmark Suite](tools/gapbs.html) 941462c7c42e. Kind: convention. Status: observed.

**Observed:** exact scores rounded to float fail verification on two Kronecker graphs

References: [beamer2015gap](references.html#beamer2015gap)

## F090 Betweenness normalization can differ by a factor 2 from the Freeman convention {#f090}

Tool: [graph-tool](tools/graphtool.html) 3.9. Kind: convention. Status: reported.

**Entry:** [Betweenness](measures/centrality/betweenness.html#betweenness) <a class="st st-t st-docs" href="method.html#state-reported-in-docs"><span class="g" aria-hidden="true">·</span>reported in docs</a> Not run: listed in the tool's public API listing; no comparison set up for this measure yet. [Full reason](measures/centrality/betweenness.html#why-betweenness-graphtool).

**Expected:** Freeman / BGL

**Notes:** Reported on the tool's public forum; not re-measured here.

References: [brandes2001faster](references.html#brandes2001faster)
{% endraw %}
