#!/usr/bin/env Rscript
# Golden values from igraph (Csardi and Nepusz 2006), whose automorphism and
# canonical-form functions call bliss (Junttila and Kaski 2007), for the
# automorphism measures (manifest/automorphisms.yaml). igraph is
# run as a black box.
#
#   Rscript oracles/r_automorphisms.R
#
# Requires igraph and yaml. Run from the repository root.
#
# bliss takes simple coloured graphs, so each fixture is reduced as in
# oracles/aut_reduce.py: self-loops become part of the node colour,
# and under `multiplicity` each pair is subdivided by a node coloured by the
# number of parallel edges (the group order and the orbits of the original
# nodes are those of the multigraph). The order is
# `igraph::count_automorphisms(g, colors)$group_size` (an exact decimal
# string), written as 16-bit limbs, least significant first, as the engine's
# runner does. The orbits are the classes of the original nodes joined by
# the generators of `igraph::automorphism_group`. The `generators` entry has
# the order's value. Canonical forms: for each of 8 seeded relabelings, and
# for rev(fixture) and perturbed(fixture), whether the graph permuted by
# `igraph::canonical_permutation` (with its colours) is the same as the
# fixture's.

suppressPackageStartupMessages(library(igraph))

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "automorphisms.yaml"))

fmt <- function(x) formatC(as.numeric(x), digits = 17, format = "g")

write_values <- function(oracle, fixture, variant, values) {
  d <- file.path(golden_dir, oracle, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  writeLines(c("value", fmt(values)), file.path(d, paste0(variant, ".csv")))
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

# 16-bit limbs, least significant first, of a decimal string.
decimal_to_limbs16 <- function(text) {
  digits <- as.integer(strsplit(text, "")[[1]])
  limbs <- integer(0)
  while (length(digits) > 0 && !(length(digits) == 1 && digits[1] == 0)) {
    remainder <- 0
    quotient <- integer(length(digits))
    for (i in seq_along(digits)) {
      current <- remainder * 10 + digits[i]
      quotient[i] <- current %/% 65536
      remainder <- current %% 65536
    }
    limbs <- c(limbs, remainder)
    first <- which(quotient != 0)
    digits <- if (length(first)) quotient[first[1]:length(quotient)] else integer(0)
  }
  if (!length(limbs)) 1 else limbs
}

first_appearance <- function(x) match(x, unique(x)) - 1L

# The coloured simple graph of a fixture: list(n, edges (a matrix of 0-based
# pairs), colors (integers), n_original). `user` is one colour per original node.
reduce_graph <- function(n, from, to, directed, user, multi) {
  loops <- integer(n)
  keys <- character(0)
  a_of <- integer(0)
  b_of <- integer(0)
  counts <- integer(0)
  for (i in seq_along(from)) {
    a <- from[i]
    b <- to[i]
    if (a == b) {
      loops[a + 1L] <- loops[a + 1L] + 1L
      next
    }
    if (!directed && b < a) { t <- a; a <- b; b <- t }
    key <- paste(a, b)
    hit <- match(key, keys)
    if (is.na(hit)) {
      keys <- c(keys, key); a_of <- c(a_of, a); b_of <- c(b_of, b); counts <- c(counts, 1L)
    } else {
      counts[hit] <- counts[hit] + 1L
    }
  }
  ord <- order(a_of, b_of)
  a_of <- a_of[ord]; b_of <- b_of[ord]; counts <- counts[ord]
  node_tuple <- sprintf("0:%d:%d", user, if (multi) loops else as.integer(loops > 0))
  if (multi) {
    k <- length(a_of)
    edge_tuple <- sprintf("1:%d:0", counts)
    edges <- rbind(cbind(a_of, n + seq_len(k) - 1L), cbind(n + seq_len(k) - 1L, b_of))
    tuples <- c(node_tuple, edge_tuple)
  } else {
    edges <- cbind(a_of, b_of)
    tuples <- node_tuple
  }
  list(n = length(tuples), edges = edges, tuples = tuples, n_original = n)
}

# Integer colours for the tuples of several graphs from one table.
color_ids <- function(...) {
  lists <- list(...)
  # Order tuples as (kind, value, loops) numerically, like the Python oracles.
  all <- unique(unlist(lists))
  parts <- do.call(rbind, lapply(strsplit(all, ":"), as.integer))
  table <- all[order(parts[, 1], parts[, 2], parts[, 3])]
  lapply(lists, function(l) match(l, table))
}

make_igraph <- function(red, directed) {
  edges <- red$edges
  igraph::make_graph(if (nrow(edges)) as.vector(t(edges)) + 1L else numeric(0),
                     n = red$n, directed = directed)
}

# A key that is equal for two coloured graphs exactly when bliss maps them to
# the same canonical graph.
canonical_key <- function(red, colors, directed) {
  g <- make_igraph(red, directed)
  cp <- igraph::canonical_permutation(g, colors = colors)
  labeling <- as.integer(cp$labeling)
  if (min(labeling) == 0L) labeling <- labeling + 1L
  permuted <- igraph::permute(g, labeling)
  new_colors <- integer(red$n)
  new_colors[labeling] <- colors
  el <- igraph::as_edgelist(permuted, names = FALSE)
  if (!directed && nrow(el)) el <- t(apply(el, 1, sort))
  if (nrow(el)) el <- el[order(el[, 1], el[, 2]), , drop = FALSE]
  paste(red$n, paste(new_colors, collapse = ","), paste(el, collapse = ","), sep = "|")
}

rev_edges <- function(n, from, to) list(perm = rev(seq_len(n)) - 1L,
                                        from = rev(n - 1L - from), to = rev(n - 1L - to))
perturbed_edges <- function(n, from, to) list(perm = seq_len(n) - 1L,
                                              from = c(from[-1], 0L), to = c(to[-1], n - 1L))

count <- 0L
for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  n <- meta$n
  if (n == 0) next
  e <- utils::read.csv(file.path(d, "edges.csv"))
  from <- as.integer(e$from)
  to <- as.integer(e$to)
  for (variant in names(manifest)) {
    spec <- manifest[[variant]]
    if (!applies(spec, meta) || !("igraph" %in% names(spec$oracles))) next
    eng <- spec$params
    kind <- if (is.null(eng$colors)) "none" else eng$colors
    multi <- identical(eng$edges, "multiplicity")
    base <- if (kind == "none") integer(n) else (seq_len(n) - 1L) %% 2L
    red <- reduce_graph(n, from, to, meta$directed, base, multi)
    values <- tryCatch({
      if (eng$fn == "automorphism") {
        colors <- color_ids(red$tuples)[[1]]
        g <- make_igraph(red, meta$directed)
        if (eng$output == "orbits") {
          gens <- igraph::automorphism_group(g, colors = colors)
          parent <- seq_len(red$n)
          find <- function(x) { while (parent[x] != x) x <- parent[x]; x }
          for (p in gens) for (v in seq_len(red$n)) {
            a <- find(v); b <- find(as.integer(p)[v])
            if (a != b) parent[a] <- b
          }
          first_appearance(vapply(seq_len(n), find, 1L))
        } else {
          size <- igraph::count_automorphisms(g, colors = colors)$group_size
          if (!grepl("^[0-9]+$", size)) stop("group_size is not an exact integer: ", size)
          decimal_to_limbs16(size)
        }
      } else {
        make_other <- function(perm, f, t) {
          moved <- integer(n)
          moved[perm + 1L] <- base
          reduce_graph(n, f, t, meta$directed, moved, multi)
        }
        same <- function(other) {
          ids <- color_ids(red$tuples, other$tuples)
          canonical_key(red, ids[[1]], meta$directed) == canonical_key(other, ids[[2]], meta$directed)
        }
        if (eng$check == "relabelings") {
          hits <- 0L
          for (s in 0:7) {
            set.seed(1000L * nchar(name) + s)
            perm <- sample.int(n) - 1L
            flip <- if (meta$directed) rep(FALSE, length(from)) else stats::runif(length(from)) < 0.5
            f <- perm[from + 1L]; t <- perm[to + 1L]
            f2 <- ifelse(flip, t, f); t2 <- ifelse(flip, f, t)
            order <- sample.int(length(f2))
            hits <- hits + as.integer(same(make_other(perm, f2[order], t2[order])))
          }
          hits
        } else {
          r <- rev_edges(n, from, to)
          p <- perturbed_edges(n, from, to)
          c(as.integer(same(make_other(r$perm, r$from, r$to))),
            as.integer(same(make_other(p$perm, p$from, p$to))))
        }
      }
    }, error = function(err) {
      message(sprintf("igraph %s on %s failed: %s", variant, name, conditionMessage(err)))
      NULL
    })
    if (!is.null(values)) {
      write_values("igraph", name, variant, values)
      count <- count + 1L
    }
  }
}
dir.create(file.path(golden_dir, "igraph"), recursive = TRUE, showWarnings = FALSE)
writeLines(sprintf("igraph %s", utils::packageVersion("igraph")),
           file.path(golden_dir, "igraph", "VERSION"))
cat(sprintf("igraph: wrote %d golden files\n", count))
