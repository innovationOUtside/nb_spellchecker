import click
from .nb_spellchecker import pyspelling_reporter

@click.group()
def cli():
	pass


@cli.command()
@click.argument('path', default='typos.txt', type=click.Path(exists=True))
@click.option('--out_csv', '-c', default='typos.csv',  help='CSV report')
@click.option('--out_report', '-r', default=None,  help='Summary report')
@click.option('--typo_report', '-t', default=None,  help='Typos report')
@click.option('--typo_wordlist', '-w', default=None,  help='Typo wordlist')
def reporter(path, out_csv, out_report, typo_report, typo_wordlist):
	"""Pyspelling reporter."""
	click.echo('Using file/directory: {}'.format(path))
	pyspelling_reporter(path, out_csv, out_report, typo_report, typo_wordlist)