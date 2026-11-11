#!/usr/bin/env Rscript
# oracle-entries: netrankr
# Golden values from netrankr (`schoch2018centrality`), which builds centralities as
# an indirect relation between pairs (indirect_relations()) aggregated per
# node (aggregate_positions()); an implementation independent of igraph's
# centrality code (igraph supplies only the graph object).
#
#   Rscript oracles/r_netrankr.R
#
# netrankr is for undirected, unweighted, simple graphs, so every fixture
# is read that way (igraph::simplify of the undirected reading); the
# manifest records where that reading differs from the engine's. Two
# conventions are mapped here: the pair dependencies of 'depend_sp' and
# 'depend_curflow' summed over a node count both orderings of an
# unordered pair (twice the usual betweenness), and 'dist_resist' with
# 'invsum' is information centrality divided by n (as in NetworkX).
# Requires netrankr, igraph, and yaml; exits quietly without netrankr.

if (!requireNamespace("netrankr", quietly = TRUE)) {
  cat("netrankr is not installed; no netrankr golden files written.\n")
  quit(status = 0)
}

# ---- shared plumbing (the same in every r_<tool>.R; R scripts stay
# self-contained, see README.md) -------------------------------

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))

# Every manifest entry, and the area (manifest file) each comes from.
manifest <- list()
area_of <- character()
for (f in sort(list.files(file.path(root, "manifest"), "\\.yaml$",
                          full.names = TRUE))) {
  y <- yaml::read_yaml(f)
  for (k in names(y)) {
    manifest[[k]] <- y[[k]]
    area_of[[k]] <- sub("\\.yaml$", "", basename(f))
  }
}

# How each area writes values that are not finite (its manifest header):
# NaN and +Inf markers; "" is an empty line; NA leaves the value.
encoding <- list(
  assortativity = c(-999, NA), centrality_extra = c(-999, -1000),
  descriptive = c(-999, -1000), distance_measures = c(-999, -1000),
  temporal = c(-999, -1000), topography = c(-1, NA), groups = c(-1, NA),
  resilience = c(-1, NA), twomode = c(-1, NA), connectivity = c(-1, NA),
  spectral = c("", NA), roles = c("", NA), positions = c("", NA))

format_row <- function(x, area) {
  code <- encoding[[area]]
  x <- as.numeric(x)
  out <- formatC(x, digits = 17, format = "g")
  if (!is.null(code)) {
    if (!is.na(code[1])) out[is.nan(x) | is.na(x)] <- code[1]
    if (!is.na(code[2])) out[is.infinite(x) & x > 0] <- code[2]
  }
  if (area == "distance_measures") out[is.infinite(x) & x < 0] <- "-1001"
  if (length(out) == 1L && out == "") return("")
  paste(out, collapse = " ")
}

# values: a numeric vector (one value per line) or a list of numeric
# vectors (one group per line).
write_values <- function(oracle, fixture, variant, values) {
  area <- area_of[[variant]]
  lines <- if (is.list(values)) vapply(values, format_row, "", area = area)
           else vapply(as.numeric(values), format_row, "", area = area)
  d <- file.path(golden_dir, oracle, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  writeLines(c("value", lines), file.path(d, paste0(variant, ".csv")))
}

applies <- function(spec, meta) {
  kind <- if (is.null(spec$applies_to)) "any" else spec$applies_to
  if (kind == "directed" && !meta$directed) return(FALSE)
  if (kind == "undirected" && meta$directed) return(FALSE)
  if (isTRUE(spec$requires_weights) && !meta$weighted) return(FALSE)
  TRUE
}

# meta.json is flat and simple; parse it without a JSON dependency.
read_meta <- function(path) {
  txt <- paste(readLines(path), collapse = "")
  get <- function(key) sub(sprintf('.*"%s": *([^,}]+).*', key), "\\1", txt)
  list(n = as.integer(get("n")),
       directed = get("directed") == "true",
       weighted = get("weighted") == "true")
}

load_fixture <- function(name) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  e <- utils::read.csv(file.path(d, "edges.csv"))
  if (!meta$weighted) e$weight <- rep(1, nrow(e))
  list(name = name, n = meta$n, directed = meta$directed, weighted = meta$weighted,
       from = e$from, to = e$to, weight = e$weight)
}

# The fixture as an igraph graph (1-based vertices, parallel edges and loops
# kept, weights as the `weight` attribute when the fixture has them).
as_igraph <- function(fx, weighted = fx$weighted) {
  g <- igraph::make_empty_graph(n = fx$n, directed = fx$directed)
  if (length(fx$from)) {
    g <- igraph::add_edges(g, as.vector(rbind(fx$from, fx$to)) + 1L)
    if (weighted) igraph::E(g)$weight <- fx$weight
  }
  g
}

# Dense adjacency: parallel edges summed (weights when weighted), loops on
# the diagonal once, or dropped; simple = 0/1.
adjacency <- function(fx, weighted = FALSE, loops = TRUE, simple = FALSE) {
  m <- matrix(0, fx$n, fx$n)
  for (i in seq_along(fx$from)) {
    a <- fx$from[i] + 1L
    b <- fx$to[i] + 1L
    x <- if (weighted) fx$weight[i] else 1
    if (a == b) {
      if (loops) m[a, a] <- m[a, a] + x
      next
    }
    m[a, b] <- m[a, b] + x
    if (!fx$directed) m[b, a] <- m[b, a] + x
  }
  if (simple) m <- (m != 0) * 1
  m
}

node_rule <- function(rule, n) {
  v <- seq_len(n) - 1
  switch(rule, mod3 = v %% 3, mod2 = v %% 2, mod3plus1 = v %% 3 + 1,
         blocks3 = (3 * v) %/% n, num7 = (7 * v) %% 11, num3 = (3 * v) %% 5, id = v,
         stop("unknown node rule ", rule))
}

# Runs compute(variant, spec, fx) for every variant that lists `oracle` on
# every fixture it applies to. An error on one input is reported and writes
# nothing, so the comparison shows it as not run until the manifest records
# it as undefined.
run_oracle <- function(oracle, version, compute) {
  count <- 0L
  errors <- 0L
  for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
    if (!file.exists(file.path(fixtures_dir, name, "meta.json"))) next
    fx <- load_fixture(name)
    for (variant in names(manifest)) {
      spec <- manifest[[variant]]
      if (!(oracle %in% names(spec$oracles)) || !applies(spec, fx)) next
      v <- tryCatch(suppressWarnings(compute(variant, spec, fx)), error = function(err) {
        errors <<- errors + 1L
        message(sprintf("  %s on %s: %s", variant, name, conditionMessage(err)))
        NULL
      })
      if (is.null(v)) next
      write_values(oracle, name, variant, v)
      count <- count + 1L
    }
  }
  dir.create(file.path(golden_dir, oracle), recursive = TRUE, showWarnings = FALSE)
  writeLines(version, file.path(golden_dir, oracle, "VERSION"))
  cat(sprintf("%s: wrote %d golden files (%d inputs rejected by the tool)\n",
              version, count, errors))
}

# ---- end of shared plumbing ---------------------------------------------

simple_graph <- function(fx) {
  g <- as_igraph(fx, weighted = FALSE)
  if (igraph::is_directed(g)) g <- igraph::as_undirected(g, mode = "collapse")
  igraph::simplify(g)
}

compute <- function(variant, spec, fx) {
  e <- spec$params
  if (fx$directed || fx$n < 2) return(NULL)
  g <- simple_graph(fx)
  rel <- function(type, ...) netrankr::indirect_relations(g, type = type, ...)
  agg <- function(m, type) as.numeric(netrankr::aggregate_positions(m, type = type))
  switch(e$fn,
    closeness = if (!isTRUE(e$weighted) && identical(e$unreachable, "ignore") &&
                    !isTRUE(e$normalized)) agg(rel("dist_sp"), "invsum"),
    harmonic = if (!isTRUE(e$weighted) && !isTRUE(e$normalized))
      agg(rel("dist_sp", FUN = netrankr::dist_inv), "sum"),
    betweenness = if (!isTRUE(e$weighted) && !isTRUE(e$normalized)) agg(rel("depend_sp"), "sum") / 2,
    information_centrality = if (!isTRUE(e$weighted)) igraph::vcount(g) * agg(rel("dist_resist"), "invsum"),
    cx_current_flow_closeness = if (!isTRUE(e$weighted)) agg(rel("dist_resist"), "invsum"),
    cx_resistance = if (!isTRUE(e$weighted)) {
      m <- rel("dist_resist")
      lapply(seq_len(nrow(m)), function(i) m[i, ])
    },
    cx_current_flow = if (!isTRUE(e$weighted) && identical(e$output %||% "nodes", "nodes") &&
                          identical(e$normalized, FALSE)) agg(rel("depend_curflow"), "sum") / 2,
    cx_communicability = {
      m <- rel("walks", FUN = netrankr::walks_exp)
      lapply(seq_len(nrow(m)), function(i) m[i, ])
    },
    NULL)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

run_oracle("netrankr", sprintf("netrankr %s", utils::packageVersion("netrankr")), compute)
