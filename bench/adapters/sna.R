#!/usr/bin/env Rscript
# sna (statnet) on a sparse edge list; the package computes every node, so only measures over all nodes are offered.
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(sna))

bench_main(
  tool = "sna",
  version = function() as.character(packageVersion("sna")),
  load = function(ctx) {
    el <- matrix(ctx$edges + 1L, ncol = 2, byrow = TRUE)
    attr(el, "n") <- ctx$n
    el
  },
  calls = list(
    components = function(G, ctx) list(components = sum(component.dist(G, connected = "weak")$cdist)),
    closeness = function(G, ctx) vec(closeness(G, gmode = if (ctx$directed) "digraph" else "graph", cmode = if (ctx$directed) "directed" else "undirected"))
  )
)
