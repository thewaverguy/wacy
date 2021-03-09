import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read()

with open('README.md', 'r') as f:
    long_description = f.read()

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
        'Source': 'https://github.com/thewaverguy/wacy',
        'Tracker': 'https://github.com/thewaverguy/wacy'
    },
    python_requires='>=3.7',
    install_requires=[
        'h2o_wave>=0.13.0',
        'spacy>=3.0.0'
    ],
    packages=setuptools.find_packages(),
    license='Apache License, Version 2.0',
    platforms='any',
    classifiers=[
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
