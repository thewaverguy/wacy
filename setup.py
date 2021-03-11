import setuptools

version = open('VERSION.txt', 'r').read()

long_description = open('README.md', 'r').read()
long_description = long_description.replace(
    'docs/source/_static',
    'https://raw.githubusercontent.com/thewaverguy/wacy/main/docs/source/_static'
)
long_description = long_description.replace(
    '[Installation](#-installation) • [Setup](#-setup) • [Usage](#%EF%B8%8F-usage) • [Documentation](#-documentation)',
    ''
)
long_description = long_description.replace(
    ' • [License](#-license) • [Credits](#-credits)',
    ''
)

setuptools.setup(
    name='wacy',
    version=version,
    author='TheWaverGuy',
    author_email='thewaverguy@gmail.com',
    description='Powering spaCy with Wave',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thewaverguy/wacy',
    project_urls={
        'Documentation': 'https://wacy.readthedocs.io',
        'Source': 'https://github.com/thewaverguy/wacy',
        'Tracker': 'https://github.com/thewaverguy/wacy/issues'
    },
    python_requires='>=3.6',
    install_requires=[
        'h2o_wave>=0.13.0',
        'spacy>=3.0.0'
    ],
    packages=setuptools.find_packages(),
    license='Apache License, Version 2.0',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'app',
        'h2o_wave',
        'nlp',
        'spacy'
    ]
)
