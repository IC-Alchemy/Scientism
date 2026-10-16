# Shared helpers for auditing the Nordvall et al. 2026 (Communications Medicine)
# analysis script, CommMedNordvall2025Rscript.txt (Zenodo 10.5281/zenodo.18138478, v1.0).
#
# Run under a UTF-8 locale, e.g.  LC_ALL=C.UTF-8 Rscript <file>.R
# The original script is CP1252-encoded, uses Swedish identifiers, and is a
# text document (prose header, two curly-quote lines), so it cannot be
# source()d. These helpers run selected line ranges of it verbatim, one
# top-level expression at a time, and log row counts after every expression.

suppressPackageStartupMessages(library(survival))

AGE   <- "\u00c5lderStartdatum"   # age at 2021-01-01
FOD   <- "F\u00f6delsedatum"      # date of birth
KON   <- "K\u00f6n"               # sex
START <- as.Date("2021-01-01")
SLUT  <- as.Date("2023-09-30")

# md5 of the Zenodo v1.0 file; line numbers below assume this exact file.
SCRIPT_MD5 <- "f6c85aa0f65fe4a69da1f726c0e77f13"

# Line ranges in the original file.
PART1_PREP   <- c(22L, 129L)   # cohort build through the miscarriage removal
PART2_PREP   <- c(321L, 413L)  # miscarriage-outcome cohort build
LINE_OFFSET_280 <- 38L         # Befruktningsdatum <- Kontaktdatum - 280
LINE_OFFSET_266 <- 39L         # Befruktningsdatum <- Kontaktdatum - 266 (overwrites 38)
LINE_MISSFALL_FILTER <- 128L   # comb <- comb[!(comb$Personnr %in% Missfall$Personnr),]

read_script_lines <- function(path) {
  if (!file.exists(path)) stop("Original script not found: ", path)
  md5 <- unname(tools::md5sum(path))
  if (!identical(md5, SCRIPT_MD5))
    warning("Script md5 ", md5, " differs from Zenodo v1.0 (", SCRIPT_MD5,
            "); line numbers may not match.")
  x <- readLines(path, warn = FALSE)
  x <- iconv(x, from = "CP1252", to = "UTF-8")
  sub("\r$", "", x)
}

fetch_script_from_zenodo <- function(dest_dir = tempdir()) {
  zip <- file.path(dest_dir, "VaccEval-v1.0.zip")
  utils::download.file(
    "https://zenodo.org/api/records/18138478/files/Tooti02/VaccEval-v1.0.zip/content",
    zip, mode = "wb", quiet = TRUE)
  files <- utils::unzip(zip, exdir = dest_dir)
  files[basename(files) == "CommMedNordvall2025Rscript.txt"][1]
}

# ---------------------------------------------------------------------------
# Traced execution
# ---------------------------------------------------------------------------

WATCH <- c("data", "grav", "test", "sista", "comb", "pat")

snapshot <- function(env, watch) {
  vapply(watch, function(nm) {
    if (!exists(nm, envir = env, inherits = FALSE)) return(c(NA_real_, NA_real_, NA_real_))
    d <- get(nm, envir = env, inherits = FALSE)
    if (!is.data.frame(d)) return(c(NA_real_, NA_real_, NA_real_))
    pn <- if ("Personnr" %in% names(d)) d$Personnr else rep(NA, nrow(d))
    c(nrow(d), length(unique(pn[!is.na(pn)])), sum(rowSums(!is.na(d)) == 0))
  }, numeric(3))
}

# Evaluate lines[from:to] of the original script in `env`, one top-level
# expression at a time. `hooks` is a named list (names = source line numbers)
# of functions(env) run right after that line; `skip` lists line numbers not
# to evaluate. Returns a log with one row per watched object whose row count,
# person count or phantom-row count changed, plus any error raised.
run_traced <- function(lines, from, to, env, hooks = list(), skip = integer(),
                       watch = WATCH, stop_on_error = FALSE, quiet = TRUE) {
  exprs <- parse(text = lines[from:to], keep.source = TRUE)
  sr <- attr(exprs, "srcref")
  out <- list()
  prev <- snapshot(env, watch)
  for (k in seq_along(exprs)) {
    ln <- from - 1L + sr[[k]][1]
    if (ln %in% skip) next
    err <- tryCatch({
      if (quiet) utils::capture.output(eval(exprs[[k]], envir = env)) else eval(exprs[[k]], envir = env)
      NA_character_
    }, error = function(e) conditionMessage(e))
    h <- hooks[[as.character(ln)]]
    if (!is.null(h)) h(env)
    cur <- snapshot(env, watch)
    for (j in seq_along(watch)) {
      if (!identical(cur[, j], prev[, j]))
        out[[length(out) + 1L]] <- data.frame(
          line = ln, object = watch[j], rows = cur[1, j], persons = cur[2, j],
          phantom_na_rows = cur[3, j], error = NA_character_,
          code = substr(trimws(lines[ln]), 1, 72), stringsAsFactors = FALSE)
    }
    if (!is.na(err)) {
      out[[length(out) + 1L]] <- data.frame(
        line = ln, object = NA, rows = NA, persons = NA, phantom_na_rows = NA,
        error = err, code = substr(trimws(lines[ln]), 1, 72), stringsAsFactors = FALSE)
      if (stop_on_error) break
    }
    prev <- cur
  }
  if (length(out)) do.call(rbind, out) else NULL
}

# Run Part I data preparation (lines 22-129) inside directory `root`, which
# must contain the input files at the script's own relative paths
# ("H:/Dokument/..."). offset = 280 or 266 selects which of lines 38/39 runs
# last; offset = "custom" keeps line 39 and then calls custom_index(env).
run_part1 <- function(lines, root, offset = 280, custom_index = NULL,
                      stop_before = NULL, hooks = list()) {
  env <- new.env(parent = globalenv())
  old <- setwd(root); on.exit(setwd(old))
  skip <- integer()
  if (identical(offset, 280)) skip <- LINE_OFFSET_266
  if (!is.null(custom_index)) hooks[[as.character(LINE_OFFSET_266)]] <- custom_index
  to <- if (is.null(stop_before)) PART1_PREP[2] else stop_before - 1L
  log <- run_traced(lines, PART1_PREP[1], to, env, hooks = hooks, skip = skip)
  list(env = env, log = log)
}

# ---------------------------------------------------------------------------
# Interval checks on the script's counting-process dataset (comb)
# ---------------------------------------------------------------------------

check_intervals <- function(comb) {
  comb <- comb[order(comb$Personnr, comb$startTime), ]
  by_p <- split(seq_len(nrow(comb)), comb$Personnr)
  n_rows <- lengths(by_p)
  first <- vapply(by_p, `[`, 1L, 1L)
  last  <- vapply(by_p, function(i) i[length(i)], 1L)
  gap_or_overlap <- 0L
  multi <- by_p[n_rows > 1]
  for (i in multi)
    gap_or_overlap <- gap_or_overlap + sum(comb$startTime[i[-1]] != comb$endTime[i[-length(i)]])
  ev_per_p <- vapply(by_p, function(i) sum(comb$status[i]), 1)
  ev_not_last <- sum(comb$status[-last] == 1)
  exposed_then_unexposed <- sum(vapply(multi, function(i) any(diff(comb$exposure[i]) < 0), TRUE))
  data.frame(
    check = c("rows", "persons", "rows with startTime < 0 (exposure or entry before 2021-01-01)",
              "rows with endTime <= startTime", "persons whose first row is not at time 0",
              "gaps/overlaps between consecutive rows of a person",
              "persons with >1 event", "events on a non-final row",
              "persons going exposed -> unexposed", "persons with >2 rows",
              "rows ending after study end (day 1002 = 2023-09-30)"),
    value = c(nrow(comb), length(by_p), sum(comb$startTime < 0),
              sum(comb$endTime <= comb$startTime), sum(comb$startTime[first] != 0),
              gap_or_overlap, sum(ev_per_p > 1), ev_not_last,
              exposed_then_unexposed, sum(n_rows > 2),
              sum(comb$endTime > as.integer(SLUT - START))),
    stringsAsFactors = FALSE)
}

# Rebuild the same counting-process dataset with survival::tmerge(), from the
# eligible cohort the script itself used (env after line 61), so that only the
# interval-splitting step differs.
#   index : data.frame(Personnr, idx_date)  estimated conception (index) date
#   dose2 : data.frame(Personnr, d2)        dose-2 date
#   dose3 : data.frame(Personnr, d3)        dose-3 date
#   death : data.frame(Personnr, dd)        death date
build_tmerge <- function(persons, index, dose2, dose3, death) {
  b <- data.frame(Personnr = persons, stringsAsFactors = FALSE)
  day <- function(d) as.integer(d - START)
  m <- function(x, y) merge(x, y, by = "Personnr", all.x = TRUE)
  b <- m(b, aggregate(dd ~ Personnr, death, min))
  b <- m(b, aggregate(d3 ~ Personnr, dose3, min))
  b <- m(b, index)
  b$end <- pmin(day(SLUT), day(b$dd), day(b$d3), na.rm = TRUE)
  b$idx <- day(b$idx_date)
  b$stop <- ifelse(!is.na(b$idx) & b$idx <= b$end, b$idx, b$end)
  b <- b[b$stop > 0, ]
  td <- tmerge(b[, "Personnr", drop = FALSE], b, id = Personnr, tstart = 0, tstop = stop)
  ev <- b[!is.na(b$idx) & b$idx <= b$end & b$idx > 0, c("Personnr", "idx")]
  td <- tmerge(td, ev, id = Personnr, status = event(idx))
  d2 <- dose2[!is.na(dose2$d2), ]
  d2$t2 <- day(d2$d2)
  td <- tmerge(td, d2, id = Personnr, exposure = tdc(t2))
  td$exposure[is.na(td$exposure)] <- 0
  td
}

compare_datasets <- function(comb, td) {
  a <- data.frame(Personnr = comb$Personnr, start = comb$startTime, stop = comb$endTime,
                  status = comb$status, exposure = comb$exposure)
  b <- data.frame(Personnr = td$Personnr, start = td$tstart, stop = td$tstop,
                  status = td$status, exposure = td$exposure)
  # Row multisets per person: duplicated rows count as differences.
  key <- function(d) paste(d$Personnr, d$start, d$stop, d$status, d$exposure)
  ta <- table(key(a)); tb <- table(key(b))
  k <- union(names(ta), names(tb))
  na_ <- as.integer(ta[k]); nb_ <- as.integer(tb[k])
  na_[is.na(na_)] <- 0L; nb_[is.na(nb_)] <- 0L
  diff_p <- sort(unique(sub(" .*", "", k[na_ != nb_])))
  list(identical_rows = sum(pmin(na_, nb_)), script_only = sum(pmax(na_ - nb_, 0L)),
       tmerge_only = sum(pmax(nb_ - na_, 0L)), persons_differing = diff_p)
}

fit_hr <- function(d, start = "startTime", stop = "endTime", adjust = TRUE) {
  f <- if (adjust) "exposure + age" else "exposure"
  fo <- as.formula(sprintf("Surv(%s, %s, status) ~ %s", start, stop, f))
  m <- coxph(fo, data = d)
  ci <- exp(confint.default(m)["exposure", ])
  c(HR = unname(exp(coef(m)["exposure"])), lo = unname(ci[1]), hi = unname(ci[2]),
    events = m$nevent)
}

# Schoenfeld test p-value for exposure and the three calendar-period HRs the
# paper reports (Table S4: cuts at day 212 and 365, as in script lines 229-235).
ph_outputs <- function(d, start = "startTime", stop = "endTime") {
  fo <- as.formula(sprintf("Surv(%s, %s, status) ~ exposure + age", start, stop))
  m <- coxph(fo, data = d)
  z <- cox.zph(m)$table["exposure", "p"]
  d2 <- d; d2$t0 <- d2[[start]]; d2$t1 <- d2[[stop]]
  sp <- survSplit(Surv(t0, t1, status) ~ exposure + age, data = d2, cut = c(212, 365),
                  episode = "tgroup")
  per <- vapply(1:3, function(g) exp(coef(coxph(Surv(t0, t1, status) ~ exposure + age,
                                                 data = sp[sp$tgroup == g, ]))["exposure"]), 1)
  c(zph_p_exposure = unname(z), HR_0_212 = per[1], HR_213_365 = per[2], HR_366_end = per[3])
}
