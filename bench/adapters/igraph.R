#!/usr/bin/env Rscript
# igraph through its R interface (tool id igraph), one thread.
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(igraph))

bench_main(
  tool = "igraph",
  version = function() as.character(packageVersion("igraph")),
  load = function(ctx) {
    g <- make_empty_graph(ctx$n, directed = ctx$directed)
    add_edges(g, ctx$edges + 1L)
  },
  calls = list(
    bfs = function(G, ctx) list(reached = sum(!is.na(bfs(G, ctx$sources[1] + 1L, mode = "out", unreachable = FALSE)$order))),
    components = function(G, ctx) list(components = components(G, mode = "weak")$no),
    pagerank = function(G, ctx) vec(page_rank(G, damping = 0.85)$vector),
    triangles = function(G, ctx) list(clustering_mean = sig(mean(transitivity(G, type = "local", isolates = "zero")))),
    betweenness = function(G, ctx) unsupported("no source subset in the R interface"),
    closeness = function(G, ctx) vec(closeness(G, normalized = TRUE))
  )
)
