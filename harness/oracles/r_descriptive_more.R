#!/usr/bin/env Rscript
# Golden values from igraph (Csardi and Nepusz 2006) and sna (Butts 2008) for
# the measures of manifest/descriptive_more.yaml that either
# implements: dyad census, degree distribution, Krackhardt's dimensions
# (sna), symmetrize, dichotomize (sna::event2dichot), cocitation and
# bibliographic coupling (igraph), and the motif census (igraph::motifs,
# igraph::triad_census, sna::triad.census). Encodings: bindings/descriptive_more.py.
#
#   Rscript oracles/r_descriptive_more.R
#
# Requires igraph, sna and yaml. Run from the repository root. NaN and NA are
# written as -999, as the engine runner does. A tool that has no value on a
# fixture writes nothing and the manifest declares it with undefined_on.
# Both tools are black boxes: the calls below only run their exported
# functions.

suppressPackageStartupMessages({
  library(igraph)
  library(sna)
})

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "descriptive_more.yaml"))

encode <- function(v) {
  v <- as.numeric(v)
  v[is.na(v)] <- -999
  v[is.infinite(v)] <- -1000
  formatC(v, digits = 17, format = "g")
}

# A vector is written one value per line; a matrix one row per line.
write_values <- function(oracle, fixture, variant, values) {
  d <- file.path(golden_dir, oracle, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  lines <- if (is.matrix(values)) {
    vapply(seq_len(nrow(values)), function(i) paste(encode(values[i, ]), collapse = " "),
           character(1))
  } else {
    encode(values)
  }
  writeLines(c("value", lines), file.path(d, paste0(variant, ".csv")))
}

applies <- function(spec, meta) {
  kind <- if (is.null(spec$applies_to)) "any" else spec$applies_to
  if (kind == "directed" && !meta$directed) return(FALSE)
  if (kind == "undirected" && meta$directed) return(FALSE)
  if (isTRUE(spec$requires_weights) && !meta$weighted) return(FALSE)
  TRUE
}

read_meta <- function(path) {
  txt <- paste(readLines(path), collapse = "")
  get <- function(key) sub(sprintf('.*"%s": *([^,}]+).*', key), "\\1", txt)
  list(n = as.integer(get("n")),
       directed = get("directed") == "true",
       weighted = get("weighted") == "true")
}

# Rows (i, j, value) with i < j of the non-zero entries of a symmetric matrix,
# 0-based; a matrix with 3 columns even when empty.
tie_rows <- function(m) {
  idx <- which(upper.tri(m) & m != 0, arr.ind = TRUE)
  idx <- idx[order(idx[, 1], idx[, 2]), , drop = FALSE]
  cbind(idx[, 1] - 1, idx[, 2] - 1, m[idx])[seq_len(nrow(idx)), , drop = FALSE]
}

# The edges of an undirected igraph graph as (low, high, 1) rows, sorted, 0-based.
unit_ties <- function(u) {
  k <- igraph::ecount(u)
  if (k == 0L) return(matrix(0, 0, 3))
  e <- igraph::ends(u, igraph::E(u), names = FALSE) - 1
  lo <- pmin(e[, 1], e[, 2])
  hi <- pmax(e[, 1], e[, 2])
  o <- order(lo, hi)
  cbind(lo[o], hi[o], 1)
}

pair_rows <- function(m, directed) {
  idx <- which(m != 0, arr.ind = TRUE)
  if (!directed) idx <- idx[idx[, 1] <= idx[, 2], , drop = FALSE]
  idx <- idx[order(idx[, 1], idx[, 2]), , drop = FALSE]
  matrix(idx - 1, ncol = 2)
}

# Population statistics of a degree sequence, as the engine reports them.
degree_summary <- function(deg) {
  n <- length(deg)
  s <- sort(deg)
  total <- sum(s)
  gini <- if (total > 0) (2 * sum(seq_len(n) * s) - (n + 1) * total) / (n * total) else NA
  c(mean(deg), sum((deg - mean(deg))^2) / n, min(deg), max(deg), gini)
}

degree_values <- function(g, mode, loops) {
  deg <- igraph::degree(g, mode = mode, loops = loops)
  hist <- round(igraph::degree_distribution(g, mode = mode, loops = loops) * length(deg))
  c(hist, degree_summary(deg))
}

triad_connected <- c("021D", "021U", "021C", "111D", "111U", "030T", "030C", "201", "120D",
                     "120U", "120C", "210", "300")

sna_dich <- function(W, rule, value, directed) {
  d <- if (rule == "cutoff") {
    sna::event2dichot(W, method = "absolute", thresh = value, leq = FALSE)
  } else {
    sna::event2dichot(W, method = "quantile", thresh = 1 - value, leq = FALSE)
  }
  pair_rows(d, directed)
}

igraph_values <- function(variant, e, g, gs, W, Wd, meta) {
  n <- meta$n
  switch(e$fn,
    dyad_census = {
      d <- igraph::dyad_census(gs)
      c(d$mut, d$asym, d$null)
    },
    degree_distribution = degree_values(g, e$mode, isTRUE(e$loops)),
    symmetrize = {
      comb <- c(max = "max", min = "min", sum = "sum", mean = "mean", product = "prod")[e$method]
      wg <- igraph::graph_from_adjacency_matrix(Wd, mode = "directed", weighted = TRUE)
      switch(e$method,
        strong = {
          unit_ties(igraph::as_undirected(gs, mode = "mutual"))
        },
        weak = {
          unit_ties(igraph::as_undirected(gs, mode = "collapse"))
        },
        max = , min = , sum = , mean = , product = {
          u <- igraph::as_undirected(wg, mode = "collapse",
                                     edge.attr.comb = list(weight = comb[[1]]))
          m <- igraph::as_adjacency_matrix(u, attr = "weight", sparse = FALSE)
          tie_rows(m)
        },
        NULL)
    },
    cocitation = , coupling = {
      cc <- if (e$kind == "cocitation") igraph::cocitation(gs) else igraph::bibcoupling(gs)
      tie_rows(cc)
    },
    motif_census = {
      if (meta$directed) {
        tc <- igraph::triad_census(gs)
        unname(tc[4:16])
      } else if (e$size == 3) {
        m <- igraph::motifs(gs, 3)
        c(m[3], m[4])
      } else {
        m <- igraph::motifs(gs, 4)
        unname(m[FOUR + 1])
      }
    },
    NULL)
}

sna_values <- function(variant, e, m0, W, Wd, meta) {
  switch(e$fn,
    dyad_census = {
      d <- sna::dyad.census(m0)
      c(d[1, "Mut"], d[1, "Asym"], d[1, "Null"])
    },
    krackhardt_dimensions = if (identical(e$part, "lubness")) {
      sna::lubness(m0)
    } else {
      c(sna::connectedness(m0), sna::hierarchy(m0, measure = "krackhardt"), sna::efficiency(m0))
    },
    symmetrize = {
      rule <- e$method
      if (!rule %in% c("upper", "lower", "strong", "weak")) return(NULL)
      tie_rows(sna::symmetrize(Wd, rule = rule))
    },
    dichotomize = {
      if (e$by == "cutoff" && e$rule == "ge") {
        sna_dich(W, "cutoff", e$value, meta$directed)
      } else if (e$by == "density") {
        sna_dich(W, "density", e$value, meta$directed)
      }
    },
    motif_census = {
      if (meta$directed) {
        tc <- sna::triad.census(m0, mode = "digraph")
        unname(tc[1, triad_connected])
      } else if (e$size == 3) {
        tc <- sna::triad.census(m0, mode = "graph")
        c(tc[1, 3], tc[1, 4])
      }
    },
    NULL)
}

attempt <- function(oracle, variant, name, expr) {
  tryCatch(expr, error = function(err) {
    message(sprintf("%s %s on %s failed: %s", oracle, variant, name, conditionMessage(err)))
    NULL
  })
}

# The 4-node undirected classes of igraph::motifs in the engine's order
# (star, path, cycle, paw, diamond, clique), found by asking igraph which
# of its 11 classes each shape is.
FOUR <- {
  shapes <- list(igraph::make_star(4, mode = "undirected"),
                 igraph::make_ring(4, circular = FALSE),
                 igraph::make_ring(4),
                 igraph::graph_from_literal(1 - 2, 2 - 3, 3 - 1, 3 - 4),
                 igraph::graph_from_literal(1 - 2, 2 - 3, 3 - 1, 2 - 4, 3 - 4),
                 igraph::make_full_graph(4))
  vapply(shapes, function(s) {
    hit <- which(vapply(0:10, function(id)
      igraph::isomorphic(igraph::graph_from_isomorphism_class(4, id, directed = FALSE), s),
      logical(1)))
    hit - 1
  }, numeric(1))
}

counts <- c(igraph = 0L, sna = 0L)
for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  e <- utils::read.csv(file.path(d, "edges.csv"))
  n <- meta$n
  g <- igraph::make_empty_graph(n = n, directed = meta$directed)
  if (nrow(e)) {
    g <- igraph::add_edges(g, as.vector(t(as.matrix(e[, c("from", "to")]))) + 1L)
    if (meta$weighted) igraph::E(g)$weight <- e$weight
  }
  # The simple unweighted reading: parallel edges once, loops dropped.
  gs <- igraph::simplify(if (meta$weighted) igraph::delete_edge_attr(g, "weight") else g)
  # Summed weights with the diagonal (W) and without it (Wd); an undirected
  # edge fills both triangles, a loop the diagonal once.
  W <- matrix(0, n, n)
  for (k in seq_len(nrow(e))) {
    i <- e$from[k] + 1L
    j <- e$to[k] + 1L
    x <- if (meta$weighted) e$weight[k] else 1
    W[i, j] <- W[i, j] + x
    if (!meta$directed && i != j) W[j, i] <- W[j, i] + x
  }
  Wd <- W
  diag(Wd) <- 0
  m0 <- (Wd != 0) * 1
  # sna reads an unweighted matrix: ties only (no weights), no diagonal.
  m0[Wd == 0] <- 0

  for (variant in names(manifest)) {
    spec <- manifest[[variant]]
    if (!applies(spec, meta)) next
    ev <- spec$params
    if ("igraph" %in% names(spec$oracles)) {
      v <- attempt("igraph", variant, name, igraph_values(variant, ev, g, gs, W, Wd, meta))
      if (!is.null(v)) {
        write_values("igraph", name, variant, v)
        counts[["igraph"]] <- counts[["igraph"]] + 1L
      }
    }
    if ("sna" %in% names(spec$oracles) && n > 0) {
      v <- attempt("sna", variant, name, sna_values(variant, ev, m0, W, Wd, meta))
      if (!is.null(v)) {
        write_values("sna", name, variant, v)
        counts[["sna"]] <- counts[["sna"]] + 1L
      }
    }
  }
}

writeLines(sprintf("igraph %s", utils::packageVersion("igraph")),
           file.path(golden_dir, "igraph", "VERSION"))
writeLines(sprintf("sna %s", utils::packageVersion("sna")),
           file.path(golden_dir, "sna", "VERSION"))
cat(sprintf("Wrote %d igraph and %d sna golden files (descriptive_more).\n",
            counts[["igraph"]], counts[["sna"]]))
