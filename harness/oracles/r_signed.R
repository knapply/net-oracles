#!/usr/bin/env Rscript
# oracle-entries: signnet
# Golden values from signnet (`schoch2023signnet`): positive-negative
# centrality, pn_index() (Everett and Borgatti 2014), run as a black box.
#
#   Rscript oracles/r_signed.R
#
# signnet is not in the runner image: it is installed for this run into a
# private library; without it the script exits quietly. The graph handed to
# signnet is the signed simple graph of manifest/signed.yaml
# (pair sign = sign of the summed edge signs, loops dropped), with the
# signs in E(g)$sign. Each call has a time limit of 300 seconds.

if (!requireNamespace("signnet", quietly = TRUE)) {
  lib <- file.path(tempdir(), "rlib")
  dir.create(lib, showWarnings = FALSE)
  tryCatch(utils::install.packages("signnet", lib = lib, repos = "https://cloud.r-project.org",
                                   quiet = TRUE),
           error = function(err) message("signnet: install failed: ", conditionMessage(err)),
           warning = function(w) message("signnet: install warning: ", conditionMessage(w)))
  .libPaths(c(lib, .libPaths()))
}
if (!requireNamespace("signnet", quietly = TRUE)) {
  cat("signnet is not installed; no signnet golden files written.\n")
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
  out[is.na(x)] <- "NaN"
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

# Node attributes and dyadic covariates from the node index, as the area
# manifests define them: num7 (7 v) % 11; dmat (i + 2 j) % 5, smat
# (i + j) % 4, adiff |num7_i - num7_j|, all with a zero diagonal.
num7 <- function(n) (7 * (seq_len(n) - 1)) %% 11
dyad_rule <- function(rule, n) {
  i <- matrix(seq_len(n) - 1, n, n)
  j <- t(i)
  m <- switch(rule, dmat = (i + 2 * j) %% 5, smat = (i + j) %% 4,
              adiff = abs(outer(num7(n), num7(n), "-")), stop("unknown dyad rule ", rule))
  diag(m) <- 0
  m
}

# A call under the per-fit time limit of 300 seconds.
FIT_LIMIT <- 300
limited <- function(expr) {
  setTimeLimit(elapsed = FIT_LIMIT, transient = TRUE)
  on.exit(setTimeLimit(elapsed = Inf))
  expr
}

# ---- end of shared plumbing ---------------------------------------------

sign_matrix <- function(fx, signs) {
  n <- fx$n
  m <- matrix(0, n, n)
  for (k in seq_along(fx$from)) {
    a <- fx$from[k]
    b <- fx$to[k]
    if (a == b) next
    s <- if (identical(signs, "rule")) (if ((a + b) %% 3 == 0) -1 else 1) else fx$weight[k]
    m[a + 1, b + 1] <- m[a + 1, b + 1] + s
    if (!fx$directed) m[b + 1, a + 1] <- m[b + 1, a + 1] + s
  }
  sign(m)
}

compute <- function(variant, spec, fx) {
  e <- spec$params
  if (e$fn != "pn_centrality" || fx$n < 2) return(NULL)
  s <- sign_matrix(fx, e$signs)
  g <- igraph::graph_from_adjacency_matrix(s, mode = if (fx$directed) "directed" else "undirected",
                                           weighted = "sign")
  mode <- if (fx$directed) e$mode else "all"
  as.numeric(limited(signnet::pn_index(g, mode = mode)))
}

run_oracle("signnet", sprintf("signnet %s", utils::packageVersion("signnet")), compute)
