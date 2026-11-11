#!/usr/bin/env Rscript
# oracle-entries: tnet
# Golden values from tnet (Opsahl 2009), the reference implementation of
# weighted-network measures in which a weight is a tie's strength:
# path lengths are 1 / w^alpha (Opsahl, Agneessens, and Skvoretz 2010)
# and weighted clustering follows Opsahl and Panzarasa (2009).
#
#   Rscript oracles/r_tnet.R
#
# tnet takes an edge list (i, j, w) with 1-based node ids, rejects loops
# and repeated pairs, and wants undirected ties listed in both directions,
# so loops are dropped and parallel edges summed into one tie; the
# manifest records where that changes the answer. Requires tnet and yaml;
# exits quietly without tnet.

if (!requireNamespace("tnet", quietly = TRUE)) {
  cat("tnet is not installed; no tnet golden files written.\n")
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

# Summed simple tie list, both directions for undirected fixtures.
tnet_edges <- function(fx, weighted = TRUE) {
  m <- adjacency(fx, weighted = weighted, loops = FALSE)
  idx <- which(m != 0, arr.ind = TRUE)
  if (!nrow(idx)) return(NULL)
  df <- data.frame(i = idx[, 1], j = idx[, 2], w = m[idx])
  df[order(df$i, df$j), ]
}

# A tnet result (rows keyed by node id) as a vector over all n nodes;
# nodes tnet leaves out (isolates) are NA.
by_node <- function(res, col, n) {
  out <- rep(NA_real_, n)
  res <- as.data.frame(res)
  out[res$node] <- res[[col]]
  out
}

twomode_types <- function(name) {
  txt <- paste(readLines(file.path(fixtures_dir, name, "meta.json")), collapse = "")
  if (!grepl('"type"', txt)) return(NULL)
  as.integer(strsplit(sub('.*"type": *\\[([^]]*)\\].*', "\\1", txt), " *, *")[[1]])
}

compute <- function(variant, spec, fx) {
  e <- spec$params
  n <- fx$n
  if (n < 2) return(NULL)
  w <- isTRUE(e$weighted)
  net <- tnet_edges(fx)
  if (is.null(net) && e$fn != "project") return(NULL)
  dir <- fx$directed
  switch(e$fn,
    strength = {
      out <- by_node(tnet::degree_w(net, measure = "output", type = "out"), "output", n)
      if (dir) out + by_node(tnet::degree_w(net, measure = "output", type = "in"), "output", n)
      else out
    },
    betweenness = if (w && identical(e$weights_as, "strength") && !isTRUE(e$normalized))
      by_node(tnet::betweenness_w(net, directed = dir, alpha = 1), "betweenness", n),
    distances = if (w && identical(e$weights_as, "strength") && identical(e$mode, "out")) {
      d <- tnet::distance_w(net, directed = dir, gconly = FALSE)
      full <- matrix(Inf, n, n)
      full[seq_len(nrow(d)), seq_len(ncol(d))] <- d
      full[is.na(full)] <- Inf
      diag(full) <- 0
      lapply(seq_len(n), function(i) full[i, ])
    },
    closeness = if (w && identical(e$weights_as, "strength") && identical(e$mode, "out"))
      by_node(tnet::closeness_w(net, directed = dir, gconly = FALSE, alpha = 1),
              if (isTRUE(e$normalized)) "n.closeness" else "closeness", n),
    clustering = if (!dir && identical(e$weighting, "barrat"))
      by_node(tnet::clustering_local_w(net, measure = "am"), "am", n),
    project = {
      types <- twomode_types(fx$name)
      if (is.null(types) || isTRUE(e$loops) || !identical(e$weight %||% "count", "newman") &&
          !identical(e$weight %||% "count", "count")) return(NULL)
      keep <- if (isTRUE(e$second)) 1L else 0L
      a <- fx$from + 1L
      b <- fx$to + 1L
      # tnet's two-mode edge list: (node of the projected mode, other node).
      ta <- types[a]
      i <- ifelse(ta == keep, a, b)
      p <- ifelse(ta == keep, b, a)
      tm <- data.frame(i = i, p = p)
      method <- if (identical(e$weight, "newman")) "Newman" else "sum"
      pr <- as.data.frame(tnet::projecting_tm(tm, method = method))
      pr <- pr[pr$i < pr$j, ]
      pr <- pr[order(pr$i, pr$j), ]
      lapply(seq_len(nrow(pr)), function(k) c(pr$i[k] - 1, pr$j[k] - 1, pr$w[k]))
    },
    NULL)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

run_oracle("tnet", sprintf("tnet %s", utils::packageVersion("tnet")), compute)
