#!/usr/bin/env Rscript
# Writes a statistical-modelling dataset as text, for tools that do not read R data:
#   Rscript bench/data/export_statnet.R DATASET OUTDIR
# OUTDIR/meta.tsv   n, directed, waves
# OUTDIR/edges.tsv  wave, from, to (1-based), one row per tie
# OUTDIR/nodes.tsv  one column per node attribute
args <- commandArgs(TRUE)
ds <- args[1]; out <- args[2]
dir.create(out, recursive = TRUE, showWarnings = FALSE)
suppressPackageStartupMessages(library(network))

from_networks <- function(nets) {
  directed <- is.directed(nets[[1]])
  el <- do.call(rbind, lapply(seq_along(nets), function(w) {
    e <- as.edgelist(nets[[w]])
    if (!nrow(e)) return(NULL)
    data.frame(wave = w, from = e[, 1], to = e[, 2])
  }))
  at <- list.vertex.attributes(nets[[1]])
  at <- setdiff(at, c("na", "vertex.names"))
  nd <- as.data.frame(lapply(at, function(a) get.vertex.attribute(nets[[1]], a)), stringsAsFactors = FALSE)
  names(nd) <- at
  list(n = network.size(nets[[1]]), directed = directed, edges = el, nodes = nd, waves = length(nets))
}

get_data <- function(name, pkgs) {
  for (p in pkgs) {
    ok <- tryCatch({ e <- new.env(); suppressMessages(utils::data(list = name, package = p, envir = e)); length(ls(e)) > 0 }, error = function(e) FALSE, warning = function(w) FALSE)
    if (ok) { e <- new.env(); utils::data(list = name, package = p, envir = e); return(e) }
  }
  stop("dataset ", name, " not found in ", paste(pkgs, collapse = ", "))
}

res <- switch(ds,
  flomarriage = { e <- get_data("florentine", "ergm"); from_networks(list(e$flomarriage)) },
  faux.mesa.high = { e <- get_data("faux.mesa.high", "ergm"); from_networks(list(e$faux.mesa.high)) },
  samplk = { e <- get_data("samplk", "ergm"); from_networks(list(e$samplk1, e$samplk2, e$samplk3)) },
  lazega = {
    # Lazega's law firm, collaboration ties (undirected, 36 lawyers), from the sand package
    suppressPackageStartupMessages(library(sand)); suppressMessages(g <- igraph::upgrade_graph(sand::lazega))
    el <- igraph::as_edgelist(g, names = FALSE)
    at <- igraph::vertex_attr_names(g); at <- setdiff(at, "name")
    nd <- as.data.frame(lapply(at, function(a) igraph::vertex_attr(g, a)))
    names(nd) <- at
    list(n = igraph::vcount(g), directed = FALSE, edges = data.frame(wave = 1L, from = el[, 1], to = el[, 2]), nodes = nd, waves = 1L)
  },
  s50 = {
    suppressPackageStartupMessages(library(RSiena))
    mats <- list(s501, s502, s503)
    el <- do.call(rbind, lapply(1:3, function(w) { ij <- which(mats[[w]] == 1, arr.ind = TRUE); data.frame(wave = w, from = ij[, 1], to = ij[, 2]) }))
    list(n = nrow(s501), directed = TRUE, edges = el, nodes = data.frame(alcohol1 = s50a[, 1], alcohol2 = s50a[, 2], alcohol3 = s50a[, 3]), waves = 3)
  },
  stop("unknown dataset ", ds))
write.table(data.frame(n = res$n, directed = as.integer(res$directed), waves = res$waves), file.path(out, "meta.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
write.table(res$edges, file.path(out, "edges.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
write.table(res$nodes, file.path(out, "nodes.tsv"), sep = "\t", quote = FALSE, row.names = FALSE)
