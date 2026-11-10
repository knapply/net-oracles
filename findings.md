---
title: Findings
layout: default
nav_order: 5
---

{% raw %}
# Findings

Bugs, disagreements and limitations observed in other tools. `kind` is *defect* (wrong under the published definition), *convention* (differs by a convention) or *limitation* (refuses or cannot represent the input). `status` is *reproduced* (minimal reproduction recorded), *observed* (seen on a shared corpus of test graphs) or *reported* (public discussion, not re-measured). Versions are those tested; a finding may not hold in later versions.

| Id | Tool | Version | Measure | Kind | Status | Title |
|---|---|---|---|---|---|---|
| [F001](#f001) | NetworkX | 3.7 | [Group / betweenness](measures/group-betweenness.html) | defect | reproduced | group\_betweenness\_centrality compares float path lengths exactly |
| [F002](#f002) | NetworkX | 3.7 | [Prominent group](measures/nxo_prominent.html) | defect | reproduced | prominent\_group misses the best group on disconnected graphs |
| [F003](#f003) | NetworkX | 3.7 | [Graph edit distance](measures/ged.html) | defect | reproduced | graph\_edit\_distance substitutes a self-loop for an ordinary edge at no cost |
| [F004](#f004) | NetworkX | 3.7 | [Bellman ford](measures/ord_bellman_ford.html) | defect | observed | goldberg\_radzik raises NetworkXUnbounded for any negative self-loop |
| [F005](#f005) | NetworkX | 3.7 | [Pagerank](measures/pagerank.html) | convention | observed | PageRank stops on an L1 change below n \* tol |
| [F006](#f006) | rustworkx | 0.18.1 | [Pagerank](measures/pagerank.html) | convention | observed | PageRank stops on an L1 change below n \* tol |
| [F007](#f007) | NetworkX | 3.7 | [Pagerank](measures/pagerank.html) | convention | observed | Undirected self-loop is one arc |
| [F008](#f008) | rustworkx | 0.18.1 | [Pagerank](measures/pagerank.html) | convention | observed | Undirected self-loop is one arc |
| [F009](#f009) | JGraphT | 1.5.2 | [Pagerank](measures/pagerank.html) | convention | observed | Undirected self-loop is one arc |
| [F010](#f010) | igraph (R) | 2.3.4 | [Walktrap](measures/walktrap.html) | defect | observed | Walktrap skips minimal merge pairs on mid-size random networks |
| [F011](#f011) | igraph (R) | 2.3.4 | [Leading eigen](measures/leading_eigen.html) | convention | observed | Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance |
| [F012](#f012) | keyplayer | 1.0.4 | [Kpp\_single / distance\_reach](measures/kpp_single-distance_reach.html) | defect | observed | Weighted distances (binary = FALSE) are not shortest-path lengths |
| [F013](#f013) | centiserve | 1.0.0 | [Communicability betweenness](measures/cx_communicability_betweenness.html) | defect | reproduced | communibet() cannot find an installed expm |
| [F014](#f014) | Gephi toolkit | 0.11.3 | [Eigenvector](measures/eigenvector.html) | defect | reproduced | Eigenvector centrality is not converged |
| [F015](#f015) | Gephi toolkit | 0.11.3 | [Louvain quality](measures/louvain_quality.html) | defect | reproduced | Louvain with setRandom(false) is not reproducible |
| [F016](#f016) | Gephi toolkit | 0.11.3 | [Louvain quality](measures/louvain_quality.html) | defect | reproduced | Louvain sometimes does not return |
| [F017](#f017) | Gephi toolkit | 0.11.3 | [Pagerank](measures/pagerank.html) | defect | reproduced | PageRank loses probability mass at self-loops |
| [F018](#f018) | Gephi toolkit | 0.11.3 | [Closeness](measures/closeness.html) | convention | observed | Closeness is reached/sum of distances; 0 for a node reaching nobody |
| [F019](#f019) | Gephi toolkit | 0.11.3 | [Hits](measures/hits.html) | convention | observed | HITS uses unit Euclidean scaling and ignores self-loops |
| [F020](#f020) | Gephi toolkit | 0.11.3 | [Degree](measures/degree.html) | convention | observed | Degree counts a self-loop twice |
| [F021](#f021) | Gephi toolkit | 0.11.3 | [Average clustering](measures/average_clustering.html) | convention | observed | Average clustering leaves out nodes of degree below 2 |
| [F022](#f022) | Gephi toolkit | 0.11.3 | [Louvain quality](measures/louvain_quality.html) | convention | observed | Louvain resolution acts as the reciprocal of gamma |
| [F023](#f023) | NetworkX | 3.7 | [Index](measures/dm_index.html) | defect | observed | hyper\_wiener\_index is twice the published value |
| [F024](#f024) | NetworkX | 3.7 | [Betweenness subset](measures/cx_betweenness_subset.html) | defect | observed | edge\_betweenness\_centrality\_subset deviates from its documented formula |
| [F025](#f025) | NetworkX | 3.7 | [Effective size](measures/effective_size.html) | defect | observed | effective\_size is wrong for weighted or directed graphs on its vectorized path |
| [F026](#f026) | NetworkX | 3.7 |  | defect | observed | Network simplex can misreport feasibility with float weights |
| [F027](#f027) | NetworkX | 3.7 |  | defect | observed | maximum\_spanning\_arborescence occasionally misses the maximum |
| [F028](#f028) | NetworkX | 3.7 | [K edge components](measures/k_edge_components.html) | limitation | observed | k\_edge\_components hits the recursion limit near n = 1000 |
| [F029](#f029) | NetworkX | 3.7 | [Label propagation](measures/label_propagation.html) | convention | observed | Ties are broken by Python set or insertion order |
| [F030](#f030) | NetworkX | 3.7 | [Group / betweenness](measures/group-betweenness.html) | defect | observed | group\_betweenness\_centrality can vary with PYTHONHASHSEED |
| [F031](#f031) | NetworkX | 3.7 | [Node connectivity](measures/ap_node_connectivity.html) | defect | reproduced | approximation.node\_connectivity starts from a bound that can exceed the connectivity |
| [F032](#f032) | NetworkX | 3.7 | [CD index](measures/nxs_cd_index.html) | convention | observed | cd\_index pools every citer of the references, whatever its time |
| [F033](#f033) | NetworkX | 3.7 | [Betweenness](measures/betweenness.html) | convention | observed | Weighted betweenness counts one shortest path per neighbour pair with parallel edges |
| [F034](#f034) | NetworkX | 3.7 | [Implicit family](measures/implicit_family.html) | convention | observed | hypercube\_graph nodes are bit tuples; dimension 0 is the null graph |
| [F035](#f035) | NetworkX | 3.7 | [Modularity](measures/modularity.html) | convention | observed | Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input |
| [F036](#f036) | igraph (R) | 2.3.4 | [Compare partitions](measures/compare_partitions.html) | convention | observed | Adjusted Rand index is NaN on all-singleton partitions |
| [F037](#f037) | cdlib | 0.4.1 | [Compare partitions](measures/compare_partitions.html) | convention | observed | Adjusted Rand index is 1 on degenerate partitions |
| [F038](#f038) | igraph (R) | 2.3.4 | [Spinglass](measures/spinglass.html) | convention | observed | Spinglass reads the network as simple |
| [F039](#f039) | igraph (R) | 2.3.4 | [Triad census](measures/triad_census.html) | defect | observed | Triad census on multigraphs differs from the definition |
| [F040](#f040) | igraph (R) | 2.3.4 | [Hits](measures/hits.html) | convention | observed | HITS returns 1 for an edgeless network |
| [F041](#f041) | sna | 2.8 | [Information centrality](measures/information_centrality.html) | defect | observed | Information centrality fails on singular inputs |
| [F042](#f042) | sna | 2.8 | [Degree](measures/degree.html) | convention | observed | Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default |
| [F043](#f043) | sna | 2.8 | [Closeness](measures/closeness.html) | convention | observed | Closeness and centralization normalizations differ from other tools |
| [F044](#f044) | sna | 2.8 | [Reciprocity](measures/reciprocity.html) | convention | observed | Reciprocity correlation is 0 on a single arc |
| [F045](#f045) | JGraphT | 1.5.2 | [Betweenness](measures/betweenness.html) | convention | observed | Normalized betweenness divides by (n-1)(n-2) in undirected graphs |
| [F046](#f046) | Boost Graph Library | 1.90 | [Betweenness](measures/betweenness.html) | convention | observed | relative\_betweenness\_centrality is twice the standard value on directed graphs |
| [F047](#f047) | JGraphT | 1.5.2 | [Closeness](measures/closeness.html) | convention | observed | Closeness is 0 for a node that cannot reach every other node |
| [F048](#f048) | Boost Graph Library | 1.90 | [Closeness](measures/closeness.html) | convention | observed | Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair |
| [F049](#f049) | JGraphT | 1.5.2 | [Eccentricity](measures/eccentricity.html) | convention | observed | Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable |
| [F050](#f050) | Boost Graph Library | 1.90 | [Eccentricity](measures/eccentricity.html) | convention | observed | Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable |
| [F051](#f051) | JGraphT | 1.5.2 | [Clustering](measures/clustering.html) | convention | observed | Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs |
| [F052](#f052) | Boost Graph Library | 1.90 | [Clustering](measures/clustering.html) | convention | observed | Clustering counts loops and parallel edges as extra neighbours |
| [F053](#f053) | JGraphT | 1.5.2 | [Transitivity](measures/transitivity.html) | limitation | observed | Transitivity refuses directed input |
| [F054](#f054) | JGraphT | 1.5.2 | [Coreness](measures/coreness.html) | limitation | observed | Coreness and clique finders refuse non-simple input |
| [F055](#f055) | BCT (Octave) | 2019-03-03 | [Betweenness](measures/betweenness.html) | convention | observed | Betweenness counts ordered pairs on undirected networks |
| [F056](#f056) | BCT (Octave) | 2019-03-03 | [Clustering](measures/clustering.html) | convention | observed | clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients |
| [F057](#f057) | BCT (Octave) | 2019-03-03 | [Eccentricity](measures/eccentricity.html) | convention | observed | charpath takes the longest finite distance; NaN for a node reaching nobody |
| [F058](#f058) | BCT (Octave) | 2019-03-03 | [Assortativity degree](measures/assortativity_degree.html) | convention | observed | Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target |
| [F059](#f059) | BCT (Octave) | 2019-03-03 | [Degree](measures/degree.html) | convention | observed | Matrix-input calls carry no loops or parallel edges |
| [F060](#f060) | NetworKit | 11.2.2 | [Betweenness](measures/betweenness.html) | convention | observed | Undirected betweenness scores both orderings of a pair |
| [F061](#f061) | NetworKit | 11.2.2 | [Closeness](measures/closeness.html) | convention | observed | Closeness returns (n-1)/sum of distances whatever normalized says |
| [F062](#f062) | NetworKit | 11.2.2 | [Edge betweenness](measures/edge_betweenness.html) | convention | observed | edgeScores() follow NetworKit's own edge numbering |
| [F063](#f063) | NetworKit | 11.2.2 | [Katz](measures/katz.html) | defect | observed | Katz and degree assortativity differ by 2% to 40% |
| [F064](#f064) | NetworKit | 11.2.2 | [Eigenvector](measures/eigenvector.html) | defect | observed | Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs |
| [F065](#f065) | NetworKit | 11.2.2 | [Degree](measures/degree.html) | convention | observed | Loops, parallel edges and directed input are counted differently |
| [F066](#f066) | NetworKit | 11.2.2 | [Max cliques](measures/max_cliques.html) | convention | observed | MaximalCliques omits a node without edges |
| [F067](#f067) | NetworKit | 11.2.2 | [Diameter](measures/diameter.html) | defect | observed | Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10% |
| [F068](#f068) | NetworKit | 11.2.2 | [Pagerank](measures/pagerank.html) | convention | observed | Rank at isolated nodes is spread differently |
| [F069](#f069) | NetworKit | 11.2.2 | [Strength](measures/strength.html) | convention | observed | weightedDegree counts out-edges only; a single node gets 0 |
| [F070](#f070) | ergm (statnet) | 4.12.0 | [Density](measures/density.html) | convention | observed | A network object holds each tie once and no loops |
| [F071](#f071) | nauty | 2.8.8 | [Vf2pp](measures/vf2pp.html) | limitation | observed | Parallel edges are not representable |
| [F072](#f072) | graspologic | 3.4.4 | [Gm laplacian](measures/gm_laplacian.html) | convention | observed | The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs |
| [F073](#f073) | egor | 1.25.10 | [Ei index](measures/ei_index.html) | convention | observed | comp\_ei counts each neighbour once |
| [F074](#f074) | igraph (Python) | 1.0.0 | [Assortativity nominal](measures/assortativity_nominal.html) | limitation | observed | assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode |
| [F075](#f075) | igraph (Python) | 1.0.0 | [Katz](measures/katz.html) | limitation | observed | Alpha and power centrality exist only in the R binding |
| [F076](#f076) | influenceR | 0.1.5 | [Betweenness](measures/betweenness.html) | convention | observed | influenceR betweenness counts both orderings of an undirected pair and reads directed graphs as undirected |
| [F077](#f077) | centiserve | 1.0.0 | [Current flow closeness](measures/cx_current_flow_closeness.html) | convention | observed | Flow closeness is larger by a factor near n - 1; closeness vitality is twice the standard value on undirected networks |
| [F078](#f078) | tnet | 3.0.16 | [Distances](measures/distances.html) | defect | observed | Weighted distance and closeness with the alpha exponent differ from the definition |
| [F079](#f079) | netrankr | 2.0.0 | [Betweenness](measures/betweenness.html) | convention | observed | depend\_sp and depend\_curflow count both orderings of an unordered pair |
| [F080](#f080) | netrankr | 2.0.0 | [Information centrality](measures/information_centrality.html) | convention | observed | dist\_resist with invsum is the standard value divided by n |
| [F081](#f081) | netrankr | 2.0.0 | [Closeness](measures/closeness.html) | convention | observed | Empty distance sum inverts to 0 |
| [F082](#f082) | manynet | 2.4.0 | [Effective size](measures/effective_size.html) | defect | observed | Effective size and efficiency differ on directed networks and multigraphs with loops |
| [F083](#f083) | manynet | 2.4.0 | [Hierarchy](measures/hierarchy.html) | defect | observed | hierarchy differs from the definition on all 25 fixtures |
| [F084](#f084) | blockmodeling | 1.1.8 | [Structural equivalence](measures/structural_equivalence.html) | convention | observed | Profiles keep the entries for the two nodes themselves on asymmetric matrices |
| [F085](#f085) | RSiena | 1.6.6 | [Saom sim mean](measures/saom_sim_mean.html) | defect | observed | From a complete first wave the mean tie count stays at 5.0 |
| [F086](#f086) | GraphBLAS algorithms | 2023.10.0 | [Katz](measures/katz.html) | defect | observed | Katz loses beta at nodes without in-links |
| [F087](#f087) | scikit-network | 0.33.0 | [Pagerank](measures/pagerank.html) | defect | observed | PageRank restart vector departs from the definition |
| [F088](#f088) | GAP Benchmark Suite | 941462c7c42e | [Pagerank](measures/pagerank.html) | convention | observed | Rank held by dangling vertices is not passed on |
| [F089](#f089) | GAP Benchmark Suite | 941462c7c42e | [Betweenness](measures/betweenness.html) | convention | observed | The BC verifier uses a float-epsilon tolerance against its own float accumulation |
| [F090](#f090) | graph-tool | 3.9 | [Betweenness](measures/betweenness.html) | convention | reported | Betweenness normalization can differ by a factor 2 from the Freeman convention |

## F001 group\_betweenness\_centrality compares float path lengths exactly {#f001}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

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

**Observed:** NetworkXUnbounded, even when the loop is unreachable from the source

**Expected:** a negative self-loop that is unreachable from the source should not make the problem unbounded

**Notes:** bellman\_ford\_predecessor\_and\_distance was also checked and behaves the same way.

## F005 PageRank stops on an L1 change below n \* tol {#f005}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Observed:** absolute error 3.4e-11 (relative 4.2e-9) against the exact solution on a 2000-node directed graph, damping 0.85

**Expected:** a tighter error is available from the same iteration; rustworkx shows the same stopping rule

**Notes:** The stopping rule scales the tolerance with the number of nodes.

## F006 PageRank stops on an L1 change below n \* tol {#f006}

Tool: [rustworkx](tools/rustworkx.html) 0.18.1. Kind: convention. Status: observed.

**Observed:** same stopping rule as NetworkX

**Expected:** exact solution

**Notes:** Compared with an exact linear solve on a 2000-node directed graph.

## F007 Undirected self-loop is one arc {#f007}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

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

**Observed:** same as NetworkX: the loop adds 1 to the node's out-degree

**Expected:** two edge ends on the diagonal (igraph)

**Notes:** See the NetworkX entry.

## F009 Undirected self-loop is one arc {#f009}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Observed:** same as NetworkX

**Expected:** two edge ends on the diagonal (igraph)

**Notes:** See the NetworkX entry.

## F010 Walktrap skips minimal merge pairs on mid-size random networks {#f010}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: defect. Status: observed.

**Observed:** igraph merges a pair above the minimum (by more than a relative 1e-9) in 179 of 1999 merges (2000-node G(n,m)), 23 of 2498, 557 of 999 (dense, 1000 nodes) and 771 of 3999 (4000-node block model); the skipped pair joins a node to the group created by the preceding merge

**Expected:** merge the pair with the minimum delta sigma = \|C1\|\|C2\|/(\|C1\|+\|C2\|) r^2 / n (Pons and Latapy 2006)

**Notes:** Found by replaying igraph's merge sequence and evaluating the definition. Greedy-minimum sequence best level modularity 0.21065583 against igraph 0.21138759 on the 2000-node case; the direction of the difference varies. Mechanism unknown (the tool was used as a black box).

References: [pons2006computing](references.html#pons2006computing)

## F011 Leading-eigenvector modularity differs at 1e-6 through the ARPACK tolerance {#f011}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Observed:** 0.5404499 on Les Miserables (weighted)

**Expected:** 0.5404514 from the exact eigenvector

**Notes:** Attributed to ARPACK's tolerance on a near-zero eigenvector entry.

## F012 Weighted distances (binary = FALSE) are not shortest-path lengths {#f012}

Tool: [keyplayer](tools/keyplayer.html) 1.0.4. Kind: defect. Status: observed.

**Observed:** reach 0.4485 on an 8-node probe

**Expected:** 0.4655 with exact shortest paths and edge values as lengths

**Notes:** The tool was used as a black box; the cause is unknown.

## F013 communibet() cannot find an installed expm {#f013}

Tool: [centiserve](tools/centiserve.html) 1.0.0. Kind: defect. Status: reproduced.

**Observed:** error from requireNamespace

**Expected:** a value; a patched copy gives matching values on connected networks and NaN on disconnected ones

**Notes:** The function passes library() arguments to requireNamespace, which rejects them.

## F014 Eigenvector centrality is not converged {#f014}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: defect. Status: reproduced.

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

**Observed:** undirected edges 0-0, 0-1, 1-2, damping 0.85: scores 0.1375, 0.2058, 0.1375 (sum 0.4807); directed arcs 0&gt;0, 0&gt;1, 1&gt;0: 0.5, 0.2875 (sum 0.7875)

**Expected:** scores that sum to 1 (they do without the loop)

**Reproduction:**

```
Run PageRank with epsilon 1e-14 on the graphs above.
```

**Notes:** Two larger fixtures with loops sum to 0.545 and 0.496.

## F018 Closeness is reached/sum of distances; 0 for a node reaching nobody {#f018}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Observed:** (nodes reached)/(sum of distances); setNormalized has no effect on closeness

**Expected:** (n-1)/(sum of distances) with undefined for nodes that reach nobody

**Notes:** Harmonic closeness is sum(1/d)/(nodes reached).

References: [freeman1978centrality](references.html#freeman1978centrality)

## F019 HITS uses unit Euclidean scaling and ignores self-loops {#f019}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Observed:** unit-length vectors; 0 on an edgeless network

**Expected:** tool-specific scaling

References: [kleinberg1999authoritative](references.html#kleinberg1999authoritative)

## F020 Degree counts a self-loop twice {#f020}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Observed:** loop adds 2

**Notes:** Betweenness, eccentricity, radius, diameter, density and components agree with the definition.

## F021 Average clustering leaves out nodes of degree below 2 {#f021}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Observed:** nodes of degree 0 or 1 are excluded from the average (their local value is 0)

**Expected:** average over all nodes with local value 0 for those nodes

## F022 Louvain resolution acts as the reciprocal of gamma {#f022}

Tool: [Gephi toolkit](tools/gephi.html) 0.11.3. Kind: convention. Status: observed.

**Observed:** getModularity() always returns the gamma = 1 modularity

**Expected:** modularity at the requested resolution

**Notes:** No resolution value other than 1 can be compared.

References: [blondel2008fast](references.html#blondel2008fast)

## F023 hyper\_wiener\_index is twice the published value {#f023}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Observed:** twice the value of the defining formula (Randic 1993)

**Expected:** published value

**Notes:** Also affects schultz\_index and gutman\_index conventions noted in their documentation.

References: [randic1993novel](references.html#randic1993novel)

## F024 edge\_betweenness\_centrality\_subset deviates from its documented formula {#f024}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Observed:** values differ from the documented subset definition

**Expected:** documented formula

**Notes:** Observed on the shared fixture corpus.

## F025 effective\_size is wrong for weighted or directed graphs on its vectorized path {#f025}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

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

**Observed:** RecursionError

**Expected:** a result

## F029 Ties are broken by Python set or insertion order {#f029}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Observed:** results depend on iteration order

**Expected:** tie rule not specified by the published algorithm

**Notes:** Same for greedy modularity, lowest common ancestors, dispersion, shortest-path choice and minimum cuts.

## F030 group\_betweenness\_centrality can vary with PYTHONHASHSEED {#f030}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: observed.

**Observed:** results vary with the hash seed on some inputs

**Expected:** one value

**Notes:** Reported separately from the weighted float-comparison finding above.

## F031 approximation.node\_connectivity starts from a bound that can exceed the connectivity {#f031}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: defect. Status: reproduced.

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

**Observed:** on nodes 0, 1 with the arc 0 -&gt; 1 NetworkX gives 1

**Expected:** undefined in the published definition (Funk and Owen-Smith 2017), whose window excludes earlier citers

**Notes:** Publication times were a fixed function of the node id.

References: [funk2017dynamic](references.html#funk2017dynamic)

## F033 Weighted betweenness counts one shortest path per neighbour pair with parallel edges {#f033}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Observed:** node 1 gets 1/2 on arcs 0-&gt;1 twice, 1-&gt;2, 0-&gt;3, 3-&gt;2

**Expected:** 2/3 when each parallel edge is a distinct path (igraph, NetworKit)

References: [brandes2001faster](references.html#brandes2001faster)

## F034 hypercube\_graph nodes are bit tuples; dimension 0 is the null graph {#f034}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Observed:** tuple labels

**Expected:** integer labels from reading the tuple as a number

## F035 Returns 0 for modularity, Louvain, density and nominal assortativity on edgeless input {#f035}

Tool: [NetworkX](tools/networkx.html) 3.7. Kind: convention. Status: observed.

**Observed:** 0

**Expected:** undefined (0/0)

## F036 Adjusted Rand index is NaN on all-singleton partitions {#f036}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Observed:** NaN

**Expected:** 0/0 in the definition of Hubert and Arabie (1985); scikit-learn returns 1

References: [hubert1985comparing](references.html#hubert1985comparing)

## F037 Adjusted Rand index is 1 on degenerate partitions {#f037}

Tool: [cdlib](tools/cdlib.html) 0.4.1. Kind: convention. Status: observed.

**Observed:** 1

**Expected:** 0/0 in the definition

References: [hubert1985comparing](references.html#hubert1985comparing)

## F038 Spinglass reads the network as simple {#f038}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Observed:** two parallel edges on two nodes give -0.5

**Expected:** -1 for the multigraph Hamiltonian

## F039 Triad census on multigraphs differs from the definition {#f039}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: defect. Status: observed.

**Observed:** values differ when parallel edges exist

**Expected:** triad census of the underlying simple digraph or a documented rule

## F040 HITS returns 1 for an edgeless network {#f040}

Tool: [igraph (R)](tools/igraph.html) 2.3.4. Kind: convention. Status: observed.

**Observed:** 1

**Expected:** undefined

References: [kleinberg1999authoritative](references.html#kleinberg1999authoritative)

## F041 Information centrality fails on singular inputs {#f041}

Tool: [sna](tools/sna.html) 2.8. Kind: defect. Status: observed.

**Observed:** error or invalid values on disconnected or valued directed networks

**Expected:** a documented rule for singular matrices

## F042 Degree reads an adjacency matrix: parallel edges collapse and the diagonal is ignored by default {#f042}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Observed:** parallel edges count once; loops ignored (diag = FALSE)

**Expected:** edge-list degree counts every edge end

**Notes:** Applies to in-degree, out-degree and density.

## F043 Closeness and centralization normalizations differ from other tools {#f043}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Observed:** tool-specific normalizing constants

**Notes:** Also differs from UCINET's documented normalizations.

References: [freeman1978centrality](references.html#freeman1978centrality)

## F044 Reciprocity correlation is 0 on a single arc {#f044}

Tool: [sna](tools/sna.html) 2.8. Kind: convention. Status: observed.

**Observed:** 0

**Expected:** -1 (the correlation)

## F045 Normalized betweenness divides by (n-1)(n-2) in undirected graphs {#f045}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Observed:** exactly half the standard value on 16 undirected fixtures with n &gt;= 3 (raw betweenness agrees)

**Expected:** raw / ((n-1)(n-2)/2)

References: [brandes2001faster](references.html#brandes2001faster)

## F046 relative\_betweenness\_centrality is twice the standard value on directed graphs {#f046}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Observed:** ratio 2 on 6 directed fixtures with n &gt;= 3 (undirected agrees); 0/0 = NaN below 3 nodes

**Expected:** standard value; 0 below 3 nodes in NetworkX

References: [brandes2001faster](references.html#brandes2001faster)

## F047 Closeness is 0 for a node that cannot reach every other node {#f047}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Observed:** 0 for any node not reaching all; Infinity for the single node of a one-node network

**Expected:** reachable-only sum

References: [freeman1978centrality](references.html#freeman1978centrality)

## F048 Closeness is 1 / sum of distances, with DBL\_MAX for an unreachable pair {#f048}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Observed:** about 5.6e-309 for unreachable cases; Infinity on one node; equals the unnormalized closeness on connected networks

**Expected:** normalized (n-1)/sum

References: [freeman1978centrality](references.html#freeman1978centrality)

## F049 Eccentricity, radius and diameter follow edge direction and return Infinity when a node is unreachable {#f049}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Observed:** Infinity

**Expected:** longest finite shortest path

## F050 Eccentricity, radius and diameter return DBL\_MAX when a node is unreachable {#f050}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Observed:** DBL\_MAX

**Expected:** longest finite shortest path

## F051 Local clustering counts ordered neighbour pairs on directed input; counts loops and parallel edges in pseudographs {#f051}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: convention. Status: observed.

**Observed:** half the undirected-neighbourhood value on directed input

**Notes:** Agrees on fully reciprocated and simple undirected networks.

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F052 Clustering counts loops and parallel edges as extra neighbours {#f052}

Tool: [Boost Graph Library](tools/boost.html) 1.90. Kind: convention. Status: observed.

**Observed:** extra neighbours

**Expected:** simple-graph value

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F053 Transitivity refuses directed input {#f053}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: limitation. Status: observed.

**Observed:** "Graph must be undirected"; NaN when there is no connected triple

## F054 Coreness and clique finders refuse non-simple input {#f054}

Tool: [JGraphT](tools/jgrapht.html) 1.5.2. Kind: limitation. Status: observed.

**Observed:** "Graph must be simple"; coreness refuses directed input; the clique finder accepts directed input but does not return the maximal cliques of the underlying graph

## F055 Betweenness counts ordered pairs on undirected networks {#f055}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Observed:** exactly twice the standard value

**Expected:** each unordered pair once

References: [brandes2001faster](references.html#brandes2001faster)

## F056 clustering\_coef\_bd and transitivity\_bd are Fagiolo's directed coefficients {#f056}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Observed:** values differ from the undirected-neighbourhood value on 5 directed fixtures

**Notes:** Undirected simple networks agree.

References: [fagiolo2007clustering](references.html#fagiolo2007clustering)

## F057 charpath takes the longest finite distance; NaN for a node reaching nobody {#f057}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Observed:** NaN diameter for an edgeless network; radius ignores nodes reaching nobody

## F058 Degree assortativity is NaN for regular networks; the directed variant differs from the Pearson correlation of out-degree at the source and in-degree at the target {#f058}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Observed:** differences of 0.1% to 14% on 4 directed fixtures

**Expected:** Pearson correlation

**Notes:** Cause not identified.

References: [newman2002assortative](references.html#newman2002assortative)

## F059 Matrix-input calls carry no loops or parallel edges {#f059}

Tool: [BCT (Octave)](tools/bct.html) 2019-03-03. Kind: convention. Status: observed.

**Observed:** degree, coreness and local efficiency differ on multigraph inputs

## F060 Undirected betweenness scores both orderings of a pair {#f060}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** twice the standard value

**Expected:** each unordered pair once

References: [brandes2001faster](references.html#brandes2001faster)

## F061 Closeness returns (n-1)/sum of distances whatever normalized says {#f061}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** 1.0 on every node of K6 with normalized = False; ratio exactly n-1 on karate

**Expected:** unnormalized 1/sum of distances

References: [freeman1978centrality](references.html#freeman1978centrality)

## F062 edgeScores() follow NetworKit's own edge numbering {#f062}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** not the input edge order

**Notes:** Scores agree to 1e-14 after mapping by endpoints.

## F063 Katz and degree assortativity differ by 2% to 40% {#f063}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Observed:** differences on 7 to 11 fixtures each

**Expected:** definition

**Notes:** Cause not identified.

References: [katz1953new](references.html#katz1953new)

## F064 Eigenvector power iteration stops near 1e-7 whatever tol is requested and oscillates on bipartite graphs {#f064}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Observed:** differences of 6% to 90% on 7 to 11 fixtures

**Expected:** converged eigenvector

References: [bonacich1987power](references.html#bonacich1987power)

## F065 Loops, parallel edges and directed input are counted differently {#f065}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** k-core on a directed graph ignores direction; degenerate inputs (no edges, two nodes) return sentinel values

## F066 MaximalCliques omits a node without edges {#f066}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** isolates missing

**Expected:** a clique of one node

## F067 Exact diameter on a weighted graph returns whole numbers; weighted Laplacian differs by 5% to 10% {#f067}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: defect. Status: observed.

**Observed:** 12.0 against 12.5

**Expected:** 12.5

**Notes:** Cause not identified.

## F068 Rank at isolated nodes is spread differently {#f068}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Observed:** a 5% difference on a sparse random graph

## F069 weightedDegree counts out-edges only; a single node gets 0 {#f069}

Tool: [NetworKit](tools/networkit.html) 11.2.2. Kind: convention. Status: observed.

**Expected:** in plus out for directed input; undefined for one node

## F070 A network object holds each tie once and no loops {#f070}

Tool: [ergm (statnet)](tools/ergm.html) 4.12.0. Kind: convention. Status: observed.

**Observed:** edge count lower than a multigraph's

**Expected:** edge count including parallel edges

## F071 Parallel edges are not representable {#f071}

Tool: [nauty](tools/nauty.html) 2.8.8. Kind: limitation. Status: observed.

**Observed:** undefined on networks with parallel edges

## F072 The I-DAD normalized Laplacian normalizes by in-degrees on directed graphs {#f072}

Tool: [graspologic](tools/graspologic.html) 3.4.4. Kind: convention. Status: observed.

**Observed:** a node without in-links gets 0 on the diagonal

**Expected:** out-degree normalization (NetworkX)

**Notes:** Undirected agree.

## F073 comp\_ei counts each neighbour once {#f073}

Tool: [egor](tools/egor.html) 1.25.10. Kind: convention. Status: observed.

**Observed:** one count per neighbour whatever the number or direction of ties

**Expected:** count of ties

**Notes:** Directed and multi-edge fixtures differ.

## F074 assortativity\_nominal(normalized=False) raises SystemError; eigenvector\_centrality(directed=False) on a directed graph raises Invalid mode {#f074}

Tool: [igraph (Python)](tools/pyigraph.html) 1.0.0. Kind: limitation. Status: observed.

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

**Observed:** ratio 31 on a two-mode fixture; ratio 2.0 on a dense random graph

**Notes:** The raw Laplacian also differs on a fixture with loops.

## F078 Weighted distance and closeness with the alpha exponent differ from the definition {#f078}

Tool: [tnet](tools/tnet.html) 3.0.16. Kind: defect. Status: observed.

**Observed:** differences on 7 weighted fixtures each

**Notes:** Cause not identified.

## F079 depend\_sp and depend\_curflow count both orderings of an unordered pair {#f079}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Observed:** twice the standard value; parallel edges and loops dropped

References: [brandes2001faster](references.html#brandes2001faster)

## F080 dist\_resist with invsum is the standard value divided by n {#f080}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Observed:** ratio n on all connected fixtures

## F081 Empty distance sum inverts to 0 {#f081}

Tool: [netrankr](tools/netrankr.html) 2.0.0. Kind: convention. Status: observed.

**Observed:** 0 for nodes without reachable nodes

**Expected:** NaN (igraph)

References: [freeman1978centrality](references.html#freeman1978centrality)

## F082 Effective size and efficiency differ on directed networks and multigraphs with loops {#f082}

Tool: [manynet](tools/manynet.html) 2.4.0. Kind: defect. Status: observed.

**Observed:** half the standard value on a directed cycle

**Notes:** Simple undirected networks agree; cause not traced.

References: [burt1992structural](references.html#burt1992structural)

## F083 hierarchy differs from the definition on all 25 fixtures {#f083}

Tool: [manynet](tools/manynet.html) 2.4.0. Kind: defect. Status: observed.

**Observed:** 0.0285 against 0.0875 on karate; 0 where no value exists

## F084 Profiles keep the entries for the two nodes themselves on asymmetric matrices {#f084}

Tool: [blockmodeling](tools/blockmodeling.html) 1.1.8. Kind: convention. Status: observed.

**Observed:** 7 directed fixtures differ; 20 others agree

## F085 From a complete first wave the mean tie count stays at 5.0 {#f085}

Tool: [RSiena](tools/rsiena.html) 1.6.6. Kind: defect. Status: observed.

**Observed:** 5.0 on the 5-node complete digraph

**Expected:** relaxes to 9.3 (one tie removed agrees)

**Notes:** Cause not identified.

## F086 Katz loses beta at nodes without in-links {#f086}

Tool: [GraphBLAS algorithms](tools/graphblas.html) 2023.10.0. Kind: defect. Status: observed.

**Expected:** definition

**Notes:** Beta lost at nodes without in-links; also 0 for PageRank, HITS, Katz on edgeless input.

References: [katz1953new](references.html#katz1953new)

## F087 PageRank restart vector departs from the definition {#f087}

Tool: [scikit-network](tools/sknetwork.html) 0.33.0. Kind: defect. Status: observed.

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

**Expected:** Freeman / BGL

**Notes:** Reported on the tool's public forum; not re-measured here.

References: [brandes2001faster](references.html#brandes2001faster)
{% endraw %}
