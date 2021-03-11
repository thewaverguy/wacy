Examples
========

Base App
--------

The Base App is an out-of-box app that can be run.

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

Customize Meta / Layout
-----------------------

The metadata / layout of the app can be changed using `meta_card`:

.. code-block:: python

    from h2o_wave import ui
    from wacy.apps import BaseApp

    # option(1): use a new meta card
    new_meta_card = ui.meta_card(
        box='',
        title='My custom title',
        icon='Globe',
        layouts=[
            ...
        ],
        ...
    )
    wacy_app = BaseApp(meta_card=new_meta_card)

    # option (2): customize meta card
    wacy_app = BaseApp()
    wacy_app.meta_card.title = 'My custom title'
    wacy_app.meta_card.icon = 'Globe'
    wacy_app.meta_card.layouts = [...]
    ...

P.S. You can change the box names of any card but ensure the same names are used in the layout.

Customize Header
----------------

The header card attributes can be set using `header_card`:

.. code-block:: python

    # wave_app.py
    from h2o_wave import ui
    from wacy.apps import BaseApp

    # option(1): use a new header card
    new_header_card = ui.header_card(
        box='header',
        title='My custom title',
        subtitle='My custom subtitle',
        icon='Globe',
        icon_color='blue',
        ...
    )
    wacy_app = BaseApp(header_card=new_header_card)

    # option(2): customize header card
    wacy_app.header_card.title = 'My custom title'
    wacy_app.header_card.subtitle = 'My custom subtitle'
    wacy_app.header_card.icon = 'Globe'
    wacy_app.header_card.icon_color = 'blue'
    ...

Customize Footer
----------------

The footer card attributes can be set using `footer_card`:

.. code-block:: python

    # wave_app.py
    from h2o_wave import ui
    from wacy.apps import BaseApp

    # option(1): use a new footer card
    new_footer_card = ui.footer_card(
        box='header',
        caption='My custom caption'
        ...
    )
    wacy_app = BaseApp(footer_card=new_footer_card)

    # option(2): customize footer card
    wacy_app.footer_card.caption = 'My custom caption'
    ...

