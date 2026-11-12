#!/usr/bin/env Rscript
# network (statnet): construction of a network object from an edge-list data frame, and conversion back.
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(network))

edge_frame <- function(ctx) {
  e <- matrix(ctx$edges + 1L, ncol = 2, byrow = TRUE)
  data.frame(from = e[, 1], to = e[, 2])
}
build <- function(df, ctx) as.network(df, directed = ctx$directed, loops = FALSE, multiple = FALSE,
                                      vertices = data.frame(vertex.names = seq_len(ctx$n)), matrix.type = "edgelist")

bench_main(
  tool = "network",
  version = function() as.character(packageVersion("network")),
  load = function(ctx) {
    # G is the network built from the frame; network_build rebuilds it from the stored frame
    ctx$.df <- edge_frame(ctx)
    structure(list(nw = build(ctx$.df, ctx), df = ctx$.df), class = "netbox")
  },
  calls = list(
    network_build = function(G, ctx) { nw <- build(G$df, ctx); list(nodes = network.size(nw), edges = network.edgecount(nw)) },
    network_frame = function(G, ctx) { d <- as.data.frame(G$nw); list(rows = nrow(d), edges = network.edgecount(G$nw)) }
  )
)
