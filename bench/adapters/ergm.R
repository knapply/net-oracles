#!/usr/bin/env Rscript
# ergm (statnet): MPLE and MCMC-MLE fits. Model, seed and controls come from PATH.model (measures.yaml).
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(ergm))

ctl_mcmle <- function(m) control.ergm(
  seed = mnum(m, "controls.seed"), MCMC.burnin = mnum(m, "controls.mcmle.burnin"), MCMC.interval = mnum(m, "controls.mcmle.interval"),
  MCMC.samplesize = mnum(m, "controls.mcmle.samplesize"), MCMLE.maxit = mnum(m, "controls.mcmle.maxit"), parallel = 0)
se_of <- function(fit) sqrt(diag(vcov(fit)))

bench_main(
  tool = "ergm",
  version = function() as.character(packageVersion("ergm")),
  note = "single thread (parallel = 0); the seed is set before each fit",
  load = function(ctx) { tb <- load_tables(ctx); list(nw = make_network(tb), model = read_model(ctx$graph)) },
  calls = list(
    ergm_mple = function(G, ctx) {
      nw <- G$nw; set.seed(mnum(G$model, "controls.seed"))
      fit <- ergm(mformula(G$model, "nw"), estimate = "MPLE", control = control.ergm(seed = mnum(G$model, "controls.seed"), parallel = 0))
      fit_digest(coef(fit), se_of(fit), iterations = NA_real_, terms = names(coef(fit)))
    },
    ergm_mcmle = function(G, ctx) {
      nw <- G$nw; m <- G$model; set.seed(mnum(m, "controls.seed"))
      fit <- ergm(mformula(m, "nw"), control = ctl_mcmle(m))
      its <- as.numeric(fit$iterations)
      steps <- its * (mnum(m, "controls.mcmle.burnin") + mnum(m, "controls.mcmle.samplesize") * mnum(m, "controls.mcmle.interval"))
      fit_digest(coef(fit), se_of(fit), iterations = its, mcmc_steps = steps, converged = if (is.null(fit$converged)) NA_real_ else as.numeric(isTRUE(fit$converged)), terms = names(coef(fit)))
    }
  )
)
