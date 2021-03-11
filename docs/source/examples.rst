Examples
========

Base App
--------

The Base App is an out-of-box app that can be run.

.. code-block:: python

    # create a wave_app.py file
    from h2o_wave import Q, main, app
    from wacy.apps import BaseApp

    wacy_app = BaseApp()

    @app('/wacy')
    async def serve(q: Q):
        await wacy_app.serve(q)

Run the app:

.. code-block:: bash

    $ wave run wave_app.py

The app will be available on http://localhost:10101/wacy

Customize Meta / Layout
-----------------------

The metadata / layout of the app can be customized using `meta_card`.

Example using a new meta card:

.. code-block:: python

    from h2o_wave import ui
    from wacy.apps import BaseApp

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

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.meta_card.title = 'My custom title'
    wacy_app.meta_card.icon = 'Globe'
    wacy_app.meta_card.layouts = [...]
    ...

**P.S.** You can change the box names of any card but ensure the same names are used in the layout.

Customize Header / Footer
-------------------------

The header and footer can be customized using `header_card` and `footer_card`:

Example using a new header and footer cards:

.. code-block:: python

    from h2o_wave import ui
    from wacy.apps import BaseApp

    new_header_card = ui.header_card(
        box='header',
        title='My custom title',
        subtitle='My custom subtitle',
        icon='Globe',
        icon_color='blue',
        ...
    )

    new_footer_card = ui.footer_card(
        box='header',
        caption='My custom caption',
        ...
    )

    wacy_app = BaseApp(header_card=new_header_card, footer_card=new_footer_card)

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.header_card.title = 'My custom title'
    wacy_app.header_card.subtitle = 'My custom subtitle'
    wacy_app.header_card.icon = 'Globe'
    wacy_app.header_card.icon_color = 'blue'
    ...

    wacy_app.footer_card.caption = 'My custom caption'
    ...

Customize Models
----------------

The models for the app can be downloaded using spaCy and customized using `input_model_card`:

Example of downloading `spaCy models`_:

.. _`spaCy models`: https://spacy.io/models

.. code-block:: bash

    $ python3 -m spacy download en_core_web_sm
    $ python3 -m spacy download en_core_web_md
    $ python3 -m spacy download en_core_web_lg
    $ python3 -m spacy download fr_core_news_md
    $ python3 -m spacy download de_dep_news_trf

Example using a new input model card:

.. code-block:: python

    from wacy.apps import BaseApp
    from wacy.cards import InputModelCard

    new_input_model_card = InputModelCard(
        input_models=['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'fr_core_news_md', 'de_dep_news_trf'],
        input_model='en_core_web_md',
        title='My custom title',
        ...
    )

    wacy_app = BaseApp(input_model_card=new_input_model_card)

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.input_model_card.input_models = ['en_core_web_sm', 'en_core_web_md', 'en_core_web_lg', 'fr_core_news_md', 'de_dep_news_trf']
    wacy_app.input_model_card.title = 'My custom title'
    ...

**P.S.** Make sure to download the required models before using it in the app.

Customize Textbox
-----------------

The textbox for the app can be customized using `input_text_card`:

Example using a new input text card:

.. code-block:: python

    from wacy.apps import BaseApp
    from wacy.cards import InputTextCard

    new_input_text_card = InputTextCard(
        input_text='I want this to be the default text',
        title='My custom title',
        ...
    )

    wacy_app = BaseApp(input_text_card=new_input_text_card)

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.input_text_card.input_text = 'I want this to be the default text'
    wacy_app.input_text_card.title = 'My custom title'
    ...

Customize Entity Visualizer
---------------------------

The entity visualizer for the app can be customized using `entity_setting_card` and `entity_visualizer_card`:

Example using new entity cards:

.. code-block:: python

    from wacy.apps import BaseApp
    from wacy.cards import EntitySettingsCard, EntityVisualizerCard

    new_entity_settings_card = EntitySettingsCard(
        select_ents=['PERSON'],
        title='My custom title',
        ...
    )

    new_entity_visualizer_card = EntityVisualizerCard(
        name='new visualizer card name',
        title='displacy plot',
        ...
    )

    wacy_app = BaseApp(entity_settings_card=new_entity_settings_card, entity_visualizer_card=new_entity_visualizer_card)

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.entity_settings_card.select_ents = ['PERSON']
    wacy_app.entity_settings_card.title = 'My custom title'
    ...

    wacy_app.entity_visualizer_card.name = 'new visualizer card name'
    wacy_app.entity_visualizer_card.title = 'displacy plot'
    ...

Customize Dependency Visualizer
-------------------------------

The dependency visualizer for the app can be customized using `dependency_setting_card` and `dependency_visualizer_card`:

Example using new dependency cards:

.. code-block:: python

    from wacy.apps import BaseApp
    from wacy.cards import DependencySettingsCard, DependencyVisualizerCard

    new_dependency_settings_card = DependencySettingsCard(
        compact=True,
        color='blue',
        title='My custom title',
        ...
    )

    new_dependency_visualizer_card = DependencyVisualizerCard(
        name='new visualizer card name',
        title='displacy plot',
        ...
    )

    wacy_app = BaseApp(dependency_settings_card=new_dependency_settings_card, dependency_visualizer_card=new_dependency_visualizer_card)

Example using the BaseApp:

.. code-block:: python

    from wacy.apps import BaseApp

    wacy_app = BaseApp()
    wacy_app.dependency_settings_card.compact = True
    wacy_app.dependency_settings_card.color = 'blue'
    wacy_app.dependency_settings_card.title = 'My custom title'
    ...

    wacy_app.dependency_visualizer_card.name = 'new visualizer card name'
    wacy_app.dependency_visualizer_card.title = 'displacy plot'
    ...

