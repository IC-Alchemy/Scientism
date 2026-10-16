# Synthetic-data audit of the Nordvall et al. 2026 analysis script.
#
# The registry data behind the paper are restricted, so nothing here is a
# re-analysis of the study. This script builds a SYNTHETIC registry laid out
# like the script's input files, runs the authors' own lines verbatim on it,
# and checks what that code does to intervals, index dates and row counts.
# Every number this script prints describes the code's behaviour on invented
# data. None of it estimates anything about Jönköping County.
#
# Usage:  LC_ALL=C.UTF-8 Rscript synthetic_audit.R [path/to/CommMedNordvall2025Rscript.txt]
# With no path, the script is downloaded from Zenodo (10.5281/zenodo.18138478).

args <- commandArgs(trailingOnly = TRUE)
this_dir <- local({
  f <- sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE))
  if (length(f)) dirname(normalizePath(f)) else getwd()
})
source(file.path(this_dir, "audit_common.R"), encoding = "UTF-8")

script_path <- if (length(args)) args[1] else fetch_script_from_zenodo()
L <- read_script_lines(script_path)

N_VERBATIM <- as.integer(Sys.getenv("N_VERBATIM", "20000"))  # verbatim loop is O(N^2)
N_SIM      <- as.integer(Sys.getenv("N_SIM", "60000"))
REPS       <- as.integer(Sys.getenv("REPS", "60"))

# ---------------------------------------------------------------------------
# Synthetic world (all parameters are assumptions chosen for illustration)
# ---------------------------------------------------------------------------

# Gestational age at delivery in days from LMP: ~94.5% term N(281, 8.5)
# truncated to 259-301, ~5.5% preterm spread down to 22 weeks. Mean ~279 days.
rga <- function(n) {
  ga <- pmin(pmax(round(rnorm(n, 281, 8.5)), 259), 301)
  pre <- runif(n) < 0.055
  ga[pre] <- pmax(154, 258 - round(rgamma(sum(pre), shape = 1.6, scale = 14)))
  ga
}

# Annual hazard of a conception that leads to a delivery, by age at baseline.
h_age <- function(a) 0.10 * exp(-((a - 31) / 6)^2) + 0.004

make_world <- function(N, hr_true = 1, defer_in_pregnancy = 0.5, edge_cases = FALSE,
                       na_cases = FALSE, seed = 1) {
  set.seed(seed)
  n_inel <- round(0.08 * N)                   # men and out-of-range ages
  M <- N + n_inel
  age <- c(sample(18:45, N, TRUE), sample(c(16, 17, 46:60), n_inel, TRUE))
  sex <- c(rep("Kvinna", N), sample(c("Kvinna", "Man"), n_inel, TRUE, prob = c(.3, .7)))
  id  <- sprintf("P%07d", seq_len(M))
  fod <- START - round((age + runif(M)) * 365.25)
  elig <- seq_len(N)

  # Dose 2 schedule: ~75% uptake rising with age; early (healthcare) 5%,
  # main roll-out May-Sep 2021 (older first), late 8% Oct 2021 - Jun 2022.
  vacc <- runif(M) < plogis(1.1 + 0.05 * (age - 31))
  grp <- sample(c("early", "main", "late"), M, TRUE, prob = c(.05, .87, .08))
  d2 <- START + ifelse(grp == "early", sample(31:119, M, TRUE),
               ifelse(grp == "main", 134 + round((45 - pmin(pmax(age, 18), 45)) / 27 * 75) +
                                     round(rgamma(M, 2, scale = 15)),
                      sample(273:545, M, TRUE)))
  d2[!vacc] <- NA
  d3 <- d2 + sample(150:240, M, TRUE)
  d3 <- pmax(d3, as.Date("2021-09-15"))
  d3[runif(M) > 0.65] <- NA
  dd <- START + sample(0:1002, M, TRUE); dd[runif(M) > 0.001] <- NA
  dead_first <- !is.na(dd) & !is.na(d2) & d2 >= dd       # no vaccination after death
  d2[dead_first] <- NA
  d3[!is.na(dd) & !is.na(d3) & d3 >= dd] <- NA
  d3[is.na(d2)] <- NA

  # Pregnant on 2021-01-01 (excluded by the script via its first-delivery file).
  preg0 <- runif(M) < h_age(age) * 0.77 & sex == "Kvinna"
  ga0 <- rga(M)
  conc0 <- START - sample(1:266, M, TRUE)
  del0 <- conc0 + (ga0 - 14)
  preg0 <- preg0 & del0 >= START

  # Daily simulation of the first conception (leading to delivery) after
  # 2021-01-01, to 2024-03-31, with a time-varying dose-2 effect hr_true.
  frail <- rgamma(M, 2, 2)
  T_END <- as.integer(as.Date("2024-03-31") - START)
  conc <- rep(NA_integer_, M)
  at_risk <- !preg0 & sex == "Kvinna"
  t2 <- as.integer(d2 - START)
  base <- h_age(age) * frail / 365.25
  for (t in 1:T_END) {
    idx <- which(at_risk)
    h <- base[idx] * (1 - 0.03 * t / 365.25) *
      ifelse(!is.na(t2[idx]) & t2[idx] < t, hr_true, 1)
    hit <- idx[runif(length(idx)) < 1 - exp(-h)]
    conc[hit] <- t
    at_risk[hit] <- FALSE
  }
  conc <- START + conc
  ga <- rga(M)
  del <- conc + (ga - 14)

  # Women who know they are pregnant (>= 6 weeks) defer dose 2 until after delivery.
  defer <- !is.na(conc) & !is.na(d2) & d2 > conc + 42 & runif(M) < defer_in_pregnancy
  shift <- del[defer] + sample(30:180, sum(defer), TRUE) - d2[defer]
  d2[defer] <- d2[defer] + shift
  d3[defer] <- d3[defer] + shift

  # Recorded miscarriages: pre-2021 history and during follow-up (independent).
  mc_hist <- runif(M) < 0.03
  mc_fu   <- runif(M) < 0.01
  missfall <- rbind(
    data.frame(Personnr = id[mc_hist], PatientID = which(mc_hist),
               Kontaktdatum = as.Date("2016-01-01") + sample(0:1826, sum(mc_hist), TRUE)),
    data.frame(Personnr = id[mc_fu], PatientID = which(mc_fu),
               Kontaktdatum = START + sample(0:1002, sum(mc_fu), TRUE)))

  births <- data.frame(Personnr = id, PatientID = seq_len(M),
                       Kontaktdatum = ifelse(preg0, del0, del))
  births$Kontaktdatum <- as.Date(births$Kontaktdatum)
  births <- births[!is.na(births$Kontaktdatum) & births$Kontaktdatum <= as.Date("2024-12-31"), ]

  cohort <- data.frame(Personnr = id, PatientID = seq_len(M), age = age, fod = fod, sex = sex)
  dose2 <- data.frame(Personnr = id, Kontaktdatum = d2)[!is.na(d2), ]
  dose3 <- data.frame(Personnr = id, Kontaktdatum = d3)[!is.na(d3), ]
  deaths <- data.frame(Personnr = id, Avliden.datum = dd)[!is.na(dd), ]

  edge <- list()
  if (edge_cases) {
    pool <- sample(elig[!preg0[elig] & !is.na(conc[elig]) & conc[elig] > START + 60 &
                          conc[elig] < as.Date("2023-06-01") & !mc_hist[elig] & !mc_fu[elig]])
    # (a) dose 2 before 2021-01-01 (impossible in Sweden; a data-error probe)
    a <- sample(elig[is.na(d2[elig]) & !preg0[elig]], 3)
    dose2 <- rbind(dose2, data.frame(Personnr = id[a], Kontaktdatum = as.Date("2020-12-20")))
    # (b) dose 3 on or before dose 2
    b <- sample(elig[!is.na(d2[elig]) & !is.na(d3[elig]) & !preg0[elig]], 3)
    dose3$Kontaktdatum[match(id[b], dose3$Personnr)] <- d2[b] - c(0, 10, 30)
    # (c) dose 2 on the same day as the 280-day index date
    cc <- pool[1:5]
    dose2 <- dose2[!dose2$Personnr %in% id[cc], ]
    dose2 <- rbind(dose2, data.frame(Personnr = id[cc],
                                     Kontaktdatum = births$Kontaktdatum[match(id[cc], births$Personnr)] - 280))
    # (d) 280-day index date exactly 2021-01-01
    dsel <- pool[6:7]
    births$Kontaktdatum[match(id[dsel], births$Personnr)] <- START + 280
    # (e) dose 2 after study end (2024)
    e <- sample(elig[is.na(d2[elig]) & is.na(conc[elig]) & !preg0[elig]], 4)
    dose2 <- rbind(dose2, data.frame(Personnr = id[e], Kontaktdatum = as.Date("2024-02-01")))
    # (f) duplicated death record
    f <- elig[!is.na(dd[elig]) & !is.na(d2[elig]) & dd[elig] > d2[elig] & !preg0[elig] &
                (is.na(conc[elig]) | conc[elig] > dd[elig])][1]   # vaccinated, died after dose 2
    deaths <- rbind(deaths, deaths[deaths$Personnr == id[f], ])
    edge <- list(pre2021_dose2 = id[a], dose3_le_dose2 = id[b], index_eq_dose2 = id[cc],
                 index_on_day0 = id[dsel], dose2_after_end = id[e], dup_death = id[f])
  }
  if (na_cases) {
    pick <- function(k, cond = rep(TRUE, M)) sample(which(cond & seq_len(M) <= N & !preg0), k)
    cohort$age[pick(5)] <- NA                                   # missing age
    cohort$fod[nf <- pick(5, !is.na(conc) & conc < as.Date("2023-06-01"))] <- NA  # missing DOB
    cohort$sex[pick(2)] <- NA                                   # missing sex
    cohort$PatientID[pick(1)] <- NA                             # missing PatientID
    births$Kontaktdatum[sample(which(births$Kontaktdatum > as.Date("2021-12-31")), 3)] <- NA
    missfall <- rbind(missfall,
                      data.frame(Personnr = NA, PatientID = NA, Kontaktdatum = START + c(100, 200)),
                      data.frame(Personnr = id[pick(2)], PatientID = NA, Kontaktdatum = NA))
    dose2$Kontaktdatum[sample(nrow(dose2), 2)] <- NA
    edge$na_dob_with_event <- id[nf]
  }
  names(cohort) <- c("Personnr", "PatientID", AGE, FOD, KON)
  truth <- data.frame(Personnr = id, age = age, conc = conc, ga = ga, del = del,
                      preg0 = preg0, d2 = d2, d3 = d3, dd = dd, eligible = seq_len(M) <= N)
  list(cohort = cohort, births = births, dose2 = dose2, dose3 = dose3, deaths = deaths,
       missfall = missfall, truth = truth, edge = edge)
}

# Write the world as CSV files at the script's own relative paths under `root`.
write_world <- function(w, lines, root) {
  paths <- regmatches(lines, regexpr('read\\.csv\\("[^"]+"', lines))
  paths <- unique(sub('^read\\.csv\\("', "", sub('"$', "", paths)))
  pick <- function(pattern) paths[grepl(pattern, paths)][1]
  put <- function(d, path, sep) {
    p <- file.path(root, path)
    dir.create(dirname(p), recursive = TRUE, showWarnings = FALSE)
    write.table(d, p, sep = sep, row.names = FALSE, na = "NA", fileEncoding = "latin1")
  }
  dth <- w$deaths; names(dth) <- c("Personnr", "Avliden datum")
  put(w$cohort,   pick("data\\.csv$"), ",")
  put(dth,        pick("jkp\\.csv$"), ";")
  put(w$births,   pick("rlossningJan21_"), ";")
  put(w$dose2,    pick("Dos2\\.csv$"), ";")
  put(w$dose3,    pick("Dos3\\.csv$"), ";")
  put(w$missfall, pick("/Missfall\\.csv$"), ";")
  fm <- w$missfall[!is.na(w$missfall$Kontaktdatum) & w$missfall$Kontaktdatum >= START, ]
  fm <- fm[order(fm$Personnr, fm$Kontaktdatum), ]
  fm <- fm[!duplicated(fm$Personnr), ]
  names(fm)[3] <- "Inskrivningsdatum"
  put(fm, pick("rstaMissfall21_"), ";")
  invisible(root)
}

new_root <- function() {
  r <- tempfile("nordvall_synth_"); dir.create(r); r
}

section <- function(x) cat("\n", strrep("=", 78), "\n", x, "\n", strrep("=", 78), "\n", sep = "")
show <- function(x) print(x, row.names = FALSE)

# ---------------------------------------------------------------------------
# 0. Can the deposited script be run as deposited?
# ---------------------------------------------------------------------------
section("0. Parse check of the deposited file")
whole <- tryCatch({ parse(text = L); "parses" }, error = function(e) conditionMessage(e))
cat("Whole file:", whole, "\n")
for (ln in c(136L, 140L)) {
  r <- tryCatch({ parse(text = L[ln]); "parses" }, error = function(e) "PARSE ERROR (curly quotes)")
  cat(sprintf("Line %d: %s | %s\n", ln, r, L[ln]))
}
cat("Lines 38/39: both assign Befruktningsdatum; run top-to-bottom, line 39 (266 days) wins.\n")
cat("Paper's primary analysis uses 280 days (line 38). Part I prep run below with line 39 skipped.\n")

# ---------------------------------------------------------------------------
# 1. Interval splitting: manual construction vs survival::tmerge()
# ---------------------------------------------------------------------------
section("1. Interval splitting (verbatim lines 22-129 vs survival::tmerge)")
cat("tmerge() calls in script:", sum(grepl("tmerge", L)), "\n")
cat("survSplit() calls (calendar periods, lines):", paste(grep("survSplit", L), collapse = ", "), "\n")
cat("tt() time-varying coefficient models (lines):", paste(grep("tt\\(exposure\\)", L)[c(TRUE, FALSE)], collapse = ", "), "\n")

w1 <- make_world(N_VERBATIM, edge_cases = TRUE, seed = 11)
root1 <- write_world(w1, L, new_root())
t0 <- Sys.time()
p1 <- run_part1(L, root1, offset = 280, stop_before = LINE_MISSFALL_FILTER - 3L)  # stop before miscarriage block
cat(sprintf("Verbatim Part I prep (N=%d eligible women) ran in %.0f s\n", N_VERBATIM,
            as.numeric(Sys.time() - t0, units = "secs")))
if (any(!is.na(p1$log$error))) show(p1$log[!is.na(p1$log$error), ])
comb <- p1$env$comb

cat("\nInterval invariants on the script's comb:\n"); show(check_intervals(comb))

# tmerge rebuild from the same eligible persons (script's `data` after line 61)
elig_p <- unique(p1$env$data$Personnr)
bir <- p1$env[["FörstaFörlossningOkt21_"]]
index <- data.frame(Personnr = bir$Personnr, idx_date = bir$Kontaktdatum)
index <- index[index$Personnr %in% elig_p, ]
d2 <- w1$dose2; names(d2)[2] <- "d2"
d3 <- w1$dose3; names(d3)[2] <- "d3"
dth <- w1$deaths; names(dth)[2] <- "dd"
td <- build_tmerge(elig_p, index, d2[d2$Personnr %in% elig_p, ], d3, dth)
cmp <- compare_datasets(comb, td)
cat(sprintf("\nScript rows identical to tmerge rows: %d; script-only rows: %d; tmerge-only rows: %d\n",
            cmp$identical_rows, cmp$script_only, cmp$tmerge_only))
cat("Persons whose intervals differ:", length(cmp$persons_differing), "\n")
dp <- cmp$persons_differing
first_d2 <- with(aggregate(Kontaktdatum ~ Personnr, w1$dose2, min), setNames(Kontaktdatum, Personnr))
ix <- merge(index, data.frame(Personnr = names(first_d2), d2 = first_d2), by = "Personnr")
d3m <- merge(data.frame(Personnr = names(first_d2), d2 = first_d2), w1$dose3, by = "Personnr")
cause <- data.frame(Personnr = dp,
  dose2_before_entry = dp %in% names(first_d2)[first_d2 < START],
  index_equals_dose2 = dp %in% ix$Personnr[ix$idx_date == ix$d2],
  dose2_after_study_end = dp %in% names(first_d2)[first_d2 > SLUT],
  dose3_on_or_before_dose2 = dp %in% d3m$Personnr[d3m$Kontaktdatum <= d3m$d2],
  duplicated_input_record = dp %in% w1$deaths$Personnr[duplicated(w1$deaths$Personnr)])
ci <- check_intervals(comb)
cat(sprintf("Interval check with duplicates: gaps/overlaps %d, persons with >2 rows %d (see dup_death below)\n",
            ci$value[6], ci$value[10]))
cause$none_of_these <- rowSums(cause[, -1]) == 0
cat("  by computed cause (a person can have several):\n"); print(colSums(cause[, -1]))
cat(sprintf("  natural ties (index == dose 2) not injected: %d\n",
            length(setdiff(dp[cause$index_equals_dose2], w1$edge$index_eq_dose2))))

show_person <- function(p) {
  a <- comb[comb$Personnr == p, c("Personnr", "exposure", "startTime", "endTime", "status")]
  b <- td[td$Personnr == p, c("tstart", "tstop", "status", "exposure")]
  cat(" script:\n"); if (nrow(a)) show(a) else cat("   (no rows: person removed)\n")
  cat(" tmerge:\n"); if (nrow(b)) show(b) else cat("   (no rows)\n")
}
for (nm in names(w1$edge)) {
  cat(sprintf("\n-- Edge case '%s' (first injected person) --\n", nm))
  show_person(w1$edge[[nm]][1])
}

comb$age <- comb[[AGE]]
td$age <- w1$cohort[[AGE]][match(td$Personnr, w1$cohort$Personnr)]
edge_ids <- unique(c(unlist(w1$edge), dp))
cat("\nAge-adjusted HR, script dataset vs tmerge dataset (synthetic true HR = 1):\n")
show(data.frame(dataset = c("script, all", "tmerge, all", "script, differing persons removed",
                            "tmerge, differing persons removed"),
                round(rbind(fit_hr(comb), fit_hr(td, "tstart", "tstop"),
                            fit_hr(comb[!comb$Personnr %in% edge_ids, ]),
                            fit_hr(td[!td$Personnr %in% edge_ids, ], "tstart", "tstop")), 4)))

# Risk-set entry check: any vaccination recorded before the person's entry?
tr <- w1$truth
d2_first <- aggregate(Kontaktdatum ~ Personnr, w1$dose2, min)
pre <- d2_first[d2_first$Kontaktdatum < START & d2_first$Personnr %in% elig_p, ]
cat(sprintf("\nEligible persons with dose 2 before entry (2021-01-01): %d\n", nrow(pre)))
cat(sprintf("  ...of whom have an exposed row in comb: %d; classified unexposed for all follow-up: %d\n",
            sum(pre$Personnr %in% comb$Personnr[comb$exposure == 1]),
            sum(pre$Personnr %in% comb$Personnr & !pre$Personnr %in% comb$Personnr[comb$exposure == 1])))

# Immortal-time check of the 'ever exposed' Kaplan-Meier summary (script lines 162-189)
ks <- aggregate(cbind(status, endTime, exposure) ~ Personnr, comb, max)
cat("\nScript's KM summary uses ever_exposed = max(exposure) per person.\n")
cat(sprintf("  Events among 'ever exposed': %d of %d persons; among 'never exposed': %d of %d\n",
            sum(ks$status[ks$exposure == 1]), sum(ks$exposure == 1),
            sum(ks$status[ks$exposure == 0]), sum(ks$exposure == 0)))
km_cox <- coxph(Surv(endTime, status) ~ exposure, data = ks)
cat(sprintf("  Cox HR on that person-level 'ever exposed' summary: %.2f (synthetic truth: 1.00)\n",
            exp(coef(km_cox))))

# ---------------------------------------------------------------------------
# 2. Date arithmetic: fixed 280/266-day offsets vs gestational-age-based index
# ---------------------------------------------------------------------------
section("2. Index-date arithmetic (synthetic gestational ages)")
cat("Columns in the delivery file the script reads (inferred from positional drops at lines 40/64):\n")
cat("  Personnr, <col 2 dropped before merge>, Kontaktdatum -> no gestational-age field is read.\n")
cat("  A 4th column (e.g. GA) would shift the positional drops at lines 79/95.\n\n")

ga_eff <- tr$ga[!is.na(tr$conc)]
cat("Synthetic gestational-age distribution (days from LMP), assumed not observed:\n")
print(round(quantile(ga_eff, c(0, .01, .05, .25, .5, .75, .95, .99, 1))))
cat(sprintf("  mean %.1f; preterm (<259 d) %.1f%%; error of fixed 280 vs LMP-based index: mean %.1f, SD %.1f days\n",
            mean(ga_eff), 100 * mean(ga_eff < 259), mean(280 - ga_eff), sd(280 - ga_eff)))
cat(sprintf("  error of fixed 266 vs conception (GA-14): mean %.1f, SD %.1f days; |error| > 28 d in %.1f%%\n",
            mean(266 - (ga_eff - 14)), sd(266 - (ga_eff - 14)), 100 * mean(abs(266 - (ga_eff - 14)) > 28)))

# Verbatim run with a GA-based index injected at line 39 (dynamic offset)
dyn_hook <- function(kind) function(env) {
  nm <- "FörstaFörlossningOkt21_"
  b <- get(nm, envir = env)
  g <- w1$truth$ga[match(b$Personnr, w1$truth$Personnr)]
  off <- if (kind == "lmp") g else g - 14
  b$Befruktningsdatum <- as.Date(b$Kontaktdatum - off)
  assign(nm, b, envir = env)
}
cat("\nVerbatim lines 22-125 with four index definitions (same synthetic world, true HR = 1):\n")
res <- list(); ph <- list(); events_by_spec <- list()
for (spec in list(list("fixed 280 (paper primary)", 280, NULL),
                  list("GA-based, LMP (delivery - GA)", "custom", dyn_hook("lmp")),
                  list("fixed 266 (paper sensitivity)", 266, NULL),
                  list("GA-based, conception (delivery - GA + 14)", "custom", dyn_hook("conc")))) {
  r <- run_part1(L, root1, offset = spec[[2]], custom_index = spec[[3]],
                 stop_before = LINE_MISSFALL_FILTER - 3L)
  cb <- r$env$comb; cb$age <- cb[[AGE]]
  a <- fit_hr(cb); u <- fit_hr(cb, adjust = FALSE)
  res[[length(res) + 1]] <- data.frame(index = spec[[1]], crude_HR = round(u[["HR"]], 4),
    adj_HR = round(a[["HR"]], 4), adj_lo = round(a[["lo"]], 4), adj_hi = round(a[["hi"]], 4),
    events = a[["events"]], persons = length(unique(cb$Personnr)),
    excluded_pregnant_at_start = nrow(r$env$grav))
  ph[[length(ph) + 1]] <- data.frame(index = spec[[1]], t(round(ph_outputs(cb), 4)))
  ev <- cb[cb$status == 1, c("Personnr", "exposure")]
  events_by_spec[[spec[[1]]]] <- setNames(ev$exposure, ev$Personnr)
}
show(do.call(rbind, res))
cat("\nProportional-hazards outputs (Schoenfeld p for exposure; period HRs as in Table S4):\n")
show(do.call(rbind, ph))
cmp_ev <- function(a, b) {
  x <- events_by_spec[[a]]; y <- events_by_spec[[b]]; both <- intersect(names(x), names(y))
  cat(sprintf("  %s vs %s: events in both %d, exposure class differs %d, event in only one %d\n",
              a, b, length(both), sum(x[both] != y[both]), length(union(setdiff(names(x), both), setdiff(names(y), both)))))
}
cat("\nEvent-level reclassification between index definitions:\n")
nm <- names(events_by_spec)
cmp_ev(nm[1], nm[2]); cmp_ev(nm[3], nm[4]); cmp_ev(nm[1], nm[3])

# Replicate simulation (fast path: tmerge, validated above against the verbatim build)
fast_hr <- function(w, kind) {
  tr <- w$truth
  b <- w$births
  g <- tr$ga[match(b$Personnr, tr$Personnr)]
  b$idx_date <- b$Kontaktdatum - switch(kind, f280 = 280, f266 = 266, lmp = g, conc = g - 14)
  coh <- w$cohort
  keep <- !is.na(coh[[AGE]]) & coh[[AGE]] >= 18 & coh[[AGE]] < 46 & coh[[KON]] %in% "Kvinna"
  persons <- coh$Personnr[keep]
  persons <- setdiff(persons, b$Personnr[b$idx_date < START])
  d2 <- w$dose2; names(d2)[2] <- "d2"; d3 <- w$dose3; names(d3)[2] <- "d3"
  dth <- w$deaths; names(dth)[2] <- "dd"
  td <- build_tmerge(persons, b[b$Personnr %in% persons, c("Personnr", "idx_date")],
                     d2[d2$Personnr %in% persons, ], d3, dth)
  td$age <- coh[[AGE]][match(td$Personnr, coh$Personnr)]
  c(crude = fit_hr(td, "tstart", "tstop", FALSE)[["HR"]], adj = fit_hr(td, "tstart", "tstop")[["HR"]])
}
set.seed(2026)
cat(sprintf("\nReplicates: %d synthetic worlds of N = %d women each, per true HR\n", REPS, N_SIM))
grid <- expand.grid(rep = seq_len(REPS), true_hr = c(1, 0.9))
sim <- parallel::mclapply(seq_len(nrow(grid)), function(g) {
  hr <- grid$true_hr[g]; r <- grid$rep[g]
  w <- make_world(N_SIM, hr_true = hr, seed = round(1000 * hr) + r)
  est <- sapply(c("f280", "lmp", "f266", "conc"), function(k) fast_hr(w, k))
  data.frame(true_hr = hr, rep = r, index = colnames(est), crude = est["crude", ], adj = est["adj", ])
}, mc.cores = max(1L, parallel::detectCores() - 0L))
sim <- do.call(rbind, sim)
agg <- aggregate(cbind(adj, crude) ~ true_hr + index, sim, function(x) c(mean = mean(x), sd = sd(x)))
agg <- do.call(data.frame, agg)
show(within(agg, { adj.mean <- round(adj.mean, 4); adj.sd <- round(adj.sd, 4)
                   crude.mean <- round(crude.mean, 4); crude.sd <- round(crude.sd, 4) }))
paired <- reshape(sim[, c("true_hr", "rep", "index", "adj")], idvar = c("true_hr", "rep"),
                  timevar = "index", direction = "wide")
cat("\nWithin-world difference in adjusted log-HR (fixed minus GA-based):\n")
for (hr in c(1, 0.9)) {
  p <- paired[paired$true_hr == hr, ]
  d1 <- log(p$adj.f280) - log(p$adj.lmp); d2x <- log(p$adj.f266) - log(p$adj.conc)
  cat(sprintf("  true HR %.1f: 280 vs LMP-based mean %+.4f (max |.| %.4f); 266 vs conception-based mean %+.4f (max |.| %.4f)\n",
              hr, mean(d1), max(abs(d1)), mean(d2x), max(abs(d2x))))
}

# ---------------------------------------------------------------------------
# 3. Missingness and row counts through the miscarriage filters
# ---------------------------------------------------------------------------
section("3. Row-count trace with injected NA values (verbatim lines 22-129)")
w3 <- make_world(N_VERBATIM, na_cases = TRUE, seed = 33)
root3 <- write_world(w3, L, new_root())
p3 <- run_part1(L, root3, offset = 280,
                hooks = list("123" = function(env) assign("comb_before_128", env$comb, envir = env)))
lg <- p3$log
cat("Every change in rows / persons / all-NA phantom rows, by source line:\n")
show(lg[, c("line", "object", "rows", "persons", "phantom_na_rows", "code")])
if (any(!is.na(lg$error))) { cat("\nErrors:\n"); show(lg[!is.na(lg$error), c("line", "error")]) }

e3 <- p3$env
cb0 <- e3$comb_before_128
mf <- e3$Missfall
cat("\nMiscarriage filter, line 128: comb <- comb[!(comb$Personnr %in% Missfall$Personnr),]\n")
hit <- cb0$Personnr %in% mf$Personnr
real <- !is.na(cb0$Personnr)
cat(sprintf("  comb rows %d -> %d; persons %d -> %d; phantom all-NA rows %d -> %d\n",
            nrow(cb0), nrow(e3$comb), length(unique(cb0$Personnr[real])),
            length(unique(e3$comb$Personnr[!is.na(e3$comb$Personnr)])),
            sum(!real), sum(is.na(e3$comb$Personnr))))
cat(sprintf("  Missfall rows: %d; NA Personnr: %d; NA date: %d\n",
            nrow(mf), sum(is.na(mf$Personnr)), sum(is.na(mf$Kontaktdatum))))
cat("  The filter reads Missfall$Personnr only. The miscarriage date and gestational week are\n")
cat("  never used, so no '>= 22 weeks' condition exists at this line.\n")
cat(sprintf("  %%in%% never returns NA, so the line cannot create NA rows. Phantom rows removed only\n"))
cat(sprintf("  because Missfall also has NA Personnr (NA %%in%% NA is TRUE): %d\n", sum(hit & !real)))
rm_p <- unique(cb0$Personnr[hit & real])
mf_ok <- mf[!is.na(mf$Personnr) & !is.na(mf$Kontaktdatum), ]
pre_only <- setdiff(mf_ok$Personnr[mf_ok$Kontaktdatum < START], mf_ok$Personnr[mf_ok$Kontaktdatum >= START])
undated <- setdiff(mf$Personnr[!is.na(mf$Personnr) & is.na(mf$Kontaktdatum)], mf_ok$Personnr)
ev_rm <- unique(cb0$Personnr[hit & real & cb0$status == 1])
cat(sprintf("  Real women removed: %d (rows %d)\n", length(rm_p), sum(hit & real)))
cat(sprintf("    whose every miscarriage record predates 2021-01-01: %d\n", length(intersect(rm_p, pre_only))))
cat(sprintf("    whose only record has a missing date: %d\n", length(intersect(rm_p, undated))))
cat(sprintf("    who carried a childbirth index event (status = 1), now deleted: %d\n", length(ev_rm)))
cat(sprintf("  Events: %d -> %d\n", sum(cb0$status, na.rm = TRUE), sum(e3$comb$status, na.rm = TRUE)))

# NA-driven exclusions upstream of the filter, by injected cause
miss_from <- function(ids) sum(!ids %in% cb0$Personnr)
dob_na <- w3$edge$na_dob_with_event
cat(sprintf("\nWomen with missing birth date (age and dates present) lost from comb: %d of %d\n",
            miss_from(dob_na), length(dob_na)))
cat("  (lines 71-121 derive interval times from age in days, so a missing birth date makes\n")
cat("   Time1 NA and the subset at line 122 turns each such row into an all-NA phantom row.)\n")
d2na <- w3$dose2$Personnr[is.na(w3$dose2$Kontaktdatum)]
cat(sprintf("Women with a dose-2 record but a missing dose-2 date: %d; kept as unexposed for all follow-up: %d\n",
            length(d2na), sum(d2na %in% cb0$Personnr & !d2na %in% cb0$Personnr[cb0$exposure == 1])))
bna <- w3$births$Personnr[is.na(w3$births$Kontaktdatum)]
cat(sprintf("Women with a delivery record but a missing delivery date: %d; counted as event-free: %d\n",
            length(bna), sum(bna %in% cb0$Personnr & !bna %in% cb0$Personnr[cb0$status == 1])))

# Part II: which miscarriage object is used?
section("3b. Part II (miscarriage outcome): object provenance")
fresh <- new.env(parent = globalenv())
old <- setwd(root3)
lg2 <- run_traced(L, PART2_PREP[1], PART2_PREP[2], fresh, watch = c("data", "test", "comb"),
                  stop_on_error = TRUE)
setwd(old)
cat("Part II run in a fresh R session:\n")
show(lg2[!is.na(lg2$error), c("line", "error", "code")])
run_part2 <- function(parent, use_shifted) {
  env <- new.env(parent = parent)
  hooks <- list(); skip <- integer()
  if (use_shifted) {
    skip <- 355L
    hooks[["354"]] <- function(e) e$test <- merge(e$test, e[["F\u00f6rstaMissfall21_"]][, -c(2)],
                                                  by = "Personnr", all.x = TRUE)
  }
  old <- setwd(root3); on.exit(setwd(old))
  lg <- run_traced(L, PART2_PREP[1], PART2_PREP[2], env, hooks = hooks, skip = skip,
                   watch = c("data", "test", "comb"))
  list(env = env, log = lg)
}
asrun <- run_part2(e3, use_shifted = FALSE)
shift <- run_part2(e3, use_shifted = TRUE)
summ <- function(x, label) {
  cb <- x$env$comb; ok <- !is.na(cb$Personnr)
  data.frame(variant = label, persons = length(unique(cb$Personnr[ok])), rows = sum(ok),
             phantom_rows = sum(!ok), events = sum(cb$status[ok]))
}
cat("\nPart II run after Part I in the same session (two variants):\n")
show(rbind(summ(asrun, "as deposited: line 355 merges Missfall (Part I object, unshifted)"),
           summ(shift, "line 355 replaced by the -154-day shifted F\u00f6rstaMissfall21_")))
cat(sprintf("Women with >1 Missfall record (the merge at line 355 multiplies their rows): %d\n",
            sum(table(e3$Missfall$Personnr) > 1)))

# Exposure attribution under the -154-day shift: an event dated m - 154 counts as
# exposed only if dose 2 <= m - 154, i.e. dose 2 came >= 154 days before the miscarriage.
cbs <- shift$env$comb; cbs <- cbs[!is.na(cbs$Personnr) & cbs$status == 1, ]
m_true <- cbs$Kontaktdatum + 154
d2_of <- w3$dose2$Kontaktdatum[match(cbs$Personnr, w3$dose2$Personnr)]
after_d2 <- !is.na(d2_of) & m_true > d2_of
cat(sprintf(paste0("Shifted variant: miscarriage events dated after the woman's dose 2: %d;",
                   " of these classified exposed: %d, unexposed: %d\n"),
            sum(after_d2), sum(after_d2 & cbs$exposure == 1), sum(after_d2 & cbs$exposure == 0)))
cat("  (any miscarriage within 154 days after dose 2, i.e. vaccination during that pregnancy,\n")
cat("   is attributed to unexposed time under the shift)\n")

cat("\nDone.\n")
