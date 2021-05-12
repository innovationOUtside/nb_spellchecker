# nb_spellchecker
Simple tools to try support spell checking of Jupyter notebooks.

The `nb_spellchecker` is a package to explore various spell checking strategies for Jupyter notebooks.

## Installation

```
pip install --upgrade git+https://github.com/innovationOUtside/nb_spellchecker.git
```


## `pyspelling`

Using an extended version of `pyspelling`, installable as `pip install --upgrade git+https://github.com/ouseful-PR/pyspelling.git@th-ipynb`, we can generate reports over notebooks markdown and code cells either together, or separately.

Original `pyspelling` docs here: https://facelessuser.github.io/pyspelling/

The extended version adds notebook parsing as described in [*Spellchecking Jupyter Notebooks with pyspelling*](https://blog.ouseful.info/2021/03/17/spellchecking-jupyter-notebooks-with-pyspelling/).


### Using the `pyspelling` spellchecker

Using the `ipyspell.yml` file in this repo, as well as a (possibly empty) `.wordlist.txt` file, we can then run a command of the form to run spell checks over `content/*/*.ipynb`:

```
pyspelling -c ipyspell.yml > typos.txt
```

You can override the specified path to particular tasks (eg check Markdown cells or Python code cells) with the `-S` switch:

```
pyspelling -c ipyspell.yml -S "quicktest/Part*/*.ipynb" -n Markdown  > typos_md.txt

pyspelling -c ipyspell.yml -S "quicktest/Part*/*.ipynb" -n Python  > typos_py.txt
```

To generate further reports on the `pyspelling` report:

```
# Convert report to CSV
nb_spellchecker reporter

# Specify CSV filename
nb_spellchecker reporter -c csv_typos.csv

# Generate a tabular typo summary over each notebook
nb_spellchecker reporter -r summary_report.txt

# Generate a report summarising typo counts over all notebooks
nb_spellchecker reporter -r summary_report.txt

# Generate an ordered typo wordlist over all notebooks
nb_spellchecker reporter -w typoswordlist.txt 

```

## Finding Repeated Words

A quick way to find repeated words is the following simple `egrep` command:

```
egrep -o  "\b(\w+)\s+\1\b" */.md/*.md
```

TO DO: add this in somehow...
