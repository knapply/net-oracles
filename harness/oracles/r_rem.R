#!/usr/bin/env Rscript
# Golden values from remstats and remstimate
# (`arena2026remstats`, `arena2026remstimate`) for relational
# event statistics and the ordinal relational event model (manifest/rem.yaml, variants
# with a `remstats` oracle).
#
#   Rscript oracles/r_rem.R
#
# Requires remify, remstats, remstimate, and yaml; exits quietly when they
# are not installed. Run from the repository root. The packages are run as
# black boxes through their documented interfaces.
#
# Every fixture is read as the event stream of derived/rem.py,
# whose rules are repeated here: self-loops dropped; edge e (0-based)
# occurs 1 + (7 e + 3) mod 3 times; occurrence j runs from the first to the
# second endpoint unless (5 e + 3 j) mod 4 = 3; occurrences are ordered by
# ((131 e + 71 j + 17) * 2654435761) mod 2^32, then (e, j); the k-th event
# happens at time k + 1. Actors are named "a0001", ... so that their
# sorted order is the node order, and the risk set is every ordered pair of
# distinct actors.
#
# Statistic variants write, per event, the statistic of the event's dyad
# and its sum and sum of squares over the risk set; fits write the
# coefficients, then NaN in place of the standard errors.

needed <- c("remify", "remstats", "remstimate", "yaml")
if (!all(vapply(needed, requireNamespace, logical(1), quietly = TRUE))) {
  cat("remstats/remstimate are not installed; no remstats golden files written (rem).\n")
  quit(status = 0)
}

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "rem.yaml"))
ORACLE <- "remstats"
UNDEFINED <- -999

write_rows <- function(fixture, variant, rows) {
  d <- file.path(golden_dir, ORACLE, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  fmt <- function(v) {
    v[is.na(v) & !is.nan(v)] <- UNDEFINED
    paste(formatC(v, digits = 17, format = "g"), collapse = " ")
  }
  lines <- if (is.list(rows)) vapply(rows, fmt, "") else vapply(rows, fmt, "")
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

# The event stream of derived/rem.py (0-based actors).
event_stream <- function(src, tgt) {
  occ <- list()
  for (e in seq_along(src) - 1L) {
    u <- src[e + 1L]; v <- tgt[e + 1L]
    if (u == v) next
    for (j in 0:((7 * e + 3) %% 3)) {
      # (131 e + 71 j + 17) * 2654435761 mod 2^32, exactly: split the
      # multiplier so every product stays below 2^53.
      a <- (131 * e + 71 * j + 17) %% 2^32
      key <- ((a * 40503) %% 2^32 * 65536 + a * 31153) %% 2^32
      rev <- (5 * e + 3 * j) %% 4 == 3
      occ[[length(occ) + 1L]] <- c(key, e, j, if (rev) c(v, u) else c(u, v))
    }
  }
  if (length(occ) == 0L) return(NULL)
  m <- do.call(rbind, occ)
  m <- m[order(m[, 1], m[, 2], m[, 3]), , drop = FALSE]
  data.frame(time = seq_len(nrow(m)), sender = m[, 4], receiver = m[, 5])
}

EFFECTS <- c(inertia = "inertia", reciprocity = "reciprocity",
             sender_out = "outdegreeSender", sender_in = "indegreeSender",
             receiver_out = "outdegreeReceiver", receiver_in = "indegreeReceiver",
             transitive = "otp", cyclic = "itp", shared_out = "osp", shared_in = "isp",
             recency_dyad = "recencyContinue", recency_sender_out = "recencySendSender",
             recency_sender_in = "recencyReceiveSender",
             recency_receiver_out = "recencySendReceiver",
             recency_receiver_in = "recencyReceiveReceiver")
CLOSURE <- c("transitive", "cyclic", "shared_out", "shared_in")

effect_term <- function(stat, triad) {
  f <- EFFECTS[[stat]]
  if (stat %in% CLOSURE && identical(triad, "binary")) paste0(f, "(unique = TRUE)")
  else paste0(f, "()")
}

# remstats statistics for `stats` on a fixture's stream; returns the array
# (events x dyads x statistics, in `stats` order) and the risk set.
compute_stats <- function(ev, n, spec, stats) {
  actors <- sprintf("a%04d", seq_len(n) - 1L)
  edgelist <- data.frame(time = ev$time, actor1 = actors[ev$sender + 1L],
                         actor2 = actors[ev$receiver + 1L])
  reh <- remify::remify(edgelist = edgelist, model = "tie", actors = actors,
                        directed = TRUE, ordinal = TRUE)
  triad <- if (is.null(spec$triad)) "min" else spec$triad
  form <- as.formula(paste("~", paste(vapply(stats, effect_term, "", triad = triad),
                                      collapse = " + ")))
  memory <- if (is.null(spec$memory)) "full" else spec$memory
  args <- list(reh = reh, tie_effects = form, memory = memory)
  if (memory != "full") args$memory_value <- spec$param
  out <- do.call(remstats::remstats, args)
  rs <- attr(out, "riskset")
  if (is.null(rs)) rs <- reh$riskset
  snd <- as.character(rs[[if ("sender" %in% names(rs)) "sender" else 1]])
  rcv <- as.character(rs[[if ("receiver" %in% names(rs)) "receiver" else 2]])
  names3 <- dimnames(out)[[3]]
  cols <- vapply(stats, function(s) {
    want <- EFFECTS[[s]]
    hit <- which(names3 == want | startsWith(names3, want))
    if (length(hit) != 1L) stop("no unique column for ", want, " in ", paste(names3, collapse = ","))
    hit
  }, 1L)
  list(arr = unclass(out)[, , cols, drop = FALSE], snd = snd, rcv = rcv, reh = reh,
       out = out, actors = actors)
}

# remstats' decayed statistics against the definition's (Brandes et al.
# 2009): remstats leaves out the factor ln 2 / T and evaluates the weights at
# the previous event's time, one time unit earlier. The statistics of the
# definition are therefore remstats' times c = (ln 2 / T) 2^(-1/T), for the
# count and smaller-of-two-counts statistics compared here.
decay_scale <- function(spec) {
  if (!identical(spec$memory, "decay")) return(1)
  log(2) / spec$param * 2^(-1 / spec$param)
}

run_statistic <- function(ev, n, spec) {
  r <- compute_stats(ev, n, spec, spec$stat)
  a <- matrix(r$arr[, , 1], ncol = dim(r$arr)[2])
  # remstats leaves out the first event, whose history is empty: its
  # statistics are zero by definition.
  if (nrow(a) == nrow(ev) - 1L) a <- rbind(0, a)
  key <- paste(r$snd, r$rcv)
  obs <- match(paste(r$actors[ev$sender + 1L], r$actors[ev$receiver + 1L]), key)
  cs <- decay_scale(spec)
  lapply(seq_len(nrow(ev)), function(k) {
    c(a[k, obs[k]] * cs, sum(a[k, ]) * cs, sum(a[k, ]^2) * cs^2)
  })
}

run_fit <- function(ev, n, spec) {
  stats <- unlist(spec$stats)
  r <- compute_stats(ev, n, spec, stats)
  fit <- remstimate::remstimate(reh = r$reh, stats = r$out, method = "MLE")
  cf <- coef(fit)
  idx <- vapply(stats, function(s) {
    want <- EFFECTS[[s]]
    hit <- which(names(cf) == want | startsWith(names(cf), want))
    if (length(hit) != 1L) stop("no unique coefficient for ", want)
    hit
  }, 1L)
  # remstimate's standard errors are not compared (written as NaN, skipped
  # by the `partial` comparison): they come from its optimizer's curvature
  # approximation and differ from the inverse information by up to a few
  # percent; the definition oracle checks the engine's.
  as.list(c(cf[idx] / decay_scale(spec), rep(NaN, length(idx))))
}

count <- 0L
failed <- 0L
for (name in sort(list.files(fixtures_dir))) {
  meta <- read_meta(file.path(fixtures_dir, name, "meta.json"))
  edges <- read.csv(file.path(fixtures_dir, name, "edges.csv"))
  ev <- event_stream(edges$from, edges$to)
  for (variant in names(manifest)) {
    spec <- manifest[[variant]]
    if (is.null(spec$oracles[[ORACLE]]) || !applies(spec, meta)) next
    eng <- spec$params
    rows <- tryCatch({
      if (is.null(ev)) {
        if (eng$fn == "rem_fit") as.list(rep(UNDEFINED, 2 * length(eng$stats))) else list()
      } else if (eng$fn == "rem_statistic") run_statistic(ev, meta$n, eng)
      else run_fit(ev, meta$n, eng)
    }, error = function(e) {
      message(sprintf("remstats: %s on %s: %s", variant, name, conditionMessage(e)))
      NULL
    })
    if (is.null(rows)) { failed <- failed + 1L; next }
    write_rows(name, variant, rows)
    count <- count + 1L
  }
}
d <- file.path(golden_dir, ORACLE)
dir.create(d, recursive = TRUE, showWarnings = FALSE)
writeLines(sprintf("remstats %s, remstimate %s, remify %s",
                   as.character(packageVersion("remstats")),
                   as.character(packageVersion("remstimate")),
                   as.character(packageVersion("remify"))), file.path(d, "VERSION"))
cat(sprintf("remstats (rem): wrote %d golden files, %d failed\n", count, failed))
