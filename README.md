# WaCy
Powering spaCy with Wave.
<p>
  <img alt="License" src="https://img.shields.io/github/license/vopani/pychesscom?color=blue">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/wacy?color=orange">
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/wacy?label=pypi&color=green">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/wacy?color=yellow">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/thewaverguy">
</p>

## Index

* [Installation](#Installation)
* [Usage](#Usage)
* [License](#License)
* [Credits](#Credits)

## Installation

* Download and run the [H2O Wave server](https://github.com/h2oai/wave/releases).

For **Linux**:

```bash
wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-linux-amd64.tar.gz
tar -xvzf wave-0.13.0-linux-amd64.tar.gz
cd wave-0.13.0-linux-amd64
./waved
```

For **Mac**:

```bash
wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-darwin-amd64.tar.gz
tar -xvzf wave-0.13.0-darwin-amd64.tar.gz
cd wave-0.13.0-darwin-amd64
./waved
```

You should see an output like:

```bash
#
# ┌─────────────────────────┐
# │  ┌    ┌ ┌──┐ ┌  ┌ ┌──┐  │ H2O Wave
# │  │ ┌──┘ │──│ │  │ └┐    │ 0.13.0 20210306054523
# │  └─┘    ┘  ┘ └──┘  └─┘  │ © 2021 H2O.ai, Inc.
# └─────────────────────────┘
#
```

* Install the WaCy package

From **PyPI**:

```bash
pip install wacy
```

From **GitHub**:

```bash
git clone https://github.com/thewaverguy/wacy.git
cd wacy
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

* Download spaCy models

```bash
venv/bin/python -m spacy download en_core_web_sm
venv/bin/python -m spacy download en_core_web_md
```

## Usage
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

## License

This project is licensed under the [Apache License 2.0](LICENSE)

## Credits

spaCy: [https://spacy.io/](https://h2oai.github.io/wave/)   
Wave: [https://h2oai.github.io/wave/](https://h2oai.github.io/wave/)
