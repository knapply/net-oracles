# Shared helpers for R adapters (the counterpart of bench/common.py).
#
# An adapter is one .R file that sources this file and ends with
#   bench_main(tool = "...", version = function() ..., load = function(ctx) ..., calls = list(id = function(G, ctx) digest))
# Command line: Rscript bench/adapters/<tool>.R --measure ID --graph PATH --threads T --reps R
# (also --list, --prepare, --budget S as in common.py). One JSON line on standard output.

.args <- commandArgs(trailingOnly = TRUE)
.opt <- function(name, default = NULL) {
  i <- match(name, .args)
  if (is.na(i) || i == length(.args)) default else .args[i + 1]
}

.status_kb <- function(key) {
  l <- tryCatch(grep(paste0("^", key), readLines("/proc/self/status"), value = TRUE), error = function(e) character())
  if (!length(l)) return(NA_real_)
  as.numeric(strsplit(trimws(sub(key, "", l[1])), " +")[[1]][1])
}
rss_mb <- function() .status_kb("VmRSS:") / 1024
peak_mb <- function() .status_kb("VmHWM:") / 1024
reset_peak <- function() try(cat("5", file = "/proc/self/clear_refs"), silent = TRUE)

# Digest helpers: numbers rounded to 6 significant digits.
sig <- function(x) signif(as.numeric(x), 6)
vec <- function(x) { x <- x[is.finite(x)]; list(sum = sig(sum(x)), max = if (length(x)) sig(max(x)) else 0) }

read_edges <- function(path) {
  con <- file(path, "rb"); on.exit(close(con))
  head <- readBin(con, "raw", 24)
  if (!identical(rawToChar(head[1:8]), "NETEDGE1")) stop("not an edge file: ", path)
  u64 <- function(b) sum(as.numeric(b) * 256^(0:7))
  n <- u64(head[9:16]); directed <- u64(head[17:24]) != 0
  m <- (file.info(path)$size - 24) / 8
  e <- readBin(con, "integer", n = 2 * m, size = 4, endian = "little")
  list(n = n, directed = directed, edges = e, m = m)  # edges: flat u,v,u,v,... (0-based)
}

.json <- function(x) {
  if (is.null(x)) return("null")
  if (is.list(x)) {
    if (!length(x)) return("{}")
    if (is.null(names(x))) return(paste0("[", paste(vapply(x, .json, ""), collapse = ","), "]"))
    return(paste0("{", paste(sprintf('"%s":%s', names(x), vapply(x, .json, "")), collapse = ","), "}"))
  }
  if (is.character(x)) {
    x <- gsub("\\\\", "\\\\\\\\", x); x <- gsub('"', '\\\\"', x); x <- gsub("[\r\n\t]", " ", x)
    if (length(x) == 1) return(paste0('"', x, '"'))
    return(paste0("[", paste0('"', x, '"', collapse = ","), "]"))
  }
  if (is.logical(x)) x <- ifelse(x, "true", "false") else x <- ifelse(is.finite(x), format(x, digits = 15, scientific = FALSE, trim = TRUE), "null")
  if (length(x) == 1) x else paste0("[", paste(x, collapse = ","), "]")
}

bench_main <- function(tool, version, load, calls, threads = function(t) 1L, note = "", prepare = function(path) NULL) {
  measure <- .opt("--measure"); graph <- .opt("--graph")
  reps <- as.integer(.opt("--reps", "3")); budget <- as.numeric(.opt("--budget", "0"))
  req <- as.integer(.opt("--threads", "0"))
  if ("--list" %in% .args) { cat(.json(as.list(sort(c("load", names(calls))))), "\n", sep = ""); return(invisible()) }
  if ("--prepare" %in% .args) { prepare(graph); return(invisible()) }
  row <- list(tool = tool, tool_version = "", measure = measure, graph = basename(graph), threads = req,
              seconds = list(), peak_megabytes = NULL, status = "ok", digest = list(), note = "")
  emit <- function(row) cat(.json(row), "\n", sep = "")
  if (measure != "load" && !(measure %in% names(calls))) { row$status <- "unsupported"; return(emit(row)) }
  res <- tryCatch({
    row$tool_version <- as.character(version()); row$threads <- threads(req)
    invisible(gc()); base <- rss_mb(); row$base_megabytes <- round(base, 1)
    d <- read_edges(graph)
    src <- if (file.exists(paste0(graph, ".sources"))) as.integer(scan(paste0(graph, ".sources"), quiet = TRUE)) else integer()
    ctx <- list(n = d$n, directed = d$directed, edges = d$edges, sources = src, threads = row$threads, graph = graph)
    row$nodes <- d$n; row$edges <- d$m
    times <- numeric(); digest <- list()
    if (measure == "load") {
      reset_peak()
      for (r in seq_len(reps)) {
        t <- proc.time()[["elapsed"]]; G <- load(ctx); invisible(gc())
        times <- c(times, proc.time()[["elapsed"]] - t)
        if (r == 1) { row$peak_megabytes <- round(max(peak_mb() - base, 0), 1); row$graph_megabytes <- round(max(rss_mb() - base, 0), 1) }
        if (budget > 0 && sum(times) > budget / 2) break
        if (r < reps) { rm(G); invisible(gc()) }
      }
    } else {
      G <- load(ctx); ctx$edges <- NULL; rm(d); invisible(gc()); reset_peak()
      for (r in seq_len(reps)) {
        t <- proc.time()[["elapsed"]]; digest <- calls[[measure]](G, ctx)
        times <- c(times, proc.time()[["elapsed"]] - t)
        if (budget > 0 && sum(times) > budget / 2) break
      }
      row$peak_megabytes <- round(max(peak_mb() - base, 0), 1)
    }
    row$seconds <- as.list(round(times, 6)); row$digest <- digest; row$note <- note
    row
  }, error = function(e) {
    msg <- conditionMessage(e)
    row$status <- if (grepl("^unsupported", msg)) "unsupported" else "error"
    row$note <- substr(msg, 1, 200); row
  })
  emit(res)
}

# The model of a statistical task: PATH.model, one "key<TAB>value" line per setting (written by the
# runner from measures.yaml); lists are joined by ";". Returns a named character vector.
read_model <- function(graph) {
  l <- readLines(paste0(graph, ".model"), warn = FALSE)
  l <- l[nzchar(l)]
  kv <- strsplit(l, "\t", fixed = TRUE)
  structure(vapply(kv, function(x) x[2], ""), names = vapply(kv, function(x) x[1], ""))
}
mnum <- function(m, key, default = NA_real_) if (key %in% names(m)) as.numeric(m[[key]]) else default
mterms <- function(m) strsplit(m[["terms"]], ";", fixed = TRUE)[[1]]
# Formula terms of the model: the shared names ("gwesp(0.5)") become the package's ("gwesp(0.5, fixed = TRUE)").
mformula <- function(m, lhs = "nw") {
  t <- sub("^gwesp\\(([^)]*)\\)$", "gwesp(\\1, fixed = TRUE)", mterms(m))
  t <- sub("^nodematch\\((\\w+)\\)$", "nodematch('\\1')", t)
  as.formula(paste(lhs, "~", paste(t, collapse = " + ")), env = parent.frame())
}
# Standard-error digest of a fit, as the runner compares it: coef and se in the order of the terms.
fit_digest <- function(coef, se, ...) c(list(coef = as.numeric(coef), se = as.numeric(se)), list(...))
# Tables of a model graph: from PATH.raw (data/export_statnet.R) when the graph is a dataset, else the
# edge file (one wave, no attributes). Returns list(n, directed, waves, edges = data.frame(wave, from, to), nodes).
load_tables <- function(ctx) {
  raw <- paste0(ctx$graph, ".raw")
  if (dir.exists(raw)) {
    meta <- read.delim(file.path(raw, "meta.tsv"))
    list(n = meta$n, directed = meta$directed != 0, waves = meta$waves,
         edges = read.delim(file.path(raw, "edges.tsv")), nodes = read.delim(file.path(raw, "nodes.tsv"), check.names = FALSE))
  } else {
    e <- matrix(ctx$edges + 1L, ncol = 2, byrow = TRUE)
    list(n = ctx$n, directed = ctx$directed, waves = 1L, edges = data.frame(wave = 1L, from = e[, 1], to = e[, 2]), nodes = data.frame())
  }
}
# One wave as a `network` object (vertex attributes from the node table).
make_network <- function(tb, wave = 1L) {
  e <- tb$edges[tb$edges$wave == wave, c("from", "to")]
  nw <- network::network.initialize(tb$n, directed = tb$directed, loops = FALSE)
  nw <- network::add.edges(nw, as.integer(e$from), as.integer(e$to))
  for (a in names(tb$nodes)) network::set.vertex.attribute(nw, a, tb$nodes[[a]])
  nw
}
# Raise from a call to mark the measure as not available in the tool.
unsupported <- function(why = "") stop("unsupported: ", why, call. = FALSE)
