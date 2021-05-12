from setuptools import setup

setup(
    name="nb_spellchecker",
    packages=['nb_spellchecker'],
    version='0.0.1',
    author="Tony Hirst",
    author_email="tony.hirst@gmail.com",
    description="Simple spellcheck reporter.",
    long_description='''
    Tools to create simple spell check reports for Jupyter notebooks.
    ''',
    long_description_content_type="text/markdown",
    install_requires=[
        'click',
        'pandas'
    ],
    entry_points='''
        [console_scripts]
        nb_spellchecker=nb_spellchecker.cli:cli
    '''

)