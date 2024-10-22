<div align='center'>

<img src='docs/source/_static/logo/logo_horizontal_light_450_x_150.svg'>

Powering spaCy with Wave

[![Python Version](https://img.shields.io/pypi/pyversions/wacy?color=orange&logo=python)](https://pypi.org/project/wacy)
[![PyPI Version](https://img.shields.io/pypi/v/wacy?label=pypi&color=green&logo=pypi)](https://pypi.org/project/wacy)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/wacy?period=total&left_text=downloads&left_color=grey&right_color=yellow&kill_cache=1)](https://pepy.tech/project/wacy)
[![Documentation](https://img.shields.io/readthedocs/wacy/stable?logo=read-the-docs)](https://wacy.readthedocs.io)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?logo=apache)](https://github.com/thewaverguy/wacy/blob/master/LICENSE)
[![GitHub](https://img.shields.io/github/stars/thewaverguy/wacy?color=yellowgreen&logo=github)](https://github.com/thewaverguy/wacy)

Building blocks for interactive and customizable [spaCy](http://spacy.io)-powered apps with [Wave](https://h2oai.github.io/wave)

---

[Installation](#-installation) • [Setup](#-setup) • [Usage](#%EF%B8%8F-usage) • [Documentation](#-documentation) • [License](#-license) • [Credits](#-credits)

---

</div>

<img src='docs/source/_static/demo/demo.gif'>

## 🚀 Installation

**Python 3.6+ is required**

To install stable version from [PyPI](https://pypi.org/project/wacy) (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install wacy
```

To install development version:

```bash
git clone https://github.com/thewaverguy/wacy
cd wacy
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
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
python3 -m spacy download en_core_web_sm
python3 -m spacy download en_core_web_md
...
```

The above two models are required to run the sample base app.

You can also download more / other models and configure the app accordingly.

## 🛠️ Usage
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

Run the app: `wave run wave_app.py`

The app will be available on [http://localhost:10101/wacy](http://localhost:10101/wacy)

## 📖 Documentation

Documentation: [https://wacy.readthedocs.io](https://wacy.readthedocs.io)   
Examples: [https://wacy.readthedocs.io/en/latest/examples.html](https://wacy.readthedocs.io/en/latest/examples.html)

## 📋 License

This project is licensed under the [Apache License 2.0](LICENSE)

## 🙏 Credits

spaCy: [https://spacy.io/](https://h2oai.github.io/wave)   
Wave: [https://h2oai.github.io/wave/](https://h2oai.github.io/wave)
