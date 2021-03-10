from h2o_wave import ui

INPUT_MODELS = ['en_core_web_sm', 'en_core_web_md']
INPUT_MODEL = 'en_core_web_sm'
INPUT_TITLE = 'Simple, Quick and Interactive'
INPUT_SUBTITLE = 'Select a spaCy model and enter the text to analyze'
INPUT_TEXT = 'Matthew Honnibal and Ines Montani are the founders of Explosion.'

META_CARD = ui.meta_card(
    box='',
    title='WaCy',
    icon='https://raw.githubusercontent.com/thewaverguy/wacy/main/docs/source/_static/logo/logo_light_250_x_250.svg',
    layouts=[
        ui.layout(
            breakpoint='xs',
            zones=[
                ui.zone(name='header'),
                ui.zone(name='main', zones=[
                    ui.zone(name='input_row', zones=[
                        ui.zone(name='input_model'),
                        ui.zone(name='input_text')
                    ]),
                    ui.zone(name='entity_row', direction='row', zones=[
                        ui.zone(name='entity_settings', size='30%'),
                        ui.zone(name='entity_visualizer', size='70%')
                    ]),
                    ui.zone(name='dependency_row', direction='row', zones=[
                        ui.zone(name='dependency_settings', size='30%'),
                        ui.zone(name='dependency_visualizer', size='70%')
                    ]),
                    ui.zone(name='token_attributes')
                ]),
                ui.zone(name='footer')
            ]
        )
    ],
    theme='light'
)

HEADER_CARD = ui.header_card(
    box='header',
    title='WaCy',
    subtitle='Powering spaCy with Wave',
    icon='WavingHand',
    icon_color='mediumseagreen'
)

FOOTER_CARD = ui.footer_card(
    box='footer',
    caption='(c) 2021 👋 <b>TheWaverGuy</b> - <i>Data is bulletproof</i>'
)

TOKEN_ATTRIBUTES = ['idx', 'text', 'lemma_', 'norm_', 'ent_type_', 'ent_iob_', 'pos_', 'tag_', 'dep_', 'is_alpha',
                    'is_ascii', 'is_digit', 'is_lower', 'is_upper', 'is_title', 'is_punct', 'morph']
