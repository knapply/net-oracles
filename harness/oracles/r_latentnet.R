#!/usr/bin/env Rscript
# oracle-entries: latentnet
# Golden values from latentnet (`krivitsky2008fitting`), run as a black box:
# the Bernoulli-logit log-likelihood of the distance model of Hoff, Raftery
# and Handcock (`hoff2002latent`) at given positions and intercept, with its
# gradient, for the entries of manifest/latent_space.yaml that
# list a `latentnet` oracle.
#
#   Rscript oracles/r_latentnet.R
#
# Requires latentnet, network, and yaml; exits quietly without latentnet. The
# model object comes from a minimal fit (latentnet builds it with ergmm()); the
# fit's own estimates are replaced by the intercept and positions of
# derived/models.py before the log-likelihood (ergmm.lpY) and its
# gradient (ergmm.lpY.grad) are evaluated. A gradient that cannot be read is
# written as NA, which the comparison skips (`partial`).

if (!requireNamespace("latentnet", quietly = TRUE)) {
  cat("latentnet is not installed; no latentnet golden files written.\n")
  quit(status = 0)
}
suppressPackageStartupMessages({
  library(network)
  library(latentnet)
})

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

as_network <- function(fx) {
  nw <- network::network.initialize(fx$n, directed = fx$directed, loops = FALSE,
                                    multiple = FALSE)
  keep <- fx$from != fx$to
  a <- fx$from[keep] + 1L
  b <- fx$to[keep] + 1L
  if (!fx$directed) {
    lo <- pmin(a, b)
    b <- pmax(a, b)
    a <- lo
  }
  pairs <- unique(data.frame(a = a, b = b))
  if (nrow(pairs)) network::add.edges(nw, tail = pairs$a, head = pairs$b)
  nw
}


positions <- function(n, d) {
  i <- rep(seq_len(n) - 1, each = d)
  a <- rep(seq_len(d) - 1, times = n)
  matrix(1.5 * sin(0.73 * (d * i + a)) + 0.2 * ((d * i + a) %% 3), n, d, byrow = TRUE)
}

ns <- asNamespace("latentnet")

evaluate <- function(model, theta) {
  ll <- as.numeric(get("ergmm.lpY", ns)(model, theta, given = list(), up.to.const = FALSE))
  g <- tryCatch(get("ergmm.lpY.grad", ns)(model, theta, given = list()), error = function(e) NULL)
  n <- nrow(theta$Z)
  d <- ncol(theta$Z)
  ga <- NA_real_
  gz <- rep(NA_real_, n * d)
  if (is.list(g)) {
    if (!is.null(g$beta)) ga <- as.numeric(g$beta)[1]
    if (is.matrix(g$Z) && all(dim(g$Z) == c(n, d))) gz <- as.numeric(t(g$Z))
  }
  list(ll = ll, ga = ga, gz = gz)
}

compute <- function(variant, spec, fx) {
  e <- spec$params
  if (fx$n < 3) stop("latentnet needs at least three nodes")
  d <- as.integer(if (is.null(e$dim)) 2L else e$dim)
  alpha <- as.numeric(e$alpha)
  nw <- as_network(fx)
  fit <- ergmm(nw ~ euclidean(d = d), tofit = "mle",
               control = ergmm.control(burnin = 10, interval = 1, sample.size = 2, threads = 1))
  model <- fit$model
  theta <- fit$mle
  theta$beta <- alpha
  theta$Z <- positions(fx$n, d)
  r <- evaluate(model, theta)
  if (identical(e$fn, "latent_loglik")) return(c(r$ll, r$ga, r$gz))
  base <- c(0.3, -0.2, 0.1)
  theta$Z[1, ] <- base[(seq_len(d) - 1) %% 3 + 1]
  r2 <- evaluate(model, theta)
  c(r2$ll - r$ll, r2$gz)
}

run_oracle("latentnet", sprintf("latentnet %s", utils::packageVersion("latentnet")), compute)
