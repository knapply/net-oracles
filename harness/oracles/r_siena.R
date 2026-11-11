#!/usr/bin/env Rscript
# oracle-entries: rsiena
# Golden values from RSiena (Ripley, Snijders, Boda, Voros, Preciado; manual
# `ripley2026manual`): simulation of a stochastic actor-oriented model
# (`snijders2001statistical`, `snijders2010introduction`) from fixed
# coefficients, for the SAOM entries of manifest/ergm.yaml that
# list a `rsiena` oracle. RSiena is run as a black box through its documented
# interface (siena07 with simOnly = TRUE and returnDeps = TRUE); its source is
# not read. The simulated networks are returned by the tool, and the
# statistics below are computed here from them, in the engine's terms:
# the mean over runs of the sum over actors of each effect's statistic at the
# end of the period, then the mean number of changed ties.
#
#   Rscript oracles/r_siena.R
#
# Requires RSiena and yaml; exits quietly without them. Run from the
# repository root. Every run starts from the fixture (loops dropped,
# repeated pairs once) with the same network at both waves, so only the
# first wave matters in simulation; the rate is the basic rate of the single
# period, with the unconditional scheme (cond = FALSE).

if (!requireNamespace("RSiena", quietly = TRUE) || !requireNamespace("yaml", quietly = TRUE)) {
  cat("RSiena is not installed; no rsiena golden files written.\n")
  quit(status = 0)
}
suppressPackageStartupMessages(library(RSiena))

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

# Leaves of a nested list that are matrices (one per iteration, group,
# dependent variable and period; here exactly one).
leaf_matrices <- function(x) {
  if (is.matrix(x)) return(list(x))
  if (is.list(x)) return(unlist(lapply(x, leaf_matrices), recursive = FALSE))
  list()
}

# A simulated network as a dense 0/1 matrix, whether returned as an
# n x n matrix or as an edge list of (sender, receiver, value) rows.
as_dense <- function(m, n) {
  if (nrow(m) == n && ncol(m) == n) return((m != 0) * 1)
  d <- matrix(0, n, n)
  if (nrow(m) > 0) {
    keep <- m[, 3] != 0
    d[cbind(m[keep, 1], m[keep, 2])] <- 1
  }
  d
}

simulate_stats <- function(spec, fx) {
  e <- spec$params
  n <- fx$n
  if (n < 3) stop("RSiena needs at least three actors")
  a0 <- adjacency(fx, simple = TRUE, loops = FALSE)
  arr <- array(c(a0, a0), dim = c(n, n, 2))
  net <- sienaNet(arr, allowOnly = FALSE)
  data <- sienaDataCreate(net)
  eff <- getEffects(data)
  short <- c(outdegree = "density", reciprocity = "recip")
  eff$initialValue[eff$shortName == "Rate" & eff$type == "rate"] <- e$rate
  eff$fix[eff$shortName == "Rate" & eff$type == "rate"] <- TRUE
  eff$include[eff$type == "eval" & eff$shortName %in% short] <- FALSE
  for (k in seq_along(e$effects)) {
    s <- short[[e$effects[[k]]]]
    eff$include[eff$shortName == s & eff$type == "eval"] <- TRUE
    eff$initialValue[eff$shortName == s & eff$type == "eval"] <- e$beta[[k]]
    eff$fix[eff$shortName == s & eff$type == "eval"] <- TRUE
  }
  algo <- sienaAlgorithmCreate(projname = NULL, useStdInits = FALSE, cond = FALSE,
                               nsub = 0, n3 = 2L * e$runs, simOnly = TRUE, seed = e$seed)
  ans <- siena07(algo, data = data, effects = eff, returnDeps = TRUE, batch = TRUE,
                 silent = TRUE, useCluster = FALSE)
  mats <- leaf_matrices(ans$sims)
  if (length(mats) != 2L * e$runs) stop(sprintf("expected %d simulated networks, got %d", 2L * e$runs, length(mats)))
  acc <- numeric(length(e$effects) + 1L)
  for (m in mats) {
    x <- as_dense(m, n)
    diag(x) <- 0
    for (k in seq_along(e$effects)) {
      acc[k] <- acc[k] + switch(e$effects[[k]],
        outdegree = sum(x), reciprocity = sum(x * t(x)),
        stop("effect not supported: ", e$effects[[k]]))
    }
    acc[length(acc)] <- acc[length(acc)] + sum(abs(x - a0))
  }
  acc / length(mats)
}

run_oracle("rsiena", paste("RSiena", as.character(utils::packageVersion("RSiena"))),
           function(variant, spec, fx) simulate_stats(spec, fx))
