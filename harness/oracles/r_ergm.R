#!/usr/bin/env Rscript
# oracle-entries: ergm
# Golden values from ergm (Handcock et al.; Krivitsky et al. 2023):
# summary() of ERGM terms on the observed network as exact counts for the
# descriptive measures, and, for the model entries (manifest/
# ergm.yaml), statistics, summed change statistics (ergmMPLE), MPLE and
# MCMC-MLE coefficients, and mean simulated statistics. ergm is run as a
# black box; its source is not read.
#
#   Rscript oracles/r_ergm.R
#
# A network object cannot hold parallel edges here (multiple = FALSE), so
# repeated pairs are entered once and loops dropped; the manifest records
# where that matters. Each value is the term itself or a ratio of terms,
# as the manifest's `call` says. Requires ergm, network, and yaml; exits
# quietly without ergm.

if (!requireNamespace("ergm", quietly = TRUE)) {
  cat("ergm is not installed; no ergm golden files written.\n")
  quit(status = 0)
}
suppressPackageStartupMessages({
  library(network)
  library(ergm)
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

stat <- function(nw, f) as.numeric(summary(f, basis = nw))

# A manifest term ("gwesp:0.5", "nodematch:mod3", "nodefactor:mod3:1", ...;
# bindings/ergm.py) as an ergm term. Consecutive nodefactor
# levels of one attribute become one nodefactor() term, which drops the
# first level as the manifest's engine terms do.
term_r <- function(t) {
  p <- strsplit(t, ":", fixed = TRUE)[[1]]
  gw <- function(name) sprintf("%s(%s, fixed = TRUE, cutoff = 100)", name, p[2])
  switch(p[1],
    edges = "edges", mutual = "mutual", isolates = "isolates", triangle = "triangle",
    ttriple = "ttriple", ctriple = "ctriple",
    kstar = sprintf("kstar(%s)", p[2]), istar = sprintf("istar(%s)", p[2]),
    ostar = sprintf("ostar(%s)", p[2]),
    gwdegree = gw("gwdegree"), gwidegree = gw("gwidegree"), gwodegree = gw("gwodegree"),
    gwesp = gw("gwesp"), gwdsp = gw("gwdsp"),
    nodematch = sprintf('nodematch("%s")', p[2]),
    nodefactor = sprintf('nodefactor("%s")', p[2]),
    nodecov = sprintf('nodecov("%s")', p[2]),
    stop("unknown term ", t))
}

model_formula <- function(nw, terms) {
  r <- vapply(unlist(terms), term_r, "")
  r <- r[!(duplicated(r) & startsWith(r, "nodefactor"))]
  f <- stats::as.formula(paste("nw ~", paste(r, collapse = " + ")))
  environment(f) <- list2env(list(nw = nw))
  f
}

with_rules <- function(nw, n) {
  network::set.vertex.attribute(nw, "mod3", node_rule("mod3", n))
  network::set.vertex.attribute(nw, "num7", node_rule("num7", n))
  nw
}

# Model fits and simulations: only on the fixtures the manifest lists for
# this oracle (they are slow and undefined elsewhere).
model_value <- function(spec, fx, nw) {
  e <- spec$params
  o <- spec$oracles$ergm
  if (!is.null(o$only_on) && !(fx$name %in% unlist(o$only_on))) return(NULL)
  if (fx$name %in% unlist(o$undefined_on)) return(NULL)
  nw <- with_rules(nw, fx$n)
  f <- model_formula(nw, e$terms)
  set.seed(1)
  switch(e$fn,
    ergm_statistics = stat(nw, f),
    ergm_change_sums = {
      m <- ergm::ergmMPLE(f, output = "matrix")
      as.numeric(colSums(m$predictor * m$weights))
    },
    ergm_mple = as.numeric(stats::coef(ergm::ergm(f, estimate = "MPLE"))),
    ergm_sim_mean = as.numeric(colMeans(stats::simulate(
      f, coef = unlist(e$coef), nsim = 4000, output = "stats", seed = 1,
      control = ergm::control.simulate.formula(MCMC.burnin = e$burnin,
                                               MCMC.interval = e$oracle_interval)))),
    ergm_mcmle = {
      ctl <- if (length(e$terms) > 1 && any(grepl("^gw", unlist(e$terms))))
        ergm::control.ergm(seed = 1, MCMC.samplesize = 4096) else ergm::control.ergm(seed = 1)
      as.numeric(stats::coef(ergm::ergm(f, control = ctl)))
    },
    NULL)
}

# ---- the term catalog (manifest entries with fn: oracle_only) ----------------
# Every ergm term page: its statistics and its summed change statistics on
# each fixture, one line per term of the entry's list (a term with several
# statistics gives several values on its line; a term ergm rejects on that
# fixture gives NaN). Attributes and covariate matrices are defined from the
# node index, as the manifest header says.

catalog_errors <- new.env()

read_types <- function(name) {
  txt <- paste(readLines(file.path(fixtures_dir, name, "meta.json")), collapse = " ")
  m <- regmatches(txt, regexpr('"type": *\\[[^]]*\\]', txt))
  if (!length(m)) return(NULL)
  as.integer(strsplit(gsub("[^0-9,]", "", sub('"type":', "", m)), ",")[[1]])
}

catalog_network <- function(fx, type) {
  n <- fx$n
  ord <- if (is.null(type)) seq_len(n) else c(which(type == 0), which(type == 1))
  pos <- integer(n)
  pos[ord] <- seq_len(n)
  n1 <- if (is.null(type)) 0L else sum(type == 0)
  nw <- if (is.null(type))
    network::network.initialize(n, directed = fx$directed, loops = FALSE, multiple = FALSE)
  else network::network.initialize(n, directed = FALSE, bipartite = n1, loops = FALSE,
                                   multiple = FALSE)
  keep <- fx$from != fx$to
  a <- pos[fx$from[keep] + 1L]
  b <- pos[fx$to[keep] + 1L]
  if (!fx$directed) {
    lo <- pmin(a, b)
    b <- pmax(a, b)
    a <- lo
  }
  pairs <- unique(data.frame(a = a, b = b))
  if (!is.null(type) && nrow(pairs) && any(pairs$a > n1 | pairs$b <= n1))
    stop("an edge inside one mode")
  if (nrow(pairs)) network::add.edges(nw, tail = pairs$a, head = pairs$b)
  for (r in c("mod2", "mod3", "blocks3", "num7", "num3", "id"))
    network::set.vertex.attribute(nw, r, node_rule(r, n)[ord])
  env <- new.env(parent = globalenv())
  env$nw <- nw
  i <- row(matrix(0, n, n)) - 1
  j <- col(matrix(0, n, n)) - 1
  clean <- function(m) { diag(m) <- 0; m }
  env$smat <- clean((i + j) %% 4)
  env$dmat <- clean((i + 2 * j) %% 5)
  env$amats <- (row(matrix(0, 3, 3)) + col(matrix(0, 3, 3)) - 2) %% 4
  env$amatd <- (row(matrix(0, 3, 3)) - 1 + 2 * (col(matrix(0, 3, 3)) - 1)) %% 5
  env$sbin <- clean(((i + j) %% 3 == 0) * 1)
  env$dbin <- clean(((i + 2 * j) %% 3 == 0) * 1)
  if (!is.null(type)) {
    i <- row(matrix(0, n1, n - n1)) - 1
    j <- col(matrix(0, n1, n - n1)) - 1
    env$bmat <- (i + 2 * j) %% 5
  }
  env
}

catalog_value <- function(variant, spec, fx) {
  e <- spec$params
  o <- spec$oracles$ergm
  if (is.null(e$terms)) return(NULL)
  if (!is.null(o$only_on) && !(fx$name %in% unlist(o$only_on))) return(NULL)
  bip <- identical(e$mode, "bipartite")
  env <- catalog_network(fx, if (bip) read_types(fx$name) else NULL)
  t0 <- Sys.time()
  on.exit(message(sprintf("  %s on %s: %.1f s", variant, fx$name,
                          as.numeric(Sys.time() - t0, units = "secs"))))
  lapply(unlist(e$terms), function(term) {
    t1 <- Sys.time()
    on.exit({
      d <- as.numeric(Sys.time() - t1, units = "secs")
      if (d > 3) message(sprintf("  slow: %s on %s: %s %.0f s", variant, fx$name, term, d))
    })
    tryCatch({
      # A term that takes more than 20 s on one fixture counts as rejected.
      setTimeLimit(elapsed = 20, transient = TRUE)
      f <- stats::as.formula(paste("nw ~", term), env = env)
      if (identical(e$kind, "change_sums")) {
        # No dyads (one node): the sum over the empty set is zero (ergmMPLE
        # does not return on such a network).
        if (network::network.size(env$nw) < 2)
          return(numeric(length(as.numeric(summary(f)))))
        m <- ergm::ergmMPLE(f, output = "matrix")
        as.numeric(colSums(m$predictor * m$weights))
      } else as.numeric(summary(f))
    }, error = function(err) {
      key <- paste(variant, term, sep = " | ")
      old <- catalog_errors[[key]]
      catalog_errors[[key]] <- list(n = (if (is.null(old)) 0L else old$n) + 1L,
        first = if (is.null(old)) paste0(fx$name, ": ", substr(conditionMessage(err), 1, 90))
                else old$first)
      NaN
    })
  })
}

compute <- function(variant, spec, fx) {
  e <- spec$params
  n <- fx$n
  if (e$fn == "oracle_only") return(catalog_value(variant, spec, fx))
  if (n < 1) return(NULL)
  nw <- as_network(fx)
  if (startsWith(e$fn, "ergm_")) return(model_value(spec, fx, nw))
  switch(e$fn,
    triad_census = if (fx$directed && n >= 3) stat(nw, nw ~ triadcensus(0:15)),
    density = if (!isTRUE(e$loops) && n >= 2) {
      pairs <- if (fx$directed) n * (n - 1) else n * (n - 1) / 2
      stat(nw, nw ~ edges) / pairs
    },
    reciprocity = if (fx$directed && identical(e$mode, "default")) {
      m <- stat(nw, nw ~ edges)
      if (m > 0) 2 * stat(nw, nw ~ mutual) / m
    },
    transitivity = if (!fx$directed) {
      k2 <- stat(nw, nw ~ kstar(2))
      if (k2 > 0) 3 * stat(nw, nw ~ triangle) / k2 else
        if (identical(e$undefined, "zero")) 0
    },
    # Counted only up to max_nodes nodes; beyond that the measure is the
    # marker -1, as for every oracle (cycle enumeration is exponential).
    gb_cycle_count = if (n > e$max_nodes) -1 else if (n < 2) 0 else {
      ks <- if (fx$directed) 2:n else if (n >= 3) 3:n else integer()
      if (length(ks)) sum(stat(nw, nw ~ cycle(ks))) else 0
    },
    NULL)
}

# ERGM_ENTRY_FILTER (a regular expression) restricts a run to the matching
# manifest entries, for trying a new entry without the model fits.
keep <- Sys.getenv("ERGM_ENTRY_FILTER")
if (nzchar(keep)) manifest <- manifest[grepl(keep, names(manifest))]

run_oracle("ergm", sprintf("ergm %s (summary statistics; network %s)",
                           utils::packageVersion("ergm"), utils::packageVersion("network")),
           compute)

errs <- sort(ls(catalog_errors))
if (length(errs)) {
  cat(sprintf("catalog: %d (entry | term) pairs failed on some fixture\n", length(errs)))
  for (k in errs) cat(sprintf("  %s  x%d  %s\n", k, catalog_errors[[k]]$n, catalog_errors[[k]]$first))
}
