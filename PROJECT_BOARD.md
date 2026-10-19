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
- [ ] README: each recording lists its tag
- [x] Inventory (below)
- [ ] Environment: `mamba env create -f environment.yml` (name `CompStats`)

**1. Runs in a current environment**
- [ ] `environment.yml` (Python 3.12, conda-forge, pytest, nbmake), `requirements.txt`, `requirements-dev.txt`
- [ ] First code cell installs what Colab lacks and downloads data and helper files if missing
- [ ] Fix breakage and deprecation warnings (run with warnings as errors); `pmf_intro` is Python 2.7
- [ ] Data URLs (the NSFG files are in the repo)
- [ ] Replace Binder and Anaconda instructions (`tutorial.md`) with Colab first, then pip or mamba

**2. Tests and CI**
- [ ] `pytest --nbmake` on the notebooks that should run top to bottom
- [ ] `.github/workflows/tests.yml`; watch the first run
- [ ] Status badge in the README

**3. Colab**
- [ ] "Click here to run this notebook on Colab" cell after each title (solutions link to the version with blanks); Colab links in the README
- [ ] Allen runs one notebook on Colab end to end

**4. Text**
- [ ] Typos, wrong docstrings, broken links (codespell, and read the markdown)
- [ ] Everything else under "Content issues"

**5. README in the standard shape**
- [ ] Title, badge, author, abstract, level and prerequisites, length (ask Allen), outline, notebook table, slides, recordings with tags, running instructions, next steps (*Think Stats*, hub), license

**6. Site and visibility**
- [ ] `jb/` (Jupyter Book 1, BayesMadeSimple as the template); the current site is the README via Jekyll (Pages from `master` /, `_config.yml`)
- [ ] SEO checklist in a test build; Allen reviews the descriptions
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
- Candidates, to confirm after step 1: `hypothesis.py` and `nsfg2.py` (scripts from *Think Stats*; no notebook imports them), `check_env.py` (old install check), `tutorial.md` (2017 install instructions, Binder), `_config.yml` (until the `jb/` site replaces it).
- `.gitignore` is the GitHub Python template; add `.ipynb_checkpoints/`.

**Local state not in git (discarded 2026-10-19, backups in the session scratchpad):**

- Uncommitted: `pmf_intro.ipynb` (an older Python 2 rewrite with `izip`, `urllib2`), Python-version metadata in `effect_size` and `resampling`, Inkscape edits to `resampling.svg` (2021) and `hypothesis_testing.svg` (2024), `_config.yml` deleted.
- Untracked: `.ipynb_checkpoints/`, `animal_farm.txt`, `doc185996775_448161735` (another copy of *The Fault in Our Stars*), `hypothesis_testing_backup.svg` (same as the committed SVG).

### Decisions (Allen, 2026-10-19)

- Local edits and untracked files discarded.
- The workshop is `effect_size`, `sampling`, `hypothesis` (student and solution), and `resampling`.
- Keep `pmf_intro`, `text_analysis`, `tumbleweed` as extras; delete `look_and_say`.
- Remove the copyrighted texts from `master` (no history rewrite).

### Content issues

(For Allen to decide.)

1. `text_analysis` and `pmf_intro` read the copyrighted texts that are being removed; they need public-domain replacements (e.g. Project Gutenberg) or a different example.
2. `resampling` has no student version; does it need one?
3. Licenses: `LICENSE` is MIT; the 2016 notebooks say CC BY 4.0, `text_analysis` says MIT.
4. The README describes the workshop only in one line; the abstract in `tutorial.md` links to the old blogspot blog and Think Stats URL.
