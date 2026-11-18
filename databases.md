---
title: Graph databases
layout: default
nav_order: 10
---

{% raw %}

# Graph databases

A survey of graph and RDF database systems as possible oracles (independent sources of correct answers to compare against) and benchmark targets for graph analytics and graph queries. Each entry gives what the system is, its data model, query languages, licence, deployment, built-in algorithms, standards, published benchmark results and a rating of its value as an oracle or benchmark target. Facts come from the vendor's documentation, papers and public records, each linked where it is used; nothing here was measured. Surveyed in November 2026; products change quickly, so check the linked source before relying on an entry.

Licence column: "OSI" means the licence of the freely available edition is approved by the Open Source Initiative ([licence list](https://opensource.org/licenses)). Source-available licences such as the Business Source License (BSL), the Server Side Public License (SSPL) and the Commons Clause are not OSI-approved. "Proprietary" means no source is available.

Benchmark terms: LDBC SNB is the Linked Data Benchmark Council's Social Network Benchmark (Interactive and Business Intelligence workloads); Graphalytics is its analytics benchmark with six algorithms (BFS, PageRank, weakly connected components, label propagation, local clustering coefficient, single-source shortest paths; [LDBC](https://ldbcouncil.org/benchmarks/graphalytics/algorithms/)); FinBench is its financial benchmark, which has [no audited results yet](https://ldbcouncil.org/benchmarks/finbench/results/). Only audited results are listed as audited; vendor-run numbers are labelled as such.

Oracle value: **high** means it can run headless and locally (or in a container) and computes well-defined algorithms or query semantics worth comparing against; **medium** means useful for a narrower purpose or with a practical obstacle; **low** means cloud-only, unmaintained, or with little to compare.

## Summary

| System | Kind | Data model | Query languages | Licence (free edition) | OSI | Deployment | Audited LDBC | Oracle value |
|---|---|---|---|---|---|---|---|---|
| [Stardog](#stardog) | knowledge-graph platform | RDF | SPARQL, GraphQL, SQL (BI server) | proprietary | no | server, cluster, cloud | none | low |
| [Ontotext GraphDB](#ontotext-graphdb) | RDF store with reasoning | RDF | SPARQL 1.1 | proprietary (Free Edition is freeware) | no | server, cluster | SNB Interactive SF30 (2023) | medium |
| [OpenLink Virtuoso](#openlink-virtuoso) | hybrid SQL / RDF column store | RDF, relational | SPARQL, SQL | GPL-2.0 (open source edition) | yes | server, cluster | SNB Interactive v0.2.2 (2015) | high |
| [RDFox](#rdfox) | in-memory RDF store and Datalog reasoner | RDF | SPARQL 1.1, Datalog rules | proprietary (time-limited licence key) | no | embedded library, server | none | medium |
| [QLever](#qlever) | SPARQL engine | RDF | SPARQL 1.1 | Apache-2.0 | yes | server, embedded | none | high |
| [AllegroGraph](#allegrograph) | RDF store | RDF (quints) | SPARQL, Prolog | proprietary (clients EPL-1.0) | no | server, cluster | none | low |
| [Blazegraph](#blazegraph) | RDF store | RDF, TinkerPop | SPARQL, Gremlin | GPL-2.0 | yes | server | none | low |
| [TigerGraph](#tigergraph) | MPP property-graph database | property graph | GSQL, openCypher subset | proprietary (free Community Edition) | no | server, cluster, cloud | SNB BI SF100 to SF10000 | medium |
| [NebulaGraph](#nebulagraph) | distributed property-graph database | property graph | nGQL, openCypher subset | Apache-2.0 with Commons Clause (as listed) | no | cluster | none | low |
| [JanusGraph](#janusgraph) | graph layer over wide-column stores | property graph | Gremlin | Apache-2.0 | yes | embedded (JVM), server | none | low |
| [Dgraph](#dgraph) | distributed graph database | RDF-like triples | DQL, GraphQL | Apache-2.0 | yes | cluster | none | low |
| [HugeGraph](#hugegraph) | graph database and computing stack | property graph | Gremlin, openCypher | Apache-2.0 | yes | server, cluster | none | medium |
| [TuGraph](#tugraph) | property-graph database | property graph | openCypher | Apache-2.0 | yes | server | SNB Interactive SF30 to SF300; SNB BI SF30000 | medium |
| [GraphScope](#graphscope) | graph computing stack | property graph | Gremlin, Cypher | Apache-2.0 | yes | single machine, cluster | SNB Interactive SF30 to SF1000 | high |
| [Apache AGE](#apache-age) | PostgreSQL extension | property graph | openCypher inside SQL | Apache-2.0 | yes | PostgreSQL extension | none | medium |
| [DuckPGQ](#duckpgq) | DuckDB extension | property graph views over tables | SQL/PGQ | MIT | yes | embedded | none | high |
| [Spanner Graph](#google-spanner-graph) | graph on a distributed SQL database | property graph over tables | ISO GQL, SQL | proprietary service | no | cloud only | none | low |
| [Amazon Neptune](#amazon-neptune-and-neptune-analytics) | managed graph database | property graph, RDF | Gremlin, openCypher, SPARQL | proprietary service | no | cloud only | none | low |
| [Neptune Analytics](#amazon-neptune-and-neptune-analytics) | in-memory analytics engine | property graph and RDF in one store | openCypher | proprietary service | no | cloud only | none | medium |
| [Azure Cosmos DB for Gremlin](#azure-cosmos-db-for-apache-gremlin) | managed graph API | property graph | Gremlin | proprietary service | no | cloud only | none | low |
| [Aerospike Graph](#aerospike-graph) | graph compute layer over a key-value store | property graph | Gremlin | proprietary (free start offered) | no | server, cloud | none | low |
| [ArangoDB](#arangodb) | multi-model database | document, key-value, graph | AQL | BSL-1.1 (source), Community License (binaries) | no | server, cluster, cloud | none | low |
| [SurrealDB](#surrealdb) | multi-model database | document, graph, relational | SurrealQL | BSL | no | embedded, server, cloud | none | low |
| [PuppyGraph](#puppygraph) | graph query engine over existing tables | property graph views | openCypher, Gremlin | proprietary (free Developer Edition) | no | server, cloud | none | low |
| [Weaviate](#weaviate) | vector database | objects with vectors and cross-references | GraphQL, REST | BSD-3-Clause | yes | server, cloud | none | low |
| [Kùzu and LadybugDB](#kùzu-and-ladybugdb) | embedded graph database | property graph | Cypher | MIT | yes | embedded | none | medium |
| [FalkorDB](#falkordb) | sparse-matrix graph database | property graph | openCypher | SSPL-1.0 | no | server (Redis module) | none | low |
| [Memgraph](#memgraph) | in-memory graph database | property graph | openCypher | BSL-1.1 | no | server | none | medium |
| [TerminusDB](#terminusdb) | versioned document graph store | RDF graph of documents | WOQL, GraphQL | Apache-2.0 | yes | server | none | low |
| [ArcadeDB](#arcadedb) | multi-model database | graph, document, key-value and more | SQL, Cypher, Gremlin and others | Apache-2.0 | yes | embedded, server | none | low |
| [AnzoGraph](#anzograph) | MPP graph OLAP database | RDF, RDF-star | SPARQL, Cypher | proprietary | no | cluster | none | low |
| [Oracle Graph Server (PGX)](#oracle-graph-server-pgx) | in-memory graph analytics server | property graph, RDF | PGQL, SQL/PGQ | proprietary | no | server, in-database | none | low |

## Audited LDBC results

From the LDBC result pages ([SNB Interactive](https://ldbcouncil.org/benchmarks/snb/interactive/), [SNB BI](https://ldbcouncil.org/benchmarks/snb/bi/), [legacy SNB](https://ldbcouncil.org/benchmarks/snb/audited-results-v0.2.2/)), restricted to the systems on this page. Throughput is the audited operations per second; BI scores are power@SF and throughput@SF. Results from different scale factors (SF) or hardware are not comparable.

| Workload | System | Sponsor | Date | SF and score |
|---|---|---|---|---|
| SNB Interactive v1 | GraphScope Flex | Alibaba Cloud | 2025-04-21 | SF30 37,650; SF100 79,244; SF300 80,511 |
| SNB Interactive v1 | GraphScope Flex | Alibaba Cloud | 2024-05-14 | SF100 130,098; SF300 131,264; SF1000 127,785 |
| SNB Interactive v1 | GraphScope Flex | Alibaba DAMO | 2023-07-13 | SF30 33,181; SF100 33,625; SF300 33,261 |
| SNB Interactive v1 | GraphDB | Ontotext | 2023-01-31 | SF30 3, 7 and 12 (three runs) |
| SNB Interactive v1 | TuGraph | Ant Group | 2023-01-28 | SF30 16,133; SF100 16,966; SF300 13,533 |
| SNB Interactive v1 | TuGraph | Ant Group | 2022-08-16 | SF30 12,253; SF100 12,935; SF300 12,721 |
| SNB Interactive v1 | TuGraph | FMA | 2020-07-26 | SF30 5,436; SF100 5,011; SF300 4,856 |
| SNB Interactive v0.2.2 | Virtuoso 7.50 | OpenLink | 2015-04-27 | SF30 1,287; SF100 1,200; SF300 635 |
| SNB BI | TigerGraph | TigerGraph | 2024-10-10 | SF1000 power 34,950, throughput 15,089 |
| SNB BI | TuGraph | TuGraph | 2023-12-03 | SF30000 power 111,775, throughput 56,920 |
| SNB BI | TigerGraph | TigerGraph | 2023-04-06 | SF100 6,254 / 3,723; SF1000 23,952 / 10,605; SF10000 89,445 / 41,026 |
| SNB BI | TigerGraph | TigerGraph | 2022-11-09 | SF1000 power 30,990, throughput 12,994 |

The other recent SNB Interactive results (Galaxybase, Huawei Graph Engine Service, AtlasGraph) are for systems outside this survey. No system on this page has an audited FinBench result.

## RDF and knowledge-graph stores

### Stardog

- **What it is:** an "Enterprise Knowledge Graph platform and graph DBMS with high availability, high performance reasoning, and virtualization" ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGigaSpaces%3BMySQL%3BStardog)).
- **Data model and languages:** RDF; SPARQL, GraphQL, TinkerPop 3, and SQL through a BI/SQL server (same source).
- **Reasoning:** at query time by rewriting, not materialization: Stardog does "not materialize inferences; rather, reasoning is performed at query time". Profiles RDFS, OWL 2 QL, RL and EL, and a default SL profile combining them with SWRL rules; a beta engine (Stride) adds negation and aggregation in rules ([docs](https://docs.stardog.com/inference-engine/)).
- **Virtual graphs:** answers SPARQL over data left in a relational source by translating part of the query to SQL and pushing filters and aggregates down ([blog](https://www.stardog.com/blog/virtual-graphs-in-stardog-5)).
- **Licence:** proprietary. The free licence is "for the sole purpose of evaluating Stardog" ([terms](https://www.stardog.com/legal/stardog-free/)); DB-Engines lists a 60-day trial and a one-year non-commercial academic licence.
- **Deployment:** server and HA cluster; no partitioning ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGigaSpaces%3BMySQL%3BStardog)).
- **Benchmarks:** no audited LDBC result.
- **Oracle value: low.** Evaluation-only licence; reasoning results can be had from open reasoners.

### Ontotext GraphDB

- **What it is:** an RDF store with reasoning, formerly OWLIM ([DB-Engines](https://db-engines.com/en/system/AnzoGraph+DB%3BBlazegraph%3BGraphDB%3BSingleStore)).
- **Languages and standards:** SPARQL 1.1, GraphQL, and stored SPARQL exposed as SQL through Apache Calcite over JDBC/ODBC ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGraphDB%3BMemgraph)).
- **Reasoning:** forward-chaining total materialization at load time with selectable rulesets (`empty`, `rdfs`, `rdfsplus`, `owl-horst`, `owl-max`, `owl2-ql`, `owl2-rl`, custom `.pie` rules). Retraction removes only inferred statements that are no longer supported, using a backward-chaining support check, and `owl:sameAs` is handled by an equivalence-class representative ([docs](https://graphdb.ontotext.com/documentation/11.0/reasoning.html)).
- **Licence:** proprietary; Standard and Enterprise are commercial and the Free Edition is freeware ([Wikipedia](https://en.wikipedia.org/wiki/Graph_Database)).
- **Benchmarks:** audited SNB Interactive v1 at SF30 in January 2023 (table above).
- **Oracle value: medium.** The free edition runs locally and its rulesets give a second opinion on RDFS and OWL 2 RL materialization; not an analytics engine.

### OpenLink Virtuoso

- **What it is:** a hybrid relational and RDF database whose RDF quads live in a compressed column store ([white paper](https://virtuoso.openlinksw.com/whitepapers/Virtuoso_a_Hybrid_RDBMS_Graph_Column_Store.html)).
- **Storage:** two covering indexes (PSOG, POGS) plus distinct projections (OP, SP, GS); column compression by run length, deltas, bitmaps and dictionaries, chosen automatically. DBpedia 3.7 (256.5 million quads) took 302,423 pages in the column store against 1,021,470 as rows, "under 1/3 of the memory footprint" (about 9.7 bytes per quad including overhead, derived from the page counts). Execution is vectored, with batches "from 10000 to 1000000 values"; cluster partitioning is by value on S or O (same source).
- **Languages:** SPARQL and SQL in one engine.
- **Licence:** the open source edition is GPL-2.0 ("the only valid version of the GPL as far as this project is concerned", [VOS licence](https://vos.openlinksw.com/owiki/wiki/VOS/VOSLicense)); the enterprise edition is proprietary ([Wikipedia](https://en.wikipedia.org/wiki/Graph_Database)).
- **Benchmarks:** audited SNB Interactive v0.2.2 in 2015 (table above). One of two finalists for the Wikidata Query Service backend in 2026 ([report](https://wikwiand-revamp.pages.dev/en/Wikipedia:Wikipedia_Signpost/2026-02-17/Technology_report)).
- **Oracle value: high.** Runs locally, mature SPARQL 1.1 implementation; a black-box oracle for SPARQL results and a benchmark target for RDF loading and queries.

### RDFox

- **What it is:** a main-memory RDF store and Datalog reasoner ([features](https://docs.oxfordsemantic.tech/features-and-requirements.html)).
- **Languages and features:** SPARQL 1.1; rules in RDFox's Datalog dialect, OWL 2 and SWRL import; materialization-based reasoning that is updated incrementally; proofs for derived facts; SHACL validation; ACID transactions; incremental persistence to a binary file (same source).
- **Algorithms:** reasoning rather than graph analytics. Parallel materialization breaks the work "into as many subtasks as there are triples", with "almost" lock-free index updates; 87x speed-up on 128 cores (1,024 threads) for DBpedia. Deletion uses the backward/forward algorithm, which checks for an alternative derivation before deleting, instead of DRed's overdelete-then-rederive ([Nenov et al. 2015](https://www.cs.ox.ac.uk/people/boris.motik/pubs/npmhwb15RDFox-scalable.pdf); [Motik et al. 2015](https://www.cs.ox.ac.uk/boris.motik/pubs/mnph15incremental-BF-sameAs.pdf)).
- **Memory:** the vendor recommends 60 to 110 bytes of RAM per triple, imported or derived ([features](https://docs.oxfordsemantic.tech/features-and-requirements.html)); the 2015 paper reports 36.9 to 124.1 bytes per triple across datasets.
- **Licence:** proprietary; a server needs a "time-limited license key" (same source).
- **Oracle value: medium.** The reference point for incremental Datalog materialization; licence keys make it awkward for unattended comparison runs.

### QLever

- **What it is:** a SPARQL engine that "implements the full SPARQL 1.1 standard" (including update and the Graph Store protocol), with text search combined with SPARQL, autocompletion and spatial queries; it can also run embedded in C++ programs ([repository](https://github.com/ad-freiburg/qlever)). Full SPARQL 1.1 compliance was reached in June 2025 ([Wikipedia](https://en.wikipedia.org/wiki/QLever)).
- **Scale:** "more than a trillion triples on a single commodity machine" (repository).
- **Index design:** identifiers in lexicographic order with numeric values encoded so ID order equals value order, so filters compare IDs; PSO and POS permutations suffice for typical queries (all six optional); per-predicate pair lists, blocked with in-memory block starts; joins mostly merge joins over sorted lists; a dynamic-programming planner whose scan sizes come from the index and whose multiplicities are stored as one-byte logarithms; results are materialized bottom-up and cached across queries ([Bast and Buchhold 2017](https://ad-publications.informatik.uni-freiburg.de/CIKM_qlever_BB_2017.pdf)).
- **Licence:** Apache-2.0 (repository).
- **Benchmarks:** none from LDBC; recommended in 2026 as the new Wikidata Query Service database ("we recommend QLever as the new RDF database for the Wikidata Platform", the Wikidata backend replacement proposal as [mirrored here](https://hackernews-dynamic.seasondane.workers.dev/news/48188965)).
- **Oracle value: high.** Permissive, runs locally, scales to the largest public RDF dumps; the obvious SPARQL oracle and benchmark target.

### AllegroGraph

- **What it is:** an RDF store holding each triple with a graph and a triple id, with seven default indexes (spogi, posgi, ospgi, gspoi, gposi, gospi, i) that degrade under updates and are rewritten by an optimization step ([docs](https://allegro.callisto.calmip.univ-toulouse.fr/doc/triple-index.html)).
- **Licence:** proprietary; clients under the Eclipse Public License 1.0 ([Wikipedia](https://en.wikipedia.org/wiki/Graph_Database)).
- **Oracle value: low.** Proprietary and adds no algorithms not available elsewhere.

### Blazegraph

- **What it is:** a Java triplestore and graph database with SPARQL and TinkerPop 3 support ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGraphDB%3BMemgraph)); GPL-2.0; last stable release 2.1.5 (19 March 2019); "Amazon acquired the Blazegraph developers" and open source development essentially stopped in April 2018 ([Wikipedia](https://en.wikipedia.org/wiki/Blazegraph)).
- **Why Wikidata is leaving it:** Wikimedia's epic noted the project "seems to not be active anymore" and required full SPARQL 1.1 with update, open source, and the ability to load all of Wikidata ([T206560](https://phabricator.wikimedia.org/T206560)). At about 16 billion triples Wikidata is "beyond what it was built for"; Blazegraph does not distribute data itself, so Wikimedia runs full copies, and the scholarly articles were split into a separate graph, doubling maintenance ([BigDATAwire, July 2025](https://www.bigdatawire.com/2025/07/10/scaling-the-knowledge-graph-behind-wikipedia)). A recent load failure is logged in November 2025 ([T417504](https://phabricator.wikimedia.org/T417504)). The 2026 evaluation left QLever and Virtuoso as finalists ([report](https://wikwiand-revamp.pages.dev/en/Wikipedia:Wikipedia_Signpost/2026-02-17/Technology_report)), and the replacement proposal recommends QLever (see QLever).
- **Oracle value: low.** Unmaintained; useful only to reproduce historical Wikidata query behaviour.

## Property-graph databases

### TigerGraph

- **What it is:** a native massively parallel (MPP) property-graph database. Storage is compressed ("typical compression factors are between 2x and 10x"); vertices are placed by hash and a vertex's out-edges live on one server; queries run vertex- and edge-parallel in bulk synchronous phases with accumulators ([Deutsch et al. 2019](https://arxiv.org/pdf/1901.08248.pdf)). The paper's loading results imply about 6.5 bytes per edge for the Twitter graph (9.5 GB for 1.47 billion edges, derived).
- **Language:** GSQL, SQL-like with pattern matching, accumulators (`@` per vertex, `@@` global) and loops for iterative algorithms (same source).
- **Algorithms:** a GSQL algorithm library; the free Community Edition allows 300 GB and 16 CPUs on a single server ([Community Edition](https://www.tigergraph.com/community-edition/)).
- **Licence:** proprietary.
- **Benchmarks:** audited SNB BI at SF100 to SF10000 (table above).
- **Oracle value: medium.** Audited scale results make it a benchmark reference; algorithm semantics are in GSQL source that must be read per algorithm.

### NebulaGraph

- **What it is:** a distributed property-graph database. Vertices and edges are key-value pairs in RocksDB; each edge is stored twice (out-key in the source's partition, in-key in the target's); partitions are a static hash of the vertex id and are replicated by Raft ([docs](https://docs.nebula-graph.io/3.8.0/1.introduction/3.nebula-graph-architecture/4.storage-service/)).
- **Licence:** "Apache 2.0, Common Clause 1.0" for the open source edition as listed by [Wikipedia](https://en.wikipedia.org/wiki/Graph_Database); check the repository before use.
- **Oracle value: low.** A cluster system with no audited results; analytics live in separate tools.

### JanusGraph

- **What it is:** a graph layer storing each vertex's adjacency list as one row of a Bigtable-model store (Cassandra, HBase, Berkeley DB), with every edge stored at both endpoints and cells sorted by edge label sort keys for vertex-centric indexes ([data model](https://old-docs.janusgraph.org/0.3.2/data-model.html)). Gremlin only; transactions "are not necessarily ACID"; Apache-2.0, hosted by the Linux Foundation ([DBDB](https://dbdb.io/db/janusgraph)).
- **Oracle value: low.** Gremlin semantics are better checked on the TinkerPop reference implementation.

### Dgraph

- **What it is:** a distributed graph database storing posting lists keyed by subject and predicate, grouped by predicate into tablets so a join runs on one server ([docs](https://docs.dgraph.io/design-concepts/posting-list-concept)); Badger (an LSM key-value store) underneath, MVCC with snapshot isolation, Raft replication, DQL and GraphQL, Apache-2.0 ([DBDB](https://dbdb.io/db/dgraph/revisions/17)).
- **Oracle value: low.** Few analytics; query semantics are its own.

### HugeGraph

- **What it is:** an Apache Software Foundation graph system with Gremlin and openCypher, RocksDB (standalone) or HStore (distributed) storage, and two analytics engines: Vermeer (Go, in memory) and Computer (Java, BSP/Pregel, spills to disk) ([docs](https://hugegraph.apache.org/docs/introduction/)). Licence Apache-2.0 as an ASF top-level project ([ArcadeDB survey](https://arcadedb.com/blog/neo4j-alternatives-in-2026-a-fair-look-at-the-open-source-options/)).
- **Oracle value: medium.** Permissive and has Pregel-style implementations of common algorithms to compare; the algorithm list is not documented on the overview page.

### TuGraph

- **What it is:** Ant Group's property-graph database (openCypher, "Graph analytics algorithms embedded with graph computing framework", Apache-2.0, [repository](https://github.com/TuGraph-family/tugraph-db)). Storage packs a vertex's out- and in-edges CSR-style under its key with properties beside them, merging small vertices into one key-value pair and splitting large ones, on LMDB (a B+ tree) chosen over RocksDB for read performance ([storage paper](https://pacman.cs.tsinghua.edu.cn/~cwg/publication/10372995/10372995.pdf)).
- **Benchmarks:** audited SNB Interactive (2020 to 2023) and SNB BI at SF30000 (table above).
- **Oracle value: medium.** Permissive with audited results; documentation of algorithm conventions is thin.

### GraphScope

- **What it is:** Alibaba's graph computing stack, Apache-2.0 ([ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Falibaba%2FGraphScope)). Components include GRAPE (distributed analytics, CPU and GPU), Gaia (dataflow queries), Hiactor (high-throughput queries), Vineyard (immutable in-memory storage), GART (multi-version mutable storage), GraphAr (file format), Graph-Learn (GNN sampling) and GRIN (a common storage access interface); Gremlin and Cypher ([GraphScope Flex](https://graphscope.io/blog/tech/2024/08/05/GraphScope-Flex-LEGO-like-Graph-Computing-Stack)).
- **Programming models:** PIE (PEval, IncEval, Assemble), which parallelizes a sequential algorithm by running it per fragment and then an incremental step on received messages until a fixpoint ([PIE](https://graphscope.io/docs/analytical_engine/programming_model_pie)); Pregel and FLASH are also offered.
- **Benchmarks:** audited SNB Interactive v1 up to SF1000 (table above).
- **Oracle value: high.** Permissive, runs on one machine, implements the Graphalytics-style algorithms at scale; a strong benchmark target.

### Memgraph

- **What it is:** an in-memory property-graph database compatible with Neo4j's Cypher, with skip-list indexes, MVCC snapshot isolation, Raft replication ([DBDB](https://dbdb.io/db/memgraph/revisions/18)) and the MAGE algorithm library, whose online (dynamic) variants need the enterprise edition ([MAGE](https://memgraph.com/docs/mage/algorithms)).
- **Licence:** BSL-1.1, with a commercial enterprise licence ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGraphDB%3BMemgraph)).
- **Oracle value: medium.** Runs in a container and exposes many algorithms through Cypher; the licence is not OSI.

### FalkorDB

- **What it is:** a property-graph database (successor of RedisGraph) that holds one sparse adjacency matrix per graph, one per relationship type and one diagonal matrix per label, and evaluates patterns as GraphBLAS matrix products, reordering terms for sparse intermediates ([design](https://docs.falkordb.com/design)).
- **Licence:** SSPL-1.0 ([licence](https://docs.falkordb.com/references/license)).
- **Oracle value: low.** Few analytics; useful as a reference for linear-algebra pattern matching.

## Graph on relational and analytical engines

### Apache AGE

- **What it is:** a PostgreSQL extension; each graph is a PostgreSQL namespace with one table per label under parent vertex and edge tables, and openCypher runs inside SQL through the `cypher()` function returning `agtype` ([manual](https://age.apache.org/age-manual/master/intro/graphs.html)). Apache-2.0 as an ASF project.
- **Oracle value: medium.** Easy to run; a check on openCypher semantics over relational storage, not on analytics.

### DuckPGQ

- **What it is:** a DuckDB extension adding SQL/PGQ and graph functions (PageRank, weakly connected components, local clustering coefficient, shortest and cheapest paths, reachability; [extension page](https://duckdb.org/community_extensions/extensions/duckpgq)); MIT ([ecosyste.ms](https://science.ecosyste.ms/projects/17863)).
- **Design:** `MATCH` is rewritten to ordinary joins; path finding builds a CSR on the fly per query and runs vectorized multi-source BFS (one bit per search, 512 searches per AVX-512 register) or multi-source Bellman-Ford for cheapest paths ([ten Wolde et al., VLDB 2023 demo](https://www.vldb.org/pvldb/vol16/p4034-wolde.pdf)). The CIDR 2023 paper reports beating Neo4j on path finding and pattern matching on SNB-derived workloads, run by the authors ([paper](https://ir.cwi.nl/pub/32773/32773.pdf)).
- **Oracle value: high.** Embedded, permissive, scriptable from Python and R; an independent implementation of common algorithms and a benchmark target for SQL-hosted graph analytics.

### Google Spanner Graph

- **What it is:** a property-graph schema declared over existing Spanner tables, queried with ISO GQL interoperable with SQL, with vector and full-text search in graph queries ([overview](https://docs.cloud.google.com/spanner/docs/graph/overview?hl=en)). Algorithms announced in June 2026 (betweenness, closeness, PageRank, label propagation, correlation and modularity clustering, weakly connected components, shortest paths, similarity) are called from GQL and run "on dedicated compute resources, so as not to impact live production traffic", reading through Data Boost; Enterprise editions only ([blog](https://cloud.google.com/blog/products/databases/introducing-spanner-graph-algorithms)).
- **Oracle value: low.** Cloud-only and paid.

### PuppyGraph

- **What it is:** "A graph query engine, not a graph database": openCypher and Gremlin over tables left in lakehouse formats, warehouses and databases (Iceberg, Delta, Hudi, Snowflake, BigQuery, PostgreSQL and others); free Developer Edition, enterprise pricing otherwise ([site](https://puppygraph.com/)).
- **Oracle value: low.** Proprietary; its value is as a pattern (graph views over columnar tables), not as an oracle.

## Cloud graph services

### Amazon Neptune and Neptune Analytics

- **Neptune (database):** a managed graph database for Gremlin, openCypher and SPARQL storing quads (subject, predicate, object, graph or edge id) under three default indexes (SPOG, POGS, GPSO), with an optional OSGP index that costs up to 23% insert rate and 20% storage ([docs](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage-indexing.html)). Neptune is reported to be based on Blazegraph ([DB-Engines](https://db-engines.com/en/system/Blazegraph%3BGraphDB%3BMemgraph)).
- **Neptune Analytics:** an in-memory engine (November 2023) sized in memory-optimized capacity units of 1 GiB each, 128 to 4,096 per graph, loading from Neptune or S3, queried with openCypher ([AWS blog](https://aws.amazon.com/blogs/aws/introducing-amazon-neptune-analytics-a-high-performance-graph-analytics)). Algorithms are openCypher `CALL` procedures: BFS, SSSP, top-k and source-target shortest paths, egonet, degree, PageRank, closeness, eigenvector, similarity measures, WCC, SCC, label propagation, Louvain, Leiden and vector top-k ([algorithms](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/algorithms.html)).
- **Engine design (published 2025):** RDF and property graphs in one store of dictionary-encoded 64-bit ids; 16-byte edge tuples and 21-byte property tuples in 2 MB pages with a PAX layout; two-dimensional partitioning of topology; a columnar vectorized dataflow engine; MVCC adapted from Neumann et al.; statistics from extended characteristic sets with HyperLogLog sketches; multi-pass algorithms build partition-local CSR views ([Poseidon paper](https://arxiv.org/html/2510.11166v1)).
- **Licence:** proprietary services.
- **Oracle value:** Neptune **low** (cloud-only); Neptune Analytics **medium**: cloud-only and paid, but it documents its algorithm parameters and is a credible scale benchmark if access is available.

### Azure Cosmos DB for Apache Gremlin

- **What it is:** a managed property-graph service with wire compatibility with Apache TinkerPop ("Some features might differ"); Microsoft points users who want OLAP graph work or a Gremlin migration to Graph in Microsoft Fabric ([overview](https://learn.microsoft.com/en-us/azure/cosmos-db/gremlin/overview)).
- **Oracle value: low.** Cloud-only, no analytics.

### Aerospike Graph

- **What it is:** a stateless Gremlin (TinkerPop) compute layer, the Aerospike Graph Service, over the Aerospike key-value database, launched June 2023 ([architecture](https://aerospike.com/docs/graph/overview/architecture/); [announcement](https://aerospike.com/blog/introducing-aerospike-graph-database)). Licence terms not stated on those pages; commercial product.
- **Oracle value: low.**

## Multi-model and adjacent systems

### ArangoDB

- **What it is:** documents, key-value and graphs on one core, AQL, RocksDB storage, graph-aware sharding (SmartGraphs) in the enterprise edition ([Wikipedia](https://en.wikipedia.org/wiki/ArangoDB)).
- **Licence:** from 3.12 the source moved from Apache-2.0 to BSL-1.1 and the community binaries to a Community License that "limits its use for commercial purposes" and caps a cluster at 100 GB ([ArangoDB, October 2023](https://arango.ai/?p=2755)).
- **Oracle value: low.**

### SurrealDB

- **What it is:** a Rust multi-model database (documents, graph edges created with `RELATE`, record links) with HNSW vector and BM25 full-text indexes, embedded or server, distributed only in its enterprise and cloud offerings ([deep dive](https://surrealdb.com/deep-dive)); BSL ([DBDB](https://dbdb.io/db/surrealdb/revisions/20)).
- **Oracle value: low.**

### Weaviate

- **What it is:** a Go vector database with cross-references between objects, HNSW, flat and dynamic vector indexes, quantization (RQ, BQ, SQ, PQ) and ACORN filtered search by default ([vector index](https://docs.weaviate.io/weaviate/config-refs/schema/vector-index)); BSD-3-Clause ([ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fweaviate%2Fweaviate)).
- **Oracle value: low** for graph analytics; a reference for vector-index behaviour only.

## Brief entries

### Kùzu and LadybugDB

Kùzu was an embedded, disk-based property-graph database: columnar node properties, double-indexed CSR adjacency, factorized intermediate results, a worst-case optimal multiway join by adjacency-list intersection and morsel-driven parallelism ([CIDR 2023](https://cs.uwaterloo.ca/~ssalihog/papers/kuzu-tr.pdf)). The MIT-licensed project was archived in October 2025 ([The Register](https://www.theregister.com/2025/10/14/kuzudb_abandoned/)); LadybugDB is an MIT community fork ([ArcadeDB survey](https://arcadedb.com/blog/neo4j-alternatives-in-2026-a-fair-look-at-the-open-source-options/)). **Oracle value: medium** through the fork, if it stays maintained.

### TerminusDB

A versioned store of JSON documents as an RDF graph in immutable layers ("Every write is an immutable commit", [site](https://terminusdb.com/?p=6369)), built on succinct structures in a Rust library, Apache-2.0 since v4.0, queried with WOQL (Datalog-based) and GraphQL ([Wikipedia](https://en.wikipedia.org/wiki/TerminusDB)). An ingest of 17 billion triples took 13.57 bytes per triple ([DZone](https://dzone.com/articles/smaller-is-better-ultra-compact-graph-representati)). **Oracle value: low** for analytics.

### ArcadeDB

A multi-model database (graph, document, key-value and more) under Apache-2.0, embedded or server ([ArcadeDB](https://arcadedb.com/blog/neo4j-alternatives-in-2026-a-fair-look-at-the-open-source-options/)). **Oracle value: low.**

### AnzoGraph

A "native, massively parallel processing (MPP) graph OLAP database" with SPARQL 1.1, RDF-star, Cypher over Bolt on the same data, graph algorithms and extension libraries ([features](https://docs.cambridgesemantics.com/anzograph/userdoc/features.htm)); commercial with a free trial ([DB-Engines](https://db-engines.com/en/system/AnzoGraph+DB%3BBlazegraph%3BGraphDB%3BSingleStore)). **Oracle value: low.**

### Oracle Graph Server (PGX)

"A high-speed, in-memory, parallel server for property graph queries and analytics" with "More than 80 out-of-box parallelized, in-memory algorithms", SQL and PGQL property graphs and RDF graphs ([Oracle](https://www.oracle.com/database/integrated-graph-database/features/)). Graphalytics lists PGX.D among its supported platforms ([LDBC](https://ldbcouncil.org/benchmarks/graphalytics/algorithms/)). **Oracle value: low** (proprietary), though its algorithm documentation is detailed.

## Ranking as oracles

For graph analytics: GraphScope, DuckPGQ (high); HugeGraph, Memgraph, Neptune Analytics, TigerGraph, TuGraph, the Kùzu fork (medium). For SPARQL and RDF: QLever, Virtuoso (high); GraphDB, RDFox (medium, for reasoning). For openCypher semantics: Apache AGE and Memgraph (medium). Audited scale references: TigerGraph and TuGraph (SNB BI), GraphScope and TuGraph (SNB Interactive).

{% endraw %}
