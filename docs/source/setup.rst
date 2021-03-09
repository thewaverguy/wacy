Setup
=====

**Wave**

Download and run the `Wave server`_ (latest version recommended):

.. _`Wave server`: https://github.com/h2oai/wave/releases

On **Linux**:

.. code-block:: bash

    $ wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-linux-amd64.tar.gz
    $ tar -xvzf wave-0.13.0-linux-amd64.tar.gz
    $ cd wave-0.13.0-linux-amd64
    $ ./waved

On **Mac**:

.. code-block:: bash

    $ wget https://github.com/h2oai/wave/releases/download/v0.13.0/wave-0.13.0-darwin-amd64.tar.gz
    $ tar -xvzf wave-0.13.0-darwin-amd64.tar.gz
    $ cd wave-0.13.0-darwin-amd64
    $ ./waved

You should see the Wave server running:

.. code-block:: bash

    #
    # ┌─────────────────────────┐
    # │  ┌    ┌ ┌──┐ ┌  ┌ ┌──┐  │ H2O Wave
    # │  │ ┌──┘ │──│ │  │ └┐    │ 0.13.0 20210306054523
    # │  └─┘    ┘  ┘ └──┘  └─┘  │ © 2021 H2O.ai, Inc.
    # └─────────────────────────┘
    #

**spaCy**

Download `spaCy models`_

.. _`spaCy models`: https://spacy.io/usage/models

.. code-block:: bash

    $ venv/bin/python -m spacy download en_core_web_sm
    $ venv/bin/python -m spacy download en_core_web_md
    $ ...

The above two models are required to run the sample base app.

You can also download more / other models and configure the app accordingly.
