# CompStats

Allen Downey's tutorial "Computational Statistics": statistical inference with resampling and simulation in Python (effect sizes, sampling distributions, hypothesis testing). Given at PyCon US 2015 and 2016 and SciPy 2015 and 2017. The README is also the GitHub Pages site (`allendowney.github.io/CompStats/`, Jekyll minimal theme via `_config.yml`).

**Guide for the 2026 refresh:** the "Refresh checklist" in `~/GreenTeaPress/plans/workshops.md` (BayesMadeSimple is the worked example). Progress goes on `PROJECT_BOARD.md` here (Task 1) and in GreenTeaPress Task 24.

## Which notebooks are the workshop

- `effect_size.ipynb` / `effect_size_soln.ipynb`
- `sampling.ipynb` / `sampling_soln.ipynb`
- `hypothesis.ipynb` / `hypothesis_soln.ipynb` (imports `first.py`, which uses `nsfg.py`, `thinkstats2.py`, `thinkplot.py` and the NSFG files `2002FemPreg.*`)
- `resampling.ipynb` (2018; no student version)

Extras, not part of the workshop: `pmf_intro.ipynb`, `text_analysis.ipynb`, `tumbleweed.ipynb`.

## Tags

- `pycon-2015`, `scipy-2015`, `pycon-2016`, `scipy-2017`: the code in each recording (the last commit before the event).
- `pre-refresh-2026`: the state before the 2026 refresh.

## Testing

Environment: `mamba env create -f environment.yml` (name `CompStats`). To be set up in step 2 of the refresh: `pytest --nbmake` on the notebooks that run top to bottom.
