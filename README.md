# Computational Statistics

[![tests](https://github.com/AllenDowney/CompStats/actions/workflows/tests.yml/badge.svg)](https://github.com/AllenDowney/CompStats/actions/workflows/tests.yml)

[Allen Downey](https://allendowney.com)

Do you know the difference between standard deviation and standard error? Do you know what statistical test to use for any occasion? Do you really know what a p-value is? How about a confidence interval?

Most people don't really understand these concepts, even after taking several statistics classes. The problem is that these classes focus on mathematical methods that bury the concepts under a mountain of details.

This tutorial uses Python to implement simple statistical experiments that develop deep understanding: effect sizes, sampling distributions, and hypothesis testing with resampling and simulation. The examples use real-world data to answer relevant questions, and you will practice with hands-on exercises.

It is based on my book, [*Think Stats*](https://allendowney.github.io/ThinkStats/), and my blog, [*Probably Overthinking It*](https://allendowney.com/blog).

This is one of [my workshops and tutorials](https://allendowney.github.io/#workshops).

**Level:** beginner. You should be comfortable with basic Python; some experience with NumPy helps. You don't need any background in statistics.

**Length:** about 3 hours.

## Outline

1. **Effect size:** the difference in height between men and women, described as a difference in means, as overlap, as "probability of superiority", and as Cohen's *d*.
2. **Random sampling:** sampling distributions, standard errors, and confidence intervals, first by simulating experiments from a known population, then by resampling (bootstrapping) from the sample itself.
3. **Hypothesis testing:** are first babies more likely to be late? A permutation test and its p-value, a framework for hypothesis tests, and simulations of p-hacking and statistical power.
4. **Resampling:** the whole approach in one notebook. The Euro problem (is a coin that comes up heads 140 times in 250 spins biased?), estimating average height with weighted resampling, and first babies again with several test statistics.

Parts 1–3 come in two versions: one with blanks for the exercises, and one with solutions.

| Notebook | Exercises | Solutions |
|---|---|---|
| 1. Effect size | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/effect_size.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/effect_size_soln.ipynb) |
| 2. Random sampling | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/sampling.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/sampling_soln.ipynb) |
| 3. Hypothesis testing | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/hypothesis.ipynb) | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/hypothesis_soln.ipynb) |
| 4. Resampling | | [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/resampling.ipynb) |

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vRe63FWi5zgPrQ3MMeCsREmmZM8tHQqKYcTQRlIS9TlA28c_jXlQcQD9Tv9kGs6c5cqcd7_Opq-JYxD/pub).

### Extras

These notebooks are not part of the workshop, but they use the same ideas:

* [Introduction to PMFs](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/pmf_intro.ipynb): histograms and probability mass functions, with dice, first babies, and word frequencies in Grimm's fairy tales.
* [Text analysis](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/text_analysis.ipynb): Zipf's law, n-grams, and random text generated from *Pride and Prejudice*.
* [There is only one test](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/tumbleweed.ipynb): a problem from the 2019 AP Statistics exam, solved by simulation.

### Data

* Pregnancy data from the [National Survey of Family Growth](https://www.cdc.gov/nchs/nsfg/index.htm) (NSFG), 2002: `2002FemPreg.dct` and `2002FemPreg.dat.gz`.
* Height and weight from the [Behavioral Risk Factor Surveillance System](https://www.cdc.gov/brfss/index.html) (BRFSS), 2016: `brfss2016_subset.csv.gz` has the four columns the notebook uses; `resampling.ipynb` shows how it was made from the original.
* Texts from [Project Gutenberg](https://www.gutenberg.org/): `pg2591.txt` (Grimm's fairy tales) and `pg42671.txt` (*Pride and Prejudice*).

## Recordings

I presented this tutorial at PyCon US 2015 and 2016 and at SciPy 2015 and 2017. The code in the videos is not the current version; the tag after each link is the version of the code that goes with it.

* [SciPy 2017](https://www.youtube.com/watch?v=He9MCbs1wgE): tag [`scipy-2017`](https://github.com/AllenDowney/CompStats/tree/scipy-2017)
* [PyCon 2016](https://www.youtube.com/watch?v=VR52vSbHBAk): tag [`pycon-2016`](https://github.com/AllenDowney/CompStats/tree/pycon-2016)
* [SciPy 2015](https://www.youtube.com/watch?v=fMycLa1bsno): tag [`scipy-2015`](https://github.com/AllenDowney/CompStats/tree/scipy-2015)
* [PyCon 2015](https://www.youtube.com/watch?v=5Vjrqnk7Igs): tag [`pycon-2015`](https://github.com/AllenDowney/CompStats/tree/pycon-2015)

## Running the notebooks

The easiest way to run the notebooks is on Colab: click one of the links above. You need a Google account, but you don't have to install anything. The notebooks download the data files they need.

To run them on your own computer, you need Python 3 with Jupyter, NumPy, pandas, SciPy, Matplotlib, Seaborn, and ipywidgets. You can [download the code in this zip file](https://github.com/AllenDowney/CompStats/archive/master.zip), or clone the repository:

```
git clone https://github.com/AllenDowney/CompStats
cd CompStats
```

Then install the packages with pip:

```
pip install -r requirements.txt
```

Or, if you use conda or mamba, create an environment:

```
mamba env create -f environment.yml
mamba activate CompStats
```

Then run `jupyter lab` and open `effect_size.ipynb`.

## Next steps

To go further, read [*Think Stats*](https://allendowney.github.io/ThinkStats/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

## License

The code is available under the [MIT License](LICENSE). The text is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
