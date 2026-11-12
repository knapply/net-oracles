#!/usr/bin/env Rscript
# latentnet (statnet): Euclidean latent space model (d = 2) fitted by MCMC; fixed chain settings from PATH.model.
.dir <- dirname(sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE)[1]))
source(file.path(.dir, "common.R"))
suppressPackageStartupMessages(library(latentnet))

bench_main(
  tool = "latentnet",
  version = function() as.character(packageVersion("latentnet")),
  note = "posterior mean and sd of the intercept as coef and se",
  load = function(ctx) { tb <- load_tables(ctx); list(nw = make_network(tb), model = read_model(ctx$graph)) },
  calls = list(
    latent_fit = function(G, ctx) {
      nw <- G$nw; m <- G$model
      fit <- ergmm(nw ~ euclidean(d = mnum(m, "controls.latent.dim")), seed = mnum(m, "controls.seed"),
                   control = ergmm.control(burnin = mnum(m, "controls.latent.burnin"), sample.size = mnum(m, "controls.latent.samplesize"),
                                           interval = mnum(m, "controls.latent.interval")), verbose = 0)
      b <- fit$sample$beta
      fit_digest(mean(b), sd(b), draws = length(b), burnin = mnum(m, "controls.latent.burnin"))
    }
  )
)
