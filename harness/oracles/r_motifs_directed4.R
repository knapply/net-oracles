#!/usr/bin/env Rscript
# Golden values from R igraph (Csardi and Nepusz 2006) for the directed size-4
# motif census (manifest/motifs_directed4.yaml):
# igraph::motifs(g, 4) on the simple digraph. It returns NA for the 19
# isoclasses that are not weakly connected; they are dropped, leaving the 199
# connected classes in igraph's id order. igraph is run as a black box.
#
#   Rscript oracles/r_motifs_directed4.R
#
# Run from the repository root.

suppressPackageStartupMessages(library(igraph))

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "motifs_directed4.yaml"))

read_meta <- function(path) {
  txt <- paste(readLines(path), collapse = "")
  get <- function(key) sub(sprintf('.*"%s": *([^,}]+).*', key), "\\1", txt)
  list(n = as.integer(get("n")), directed = get("directed") == "true")
}

count <- 0L
for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  if (!meta$directed) next
  e <- utils::read.csv(file.path(d, "edges.csv"))
  g <- igraph::make_empty_graph(n = meta$n, directed = TRUE)
  if (nrow(e)) g <- igraph::add_edges(g, as.vector(t(as.matrix(e[, c("from", "to")]))) + 1L)
  g <- igraph::simplify(g)
  counts_by_class <- igraph::motifs(g, 4)
  values <- counts_by_class[!is.na(counts_by_class)]
  for (variant in names(manifest)) {
    if (!("igraph" %in% names(manifest[[variant]]$oracles))) next
    out <- file.path(golden_dir, "igraph", name)
    dir.create(out, recursive = TRUE, showWarnings = FALSE)
    writeLines(c("value", formatC(as.numeric(values), digits = 17, format = "g")),
               file.path(out, paste0(variant, ".csv")))
    count <- count + 1L
  }
}

dir.create(file.path(golden_dir, "igraph"), recursive = TRUE, showWarnings = FALSE)
writeLines(sprintf("igraph %s", utils::packageVersion("igraph")),
           file.path(golden_dir, "igraph", "VERSION"))
cat(sprintf("Wrote %d igraph golden files (motifs_directed4).\n", count))
