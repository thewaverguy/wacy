# WaCy
Powering spaCy with Wave.

## Installation

* Download and run the [H2O Wave server](https://github.com/h2oai/wave/releases).

For **Linux**:

```bash
wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-linux-amd64.tar.gz
tar -xvzf wave-0.13.0-linux-amd64.tar.gz
cd wave-0.13.0-linux-amd64
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

* Run WaCy app

```bash
venv/bin/wave run apps.01_base
```

The app will be available on [http://localhost:10101/wacy](http://localhost:10101/wacy)

## License

This project is licensed under the [Apache License 2.0](LICENSE)

## Credits

spaCy: [https://spacy.io/](https://h2oai.github.io/wave/)   
Wave: [https://h2oai.github.io/wave/](https://h2oai.github.io/wave/)

