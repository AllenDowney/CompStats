---
myst:
  html_meta:
    description: "A beginner's tutorial on computational statistics in Python: effect size, sampling distributions, and hypothesis testing with simulation and resampling."
og:description: "A beginner's tutorial on computational statistics in Python: effect size, sampling distributions, and hypothesis testing with simulation and resampling."
---

# Computational Statistics: A Tutorial in Python

[Allen Downey](https://allendowney.com)

Do you know the difference between standard deviation and standard error? Do you know what statistical test to use for any occasion? Do you really know what a p-value is? How about a confidence interval?

Most people don't really understand these concepts, even after taking several statistics classes. The problem is that these classes focus on mathematical methods that bury the concepts under a mountain of details.

This tutorial uses Python to implement simple statistical experiments that develop deep understanding: effect sizes, sampling distributions, and hypothesis testing with resampling and simulation. The examples use real-world data to answer relevant questions, and you will practice with hands-on exercises.

It is based on my book, [*Think Stats*](https://allendowney.github.io/ThinkStats/), and my blog, [*Probably Overthinking It*](https://allendowney.com/blog).

**Level:** beginner. You should be comfortable with basic Python; some experience with NumPy helps. You don't need any background in statistics.

**Length:** about 3 hours.

## The notebooks

The pages on this site show the notebooks with solutions. To do the exercises, run the versions with blanks on Colab:

1. [Effect size](effect_size): the difference in height between men and women, described as a difference in means, as overlap, as "probability of superiority", and as Cohen's *d*. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/effect_size.ipynb)
2. [Random sampling](sampling): sampling distributions, standard errors, and confidence intervals, by simulation and by resampling. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/sampling.ipynb)
3. [Hypothesis testing](hypothesis): are first babies more likely to be late? Permutation tests, p-values, p-hacking, and statistical power. [Exercises on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/hypothesis.ipynb)
4. [Resampling](resampling): the whole approach in one notebook, with the Euro problem, estimating average height, and first babies again. [Run on Colab](https://colab.research.google.com/github/AllenDowney/CompStats/blob/master/resampling.ipynb)

[Slides for this tutorial are here](https://docs.google.com/presentation/d/e/2PACX-1vRe63FWi5zgPrQ3MMeCsREmmZM8tHQqKYcTQRlIS9TlA28c_jXlQcQD9Tv9kGs6c5cqcd7_Opq-JYxD/pub).

The extras use the same ideas: [an introduction to PMFs](pmf_intro), [text analysis](text_analysis) with *Pride and Prejudice*, and [There is only one test](tumbleweed), a problem from the AP Statistics exam solved by simulation.

## Recordings

I presented this tutorial at PyCon US 2015 and 2016 and at SciPy 2015 and 2017. The most recent recording is from [SciPy 2017](https://www.youtube.com/watch?v=He9MCbs1wgE). The code in the videos is an earlier version; the [repository README](https://github.com/AllenDowney/CompStats) lists the version that goes with each video.

## Next steps

To go further, read [*Think Stats*](https://allendowney.github.io/ThinkStats/), which is free online, or see [my other workshops](https://allendowney.github.io/#workshops).

The code is on [GitHub](https://github.com/AllenDowney/CompStats), under the MIT License.
