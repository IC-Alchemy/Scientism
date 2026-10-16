# Registry-side audit of the Nordvall et al. 2026 analysis script.
#
# For someone WITH authorised access to the study's restricted input files.
# It runs the authors' own lines (Zenodo v1.0) verbatim against those files and
# reports the three checks below. It writes only to OUT_DIR and never modifies
# the input files.
#
#   1. Interval splitting: is survival::tmerge() used? Does the hand-built
#      start/stop dataset match a tmerge() rebuild? Does any woman have a
#      vaccination before her entry into the risk set?
#   2. Index-date arithmetic: the raw gestational-age distribution of the
#      deliveries, and HR / Schoenfeld / period-HR output when the fixed
#      280- or 266-day offset is replaced by each delivery's recorded GA.
#   3. Missingness: row and person counts after every line, phantom all-NA
#      rows, and a before/after breakdown of the miscarriage filters.
#
# Usage (UTF-8 locale; on Windows run R with a UTF-8 code page, R >= 4.2):
#   Rscript registry_audit.R <original_script.txt> [ga_file.csv] [out_dir]
#
# Input files are read from the paths written in the original script
# ("H:/Dokument/..."). Set DATA_ROOT to a directory if those paths are
# relative to it rather than absolute drive paths.
#
# ga_file.csv (optional) is needed for check 2. It needs one row per delivery,
# from the Medical Birth Register or the obstetric record. The default columns
# are Personnr;Forlossningsdatum;GA_dagar (GA in completed days from LMP or
# ultrasound dating). Override them with the GA_ID, GA_DATE, GA_DAYS and
# GA_SEP environment variables.

args <- commandArgs(trailingOnly = TRUE)
if (!length(args)) stop("Usage: Rscript registry_audit.R <original_script.txt> [ga_file.csv] [out_dir]")
this_dir <- local({
  f <- sub("^--file=", "", grep("^--file=", commandArgs(FALSE), value = TRUE))
  if (length(f)) dirname(normalizePath(f)) else getwd()
})
source(file.path(this_dir, "audit_common.R"), encoding = "UTF-8")

L <- read_script_lines(args[1])
ga_path <- if (length(args) >= 2 && nzchar(args[2])) args[2] else NA
OUT <- if (length(args) >= 3) args[3] else file.path(getwd(), "nordvall_registry_audit")
dir.create(OUT, showWarnings = FALSE, recursive = TRUE)
ROOT <- Sys.getenv("DATA_ROOT", getwd())

log_file <- file.path(OUT, "registry_audit_report.txt")
sink(log_file, split = TRUE)
on.exit(sink(), add = TRUE)
section <- function(x) cat("\n", strrep("=", 78), "\n", x, "\n", strrep("=", 78), "\n", sep = "")
show <- function(x) print(x, row.names = FALSE)
save_csv <- function(x, name) utils::write.csv(x, file.path(OUT, name), row.names = FALSE)

NM_BIRTH <- "F\u00f6rstaF\u00f6rlossningOkt21_"
NM_D2 <- "F\u00f6rstaVaccinationDos2"
NM_D3 <- "F\u00f6rstaVaccinationDos3"
NM_DEATH <- "d\u00f6da"
NM_FM <- "F\u00f6rstaMissfall21_"

cat("Audit run:", format(Sys.time()), "| R", R.version$major, ".", R.version$minor,
    "| survival", as.character(packageVersion("survival")), "\n")
cat("Script:", args[1], "| md5", unname(tools::md5sum(args[1])), "\n")

# ---------------------------------------------------------------------------
# 0. Input files as the script reads them (lines 22-51, 84-86, 126-127)
# ---------------------------------------------------------------------------
section("0. Input files")
CAPTURE <- list(
  "37"  = function(env) assign("births_raw", env[[NM_BIRTH]], envir = env),   # delivery dates
  "123" = function(env) assign("comb_before_128", env$comb, envir = env))
p0 <- run_part1(L, ROOT, offset = 280, stop_before = 54L, hooks = CAPTURE)   # through dose-2 read
e0 <- p0$env
old <- setwd(ROOT)
d3_raw <- eval(parse(text = L[84:86]), envir = e0)
eval(parse(text = L[126:127]), envir = e0)
setwd(old)
inputs <- list(cohort = e0$data, deaths = e0[[NM_DEATH]], births = e0$births_raw,
               dose2 = e0[[NM_D2]], dose3 = e0[[NM_D3]], missfall = e0$Missfall)
desc <- do.call(rbind, lapply(names(inputs), function(n) {
  d <- inputs[[n]]
  data.frame(file = n, rows = nrow(d), cols = ncol(d), columns = paste(names(d), collapse = ", "),
             persons = length(unique(d$Personnr)), dup_personnr_rows = sum(duplicated(d$Personnr)),
             na_personnr = sum(is.na(d$Personnr) | d$Personnr == ""),
             cells_na = sum(is.na(d)))
}))
show(desc); save_csv(desc, "inputs_overview.csv")
na_cols <- do.call(rbind, lapply(names(inputs), function(n) {
  d <- inputs[[n]]
  data.frame(file = n, column = names(d), na = vapply(d, function(v) sum(is.na(v) | (is.character(v) & v == "")), 1))
}))
cat("\nMissing values by column:\n"); show(na_cols[na_cols$na > 0, ])
save_csv(na_cols, "inputs_missing_by_column.csv")
cat("\nNote: the cohort here is already restricted by line 46 (pregnant at start removed).\n")
if (ncol(inputs$births) != 3)
  cat("WARNING: delivery file does not have the 3 columns the positional drops at lines 40/64/79/95 assume.\n")

d2 <- inputs$dose2; d3 <- inputs$dose3
first_d2 <- with(aggregate(Exposuredatum ~ Personnr, d2, min), setNames(Exposuredatum, Personnr))
d3m <- merge(d2, d3, by = "Personnr")
rng <- function(x) paste(format(range(x, na.rm = TRUE)), collapse = " to ")
cat(sprintf("\nDose 2 dates: %s | before 2021-01-01: %d | after 2023-09-30: %d | NA: %d\n",
            rng(d2$Exposuredatum), sum(d2$Exposuredatum < START, na.rm = TRUE),
            sum(d2$Exposuredatum > SLUT, na.rm = TRUE), sum(is.na(d2$Exposuredatum))))
cat(sprintf("Dose 3 dates: %s | on/before own dose 2: %d\n", rng(d3$Censurdatum),
            sum(d3m$Censurdatum <= d3m$Exposuredatum, na.rm = TRUE)))
b <- inputs$births
cat(sprintf("Delivery dates in file: %s (paper: deliveries 2021-10-08 to 2024-07-06 used)\n",
            rng(b$Kontaktdatum)))
for (off in c(280, 266)) {
  idx <- b$Kontaktdatum - off
  m <- merge(data.frame(Personnr = b$Personnr, idx = idx), d2, by = "Personnr")
  cat(sprintf("  offset %d: index before 2021-01-01 (excluded as pregnant at start): %d | index == 2021-01-01: %d | index == dose-2 date: %d\n",
              off, sum(idx < START, na.rm = TRUE), sum(idx == START, na.rm = TRUE),
              sum(m$idx == m$Exposuredatum, na.rm = TRUE)))
}

# ---------------------------------------------------------------------------
# 1. Interval splitting
# ---------------------------------------------------------------------------
section("1. Interval splitting")
cat("tmerge() calls in script:", sum(grepl("tmerge", L)), "\n")
part1 <- function(offset, custom = NULL, full = FALSE) {
  run_part1(L, ROOT, offset = offset, custom_index = custom, hooks = CAPTURE,
            stop_before = if (full) NULL else LINE_MISSFALL_FILTER - 3L)
}
r280 <- part1(280, full = TRUE)
save_csv(r280$log, "trace_part1_offset280.csv")
comb <- r280$env$comb_before_128
comb$age <- comb[[AGE]]
inv <- check_intervals(comb[!is.na(comb$Personnr), ])
show(inv); save_csv(inv, "interval_invariants_280.csv")

elig <- unique(r280$env$data$Personnr); elig <- elig[!is.na(elig)]
bir <- r280$env[[NM_BIRTH]]
index <- data.frame(Personnr = bir$Personnr, idx_date = bir$Kontaktdatum)
index <- index[index$Personnr %in% elig & !is.na(index$idx_date), ]
dth <- r280$env[[NM_DEATH]]
dth <- data.frame(Personnr = dth$Personnr, dd = as.Date(dth$Avliden.datum))
dth <- dth[!is.na(dth$dd), ]
td <- build_tmerge(elig, index,
                   data.frame(Personnr = d2$Personnr, d2 = d2$Exposuredatum)[d2$Personnr %in% elig, ],
                   data.frame(Personnr = d3$Personnr, d3 = d3$Censurdatum), dth)
td$age <- inputs$cohort[[AGE]][match(td$Personnr, inputs$cohort$Personnr)]
cmp <- compare_datasets(comb[!is.na(comb$Personnr), ], td)
cat(sprintf("\nScript vs tmerge rows: identical %d | script-only %d | tmerge-only %d | persons differing %d\n",
            cmp$identical_rows, cmp$script_only, cmp$tmerge_only, length(cmp$persons_differing)))
dp <- cmp$persons_differing
coh <- inputs$cohort
cats <- data.frame(Personnr = dp,
  pre2021_dose2 = dp %in% names(first_d2)[first_d2 < START],
  dose2_after_end = dp %in% names(first_d2)[first_d2 > SLUT],
  dose3_le_dose2 = dp %in% d3m$Personnr[d3m$Censurdatum <= d3m$Exposuredatum],
  index_eq_dose2 = dp %in% merge(index, d2, by = "Personnr")$Personnr[
    with(merge(index, d2, by = "Personnr"), idx_date == Exposuredatum)],
  duplicated_input = dp %in% unlist(lapply(inputs[c("deaths", "births", "dose2", "dose3")],
                                           function(d) d$Personnr[duplicated(d$Personnr)])),
  no_birth_date = dp %in% bir$Personnr[is.na(bir$Kontaktdatum)],
  na_patientid = dp %in% coh$Personnr[is.na(coh$PatientID)],
  na_date_of_birth = dp %in% coh$Personnr[is.na(coh[[FOD]])])
cats$unexplained <- rowSums(cats[, -1]) == 0
cat("Differing persons by cause (a person can have several):\n")
print(colSums(cats[, -1])); save_csv(cats, "tmerge_differences_by_person.csv")
hr_tab <- data.frame(dataset = c("script (lines 22-123)", "tmerge rebuild"),
                     round(rbind(fit_hr(comb[!is.na(comb$Personnr), ]), fit_hr(td, "tstart", "tstop")), 4))
show(hr_tab); save_csv(hr_tab, "hr_script_vs_tmerge_280.csv")

pre <- names(first_d2)[first_d2 < START & names(first_d2) %in% elig]
cat(sprintf("\nWomen with dose 2 before entry (2021-01-01): %d; kept as unexposed for all follow-up: %d\n",
            length(pre), sum(pre %in% comb$Personnr & !pre %in% comb$Personnr[comb$exposure == 1])))
ks <- aggregate(cbind(status, endTime, exposure) ~ Personnr, comb, max)
cat(sprintf("'Ever exposed' person summary (script lines 162-167): Cox HR %.3f vs time-varying HR %.3f\n",
            exp(coef(coxph(Surv(endTime, status) ~ exposure, data = ks))), hr_tab$HR[1]))

# ---------------------------------------------------------------------------
# 2. Index-date arithmetic
# ---------------------------------------------------------------------------
section("2. Gestational age and index-date offset")
r266 <- part1(266)
ga <- NULL
if (!is.na(ga_path)) {
  ga <- utils::read.csv(ga_path, sep = Sys.getenv("GA_SEP", ";"), encoding = "latin1",
                        stringsAsFactors = FALSE)
  id_col <- Sys.getenv("GA_ID", "Personnr"); dt_col <- Sys.getenv("GA_DATE", "Forlossningsdatum")
  ga_col <- Sys.getenv("GA_DAYS", "GA_dagar")
  ga <- data.frame(Personnr = ga[[id_col]],
                   del = if (dt_col %in% names(ga)) as.Date(ga[[dt_col]]) else as.Date(NA),
                   ga = as.numeric(ga[[ga_col]]))
}
if (is.null(ga)) {
  cat("No gestational-age file supplied. The delivery extract read at line 36 holds\n")
  cat("Personnr, one dropped column and the delivery date only, so the raw GA distribution\n")
  cat("cannot be pulled from the script's inputs. Supply ga_file.csv (see header).\n")
} else {
  braw <- r280$env$births_raw
  m <- merge(data.frame(Personnr = braw$Personnr, del = braw$Kontaktdatum), ga,
             by = if (all(is.na(ga$del))) "Personnr" else c("Personnr", "del"), all.x = TRUE)
  cat(sprintf("Deliveries in script extract: %d | matched to a GA value: %d | GA missing: %d\n",
              nrow(braw), sum(!is.na(m$ga)), sum(is.na(m$ga))))
  q <- quantile(m$ga, c(0, .001, .01, .05, .25, .5, .75, .95, .99, .999, 1), na.rm = TRUE)
  cat("GA (days) quantiles:\n"); print(q)
  wk <- table(cut(m$ga, c(0, 154, 196, 224, 245, 259, 273, 287, 294, 400), right = FALSE))
  cat("GA by band (days, [lower, upper)):\n"); print(wk)
  save_csv(as.data.frame(table(ga_days = m$ga)), "ga_distribution_days.csv")
  cat(sprintf("Mean %.1f, SD %.1f | fixed 280 minus GA: mean %.1f, SD %.1f | |280 - GA| > 28 d: %.2f%%\n",
              mean(m$ga, na.rm = TRUE), sd(m$ga, na.rm = TRUE), mean(280 - m$ga, na.rm = TRUE),
              sd(280 - m$ga, na.rm = TRUE), 100 * mean(abs(280 - m$ga) > 28, na.rm = TRUE)))
}
dyn <- function(kind) function(env) {
  bb <- get(NM_BIRTH, envir = env)
  key <- if (all(is.na(ga$del))) match(bb$Personnr, ga$Personnr) else
    match(paste(bb$Personnr, bb$Kontaktdatum), paste(ga$Personnr, ga$del))
  g <- ga$ga[key]
  fallback <- if (kind == "lmp") 280 else 266
  off <- ifelse(is.na(g), fallback, if (kind == "lmp") g else g - 14)
  bb$Befruktningsdatum <- as.Date(bb$Kontaktdatum - off)
  assign(NM_BIRTH, bb, envir = env)
}
specs <- list(list("fixed 280 (paper primary)", r280),
              list("fixed 266 (paper sensitivity)", r266))
if (!is.null(ga)) specs <- c(specs, list(
  list("GA-based, LMP (delivery - GA)", part1("custom", dyn("lmp"))),
  list("GA-based, conception (delivery - GA + 14)", part1("custom", dyn("conc")))))
res <- do.call(rbind, lapply(specs, function(s) {
  cb <- s[[2]]$env$comb_before_128
  if (is.null(cb)) cb <- s[[2]]$env$comb
  cb <- cb[!is.na(cb$Personnr), ]; cb$age <- cb[[AGE]]
  a <- fit_hr(cb); u <- fit_hr(cb, adjust = FALSE)
  data.frame(index = s[[1]], persons = length(unique(cb$Personnr)), events = a[["events"]],
             crude_HR = u[["HR"]], crude_lo = u[["lo"]], crude_hi = u[["hi"]],
             adj_HR = a[["HR"]], adj_lo = a[["lo"]], adj_hi = a[["hi"]], t(ph_outputs(cb)))
}))
show(cbind(res[, 1:3], round(res[, -(1:3)], 4))); save_csv(res, "hr_by_index_definition.csv")
cat("Published (Table S4): 280 -> N 56,787, crude 0.94 (0.89-1.00), adjusted 1.03 (0.97-1.09);\n")
cat("                      266 -> N 56,935, crude 0.96 (0.90-1.02), adjusted 1.04 (0.98-1.11).\n")

# ---------------------------------------------------------------------------
# 3. Row counts and missingness through the miscarriage filters
# ---------------------------------------------------------------------------
section("3. Row-count trace and miscarriage filters")
show(r280$log[, c("line", "object", "rows", "persons", "phantom_na_rows", "code")])
if (any(!is.na(r280$log$error))) { cat("Errors:\n"); show(r280$log[!is.na(r280$log$error), ]) }
e <- r280$env; cb0 <- e$comb_before_128; mf <- e$Missfall
hit <- cb0$Personnr %in% mf$Personnr; real <- !is.na(cb0$Personnr)
mf_ok <- mf[!is.na(mf$Personnr) & !is.na(mf$Kontaktdatum), ]
pre_only <- setdiff(mf_ok$Personnr[mf_ok$Kontaktdatum < START], mf_ok$Personnr[mf_ok$Kontaktdatum >= START])
undated <- setdiff(mf$Personnr[!is.na(mf$Personnr) & is.na(mf$Kontaktdatum)], mf_ok$Personnr)
rm_p <- unique(cb0$Personnr[hit & real])
mtab <- data.frame(
  item = c("comb rows before line 128", "comb rows after line 128", "persons before", "persons after",
           "phantom all-NA rows before", "phantom all-NA rows after",
           "Missfall rows", "Missfall NA Personnr", "Missfall NA date",
           "real women removed", "  removed, all records before 2021-01-01", "  removed, only undated records",
           "  removed while carrying a childbirth event", "events before", "events after"),
  value = c(nrow(cb0), nrow(e$comb), length(unique(cb0$Personnr[real])),
            length(unique(e$comb$Personnr[!is.na(e$comb$Personnr)])), sum(!real), sum(is.na(e$comb$Personnr)),
            nrow(mf), sum(is.na(mf$Personnr)), sum(is.na(mf$Kontaktdatum)), length(rm_p),
            length(intersect(rm_p, pre_only)), length(intersect(rm_p, undated)),
            length(unique(cb0$Personnr[hit & real & cb0$status == 1])),
            sum(cb0$status, na.rm = TRUE), sum(e$comb$status, na.rm = TRUE)))
show(mtab); save_csv(mtab, "miscarriage_filter_line128.csv")
cat(sprintf("Published Model 1 N = 56,787. Persons before line 128: %d; after: %d.\n",
            mtab$value[3], mtab$value[4]))

cat("\nPart II (miscarriage outcome), run after Part I in the same session:\n")
run_part2 <- function(use_shifted) {
  env <- new.env(parent = e)
  hooks <- list(); skip <- integer()
  if (use_shifted) {
    skip <- 355L
    hooks[["354"]] <- function(x) x$test <- merge(x$test, x[[NM_FM]][, -c(2)], by = "Personnr", all.x = TRUE)
  }
  old <- setwd(ROOT); on.exit(setwd(old))
  lg <- run_traced(L, PART2_PREP[1], PART2_PREP[2], env, hooks = hooks, skip = skip,
                   watch = c("data", "test", "comb"))
  list(env = env, log = lg)
}
p2 <- list(as_deposited = run_part2(FALSE), shifted_FM21 = run_part2(TRUE))
p2tab <- do.call(rbind, lapply(names(p2), function(n) {
  cb <- p2[[n]]$env$comb; ok <- !is.na(cb$Personnr); cb$age <- cb[[AGE]]
  f <- fit_hr(cb[ok, ]); u <- fit_hr(cb[ok, ], adjust = FALSE)
  save_csv(p2[[n]]$log, paste0("trace_part2_", n, ".csv"))
  data.frame(variant = n, persons = length(unique(cb$Personnr[ok])), phantom_rows = sum(!ok),
             events = sum(cb$status[ok]), crude_HR = round(u[["HR"]], 3),
             adj_HR = round(f[["HR"]], 3), adj_lo = round(f[["lo"]], 3), adj_hi = round(f[["hi"]], 3))
}))
show(p2tab); save_csv(p2tab, "part2_variants.csv")
for (n in names(p2)) {
  cb <- p2[[n]]$env$comb
  cat("Interval invariants, Part II", n, ":\n"); show(check_intervals(cb[!is.na(cb$Personnr), ]))
}
cat("Published Model 2 (Table S4): N 59,661; crude 0.84 (0.69-1.03); adjusted 0.86 (0.70-1.05).\n")
cbs <- p2$shifted_FM21$env$comb; cbs <- cbs[!is.na(cbs$Personnr) & cbs$status == 1, ]
d2o <- first_d2[cbs$Personnr]
aft <- !is.na(d2o) & (cbs$Kontaktdatum + 154) > d2o
cat(sprintf("Shifted variant: miscarriages after the woman's dose 2: %d; classified exposed %d, unexposed %d\n",
            sum(aft), sum(aft & cbs$exposure == 1), sum(aft & cbs$exposure == 0)))
cat("\nOutputs written to:", OUT, "\n")
