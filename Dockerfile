FROM jupyter/scipy-notebook:latest

# launchbot-specific labels
LABEL name.launchbot.io="CompStats"
LABEL workdir.launchbot.io="/usr/workdir"
LABEL description.launchbot.io="CompStats"
LABEL 8888.port.launchbot.io="Jupyter Notebook"

# Set the working directory
WORKDIR /usr/workdir
COPY 2002FemPreg.dct /usr/workdir/2002FemPreg.dct
COPY 2002FemPreg.dat.gz /usr/workdir/2002FemPreg.dat.gz
COPY check_env.py /usr/workdir/check_env.py 
COPY cumulative_snowfall.png /usr/workdir/cumulative_snowfall.png	
COPY effect_size.ipynb /usr/workdir/effect_size.ipynb
COPY effect_size_soln.ipynb /usr/workdir/effect_size_soln.ipynb
COPY effect_size_soln.ipynb /usr/workdir/effect_size_soln.ipynb
COPY first.py /usr/workdir/first.py
COPY hypothesis.ipynb /usr/workdir/hypothesis.ipynb
COPY hypothesis.py /usr/workdir/hypothesis.py
COPY hypothesis_soln.ipynb /usr/workdir/hypothesis_soln.ipynb
COPY lyrics-elvis-presley.txt /usr/workdir/lyrics-elvis-presley.txt
COPY nsfg.py /usr/workdir/nsfg.py
COPY nsfg2.py /usr/workdir/nsfg2.py
COPY pg2591.txt /usr/workdir/pg2591.txt
COPY pmf_intro.ipynb /usr/workdir/pmf_intro.ipynb
COPY sampling.ipynb /usr/workdir/sampling.ipynb
COPY sampling_soln.ipynb /usr/workdir/sampling_soln.ipynb
COPY thinkplot.py /usr/workdir/thinkplot.py
COPY thinkstats2.py /usr/workdir/thinkstats2.py

# Expose the notebook port
EXPOSE 8888

# Start the notebook server
CMD jupyter notebook --no-browser --port 8888 --ip=* --NotebookApp.token='' --NotebookApp.disable_check_xsrf=True

