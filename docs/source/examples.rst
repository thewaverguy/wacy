Examples
========
Create a file for the Wave app:

.. code-block:: python

    # wave_app.py
    from h2o_wave import Q, main, app
    from wacy.apps import BaseApp

    wacy_app = BaseApp()

    @app('/wacy')
    async def serve(q: Q):
        await wacy_app.serve(q)

Run the app:

.. code-block:: bash

    $ venv/bin/wave run wave_app.py

The app will be available on http://localhost:10101/wacy
