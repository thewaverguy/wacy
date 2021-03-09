# WaCy
Powering spaCy with Wave
<p>
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/wacy?color=yellow">
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/wacy?label=pypi&color=green&logo=pypi">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/wacy?color=orange&logo=python">
  <img src='https://readthedocs.org/projects/wacy/badge/?version=latest' alt='Documentation Status' />
  <img alt="License" src="https://img.shields.io/github/license/vopani/pychesscom?color=blue">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/thewaverguy">
</p>

Building blocks for interactive and customizable [spaCy](http://spacy.io)-powered apps with [Wave](https://h2oai.github.io/wave)

## Index

* [Installation](#Installation)
* [Setup](#Setup)
* [Usage](#Usage)
* [Documentation](#Documentation)
* [License](#License)
* [Credits](#Credits)

## 🚀 Installation

**Python 3.7 or higher is required**

To install stable version from [PyPI](https://pypi.org/project/wacy) (recommended):

```bash
pip install wacy
```

To install development version:

```bash
$ git clone https://github.com/thewaverguy/wacy
$ cd wacy
$ python3 -m pip install -r requirements.txt
```

## 💻 Setup

#### Wave

Download and run the [Wave server](https://github.com/h2oai/wave/releases) (latest version recommended):

On **Linux**:

```bash
wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-linux-amd64.tar.gz
tar -xvzf wave-0.13.0-linux-amd64.tar.gz
cd wave-0.13.0-linux-amd64
./waved
```

On **Mac**:

```bash
wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-darwin-amd64.tar.gz
tar -xvzf wave-0.13.0-darwin-amd64.tar.gz
cd wave-0.13.0-darwin-amd64
./waved
```

You should see the Wave server running:

```bash
#
# ┌─────────────────────────┐
# │  ┌    ┌ ┌──┐ ┌  ┌ ┌──┐  │ H2O Wave
# │  │ ┌──┘ │──│ │  │ └┐    │ 0.13.0 20210306054523
# │  └─┘    ┘  ┘ └──┘  └─┘  │ © 2021 H2O.ai, Inc.
# └─────────────────────────┘
#
```

#### spaCy

Download [spaCy models](https://spacy.io/usage/models)

```bash
venv/bin/python -m spacy download en_core_web_sm
venv/bin/python -m spacy download en_core_web_md
...
```

The above two models are required to run the sample base app.

You can also download more / other models and configure the app accordingly.

## ⌨️ Usage
Create a file for the Wave app:

```python
# wave_app.py
from h2o_wave import Q, main, app
from wacy.apps import BaseApp

wacy_app = BaseApp()

@app('/wacy')
async def serve(q: Q):
    await wacy_app.serve(q)
```

Run the app: `venv/bin/wave run wave_app.py`

The app will be available on [http://localhost:10101/wacy](http://localhost:10101/wacy)

## 📖 Documentation

Documentation: [https://wacy.readthedocs.io](https://wacy.readthedocs.io)

## 📋 License

This project is licensed under the [Apache License 2.0](LICENSE)

## 🙏 Credits

spaCy: [https://spacy.io/](https://h2oai.github.io/wave)   
Wave: [https://h2oai.github.io/wave/](https://h2oai.github.io/wave)
