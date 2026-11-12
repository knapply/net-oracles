#!/usr/bin/env Rscript
# RSiena (siena07, method of moments): three waves of friendship (s50) with drinking behaviour.
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(RSiena))

bench_main(
  tool = "rsiena",
  version = function() as.character(packageVersion("RSiena")),
  note = "one thread (nbrNodes = 1); the seed is the algorithm's",
  load = function(ctx) {
    tb <- load_tables(ctx)
    arr <- array(0, c(tb$n, tb$n, tb$waves))
    for (w in seq_len(tb$waves)) { e <- tb$edges[tb$edges$wave == w, ]; arr[cbind(e$from, e$to, w)] <- 1 }
    beh <- as.matrix(tb$nodes[, grep("^alcohol", names(tb$nodes))])
    d <- sienaDataCreate(friendship = sienaDependent(arr), drinking = sienaDependent(beh, type = "behavior"))
    eff <- getEffects(d)
    eff <- includeEffects(eff, transTrip, cycle3, verbose = FALSE)
    eff <- includeEffects(eff, egoX, altX, simX, interaction1 = "drinking", verbose = FALSE)
    eff <- includeEffects(eff, avAlt, name = "drinking", interaction1 = "friendship", verbose = FALSE)
    list(data = d, effects = eff, model = read_model(ctx$graph))
  },
  calls = list(
    siena_mom = function(G, ctx) {
      m <- G$model
      alg <- sienaAlgorithm(nsub = mnum(m, "controls.siena.nsub"), n3 = mnum(m, "controls.siena.n3"), seed = mnum(m, "controls.seed"),
                            projname = tempfile("siena"), useStdInits = FALSE, nbrNodes = 1)
      ans <- siena07(alg, data = G$data, effects = G$effects, batch = TRUE, verbose = FALSE, silent = TRUE, returnDeps = FALSE)
      ph <- function(x) if (is.null(x)) NA_real_ else as.numeric(x)[1]
      fit_digest(ans$theta, ans$se, tconv_max = ph(ans$tconv.max), converged = as.numeric(isTRUE(ans$OK)),
                 phase3_iterations = ph(nrow(ans$sf)), n = ph(ans$n), fields = paste(names(ans), collapse = " "))
    }
  )
)
