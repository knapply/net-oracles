#!/usr/bin/env Rscript
# tergm (statnet): separable formation and persistence fit on a small panel (conditional MLE).
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(tergm))

bench_main(
  tool = "tergm",
  version = function() as.character(packageVersion("tergm")),
  load = function(ctx) { tb <- load_tables(ctx); list(nws = lapply(seq_len(tb$waves), function(w) make_network(tb, w)), model = read_model(ctx$graph)) },
  calls = list(
    tergm_fit = function(G, ctx) {
      nws <- G$nws; set.seed(mnum(G$model, "controls.seed"))
      fit <- tergm(nws ~ Form(~edges + mutual) + Persist(~edges + mutual), estimate = G$model[["controls.tergm.estimate"]],
                   control = control.tergm(seed = mnum(G$model, "controls.seed"), parallel = 0))
      fit_digest(coef(fit), sqrt(diag(vcov(fit))), terms = names(coef(fit)))
    }
  )
)
