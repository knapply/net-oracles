#!/usr/bin/env Rscript
# Golden values from sna (Butts 2008) for flow betweenness (Freeman,
# Borgatti, and White 1991), and from keyplayer (An and Liu 2016) for the
# fragmentation centrality of single nodes (Borgatti 2006)
# (manifest/resilience.yaml).
#
#   Rscript oracles/r_resilience.R
#
# Requires the sna and yaml packages; keyplayer is used when installed.
# Run from the repository root. Undefined values (NaN or NA) are written as
# -1, as the engine runner does.

suppressPackageStartupMessages(library(sna))
has_keyplayer <- requireNamespace("keyplayer", quietly = TRUE)

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "resilience.yaml"))

write_values <- function(oracle, fixture, variant, values) {
  values <- as.numeric(values)
  values[is.na(values)] <- -1
  d <- file.path(golden_dir, oracle, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  writeLines(c("value", formatC(values, digits = 17, format = "g")),
             file.path(d, paste0(variant, ".csv")))
}

applies <- function(spec, meta) {
  kind <- if (is.null(spec$applies_to)) "any" else spec$applies_to
  if (kind == "directed" && !meta$directed) return(FALSE)
  if (kind == "undirected" && meta$directed) return(FALSE)
  if (isTRUE(spec$requires_weights) && !meta$weighted) return(FALSE)
  TRUE
}

# Whether the manifest declares the oracle undefined on this fixture.
undefined <- function(ospec, name, meta) {
  tags <- c(meta$tags, if (meta$directed) "directed" else "undirected")
  name %in% unlist(ospec$undefined_on) || any(tags %in% unlist(ospec$undefined_when))
}

read_meta <- function(path) {
  txt <- paste(readLines(path), collapse = "")
  get <- function(key) sub(sprintf('.*"%s": *([^,}]+).*', key), "\\1", txt)
  tags <- sub('.*"tags": *\\[([^]]*)\\].*', "\\1", txt)
  tags <- gsub('[" ]', "", strsplit(tags, ",")[[1]])
  list(n = as.integer(get("n")),
       directed = get("directed") == "true",
       weighted = get("weighted") == "true",
       tags = tags[nzchar(tags)])
}

sna_values <- function(variant, m, mw, meta) {
  gmode <- if (meta$directed) "digraph" else "graph"
  switch(variant,
    flow_betweenness = sna::flowbet(m, gmode = gmode, cmode = "rawflow", ignore.eval = TRUE),
    flow_betweenness_normalized = sna::flowbet(m, gmode = gmode, cmode = "normflow",
                                               ignore.eval = TRUE),
    flow_betweenness_fractional = sna::flowbet(m, gmode = gmode, cmode = "fracflow",
                                               ignore.eval = TRUE),
    flow_betweenness_capacity = sna::flowbet(mw, gmode = gmode, cmode = "rawflow",
                                             ignore.eval = FALSE),
    NULL
  )
}

# Borgatti's distance-weighted reach DR(S) = (|S| + sum_{j not in S} 1/d(S, j)) / n
# from keyplayer's M-reach closeness, which divides the sum by n - |S|.
reach_from_keyplayer <- function(score, size, n) (size + (n - size) * score) / n

# The best score over every set of k nodes (the tool's measure of each set).
best_set <- function(n, k, score) {
  if (n < k) return(NULL)
  best <- -Inf
  sets <- matrix(utils::combn(n, k), nrow = k)
  for (j in seq_len(ncol(sets))) {
    s <- score(sets[, j])
    if (is.finite(s) && s > best) best <- s
  }
  best
}

# One node at a time: a vector of nodes would score them as one set.
keyplayer_values <- function(variant, spec, m, mw) {
  e <- spec$params
  n <- nrow(m)
  each <- function(f) vapply(seq_len(n), f, numeric(1))
  switch(variant,
    kpp_distance_fragmentation_single =
      each(function(v) keyplayer::fragment(m, v, binary = TRUE)),
    kpp_distance_fragmentation_single_weighted =
      each(function(v) keyplayer::fragment(mw, v, binary = FALSE)),
    kpp_distance_reach_single =
      each(function(v) reach_from_keyplayer(
        keyplayer::mreach.closeness(m, v, M = Inf, binary = TRUE, cmode = "outdegree"), 1, n)),
    kpp_distance_reach_single_in =
      each(function(v) reach_from_keyplayer(
        keyplayer::mreach.closeness(m, v, M = Inf, binary = TRUE, cmode = "indegree"), 1, n)),
    kpp_distance_reach_single_weighted =
      each(function(v) reach_from_keyplayer(
        keyplayer::mreach.closeness(mw, v, M = Inf, binary = FALSE, cmode = "outdegree"), 1, n)),
    kpp_m_reach_single =
      each(function(v) keyplayer::mreach.degree(m, v, M = e$m, binary = TRUE,
                                                cmode = "outdegree")),
    kpp_distance_fragmentation_optimum_k2 =
      best_set(n, e$k, function(s) keyplayer::fragment(m, s, binary = TRUE)),
    kpp_distance_reach_optimum_k2 =
      best_set(n, e$k, function(s) reach_from_keyplayer(
        keyplayer::kpcent(m, s, type = "mreach.closeness", M = Inf, method = "min",
                          binary = TRUE, cmode = "outdegree"), length(s), n)),
    kpp_m_reach_optimum_k3 =
      best_set(n, e$k, function(s) keyplayer::kpcent(
        m, s, type = "mreach.degree", M = e$m, method = "min", binary = TRUE,
        cmode = "outdegree")),
    NULL
  )
}

counts <- c(sna = 0L, keyplayer = 0L)
for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  e <- utils::read.csv(file.path(d, "edges.csv"))
  e <- e[e$from != e$to, , drop = FALSE]
  m <- matrix(0, meta$n, meta$n)
  mw <- m
  if (nrow(e)) {
    m[cbind(e$from + 1L, e$to + 1L)] <- 1
    if (!meta$directed) m[cbind(e$to + 1L, e$from + 1L)] <- 1
    if (meta$weighted) {
      mw[cbind(e$from + 1L, e$to + 1L)] <- e$weight
      if (!meta$directed) mw[cbind(e$to + 1L, e$from + 1L)] <- e$weight
    }
  }

  for (variant in names(manifest)) {
    spec <- manifest[[variant]]
    if (!applies(spec, meta)) next
    ospec <- spec$oracles$sna
    if (!is.null(ospec) && !undefined(ospec, name, meta)) {
      v <- sna_values(variant, m, mw, meta)
      if (!is.null(v)) {
        write_values("sna", name, variant, v)
        counts[["sna"]] <- counts[["sna"]] + 1L
      }
    }
    ospec <- spec$oracles$keyplayer
    if (has_keyplayer && !is.null(ospec) && !undefined(ospec, name, meta)) {
      v <- tryCatch(keyplayer_values(variant, spec, m, mw), error = function(err) {
        message(sprintf("keyplayer %s on %s: %s", variant, name, conditionMessage(err)))
        NULL
      })
      if (!is.null(v)) {
        write_values("keyplayer", name, variant, v)
        counts[["keyplayer"]] <- counts[["keyplayer"]] + 1L
      }
    }
  }
}

writeLines(sprintf("sna %s", utils::packageVersion("sna")),
           file.path(golden_dir, "sna", "VERSION"))
if (has_keyplayer) {
  writeLines(sprintf("keyplayer %s", utils::packageVersion("keyplayer")),
             file.path(golden_dir, "keyplayer", "VERSION"))
} else {
  cat("keyplayer is not installed; its golden files were not written.\n")
}
cat(sprintf("Wrote %d sna and %d keyplayer golden files (resilience).\n",
            counts[["sna"]], counts[["keyplayer"]]))
