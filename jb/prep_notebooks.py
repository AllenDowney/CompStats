"""Copy the notebooks and data files into jb/ and prepare the notebooks for the book.

For the workshop parts with exercises, ../name_soln.ipynb becomes name.ipynb here
(so the page URL has no _soln); the other notebooks are copied as they are. Then:
- the title becomes the page's only H1, and setext headings ("Part One\\n====") become ATX;
- "Part ..." headings become H2, wherever they were (some were H1, some H3);
- "STOP HERE" headings, which are for the live workshop, become bold text;
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).
"""

import re
import shutil

import nbformat

DESCRIPTIONS = {
    'effect_size': "Quantify effect size in Python with the difference in height between men and women: "
                   "difference in means, overlap, probability of superiority, and Cohen's d.",
    'sampling': "Sampling distributions, standard errors, and confidence intervals in Python, "
                "by simulating experiments and by resampling (bootstrapping) from the data.",
    'hypothesis': "Hypothesis testing by simulation in Python: are first babies more likely to be late? "
                  "Permutation tests, p-values, p-hacking, and statistical power.",
    'resampling': "Statistical inference with resampling in Python: p-values for the Euro problem, "
                  "bootstrap estimates of height from BRFSS data, and permutation tests on NSFG data.",
    'pmf_intro': "Histograms and probability mass functions in Python: dice, pregnancy lengths "
                 "of first babies, and word frequencies in Grimm's fairy tales.",
    'text_analysis': "Text analysis in Python with Pride and Prejudice: word frequencies and Zipf's law, "
                     "bigrams and trigrams, and random text from a Markov chain.",
    'tumbleweed': "Solve a 2019 AP Statistics exam problem by simulation in Python: a hypothesis test "
                  "for a difference in proportions with the \"only one test\" framework.",
}

HAS_SOLN = {'effect_size', 'sampling', 'hypothesis'}

DATA_FILES = ['2002FemPreg.dct', '2002FemPreg.dat.gz', 'brfss2016_subset.csv.gz',
              'pg2591.txt', 'pg42671.txt']


def atx_headings(source):
    """Converts setext headings to ATX: 'Title\\n=====' -> '# Title', 'Title\\n-----' -> '## Title'."""
    lines = source.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (i + 1 < len(lines) and line.strip() and not line.startswith('#')
                and re.fullmatch(r'=+|-{3,}', lines[i + 1].strip())):
            level = '#' if lines[i + 1].strip()[0] == '=' else '##'
            out.append(f'{level} {line.strip()}')
            i += 2
        else:
            out.append(line)
            i += 1
    return '\n'.join(out)


def fix_heading(line):
    """Fixes the level of one ATX heading line (not the title)."""
    match = re.match(r'(#+) (.*)', line)
    if not match:
        return line
    text = match.group(2).strip()
    if text == 'STOP HERE':
        return '**STOP HERE**'
    if re.fullmatch(r'Part \w+', text):
        return '## Part ' + text.split()[1].capitalize()
    if match.group(1) == '#':
        return '## ' + text
    return line


def prepare(name, description):
    source = f'../{name}_soln.ipynb' if name in HAS_SOLN else f'../{name}.ipynb'
    nb = nbformat.read(source, 4)

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'markdown':
            continue
        lines = atx_headings(cell.source).split('\n')
        if i == 0:
            # the title: the first heading in the first cell, whatever its level
            assert lines[0].startswith('#'), name
            title = lines[0].lstrip('#').strip()
            lines[0] = f'# {title}'
            lines[1:] = [fix_heading(line) for line in lines[1:]]
        else:
            lines = [fix_heading(line) for line in lines]
        cell.source = '\n'.join(lines)

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name}: {title} ({len(description)} characters)')


for name, description in DESCRIPTIONS.items():
    prepare(name, description)

for filename in DATA_FILES:
    shutil.copy(f'../{filename}', filename)
