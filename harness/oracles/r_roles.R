#!/usr/bin/env Rscript
# Golden values from igraph (Csardi and Nepusz 2006), sna (Butts 2008), and
# base R's stats::cmdscale() for reach, edge betweenness, eigenvector
# centralization, information centrality, regular equivalence, blockmodel
# densities, and classical scaling (manifest/roles.yaml).
#
#   Rscript oracles/r_roles.R
#
# Requires the igraph, sna, and yaml packages (the geospatial variants also
# the s2 and sf packages, and are left out without them). Run from the
# repository root.
#
# Golden-file conventions (see bindings/roles.py): an undefined
# value is an empty line, block densities are written one block row per
# line, classical scaling writes one point per line, and partitions are
# written as class numbers (compared up to relabelling). The fixtures carry
# no partitions, so block and seed partitions put node v (0-based) in class
# v %% 3 (`mod3`) or v %% 2 (`mod2`), as every oracle does. Classical
# scaling runs on hop distances of the undirected simple reading of the
# network with unreachable pairs set to the longest finite distance plus 1,
# as in the bindings; its coordinates are written with each dimension's
# sign fixed so that the first coordinate larger than 1e-8 times the
# dimension's largest magnitude is positive (the engine's rule), and only
# dimensions whose eigenvalue exceeds 1e-12 times the largest are kept.

suppressPackageStartupMessages({
  library(igraph)
  library(sna)
})

root <- normalizePath(".")
fixtures_dir <- Sys.getenv("NETORACLES_FIXTURES_DIR", file.path(root, "fixtures"))
golden_dir <- Sys.getenv("NETORACLES_GOLDEN_DIR", file.path(root, "golden"))
manifest <- yaml::read_yaml(file.path(root, "manifest", "roles.yaml"))

fmt <- function(x) formatC(as.numeric(x), digits = 17, format = "g")

# `values` is a numeric vector (one value per line, NaN or NA as an empty
# line) or a matrix (one row per line).
write_values <- function(oracle, fixture, variant, values) {
  d <- file.path(golden_dir, oracle, fixture)
  dir.create(d, recursive = TRUE, showWarnings = FALSE)
  lines <- if (is.matrix(values)) {
    if (nrow(values)) apply(values, 1, function(r) paste(fmt(r), collapse = " ")) else character(0)
  } else {
    values <- as.numeric(values)
    ifelse(is.na(values), "", fmt(values))
  }
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

partition_for <- function(rule, n) {
  v <- seq_len(n) - 1L
  switch(rule, mod3 = v %% 3L, mod2 = v %% 2L, stop("unknown partition rule ", rule))
}

# Classes (numbered in order of first node) of the nodes at distance 0 in
# a CATREGE distance matrix.
zero_classes <- function(d) {
  d <- as.matrix(d)
  keys <- apply(d == 0, 1, function(r) paste(as.integer(r), collapse = ""))
  match(keys, unique(keys)) - 1L
}

# Hop distances of the undirected simple reading, unreachable pairs filled
# with the longest finite distance plus 1 (1 when no pair is connected).
mds_input <- function(g) {
  u <- igraph::simplify(igraph::as_undirected(g, mode = "collapse"))
  d <- igraph::distances(u, weights = NA)
  finite <- d[is.finite(d)]
  fill <- if (length(finite)) max(finite) + 1 else 1
  d[!is.finite(d)] <- fill
  unname(d)
}

fix_signs <- function(points) {
  for (j in seq_len(ncol(points))) {
    v <- points[, j]
    big <- max(abs(v))
    first <- v[which(abs(v) > 1e-8 * big)[1]]
    if (!is.na(first) && first < 0) points[, j] <- -v
  }
  points
}

igraph_values <- function(variant, spec, g, meta) {
  e <- spec$params
  w <- if (meta$weighted) igraph::E(g)$weight else NULL
  quiet <- function(expr) suppressWarnings(expr)
  switch(e$fn,
    reach = {
      order <- if (identical(e$k, "inf")) igraph::vcount(g) else as.integer(e$k)
      mode <- if (is.null(e$mode)) "out" else e$mode
      size <- igraph::ego_size(g, order = order, mode = mode) - 1
      if (isTRUE(e$normalized)) {
        n <- igraph::vcount(g)
        size <- if (n < 2) rep(NA_real_, n) else size / (n - 1)
      }
      size
    },
    edge_betweenness = {
      weights <- if (isTRUE(e$weighted)) {
        if (identical(e$weights_as, "strength")) 1 / w else w
      } else {
        NA
      }
      igraph::edge_betweenness(g, directed = TRUE, weights = weights)
    },
    centralization_eigenvector = quiet(
      igraph::centr_eigen(g, directed = FALSE, scale = TRUE, normalized = TRUE)$centralization),
    NULL
  )
}

# `binary` is the 0/1 adjacency matrix (parallel edges collapsed, loops on
# the diagonal); `valued` holds total edge weights.
sna_values <- function(variant, spec, binary, valued, meta) {
  e <- spec$params
  gmode <- if (meta$directed) "digraph" else "graph"
  switch(e$fn,
    information_centrality = {
      m <- if (isTRUE(e$weighted)) valued else binary
      sna::infocent(m, gmode = gmode, cmode = "weak", diag = FALSE)
    },
    regular_equivalence = {
      if (isTRUE(e$weighted)) return(NULL)
      seed <- if (is.null(e$seed)) NULL else partition_for(e$seed, meta$n) + 1L
      d <- sna::redist(binary, mode = gmode, method = "catrege", diag = FALSE,
                       seed.partition = seed)
      zero_classes(d)
    },
    block_density = {
      if (isTRUE(e$loops)) return(NULL)
      m <- if (isTRUE(e$weighted)) valued else binary
      classes <- partition_for(e$partition, meta$n) + 1L
      bm <- sna::blockmodel(m, classes, block.content = "density", mode = gmode, diag = FALSE)
      out <- unname(as.matrix(bm$block.model))
      out[is.na(out)] <- -1
      out
    },
    NULL
  )
}

stats_values <- function(variant, spec, g, meta) {
  e <- spec$params
  if (e$fn != "classical_mds") return(NULL)
  k <- as.integer(e$k)
  n <- meta$n
  if (n <= k) return(matrix(numeric(0), 0, 0))
  d <- mds_input(g)
  fit <- suppressWarnings(stats::cmdscale(d, k = k, eig = TRUE))
  switch(e$output,
    stress = {
      pts <- as.matrix(fit$points)
      keep <- which(fit$eig[seq_len(ncol(pts))] > 1e-12 * abs(fit$eig[1]))
      pts <- pts[, keep, drop = FALSE]
      dist_in <- stats::as.dist(d)
      dist_out <- stats::dist(pts)
      den <- sum(dist_out^2)
      if (den > 0) sqrt(sum((dist_out - dist_in)^2) / den) else NA_real_
    },
    points = {
      pts <- as.matrix(fit$points)
      floor <- 1e-12 * abs(fit$eig[1])
      keep <- which(fit$eig[seq_len(ncol(pts))] > floor)
      fix_signs(pts[, keep, drop = FALSE])
    },
    eigenvalues = fit$eig,
    gof = fit$GOF,
    NULL
  )
}


# ---- Geospatial variants (s2 for longitude and latitude, sf for planar) -----
#
# Node coordinates follow bindings/roles.py (`coordinates`): a
# multiplicative hash of the node index in exact integer arithmetic, which is
# reproduced here with 16-bit pieces so that doubles stay exact.
EARTH_RADIUS_M <- 6371008.7714

xor32 <- function(a, b) {
  bitwXor(as.integer(a %/% 65536), as.integer(b %/% 65536)) * 65536 +
    bitwXor(as.integer(a %% 65536), as.integer(b %% 65536))
}

mul32 <- function(a, b) {
  (a * (b %% 65536) + ((a * (b %/% 65536)) %% 65536) * 65536) %% 4294967296
}

hash_unit <- function(v, salt) {
  h <- ((v + 1) * 2654435761 + salt * 40503 + 12345) %% 4294967296
  h <- mul32(xor32(h, h %/% 8192), 1274126177)
  h / 4294967296
}

coordinates <- function(crs, n) {
  v <- seq_len(n) - 1
  u <- hash_unit(v, 1)
  w <- hash_unit(v, 2)
  if (crs == "lonlat") {
    list(x = 360 * u - 180, y = asin(2 * w - 1) * 180 / pi)
  } else {
    list(x = 100 * u, y = 100 * w)
  }
}

# Distances between the points of index vectors i and j (parallel), by s2
# on a sphere of the engine's radius or by GEOS through sf.
geo_distance <- function(crs, pts, i, j) {
  if (crs == "lonlat") {
    s2::s2_distance(pts$geog[i], pts$geog[j], radius = EARTH_RADIUS_M)
  } else {
    as.numeric(sf::st_distance(pts$geom[i], pts$geom[j], by_element = TRUE))
  }
}

geo_points <- function(crs, xy) {
  if (crs == "lonlat") {
    list(geog = s2::s2_geog_point(xy$x, xy$y))
  } else {
    list(geom = sf::st_geometry(sf::st_as_sf(data.frame(x = xy$x, y = xy$y),
                                             coords = c("x", "y"), crs = NA)))
  }
}

geo_matrix <- function(crs, pts, n) {
  if (crs == "lonlat") {
    s2::s2_distance_matrix(pts$geog, pts$geog, radius = EARTH_RADIUS_M)
  } else {
    unclass(sf::st_distance(pts$geom, pts$geom))
  }
}

geo_values <- function(variant, spec, e_df, meta) {
  e <- spec$params
  crs <- e$crs
  n <- meta$n
  if (n == 0) return(NULL)
  xy <- coordinates(crs, n)
  pts <- geo_points(crs, xy)
  switch(e$fn,
    edge_lengths = {
      if (!nrow(e_df)) return(numeric(0))
      geo_distance(crs, pts, e_df$from + 1L, e_df$to + 1L)
    },
    proximity = {
      d <- geo_matrix(crs, pts, n)
      rows <- list()
      if (!is.null(e$k) && e$k > 0) {
        for (i in seq_len(n)) {
          others <- setdiff(seq_len(n), i)
          nearest <- others[order(d[i, others], others)]
          nearest <- head(nearest, e$k)
          for (j in nearest) rows[[length(rows) + 1L]] <- c(i - 1, j - 1, d[i, j])
        }
      } else {
        within <- if (crs == "lonlat") {
          s2::s2_dwithin_matrix(pts$geog, pts$geog, as.numeric(e$r), radius = EARTH_RADIUS_M)
        } else {
          sf::st_is_within_distance(pts$geom, pts$geom, dist = as.numeric(e$r))
        }
        for (i in seq_len(n)) for (j in sort(within[[i]])) {
          if (j > i) rows[[length(rows) + 1L]] <- c(i - 1, j - 1, d[i, j])
        }
      }
      if (length(rows)) do.call(rbind, rows) else matrix(numeric(0), 0, 3)
    },
    group_geometry = {
      labels <- partition_for(e$partition, n)
      out <- list()
      for (g in unique(labels)) {
        mem <- which(labels == g)
        if (crs == "lonlat") {
          centre <- s2::s2_centroid_agg(pts$geog[mem])
          cx <- s2::s2_x(centre)
          cy <- s2::s2_y(centre)
          ds <- s2::s2_distance(pts$geog[mem], centre, radius = EARTH_RADIUS_M)
        } else {
          centre <- sf::st_centroid(sf::st_union(pts$geom[mem]))
          cx <- sf::st_coordinates(centre)[1, 1]
          cy <- sf::st_coordinates(centre)[1, 2]
          ds <- as.numeric(sf::st_distance(pts$geom[mem], centre))
        }
        out[[length(out) + 1L]] <- c(length(mem), cx, cy, mean(ds), sqrt(mean(ds^2)))
      }
      do.call(rbind, out)
    },
    NULL
  )
}

has_geo <- requireNamespace("s2", quietly = TRUE) && requireNamespace("sf", quietly = TRUE)
if (has_geo) suppressPackageStartupMessages({ library(s2); library(sf) })

counts <- c(igraph = 0L, sna = 0L, stats = 0L, s2 = 0L, sf = 0L)
for (name in sort(list.dirs(fixtures_dir, full.names = FALSE, recursive = FALSE))) {
  d <- file.path(fixtures_dir, name)
  meta <- read_meta(file.path(d, "meta.json"))
  e <- utils::read.csv(file.path(d, "edges.csv"))
  n <- meta$n
  g <- igraph::make_empty_graph(n = n, directed = meta$directed)
  if (nrow(e)) {
    g <- igraph::add_edges(g, as.vector(t(as.matrix(e[, c("from", "to")]))) + 1L)
    if (meta$weighted) igraph::E(g)$weight <- e$weight
  }
  binary <- matrix(0, n, n)
  valued <- matrix(0, n, n)
  if (nrow(e)) {
    i <- e$from + 1L
    j <- e$to + 1L
    w <- if (meta$weighted) e$weight else rep(1, nrow(e))
    binary[cbind(i, j)] <- 1
    if (!meta$directed) binary[cbind(j, i)] <- 1
    for (k in seq_along(i)) {
      valued[i[k], j[k]] <- valued[i[k], j[k]] + w[k]
      if (!meta$directed && i[k] != j[k]) valued[j[k], i[k]] <- valued[j[k], i[k]] + w[k]
    }
  }

  for (variant in names(manifest)) {
    spec <- manifest[[variant]]
    if (!applies(spec, meta)) next
    for (oracle in intersect(c("igraph", "sna", "stats", "s2", "sf"), names(spec$oracles))) {
      if (oracle == "sna" && n == 0) next
      if (oracle %in% c("s2", "sf") && !has_geo) next
      v <- tryCatch(
        switch(oracle,
          igraph = igraph_values(variant, spec, g, meta),
          sna = sna_values(variant, spec, binary, valued, meta),
          stats = stats_values(variant, spec, g, meta),
          s2 = geo_values(variant, spec, e, meta),
          sf = geo_values(variant, spec, e, meta)
        ),
        error = function(err) {
          message(sprintf("%s %s on %s failed: %s", oracle, variant, name, conditionMessage(err)))
          NULL
        }
      )
      if (!is.null(v)) {
        write_values(oracle, name, variant, v)
        counts[[oracle]] <- counts[[oracle]] + 1L
      }
    }
  }
}

writeLines(sprintf("igraph %s", utils::packageVersion("igraph")),
           file.path(golden_dir, "igraph", "VERSION"))
writeLines(sprintf("sna %s", utils::packageVersion("sna")),
           file.path(golden_dir, "sna", "VERSION"))
dir.create(file.path(golden_dir, "stats"), recursive = TRUE, showWarnings = FALSE)
writeLines(sprintf("R %s stats::cmdscale", getRversion()),
           file.path(golden_dir, "stats", "VERSION"))
if (has_geo) {
  dir.create(file.path(golden_dir, "s2"), recursive = TRUE, showWarnings = FALSE)
  writeLines(sprintf("s2 %s (sphere of radius %s m)", utils::packageVersion("s2"), EARTH_RADIUS_M),
             file.path(golden_dir, "s2", "VERSION"))
  dir.create(file.path(golden_dir, "sf"), recursive = TRUE, showWarnings = FALSE)
  writeLines(sprintf("sf %s (GEOS %s)", utils::packageVersion("sf"), sf::sf_extSoftVersion()[["GEOS"]]),
             file.path(golden_dir, "sf", "VERSION"))
}
cat(sprintf("Wrote %d igraph, %d sna, %d stats, %d s2, and %d sf golden files (roles).\n",
            counts[["igraph"]], counts[["sna"]], counts[["stats"]], counts[["s2"]],
            counts[["sf"]]))
