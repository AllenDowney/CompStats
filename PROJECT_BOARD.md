# CompStats Project Board

Numbered tasks for tracking work. Each task has a permanent number; add new tasks at the end. Update status as work progresses.

**Status values:** `Pending`, `In progress`, `DONE`

---

## Task 1: Refresh

**Status:** In progress (2026-10-19)

**Context:** CompStats is a "current" workshop (GreenTeaPress Task 24). The guide is the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md`; BayesMadeSimple is the worked example. 223 stars; last content change 2021-03-08. The most recent recording is [SciPy 2017](https://www.youtube.com/watch?v=He9MCbs1wgE).

**0. Set up**
- [x] `git fetch`, pulled one commit (README: venues, recordings); local edits listed and discarded (Inventory, below), backed up to the session scratchpad (2026-10-19)
- [x] `PROJECT_BOARD.md` and `CLAUDE.md` (2026-10-19)
- [x] Tags created locally (2026-10-19): `pycon-2015` at `3881760` (2015-04-03, "Updating for PyCon 2015"), `scipy-2015` at `78e946e` (2015-06-23), `pycon-2016` at `f26bc0a` (2016-05-24), `scipy-2017` at `9fdd22e` (2017-07-10; the notebooks are the same from `8371d79`, 2017-07-08, through `9fdd22e`, so the exact tutorial day doesn't matter; the 2017-07-14 "Fixing problem with interactions" came after), `pre-refresh-2026` at `64ee4bd`
- [x] Tags pushed (2026-10-19)
- [x] README: each recording lists its tag
- [x] Inventory (below)
- [x] Environment: `mamba env create -f environment.yml` (name `CompStats`; Python 3.12.15, NumPy 2.5, pandas 3.0, SciPy 1.18, Matplotlib 3.11, seaborn 0.13, ipywidgets 8.1)

**1. Runs in a current environment**
- [x] `environment.yml` (Python 3.12, conda-forge, Jupyter, ipywidgets, the scientific stack, pytest, nbmake), `requirements.txt` (unpinned; Colab has everything), `requirements-dev.txt` (2026-10-19)
- [x] First code cell downloads the data files from the repo if missing (`hypothesis`, `resampling`, `pmf_intro`, `text_analysis`); nothing to install. `effect_size`, `sampling`, `tumbleweed` need no cell. Tested in an empty directory with `pmf_intro`; the others need the new files pushed first
- [x] Breakage and warnings, found with scratch runs with warnings as errors:
  - NumPy 2 removed `np.int`/`np.float`, used in the copy of `thinkstats2.py` (`hypothesis`, `resampling`, `pmf_intro`)
  - pandas 3: `nsfg.CleanFemPreg` used chained `df.col.replace(..., inplace=True)`, which now does nothing, so the 97/98/99 codes stayed in `birthwgt_oz` and the mean birth weights were off (7.22/7.36 lb instead of the book's 7.20/7.33)
  - Fix (Allen: inline the code): `read_stata_dct` and `read_fem_preg` in a cell in each notebook that reads the NSFG; `first.py`, `nsfg.py`, `nsfg2.py`, `hypothesis.py`, `thinkstats2.py`, `thinkplot.py`, `check_env.py` deleted
  - `pmf_intro` ported to Python 3 (`izip` → `zip`, `iteritems` → `items`, kernel metadata)
  - All notebooks now run with no errors or warnings, except the exercise blanks in `sampling.ipynb` (`StdResampler`) and `hypothesis.ipynb` (`DiffStdPermute`), which are expected (step 2: `raises-exception`)
- [x] Data: `resampling` read `LLCP2016.HDF`, which was never in the repo. Now `brfss2016_subset.csv.gz` (BRFSS 2016, 4 columns, 486,303 rows, 5.7 MB) is in the repo, made from the CDC file (https://www.cdc.gov/brfss/annual_data/2016/files/LLCP2016XPT.zip) by `read_brfss()` in the notebook. `text_analysis` uses `pg42671.txt` (*Pride and Prejudice*, Gutenberg, R. W. Chapman edition; #1342 has "Copyright 1894 by George Allen" captions that top the trigram counts), and its `d['I', 'said']` example is now `d['Mr.', 'Darcy']`. `pmf_intro` loses the commented-out Elvis line
- [x] Binder and Anaconda instructions replaced: `tutorial.md` deleted; its abstract is in the README, with Colab first, then pip or mamba (2026-10-19)

**2. Tests and CI**
- [x] `pytest --nbmake *.ipynb`: all 10 notebooks, student versions too; the two cells with exercise blanks (`sampling`: `StdResampler`; `hypothesis`: `DiffStdPermute`) are tagged `raises-exception` (2026-10-19). About 2 minutes
- [x] `.github/workflows/tests.yml` (push to master, PR, monthly, manual; Python 3.12; pip; 20-minute timeout; checkout@v5, setup-python@v6). First run passed: https://github.com/AllenDowney/CompStats/actions/runs/39333749191
- [x] Status badge in the README

**3. Colab**
- [x] "Click here to run this notebook on Colab" cell after each title, all 10 notebooks; solutions also link to the version with blanks (2026-10-19)
- [x] Colab links in the README's notebook table (step 5)
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [x] Typos, wrong docstrings, broken links (codespell, and read all the markdown; 2026-10-19), in both versions where there are two:
  - effect_size: "takes and rv object"
  - hypothesis: "Exercize", "signficance"
  - sampling: "sample standard mean" → "sample mean", "also considering resampling" → "considered"
  - pmf_intro: `pregorder` → `pregordr` (the variable), "samples sizes", stray quote in the Gutenberg URL
  - resampling: "Getting get back", "computaton", "these weight", "by a one of … and 244, one for each variable", `prglength` → `prglngth`, "about 0.78 weeks" → 0.078 (13 hours), "13 about hours", "pregnancies lengths in one groups", "test statistics" → "test statistic", list numbered 1-4, 4, 5 → 1-6, "these is", "suprising", "is would not", `TestStat` → `test_stat` (the method)
  - text_analysis: Zipf counts updated for *Pride and Prejudice* (4230, 4117, 3689)
  - tumbleweed: "suprising", docstring "return:" → "returns:"
  - Links: http → https (Creative Commons, ColorBrewer, CDC BRFSS, Wikipedia, Gutenberg), opensource.org MIT license URL updated to its new address
  - The numbers quoted in the text (p-values, differences) still match fresh runs
- [x] Everything else under "Content issues"

**5. README in the standard shape**
- [x] README rewritten (2026-10-19): abstract (from `tutorial.md`, Olin class dropped), level (beginner, Allen), length (3 hours, Allen), outline with `resampling` as part 4 (Allen), Colab table, slides (Google Slides, Allen), extras, data sources, recordings with tags, running instructions, next steps (*Think Stats*, hub), license (MIT, the `LICENSE` file; see Content issues 3)

**6. Site and visibility**
- [x] `jb/` (Jupyter Book 1, 2026-10-19): `build.sh [publish]` runs `prep_notebooks.py` (copies the solution notebooks in without `_soln`, the other notebooks as they are, and the data files; makes the title the only H1, setext → ATX, "Part …" headings → H2, "STOP HERE" → bold; adds the page descriptions) and `jb build` (executes the notebooks, about 2 minutes). TOC: "The workshop" (4 pages) and "Extras" (3). Build tools in `environment.yml` (`mamba env update` timed out after 20 minutes; `mamba install` of the four packages worked in seconds). The current site is still the README via Jekyll (Pages from `master` /, `_config.yml`)
- [x] SEO checklist in a test build (scratch copy): sitemap lists only the 8 pages; each page has one description, one `og:description`, `rel="canonical"`; landing H1 "Computational Statistics: A Tutorial in Python" differs from the site title; page-view counter in `extra_footer`; social image is the *Think Stats* 3e cover; no cell errors
- [ ] Allen reviews the eight descriptions (`jb/index.md` front matter, `jb/prep_notebooks.py`)
- [ ] Publish, switch Pages to `gh-pages`, delete the root `_config.yml`; `Sitemap:` line in `~/AllenDowney.github.io/robots.txt`; Search Console; GreenTeaPress Task 22
- [ ] Hub entry, repo description and topics

**7. Close**
- [ ] Tag `2026-refresh`; note in GreenTeaPress Task 24

### Inventory (2026-10-19)

**The workshop (Allen, 2026-10-19): the three 2015–2017 notebooks plus `resampling`.**

| Notebook | Topic | Imports, files |
|---|---|---|
| `effect_size` / `effect_size_soln` | Effect size (height distributions), Cohen's d | numpy, scipy.stats, matplotlib, ipywidgets |
| `sampling` / `sampling_soln` | Sampling distributions, standard error, confidence intervals | same |
| `hypothesis` / `hypothesis_soln` | Hypothesis testing by simulation (NSFG pregnancy lengths) | + `first.py` → `nsfg.py`, `thinkstats2.py`, `thinkplot.py`; `2002FemPreg.dct`, `2002FemPreg.dat.gz` |
| `resampling` (2018, no student version) | "Teaching statistical inference with resampling" | numpy, pandas, matplotlib, `nsfg.py` (+ `thinkstats2`); NSFG files; figures `resampling.png`, `hypothesis_testing.png` (and `_small`, `.svg`, `.pdf`, 2021) |

All notebooks use `from __future__ import …`; kernel metadata says Python 3.6. Student and solution versions of the three are saved without outputs.

**Extras (kept, Allen 2026-10-19):**

- `pmf_intro.ipynb` (2015, Python 2.7 kernel; `thinkstats2`, seaborn): uses `lyrics-elvis-presley.txt`, `pg2591.txt` (Grimm's fairy tales, Project Gutenberg), `cumulative_snowfall.png`, and the NSFG files. Needs porting to Python 3.
- `text_analysis.ipynb` (2019): uses `the_fault_in_our_stars.txt`.
- `tumbleweed.ipynb` ("There is only one test", 2018): numpy, matplotlib.

**Leftovers (to delete from `master`; they stay in the tags and history):**

- `look_and_say.ipynb` (2019, not related to the workshop).
- `the_fault_in_our_stars.txt` and `lyrics-elvis-presley.txt` (copyrighted texts; see Content issues 1).
- Deleted in step 1 (2026-10-19): `look_and_say.ipynb`, the two copyrighted texts, `cumulative_snowfall.png` (unused), the helper modules and scripts (above).
- `tutorial.md` deleted in step 5. Still to go: `_config.yml` (when the `jb/` site replaces it).
- `.gitignore`: `.ipynb_checkpoints/` added.

**Local state not in git (discarded 2026-10-19, backups in the session scratchpad):**

- Uncommitted: `pmf_intro.ipynb` (an older Python 2 rewrite with `izip`, `urllib2`), Python-version metadata in `effect_size` and `resampling`, Inkscape edits to `resampling.svg` (2021) and `hypothesis_testing.svg` (2024), `_config.yml` deleted.
- Untracked: `.ipynb_checkpoints/`, `animal_farm.txt`, `doc185996775_448161735` (another copy of *The Fault in Our Stars*), `hypothesis_testing_backup.svg` (same as the committed SVG).

### Decisions (Allen, 2026-10-19)

- Local edits and untracked files discarded.
- The workshop is `effect_size`, `sampling`, `hypothesis` (student and solution), and `resampling`.
- Keep `pmf_intro`, `text_analysis`, `tumbleweed` as extras; delete `look_and_say`.
- Remove the copyrighted texts from `master` (no history rewrite).
- BRFSS: a 4-column subset in the repo. Helpers: inline the code in the notebooks. `text_analysis`: *Pride and Prejudice*. `pmf_intro`: the Grimm text instead of the lyrics.

### Content issues

(For Allen to decide.)

1. Resolved 2026-10-19: the copyrighted texts replaced (Decisions).
2. Resolved 2026-10-19 (Allen): `resampling` stays a demo, with no student version.
3. Resolved 2026-10-19 (Allen): MIT everywhere; notebook headers changed from CC BY 4.0, copyright years now e.g. "2016–2026".
4. Resolved 2026-10-19: README rewritten.
5. `text_analysis` has no explanation of the new example text; the markdown just says "an example using a book". The Gutenberg header and license text are included in the counts (as with `pg2591.txt` in `pmf_intro`).
6. Resolved 2026-10-19 (Allen): `from __future__` imports removed.
7. `resampling` says it reads "the most recent data from BRFSS (2016)"; the latest BRFSS is much newer.
8. `pmf_intro` and `tumbleweed` link to the old blogspot posts (`allendowney.blogspot.com`, still working); `pmf_intro` says the first-babies post is "still the most popular, with more than 100,000 page views".
9. `tumbleweed`: the 2019 AP Statistics exam PDF is gone (the URL redirects to the College Board's past exam questions page); no obvious replacement.
10. `pmf_intro`: introduces the "cumulative mass function (CMF)", then calls the curves CDFs.
11. `pmf_intro` and `text_analysis`: "reads lines from a file or URL", but `iterate_words` reads only files.
12. `sampling` ends: "permutation tests, which we'll see in the next section", which is in another notebook (`hypothesis`).
13. `resampling` has two headings "Different test statistics" and "Different test statistic"; `hypothesis` has "Part four" vs "Part One/Two/Three", and mixes `===` and `##` heading styles.
