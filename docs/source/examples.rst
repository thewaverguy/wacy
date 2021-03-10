Examples
========

Base App
--------

Create an app:

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

Customize Header
----------------

Create an app:

.. code-block:: python

    # wave_app.py
    from h2o_wave import Q, main, app
    from wacy.apps import BaseApp

    wacy_app = BaseApp()

    # customize header card
    wacy_app.header_card.title = 'My custom title'
    wacy_app.header_card.subtitle = 'My custom subtitle'
    wacy_app.header_card.icon = 'Globe'
    wacy_app.header_card.icon_color = 'blue'

    @app('/wacy')
    async def serve(q: Q):
        await wacy_app.serve(q)

Run the app:

.. code-block:: bash

    $ venv/bin/wave run wave_app.py

The app will be available on http://localhost:10101/wacy

Customize Footer
----------------

Create an app:

.. code-block:: python

    # wave_app.py
    from h2o_wave import Q, main, app
    from wacy.apps import BaseApp

    wacy_app = BaseApp()

    # customize footer card
    wacy_app.footer_card.caption = 'My custom caption'

    @app('/wacy')
    async def serve(q: Q):
        await wacy_app.serve(q)

Run the app:

.. code-block:: bash

    $ venv/bin/wave run wave_app.py

The app will be available on http://localhost:10101/wacy
